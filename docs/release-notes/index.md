---
id: PP-RELEASE-001
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015", "E-016", "E-017", "E-018", "E-019", "E-020", "E-021"]
features: []
---

# Documentation releases

<div class="meta">DRAFT · source review 20 October 2026 · documentation foundation D02</div>

## 20 October 2026 — Calculation, runtime-log guard, and PP-REV-001/002/003/006 sync

Synchronized the documentation atlas, schema reconstruction (84 migrations including `084_CashRoundingTieRule.sql`), source-checked business rules (`PP-RULE-010`), and verification register (`E-016`–`E-021`) with the 20 October 2026 application updates:

- **Calculation, rounding, pricing, and UOM cleanup:** Exclusive-only tax branch cleanup (`TaxMode == 2`) for new carts while preserving historical invoice snapshots; discounted service-charge tax share on net line base; configurable cash rounding tie rule (`even` vs `up`, migration `084_CashRoundingTieRule.sql`); expanded floor-to-increment pricing presets (`1, 5, 10, 50, 100, 500, 1000, 5000, 10000`) with localized microcopy; and removal of the unused legacy `UomConversionEngine.cs`.
- **View-model runtime-log guards:** Guarded background commercial/manufacturing/recipe/third-party readers, headless receipt design preview rendering, and unshared `:memory:` search-usage persistence so unauthenticated or headless view-model initialization writes zero spurious runtime errors (`E-019`).
- **Resolution of P2 review findings (`PP-REV-001`, `PP-REV-002`, `PP-REV-003`, `PP-REV-006`):**
  - `PP-REV-001`: Added `WorkspaceLaunchSelector` and startup conflict rejection in `App.axaml.cs` when contradictory explicit workspace flags are supplied (`E-020`).
  - `PP-REV-002`: Normalized post-gate preflight exceptions and cancellation inside `CommandPipeline.ExecuteAsync` without rolling back unstarted transactions (`E-020`).
  - `PP-REV-003`: Added bounded deduplicated cycle-error logging in `OutputDeviceWorker.RunAsync` (`E-020`).
  - `PP-REV-006`: Restored active single-register bootstrapper integration tests in `SingleRegisterProductionBootstrapperTests.cs` (`E-021`).

## Source review atlas — 18 October 2026

Added source-linked workflow and runtime maps, 172 handled command routes, SQL-only reconstruction of 137 tables, full application method catalogues, UI binding and failure-code indexes, and eight open review decisions with local draft choices. No application code, live database or public hosting changes. See the [atlas](../review/index.md) and its [methodology](../review/method.md).

## 18 October 2026 — D02 foundation

Established the independent documentation project, inspected Restaurant patterns, recorded infrastructure/source baselines, inventoried Premium workflows and evidence, and introduced a pinned Zensical scaffold with automated validation and a local preview.

This edition contains orientation, role/workflow maps, evidence definitions and maintainers' build instructions. It does not claim completion of the detailed operator/administrator/developer manuals, a new application acceptance run, or public deployment.

The next planned work is D03 user manuals and D04 technical references/evidence reconciliation, followed by D05 content/site QA. Live Caddy, a dedicated tunnel, DNS and startup persistence remain D06–D08 work.

The source cross-check corrected expense photo storage to transactional SQLite BLOBs, distinguished current Cafe counter checkout from legacy kitchen queues, and expanded the pipeline maps around preflight exceptions and unavailable idempotent results.
