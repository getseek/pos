---
id: PP-REVIEW-RUNTIME
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# Runtime and integration map

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

## Executable and library dependencies

These arrows come from `ProjectReference` entries. They show compile-time project dependencies, not a runtime request sequence.

```mermaid
flowchart TD
    p0["GetSeek.Application"]
    p1["GetSeek.Contracts"]
    p2["GetSeek.DataService"]
    p3["GetSeek.Desktop"]
    p4["GetSeek.Domain"]
    p5["GetSeek.Infrastructure"]
    p6["GetSeek.Recovery"]
    p7["GetSeek.UI.Components"]
    p0 -->|"references"| p4
    p2 -->|"references"| p0
    p2 -->|"references"| p5
    p2 -->|"references"| p1
    p3 -->|"references"| p7
    p3 -->|"references"| p1
    p3 -->|"references"| p5
    p3 -->|"references"| p0
    p3 -->|"references"| p4
    p5 -->|"references"| p0
    p5 -->|"references"| p4
    p6 -->|"references"| p5
    p6 -->|"references"| p0
    p6 -->|"references"| p4
```

## Runtime ownership and connection points

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
| Desktop storage/bootstrap | [PosBootstrapper.cs:1](code-desktop.md#src-d26211d90637) — local composition inspected; no workspace opened |
| Separate service storage | [DataServiceComposition.cs:1](code-dataservice.md#src-a71687a05d71) — fixed service paths inspected; no service started |
| Supported/blocked service routes | [DataServiceRequestRouter.cs:1](code-dataservice.md#src-46b520696446) — router switch includes explicit not-ready fallback |
| Physical queue processing | [OutputDeviceWorker.cs:1](code-infrastructure.md#src-64d2e3097e9f) — spool acceptance is distinct from physical confirmation |
| Recovery executable | [Program.cs:1](code-recovery.md#src-84079254141c) — template output only; no recovery workflow implemented |

The [workspace map](workspaces.md), [service map](service.md), [migration map](migrations.md) and [output map](output.md) expand these boundaries.
