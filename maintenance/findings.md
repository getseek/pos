# Current documentation findings

Reviewed 2026-10-20. This is Premium's single active findings register; historical application audits remain evidence inputs.

| ID | Finding | Status and disposition | Evidence |
| --- | --- | --- | --- |
| PP-DOC-001 | Master document retains 1,203/open-audit language while a repair audit reports 1,228 passing tests. | Reconciled for historical count only: parsed final TRX files total 1,228. A01–A12 repair acceptance remains a dated claim until focused behavior review. | E-007, E-008, E-012–014 |
| PP-DOC-002 | Older text says Thai/Myanmar fonts are not confirmed bundled. | Source contradiction resolved: UI project declares bundled TTFs; Infrastructure copies print fonts. Physical rendering remains unverified. | E-004, E-005 |
| PP-DOC-003 | Desktop and DataService storage can be confused. | Source paths separated in orientation; service installation does not demonstrate desktop cutover. Runtime integration remains unverified. | E-001, E-003 |
| PP-DOC-004 | Main master document mixes current information and extensive historical archive. | Open: migrate selectively; never publish the master wholesale. | E-007; content-inventory.json |
| PP-DOC-005 | Restaurant example selects Caddy while active configuration selects Python. | Comparison recorded; do not copy operational configuration. Premium Caddy GET/HEAD/public-Host compatibility is a D06 gate. | restaurant-comparison.md |
| PP-DOC-006 | Three historical test files are excluded from compilation. | Audited and resolved for single-register startup: the three `Compile Remove` entries target retired pre-migration-068 multi-terminal transfer APIs, while `SingleRegisterProductionBootstrapperTests.cs` compiles and passes (7/7). | E-009, E-021 |
| PP-DOC-007 | No Git remote, public DNS or Premium runtime identity established. | Deferred to later phases; no remote, tunnel, task or public deployment is created in D02. | D00 snapshot; approved plan |
| PP-DOC-008 | Historical screenshots differ from current UI and cannot prove a workflow. | Publish only inspected synthetic Demo captures, visibly dated/limited; inventory remains outside publication. | E-011; future assets registry |

## Source review extension — updated 20 October 2026

`review-decisions.json` is the canonical structured detail for the PP-REV entries below. On 20 October 2026, all four code-fixable P2 findings (`PP-REV-001`, `PP-REV-002`, `PP-REV-003`, and `PP-REV-006`) were resolved in source and verified with fresh automated unit and integration tests (`E-020`, `E-021`). The four P1 items (`PP-REV-004`, `PP-REV-005`, `PP-REV-007`, and `PP-REV-008`) remain explicit architectural/hardware review gates.

| ID | Finding | Classification / status |
| --- | --- | --- |
| PP-REV-001 | Contradictory workspace flags select Demo implicitly | source-observed behavior · RESOLVED (2026-10-20 · option `reject`, `WorkspaceLaunchSelector`, E-020) · P2 |
| PP-REV-002 | Pre-transaction pipeline failures use a different error path | source-observed contract gap · RESOLVED (2026-10-20 · option `boundary`, `CommandPipeline.ExecuteAsync`, E-020) · P2 |
| PP-REV-003 | Worker-level failures can repeat without a diagnostic | source-observed observability gap · RESOLVED (2026-10-20 · option `log`, `OutputDeviceWorker` deduplicated cycle logger, E-020) · P2 |
| PP-REV-004 | DataService contracts do not establish Desktop cutover | implementation boundary / incomplete endpoints · OPEN · P1 review gate |
| PP-REV-005 | Physical output remains a separate acceptance gate | verification gap / operator decision · OPEN · P1 review gate |
| PP-REV-006 | Historical passing tests omit excluded files | verification gap · RESOLVED (2026-10-20 · option `audit`, `SingleRegisterProductionBootstrapperTests.cs`, E-021) · P2 |
| PP-REV-007 | Recovery executable is a placeholder | source-observed incomplete implementation · OPEN · P1 review gate |
| PP-REV-008 | Kitchen ticket producers have no bundled worker claim route | source-observed connection gap · OPEN · P1 review gate |

Source evidence, options, implementation steps, acceptance checks and rollback considerations: `review-decisions.json`. The existing PP-DOC-003 and PP-DOC-006 are expanded by PP-REV-004 and PP-REV-006.

Source-check updates (2026-10-20): `PP-RULE-010` documents exclusive tax (`TaxMode == 2`) for new carts, discounted service-charge tax share, configurable cash rounding tie rules (`even` vs `up`, migration `084_CashRoundingTieRule.sql`), removal of the unused legacy `UomConversionEngine`, and expanded floor-to-increment pricing presets (`1, 5, 10, 50, 100, 500, 1000, 5000, 10000`).

## Import preview lifecycle — 23 October 2026

PP-DOC-009: Successful Desktop inventory and third-party imports previously retained preview backing rows. Patch A clears preview state after success and on cancel/replacement, while preserving records and completed XLSX download requests. E-022 records 30 passing targeted tests; before the fix four new success/reset cases failed and two rejection cases passed. Failed commands retain their preview/error. Failure XLSX reporting remains pending separately. Native dialogs, actual saved downloads, real shop data and physical devices require owner checks. Pricing and import command handlers were not changed.

## Import result reporting — Patch B, 23 October 2026

PP-DOC-010: The missing failure XLSX and missing Download Result recovery identified after PP-DOC-009 are implemented. E-023 records 53 passing targeted current-source tests. Correctable failures retain uncommitted input, while unsafe/uncertain cases are diagnostic-only. Success/known failure clears the finished preview; saved/cancelled/save-error outcomes are distinct from import outcome. Result download never calls Confirm. Owner-run native dialogs, actual saved downloads, real shop and physical-device checks remain unverified. The earlier Patch A note about retaining failed previews describes historical behavior and is superseded by this result workflow.
