"""Deterministic public review views from frozen local registries; no app access."""
import hashlib
import html
import json
from pathlib import Path
import re
import textwrap

ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def anchor(path):return 'src-'+hashlib.sha256(path.encode()).hexdigest()[:12]
def cell(s):return html.escape(str(s)).replace('|','&#124;').replace('\n',' ')
def code(s):return '<code>'+cell(s)+'</code>'
def project_slug(name):return 'code-'+name.lower().replace('getseek.','')
def head(name,title,features=None):
    return f'---\nid: PP-REVIEW-{name.upper()}\nrevision: "1.0"\nstatus: DRAFT\nreviewed_on: "2026-10-20"\nevidence: ["E-015"]\nfeatures: {json.dumps(features or [])}\n---\n\n# {title}\n\n<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>\n\n'
def clean(s):return s.replace('"',"'").replace('<','(').replace('>',')').replace('&','and')
def diagram(nodes,edges):
    result='```mermaid\nflowchart TD\n'
    for n,label in nodes:result+=f'    {n}["{clean(label)}"]\n'
    for a,b,label in edges:result+=f'    {a} -->|"{clean(label)}"| {b}\n'
    return result+'```\n\n'

def render():
    data=load('maintenance/code-review-index.json')
    workflows=load('maintenance/review-workflows.json')['workflows']
    findings=load('maintenance/review-decisions.json')['findings']
    commands={c['name']:c for c in data['commands']}
    app=[f for f in data['files'] if not f['test']]
    sources={f['path']:f for f in data['files']+data['other_files']}
    methods={m['id']:(f,m) for f in app for m in f['methods']}
    same_owner={}
    for f,m in methods.values():same_owner.setdefault((f['project'],m['owner'],m['name']),[]).append((f,m))
    def candidates(f,m):
        found={}
        for c in m['calls']:
            if c['receiver'] in {'<implicit>','this'}:
                for other,callee in same_owner.get((f['project'],m['owner'],c['name']),[]):
                    if callee['id']!=m['id']:found[callee['id']]=(other,callee)
        return list(found.values())
    projects={p['name']:p for p in data['projects']}
    tables=data['schema']['tables'];table_names={t['name'] for t in tables}
    def source(path,line=1,label=None):
        f=sources[path];p=f['project']
        target=(project_slug(p)+'.md#'+anchor(path)) if p in projects else 'tests.md#'+anchor(path)
        return f'[{cell(label or Path(path).name+":"+str(line))}]({target})'
    def refs(rows):return ', '.join(source(r['path'],r.get('line',1)) for r in rows)
    def method_link(f,m):return f'[{cell(m["owner"]+"."+m["signature"])}]({project_slug(f["project"])}.md#{m["id"].lower()})'
    def add(name,title,text,features=None):out['docs/review/'+name+'.md']=head(name,title,features)+text
    out={}
    total_methods=len(methods);testfiles=[f for f in data['files'] if f['test']]
    add('index','Code review atlas',f'''Use this atlas to inspect **{len(app)} application C# files, {total_methods:,} method declarations, {len(commands)} handled command types, {len(tables)} reconstructed tables and {sum(len(t['foreign_keys']) for t in tables)} foreign-key column mappings**. All {len(workflows)} workflow groups have a map. The catalogues include the remaining helper, reader, domain and UI declarations.

**Producer coverage:** 74 handled command types have no explicit construction site in this syntax snapshot. That is a connection-analysis gap, not proof of unreachable code; target-typed construction, factories and runtime dispatch need further analysis. 55 methods contain interpolated SQL requiring manual inspection.

**Scope:** source connections and selected manual control-flow review. Syntax parsing found no C# syntax errors in {len(data['files'])} files, including {len(testfiles)} test files. This does not establish compilation, resolved calls, passing tests or a working business journey. [Read the extraction limits](method.md).

See [source-checked business rules](source-check.md) for corrected checkout, Cafe, attachment, expense, payroll and settings claims.

## Start a review

1. Open the [runtime map](runtime.md), [command pipeline](pipeline.md) and [access/read paths](access.md).
2. Choose a workflow below; follow its command, permission, producer, handler, table and failure references.
3. Inspect [database relationships](schema.md), [error codes](errors.md) and [UI command bindings](bindings.md).
4. Use [findings and change choices](decisions.md) to select a proposal and review its implementation steps and acceptance checks. Choices are a local review draft, not application changes.

## Business and operational maps

| Map | Feature coverage | Handled command types |
| --- | --- | ---: |
'''+''.join(f'| [{w["title"]}]({w["slug"]}.md) | {", ".join(w["features"])} | {len(w["commands"])} |\n' for w in workflows)+'''
## Source catalogues

'''+''.join(f'- [{p["name"]}]({project_slug(p["name"])}.md) — {sum(f["project"]==p["name"] for f in app)} C# files.\n' for p in data['projects'])+'''
Arrows show source-declared routes or the stated review order. They do not imply that every branch executes in one transaction. SQL tables are literal references filtered against the reconstructed schema; dynamic SQL and runtime dispatch remain explicit analysis limits. Physical side effects require separate evidence.
''')
    runtime='''## Executable and library dependencies

These arrows come from `ProjectReference` entries. They show compile-time project dependencies, not a runtime request sequence.

'''
    runtime+=diagram([('p'+str(i),p['name']) for i,p in enumerate(data['projects'])],[(('p'+str(i)),('p'+str(next(j for j,q in enumerate(data['projects']) if q['name']==r))),'references') for i,p in enumerate(data['projects']) for r in p['references'] if r in projects])
    runtime+='''## Runtime ownership and connection points

```mermaid
flowchart TD
    Flags["Desktop arguments / Demo environment selector"] --> App["Avalonia App and MainWindow"]
    App --> Bootstrap["PosBootstrapper"]
    Bootstrap --> Local["Desktop LocalAppData Real or persistent Demo SQLite"]
    Bootstrap --> Migrate["DatabaseMigrator: versioned SQL"]
    Bootstrap --> VM["MainViewModel and partial workflow view models"]
    VM --> Read["Read services and SQLite projections"]
    VM --> Pipeline["CommandPipeline"]
    Pipeline --> Handlers["Application handlers and policy helpers"]
    Handlers --> Local
    Read --> Local
    App --> Worker["Real Shop only: OutputDeviceWorker"]
    Worker --> Local
    Worker --> Spool["Windows printer queue / drawer / label output"]
    Host["Separate Windows DataService host"] --> Pipe["ACL-controlled named pipe / framed Contracts"]
    Pipe --> Router["DataServiceRequestRouter and session authorizer"]
    Router --> ServiceDB["Service-owned ProgramData Real / DisposableDemo SQLite"]
    Router --> NotReady["Unsupported operations: SERVICE_ENDPOINT_NOT_READY"]
    Recovery["GetSeek.Recovery: template placeholder; no recovery route"]
```

Desktop and DataService are distinct source compositions. The diagram does not assert a completed Desktop-to-service cutover. The Recovery project is a template placeholder, with no implemented restore route; see [PP-REV-007](decisions.md#pp-rev-007).

## Boundary review

| Connection | Evidence and limit |
| --- | --- |
'''+''.join(f'| {title} | {refs([next({"path":f["path"],"line":1} for f in app if f["path"].endswith("/"+tail))])} — {limit} |\n' for title,tail,limit in [
('Desktop storage/bootstrap','PosBootstrapper.cs','local composition inspected; no workspace opened'),('Separate service storage','DataServiceComposition.cs','fixed service paths inspected; no service started'),('Supported/blocked service routes','DataServiceRequestRouter.cs','router switch includes explicit not-ready fallback'),('Physical queue processing','OutputDeviceWorker.cs','spool acceptance is distinct from physical confirmation'),('Recovery executable','GetSeek.Recovery/Program.cs','template output only; no recovery workflow implemented')])
    runtime+='\nThe [workspace map](workspaces.md), [service map](service.md), [migration map](migrations.md) and [output map](output.md) expand these boundaries.\n'
    add('runtime','Runtime and integration map',runtime)
    pipeline='''This map follows the inspected `ExecuteAsync` control flow. Both the post-gate preflight block and the in-transaction block share a unified cancellation/exception normalization boundary (`PP-REV-002` option `boundary`), rolling back only when an active transaction was opened.

## Session and preflight

```mermaid
flowchart TD
    A["ExecuteAsync: command and handler"] --> S{"Session unlocked and authenticated?"}
    S -->|no| Deny["SESSION_LOCKED or AUTH_UNAUTHORIZED"]
    S -->|yes| Wait["Wait for per-instance execution gate"]
    Wait -->|cancelled| Cancel["OPERATION_CANCELLED; gate not acquired"]
    Wait -->|acquired| Recheck{"Same active unlocked user?"}
    Recheck -->|no| Deny2["Session/auth failure; release gate"]
    Recheck -->|yes| Key{"Payload and envelope keys agree?"}
    Key -->|no| Conflict["IDEMPOTENCY_CONFLICT; release gate"]
    Key -->|yes or only one supplied| Permission["Resolve every required permission"]
    Permission -->|denied| Unauthorized["AUTH_UNAUTHORIZED; release gate"]
    Permission -->|allowed| License["Required module licensed; clock check valid"]
    License -->|denied| Restricted["LICENSE_EXPIRED or SECURITY_CLOCK_TAMPER; release gate"]
    License -->|allowed| Next["Continue to durable idempotency map"]
    Permission -.->|dependency throws| Boundary["Normalized to OPERATION_CANCELLED or SYSTEM_TRANSACTION_ERROR; finally releases gate"]
    License -.->|dependency throws| Boundary
```

Preflight permission resolution, licensing/clock checks, serialization, optimistic idempotency reads, and `BeginTransactionAsync` are wrapped inside the post-gate cancellation/exception boundary (`PP-REV-002`). If a preflight step fails before a transaction starts, no rollback is attempted and the gate is released in `finally`.

## Durable idempotency and transaction entry

```mermaid
flowchart TD
    Hash["Serialize/hash command; optimistic durable key lookup"] --> Exists{"Existing key?"}
    Exists -->|hash differs| Conflict["IDEMPOTENCY_CONFLICT"]
    Exists -->|same hash and usable result| Cached["CACHED_IDEMPOTENT_RESULT"]
    Exists -->|new key or same hash without usable result| Begin["BeginTransactionAsync: inside outer boundary"]
    Begin -->|throws| Boundary["Normalized to OPERATION_CANCELLED or SYSTEM_TRANSACTION_ERROR; no rollback; release gate"]
    Begin -->|started| Again["Recheck durable key inside transaction"]
    Again -->|already committed| RB["Roll back the new transaction"]
    RB -->|different hash| Conflict
    RB -->|same hash and usable result| Cached
    RB -->|same hash and unavailable result| Missing["IDEMPOTENCY_RESULT_UNAVAILABLE"]
    Again -->|not committed| Live["Recheck every permission under transaction"]
    Live -->|denied| Deny["Rollback; AUTH_UNAUTHORIZED"]
    Live -->|allowed| Handler["Continue to handler and commit map"]
    Hash -.->|throws| Boundary
```

Existing-result deserialization and the under-transaction checks share the outer boundary, with `RollbackAsync` gated on whether `tx is not null`. An unusable optimistic cache entry is not permission to repeat a committed financial action; the durable check inside the writer transaction decides the outcome.

## Handler, audit and commit

```mermaid
flowchart TD
    H["Invoke typed handler using current UnitOfWork transaction"] --> Result{"Handler succeeds?"}
    Result -->|no| Rollback["Rollback and return original handler failure"]
    Result -->|yes| Audit["Append audit: sanitized payload if supported; otherwise serialized payload"]
    Audit --> Save["Save durable idempotency result in the same transaction"]
    Save --> Commit["Commit and return handler result"]
    H -.->|cancellation in inner block| Cancel["Best-effort rollback; OPERATION_CANCELLED"]
    Audit -.->|unexpected exception in inner block| Fault["Best-effort sanitized diagnostic and rollback"]
    Save -.->|unexpected exception| Fault
    Commit -.->|unexpected exception| Fault
    Fault --> System["SYSTEM_TRANSACTION_ERROR plus diagnostic ID"]
    Commit --> Finally["Finally: release the acquired execution gate"]
    Rollback --> Finally
    Cancel --> Finally
    System --> Finally
```

The boundary covers preflight checks, transaction creation, under-transaction rechecks, permission checks, handler execution, audit, idempotency save and commit. Rollback is executed only when a transaction has begun (`tx is not null`). Logging and rollback are best effort; a generated diagnostic ID does not prove that a log was written. A commit exception does not by itself prove that nothing was committed.

The gate is local to a pipeline instance. Durable idempotency and SQLite transaction checks add safeguards; no distributed exactly-once guarantee is made.

## Failure and retry review

| Point | Result / review action |
| --- | --- |
| Locked/changed session, permission or license denial | Correct identity/access/configuration; do not repeatedly resubmit a financial command. |
| Idempotency conflict | Inspect the recorded command key and request hash. A different action needs a different key. |
| Cached success | Display the recorded result; avoid a second physical output action. |
| Handler failure | Transaction rollback is requested; inspect the stable code and its handler context. |
| Unexpected transaction exception | Safe diagnostic reference, best-effort rollback; inspect the recorded outcome before retry. |
| Preflight dependency exception | Normalized at the pipeline boundary (`SYSTEM_TRANSACTION_ERROR` or `OPERATION_CANCELLED`) without rolling back an unstarted transaction (`PP-REV-002`). |
| Commit outcome uncertain to caller | Reconcile by durable key/result rather than assuming failure means no commit. |

## Source

'''
    pipeline+=refs([next({'path':f['path'],'line':27} for f in app if f['path'].endswith('/CommandPipeline.cs'))])+'\n\n[ICommand and permission declarations](access.md) · [Error catalogue](errors.md) · [Physical output](output.md)\n'
    add('pipeline','Command and failure pipeline',pipeline)
    access='''## Read and authentication paths

```mermaid
flowchart TD
    Screen["AXAML view binding"] --> VM["View-model method"]
    VM --> Query["Read service / SQLite projection"]
    Query --> Guard["Reader/session-specific permission and redaction rules"]
    Guard --> DB["SQLite read connection or supplied connection"]
    DB --> Projection["Paged/filter/sort projection"]
    Projection --> UI["UI list, details or export"]
    Login["Selected operator + PIN"] --> Validator["SqliteSessionUnlockValidator"]
    Validator --> Lockout["Credential verification, terminal lockout and clock policy"]
    Lockout --> Session["Desktop session or service-issued workspace token"]
    Session --> Gate["Action-specific live authorization"]
```

Reads do not automatically run through CommandPipeline. Authorization must be inspected in each reader and caller. A visible or disabled UI control alone does not establish server-side permission enforcement.

## Explicit exceptions to the normal write pipeline

| Path | Observed ownership | Review requirement |
| --- | --- | --- |
| First administrator | Desktop view model and service router invoke UserCommandHandler in their own transaction and append a sanitized audit record. The handler rejects setup after users exist. | Review simultaneous first-run requests and rollback; an authenticated normal session cannot be assumed before setup. |
| Workspace reset and Demo seeding | Dedicated infrastructure service and migration/seeding paths. | Separate authorization, workspace classification, transaction and lifecycle review; no reset executed here. |
| Expense photo preparation and reads | Separate image preparation and permission-checked read service; the command handler stores versioned image bytes in SQLite. | Review image validation, authorization, attachment replacement and transactional BLOB writes. See [source-checked rules](source-check.md). |
| Search usage and output worker | Infrastructure-maintained state outside the ordinary business command caller. | Review their explicit lifecycle, permissions and diagnostic paths. |

The source catalogues expose all methods and literal table references so these paths can be inspected without inventing a universal write guarantee.

## Permission constants

| Constant | Permission value | Declaration |
| --- | --- | --- |
'''
    for f in app:
        for c in f['constants']:
            access+=f'| {code(c["name"])} | {code(c["value"])} | {source(f["path"],c["line"])} |\n'
    access+='\nEach workflow lists the command-declared RequiredPermission/AdditionalPermissions/RequiredModule expressions. These are declarations, not a computed role matrix. Permission resolution, overrides and handler-specific checks can add conditions.\n'
    add('access','Access, reads and first-run exceptions',access)
    for w in workflows:
        text=f'Feature coverage: {", ".join(w["features"])}. Source: {refs(w["sources"])}.\n\n'
        text+=(w.get('notes','')+'\n\n' if w.get('notes') else '')
        text+='## Step-by-step review route\n\nThe numbered route is a business review checklist. Branches are separate actions; it does not imply that all actions occur in one transaction.\n\n'+''.join(f'{i}. {s}.\n' for i,s in enumerate(w['steps'],1))+'\n'
        if w['commands']:
            nodes=[('Entry','Choose a typed command'),('Gate','Session, permission, license and transaction gate'),('Good','Inspect result and read projection'),('Bad','Inspect failure and rollback outcome')]
            edges=[('Entry','Gate',str(len(w['commands']))+' command choices below')];handlers={}
            for name in w['commands']:
                h=commands[name]['handler'];handlers.setdefault(h,[]).append(name)
            for i,(h,names) in enumerate(handlers.items()):
                hid='h'+str(i);nodes.append((hid,h));edges.extend([('Gate',hid,str(len(names))+' typed routes'),(hid,'Good','success'),(hid,'Bad','failure')])
            text+='## Command routing map\n\n'+diagram(nodes,edges)
            text+='This overview groups routes by handler to stay readable; each named command and its connections follow below. [Shared gate details](pipeline.md) apply when this handler is invoked through the pipeline. First-run provisioning is an explicit [separate path](access.md). Source construction sites show candidates, not proof of a connected or reachable UI path.\n\n'
            text+='## Commands, options and implementation connections\n\n'
            for name in w['commands']:
                c=commands[name];text+=f'### {name}\n\n'
                text+=f'Handler: {source(c["path"],c["line"],c["handler"])}. Result type: {code(c["result"])}.\n\n'
                for d in c['declarations']:
                    props='; '.join(p['name']+' = '+p['expression'] for p in d['properties'])
                    text+=f'Declaration: {source(d["path"],d["line"])}. '+(code(props) if props else 'No special permission/module property extracted here; inspect defaults, inherited contracts and handler checks.')+'\n\n'
                text+='Construction sites: '+(', '.join(source(p['path'],p['line'],p['method']+':'+str(p['line'])) for p in c['producers']) or '**None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.')+'\n\n'
                for mid in c['methods']:
                    f,m=methods[mid];text+='Handler method: '+method_link(f,m)+'.\n\n'
                    helpers=candidates(f,m)
                    if helpers:text+='Same-owner helper candidates: '+', '.join(method_link(other,callee) for other,callee in helpers)+'. These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.\n\n'
                    reads=sorted({s['table'] for s in m['sql'] if s['operation'] in {'FROM','JOIN'}})
                    writes=sorted({s['table'] for s in m['sql'] if s['operation'] not in {'FROM','JOIN'}})
                    errors=sorted({e['code'] for e in m['errors']})
                    text+='| Direct method syntax | Extracted references |\n| --- | --- |\n'
                    for label,values in [('Reads',reads),('Writes / DDL',writes),('Literal failure codes',errors)]:text+=f'| {label} | '+(', '.join(code(v) for v in values) or 'None extracted directly; inspect helpers and dynamic paths.')+' |\n'
                    text+='\nHelper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.\n\n'
        else:
            text+='## Lifecycle review map\n\n'+diagram([('s'+str(i),step) for i,step in enumerate(w['steps'])],[('s'+str(i),'s'+str(i+1),'review next') for i in range(len(w['steps'])-1)])
            text+='This is a review route across the cited implementation, not a runtime trace captured from an executing application. [Runtime ownership](runtime.md) and the [source catalogues](index.md#source-catalogues) provide the actual composition evidence.\n\n'
        linked=[f for f in findings if f['workflow']==w['slug']]
        if linked:text+='## Open review points\n\n'+''.join(f'- [{f["id"]}: {f["title"]}](decisions.md#{f["id"].lower()}) — {f["kind"]}.\n' for f in linked)+'\n'
        text+='## Verification still required\n\nNo application journey was executed for this map. Use a separate synthetic test environment to verify permission denial, valid success, invalid inputs, state conflicts, cancellation, transaction rollback, retry/idempotency and the resulting projection. Add physical-device checks only where the workflow dispatches output. Preserve original financial history when reviewing corrections or reversals.\n'
        add(w['slug'],w['title'],text,w['features'])
    # All application methods, not a hand-picked subset. Call lists are syntax names.
    for p in data['projects']:
        name=project_slug(p['name']);text='Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.\n\n'
        text+='Project: '+source(p['path'])+'. Dependencies: '+(', '.join(code(r) for r in p['references']) or 'none declared')+'.\n\n'
        for f in sorted([f for f in app if f['project']==p['name']],key=lambda f:f['path']):
            text+=f'## {Path(f["path"]).name} {{#{anchor(f["path"])}}}\n\n{code(f["path"])} · {f["lines"]:,} lines.\n\nSHA-256: {code(f["sha256"])}.\n\n'
            text+='Declarations: '+', '.join(code(t['name']+(' : '+', '.join(t['bases']) if t['bases'] else ''))+' (line '+str(t['line'])+')' for t in f['types'])+'.\n\n'
            if f['methods']:
                text+='<details markdown>\n<summary>Methods, calls, table effects and failures ('+str(len(f['methods']))+')</summary>\n\n'
                text+='| Method and lines | Invocation syntax | Literal SQL / failures / throws |\n| --- | --- | --- |\n'
                for m in f['methods']:
                    calls='; '.join(c['name']+('('+', '.join(c['generic_types'])+')' if c['generic_types'] else '')+' @'+str(c['line']) for c in m['calls'])
                    sql='; '.join(sorted({s['operation']+' '+s['table']+' @'+str(s['line']) for s in m['sql']}))
                    errors='; '.join(e['code']+' @'+str(e['line']) for e in m['errors'])
                    throws='; '.join(t['type']+' @'+str(t['line']) for t in m['throws'])
                    effects=' · '.join(v for v in (sql,errors,throws,'DYNAMIC SQL: inspect manually' if m['dynamic_sql'] else '') if v)
                    text+=f'| <span id="{m["id"].lower()}"></span>{code(m["owner"]+"."+m["signature"])}<br>{m["line"]}–{m["end"]} | {cell(calls) or "—"} | {cell(effects) or "No extracted literal effects."} |\n'
                text+='\n</details>\n\n'
        extra=[f for f in data['other_files'] if f['project']==p['name']]
        if extra:
            text+='## AXAML, migrations and project inputs\n\n'
            for f in extra:text+=f'### {Path(f["path"]).name} {{#{anchor(f["path"])}}}\n\n{code(f["path"])} · {f["lines"]} lines · SHA-256 {code(f["sha256"])}.\n\n'
        add(name,p['name']+' source catalogue',text)
    errors={}
    for f in app:
        for m in f['methods']:
            for e in m['errors']:errors.setdefault(e['code'],[]).append((f,m,e['line']))
    text=f'This catalogue contains **{len(errors)} distinct uppercase literal codes** extracted from `Failure(...)` calls in application method bodies. It is an index of code sites, not a claim that every code is reachable or user-visible. Dynamic/propagated codes, exceptions, worker message prefixes and validation outside method bodies may require separate inspection.\n\n'
    text+='## Triage route\n\n1. Record the safe diagnostic reference, workspace, action and time.\n2. Find the code and matching handler context below.\n3. Inspect transaction/output outcome before repeating financial or device actions.\n4. Correct input, access, state or configuration; escalate unexpected faults with sanitized evidence.\n\n'
    text+='| Code | Source occurrences |\n| --- | --- |\n'
    for error,sites in sorted(errors.items()):text+=f'| {code(error)} | '+', '.join(source(f['path'],line,m['owner']+'.'+m['name']+':'+str(line)) for f,m,line in sites)+' |\n'
    add('errors','Error code catalogue',text)
    text=f'**{len(data["bindings"])} literal AXAML Command bindings** were located. This is a binding inventory, not a runtime binding-resolution pass. Compiled bindings, data templates, inherited data contexts, code-behind events and ReactiveCommand creation must be reviewed together.\n\n| Binding expression | View location |\n| --- | --- |\n'
    for b in data['bindings']:text+=f'| {code(b["binding"])} | {source(b["path"],b["line"])} |\n'
    add('bindings','UI command bindings',text)
    text=f'The extractor parsed **{len(testfiles)} C# test source files**. Attribute counts below are syntax counts, not executed test totals. Parameterized cases, exclusions and compilation determine actual execution. See [verification and limits](../reference/verification.md) for both the 15 October 2026 historical baseline and the 20 October 2026 targeted automated test runs.\n\nThe integration project excludes three retired multi-terminal transfer files while compiling `SingleRegisterProductionBootstrapperTests.cs` for single-register startup; see [PP-REV-006](decisions.md#pp-rev-006).\n\n'
    for f in testfiles+[f for f in data['other_files'] if f['project'] not in projects]:
        text+=f'## {Path(f["path"]).name} {{#{anchor(f["path"])}}}\n\n{code(f["path"])} · SHA-256 {code(f["sha256"])}.\n\n'
        tests=[m for m in f.get('methods',[]) if any(a.split('.')[-1] in {'Fact','Theory','Test','TestCase'} for a in m['attributes'])]
        if tests:text+='Located test declarations: '+', '.join(code(m['name'])+' @'+str(m['line']) for m in tests)+'.\n\n'
    add('tests','Test source and verification limits',text)
    text='''These review records track P1 architectural/hardware boundaries and P2 source-observed findings. On 20 October 2026, the four code-fixable P2 items (`PP-REV-001`, `PP-REV-002`, `PP-REV-003`, and `PP-REV-006`) were implemented and covered by fresh automated tests, while the four P1 boundaries (`PP-REV-004`, `PP-REV-005`, `PP-REV-007`, and `PP-REV-008`) remain explicit review gates.

Choose one option per finding to assemble a step-by-step review draft. Choices stay in this browser's local storage and can be exported. They do not submit approval, edit application files, run commands or publish anything. All options and checks remain readable without JavaScript.

<div class="review-toolbar"><button type="button" data-review-export>Export choices</button><button type="button" data-review-clear>Clear saved choices</button><span role="status" aria-live="polite" data-review-status></span></div>

'''
    for f in findings:
        status_label=f.get("status","OPEN")
        text+=f'## {f["id"]} {{#{f["id"].lower()}}}\n\n### {f["title"]}\n\n**{f["priority"]} · {f["kind"]} · {status_label}.** {f["runtime_status"]}\n\n{f["observation"]}\n\nEvidence: {refs(f["sources"])}. [Workflow map]({f["workflow"]}.md).\n\n'
        text+=f'<section class="review-choice" data-review-id="{f["id"]}" data-review-title="{html.escape(f["title"],quote=True)}">\n<label for="choice-{f["id"]}">Review choice for {f["id"]}</label>\n<select id="choice-{f["id"]}" data-review-select><option value="">Choose an option…</option>'
        text+=''.join(f'<option value="{o["id"]}">{html.escape(o["title"])}</option>' for o in f['options'])+'</select>\n</section>\n\n'
        for o in f['options']:
            text+=f'<div class="review-option" data-review-finding="{f["id"]}" data-review-option="{o["id"]}" markdown>\n\n#### {o["title"]}\n\n{o["tradeoff"]}\n\n'+''.join(f'{i}. {s}\n' for i,s in enumerate(o['steps'],1))+'\nAcceptance checks:\n\n'+''.join('- '+s+'\n' for s in o['acceptance'])+'\n</div>\n\n'
        text+='Rollback consideration: '+f['rollback']+'\n\n'
    text+='Browser selections are drafts. To authorize later engineering work, share the exported choices or state the finding ID and chosen option. Source fixes and application testing remain separate work in an authorized isolated application checkout.\n'
    add('decisions','Review findings and change choices',text)
    # SQL relationships: one complete catalogue plus bounded per-table local diagrams.
    table_page={t['name']:'schema-'+str(i//12+1).zfill(2)+'.md' for i,t in enumerate(tables)}
    schema_intro=f'''## Reconstruction evidence

All **{len(data['schema']['migrations'])} migration SQL files** were replayed sequentially into an ephemeral **SQLite {data['schema']['sqlite_version']} `:memory:`** connection. This produced **{len(tables)} tables**, **{sum(len(t['columns']) for t in tables)} columns** and **{sum(len(t['foreign_keys']) for t in tables)} foreign-key column mappings**. `PRAGMA foreign_key_check` returned no violations in this synthetic seeded reconstruction.

This does not exercise the .NET migration runner, its transaction behavior, upgrades of shop data, runtime SQLite version or live database integrity. No real application database was opened. The `schema_version` table was created as the runner does, and synthetic version rows were added between scripts. See [migration lifecycle](migrations.md).

## Table index

'''+ ' · '.join(f'[{t["name"]}]({table_page[t["name"]]}#{slug(t["name"])})' for t in tables)+'''

## Relationship notation

Each local diagram shows the table and its declared outgoing foreign keys. The complete column-to-column mapping and delete/update policies follow it. A parent may have many child rows unless unique constraints restrict that relationship; arrows deliberately do not invent cardinality. Relationships enforced only by application logic, JSON payloads or dynamic SQL are not declared foreign keys and are not inferred here. The code catalogues show observed table use.

'''
    add('schema','Database relationships',schema_intro+'\n[Migration inputs](code-infrastructure.md) retain every SQL path and digest.\n',['PP-F022'])
    for i,t in enumerate(tables):
        if i%12==0:text='[Complete table index and reconstruction limits](schema.md). Arrows below are declared foreign keys, not inferred cardinalities.\n\n'
        text+=f'## {t["name"]} {{#{slug(t["name"])}}}\n\n'
        parents=sorted({k['parent'] for k in t['foreign_keys']})
        if parents:
            text+='<details markdown>\n<summary>Relationship diagram</summary>\n\n'+diagram([('T',t['name'])]+[('P'+str(i),parent) for i,parent in enumerate(parents)],[('T','P'+str(i),', '.join(k['from']+' → '+str(k['to'] or 'PK') for k in t['foreign_keys'] if k['parent']==parent)) for i,parent in enumerate(parents)])+'</details>\n\n'
        else:text+='No outgoing foreign key declared in the reconstructed schema.\n\n'
        text+='<details markdown>\n<summary>Columns and foreign-key policies</summary>\n\n| Column | SQLite type | NOT NULL | Primary-key position |\n| --- | --- | --- | --- |\n'
        for c in t['columns']:text+=f'| {code(c["name"])} | {code(c["type"])} | {c["not_null"]} | {c["pk"] or "—"} |\n'
        if t['foreign_keys']:
            text+='\n| FK / sequence | Child column | Parent table / column | On update / delete |\n| --- | --- | --- | --- |\n'
            for k in t['foreign_keys']:text+=f'| {k["id"]} / {k["sequence"]} | {code(k["from"])} | [{k["parent"]}]({table_page[k["parent"]]}#{slug(k["parent"])}) / {code(k["to"] or "implicit PK")} | {k["on_update"]} / {k["on_delete"]} |\n'
        text+='\n</details>\n\n'
        if i%12==11 or i==len(tables)-1:
            number=str(i//12+1).zfill(2);first=tables[(i//12)*12]['name']
            add('schema-'+number,'Schema '+number+': '+first+' to '+t['name'],text,['PP-F022'])
    add('method','Methodology and refresh','''## What was checked

- Every C# file under `Software/src` and `Software/tests`, excluding generated `bin`, `obj` and test-output directories, was parsed using the installed .NET SDK's Roslyn syntax libraries. No application project was compiled or loaded.
- Type bases identify typed handler declarations. Explicit `new CommandType(...)` sites identify potential producers; they do not prove dispatch or reachability. Handler methods are matched by their first parameter type.
- Method-body invocation names, uppercase literal `Failure(...)` codes, throw statements and literal SQL table references were extracted. Repeated invocation syntax names in a method are deduplicated with the first line retained.
- SQL references are filtered to reconstructed table names. Interpolated SQL is flagged for manual review. Aliases, views, triggers, nested helper effects, generated SQL and dynamic dispatch are not semantically resolved.
- AXAML inventory covers literal `Command="{Binding ...}"` attributes. Code-behind events, data-context resolution and runtime binding errors require a separate UI check.
- Project edges come from project-reference declarations. Database edges come from SQLite foreign-key metadata after in-memory SQL replay.
- Startup flags, pipeline boundaries, first-run provisioning, service ownership, error reporting and worker failure handling received selected manual source inspection. Broad cataloguing does not imply every method received a manual correctness audit.

Roslyn syntax trees describe declarations and syntax; semantic models are a separate analysis step. [Microsoft's syntax-analysis documentation](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/get-started/syntax-analysis) explains this distinction.

## Reproduce an explicit source refresh

Ordinary documentation builds use frozen JSON registries and never read the application. Refresh is a deliberate read-only analysis operation from `F:\\Premium_POS_docs`:

```powershell
dotnet restore .\\scripts\\source-indexer\\SourceIndexer.csproj --configfile .\\scripts\\source-indexer\\NuGet.Config
dotnet build .\\scripts\\source-indexer\\SourceIndexer.csproj -c Release --no-restore
dotnet .\\.build\\source-indexer\\bin\\Release\\net10.0\\SourceIndexer.dll F:\\Premium_POS .\\.build\\code-index.raw.json
.\\.venv\\Scripts\\python.exe -B .\\scripts\\refresh_review.py --application-root F:\\Premium_POS --raw-index .\\.build\\code-index.raw.json
```

The analysis helper targets .NET 10 and references SDK-bundled Roslyn assemblies; it has no NuGet package dependency and clears package feeds. Its build outputs live under the documentation `.build` directory. A .NET 10 SDK is required only for source refresh, not normal documentation builds. Python replays migration SQL only into `:memory:` and rejects a documentation root inside the app.

After refresh, review changed hashes and extraction limits, update source-linked workflow/decision records and E-015's digest, then run the standard build, validation and documentation tests. Do not rerun the one-time configuration initializer as a substitute for a source review. Changed source can invalidate manually reviewed conclusions even when syntax still parses.

## Diagram runtime

Mermaid 11.17.2 is vendored from an official npm tarball verified against its SHA-512 integrity. The asset and MIT license are registered by SHA-256; a small theme override loads it before the theme so the floating external CDN loader is not used. Flowcharts retain intrinsic dimensions inside a horizontally scrollable region instead of shrinking long technical labels. [Mermaid usage guidance](https://mermaid.js.org/config/usage.html) describes local hosting and renderer initialization.

## Safety and publication

Only metadata and reviewed diagrams are rendered. Full source, raw syntax output, databases, PINs, tokens, logs and TRX are outside `docs/`. Validation checks all registered source paths/line ranges/digests, command coverage, foreign-key endpoints, decision options, page metadata, navigation, links and assets. A source snapshot is a dated reference, not a runtime import or continuous assertion about the live app.

The website remains a loopback preview on port 18181. The user selected GitHub Pages at getseek/pos after local checks; the prepared workflow publishes only on an explicit manual run after validation. Repository authentication, Pages/domain settings and a successful remote deployment remain separate evidence. Application fixes, application test execution and physical-device acceptance are not performed by the review pages or their choice controls.
''')
    rules=load('maintenance/review-rules.json')['rules']
    checked='The following statements were checked against the cited code after the initial atlas generation. They correct or constrain documentation claims. All are source observations; no application journey or physical device was executed.\n\n'
    for rule in rules:
        checked+=f"## {rule['id']}: {rule['title']}\n\n{rule['statement']}\n\nEvidence: {refs(rule['sources'])}. Verification: **{rule['verification']}**.\n\n"
    checked+='The full [command pipeline](pipeline.md), [expense map](expenses.md), [legacy order boundary](orders.md) and [findings](decisions.md) show the related branches and proposed changes.\n'
    add('source-check','Source-checked business rules',checked)
    return {path:content.rstrip()+"\n" for path,content in out.items()}
