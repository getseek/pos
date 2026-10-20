---
id: PP-REVIEW-DECISIONS
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# Review findings and change choices

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

These review records track P1 architectural/hardware boundaries and P2 source-observed findings. On 20 October 2026, the four code-fixable P2 items (`PP-REV-001`, `PP-REV-002`, `PP-REV-003`, and `PP-REV-006`) were implemented and covered by fresh automated tests, while the four P1 boundaries (`PP-REV-004`, `PP-REV-005`, `PP-REV-007`, and `PP-REV-008`) remain explicit review gates.

Choose one option per finding to assemble a step-by-step review draft. Choices stay in this browser's local storage and can be exported. They do not submit approval, edit application files, run commands or publish anything. All options and checks remain readable without JavaScript.

<div class="review-toolbar"><button type="button" data-review-export>Export choices</button><button type="button" data-review-clear>Clear saved choices</button><span role="status" aria-live="polite" data-review-status></span></div>

## PP-REV-001 {#pp-rev-001}

### Contradictory workspace flags select Demo implicitly

**P2 · source-observed behavior · RESOLVED (2026-10-20 · option reject).** Resolved in source and verified by 11 parameterized unit test cases (E-020).

WorkspaceLaunchSelector.Select now parses --real-workspace, --demo-workspace, --demo, and GETSEEK_POS_DEMO before window bootstrap. Any combination of two or more explicit CLI workspace flags returns WorkspaceLaunchMode.ConflictingFlags, logs WORKSPACE_FLAG_CONFLICT, presents the startup error screen, and opens no database or worker.

