---
id: PP-REVIEW-INDEX
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: []
---

# Code review atlas

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

Use this atlas to inspect **331 application C# files, 2,264 method declarations, 174 handled command types, 138 reconstructed tables and 262 foreign-key column mappings**. All 25 workflow groups have a map. The catalogues include the remaining helper, reader, domain and UI declarations.

**Producer coverage:** 74 handled command types have no explicit construction site in this syntax snapshot. That is a connection-analysis gap, not proof of unreachable code; target-typed construction, factories and runtime dispatch need further analysis. 55 methods contain interpolated SQL requiring manual inspection.

**Scope:** source connections and selected manual control-flow review. Syntax parsing found no C# syntax errors in 494 files, including 163 test files. This does not establish compilation, resolved calls, passing tests or a working business journey. [Read the extraction limits](method.md).

See [source-checked business rules](source-check.md) for corrected checkout, Cafe, attachment, expense, payroll and settings claims.

## Start a review

1. Open the [runtime map](runtime.md), [command pipeline](pipeline.md) and [access/read paths](access.md).
2. Choose a workflow below; follow its command, permission, producer, handler, table and failure references.
3. Inspect [database relationships](schema.md), [error codes](errors.md) and [UI command bindings](bindings.md).
4. Use [findings and change choices](decisions.md) to select a proposal and review its implementation steps and acceptance checks. Choices are a local review draft, not application changes.

## Business and operational maps

| Map | Feature coverage | Handled command types |
| --- | --- | ---: |
| [Launch and startup](launch.md) | PP-F001 | 0 |
| [Workspace isolation and reset](workspaces.md) | PP-F002 | 0 |
| [Identity, access and first run](security.md) | PP-F003 | 5 |
| [Cart and checkout](checkout.md) | PP-F004 | 11 |
| [Invoice collection and commercial lifecycle](invoices.md) | PP-F005 | 7 |
| [Customer returns and inspection](returns.md) | PP-F006 | 2 |
| [Shifts, cash loss and reports](cash.md) | PP-F007 | 5 |
| [Products, categories and units](catalog.md) | PP-F008 | 21 |
| [Stock, locations, lots and serials](inventory.md) | PP-F009 | 13 |
| [Inventory loss and waste](waste.md) | PP-F010 | 1 |
| [Pricing, offers, labels and mass runs](pricing.md) | PP-F011 | 14 |
| [Kits, BOM and production](production.md) | PP-F012 | 13 |
| [Customers, suppliers and third parties](parties.md) | PP-F013 | 9 |
| [Product and third-party imports](imports.md) | PP-F014, PP-F013 | 2 |
| [Team membership and login access](teams.md) | PP-F015 | 2 |
| [People, agreements and salary](salary.md) | PP-F016 | 12 |
| [Expenses, payments and attachments](expenses.md) | PP-F017 | 11 |
| [Settings and output verification](settings.md) | PP-F018 | 8 |
| [Receipts and physical output](output.md) | PP-F019 | 1 |
| [Order backend and legacy kitchen boundary](orders.md) | PP-F020 | 5 |
| [Desktop and DataService boundaries](service.md) | PP-F021 | 0 |
| [Migration and persistence lifecycle](migrations.md) | PP-F022 | 0 |
| [Purchases, supplier returns and money accounts](procurement.md) | PP-F023 | 13 |
| [Order drafts, reservations and shipping](shipping.md) | PP-F024 | 5 |
| [Batch previews and master-data changes](batch.md) | PP-F025 | 14 |

## Source catalogues

- [GetSeek.Application](code-application.md) — 154 C# files.
- [GetSeek.Contracts](code-contracts.md) — 2 C# files.
- [GetSeek.DataService](code-dataservice.md) — 8 C# files.
- [GetSeek.Desktop](code-desktop.md) — 39 C# files.
- [GetSeek.Domain](code-domain.md) — 31 C# files.
- [GetSeek.Infrastructure](code-infrastructure.md) — 72 C# files.
- [GetSeek.Recovery](code-recovery.md) — 1 C# files.
- [GetSeek.UI.Components](code-ui.components.md) — 24 C# files.

Arrows show source-declared routes or the stated review order. They do not imply that every branch executes in one transaction. SQL tables are literal references filtered against the reconstructed schema; dynamic SQL and runtime dispatch remain explicit analysis limits. Physical side effects require separate evidence.
