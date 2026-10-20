---
id: PP-REVIEW-SCHEMA-02
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: ["PP-F022"]
---

# Schema 02: cash_movements to facilities

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

[Complete table index and reconstruction limits](schema.md). Arrows below are declared foreign keys, not inferred cardinalities.

## cash_movements {#cash-movements}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["cash_movements"]
    P0["shifts"]
    P1["users"]
    T -->|"shift_id → id"| P0
    T -->|"supervisor_user_id → id, initiator_user_id → id"| P1
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>shift_id</code> | <code>TEXT</code> | True | — |
| <code>movement_type</code> | <code>INTEGER</code> | True | — |
| <code>amount_minor</code> | <code>INTEGER</code> | True | — |
| <code>currency</code> | <code>TEXT</code> | True | — |
| <code>reference_type</code> | <code>TEXT</code> | True | — |
| <code>reference_id</code> | <code>TEXT</code> | True | — |
| <code>initiator_user_id</code> | <code>TEXT</code> | True | — |
| <code>supervisor_user_id</code> | <code>TEXT</code> | False | — |
| <code>reason</code> | <code>TEXT</code> | False | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>supervisor_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |
| 1 / 0 | <code>initiator_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |
| 2 / 0 | <code>shift_id</code> | [shifts](schema-10.md#shifts) / <code>id</code> | NO ACTION / NO ACTION |

</details>

## command_deduplication {#command-deduplication}

No outgoing foreign key declared in the reconstructed schema.

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>idempotency_key</code> | <code>TEXT</code> | False | 1 |
| <code>canonical_hash</code> | <code>TEXT</code> | True | — |
| <code>result_payload</code> | <code>TEXT</code> | True | — |
| <code>executed_at_utc</code> | <code>TEXT</code> | True | — |

</details>

## commercial_shipping_events {#commercial-shipping-events}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["commercial_shipping_events"]
    P0["shipments"]
    P1["supplier_returns"]
    P2["users"]
    T -->|"shipment_id → id"| P0
    T -->|"supplier_return_id → id"| P1
    T -->|"actor_user_id → id"| P2
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>shipment_id</code> | <code>TEXT</code> | False | — |
| <code>supplier_return_id</code> | <code>TEXT</code> | False | — |
| <code>event_kind</code> | <code>TEXT</code> | True | — |
| <code>details</code> | <code>TEXT</code> | True | — |
| <code>actor_user_id</code> | <code>TEXT</code> | True | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>actor_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |
| 1 / 0 | <code>supplier_return_id</code> | [supplier_returns](schema-11.md#supplier-returns) / <code>id</code> | NO ACTION / NO ACTION |
| 2 / 0 | <code>shipment_id</code> | [shipments](schema-10.md#shipments) / <code>id</code> | NO ACTION / NO ACTION |

</details>

## demo_dataset_state {#demo-dataset-state}

No outgoing foreign key declared in the reconstructed schema.

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>INTEGER</code> | False | 1 |
| <code>state</code> | <code>TEXT</code> | True | — |
| <code>dataset_version</code> | <code>INTEGER</code> | True | — |
| <code>completed_at_utc</code> | <code>TEXT</code> | False | — |
| <code>failure_code</code> | <code>TEXT</code> | False | — |
| <code>updated_at_utc</code> | <code>TEXT</code> | True | — |

</details>

## demo_seeded_users {#demo-seeded-users}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["demo_seeded_users"]
    P0["users"]
    T -->|"user_id → id"| P0
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>role_name</code> | <code>TEXT</code> | False | 1 |
| <code>user_id</code> | <code>TEXT</code> | True | — |
| <code>username_snapshot</code> | <code>TEXT</code> | True | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / RESTRICT |

</details>

## draft_cart_lines {#draft-cart-lines}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["draft_cart_lines"]
    P0["draft_carts"]
    P1["items"]
    T -->|"cart_id → id"| P0
    T -->|"item_id → id"| P1
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>cart_id</code> | <code>TEXT</code> | True | — |
| <code>item_id</code> | <code>TEXT</code> | True | — |
| <code>item_sku</code> | <code>TEXT</code> | True | — |
| <code>item_name</code> | <code>TEXT</code> | True | — |
| <code>quantity</code> | <code>REAL</code> | True | — |
| <code>unit_code</code> | <code>TEXT</code> | True | — |
| <code>conversion_factor</code> | <code>REAL</code> | True | — |
| <code>unit_price_minor</code> | <code>INTEGER</code> | True | — |
| <code>currency</code> | <code>TEXT</code> | True | — |
| <code>discount_percentage</code> | <code>REAL</code> | True | — |
| <code>discount_minor</code> | <code>INTEGER</code> | True | — |
| <code>tax_rate</code> | <code>REAL</code> | True | — |
| <code>lot_id</code> | <code>TEXT</code> | False | — |
| <code>serial_number</code> | <code>TEXT</code> | False | — |
| <code>quantity_decimal</code> | <code>TEXT</code> | False | — |
| <code>conversion_factor_decimal</code> | <code>TEXT</code> | False | — |
| <code>tax_rate_decimal</code> | <code>TEXT</code> | False | — |
| <code>is_manual_price_override</code> | <code>INTEGER</code> | True | — |
| <code>price_override_reason</code> | <code>TEXT</code> | True | — |
| <code>benchmark_price_minor</code> | <code>INTEGER</code> | False | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>item_id</code> | [items](schema-04.md#items) / <code>id</code> | NO ACTION / NO ACTION |
| 1 / 0 | <code>cart_id</code> | [draft_carts](schema-02.md#draft-carts) / <code>id</code> | NO ACTION / CASCADE |

</details>

## draft_carts {#draft-carts}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["draft_carts"]
    P0["shifts"]
    P1["third_parties"]
    P2["users"]
    T -->|"shift_id → id"| P0
    T -->|"customer_id → id"| P1
    T -->|"cashier_user_id → id"| P2
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>cashier_user_id</code> | <code>TEXT</code> | True | — |
| <code>shift_id</code> | <code>TEXT</code> | True | — |
| <code>customer_reference</code> | <code>TEXT</code> | False | — |
| <code>status</code> | <code>INTEGER</code> | True | — |
| <code>suspension_note</code> | <code>TEXT</code> | False | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |
| <code>updated_at_utc</code> | <code>TEXT</code> | False | — |
| <code>customer_id</code> | <code>TEXT</code> | False | — |
| <code>customer_name_snapshot</code> | <code>TEXT</code> | False | — |
| <code>promo_type</code> | <code>TEXT</code> | False | — |
| <code>promo_value_decimal</code> | <code>TEXT</code> | False | — |
| <code>promo_reason</code> | <code>TEXT</code> | False | — |
| <code>cart_revision</code> | <code>INTEGER</code> | True | — |
| <code>origin</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>customer_id</code> | [third_parties](schema-11.md#third-parties) / <code>id</code> | NO ACTION / NO ACTION |
| 1 / 0 | <code>shift_id</code> | [shifts](schema-10.md#shifts) / <code>id</code> | NO ACTION / NO ACTION |
| 2 / 0 | <code>cashier_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |

</details>

## expense_attachments {#expense-attachments}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["expense_attachments"]
    P0["expense_attachments"]
    P1["expense_records"]
    P2["users"]
    T -->|"replaced_by_attachment_id → id"| P0
    T -->|"expense_id → id"| P1
    T -->|"actor_user_id → id"| P2
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>expense_id</code> | <code>TEXT</code> | True | — |
| <code>version</code> | <code>INTEGER</code> | True | — |
| <code>is_current</code> | <code>INTEGER</code> | True | — |
| <code>replaced_by_attachment_id</code> | <code>TEXT</code> | False | — |
| <code>mime_type</code> | <code>TEXT</code> | True | — |
| <code>width</code> | <code>INTEGER</code> | True | — |
| <code>height</code> | <code>INTEGER</code> | True | — |
| <code>byte_size</code> | <code>INTEGER</code> | True | — |
| <code>sha256_hash</code> | <code>TEXT</code> | True | — |
| <code>image_data</code> | <code>BLOB</code> | True | — |
| <code>actor_user_id</code> | <code>TEXT</code> | True | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>actor_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |
| 1 / 0 | <code>replaced_by_attachment_id</code> | [expense_attachments](schema-02.md#expense-attachments) / <code>id</code> | NO ACTION / NO ACTION |
| 2 / 0 | <code>expense_id</code> | [expense_records](schema-02.md#expense-records) / <code>id</code> | NO ACTION / CASCADE |

</details>

## expense_categories {#expense-categories}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["expense_categories"]
    P0["users"]
    T -->|"actor_user_id → id"| P0
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>name</code> | <code>TEXT</code> | True | — |
| <code>code</code> | <code>TEXT</code> | True | — |
| <code>is_active</code> | <code>INTEGER</code> | True | — |
| <code>is_system</code> | <code>INTEGER</code> | True | — |
| <code>revision</code> | <code>INTEGER</code> | True | — |
| <code>actor_user_id</code> | <code>TEXT</code> | False | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |
| <code>updated_at_utc</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>actor_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |

</details>

## expense_payments {#expense-payments}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["expense_payments"]
    P0["expense_payments"]
    P1["expense_records"]
    P2["money_accounts"]
    P3["money_events"]
    P4["shifts"]
    P5["users"]
    T -->|"reversal_of_id → id"| P0
    T -->|"expense_id → id"| P1
    T -->|"account_id → id"| P2
    T -->|"money_event_id → id"| P3
    T -->|"shift_id → id"| P4
    T -->|"actor_user_id → id"| P5
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>expense_id</code> | <code>TEXT</code> | True | — |
| <code>kind</code> | <code>TEXT</code> | True | — |
| <code>amount_minor</code> | <code>INTEGER</code> | True | — |
| <code>account_id</code> | <code>TEXT</code> | True | — |
| <code>shift_id</code> | <code>TEXT</code> | False | — |
| <code>paid_at_utc</code> | <code>TEXT</code> | True | — |
| <code>external_reference</code> | <code>TEXT</code> | False | — |
| <code>money_event_id</code> | <code>TEXT</code> | False | — |
| <code>reason</code> | <code>TEXT</code> | True | — |
| <code>actor_user_id</code> | <code>TEXT</code> | True | — |
| <code>reversal_of_id</code> | <code>TEXT</code> | False | — |
| <code>command_key</code> | <code>TEXT</code> | True | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>reversal_of_id</code> | [expense_payments](schema-02.md#expense-payments) / <code>id</code> | NO ACTION / NO ACTION |
| 1 / 0 | <code>actor_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |
| 2 / 0 | <code>money_event_id</code> | [money_events](schema-05.md#money-events) / <code>id</code> | NO ACTION / NO ACTION |
| 3 / 0 | <code>shift_id</code> | [shifts](schema-10.md#shifts) / <code>id</code> | NO ACTION / NO ACTION |
| 4 / 0 | <code>account_id</code> | [money_accounts](schema-05.md#money-accounts) / <code>id</code> | NO ACTION / NO ACTION |
| 5 / 0 | <code>expense_id</code> | [expense_records](schema-02.md#expense-records) / <code>id</code> | NO ACTION / CASCADE |

</details>

## expense_records {#expense-records}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["expense_records"]
    P0["expense_categories"]
    P1["expense_records"]
    P2["inventory_loss_records"]
    P3["person_records"]
    P4["shifts"]
    P5["users"]
    T -->|"category_id → id"| P0
    T -->|"replacement_expense_id → id"| P1
    T -->|"inventory_loss_record_id → id"| P2
    T -->|"payee_person_id → id"| P3
    T -->|"shift_id → id"| P4
    T -->|"cancelled_by_user_id → id, actor_user_id → id"| P5
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>reference</code> | <code>TEXT</code> | True | — |
| <code>category_id</code> | <code>TEXT</code> | True | — |
| <code>name</code> | <code>TEXT</code> | True | — |
| <code>cost_minor</code> | <code>INTEGER</code> | True | — |
| <code>currency</code> | <code>TEXT</code> | True | — |
| <code>decimal_places</code> | <code>INTEGER</code> | True | — |
| <code>occurred_at_utc</code> | <code>TEXT</code> | True | — |
| <code>payee_person_id</code> | <code>TEXT</code> | False | — |
| <code>payee_name_snapshot</code> | <code>TEXT</code> | False | — |
| <code>notes</code> | <code>TEXT</code> | False | — |
| <code>revision</code> | <code>INTEGER</code> | True | — |
| <code>command_key</code> | <code>TEXT</code> | True | — |
| <code>actor_user_id</code> | <code>TEXT</code> | True | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |
| <code>updated_at_utc</code> | <code>TEXT</code> | True | — |
| <code>cancelled_at_utc</code> | <code>TEXT</code> | False | — |
| <code>cancelled_by_user_id</code> | <code>TEXT</code> | False | — |
| <code>cancellation_reason</code> | <code>TEXT</code> | False | — |
| <code>replacement_expense_id</code> | <code>TEXT</code> | False | — |
| <code>shift_id</code> | <code>TEXT</code> | False | — |
| <code>inventory_loss_record_id</code> | <code>TEXT</code> | False | — |
| <code>is_non_cash</code> | <code>INTEGER</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>inventory_loss_record_id</code> | [inventory_loss_records](schema-03.md#inventory-loss-records) / <code>id</code> | NO ACTION / NO ACTION |
| 1 / 0 | <code>shift_id</code> | [shifts](schema-10.md#shifts) / <code>id</code> | NO ACTION / NO ACTION |
| 2 / 0 | <code>replacement_expense_id</code> | [expense_records](schema-02.md#expense-records) / <code>id</code> | NO ACTION / NO ACTION |
| 3 / 0 | <code>cancelled_by_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |
| 4 / 0 | <code>actor_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |
| 5 / 0 | <code>payee_person_id</code> | [person_records](schema-05.md#person-records) / <code>id</code> | NO ACTION / NO ACTION |
| 6 / 0 | <code>category_id</code> | [expense_categories](schema-02.md#expense-categories) / <code>id</code> | NO ACTION / NO ACTION |

</details>

## facilities {#facilities}

No outgoing foreign key declared in the reconstructed schema.

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>code</code> | <code>TEXT</code> | True | — |
| <code>name</code> | <code>TEXT</code> | True | — |
| <code>type</code> | <code>TEXT</code> | True | — |
| <code>is_active</code> | <code>INTEGER</code> | True | — |

</details>
