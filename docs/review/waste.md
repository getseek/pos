---
id: PP-REVIEW-WASTE
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: ["PP-F010"]
---

# Inventory loss and waste

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

Feature coverage: PP-F010. Source: [InventoryLossCommandHandler.cs:1](code-application.md#src-ad1ac7eca868).

## Step-by-step review route

The numbered route is a business review checklist. Branches are separate actions; it does not imply that all actions occur in one transaction.

1. Select lost stock, quantity and reason.
2. Validate tracking and cost snapshot.
3. Submit authorized loss command.
4. Commit loss movement and configured financial effects.
5. Read loss and stock registers.
6. Review correction requirements without deleting history.

## Command routing map

```mermaid
flowchart TD
    Entry["Choose a typed command"]
    Gate["Session, permission, license and transaction gate"]
    Good["Inspect result and read projection"]
    Bad["Inspect failure and rollback outcome"]
    h0["InventoryLossCommandHandler"]
    Entry -->|"1 command choices below"| Gate
    Gate -->|"1 typed routes"| h0
    h0 -->|"success"| Good
    h0 -->|"failure"| Bad
```

This overview groups routes by handler to stay readable; each named command and its connections follow below. [Shared gate details](pipeline.md) apply when this handler is invoked through the pipeline. First-run provisioning is an explicit [separate path](access.md). Source construction sites show candidates, not proof of a connected or reachable UI path.

## Commands, options and implementation connections

### RecordInventoryLossCommand

Handler: [InventoryLossCommandHandler](code-application.md#src-ad1ac7eca868). Result type: <code>InventoryLossResult</code>.

Declaration: [InventoryLossCommands.cs:7](code-application.md#src-b3991f732d77). <code>RequiredPermission = Permissions.AdjustStock</code>

Construction sites: **None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.

Handler method: [InventoryLossCommandHandler.HandleAsync(RecordInventoryLossCommand,CommandEnvelope&lt;RecordInventoryLossCommand&gt;,CancellationToken)](code-application.md#m-435d0a757769).

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>inventory_loss_records</code> |
| Writes / DDL | None extracted directly; inspect helpers and dynamic paths. |
| Literal failure codes | <code>INVALID_LOSS</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

## Verification still required

No application journey was executed for this map. Use a separate synthetic test environment to verify permission denial, valid success, invalid inputs, state conflicts, cancellation, transaction rollback, retry/idempotency and the resulting projection. Add physical-device checks only where the workflow dispatches output. Preserve original financial history when reviewing corrections or reversals.
