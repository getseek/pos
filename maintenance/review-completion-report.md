# Local code review atlas completion — 18 October 2026

The local Premium POS documentation extension is complete in **F:\Premium_POS_docs**, with preview at **http://127.0.0.1:18181/** and the atlas at **http://127.0.0.1:18181/review/**. The user most recently instructed that local documentation be created and corrected against application code first. No GitHub push, Pages activation, public deployment or DNS change was performed.

The original D00–D02 completion report and approved plan remain dated history. This report records the subsequently authorized diagrams, source review, corrections and review choices. It does not claim completion of every operator manual or runtime acceptance of the application.

## Deliverables and coverage

| Item | Completed local result |
| --- | --- |
| Public Markdown pages | 69 registered pages, each in navigation and the generated search index; 56 new pages under `docs/review/`. |
| Workflow maps | 25 groups covering all 25 feature IDs, including newly inventoried procurement/money accounts, shipping/reservations and batch changes. |
| Command connections | All 172 source-declared handled command types assigned once to workflow maps, with declarations, permission/module expressions, construction sites, handler methods, direct SQL/failure references and same-owner helper candidates. |
| Application syntax inventory | 326 application C# files; 2,132 method declarations across eight projects. |
| Test source inventory | 144 C# test files; source declarations are distinguished from executed test evidence and compile exclusions. |
| C# syntax extraction | 470 files parsed with zero syntax errors. The docs-owned Roslyn helper built with zero warnings/errors; no application project was compiled. |
| Database reconstruction | All 83 SQL migrations replayed into ephemeral Python SQLite 3.49.1 `:memory:`; 137 tables, 1,485 columns and 261 foreign-key column mappings. Synthetic `foreign_key_check` returned no violations. |
| Diagrams | 145 Mermaid diagrams overall, including 25 workflow maps, project/runtime maps, three detailed pipeline maps, access/read map and bounded table relationship diagrams. |
| UI and errors | 315 literal AXAML command bindings; 385 distinct uppercase literal failure codes at 946 extracted source sites. These counts are syntax inventory, not runtime reachability. |
| Corrected business rules | Nine explicit source-linked rules for checkout, deferred invoices, Cafe mode, photos, waste expense payments, advances, settings, inventory loss and kitchen queues. |
| Review decisions | Eight open findings, each with three alternatives, implementation steps, acceptance checks, evidence limits and rollback considerations. Browser choices persist locally and export a draft JSON; they execute no application changes. |
| Diagram dependency | Mermaid 11.17.2 copied from the official npm package after SHA-512 integrity verification; renderer and MIT license registered by SHA-256. A theme override preloads it locally before the theme's external fallback. |

## Files created and changed

The exact 69-page list is in `maintenance/document-register.json` and the generated website document register. New review content includes:

- `docs/review/index.md`, `runtime.md`, `pipeline.md`, `access.md`, `schema.md`, `errors.md`, `bindings.md`, `tests.md`, `decisions.md`, `method.md` and `source-check.md`.
- 25 workflow pages, eight project source catalogues and 12 schema detail pages.
- `maintenance/code-review-index.json`, `review-workflows.json`, `review-decisions.json`, `review-rules.json` and `mermaid-dependency.json` as the frozen source metadata and canonical review configuration. Existing feature/evidence/document/asset records and the single findings register were extended.
- `scripts/source-indexer/Program.cs`, `SourceIndexer.csproj`, `Directory.Build.props` and `NuGet.Config`: an optional offline SDK/Roslyn syntax extractor whose outputs remain under the documentation `.build` directory.
- `scripts/refresh_review.py`, `render_review.py`, `validate_review.py` and `smoke_preview.py`. Normal build/render/validation uses only checked-in local records; source refresh is a separate explicit read-only operation.
- `tests/test_review.py`, additional publication/search/renderer regression checks, and the corrected candidate-build fixture including `overrides/`.
- `overrides/main.html`, `docs/assets/javascripts/diagram-config.js`, `review-choices.js`, `assets/stylesheets/review.css`, and the vendored Mermaid renderer/license.
- Updated navigation, project settings, README, working rules, home, operations, architecture, roles, workspace, daily-workflow, verification, feature/register and release pages. Text formats are pinned to LF for consistent future checkouts and asset digests.
- `.github/workflows/docs.yml` and `deployment/github-pages.md` are prepared local files for the user-selected future `getseek/pos` GitHub Pages deployment. They remain inactive. The original Caddy/Tunnel plan was preserved as history; no Premium Caddy/tunnel runtime was started.

