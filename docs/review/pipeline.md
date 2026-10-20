---
id: PP-REVIEW-PIPELINE
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: []
---

# Command and failure pipeline

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

This map follows the inspected `ExecuteAsync` control flow. Both the post-gate preflight block and the in-transaction block share a unified cancellation/exception normalization boundary (`PP-REV-002` option `boundary`), rolling back only when an active transaction was opened.

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

[CommandPipeline.cs:27](code-application.md#src-b29270acda74)

[ICommand and permission declarations](access.md) · [Error catalogue](errors.md) · [Physical output](output.md)
