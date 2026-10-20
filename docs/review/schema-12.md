---
id: PP-REVIEW-SCHEMA-12
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: ["PP-F022"]
---

# Schema 12: user_permission_overrides to workspace_classification

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

[Complete table index and reconstruction limits](schema.md). Arrows below are declared foreign keys, not inferred cardinalities.

## user_permission_overrides {#user-permission-overrides}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["user_permission_overrides"]
    P0["permissions"]
    P1["users"]
    T -->|"permission_key → name"| P0
    T -->|"updated_by_user_id → id, user_id → id"| P1
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>user_id</code> | <code>TEXT</code> | True | 1 |
| <code>permission_key</code> | <code>TEXT</code> | True | 2 |
| <code>is_granted</code> | <code>INTEGER</code> | True | — |
| <code>updated_at_utc</code> | <code>TEXT</code> | True | — |
| <code>updated_by_user_id</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>updated_by_user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / NO ACTION |
| 1 / 0 | <code>permission_key</code> | [permissions](schema-05.md#permissions) / <code>name</code> | NO ACTION / CASCADE |
| 2 / 0 | <code>user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / CASCADE |

</details>

## user_roles {#user-roles}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["user_roles"]
    P0["roles"]
    P1["users"]
    T -->|"role_name → name"| P0
    T -->|"user_id → id"| P1
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>user_id</code> | <code>TEXT</code> | True | 1 |
| <code>role_name</code> | <code>TEXT</code> | True | 2 |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>role_name</code> | [roles](schema-08.md#roles) / <code>name</code> | NO ACTION / CASCADE |
| 1 / 0 | <code>user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / CASCADE |

</details>

## user_security_revisions {#user-security-revisions}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["user_security_revisions"]
    P0["users"]
    T -->|"user_id → id"| P0
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>user_id</code> | <code>TEXT</code> | False | 1 |
| <code>revision</code> | <code>INTEGER</code> | True | — |
| <code>updated_at_utc</code> | <code>TEXT</code> | True | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>user_id</code> | [users](schema-12.md#users) / <code>id</code> | NO ACTION / CASCADE |

</details>

## users {#users}

<details markdown>
<summary>Relationship diagram</summary>

```mermaid
flowchart TD
    T["users"]
    P0["product_categories"]
    T -->|"category_id → id"| P0
```

</details>

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>TEXT</code> | False | 1 |
| <code>username</code> | <code>TEXT</code> | True | — |
| <code>display_name</code> | <code>TEXT</code> | True | — |
| <code>quick_pin_hash</code> | <code>TEXT</code> | False | — |
| <code>is_active</code> | <code>INTEGER</code> | True | — |
| <code>created_at_utc</code> | <code>TEXT</code> | True | — |
| <code>last_login_at_utc</code> | <code>TEXT</code> | False | — |
| <code>category_id</code> | <code>TEXT</code> | False | — |

| FK / sequence | Child column | Parent table / column | On update / delete |
| --- | --- | --- | --- |
| 0 / 0 | <code>category_id</code> | [product_categories](schema-06.md#product-categories) / <code>id</code> | NO ACTION / NO ACTION |

</details>

## workspace_classification {#workspace-classification}

No outgoing foreign key declared in the reconstructed schema.

<details markdown>
<summary>Columns and foreign-key policies</summary>

| Column | SQLite type | NOT NULL | Primary-key position |
| --- | --- | --- | --- |
| <code>id</code> | <code>INTEGER</code> | False | 1 |
| <code>environment</code> | <code>TEXT</code> | True | — |
| <code>marked_at_utc</code> | <code>TEXT</code> | True | — |

</details>
