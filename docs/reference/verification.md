---
id: PP-REF-002
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-004", "E-005", "E-007", "E-008", "E-009", "E-012", "E-013", "E-014"]
features: []
---

# Verification and limits

<div class="meta">DRAFT · source review 18 October 2026 · documentation foundation D02</div>

Documentation maturity and application verification are separate. This foundation is a source/evidence inventory, not a new release acceptance certificate.

| Evidence type | What it establishes | What it does not establish |
| --- | --- | --- |
| Located | An implementation entry point exists. | That it is reachable, complete or correct. |
| Source-inspected | Selected code/configuration was read and hashed. | A successful runtime journey. |
| Reported | An existing document makes a claim. | Independent verification of that claim. |
| Historical automated | A saved result has been inspected with its original timestamp. | A new test run or acceptance of later source. |
| Fresh automated | A check ran against a specific input in this stage. | Manual UX or physical hardware success. |
| Manual / hardware | A recorded human/device check occurred. | Coverage outside its documented scenario. |

## Historical application tests

The three saved final TRX files from **15 October 2026** were parsed during D01:

| Assembly | Passed | Failed | Not executed |
| --- | ---: | ---: | ---: |
| Unit | 251 | 0 | 0 |
| Integration | 976 | 0 | 0 |
| Acceptance | 1 | 0 | 0 |
| **Total** | **1,228** | **0** | **0** |

Evidence IDs: E-012–E-014. The integration project still excludes `DesktopProductionBootstrapperTests.cs`, `TerminalTransferCrashRecoveryTest.cs`, and `TerminalTransferProcessCrashTest.cs` from compilation (E-009). A passing executed suite does not cover those excluded files.

The large master document retains older 1,203/open-audit wording, while the repair audit reports A01–A12 resolved. Parsing the final TRX resolves the historical count; it does not independently repeat every repair probe. No application build or test suite was rerun for D00–D02.

## Current known limits

- Physical printers/cutters/drawers, touch gestures and native display scaling were not checked in this stage.
- Clean-machine application installation, stopped-writer data transfer, reset journeys and service IPC cutover were not executed.
- Bundled Thai/Myanmar fonts are declared in source, but application/physical-print rendering still requires scenario-specific evidence.
- Historical screenshots show synthetic legacy Demo UI. They are not proof of today's controls or business outcomes.
- Complete user and technical manuals remain later documentation work.

The [feature evidence table](feature-status.md) records limits per workflow; the [document register](document-register.md) records the maturity of each page.
