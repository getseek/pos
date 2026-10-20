---
id: PP-REVIEW-SOURCE-CHECK
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# Source-checked business rules

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

The following statements were checked against the cited code after the initial atlas generation. They correct or constrain documentation claims. All are source observations; no application journey or physical device was executed.

## PP-RULE-001: Checkout payment options

The inspected PlaceOrderAsync handles cash and cashier-confirmed static QR/bank transfers. It explicitly rejects QRIS gateway checkout and unallocated Split Bill. A cashier-confirmed transfer is not provider confirmation.

Evidence: [MainViewModel.cs:5485](code-desktop.md#src-16497b924a99), [MainViewModel.cs:5539](code-desktop.md#src-16497b924a99). Verification: **source-only; runtime not rerun**.

## PP-RULE-002: Deferred invoice eligibility

The common IssueAsync path requires an active named customer for deferred settlement. It also validates tender amounts/currencies and rejects an empty cart; TakePaymentCommand delegates to that shared helper.

Evidence: [SaleCommandHandler.cs:211](code-application.md#src-b90bee551ece), [SaleCommandHandler.cs:254](code-application.md#src-b90bee551ece). Verification: **source-only; runtime not rerun**.

## PP-RULE-003: Current Cafe service style

SqliteStoreProfileReader normalizes saved Table Service to Counter Service; the view-model toggle states Counter Service is fixed. Current Cafe checkout must be distinguished from legacy/backend order and kitchen queue code.

Evidence: [SqliteProductionReaders.cs:77](code-infrastructure.md#src-212da8ad4eb4), [MainViewModel.cs:7997](code-desktop.md#src-16497b924a99). Verification: **source-only; runtime not rerun**.

## PP-RULE-004: Expense photo preparation and storage

Photo preparation accepts JPEG/PNG signatures, limits input to 10 MiB and decoded size to 12 megapixels, resizes the longest side to at most 1600 px, and limits prepared output to 2 MiB. Prepared bytes are validated and stored in expense_attachments.image_data with attachment version/replacement metadata.

Evidence: [SqliteExpenseAttachmentService.cs:14](code-infrastructure.md#src-87a2fd6ad020), [SqliteExpenseAttachmentService.cs:78](code-infrastructure.md#src-87a2fd6ad020), [ExpenseCommandHandler.cs:630](code-application.md#src-c02b00854044), [ExpenseCommandHandler.cs:743](code-application.md#src-c02b00854044). Verification: **source-only; runtime not rerun**.

## PP-RULE-005: Non-cash waste expense payments

PayExpenseCommand validates revision/cancellation and explicitly rejects a non-cash expense with NON_CASH_EXPENSE_CANNOT_BE_PAID. Recording inventory waste does not imply a payable cash expense.

Evidence: [ExpensePaymentCommandHandler.cs:94](code-application.md#src-458534a2cf6c). Verification: **source-only; runtime not rerun**.

## PP-RULE-006: Advance payment checks

PayAdvanceCommand requires person/account IDs, a positive amount and reason. It checks that the person exists, is enabled and matches ExpectedPersonRevision before continuing to account validation.

Evidence: [SalaryPaymentCommandHandler.cs:25](code-application.md#src-c26df3332168). Verification: **source-only; runtime not rerun**.

## PP-RULE-007: Settings authority and monetary identity

ApplySettingsCommandHandler requires a live active Admin role. It blocks changing currency/monetary precision when the checked monetary records exist, and writes tax_mode=2 for the exclusive-tax policy. TaxMode in the command shape is not evidence of a freely selectable policy.

Evidence: [ApplySettingsCommandHandler.cs:25](code-application.md#src-87133587a4b1), [ApplySettingsCommandHandler.cs:42](code-application.md#src-87133587a4b1), [ApplySettingsCommandHandler.cs:76](code-application.md#src-87133587a4b1). Verification: **source-only; runtime not rerun**.

## PP-RULE-008: Inventory loss delegates to adjustment

RecordInventoryLossCommand validates positive quantity, allowed reason and explanation, then calls InventoryCommandHandler with a negative AdjustStockCommand sharing the UnitOfWork. The loss result is read from inventory_loss_records for that movement.

Evidence: [InventoryLossCommandHandler.cs:10](code-application.md#src-ad1ac7eca868). Verification: **source-only; runtime not rerun**.

## PP-RULE-009: Kitchen queue is not physical output

KitchenTicket and KitchenTicketCancel are produced by order handlers. The bundled worker claim SQL selects only receipt, drawer and shelf-label jobs. The missing consumer is PP-REV-008.

Evidence: [RestaurantOrderCommandHandler.cs:194](code-application.md#src-b930bdf2056c), [RestaurantOrderCommandHandler.cs:280](code-application.md#src-b930bdf2056c), [OutputDeviceWorker.cs:254](code-infrastructure.md#src-64d2e3097e9f). Verification: **source-only; runtime not rerun**.

## PP-RULE-010: Exclusive tax, cash rounding tie rule, and pricing floor presets

CartCalculationService and SaleCommandHandler enforce exclusive tax (TaxMode 2) for new carts, compute service-charge tax share on the discounted net line base, and apply configurable cash rounding tie rules (even vs up, persisted via migration 084_CashRoundingTieRule.sql). PricingCalculationEngine.RoundToIncrement uses floor-to-increment semantics with UI presets 1, 5, 10, 50, 100, 500, 1000, 5000, and 10000.

Evidence: [CartCalculationService.cs:142](code-application.md#src-32a44e0155db), [PricingCalculationEngine.cs:85](code-domain.md#src-d7d3ebe3099f), [084_CashRoundingTieRule.sql:1](code-infrastructure.md#src-edd8b63847ba). Verification: **source-only; runtime not rerun**.

The full [command pipeline](pipeline.md), [expense map](expenses.md), [legacy order boundary](orders.md) and [findings](decisions.md) show the related branches and proposed changes.