Evidence: [WorkspaceLaunchSelector.cs:21](code-desktop.md#src-7282538860ec), [App.axaml.cs:42](code-desktop.md#src-de5bb454765b), [ReviewDecisionsResolutionUnitTests.cs:25](tests.md#src-3c43bbc15abd). [Workflow map](workspaces.md).

<section class="review-choice" data-review-id="PP-REV-001" data-review-title="Contradictory workspace flags select Demo implicitly">
<label for="choice-PP-REV-001">Review choice for PP-REV-001</label>
<select id="choice-PP-REV-001" data-review-select><option value="">Choose an option…</option><option value="reject">Reject contradictory workspace flags (recommended)</option><option value="precedence">Keep and document Demo precedence</option><option value="selector">Replace flags with one workspace option</option></select>
</section>

<div class="review-option" data-review-finding="PP-REV-001" data-review-option="reject" markdown>

#### Reject contradictory workspace flags (recommended)

Adds an explicit startup error for ambiguous scripts.

1. Add a single workspace argument parser before creating the window.
2. Reject conflicting explicit workspace selectors; preserve each valid selector.
3. Use the parsed workspace for title, logging, bootstrap and worker selection.

Acceptance checks:

- Table-driven tests for all flag combinations and GETSEEK_POS_DEMO precedence.
- Verify invalid flags open no database and start no worker.

</div>

<div class="review-option" data-review-finding="PP-REV-001" data-review-option="precedence" markdown>

#### Keep and document Demo precedence

Small change; conflicting launch scripts remain ambiguous.

1. Document the existing precedence in launcher configuration.
2. Add regression tests for the precedence and window identity.

Acceptance checks:

- Verify the chosen database, title and worker state for each combination.

</div>

<div class="review-option" data-review-finding="PP-REV-001" data-review-option="selector" markdown>

#### Replace flags with one workspace option

Clear long-term interface; needs launcher compatibility work.

1. Introduce --workspace real|demo|preview.
2. Provide a deprecation path for existing flags.
3. Update launchers and documented examples together.

Acceptance checks:

- Compatibility tests and an explicit invalid-value error.

</div>

Rollback consideration: Revert the parser/launcher changes together; do not migrate or reset any workspace.

## PP-REV-002 {#pp-rev-002}

### Pre-transaction pipeline failures use a different error path

**P2 · source-observed contract gap · RESOLVED (2026-10-20 · option boundary).** Resolved in source and verified by injected preflight fault/cancellation unit tests (E-020).

CommandPipeline.ExecuteAsync wraps all post-gate preflight operations (permission resolution, module license check, clock-tamper check, canonical hash serialization, optimistic idempotency check, and BeginTransactionAsync) inside the unified cancellation/exception boundary. Rollback is invoked only when tx is not null, and the execution gate is always released in finally.

Evidence: [CommandPipeline.cs:60](code-application.md#src-b29270acda74), [CommandPipeline.cs:156](code-application.md#src-b29270acda74), [CommandPipeline.cs:230](code-application.md#src-b29270acda74), [ReviewDecisionsResolutionUnitTests.cs:58](tests.md#src-3c43bbc15abd). [Workflow map](checkout.md).

<section class="review-choice" data-review-id="PP-REV-002" data-review-title="Pre-transaction pipeline failures use a different error path">
<label for="choice-PP-REV-002">Review choice for PP-REV-002</label>
<select id="choice-PP-REV-002" data-review-select><option value="">Choose an option…</option><option value="boundary">Normalize failures at the pipeline boundary (recommended)</option><option value="caller">Keep exception ownership in every caller</option><option value="typed">Introduce typed preflight failures</option></select>
</section>

<div class="review-option" data-review-finding="PP-REV-002" data-review-option="boundary" markdown>

#### Normalize failures at the pipeline boundary (recommended)

Makes callers consistent; transaction state must remain precise.

1. Define an outer cancellation/exception boundary for all asynchronous preflight work.
2. Track whether a transaction began; roll back only an active transaction.
3. Keep one sanitized diagnostic ID and preserve finally-based gate release.

Acceptance checks:

- Inject resolver, license, clock, idempotency-read and transaction-start failures.
- Assert no duplicate command execution, correct cancellation result, released gate and no leaked transaction.

</div>

<div class="review-option" data-review-finding="PP-REV-002" data-review-option="caller" markdown>

#### Keep exception ownership in every caller

Avoids pipeline restructuring; every consumer must honor the same contract.

1. Document which failures may throw.
2. Audit each UI/service caller and centralize safe error reporting.
3. Add consumer contract tests.

Acceptance checks:

- Failure injection for each distinct consumer and user-visible safe message.

</div>

<div class="review-option" data-review-finding="PP-REV-002" data-review-option="typed" markdown>

#### Introduce typed preflight failures

More explicit diagnostics; larger API change.

1. Define preflight failure categories and stable safe codes.
2. Adapt ports and pipeline to convert known operational failures.
3. Retain a final boundary for unexpected failures.

Acceptance checks:

- Cancellation, storage-busy, storage-unavailable and unexpected-exception cases.

</div>

Rollback consideration: Revert the error-boundary/API change; preserve existing transaction and idempotency semantics.

## PP-REV-003 {#pp-rev-003}

### Worker-level failures can repeat without a diagnostic

**P2 · source-observed observability gap · RESOLVED (2026-10-20 · option log).** Resolved in source and verified by worker cycle deduplication unit test (E-020).

OutputDeviceWorker accepts an optional cycleErrorLogger callback (wired in App.axaml.cs to PosBootstrapper.LogDiagnosticError) and deduplicates contiguous pre-claim cycle exceptions by exception type and message signature, resetting the signature after any healthy cycle.

Evidence: [OutputDeviceWorker.cs:11](code-infrastructure.md#src-64d2e3097e9f), [OutputDeviceWorker.cs:43](code-infrastructure.md#src-64d2e3097e9f), [OutputDeviceWorker.cs:65](code-infrastructure.md#src-64d2e3097e9f), [App.axaml.cs:102](code-desktop.md#src-de5bb454765b), [ReviewDecisionsResolutionUnitTests.cs:185](tests.md#src-3c43bbc15abd). [Workflow map](output.md).

<section class="review-choice" data-review-id="PP-REV-003" data-review-title="Worker-level failures can repeat without a diagnostic">
<label for="choice-PP-REV-003">Review choice for PP-REV-003</label>
<select id="choice-PP-REV-003" data-review-select><option value="">Choose an option…</option><option value="log">Add bounded worker diagnostics (recommended)</option><option value="health">Add durable worker health and backoff</option><option value="supervise">Stop the loop and let a supervisor restart it</option></select>
</section>

<div class="review-option" data-review-finding="PP-REV-003" data-review-option="log" markdown>

#### Add bounded worker diagnostics (recommended)

Preserves recovery; needs deduplication to avoid flooding.

1. Inject a sanitized worker diagnostic sink.
2. Report pre-claim failures with a stable context and deduplicate repeated errors.
3. Record recovery and expose worker health without automatically retrying drawer output.

Acceptance checks:

- Inject connection/settings/transition failures and assert a bounded diagnostic plus recovery.
- Assert no extra claim, print or drawer pulse is caused by logging.

</div>

<div class="review-option" data-review-finding="PP-REV-003" data-review-option="health" markdown>

#### Add durable worker health and backoff

Better operator visibility; adds persistence and lifecycle complexity.

1. Define healthy/degraded/recovering worker states.
2. Persist the last safe error reference and bounded retry timing.
3. Expose an operator view and recovery probe.

Acceptance checks:

- State-transition tests, restart recovery and no secret payloads in health records.

</div>

<div class="review-option" data-review-finding="PP-REV-003" data-review-option="supervise" markdown>

#### Stop the loop and let a supervisor restart it

Central supervision; restart policy must respect uncertain physical outcomes.

1. Define fatal versus transient worker errors.
2. Report fatal errors to the owner process.
3. Use bounded restarts and preserve startup outcome-unknown recovery.

Acceptance checks:

- Restart loop limits and receipt/drawer uncertainty recovery tests.

</div>

Rollback consideration: Disable the new health/logging integration while retaining existing uncertain-output handling.

## PP-REV-004 {#pp-rev-004}

### DataService contracts do not establish Desktop cutover

**P1 review gate · implementation boundary / incomplete endpoints · OPEN.** Not installed, started or exercised during this review.

Desktop bootstrap composes direct LocalAppData SQLite access. DataService separately owns ProgramData workspaces. The router implements selected setup, authentication and read operations, while other typed contracts return SERVICE_ENDPOINT_NOT_READY. A full service-owned checkout/import/export path must not be presented as complete.

Evidence: [PosBootstrapper.cs:140](code-desktop.md#src-d26211d90637), [DataServiceComposition.cs:74](code-dataservice.md#src-a71687a05d71), [DataServiceRequestRouter.cs:166](code-dataservice.md#src-46b520696446). [Workflow map](service.md).

<section class="review-choice" data-review-id="PP-REV-004" data-review-title="DataService contracts do not establish Desktop cutover">
<label for="choice-PP-REV-004">Review choice for PP-REV-004</label>
<select id="choice-PP-REV-004" data-review-select><option value="">Choose an option…</option><option value="boundary">Keep the current boundary explicit (recommended now)</option><option value="migrate">Plan an incremental service cutover</option><option value="defer">Defer service distribution</option></select>
</section>

<div class="review-option" data-review-finding="PP-REV-004" data-review-option="boundary" markdown>

#### Keep the current boundary explicit (recommended now)

Documentation correction only; service cutover remains future work.

1. Document Desktop and service stores as separate runtime profiles.
2. List implemented routes and unavailable contracts.
3. Require an ownership and migration decision before claiming a cutover.

Acceptance checks:

- Review launch/configuration evidence and a route capability matrix.

</div>

<div class="review-option" data-review-finding="PP-REV-004" data-review-option="migrate" markdown>

#### Plan an incremental service cutover

Larger engineering program requiring isolated fixtures and migration controls.

1. Select one vertical workflow and define data ownership.
2. Implement live session/permission checks, transaction/audit/idempotency and projections.
3. Cut over only after migration, failure and rollback rehearsals.

Acceptance checks:

- End-to-end isolated fixture tests, stale token/permission revocation, disconnect/retry and migration rollback.

</div>

<div class="review-option" data-review-finding="PP-REV-004" data-review-option="defer" markdown>

#### Defer service distribution

Simpler deployment surface; explicitly limits the service capability.

1. Mark unsupported contracts unavailable in all product-facing material.
2. Keep direct Desktop operations as the documented supported profile pending owner confirmation.

Acceptance checks:

- Packaging review ensures no promise of completed service-owned operations.

</div>

Rollback consideration: For a future cutover, restore the prior application profile only under an approved data migration/backup plan; documentation changes alone move no data.

## PP-REV-005 {#pp-rev-005}

### Physical output remains a separate acceptance gate

**P1 review gate · verification gap / operator decision · OPEN.** No printer, drawer, paper, DPI or multilingual hardware checks performed.

The worker records SpoolAccepted, OutcomeUnknown and NeedsOperatorReview. Spool acceptance does not prove a physical receipt or correct drawer action. The source has dedicated thermal confirmation commands; do not replace physical verification with a successful queue submission.

Evidence: [OutputDeviceWorker.cs:16](code-infrastructure.md#src-64d2e3097e9f), [OutputDeviceCommands.cs:1](code-application.md#src-bbf9d29f8bdc). [Workflow map](output.md).

<section class="review-choice" data-review-id="PP-REV-005" data-review-title="Physical output remains a separate acceptance gate">
<label for="choice-PP-REV-005">Review choice for PP-REV-005</label>
<select id="choice-PP-REV-005" data-review-select><option value="">Choose an option…</option><option value="matrix">Run an isolated physical acceptance matrix (recommended)</option><option value="limited">Support only profiles with existing physical evidence</option><option value="disabled">Keep output disabled in evaluation environments</option></select>
</section>

<div class="review-option" data-review-finding="PP-REV-005" data-review-option="matrix" markdown>

#### Run an isolated physical acceptance matrix (recommended)

Requires operator time and test hardware.

1. Prepare synthetic receipts and a test printer/drawer profile.
2. Test Thai/Myanmar glyphs, geometry, missing/offline device, cancellation and restart uncertainty.
3. Record model, driver, paper, DPI, observations and diagnostic references.

Acceptance checks:

- Physical samples and operator sign-off for each supported profile; no automatic uncertain drawer replay.

</div>

<div class="review-option" data-review-finding="PP-REV-005" data-review-option="limited" markdown>

#### Support only profiles with existing physical evidence

Restricts advertised hardware until evidence exists.

1. Inventory actual approved hardware evidence.
2. Limit support claims to reviewed profiles.
3. Mark all other profiles unverified in configuration guidance.

Acceptance checks:

- Every claimed profile links to dated physical evidence.

</div>

<div class="review-option" data-review-finding="PP-REV-005" data-review-option="disabled" markdown>

#### Keep output disabled in evaluation environments

Avoids unintended physical action; does not validate production printing.

1. Use a synthetic workspace and disabled output profile.
2. Review queued state changes without dispatching a device.

Acceptance checks:

- Confirm no worker physical output and retain the outstanding hardware gate.

</div>

Rollback consideration: Restore the previous reviewed output profile; retain job history and inspect uncertain output before reprinting.

## PP-REV-006 {#pp-rev-006}

### Historical passing tests omit excluded files

**P2 · verification gap · RESOLVED (2026-10-20 · option audit).** Audited excluded files; active single-register bootstrapper tests restored and executed (7 passed in E-021).

The three Compile Remove entries in GetSeek.IntegrationTests.csproj target retired pre-migration-068 multi-terminal identity transfer APIs (TransferTerminalIdentityAsync / TerminalId). The active single-register production bootstrapper assertions (clean startup, persisted catalog/decimals, safe error masking, currency/precision validation, and restart durability) are compiled and verified in SingleRegisterProductionBootstrapperTests.cs.

Evidence: [GetSeek.IntegrationTests.csproj:11](tests.md#src-ae399739da40), [SingleRegisterProductionBootstrapperTests.cs:10](tests.md#src-89b12d125dc4). [Workflow map](checkout.md).

<section class="review-choice" data-review-id="PP-REV-006" data-review-title="Historical passing tests omit excluded files">
<label for="choice-PP-REV-006">Review choice for PP-REV-006</label>
<select id="choice-PP-REV-006" data-review-select><option value="">Choose an option…</option><option value="audit">Review exclusions and design focused probes (recommended)</option><option value="restore">Repair and restore excluded tests</option><option value="retain">Retain exclusions with explicit coverage debt</option></select>
</section>

<div class="review-option" data-review-finding="PP-REV-006" data-review-option="audit" markdown>

#### Review exclusions and design focused probes (recommended)

Requires a later authorized application test workspace.

1. Read the exclusion reasons and map each omitted scenario to current behavior.
2. Choose focused replacement or repaired tests.
3. Run in a separate disposable test checkout with synthetic databases.

Acceptance checks:

- Report included/excluded tests separately and attach fresh test evidence.

</div>

<div class="review-option" data-review-finding="PP-REV-006" data-review-option="restore" markdown>

#### Repair and restore excluded tests

Potentially stronger regression coverage; effort depends on obsolete fixtures.

1. Update obsolete setup and expected contracts.
2. Remove exclusions only after the scenarios are valid.
3. Run focused and appropriate broader checks in isolation.

Acceptance checks:

- Compilation includes the files and meaningful assertions pass.

</div>

<div class="review-option" data-review-finding="PP-REV-006" data-review-option="retain" markdown>

#### Retain exclusions with explicit coverage debt

Lowest immediate effort; leaves known evidence gaps.

1. Record the owner, rationale and replacement verification for each excluded file.
2. Keep historical totals clearly dated.

Acceptance checks:

- No feature acceptance claim relies solely on the historical total.

</div>

Rollback consideration: Revert test-only changes in their future isolated checkout; leave production data untouched.

## PP-REV-007 {#pp-rev-007}

### Recovery executable is a placeholder

**P1 review gate · source-observed incomplete implementation · OPEN.** The entire two-line Program.cs was inspected; executable was not run.

GetSeek.Recovery/Program.cs contains only the template Hello, World output. The project does not implement a recovery workflow. Its presence must not be treated as backup, repair, restore or privileged service-recovery capability.

Evidence: [Program.cs:1](code-recovery.md#src-84079254141c). [Workflow map](service.md).

<section class="review-choice" data-review-id="PP-REV-007" data-review-title="Recovery executable is a placeholder">
<label for="choice-PP-REV-007">Review choice for PP-REV-007</label>
<select id="choice-PP-REV-007" data-review-select><option value="">Choose an option…</option><option value="exclude">Exclude recovery capability from support claims (recommended now)</option><option value="design">Design a separate recovery implementation</option><option value="remove">Plan removal from distributed packaging</option></select>
</section>

<div class="review-option" data-review-finding="PP-REV-007" data-review-option="exclude" markdown>

#### Exclude recovery capability from support claims (recommended now)

Accurate present boundary; an operational recovery procedure still needs separate evidence.

1. Mark the executable as a placeholder in technical and packaging documentation.
2. Identify the actual supported backup/restore procedure and evidence, if one exists.
3. Exclude the placeholder from any promised recovery acceptance.

Acceptance checks:

- No release or support document presents the template as working recovery.

</div>

<div class="review-option" data-review-finding="PP-REV-007" data-review-option="design" markdown>

#### Design a separate recovery implementation

Substantial engineering and operational validation.

1. Define data ownership, operator identity, offline/online restrictions and backup format.
2. Design dry-run, integrity checks, safe restoration and rollback.
3. Implement only in an isolated application checkout with synthetic recovery fixtures.

Acceptance checks:

- Interrupted restore, invalid backup, wrong workspace and permissions tests; documented recovery rehearsal.

</div>

<div class="review-option" data-review-finding="PP-REV-007" data-review-option="remove" markdown>

#### Plan removal from distributed packaging

Simplifies the package; requires checking references and installer expectations.

1. Inventory installer and tool references.
2. Remove the placeholder from a future application distribution.
3. Update support instructions.

Acceptance checks:

- Packaging validation and no broken tool references.

</div>

Rollback consideration: Documentation-only classification moves no data. Future packaging or recovery changes require their own rollback and restore rehearsal.

## PP-REV-008 {#pp-rev-008}

### Kitchen ticket producers have no bundled worker claim route

**P1 review gate · source-observed connection gap · OPEN.** Producer and worker claim SQL inspected; no order, printer or external consumer exercised.

SendOrderToKitchenCommand records SentToKitchen and enqueues KitchenTicket. Cancellation can enqueue KitchenTicketCancel. OutputDeviceWorker.ClaimAsync selects only ReceiptPrint, DrawerKick and ShelfLabelPrint. The source search found no other kitchen-ticket consumer under Software/src. Queueing a kitchen ticket therefore does not establish a bundled kitchen-print route. The current Cafe UI uses pay-now Counter Service; backend/legacy order handlers must be documented separately.

Evidence: [RestaurantOrderCommandHandler.cs:194](code-application.md#src-b930bdf2056c), [RestaurantOrderCommandHandler.cs:280](code-application.md#src-b930bdf2056c), [OutputDeviceWorker.cs:254](code-infrastructure.md#src-64d2e3097e9f), [MainViewModel.cs:7997](code-desktop.md#src-16497b924a99), [SqliteProductionReaders.cs:77](code-infrastructure.md#src-212da8ad4eb4). [Workflow map](orders.md).

<section class="review-choice" data-review-id="PP-REV-008" data-review-title="Kitchen ticket producers have no bundled worker claim route">
<label for="choice-PP-REV-008">Review choice for PP-REV-008</label>
<select id="choice-PP-REV-008" data-review-select><option value="">Choose an option…</option><option value="scope">Document the queue-only/legacy boundary (recommended now)</option><option value="consumer">Plan and implement a kitchen-output consumer</option><option value="disable">Disable unsupported kitchen actions in future packaging</option></select>
</section>

<div class="review-option" data-review-finding="PP-REV-008" data-review-option="scope" markdown>

#### Document the queue-only/legacy boundary (recommended now)

Documentation correction; does not implement kitchen output.

1. Describe current Cafe counter checkout separately from backend order handlers.
2. Label KitchenTicket and cancellation jobs as lacking a bundled consumer.
3. Verify any separately deployed consumer before making kitchen-output claims.

Acceptance checks:

- No guide equates SentToKitchen or queued jobs with a physical kitchen print.

</div>

<div class="review-option" data-review-finding="PP-REV-008" data-review-option="consumer" markdown>

#### Plan and implement a kitchen-output consumer

Requires application engineering, device policy and physical acceptance.

1. Define ticket/cancellation payload versions and printer routing.
2. Implement durable claim, snapshot validation, diagnostics and uncertain-output recovery.
3. Test using synthetic orders and a dedicated test printer; connect UI only after acceptance.

Acceptance checks:

- Queue-to-spool and physical output, duplicate send, cancellation, offline device and restart tests.

</div>

<div class="review-option" data-review-finding="PP-REV-008" data-review-option="disable" markdown>

#### Disable unsupported kitchen actions in future packaging

Reduces misleading UI/API surface; legacy unpaid orders still need a safe resolution path.

1. Inventory reachable kitchen actions and legacy order handling.
2. Design a capability gate with a clear unavailable message.
3. Preserve audited legacy-order resolution and data history.

Acceptance checks:

- No new unsupported kitchen action is offered; legacy data can still be inspected and resolved.

</div>

Rollback consideration: Documentation-only scope changes move no data. A future consumer rollback must preserve job history and treat interrupted output as uncertain.

Browser selections are drafts. To authorize later engineering work, share the exported choices or state the finding ID and chosen option. Source fixes and application testing remain separate work in an authorized isolated application checkout.
