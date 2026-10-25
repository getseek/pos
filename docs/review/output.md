---
id: PP-REVIEW-OUTPUT
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: ["PP-F019"]
---

# Receipts and physical output

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

Feature coverage: PP-F019. Source: [ReprintReceiptCommandHandler.cs:1](code-application.md#src-f881cdbb15da), [OutputDeviceWorker.cs:1](code-infrastructure.md#src-64d2e3097e9f).

## Step-by-step review route

The numbered route is a business review checklist. Branches are separate actions; it does not imply that all actions occur in one transaction.

1. Authorize a committed receipt reprint.
2. Queue a durable output job.
3. Worker recovers uncertain jobs then claims eligible work.
4. Check saved snapshot and printer capability.
5. Spool or mark failed, unknown or held.
6. Inspect physical outcome before another output.

## Command routing map

```mermaid
flowchart TD
    Entry["Choose a typed command"]
    Gate["Session, permission, license and transaction gate"]
    Good["Inspect result and read projection"]
    Bad["Inspect failure and rollback outcome"]
    h0["QueueReceiptReprintCommandHandler"]
    Entry -->|"1 command choices below"| Gate
    Gate -->|"1 typed routes"| h0
    h0 -->|"success"| Good
    h0 -->|"failure"| Bad
```

This overview groups routes by handler to stay readable; each named command and its connections follow below. [Shared gate details](pipeline.md) apply when this handler is invoked through the pipeline. First-run provisioning is an explicit [separate path](access.md). Source construction sites show candidates, not proof of a connected or reachable UI path.

## Commands, options and implementation connections

### QueueReceiptReprintCommand

Handler: [QueueReceiptReprintCommandHandler](code-application.md#src-f881cdbb15da). Result type: <code>string</code>.

Declaration: [ReprintReceiptCommandHandler.cs:10](code-application.md#src-f881cdbb15da). <code>RequiredPermission = Permissions.ViewAudit</code>

Construction sites: [ReprintSelectedReceiptAsync:191](code-desktop.md#src-3872b07af065), [PrintAuditReceiptAsync:6679](code-desktop.md#src-16497b924a99)

Handler method: [QueueReceiptReprintCommandHandler.HandleAsync(QueueReceiptReprintCommand,CommandEnvelope&lt;QueueReceiptReprintCommand&gt;,CancellationToken)](code-application.md#m-49d7caffe325).

Same-owner helper candidates: [QueueReceiptReprintCommandHandler.Add(DbCommand,string,object)](code-application.md#m-7ee6f1e899c9). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>hardware_jobs</code>, <code>invoice_collections</code>, <code>sale_returns</code>, <code>sales_invoices</code>, <code>user_roles</code>, <code>users</code> |
| Writes / DDL | <code>hardware_jobs</code> |
| Literal failure codes | <code>AUTH_UNAUTHORIZED</code>, <code>INVOICE_NOT_FOUND</code>, <code>INVOICE_REQUIRED</code>, <code>RECEIPT_SNAPSHOT_INVALID</code>, <code>RECEIPT_SNAPSHOT_MISSING</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

## Open review points

- [PP-REV-003: Worker-level failures can repeat without a diagnostic](decisions.md#pp-rev-003) — source-observed observability gap.
- [PP-REV-005: Physical output remains a separate acceptance gate](decisions.md#pp-rev-005) — verification gap / operator decision.

## Verification still required

No application journey was executed for this map. Use a separate synthetic test environment to verify permission denial, valid success, invalid inputs, state conflicts, cancellation, transaction rollback, retry/idempotency and the resulting projection. Add physical-device checks only where the workflow dispatches output. Preserve original financial history when reviewing corrections or reversals.
