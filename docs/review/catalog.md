---
id: PP-REVIEW-CATALOG
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: ["PP-F008"]
---

# Products, categories and units

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

Feature coverage: PP-F008. Source: [SaveProductConfigurationCommandHandler.cs:1](code-application.md#src-c24b9e05b3b2).

## Step-by-step review route

The numbered route is a business review checklist. Branches are separate actions; it does not imply that all actions occur in one transaction.

1. Choose product, category, supplier or unit action.
2. Validate identity, lifecycle and dimensional rules.
3. Save a product configuration or registry command.
4. Reject referenced or incompatible changes.
5. Commit catalog records.
6. Reload catalog projections and affected choices.

## Command routing map

```mermaid
flowchart TD
    Entry["Choose a typed command"]
    Gate["Session, permission, license and transaction gate"]
    Good["Inspect result and read projection"]
    Bad["Inspect failure and rollback outcome"]
    h0["CatalogRegistryCommandHandler"]
    h1["CatalogCommandHandler"]
    h2["SupplierCommandHandler"]
    h3["SaveProductConfigurationCommandHandler"]
    h4["StoreUomPreferenceCommandHandler"]
    Entry -->|"21 command choices below"| Gate
    Gate -->|"10 typed routes"| h0
    h0 -->|"success"| Good
    h0 -->|"failure"| Bad
    Gate -->|"6 typed routes"| h1
    h1 -->|"success"| Good
    h1 -->|"failure"| Bad
    Gate -->|"3 typed routes"| h2
    h2 -->|"success"| Good
    h2 -->|"failure"| Bad
    Gate -->|"1 typed routes"| h3
    h3 -->|"success"| Good
    h3 -->|"failure"| Bad
    Gate -->|"1 typed routes"| h4
    h4 -->|"success"| Good
    h4 -->|"failure"| Bad
```

This overview groups routes by handler to stay readable; each named command and its connections follow below. [Shared gate details](pipeline.md) apply when this handler is invoked through the pipeline. First-run provisioning is an explicit [separate path](access.md). Source construction sites show candidates, not proof of a connected or reachable UI path.

## Commands, options and implementation connections

### CreateCategoryCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>ProductCategoryDto</code>.

Declaration: [CatalogRegistryCommands.cs:45](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [SaveManagedCategoryAsync:11068](code-desktop.md#src-16497b924a99)

Handler method: [CatalogRegistryCommandHandler.HandleAsync(CreateCategoryCommand,CommandEnvelope&lt;CreateCategoryCommand&gt;,CancellationToken)](code-application.md#m-d66f4c4edaeb).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.NormalizeProfileScope(string?)](code-application.md#m-eec94a9863fc), [CatalogRegistryCommandHandler.CategoryCodeExistsAsync(DbConnection,DbTransaction?,string,Guid?,CancellationToken)](code-application.md#m-15dd37c6f6bd), [CatalogRegistryCommandHandler.CategoryNameExistsAsync(DbConnection,DbTransaction?,string,Guid?,CancellationToken)](code-application.md#m-055c7a8a4cf4), [CatalogRegistryCommandHandler.NormalizeTargetType(string?)](code-application.md#m-c6e674426295), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | None extracted directly; inspect helpers and dynamic paths. |
| Writes / DDL | <code>product_categories</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>CATEGORY_REQUIRED</code>, <code>DUPLICATE_CATEGORY</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### CreateProductCommand

Handler: [CatalogCommandHandler](code-application.md#src-c2d3294fc0a7). Result type: <code>CatalogItemDto</code>.

Declaration: [CatalogCommands.cs:34](code-application.md#src-8482e00dd58a). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [SaveAsync:74](code-application.md#src-14918ebf4662), [SaveProductConfigurationAsync:10103](code-desktop.md#src-16497b924a99)

Handler method: [CatalogCommandHandler.HandleAsync(CreateProductCommand,CommandEnvelope&lt;CreateProductCommand&gt;,CancellationToken)](code-application.md#m-502eda0717e5).

Same-owner helper candidates: [CatalogCommandHandler.NormalizeProductPurpose(string?)](code-application.md#m-ffc80d767ec4), [CatalogCommandHandler.TryNormalizeCoordinates(string?,string?,string?,string?,string?,string?)](code-application.md#m-1ce10e9a79f4), [CatalogCommandHandler.NormalizeTrackingPolicy(bool,string?,string?)](code-application.md#m-4b7af22d8bfb), [CatalogCommandHandler.ReadUnitDefinitionAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-d8b92ef052b7), [CatalogCommandHandler.ResolveDefaultUnitAsync(DbConnection,DbTransaction?,string?,string,UnitDefinition,CancellationToken)](code-application.md#m-660e7a28d7f4), [CatalogCommandHandler.ResolveCategoryAsync(DbConnection,DbTransaction?,Guid?,string?,CancellationToken)](code-application.md#m-43d87b7002b1), [CatalogCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-13169f17df41), [CatalogCommandHandler.AppendItemHistoryAsync(DbConnection,DbTransaction?,Guid,string,string,string,string?,object,CommandEnvelope&lt;TCommand&gt;,CancellationToken)](code-application.md#m-5845db3c3228). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>items</code> |
| Writes / DDL | <code>item_pricing</code>, <code>items</code> |
| Literal failure codes | <code>DUPLICATE_SKU</code>, <code>INVALID_BUYING_PRICE</code>, <code>INVALID_COST</code>, <code>INVALID_ITEM_LOCATION</code>, <code>INVALID_PRICE</code>, <code>INVALID_PRODUCT_PURPOSE</code>, <code>INVALID_THRESHOLD</code>, <code>INVALID_TRACKING_POLICY</code>, <code>NAME_REQUIRED</code>, <code>SERVICE_REGISTRATION_REQUIRED</code>, <code>SKU_REQUIRED</code>, <code>UOM_INACTIVE</code>, <code>UOM_NOT_FOUND</code>, <code>UOM_REQUIRED</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### CreateServiceCommand

Handler: [CatalogCommandHandler](code-application.md#src-c2d3294fc0a7). Result type: <code>CatalogItemDto</code>.

Declaration: [CatalogCommands.cs:106](code-application.md#src-8482e00dd58a). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: **None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.

Handler method: [CatalogCommandHandler.HandleAsync(CreateServiceCommand,CommandEnvelope&lt;CreateServiceCommand&gt;,CancellationToken)](code-application.md#m-ec56dbb87a53).

Same-owner helper candidates: [CatalogCommandHandler.ReadUnitDefinitionAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-d8b92ef052b7), [CatalogCommandHandler.ResolveDefaultUnitAsync(DbConnection,DbTransaction?,string?,string,UnitDefinition,CancellationToken)](code-application.md#m-660e7a28d7f4), [CatalogCommandHandler.ResolveCategoryAsync(DbConnection,DbTransaction?,Guid?,string?,CancellationToken)](code-application.md#m-43d87b7002b1), [CatalogCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-13169f17df41), [CatalogCommandHandler.AppendItemHistoryAsync(DbConnection,DbTransaction?,Guid,string,string,string,string?,object,CommandEnvelope&lt;TCommand&gt;,CancellationToken)](code-application.md#m-5845db3c3228). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>items</code> |
| Writes / DDL | <code>item_pricing</code>, <code>items</code>, <code>service_items</code> |
| Literal failure codes | <code>DUPLICATE_SKU</code>, <code>INVALID_COST</code>, <code>INVALID_PRICE</code>, <code>NAME_REQUIRED</code>, <code>SKU_REQUIRED</code>, <code>UOM_INACTIVE</code>, <code>UOM_NOT_FOUND</code>, <code>UOM_REQUIRED</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### CreateSupplierCommand

Handler: [SupplierCommandHandler](code-application.md#src-2bdfe6e3c46f). Result type: <code>SupplierDto</code>.

Declaration: [SupplierCommands.cs:21](code-application.md#src-0b51c10a2834). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: **None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.

Handler method: [SupplierCommandHandler.HandleAsync(CreateSupplierCommand,CommandEnvelope&lt;CreateSupplierCommand&gt;,CancellationToken)](code-application.md#m-441821b5ef52).

Same-owner helper candidates: [SupplierCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-8e0f95656592). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>third_parties</code> |
| Writes / DDL | <code>third_parties</code> |
| Literal failure codes | <code>CODE_REQUIRED</code>, <code>DUPLICATE_CODE</code>, <code>NAME_REQUIRED</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### CreateUomCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>UomDefinitionDto</code>.

Declaration: [CatalogRegistryCommands.cs:88](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [SaveManagedUnitAsync:11410](code-desktop.md#src-16497b924a99)

Handler method: [CatalogRegistryCommandHandler.HandleAsync(CreateUomCommand,CommandEnvelope&lt;CreateUomCommand&gt;,CancellationToken)](code-application.md#m-ae8d7a0b2824).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.NormalizeUnitKind(string?)](code-application.md#m-c8b399312411), [CatalogRegistryCommandHandler.NormalizeDimension(string?)](code-application.md#m-47f226c14f6a), [CatalogRegistryCommandHandler.UomCodeExistsAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-50d7b2328d4e), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | None extracted directly; inspect helpers and dynamic paths. |
| Writes / DDL | <code>uoms</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>DUPLICATE_UOM</code>, <code>UOM_DIMENSION_MISMATCH</code>, <code>UOM_FACTOR_INVALID</code>, <code>UOM_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### DeactivateCategoryCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>bool</code>.

Declaration: [CatalogRegistryCommands.cs:69](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [ToggleManagedCategoryActiveAsync:11126](code-desktop.md#src-16497b924a99)

Handler method: [CatalogRegistryCommandHandler.HandleAsync(DeactivateCategoryCommand,CommandEnvelope&lt;DeactivateCategoryCommand&gt;,CancellationToken)](code-application.md#m-a7fb74fc19e0).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.ReadCategoryAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-fa45c96d6b54), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>items</code> |
| Writes / DDL | <code>product_categories</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>CATEGORY_IN_USE</code>, <code>CATEGORY_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### DeactivateProductCommand

Handler: [CatalogCommandHandler](code-application.md#src-c2d3294fc0a7). Result type: <code>bool</code>.

Declaration: [CatalogCommands.cs:92](code-application.md#src-8482e00dd58a). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [DeactivateProductAsync:10198](code-desktop.md#src-16497b924a99)

Handler method: [CatalogCommandHandler.HandleAsync(DeactivateProductCommand,CommandEnvelope&lt;DeactivateProductCommand&gt;,CancellationToken)](code-application.md#m-37816510b61b).

Same-owner helper candidates: [CatalogCommandHandler.HandleAsync(CreateProductCommand,CommandEnvelope&lt;CreateProductCommand&gt;,CancellationToken)](code-application.md#m-502eda0717e5), [CatalogCommandHandler.HandleAsync(UpdateProductCommand,CommandEnvelope&lt;UpdateProductCommand&gt;,CancellationToken)](code-application.md#m-83ad1eb9103b), [CatalogCommandHandler.HandleAsync(SetProductStatusCommand,CommandEnvelope&lt;SetProductStatusCommand&gt;,CancellationToken)](code-application.md#m-3a420f15c21e), [CatalogCommandHandler.HandleAsync(CreateServiceCommand,CommandEnvelope&lt;CreateServiceCommand&gt;,CancellationToken)](code-application.md#m-ec56dbb87a53), [CatalogCommandHandler.HandleAsync(UpdateServiceCommand,CommandEnvelope&lt;UpdateServiceCommand&gt;,CancellationToken)](code-application.md#m-ea4c9a18bbae). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | None extracted directly; inspect helpers and dynamic paths. |
| Writes / DDL | None extracted directly; inspect helpers and dynamic paths. |
| Literal failure codes | None extracted directly; inspect helpers and dynamic paths. |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### DeactivateSupplierCommand

Handler: [SupplierCommandHandler](code-application.md#src-2bdfe6e3c46f). Result type: <code>bool</code>.

Declaration: [SupplierCommands.cs:51](code-application.md#src-0b51c10a2834). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: **None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.

Handler method: [SupplierCommandHandler.HandleAsync(DeactivateSupplierCommand,CommandEnvelope&lt;DeactivateSupplierCommand&gt;,CancellationToken)](code-application.md#m-d42558026794).

Same-owner helper candidates: [SupplierCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-8e0f95656592). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>third_parties</code> |
| Writes / DDL | <code>third_parties</code> |
| Literal failure codes | <code>SUPPLIER_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### DeactivateUomCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>bool</code>.

Declaration: [CatalogRegistryCommands.cs:114](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [ToggleManagedUnitActiveAsync:11460](code-desktop.md#src-16497b924a99)

Handler method: [CatalogRegistryCommandHandler.HandleAsync(DeactivateUomCommand,CommandEnvelope&lt;DeactivateUomCommand&gt;,CancellationToken)](code-application.md#m-2c2bbbc7eefc).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.ReadUomAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-541750121d7a), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>items</code> |
| Writes / DDL | <code>uoms</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>UOM_DEFINITION_IN_USE</code>, <code>UOM_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### DeleteCategoryCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>bool</code>.

Declaration: [CatalogRegistryCommands.cs:79](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: **None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.

Handler method: [CatalogRegistryCommandHandler.HandleAsync(DeleteCategoryCommand,CommandEnvelope&lt;DeleteCategoryCommand&gt;,CancellationToken)](code-application.md#m-296d2c281ff8).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.ReadCategoryAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-fa45c96d6b54), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>batch_previews</code>, <code>items</code>, <code>product_category_pricing_rules</code> |
| Writes / DDL | <code>product_categories</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>CATEGORY_BUILTIN</code>, <code>CATEGORY_DELETE_BLOCKED</code>, <code>CATEGORY_IN_USE</code>, <code>CATEGORY_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### DeleteUomCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>bool</code>.

Declaration: [CatalogRegistryCommands.cs:124](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: **None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.

Handler method: [CatalogRegistryCommandHandler.HandleAsync(DeleteUomCommand,CommandEnvelope&lt;DeleteUomCommand&gt;,CancellationToken)](code-application.md#m-5c4e71f7e297).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.ReadUomAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-541750121d7a), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>barcodes</code>, <code>bom_items</code>, <code>draft_cart_lines</code>, <code>item_kit_components</code>, <code>item_price_history</code>, <code>items</code>, <code>production_run_inputs</code>, <code>production_run_outputs</code>, <code>sales_lines</code>, <code>stock_movements</code>, <code>store_uom_preferences</code>, <code>uom_dimensions</code> |
| Writes / DDL | <code>uoms</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>UOM_BUILTIN</code>, <code>UOM_DEFINITION_IN_USE</code>, <code>UOM_DELETE_BLOCKED</code>, <code>UOM_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### ReactivateCategoryCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>bool</code>.

Declaration: [CatalogRegistryCommands.cs:74](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [ToggleManagedCategoryActiveAsync:11131](code-desktop.md#src-16497b924a99)

Handler method: [CatalogRegistryCommandHandler.HandleAsync(ReactivateCategoryCommand,CommandEnvelope&lt;ReactivateCategoryCommand&gt;,CancellationToken)](code-application.md#m-e0dafe188016).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.ReadCategoryAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-fa45c96d6b54), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | None extracted directly; inspect helpers and dynamic paths. |
| Writes / DDL | <code>product_categories</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>CATEGORY_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### ReactivateUomCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>bool</code>.

Declaration: [CatalogRegistryCommands.cs:119](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [ToggleManagedUnitActiveAsync:11465](code-desktop.md#src-16497b924a99)

Handler method: [CatalogRegistryCommandHandler.HandleAsync(ReactivateUomCommand,CommandEnvelope&lt;ReactivateUomCommand&gt;,CancellationToken)](code-application.md#m-173e9cf4959c).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.ReadUomAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-541750121d7a), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | None extracted directly; inspect helpers and dynamic paths. |
| Writes / DDL | <code>uoms</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>UOM_DIMENSION_MISMATCH</code>, <code>UOM_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### SaveProductConfigurationCommand

Handler: [SaveProductConfigurationCommandHandler](code-application.md#src-c24b9e05b3b2). Result type: <code>CatalogItemDto</code>.

Declaration: [SaveProductConfigurationCommand.cs:12](code-application.md#src-5802398b5ad9). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [SaveAsync:79](code-application.md#src-14918ebf4662), [SaveProductConfigurationAsync:10127](code-desktop.md#src-16497b924a99)

Handler method: [SaveProductConfigurationCommandHandler.HandleAsync(SaveProductConfigurationCommand,CommandEnvelope&lt;SaveProductConfigurationCommand&gt;,CancellationToken)](code-application.md#m-98f2baf362dd).

Same-owner helper candidates: [SaveProductConfigurationCommandHandler.CreateChildEnvelope(CommandEnvelope&lt;SaveProductConfigurationCommand&gt;,TChild)](code-application.md#m-b265a417a9b3), [SaveProductConfigurationCommandHandler.CopyFailure(CommandResult&lt;TIn&gt;)](code-application.md#m-b327a3a23017), [SaveProductConfigurationCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-fe15ef749c1c), [SaveProductConfigurationCommandHandler.ApplyActiveCategoryRuleAsync(CatalogItemDto,SaveItemPricingCommand,Guid?,int?,CancellationToken)](code-application.md#m-b560f7993ac1), [SaveProductConfigurationCommandHandler.SavePrimaryBarcodeAsync(Guid,string,string?,CancellationToken)](code-application.md#m-c3e2782a25a9). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>item_kits</code>, <code>items</code> |
| Writes / DDL | None extracted directly; inspect helpers and dynamic paths. |
| Literal failure codes | <code>AUTH_UNAUTHORIZED</code>, <code>CANNOT_ADJUST_KIT_STOCK</code>, <code>CATEGORY_PRICING_RULE_NOT_FOUND</code>, <code>CATEGORY_PRICING_RULE_STALE</code>, <code>COMPONENTS_REQUIRED</code>, <code>ITEM_KIND_IMMUTABLE</code>, <code>KIT_NOT_FOUND</code>, <code>PRODUCT_PAYLOAD_INVALID</code>, <code>REASON_REQUIRED</code>, <code>SERVICE_KIT_NOT_ALLOWED</code>, <code>SERVICE_STOCK_NOT_ALLOWED</code>, <code>SKU_IMMUTABLE</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### SetProductStatusCommand

Handler: [CatalogCommandHandler](code-application.md#src-c2d3294fc0a7). Result type: <code>bool</code>.

Declaration: [CatalogCommands.cs:100](code-application.md#src-8482e00dd58a). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [HandleAsync:679](code-application.md#src-c2d3294fc0a7), [SaveAsync:84](code-application.md#src-14918ebf4662)

Handler method: [CatalogCommandHandler.HandleAsync(SetProductStatusCommand,CommandEnvelope&lt;SetProductStatusCommand&gt;,CancellationToken)](code-application.md#m-3a420f15c21e).

Same-owner helper candidates: [CatalogCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-13169f17df41), [CatalogCommandHandler.AppendItemHistoryAsync(DbConnection,DbTransaction?,Guid,string,string,string,string?,object,CommandEnvelope&lt;TCommand&gt;,CancellationToken)](code-application.md#m-5845db3c3228). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>items</code> |
| Writes / DDL | <code>items</code> |
| Literal failure codes | <code>ITEM_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### UpdateCategoryCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>ProductCategoryDto</code>.

Declaration: [CatalogRegistryCommands.cs:57](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [SaveManagedCategoryAsync:11052](code-desktop.md#src-16497b924a99)

Handler method: [CatalogRegistryCommandHandler.HandleAsync(UpdateCategoryCommand,CommandEnvelope&lt;UpdateCategoryCommand&gt;,CancellationToken)](code-application.md#m-cb797c0581eb).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.NormalizeProfileScope(string?)](code-application.md#m-eec94a9863fc), [CatalogRegistryCommandHandler.ReadCategoryAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-fa45c96d6b54), [CatalogRegistryCommandHandler.CategoryNameExistsAsync(DbConnection,DbTransaction?,string,Guid?,CancellationToken)](code-application.md#m-055c7a8a4cf4), [CatalogRegistryCommandHandler.NormalizeTargetType(string?)](code-application.md#m-c6e674426295), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | None extracted directly; inspect helpers and dynamic paths. |
| Writes / DDL | <code>product_categories</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>CATEGORY_NOT_FOUND</code>, <code>CATEGORY_REQUIRED</code>, <code>DUPLICATE_CATEGORY</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### UpdateProductCommand

Handler: [CatalogCommandHandler](code-application.md#src-c2d3294fc0a7). Result type: <code>CatalogItemDto</code>.

Declaration: [CatalogCommands.cs:61](code-application.md#src-8482e00dd58a). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [SaveAsync:76](code-application.md#src-14918ebf4662), [SaveProductConfigurationAsync:10074](code-desktop.md#src-16497b924a99)

Handler method: [CatalogCommandHandler.HandleAsync(UpdateProductCommand,CommandEnvelope&lt;UpdateProductCommand&gt;,CancellationToken)](code-application.md#m-83ad1eb9103b).

Same-owner helper candidates: [CatalogCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-13169f17df41), [CatalogCommandHandler.NormalizeProductPurpose(string?)](code-application.md#m-ffc80d767ec4), [CatalogCommandHandler.TryNormalizeCoordinates(string?,string?,string?,string?,string?,string?)](code-application.md#m-1ce10e9a79f4), [CatalogCommandHandler.NormalizeTrackingPolicy(bool,string?,string?)](code-application.md#m-4b7af22d8bfb), [CatalogCommandHandler.IsWeakerTrackingPolicy(string?,string)](code-application.md#m-358646417251), [CatalogCommandHandler.IsTrackingChangeBlockedAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-33c95373caa4), [CatalogCommandHandler.ResolveCategoryAsync(DbConnection,DbTransaction?,Guid?,string?,CancellationToken)](code-application.md#m-43d87b7002b1), [CatalogCommandHandler.ReadUnitDefinitionAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-d8b92ef052b7), [CatalogCommandHandler.ResolveDefaultUnitAsync(DbConnection,DbTransaction?,string?,string,UnitDefinition,CancellationToken)](code-application.md#m-660e7a28d7f4), [CatalogCommandHandler.AppendItemHistoryAsync(DbConnection,DbTransaction?,Guid,string,string,string,string?,object,CommandEnvelope&lt;TCommand&gt;,CancellationToken)](code-application.md#m-5845db3c3228). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>item_kits</code>, <code>item_pricing</code>, <code>items</code>, <code>sales_lines</code>, <code>stock_movements</code> |
| Writes / DDL | <code>item_pricing</code>, <code>items</code> |
| Literal failure codes | <code>BASE_UNIT_IMMUTABLE_WITH_MOVEMENTS</code>, <code>DUPLICATE_SKU</code>, <code>INVALID_BUYING_PRICE</code>, <code>INVALID_COST</code>, <code>INVALID_ITEM_LOCATION</code>, <code>INVALID_PRICE</code>, <code>INVALID_PRODUCT_PURPOSE</code>, <code>INVALID_THRESHOLD</code>, <code>INVALID_TRACKING_POLICY</code>, <code>ITEM_KIND_IMMUTABLE</code>, <code>ITEM_NOT_FOUND</code>, <code>KIT_ITEM_CANNOT_BE_TRACKED</code>, <code>NAME_REQUIRED</code>, <code>SKU_IMMUTABLE</code>, <code>SKU_REQUIRED</code>, <code>TRACKING_CHANGE_BLOCKED</code>, <code>UOM_INACTIVE</code>, <code>UOM_NOT_FOUND</code>, <code>UOM_REQUIRED</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### UpdateServiceCommand

Handler: [CatalogCommandHandler](code-application.md#src-c2d3294fc0a7). Result type: <code>CatalogItemDto</code>.

Declaration: [CatalogCommands.cs:123](code-application.md#src-8482e00dd58a). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: **None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.

Handler method: [CatalogCommandHandler.HandleAsync(UpdateServiceCommand,CommandEnvelope&lt;UpdateServiceCommand&gt;,CancellationToken)](code-application.md#m-ea4c9a18bbae).

Same-owner helper candidates: [CatalogCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-13169f17df41), [CatalogCommandHandler.ResolveCategoryAsync(DbConnection,DbTransaction?,Guid?,string?,CancellationToken)](code-application.md#m-43d87b7002b1), [CatalogCommandHandler.ReadUnitDefinitionAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-d8b92ef052b7), [CatalogCommandHandler.ResolveDefaultUnitAsync(DbConnection,DbTransaction?,string?,string,UnitDefinition,CancellationToken)](code-application.md#m-660e7a28d7f4), [CatalogCommandHandler.AppendItemHistoryAsync(DbConnection,DbTransaction?,Guid,string,string,string,string?,object,CommandEnvelope&lt;TCommand&gt;,CancellationToken)](code-application.md#m-5845db3c3228). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>items</code> |
| Writes / DDL | <code>item_pricing</code>, <code>items</code> |
| Literal failure codes | <code>DUPLICATE_SKU</code>, <code>INVALID_COST</code>, <code>INVALID_PRICE</code>, <code>ITEM_KIND_IMMUTABLE</code>, <code>ITEM_NOT_FOUND</code>, <code>NAME_REQUIRED</code>, <code>SKU_IMMUTABLE</code>, <code>SKU_REQUIRED</code>, <code>UOM_INACTIVE</code>, <code>UOM_NOT_FOUND</code>, <code>UOM_REQUIRED</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### UpdateStoreUomPreferenceCommand

Handler: [StoreUomPreferenceCommandHandler](code-application.md#src-931326887202). Result type: <code>bool</code>.

Declaration: [StoreUomPreferenceCommands.cs:6](code-application.md#src-df6632bf7490). <code>RequiredPermission = Permissions.ManageSettings</code>

Construction sites: [SaveStoreUomPreferenceAsync:11347](code-desktop.md#src-16497b924a99)

Handler method: [StoreUomPreferenceCommandHandler.HandleAsync(UpdateStoreUomPreferenceCommand,CommandEnvelope&lt;UpdateStoreUomPreferenceCommand&gt;,CancellationToken)](code-application.md#m-43ba3062b01a).

Same-owner helper candidates: [StoreUomPreferenceCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-3da35b87c9b9). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>uom_dimensions</code>, <code>uoms</code> |
| Writes / DDL | <code>store_uom_preferences</code> |
| Literal failure codes | <code>DIMENSION_NOT_FOUND</code>, <code>INVALID_BASE_UOM</code>, <code>INVALID_ENTRY_UOM</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### UpdateSupplierCommand

Handler: [SupplierCommandHandler](code-application.md#src-2bdfe6e3c46f). Result type: <code>SupplierDto</code>.

Declaration: [SupplierCommands.cs:35](code-application.md#src-0b51c10a2834). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: **None found** among explicit `new Type(...)` expressions. Target-typed construction, factories and runtime dispatch are not resolved.

Handler method: [SupplierCommandHandler.HandleAsync(UpdateSupplierCommand,CommandEnvelope&lt;UpdateSupplierCommand&gt;,CancellationToken)](code-application.md#m-fe472277612b).

Same-owner helper candidates: [SupplierCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-8e0f95656592). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | <code>third_parties</code> |
| Writes / DDL | <code>third_parties</code> |
| Literal failure codes | <code>CODE_REQUIRED</code>, <code>DUPLICATE_CODE</code>, <code>NAME_REQUIRED</code>, <code>SUPPLIER_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

### UpdateUomCommand

Handler: [CatalogRegistryCommandHandler](code-application.md#src-1b8d6c18449a). Result type: <code>UomDefinitionDto</code>.

Declaration: [CatalogRegistryCommands.cs:102](code-application.md#src-e1ac9f19094b). <code>RequiredPermission = Permissions.ManageCatalog</code>

Construction sites: [SaveManagedUnitAsync:11394](code-desktop.md#src-16497b924a99)

Handler method: [CatalogRegistryCommandHandler.HandleAsync(UpdateUomCommand,CommandEnvelope&lt;UpdateUomCommand&gt;,CancellationToken)](code-application.md#m-46f59572d6fa).

Same-owner helper candidates: [CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)](code-application.md#m-a0a61a0f660e), [CatalogRegistryCommandHandler.ReadUomAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-541750121d7a), [CatalogRegistryCommandHandler.UomIsReferencedAsync(DbConnection,DbTransaction?,string,CancellationToken)](code-application.md#m-ca1e2c9bf689), [CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)](code-application.md#m-f3d25ec02ab0). These are unqualified/this-call name matches, including possible overloads; semantic binding was not performed.

| Direct method syntax | Extracted references |
| --- | --- |
| Reads | None extracted directly; inspect helpers and dynamic paths. |
| Writes / DDL | <code>uoms</code> |
| Literal failure codes | <code>ADMIN_REQUIRED</code>, <code>UOM_DEFINITION_IN_USE</code>, <code>UOM_FACTOR_INVALID</code>, <code>UOM_NOT_FOUND</code> |

Helper calls, table references in helpers, and throw sites are listed in the method catalogue. This table is not a transitive effect analysis.

## Verification still required

No application journey was executed for this map. Use a separate synthetic test environment to verify permission denial, valid success, invalid inputs, state conflicts, cancellation, transaction rollback, retry/idempotency and the resulting projection. Add physical-device checks only where the workflow dispatches output. Preserve original financial history when reviewing corrections or reversals.
