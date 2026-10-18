---
id: PP-REVIEW-CODE-DATASERVICE
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# GetSeek.DataService source catalogue

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.DataService.csproj:1](code-dataservice.md#src-427c7b6ef4e6). Dependencies: <code>GetSeek.Application</code>, <code>GetSeek.Infrastructure</code>, <code>GetSeek.Contracts</code>.

## DataServiceComposition.cs {#src-a71687a05d71}

<code>Software/src/GetSeek.DataService/DataServiceComposition.cs</code> · 94 lines.

SHA-256: <code>6d54b232004d379aade3bc521d254c82eeccedb8197f3c9390d04c7700d30298</code>.

Declarations: <code>DataServiceComposition</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9e0b107ee8f0"></span><code>DataServiceComposition.InitializeWorkspacesAsync(CancellationToken)</code><br>20–47 | Exists @22; RejectReparsePoints @24; Exists @29; ConfigureAwait @30; CreateWriteConnectionAsync @30; GetDatabaseFactory @30; InitializeDisposableDemoWorkspaceAsync @32; CreateCommand @35; ToInt64 @37; ExecuteScalarAsync @37; Equals @38; GetWorkspaceEnvironmentAsync @38; MigrateAsync @41 | InvalidOperationException @23; InvalidOperationException @39; InvalidOperationException @45 |
| <span id="m-1402433b23bf"></span><code>DataServiceComposition.RejectReparsePoints(string)</code><br>49–54 | GetFullPath @51; GetDirectoryName @51; GetAttributes @52 | InvalidOperationException @53 |
| <span id="m-7710bf5e0497"></span><code>DataServiceComposition.CreateUnlockValidator(WorkspaceKind)</code><br>56–61 | GetDatabaseFactory @58; GetResult @60; GetAwaiter @60; CreateWriteConnectionAsync @60 | No extracted literal effects. |
| <span id="m-b0005918915a"></span><code>DataServiceComposition.GetDatabaseFactory(WorkspaceKind)</code><br>63–68 | nameof @67 | No extracted literal effects. |
| <span id="m-04510183e75e"></span><code>DataServiceComposition.CreateFactory(string)</code><br>83–93 | ToString @92 | No extracted literal effects. |

</details>

## DataServiceRequestRouter.cs {#src-46b520696446}

<code>Software/src/GetSeek.DataService/DataServiceRequestRouter.cs</code> · 203 lines.

SHA-256: <code>c8e425288562a1503d996cc59457afe1ea70a6f4c9b7f26266fd766e899018e8</code>.

Declarations: <code>DataServiceRequestRouter</code> (line 16).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-564a24ceb515"></span><code>DataServiceRequestRouter.RouteAsync(ServiceRequestEnvelope,CancellationToken)</code><br>20–185 | ThrowIfNull @22; Validate @23; ThrowIfCancellationRequested @24; Success @29; GetName @29; ToString @29; ConfigureAwait @33; CreateReadConnectionAsync @33; GetDatabaseFactory @33; CreateCommand @34; ExecuteReaderAsync @36; ReadAsync @37; GetInt64 @38; GetInt32 @38; CreateAsync @43; BeginTransactionAsync @44; NewGuid @46; ToString @47; HandleAsync @48; RollbackAsync @51; Failure @52; AppendAsync @54; ToString @54; GetSanitizedAuditPayload @56; CommitAsync @57; Run @63; GetUnlockCandidates @64; CreateUnlockValidator @64; ToArray @66; Select @66; AuthorizeAsync @76; AuthorizationFailure @78; Initialize @81; GetPagedInventoryItemsAsync @83; Select @92; GetPagedThirdPartiesAsync @121; AuthenticateSelectedUser @146; Clamp @152; Issue @157; TryResolve @162; Revoke @164 | FROM schema_version @35; FROM users @35 |
| <span id="m-17d13e9ab938"></span><code>DataServiceRequestRouter.Success(Guid,ServiceResponseBody)</code><br>187–188 | — | No extracted literal effects. |
| <span id="m-2fef113a3f27"></span><code>DataServiceRequestRouter.Failure(Guid,string,string,ServiceResponseBody?)</code><br>190–191 | ToString @191; NewGuid @191 | No extracted literal effects. |
| <span id="m-3fa6e4239679"></span><code>DataServiceRequestRouter.AuthorizationFailure(Guid,ServiceSessionAuthorization)</code><br>193–202 | Failure @201 | No extracted literal effects. |

</details>

## Program.cs {#src-da6d805c7b59}

<code>Software/src/GetSeek.DataService/Program.cs</code> · 155 lines.

SHA-256: <code>66b572e135cb3291e6c5a988de4d21084a7b4e5d951e610bdad03de7a03b16a6</code>.

Declarations: <code>Program</code> (line 8), <code>WindowsServiceDispatcher</code> (line 45), <code>ServiceTableEntry</code> (line 127), <code>ServiceStatus</code> (line 134).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a9ab6d6f02fc"></span><code>Program.Main(string[])</code><br>10–42 | Contains @12; NewGuid @15; WriteRequestAsync @17; ReadRequestAsync @19; IsWindows @25; SendAsync @30; FromSeconds @30; WriteLine @35; Run @41 | No extracted literal effects. |
| <span id="m-38ca941f7f17"></span><code>WindowsServiceDispatcher.Run()</code><br>65–73 | StartServiceCtrlDispatcher @72; GetLastWin32Error @72 | No extracted literal effects. |
| <span id="m-aa104639f735"></span><code>WindowsServiceDispatcher.ServiceMain(uint,IntPtr)</code><br>75–119 | RegisterServiceCtrlHandlerEx @77; SetServiceStatus @80; Load @84; GetCurrent @85; Equals @86; GetResult @88; GetAwaiter @88; InitializeWorkspacesAsync @88; RunAsync @95 | InvalidOperationException @87 |
| <span id="m-b53aee06e0ac"></span><code>WindowsServiceDispatcher.HandleControl(uint,uint,IntPtr,IntPtr)</code><br>121–125 | Cancel @123 | No extracted literal effects. |
| <span id="m-0f4dfa398974"></span><code>WindowsServiceDispatcher.StartServiceCtrlDispatcher(ServiceTableEntry[])</code><br>149–150 | — | No extracted literal effects. |
| <span id="m-427aaa100add"></span><code>WindowsServiceDispatcher.RegisterServiceCtrlHandlerEx(string,HandlerCallback,IntPtr)</code><br>151–152 | — | No extracted literal effects. |
| <span id="m-c99fa1b7f185"></span><code>WindowsServiceDispatcher.SetServiceStatus(IntPtr,ServiceStatus)</code><br>153–154 | — | No extracted literal effects. |

</details>

## ServiceInstallationConfiguration.cs {#src-7d770a39124c}

<code>Software/src/GetSeek.DataService/ServiceInstallationConfiguration.cs</code> · 26 lines.

SHA-256: <code>446dfbd8bc73b21e8262d34795254e10659e270c9c2c41c2b52cce8c114db2f3</code>.

Declarations: <code>ServiceInstallationConfiguration</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-365371317e8e"></span><code>ServiceInstallationConfiguration.Load()</code><br>11–25 | OpenSubKey @14; GetValue @16; StartsWith @18; StartsWith @19; TryParse @20 | InvalidOperationException @21 |

</details>

## ServicePipeSecurity.cs {#src-d0afe0dc7e7d}

<code>Software/src/GetSeek.DataService/ServicePipeSecurity.cs</code> · 108 lines.

SHA-256: <code>d76a22bde95aba7d1745e12d17d1a5d82667b45c6bad6d39ef8196ab4a05ad49</code>.

Declarations: <code>ServicePipeSecurity</code> (line 12), <code>SecurityAttributes</code> (line 90).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-1be8cd8001fc"></span><code>ServicePipeSecurity.CreateServer(string,string,string?)</code><br>22–67 | IsWindows @24; ThrowIfNullOrWhiteSpace @25; BuildSecurity @28; GetSecurityDescriptorBinaryForm @30; Alloc @31; SizeOf(SecurityAttributes) @36; AddrOfPinnedObject @37; CreateNamedPipe @41; GetLastWin32Error @47; Dispose @48; Free @65 | PlatformNotSupportedException @24; Win32Exception @49; rethrow @60 |
| <span id="m-7d8e24364a34"></span><code>ServicePipeSecurity.GetAccessControlSddl(string,string?)</code><br>69–71 | GetSecurityDescriptorSddlForm @71; BuildSecurity @71 | No extracted literal effects. |
| <span id="m-1ebc9c138fee"></span><code>ServicePipeSecurity.BuildSecurity(string,string?)</code><br>73–88 | ThrowIfNullOrWhiteSpace @76; SetAccessRuleProtection @78; AddAccessRule @79; IsNullOrWhiteSpace @85 | No extracted literal effects. |
| <span id="m-312be96c6124"></span><code>ServicePipeSecurity.CreateNamedPipe(string,uint,uint,uint,uint,uint,uint,SecurityAttributes)</code><br>98–107 | — | No extracted literal effects. |

</details>

## ServicePipeServer.cs {#src-45554bb7953d}

<code>Software/src/GetSeek.DataService/ServicePipeServer.cs</code> · 104 lines.

SHA-256: <code>f7b41191153f29acc0a96c8ddf4b00a00f8f598fdda4004df42b24f25ff0d417</code>.

Declarations: <code>ServicePipeServer</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9c29cf025ea9"></span><code>ServicePipeServer.RunAsync(CancellationToken)</code><br>30–87 | IsWindows @32; CreateServer @36; ConfigureAwait @39; WaitForConnectionAsync @39; CreateLinkedTokenSource @40; CancelAfter @41; ReadRequestAsync @42; _route @46; Failure @50; WriteResponseAsync @60 | PlatformNotSupportedException @32 |
| <span id="m-970741ba8d05"></span><code>ServicePipeServer.RouteBootstrapRequestAsync(ServiceRequestEnvelope,CancellationToken)</code><br>89–100 | ThrowIfCancellationRequested @93; FromResult @95; GetName @96; ToString @96; Failure @99 | No extracted literal effects. |
| <span id="m-8d525fe2137d"></span><code>ServicePipeServer.Failure(Guid,string,string)</code><br>102–103 | ToString @103; NewGuid @103 | No extracted literal effects. |

</details>

## ServiceSessionAuthority.cs {#src-ae1b85b43194}

<code>Software/src/GetSeek.DataService/ServiceSessionAuthority.cs</code> · 75 lines.

SHA-256: <code>ca7499ecc2ae8abd66e1015897c291f90ac20aa283c2d40101e1ad4bbd7b532b</code>.

Declarations: <code>ServiceSessionAuthority</code> (line 9), <code>SessionRecord</code> (line 72), <code>ServiceSessionIdentity</code> (line 75).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9ae6a069f150"></span><code>ServiceSessionAuthority.Issue(Guid,WorkspaceKind)</code><br>23–33 | nameof @25; PruneExpired @28; Replace @29; TrimEnd @29; ToBase64String @29; GetBytes @29; Add @30; GetUtcNow @30; HashToken @31 | ArgumentException @25; ArgumentOutOfRangeException @26 |
| <span id="m-b66c73df5db2"></span><code>ServiceSessionAuthority.TryResolve(string?,WorkspaceKind,ServiceSessionIdentity)</code><br>35–49 | TryGetValue @39; HashToken @39; GetUtcNow @40; TryRemove @42 | No extracted literal effects. |
| <span id="m-9ac560e08f46"></span><code>ServiceSessionAuthority.Revoke(string?)</code><br>51–51 | TryRemove @51; HashToken @51 | No extracted literal effects. |
| <span id="m-a685929776f8"></span><code>ServiceSessionAuthority.RevokeUser(Guid)</code><br>53–62 | TryRemove @59 | No extracted literal effects. |
| <span id="m-14395648ad4a"></span><code>ServiceSessionAuthority.PruneExpired()</code><br>64–69 | GetUtcNow @66; TryRemove @68 | No extracted literal effects. |
| <span id="m-9b7cb6eded65"></span><code>ServiceSessionAuthority.HashToken(string)</code><br>71–71 | ToHexString @71; HashData @71; GetBytes @71 | No extracted literal effects. |

</details>

## ServiceSessionAuthorizer.cs {#src-60aab4245a1d}

<code>Software/src/GetSeek.DataService/ServiceSessionAuthorizer.cs</code> · 82 lines.

SHA-256: <code>96963fef86295085d354b835fe858cc55976ab5a38b07c4409148849f6dfbb00</code>.

Declarations: <code>ServiceSessionAuthorization</code> (line 7), <code>ServiceSessionAuthorizer</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-da61d3173b53"></span><code>ServiceSessionAuthorizer.AuthorizeAsync(string?,WorkspaceKind,string?,CancellationToken)</code><br>18–42 | TryResolve @24; ConfigureAwait @29; CreateReadConnectionAsync @29; GetDatabaseFactory @29; AuthorizeOnConnectionAsync @31 | rethrow @35 |
| <span id="m-fd30ea980623"></span><code>ServiceSessionAuthorizer.AuthorizeAsync(DbConnection,string?,WorkspaceKind,string?,CancellationToken)</code><br>44–55 | ThrowIfNull @51; TryResolve @52; ConfigureAwait @54; AuthorizeOnConnectionAsync @54 | No extracted literal effects. |
| <span id="m-e3e95ca05dff"></span><code>ServiceSessionAuthorizer.AuthorizeOnConnectionAsync(DbConnection,ServiceSessionIdentity,string?,CancellationToken)</code><br>57–81 | ConfigureAwait @63; ResolveEffectivePermissionsAsync @63; RevokeUser @67; IsNullOrWhiteSpace @71; Contains @73; Contains @74; Contains @75; ToArray @80 | No extracted literal effects. |

</details>

## AXAML, migrations and project inputs

### GetSeek.DataService.csproj {#src-427c7b6ef4e6}

<code>Software/src/GetSeek.DataService/GetSeek.DataService.csproj</code> · 13 lines · SHA-256 <code>bb2cc78b25ec0ba99c2640d4d5199e40c6c7af5a296f2759d5f1abbde589657c</code>.
