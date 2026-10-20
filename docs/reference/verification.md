---
id: PP-REF-002
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-004", "E-005", "E-007", "E-008", "E-009", "E-012", "E-013", "E-014", "E-016", "E-017", "E-018", "E-019", "E-020", "E-021"]
features: []
---

# Verification and limits

<div class="meta">DRAFT · source review 20 October 2026 · documentation foundation D02</div>

Documentation maturity and application verification are separate. This foundation is a source/evidence inventory, not a new release acceptance certificate.

| Evidence type | What it establishes | What it does not establish |
| --- | --- | --- |
| Located | An implementation entry point exists. | That it is reachable, complete or correct. |
| Source-inspected | Selected code/configuration was read and hashed. | A successful runtime journey. |
| Reported | An existing document makes a claim. | Independent verification of that claim. |
| Historical automated | A saved result has been inspected with its original timestamp. | A new test run or acceptance of later source. |
| Fresh automated | A check ran against a specific input in this stage. | Manual UX or physical hardware success. |
| Manual / hardware | A recorded human/device check occurred. | Coverage outside its documented scenario. |

## Fresh automated checks — 20 October 2026

Targeted unit and integration suites were executed on **20 October 2026** and recorded in `maintenance/evidence-register.json`:

| Evidence ID | Assembly / Scope | Passed | Failed | Not executed |
| --- | --- | ---: | ---: | ---: |
| `E-016` | `GetSeek.IntegrationTests` (workbook import commands and readers) | 24 | 0 | 0 |
| `E-017` | `GetSeek.UnitTests` (exclusive tax, service-charge tax share, cash rounding tie rule, pricing presets, localization parity) | 265 | 0 | 0 |
| `E-018` | `GetSeek.IntegrationTests` (migration 084, UOM registry conversions, pricing rules, tax/currency policy, invoice settlement, Z-reports) | 73 | 0 | 0 |
| `E-019` | `GetSeek.IntegrationTests` (commercial, manufacturing, recipes, third parties, and search usage runtime-log guards) | 90 | 0 | 0 |
| `E-020` | `GetSeek.UnitTests` (full unit suite including `PP-REV-001` workspace flag conflict rejection, `PP-REV-002` pipeline preflight normalization, and `PP-REV-003` worker cycle-error deduplication) | 282 | 0 | 0 |
| `E-021` | `GetSeek.IntegrationTests` (`SingleRegisterProductionBootstrapperTests` for `PP-REV-006`) | 7 | 0 | 0 |

## Historical application tests — 15 October 2026

The three saved final TRX files from **15 October 2026** were parsed during D01:

| Assembly | Passed | Failed | Not executed |
| --- | ---: | ---: | ---: |
| Unit | 251 | 0 | 0 |
| Integration | 976 | 0 | 0 |
| Acceptance | 1 | 0 | 0 |
| **Total** | **1,228** | **0** | **0** |

Evidence IDs: E-012–E-014. The integration project retains three `Compile Remove` entries (`DesktopProductionBootstrapperTests.cs`, `TerminalTransferCrashRecoveryTest.cs`, and `TerminalTransferProcessCrashTest.cs`) that target retired pre-migration-068 multi-terminal transfer APIs (E-009), while single-register production bootstrapper coverage compiles and passes in `SingleRegisterProductionBootstrapperTests.cs` (`E-021`, [PP-REV-006](../review/decisions.md#pp-rev-006)).

## Current documentation review

The [code review atlas](../review/index.md) includes a fresh syntax inventory, SQL-only in-memory schema reconstruction across all 84 migration scripts, source-linked workflows and corrected [business rules](../review/source-check.md). The [review findings](../review/decisions.md) record the 20 October 2026 resolution of `PP-REV-001`, `PP-REV-002`, `PP-REV-003`, and `PP-REV-006` alongside the open P1 deployment and hardware review gates.

## Current known limits

- Physical printers/cutters/drawers, touch gestures and native display scaling were not checked in this stage.
- Clean-machine application installation, stopped-writer data transfer, reset journeys and service IPC cutover were not executed.
- Bundled Thai/Myanmar fonts are declared in source, but application/physical-print rendering still requires scenario-specific evidence.
- Historical screenshots show synthetic legacy Demo UI. They are not proof of today's controls or business outcomes.
- Complete user and technical manuals remain later documentation work.

The [feature evidence table](feature-status.md) records limits per workflow; the [document register](document-register.md) records the maturity of each page.