## Source corrections and findings

The initial atlas draft was corrected after manual source tracing:

1. Expense photos use validated, versioned **SQLite BLOB storage** in `expense_attachments.image_data`. The preparation/read service is distinct from transactional command writes. The erroneous filesystem-storage wording was removed.
2. Current Cafe checkout is **pay-now Counter Service**. Saved Table Service is normalized by the profile reader. Backend/legacy order handlers are documented separately.
3. Order handlers produce `KitchenTicket`/`KitchenTicketCancel`, while the bundled worker claim SQL selects receipt, drawer and shelf-label jobs. A physical kitchen route is not represented as complete.
4. The pipeline now shows gate cancellation, permission/license/clock denials, preflight exception escape, unavailable cached results, transaction entry outside the inner catch, rollback, audit, idempotency save and commit uncertainty in separate readable maps.
5. `GetSeek.Recovery` is explicitly a Hello, World template placeholder. Existing architecture wording was corrected.
6. Static QR/bank payment is described as cashier-confirmed; QRIS gateway and unallocated Split Bill are rejected in the inspected checkout code. Deferred invoice eligibility, non-cash waste expense denial and active-Admin settings checks are source-linked.

The eight canonical findings are:

| ID | Review point | Evidence state |
| --- | --- | --- |
| PP-REV-001 | Conflicting Real/Demo flags implicitly select persistent Demo. | Source-observed behavior; no runtime launch performed. |
| PP-REV-002 | Pre-transaction pipeline exceptions use a different error path. | Source-observed contract gap; selected callers have safe catches; no UI crash claimed. |
| PP-REV-003 | Worker loop can suppress pre-claim failures without diagnostics. | Source-observed observability gap; no hardware fault injected. |
| PP-REV-004 | Separate DataService contracts do not establish Desktop cutover. | Inspected implementation boundary and explicit not-ready routes. |
| PP-REV-005 | Physical output remains a separate acceptance gate. | Hardware verification gap. |
| PP-REV-006 | Historical passing tests omit three excluded files. | Historical evidence/coverage gap; no application tests rerun. |
| PP-REV-007 | Recovery executable is a placeholder. | Complete two-line entry point inspected. |
| PP-REV-008 | Kitchen ticket producers lack a bundled worker claim route. | Producer and claim SQL inspected; no device/consumer execution. |

No proposed application fix was implemented. Browser recommendations are review drafts, with no option chosen on behalf of the owner. The synthetic browser test choice was cleared after testing.

## Validation performed

All final checks passed:

- Strict staged Zensical build: **70 HTML pages including 404**, 94 output files, 145 Mermaid blocks.
- Source, metadata, registry, navigation, reviewed assets, output safety, links/anchors, canonical URLs, sitemap, source/output freshness and complete search-index coverage: **12,783 internal references checked**, no errors.
- **31 documentation regression tests passed**, including broken links/anchors, private output, modified assets, failed candidate preservation, invalid search index, local renderer preload order, source-reference drift, command coverage, foreign-key endpoints and preventing source-only rules from claiming runtime acceptance.
- Local HTTP smoke: **all 69 pages, 14 registered assets and search index** returned nonempty HTTP 200 responses: 84 routes, no failures.
- Browser checks: **all 145 diagrams rendered across 45 diagram-bearing/index pages**, no unrendered Mermaid blocks and no captured warning/error logs during the diagram walk.
- Browser search returned corrected kitchen findings/rules and detailed SQLite `image_data` field content from schema pages, including collapsed reference sections.
- Browser chooser: eight controls with three options each; selection highlighting, reload persistence, JSON export and clearing verified. Export JSON contained all eight finding records and explicit draft-only status. No selection remains saved from the test.
- Responsive check at a 390 px viewport: all eight select controls fit the page; temporary viewport override reset afterwards.
- Git whitespace check passed for authored/generated text; the unmodified third-party renderer has a vendor-only whitespace exemption to preserve its verified bytes. Ignored `.build`, virtual environment, raw syntax output, npm archive, logs and application data are not part of the documentation commit.

