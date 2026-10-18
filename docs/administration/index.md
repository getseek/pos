---
id: PP-ADMIN-001
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-001", "E-003", "E-004", "E-005", "E-009"]
features: ["PP-F003", "PP-F015", "PP-F018", "PP-F019", "PP-F021"]
---

# Roles and administration

<div class="meta">DRAFT · source review 18 October 2026 · documentation foundation D02</div>

Organize guidance by responsibility. The labels below describe documentation audiences, not a claim that the application ships an identical predefined role or permission bundle.

| Responsibility | Typical documentation needs | Coverage |
| --- | --- | --- |
| Cashier | Workspace identity, sale/invoice review, customer selection, returns and recorded outcomes. | PP-F004–007, PP-F013, PP-F020 |
| Stock controller | Categories/UOM, intake, lot/serial handling, adjustments, waste and imports. | PP-F008–014 |
| Production operator | Recipe inputs, output, traceability and completion/cancellation rules. | PP-F012 |
| Manager/payroll | Teams, confidential salary data, expense records, optional payments and reports. | PP-F015–017 |
| Administrator | Accounts/effective permissions, settings, printing, data paths and migration. | PP-F003, PP-F018–021 |

## Access and confidential records

Effective permission checks must be documented from command/query boundaries, rather than inferred from a visible or hidden button. The detailed permission-key matrix will be reviewed in D04. Salary recipient details, PINs, real payment references and receipt photos should not be placed in documentation captures or support examples.

## Settings and presentation

The current application includes English, Thai and Myanmar Unicode presentation. Source declares bundled Noto Sans Thai/Myanmar TTF resources and copies fonts for printing. Bundling does not prove correct shaping, clipping, pagination, OS scaling or physical printer output on another machine.

Website text samples for layout review:

- English: **Inventory and expenses**
- Thai: <span lang="th">สินค้าและค่าใช้จ่าย</span>
- Myanmar: <span lang="my">ကုန်ပစ္စည်းနှင့် အသုံးစရိတ်</span>

## Hardware and data responsibilities

Printer queue/driver selection, receipt layout, cutter/drawer actions and queued output recovery require explicit physical-device checks. A queued/spooled result is not proof of a printed receipt or a safe drawer retry.

Data paths differ between the desktop and DataService. Start with [workspace boundaries](../getting-started/workspaces.md), and retain a source review date for any transfer, reset or recovery instructions. No new backup implementation or service-storage cutover is certified by this documentation release.
