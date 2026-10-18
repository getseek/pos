# Feature coverage matrix — D01

Authoritative record: `features.json`. Stable feature IDs connect business workflows, roles, source digests, evidence IDs, future pages and documentation maturity. **Located** means an implementation entry point was found, not that the journey works. **Source-reviewed** remains distinct from runtime verification.

| ID | Workflow / role | Source review | Documentation target / maturity | Evidence | Limitation |
| --- | --- | --- | --- | --- | --- |
| PP-F001 | Install and launch / developer | source-reviewed | `getting-started/index.md` / scaffolded | E-010 | Clean-machine installation remains unverified. |
| PP-F002 | Real Shop and persistent Demo / administrator | source-reviewed | `getting-started/workspaces.md` / scaffolded | E-001, E-002 | No reset or data-transfer journey executed. |
| PP-F003 | Sign in, permissions and session lock / administrator | located | `administration/security.md` / planned | E-009 | Detailed authorization review and operator guide are D03/D04 work. |
| PP-F004 | Pay-now checkout and tender review / cashier | located | `operator/checkout.md` / planned | not yet assigned | External QR/bank confirmation and physical output require separate evidence. |
| PP-F005 | Invoices, pay later and settlements / cashier | located | `operator/invoices.md` / planned | not yet assigned | Payment/reversal behavior needs focused guide verification. |
| PP-F006 | Returns and refunds / cashier | located | `operator/returns.md` / planned | not yet assigned | Traceable returns and quarantine promises require source review. |
| PP-F007 | Open/close shift and X/Z reports / manager | located | `operator/cash-and-reports.md` / planned | not yet assigned | Frozen report content and hardware output are not reverified. |
| PP-F008 | Catalog, categories and units / stock-controller | located | `operator/catalog.md` / planned | not yet assigned | Detailed item-purpose/UOM guide pending. |
| PP-F009 | Receive and adjust stock / stock-controller | located | `operator/inventory.md` / planned | not yet assigned | Lot/serial selection, reservations and stock-history claims need review. |
| PP-F010 | Waste and inventory loss / stock-controller | located | `operator/waste.md` / planned | E-008 | Waste-expense linkage and Z-report scope need behavior review. |
| PP-F011 | Price tiers and batch pricing / manager | located | `operator/pricing.md` / planned | not yet assigned | Pricing waterfall and mass-valuation instructions pending. |
| PP-F012 | Kits, recipes and manufacturing / production | located | `operator/production.md` / planned | not yet assigned | Do not equate a displayed BOM with proven input/output posting. |
| PP-F013 | Customers, suppliers and imports / cashier | located | `operator/third-parties.md` / planned | not yet assigned | Protected Walk-in and duplicate-import workflows need verification. |
| PP-F014 | Products workbook imports / stock-controller | located | `operator/imports.md` / planned | not yet assigned | Row validation, duplicate handling and export parity pending. |
| PP-F015 | Teams, employment and access / administrator | located | `administration/teams.md` / planned | E-008, E-013 | Historical suite is not a fresh whole-feature audit. |
| PP-F016 | Salary agreements, periods and payment / payroll | located | `operator/salary.md` / planned | E-008, E-012, E-013 | Record-only/payable distinctions and finalized-period limits need guide review. |
| PP-F017 | Operating expenses and payment / manager | located | `operator/expenses.md` / planned | E-008, E-013 | Optional payment, reversals and photo admission require detailed review. |
| PP-F018 | Settings, language and print layout / administrator | source-reviewed | `administration/settings.md` / planned | E-004, E-005 | Font packaging checked; rendering/hardware validation remains unverified. |
| PP-F019 | Receipt jobs and reprints / administrator | located | `administration/printing.md` / planned | not yet assigned | Queue acceptance does not prove physical print/drawer success. |
| PP-F020 | Restaurant orders and tables / cashier | located | `operator/orders.md` / planned | not yet assigned | Source exists; do not import Restaurant project architecture promises. |
| PP-F021 | DataService storage and recovery / administrator | source-reviewed | `operations/application-deployment.md` / planned | E-001, E-003 | Desktop IPC cutover and service-owned migration remain unverified. |
| PP-F022 | Migration/schema contracts / developer | source-reviewed | `development/schema.md` / planned | E-006 | 83 scripts observed; no real database opened or migrated. |

D02 provides orientation and a validated framework. Planned targets are backlog entries, not links to nonexistent pages and not claims of complete manuals. D03/D04 must expand source/test associations, actual permission keys, task steps and recovery information before marking a workflow documented.