Ignored local evidence includes `.build/validation.json`, `http-smoke.json`, `build-manifest.json`, `review-source-before.json`, `review-source-after.json` and the review's tool outputs. A sample browser draft export was created at `E:\Downloads\premium-pos-review-choices.json`; it is a test draft, not owner approval.

## Application and infrastructure isolation

All analysis operations read `F:\Premium_POS`; this documentation work did not write application files, run application builds/tests, open shop databases, execute transactions, reset data or operate devices. Every application write command in this task targeted only the separate documentation/scratch directories.

Seven UI/test files changed concurrently relative to the starting source baseline:

- `Software/src/GetSeek.UI.Components/Controls/WorkspaceFilterBar.axaml`
- `Software/src/GetSeek.UI.Components/Controls/WorkspaceSearchBox.axaml`
- `Software/src/GetSeek.UI.Components/Controls/CompactDateField.axaml`
- `Software/src/GetSeek.UI.Components/Themes/Inputs.axaml`
- `Software/src/GetSeek.Desktop/Views/MainWindow.axaml`
- `Software/tests/GetSeek.IntegrationTests/CommercialSearchIntegrationTests.cs`
- `Software/tests/GetSeek.IntegrationTests/CompactDatePopupLayoutTests.cs`

These changes were not reverted. The final frozen review snapshot includes their current versions, and **all 587 recorded C#/AXAML/SQL/project file hashes match the current application tree** at the final comparison. Starting-baseline comparisons normalized PowerShell's uppercase SHA-256 hex before evaluating differences.

Restaurant documentation, configuration, Caddy/cloudflared processes, tasks and ports were not modified. Only the recorded Premium preview process tree was stopped/restarted. Local preview binds `127.0.0.1:18181`; Premium origin/admin/metrics ports remain unused. No Git remote was added and no push was performed. The repository has no persistent author identity; the local commit uses its existing Codex <codex@local.invalid> identity through command-scoped Git options, without changing global settings.

## Limits and remaining work

The atlas is a complete inventory/routing review within its stated syntax scope, with selected manual correctness tracing. It is **not** a semantically bound complete call graph, an exhaustive manual audit, an application release certificate or a finished operator manual.

- 74 handled command types have no explicit producer found by this extractor; target-typed construction, factories, runtime dispatch and reachability require further analysis. 55 methods with interpolated SQL are marked for manual inspection.
- Overload resolution, dependency injection, reflection, constructors/property bodies, conditional compilation variants, runtime binding, dynamic SQL and transitive helper effects require focused follow-up. Same-owner links are explicitly candidate name matches.
- Source fixes should follow selected PP-REV choices in a separately authorized application work area with synthetic fixtures and appropriate tests. None was selected or executed here.
- Complete task-by-task operator guides, current synthetic screenshots, failure-injection journeys, clean-machine installation, data-transfer/reset/service migration acceptance and physical device/font/DPI checks remain separate work.
- GitHub Pages was selected for later hosting at `getseek/pos`, but the latest instruction is local-first. The repository was inspected empty; no noninteractive credential was available. No remote authentication, push, Pages activation, CNAME/DNS/certificate setup or remote workflow run occurred. The prepared workflow validates pushes and permits publication only through an explicit manual publish run after validation.

The local website is ready for the user's documentation and change-option review.
