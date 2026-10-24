---
id: PP-REF-001
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: []
features: []
---

# Feature evidence

<div class="meta">DRAFT · source review 20 October 2026 · generated registry view</div>

These are discovery records for the existing application. **Located** means an entry point was found. **Source-reviewed** means selected source was inspected. Neither establishes an end-to-end working journey. The source review atlas now expands these entry points; detailed operator manuals and runtime acceptance remain later work.

| Feature ID | Business workflow | Primary role | Source review | Guide maturity | Verification limit |
| --- | --- | --- | --- | --- | --- |
| PP-F001 | Install and launch | developer | source-reviewed | scaffolded | Clean-machine installation remains unverified. |
| PP-F002 | Real Shop and persistent Demo | administrator | source-reviewed | scaffolded | No reset or data-transfer journey executed. |
| PP-F003 | Sign in, permissions and session lock | administrator | source-reviewed | planned | Detailed authorization review and operator guide are D03/D04 work. |
| PP-F004 | Pay-now checkout and tender review | cashier | source-reviewed | planned | External QR/bank confirmation and physical output require separate evidence. |
| PP-F005 | Invoices, pay later and settlements | cashier | located | planned | Payment/reversal behavior needs focused guide verification. |
| PP-F006 | Returns and refunds | cashier | located | planned | Traceable returns and quarantine promises require source review. |
| PP-F007 | Open/close shift and X/Z reports | manager | source-reviewed | planned | Frozen report content and hardware output are not reverified. |
| PP-F008 | Catalog, categories and units | stock-controller | located | planned | Detailed item-purpose/UOM guide pending. |
| PP-F009 | Receive and adjust stock | stock-controller | located | planned | Lot/serial selection, reservations and stock-history claims need review. |
| PP-F010 | Waste and inventory loss | stock-controller | source-reviewed | planned | Waste-expense linkage and Z-report scope need behavior review. |
| PP-F011 | Price tiers and batch pricing | manager | located | planned | Pricing waterfall and mass-valuation instructions pending. |
| PP-F012 | Kits, recipes and manufacturing | production | located | planned | Do not equate a displayed BOM with proven input/output posting. |
| PP-F013 | Customers, suppliers and imports | cashier | source-reviewed | planned | 53 fresh targeted import/workbook/headless UI tests passed (E-023). Success and known rejection clear previews and request an XLSX; correctable failures preserve uncommitted Stock/create input. Download Result saves the separate last result without importing. Unsafe inputs and uncertain outcomes use diagnostic-only reports; uncertain outcomes do not assert rollback or safe resubmission. Native picker/save actions, live shop, physical devices and full-suite acceptance were not verified. Operator manual remains planned. |
| PP-F014 | Products workbook imports | stock-controller | source-reviewed | planned | 53 fresh targeted import/workbook/headless UI tests passed (E-023); stage-2 performance refactor of ImportProductsCommandHandler verified by import-filtered 54/54 (E-024) and full solution suite 1305/1305 (E-025) console logs on 2026-10-24. Success and known rejection clear previews and request an XLSX; correctable failures preserve uncommitted Stock/create input. Download Result saves the separate last result without importing. Unsafe inputs and uncertain outcomes use diagnostic-only reports; uncertain outcomes do not assert rollback or safe resubmission. Console logs, not TRX. Native picker/save actions, live shop and physical devices were not verified; the stage-2 timing claim (~19.5% flow reduction, batch 03, disposable DBs) is a benchmark observation, not a product acceptance criterion. Operator manual remains planned. |
| PP-F015 | Teams, employment and access | administrator | located | planned | Historical suite is not a fresh whole-feature audit. |
| PP-F016 | Salary agreements, periods and payment | payroll | source-reviewed | planned | Record-only/payable distinctions and finalized-period limits need guide review. |
| PP-F017 | Operating expenses and payment | manager | source-reviewed | planned | Optional payment, reversals and photo admission require detailed review. |
| PP-F018 | Settings, language and print layout | administrator | source-reviewed | planned | Font packaging checked; rendering/hardware validation remains unverified. |
| PP-F019 | Receipt jobs and reprints | administrator | source-reviewed | planned | Queue acceptance does not prove physical print/drawer success. |
| PP-F020 | Order backend and legacy resolution | cashier | source-reviewed | planned | Current Cafe uses pay-now Counter Service. Backend kitchen ticket producers exist, but the bundled worker does not claim their job types; no physical kitchen route is certified. |
| PP-F021 | DataService storage and recovery | administrator | source-reviewed | planned | Desktop IPC cutover and service-owned migration remain unverified. |
| PP-F022 | Migration/schema contracts | developer | source-reviewed | planned | 84 scripts observed; no real database opened or migrated. |
| PP-F023 | Procurement and money accounts | manager | source-reviewed | scaffolded | Code routing and failure sites mapped; business journey and device acceptance not rerun. |
| PP-F024 | Fulfillment, reservations and shipping | operator | source-reviewed | scaffolded | Code routing and failure sites mapped; business journey and device acceptance not rerun. |
| PP-F025 | Batch previews and changes | administrator | source-reviewed | scaffolded | Code routing and failure sites mapped; business journey and device acceptance not rerun. |

## Source review maps

- [PP-F001: Install and launch](../review/launch.md)
- [PP-F002: Real Shop and persistent Demo](../review/workspaces.md)
- [PP-F003: Sign in, permissions and session lock](../review/security.md)
- [PP-F004: Pay-now checkout and tender review](../review/checkout.md)
- [PP-F005: Invoices, pay later and settlements](../review/invoices.md)
- [PP-F006: Returns and refunds](../review/returns.md)
- [PP-F007: Open/close shift and X/Z reports](../review/cash.md)
- [PP-F008: Catalog, categories and units](../review/catalog.md)
- [PP-F009: Receive and adjust stock](../review/inventory.md)
- [PP-F010: Waste and inventory loss](../review/waste.md)
- [PP-F011: Price tiers and batch pricing](../review/pricing.md)
- [PP-F012: Kits, recipes and manufacturing](../review/production.md)
- [PP-F013: Customers, suppliers and imports](../review/parties.md)
- [PP-F014: Products workbook imports](../review/imports.md)
- [PP-F015: Teams, employment and access](../review/teams.md)
- [PP-F016: Salary agreements, periods and payment](../review/salary.md)
- [PP-F017: Operating expenses and payment](../review/expenses.md)
- [PP-F018: Settings, language and print layout](../review/settings.md)
- [PP-F019: Receipt jobs and reprints](../review/output.md)
- [PP-F020: Order backend and legacy resolution](../review/orders.md)
- [PP-F021: DataService storage and recovery](../review/service.md)
- [PP-F022: Migration/schema contracts](../review/migrations.md)
- [PP-F023: Procurement and money accounts](../review/procurement.md)
- [PP-F024: Fulfillment, reservations and shipping](../review/shipping.md)
- [PP-F025: Batch previews and changes](../review/batch.md)

The [verification register](verification.md) explains evidence types and the historical test result. Planned guide paths are tracked internally, not presented as completed pages.
