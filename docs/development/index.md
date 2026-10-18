---
id: PP-DEV-001
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-001", "E-003", "E-004", "E-005", "E-006", "E-009", "E-010", "E-012", "E-013", "E-014"]
features: ["PP-F001", "PP-F021", "PP-F022"]
---

# Application architecture

<div class="meta">DRAFT · source review 18 October 2026 · documentation foundation D02</div>

Premium POS is an existing .NET application. Its architecture must be documented from current source; the Restaurant project's proposed Rust modules are a design reference for documentation organization only.

## Solution map

| Project | Source responsibility |
| --- | --- |
| `GetSeek.Domain` | Business types, money/quantity policies and domain calculations. |
| `GetSeek.Application` | Commands, handlers, queries/read-service boundaries and business workflows. |
| `GetSeek.Infrastructure` | SQLite persistence/migrations, repositories, diagnostics, imports and native/hardware integration. |
| `GetSeek.Contracts` | Shared contracts and service protocol. |
| `GetSeek.UI.Components` | Shared Avalonia controls and bundled font resources. |
| `GetSeek.Desktop` | Application startup, workspace composition, view models and windows. |
| `GetSeek.DataService` | Separate Windows service composition and service-owned workspace paths. |
| `GetSeek.Recovery` | Template placeholder that prints Hello, World; no recovery workflow is implemented ([PP-REV-007](../review/decisions.md#pp-rev-007)). |

The D01 inventory contains 431 application `.cs`, `.axaml` and `.sql` files, 144 test source files, and migration scripts 001–083. An inventory count is not a complete behavior audit.

The [code review atlas](../review/index.md) now expands all eight projects into source-linked method and connection catalogues. [Source-checked rules](../review/source-check.md) correct or constrain current payment, Cafe, attachment and settings claims.

## Storage boundaries

Desktop defaults are user-local Real/Demo databases. DataService defaults are ProgramData Private databases. These paths and the startup selection are source-reviewed; neither proves that every UI command has moved behind service IPC.

Forward migrations, immutable historical financial records, idempotency and authorization checks need source-linked technical references in the complete D04 manual. Do not use the latest migration number as evidence that the associated journey is complete.

## Verification discipline

The [verification page](../reference/verification.md) separates source inspection, saved test evidence, new automated checks, manual journeys and physical devices. The three original final TRX files contain 1,228 passing results from October 15, with three existing compile exclusions. No application build/test was rerun in this documentation stage.

For this website's build and validation commands, see [documentation operations](../operations/index.md).
