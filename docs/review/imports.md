---
id: PP-REVIEW-IMPORTS
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: ["PP-F014"]
---

# Product and third-party imports

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

Feature coverage: PP-F014. Source: [ImportProductsCommandHandler.cs:1](code-application.md#src-2c8d126a7c07), [ImportThirdPartiesCommandHandler.cs:1](code-application.md#src-7bb9c4e66dce).

## Step-by-step review route

The numbered route is a business review checklist. Branches are separate actions; it does not imply that all actions occur in one transaction.

1. Select and parse the workbook.
2. Map and preview rows outside the command.
3. Resolve identity, unit and validation conflicts.
4. Submit authorized import command.
5. Commit accepted import result and history.
6. Review rejected rows before another import.

## Command routing map

```mermaid
flowchart TD
    Entry["Choose a typed command"]
    Gate["Session, permission, license and transaction gate"]
    Good["Inspect result and read projection"]
    Bad["Inspect failure and rollback outcome"]
    h0["ImportProductsCommandHandler"]
    h1["ImportThirdPartiesCommandHandler"]
    Entry -->|"2 command choices below"| Gate
    Gate -->|"1 typed routes"| h0
    h0 -->|"success"| Good
    h0 -->|"failure"| Bad
    Gate -->|"1 typed routes"| h1
    h1 -->|"success"| Good
    h1 -->|"failure"| Bad
```

This overview groups routes by handler to stay readable; each named command and its connections follow below. [Shared gate details](pipeline.md) apply when this handler is invoked through the pipeline. First-run provisioning is an explicit [separate path](access.md). Source construction sites show candidates, not proof of a connected or reachable UI path.

## Commands, options and implementation connections

### ImportProductsCommand

Handler: [ImportProductsCommandHandler](code-application.md#src-2c8d126a7c07). Result type: <code>ImportProductsResult</code>.

Declaration: [ImportCommands.cs:53](code-application.md#src-60301a99263c). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [ConfirmImportAsync:3655](code-desktop.md#src-16497b924a99), [ValidateInventoryAsync:34](code-infrastructure.md#src-9b8064464865)

Handler method: [ImportProductsCommandHandler.HandleAsync(ImportProductsCommand,CommandEnvelope&lt;ImportProductsCommand&gt;,CancellationToken)](code-application.md#m-c862b652239a).

Same-owner helper candidates: [ImportProductsCommandHandler.HasActivePermissionAsync(Guid,string,CancellationToken)](code-application.md#m-96bc157f6d24), [ImportProductsCommandHandler.ResolveItemIdAsync(string,CancellationToken)](code-application.md#m-e7657765daf8), [ImportProductsCommandHandler.BuildLines(ImportStockRow)](code-application.md#m-b750474035cb). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>item_kits</code>, <code>items</code>, <code>third_parties</code> |
| Writes / DDL | None extracted directly; inspect helpers and dynamic paths. |
| Literal failure codes | <code>AUTH_UNAUTHORIZED</code>, <code>IMPORT_CLEAR_NOT_ALLOWED</code>, <code>IMPORT_CURRENCY_MISMATCH</code>, <code>IMPORT_DUPLICATE_ROW</code>, <code>IMPORT_EMPTY</code>, <code>IMPORT_KIT_STOCK</code>, <code>IMPORT_ORPHAN_COMPONENT</code>, <code>IMPORT_PREVIEW_STALE</code>, <code>IMPORT_SKU_NOT_FOUND</code>, <code>IMPORT_TOO_LARGE</code>, <code>IMPORT_UNKNOWN_COLUMN</code>, <code>KIT_CYCLE_DETECTED</code>, <code>SUPPLIER_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### ImportThirdPartiesCommand

Handler: [ImportThirdPartiesCommandHandler](code-application.md#src-7bb9c4e66dce). Result type: <code>ImportThirdPartiesResult</code>.

Declaration: [ImportThirdPartiesCommands.cs:61](code-application.md#src-26c060baba90). <code>RequiredPermission = Permissions.ManageCustomers</code>

Construction sites: [ConfirmThirdPartyImportAsync:208](code-desktop.md#src-63148b75a5e2), [ValidateThirdPartiesAsync:60](code-infrastructure.md#src-9b8064464865)

Handler method: [ImportThirdPartiesCommandHandler.HandleAsync(ImportThirdPartiesCommand,CommandEnvelope&lt;ImportThirdPartiesCommand&gt;,CancellationToken)](code-application.md#m-7085a9c8a444).

Same-owner helper candidates: [ImportThirdPartiesCommandHandler.CheckPriorImportAsync(DbConnection,DbTransaction?,string,string,CancellationToken)](code-application.md#m-0801f3a5aa2c), [ImportThirdPartiesCommandHandler.LoadCategoriesAsync(DbConnection,DbTransaction?,CancellationToken)](code-application.md#m-4c40fbd47cb7), [ImportThirdPartiesCommandHandler.LoadActivePriceTiersAsync(DbConnection,DbTransaction?,CancellationToken)](code-application.md#m-800956081f91), [ImportThirdPartiesCommandHandler.LoadExistingPartyCodesAsync(DbConnection,DbTransaction?,CancellationToken)](code-application.md#m-0893eaf3353f), [ImportThirdPartiesCommandHandler.LoadExistingExternalMappingsAsync(DbConnection,DbTransaction?,CancellationToken)](code-application.md#m-abf0433534f4), [ImportThirdPartiesCommandHandler.IsSystemWalkInAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-26e2e244d8c9), [ImportThirdPartiesCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-471500ccc7e3), [ImportThirdPartiesCommandHandler.InsertExternalMappingAsync(DbConnection,DbTransaction?,string,string,string,string,CancellationToken)](code-application.md#m-95f68fed14b8), [ImportThirdPartiesCommandHandler.GenerateNextCodeAsync(DbConnection,DbTransaction?,CancellationToken)](code-application.md#m-3e0f8ca6bc31). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>third_parties</code> |
| Writes / DDL | <code>third_parties</code>, <code>third_party_imports</code> |
| Literal failure codes | <code>BARCODE_ALREADY_EXISTS</code>, <code>CATEGORY_NOT_FOUND</code>, <code>DUPLICATE_CODE_IN_FILE</code>, <code>DUPLICATE_EXTERNAL_KEY_IN_FILE</code>, <code>IDENTIFIER_CONFLICT</code>, <code>IMPORT_CLEAR_NOT_ALLOWED</code>, <code>IMPORT_EMPTY</code>, <code>IMPORT_PREVIEW_STALE</code>, <code>IMPORT_TOO_LARGE</code>, <code>INVALID_IS_ACTIVE</code>, <code>INVALID_KIND</code>, <code>INVALID_PRICE_LEVEL</code>, <code>MISSING_IDENTIFIER</code>, <code>NAME_REQUIRED</code>, <code>PHONE_FORMAT_INVALID</code>, <code>STATE_REGION_INVALID</code>, <code>SYSTEM_WALK_IN_PROTECTED</code>, <code>THIRD_PARTY_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

## Verification still required

No application journey was executed for this map. Use a separate synthetic test environment to verify permission denial, valid success, invalid inputs, state conflicts, cancellation, transaction rollback, retry/idempotency and the resulting projection. Add physical-device checks only where the workflow dispatches output. Preserve original financial history when reviewing corrections or reversals.
