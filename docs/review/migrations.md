---
id: PP-REVIEW-MIGRATIONS
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: ["PP-F022"]
---

# Migration and persistence lifecycle

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

Feature coverage: PP-F022. Source: [DatabaseMigrator.cs:1](code-infrastructure.md#src-03c231a85247), [SqliteConnectionPolicy.cs:1](code-infrastructure.md#src-4b435878ecef).

## Step-by-step review route

The numbered route is a business review checklist. Branches are separate actions; it does not imply that all actions occur in one transaction.

1. Open a connection under SQLite policy.
2. Read schema_version.
3. Load the next declared SQL migration.
4. Execute script and version row in a transaction.
5. Commit or roll back and surface startup failure.
6. Continue through version 83.

## Lifecycle review map

```mermaid
flowchart TD
    s0["Open a connection under SQLite policy"]
    s1["Read schema_version"]
    s2["Load the next declared SQL migration"]
    s3["Execute script and version row in a transaction"]
    s4["Commit or roll back and surface startup failure"]
    s5["Continue through version 83"]
    s0 -->|"review next"| s1
    s1 -->|"review next"| s2
    s2 -->|"review next"| s3
    s3 -->|"review next"| s4
    s4 -->|"review next"| s5
```

This is a review route across the cited implementation, not a runtime trace captured from an executing application. [Runtime ownership](runtime.md) and the [source catalogues](index.md#source-catalogues) provide the actual composition evidence.

## Verification still required

No application journey was executed for this map. Use a separate synthetic test environment to verify permission denial, valid success, invalid inputs, state conflicts, cancellation, transaction rollback, retry/idempotency and the resulting projection. Add physical-device checks only where the workflow dispatches output. Preserve original financial history when reviewing corrections or reversals.
