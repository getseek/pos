using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

if (args.Length != 2) throw new ArgumentException("Expected read-only application root and output JSON path.");
string app = Path.GetFullPath(args[0]);
string output = Path.GetFullPath(args[1]);
if (output.StartsWith(app + Path.DirectorySeparatorChar, StringComparison.OrdinalIgnoreCase))
    throw new InvalidOperationException("Indexer cannot write inside application source.");
string Rel(string path) => Path.GetRelativePath(app,path).Replace('\\','/');
string Hash(string text) => Convert.ToHexStringLower(SHA256.HashData(Encoding.UTF8.GetBytes(text)));
int Line(SyntaxNode node) => node.GetLocation().GetLineSpan().StartLinePosition.Line + 1;
int End(SyntaxNode node) => node.GetLocation().GetLineSpan().EndLinePosition.Line + 1;
string TypeName(SyntaxNode node) => node.Ancestors().OfType<BaseTypeDeclarationSyntax>().FirstOrDefault()?.Identifier.ValueText ?? "<top-level>";
string CallName(InvocationExpressionSyntax node) => node.Expression switch {
    MemberAccessExpressionSyntax m => m.Name.Identifier.ValueText,
    IdentifierNameSyntax i => i.Identifier.ValueText,
    GenericNameSyntax g => g.Identifier.ValueText,
    MemberBindingExpressionSyntax m => m.Name.Identifier.ValueText,
    _ => "<expression>"
};
string ArgName(ExpressionSyntax expression) => expression switch {
    IdentifierNameSyntax i => i.Identifier.ValueText,
    ObjectCreationExpressionSyntax o => "new " + o.Type,
    MemberAccessExpressionSyntax m => m.Name.Identifier.ValueText,
    _ => "<expression>"
};
var sqlRegex = new Regex(@"\b(?<op>INSERT\s+(?:OR\s+\w+\s+)?INTO|DELETE\s+FROM|UPDATE|FROM|JOIN|ALTER\s+TABLE|CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?)\s*[\""`\[]?(?<table>[A-Za-z_][A-Za-z0-9_]*)",RegexOptions.IgnoreCase);
var uppercase = new Regex("^[A-Z][A-Z0-9_]{2,}$");
var allFiles = new List<object>();
int methodCount=0,callCount=0,typeCount=0,syntaxErrorCount=0;
var excluded = new HashSet<string>(StringComparer.OrdinalIgnoreCase){"bin","obj",".build","artifacts","TestResults","test-results"};
foreach (string baseName in new[]{"src","tests"}) {
  string directory=Path.Combine(app,"Software",baseName);
  foreach (string file in Directory.EnumerateFiles(directory,"*.cs",SearchOption.AllDirectories).Order(StringComparer.Ordinal)) {
    if(Path.GetRelativePath(directory,file).Split(Path.DirectorySeparatorChar).Any(excluded.Contains)) continue;
    string text=File.ReadAllText(file);
    var tree=CSharpSyntaxTree.ParseText(text,new CSharpParseOptions(LanguageVersion.Preview),file);
    var root=tree.GetRoot();
    var diagnostics=tree.GetDiagnostics().Where(d=>d.Severity==DiagnosticSeverity.Error).Select(d=>new {code=d.Id,line=d.Location.GetLineSpan().StartLinePosition.Line+1,message=d.GetMessage()}).ToArray();
    syntaxErrorCount+=diagnostics.Length;
    var types=root.DescendantNodes().OfType<BaseTypeDeclarationSyntax>().Select(t=>new {
      name=t.Identifier.ValueText,kind=t.Kind().ToString(),line=Line(t),end=End(t),
      bases=t.BaseList?.Types.Select(b=>b.Type.ToString()).ToArray() ?? [],
      properties=(t is TypeDeclarationSyntax declaredType ? declaredType.Members.OfType<PropertyDeclarationSyntax>() : Enumerable.Empty<PropertyDeclarationSyntax>()).Where(p=>p.Identifier.ValueText is "RequiredPermission" or "AdditionalPermissions" or "RequiredModule" or "CommandKey").Select(p=>new{name=p.Identifier.ValueText,line=Line(p),expression=(p.ExpressionBody?.Expression.ToString() ?? p.AccessorList?.ToString() ?? "").Length>600?"<complex>":p.ExpressionBody?.Expression.ToString() ?? p.AccessorList?.ToString() ?? ""}).ToArray()
    }).ToArray();
    typeCount+=types.Length;
    var methods=new List<object>();
    foreach(var method in root.DescendantNodes().OfType<MethodDeclarationSyntax>()) {
      string signature=method.Identifier.ValueText+"("+string.Join(",",method.ParameterList.Parameters.Select(p=>p.Type?.ToString()))+")";
      string owner=TypeName(method);
      string id="M-"+Hash(Rel(file)+"|"+owner+"|"+signature+"|"+Line(method))[..12];
      var calls=method.DescendantNodes().OfType<InvocationExpressionSyntax>().Select(i=>new {
        name=CallName(i),line=Line(i),receiver=i.Expression is IdentifierNameSyntax or GenericNameSyntax ? "<implicit>" : i.Expression is MemberAccessExpressionSyntax m && Regex.IsMatch(m.Expression.ToString(),@"^[A-Za-z_][\w.?!<>]*$") ? m.Expression.ToString():"<expression>",
        generic_types=i.Expression.DescendantNodesAndSelf().OfType<GenericNameSyntax>().SelectMany(g=>g.TypeArgumentList.Arguments.Select(a=>a.ToString())).ToArray(),
        arguments=i.ArgumentList.Arguments.Take(3).Select(a=>ArgName(a.Expression)).ToArray()
      }).ToArray();
      callCount+=calls.Length;
      var creates=method.DescendantNodes().OfType<ObjectCreationExpressionSyntax>().Select(c=>new{type=c.Type.ToString(),line=Line(c)}).ToArray();
      var variables=method.DescendantNodes().OfType<VariableDeclaratorSyntax>().Where(v=>v.Initializer?.Value is ObjectCreationExpressionSyntax).Select(v=>new{name=v.Identifier.ValueText,type=((ObjectCreationExpressionSyntax)v.Initializer!.Value).Type.ToString(),line=Line(v)}).ToArray();
      var errors=method.DescendantNodes().OfType<InvocationExpressionSyntax>().Where(i=>CallName(i)=="Failure" && i.ArgumentList.Arguments.Count>0).Select(i=>new{
        line=Line(i),code=i.ArgumentList.Arguments[0].Expression is LiteralExpressionSyntax literal && literal.IsKind(SyntaxKind.StringLiteralExpression) ? literal.Token.ValueText : "<dynamic>",
        expression=i.ArgumentList.Arguments[0].Expression is LiteralExpressionSyntax ? "literal" : ArgName(i.ArgumentList.Arguments[0].Expression)
      }).ToArray();
      var sql=method.DescendantNodes().OfType<LiteralExpressionSyntax>().Where(l=>l.IsKind(SyntaxKind.StringLiteralExpression)).SelectMany(l=>sqlRegex.Matches(l.Token.ValueText).Select(m=>new{operation=m.Groups["op"].Value.ToUpperInvariant(),table=m.Groups["table"].Value,line=Line(l)})).ToArray();
      var throws=method.DescendantNodes().OfType<ThrowStatementSyntax>().Select(t=>new{line=Line(t),type=t.Expression is ObjectCreationExpressionSyntax o?o.Type.ToString():"rethrow"}).ToArray();
      var guards=method.DescendantNodes().OfType<IfStatementSyntax>().Where(i=>i.Statement.DescendantNodesAndSelf().Any(n=>n is ReturnStatementSyntax or ThrowStatementSyntax)).Select(i=>new{line=Line(i),condition=i.Condition.ToString().Length<=240?i.Condition.ToString():"<complex condition>"}).ToArray();
      methods.Add(new{id,name=method.Identifier.ValueText,owner,line=Line(method),end=End(method),signature,returns=method.ReturnType.ToString(),parameters=method.ParameterList.Parameters.Select(p=>new{name=p.Identifier.ValueText,type=p.Type?.ToString()??""}).ToArray(),attributes=method.AttributeLists.SelectMany(a=>a.Attributes.Select(b=>b.Name.ToString())).ToArray(),calls,creates,variables,errors,sql,throws,guards,dynamic_sql=method.DescendantNodes().OfType<InterpolatedStringExpressionSyntax>().Any(s=>Regex.IsMatch(s.ToString(),@"\b(SELECT|INSERT|UPDATE|DELETE)\b"))});
    }
    methodCount+=methods.Count;
    var constants=root.DescendantNodes().OfType<FieldDeclarationSyntax>().Where(f=>f.Modifiers.Any(SyntaxKind.ConstKeyword)).SelectMany(f=>f.Declaration.Variables.Where(v=>v.Initializer?.Value is LiteralExpressionSyntax).Select(v=>new{owner=TypeName(f),name=v.Identifier.ValueText,value=((LiteralExpressionSyntax)v.Initializer!.Value).Token.ValueText,line=Line(v)})).Where(v=>v.owner=="Permissions"||uppercase.IsMatch(v.value)).ToArray();
    allFiles.Add(new{path=Rel(file),sha256=Convert.ToHexStringLower(SHA256.HashData(File.ReadAllBytes(file))),project=Path.GetRelativePath(directory,file).Split(Path.DirectorySeparatorChar)[0],test=baseName=="tests",types,methods,constants,syntax_errors=diagnostics});
  }
}
Directory.CreateDirectory(Path.GetDirectoryName(output)!);
File.WriteAllText(output,JsonSerializer.Serialize(new{schema_version=1,extractor="Roslyn syntax; no semantic binding or runtime execution",reviewed_on="2026-10-18",files=allFiles},new JsonSerializerOptions{WriteIndented=false}),new UTF8Encoding(false));
Console.WriteLine(JsonSerializer.Serialize(new{files=allFiles.Count,types=typeCount,methods=methodCount,calls=callCount,syntax_errors=syntaxErrorCount,output}));
