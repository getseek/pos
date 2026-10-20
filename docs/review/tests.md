---
id: PP-REVIEW-TESTS
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# Test source and verification limits

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

The extractor parsed **144 C# test source files**. Attribute counts below are syntax counts, not executed test totals. Parameterized cases, exclusions and compilation determine actual execution. No application test was rerun. The prior historical evidence remains [dated and limited](../reference/verification.md).

The integration project excludes three historical files; [PP-REV-006](decisions.md#pp-rev-006) gives review options.

## FullCheckoutWorkflowAcceptanceTests.cs {#src-4d212effbeff}

<code>Software/tests/GetSeek.AcceptanceTests/FullCheckoutWorkflowAcceptanceTests.cs</code> · SHA-256 <code>0cb7582785b1dfe2bd71664623af0039326649f9c3355f1d3a9051a28ff086e2</code>.

Located test declarations: <code>CompleteE2ETradingDayCycle_ShouldExecuteAllOperationsAtomicallyAndMaintainInvariants</code> @50.

## AccountPostingIntegrationTests.cs {#src-46f306490d39}

<code>Software/tests/GetSeek.IntegrationTests/AccountPostingIntegrationTests.cs</code> · SHA-256 <code>79f27b36868172b7d2befb8a7e7c9e459dea0d610a149e4d1ae724ebaca51af0</code>.

Located test declarations: <code>PostAsync_BankPaymentWithValidReference_RecordsMoneyEvent</code> @148, <code>PostAsync_BankPaymentMissingReference_RejectedWithBankConfirmationRequired</code> @184, <code>PostAsync_BankPaymentDuplicateReference_Rejected</code> @210, <code>PostAsync_CashPaymentWithOpenShift_RecordsCashMovementAndMoneyEvent</code> @258, <code>PostAsync_InsufficientFunds_RejectedWithInsufficientFunds</code> @294, <code>SharedPipeline_ConcurrentCommands_SerializeSafelyWithoutTransactionAlreadyActive</code> @320, <code>SharedPipeline_CancelledQueuedCommand_DoesNotRollbackOrDisruptFirstActiveCommand</code> @344.

## Argon2idPasswordHasherTests.cs {#src-f81787d39cd4}

<code>Software/tests/GetSeek.IntegrationTests/Argon2idPasswordHasherTests.cs</code> · SHA-256 <code>38deab56d5e113e2d51b5517170294354e218725c19971948376f5b892b8f208</code>.

Located test declarations: <code>HashPin_ShouldVerifyCorrectly</code> @9.

## AssemblyInfo.cs {#src-2846dd08c9c0}

<code>Software/tests/GetSeek.IntegrationTests/AssemblyInfo.cs</code> · SHA-256 <code>9976d64684080884ef0f0442634d057c3fd2a2c7f74fa7a2062919955ec50a8d</code>.

## AuditJournalSha256ChainTests.cs {#src-d2cdf33d47f4}

<code>Software/tests/GetSeek.IntegrationTests/AuditJournalSha256ChainTests.cs</code> · SHA-256 <code>fce54fc9695c2298e2d2bfd90ffae50dbc69c6e13d9f97059f3f1f9b2dbde8bf</code>.

Located test declarations: <code>AuditJournal_ShouldFormValidSha256Chain</code> @12.

## BatchPricingPreviewUiIntegrationTests.cs {#src-69f43cfe7d15}

<code>Software/tests/GetSeek.IntegrationTests/BatchPricingPreviewUiIntegrationTests.cs</code> · SHA-256 <code>e956142ad14915fe5fe1a0685aedd33b596f8237a54bd0f044c3750b4ba980df</code>.

## BomWorkspaceLayoutTests.cs {#src-9f05f37c71cf}

<code>Software/tests/GetSeek.IntegrationTests/BomWorkspaceLayoutTests.cs</code> · SHA-256 <code>135c4d71a253fab50d1368eb0c5289d5031fc8d9df36fc0a6f740fe9f471d31f</code>.

## CartAllocationIntegrationTests.cs {#src-d854517bff44}

<code>Software/tests/GetSeek.IntegrationTests/CartAllocationIntegrationTests.cs</code> · SHA-256 <code>4d15b80c9c07a605f3225abd4dc91947a344a4b52dadda202cfe05ceddb273ae</code>.

Located test declarations: <code>SerialAllocation_WhenAlreadyHeldByAnotherCart_IsRejectedWithSerialAlreadyCommitted</code> @32, <code>LotAllocation_WhenBalanceInsufficient_IsRejectedWithInsufficientLotBalance</code> @88.

## CashReceiptCompletionIntegrationTests.cs {#src-efae0d8b6f91}

<code>Software/tests/GetSeek.IntegrationTests/CashReceiptCompletionIntegrationTests.cs</code> · SHA-256 <code>9e859bcf736993cd3891cc20cfc9d5db31d7f8f55b9680b0c88dcb5472e06b88</code>.

Located test declarations: <code>ThermalCapability_RequiresAdminPhysicalConfirmation_AndInvalidatesOnQueueChange</code> @23, <code>ThermalCapabilityMutation_IsDeniedToCashier</code> @89.

## CheckoutAndActivityIntegrationTests.cs {#src-60ffc7d1291c}

<code>Software/tests/GetSeek.IntegrationTests/CheckoutAndActivityIntegrationTests.cs</code> · SHA-256 <code>1535d9d9234b0f018f2a25fe54817ad8f20ea77176ced888ab36092abc30ec01</code>.

Located test declarations: <code>MainViewModel_Startup_WhenOpenShiftExists_BootsLockedAndRequiresCredentialUnlock</code> @41, <code>MainViewModel_CounterSale_WhenAuthenticated_CommitsInvoiceAndUpdatesStockAndActivity</code> @115, <code>MainViewModel_CounterSale_IdempotentRetry_PreventsDuplicateInvoiceOrStockDecrement</code> @277, <code>MainViewModel_DurableCart_SurvivesApplicationRestart</code> @387, <code>MainViewModel_CounterSale_WhenUnauthenticated_BlocksCheckout</code> @467, <code>MainViewModel_PlaceOrder_WhenCartSaveFails_HaltsCheckoutBeforeSettlement</code> @520, <code>MainViewModel_PlaceOrder_WhenPaymentMethodIsCardOrQrisOrSplit_BlocksCheckoutWithTruthfulNotification</code> @602, <code>SaleCommandHandler_TakePayment_WhenNonCashTenderIsUnverified_RejectsWithUnverifiedPaymentTender</code> @698, <code>ManualQrAndBank_AreAdminConfiguredAndCashierConfirmedWithDurableTenders</code> @808, <code>SqliteActivityReader_QueryBoundary_EnforcesAuthenticationAndShiftScoping</code> @945, <code>ApplySettings_WhenUnpaidRestaurantOrdersExist_BlocksProfileSwitch</code> @1034, <code>DatabaseMigration_UpgradeFromV5ToV6_WithPopulatedData_Succeeds</code> @1141.

## CommercialAndPosPickersIntegrationTests.cs {#src-8e77dbe7f7a5}

<code>Software/tests/GetSeek.IntegrationTests/CommercialAndPosPickersIntegrationTests.cs</code> · SHA-256 <code>53f6757bf937152ba0c03a295afe1faaa883896b8b20444d9bb1a08985a9ab7f</code>.

Located test declarations: <code>CommercialPickers_ExclusionsBeforeLimit_Honored</code> @108, <code>CommercialPickers_DuplicateNames_RemainDistinctWithCodeOrSku</code> @166, <code>CommercialPickers_GetPartyAndItemAsync_TypedDtoAndPreservation</code> @217.

## CommercialSearchIntegrationTests.cs {#src-c4856c131820}

<code>Software/tests/GetSeek.IntegrationTests/CommercialSearchIntegrationTests.cs</code> · SHA-256 <code>94ed82c097b4475983d3624d6f92e9efd73e1d1be92377411fdd4b9a1809f48a</code>.

Located test declarations: <code>CommercialSearchStates_AreIsolated_AndQueriesDoNotOverwriteEachOther</code> @167, <code>SqliteCommercialReader_InvoicesSearch_FiltersByExactId_AndText</code> @228, <code>SqliteCommercialReader_ShipmentsSearch_FiltersByExactId_AndText</code> @292, <code>SqliteCommercialReader_MoneySearch_FiltersByExactId_AndText</code> @347, <code>SqliteSearchSuggestionReader_CommercialInvoices_Shipments_FinancialRegister_PermissionAndRanking</code> @397.

## CommercialWorkflowIntegrationTests.cs {#src-6e3d098f5c2c}

<code>Software/tests/GetSeek.IntegrationTests/CommercialWorkflowIntegrationTests.cs</code> · SHA-256 <code>ae37612a99ad1a93c29cd93df73024b325ad772a7344b05a56a1af11a808d002</code>.

Located test declarations: <code>CommercialQuoteUsesSharedPrices_RejectsStaleCalculation_AndPreservesDraftChoices</code> @30, <code>CommercialSupplierRefund_AndMoneyFiltersUseAllFactsAcrossPages</code> @51, <code>CommercialShipmentTrackingAndReprintAreAudited_AndDoNotMoveStockAgain</code> @70, <code>PartialCancellationAndPartialReturnReceiptKeepRemainingObligationsOpen</code> @92, <code>PurchaseCreditsOnlyUnreceivedQuantities_WithoutChangingStockOrIssuedAmounts</code> @117, <code>LotReservationSubstitutionIsAtomicAndDispatchUsesTheReplacementIdentity</code> @132, <code>DirectNestedKitRequiresExplicitLeafIdentities_AndDispatchesMatchingComponents</code> @148, <code>BuyingDocumentUsesStoredDiscountAndTax_AndReprintPreservesThoseFacts</code> @169.

## CompactDateFieldUiTests.cs {#src-8c1124cf21d1}

<code>Software/tests/GetSeek.IntegrationTests/CompactDateFieldUiTests.cs</code> · SHA-256 <code>1fef8619945fd38be8ef75f48ebc8cf7c742468d9e950a7b73a46c47e764fc65</code>.

Located test declarations: <code>TryParseDate_ValidFormats_ParsesExpectedDateOnly</code> @14, <code>TryParseDate_LeapYearHandling_LeapYearAcceptedAndNonLeapYearRejected</code> @31, <code>TryParseDate_CenturyAmbiguity_StrictCenturyResolutionStoresFullGregorianYear</code> @44, <code>TryParseDate_RangeBoundaries_EnforcesMinimumAndMaximumDate</code> @57.

## CompactDatePopupLayoutTests.cs {#src-73136c6ce868}

<code>Software/tests/GetSeek.IntegrationTests/CompactDatePopupLayoutTests.cs</code> · SHA-256 <code>27c7f1cd58e5d0c620e50fe453893406fe86262f9b047dadac34ca3875be3028</code>.

## CompactDescriptorsAndRoutesTests.cs {#src-47178870e40b}

<code>Software/tests/GetSeek.IntegrationTests/CompactDescriptorsAndRoutesTests.cs</code> · SHA-256 <code>2a50dacfe264ebba98637fbfdfc1d35df00250602e1f10f0aa3845ec343a72fb</code>.

Located test declarations: <code>RecipesTable_HasThreeDataColumns_AndExplicitEditAction_NoAsterisksOrVersion</code> @94, <code>WipTable_HasThreeColumns_CreatedFinishedStatus_NoAsterisks</code> @125, <code>RecipesTable_RowActivation_OpensNewModeById</code> @160, <code>RecipesTable_EditAction_SuppressesRowActivation_AndOpensRecipeEditor</code> @181, <code>WipTable_RowActivation_OpensApplicableMode_PlannedToStart_InProgressToFinish_CompletedToReadOnly</code> @200, <code>Permissions_ViewOnly_CannotEditRecipe_CannotActivateRecipeRow_WipOpensReadOnly</code> @308, <code>Permissions_ExecuteOnly_CannotEditRecipe_CannotStartPlannedRun_CanFinishInProgress</code> @337, <code>NoFirstRecipeFallback_OpenProductionModalWithNull_LeavesSelectedBomNull</code> @387.

## ConnectedFinancialJourneysIntegrationTests.cs {#src-660355ad7b5c}

<code>Software/tests/GetSeek.IntegrationTests/ConnectedFinancialJourneysIntegrationTests.cs</code> · SHA-256 <code>2ba71e366deafba0c8f5c3705f982427971a836d02418b68f5b629d3b48138e2</code>.

Located test declarations: <code>U15a_Combination1_PersonOnly_LoginOff_SalaryOff_AccruesNoSalary_CannotFinalize_NoExpensesCreated</code> @177, <code>U15a_Combination2_UserAccountOnly_LoginOn_SalaryOff_AccruesNoSalary_CannotFinalize_NoExpensesCreated</code> @222, <code>U15a_Combination3_SalaryPersonOnly_LoginOff_SalaryOn_FullLifecycle_Advance_Bonus_Deduction_Finalize_Pay_History_NoExpenses</code> @265, <code>U15a_Combination4_FullTeamMember_LoginOn_SalaryOn_FullLifecycle_Advance_Bonus_Deduction_Finalize_Pay_History_NoExpenses</code> @374, <code>U15b_CategorizedExpense_SaveUnpaid_CreatesZeroOutflow_MaintainsActiveCategory</code> @472, <code>U15b_CategorizedExpense_PartialPaymentCash_RemainderSafe_RealPostingServices</code> @509, <code>U15b_CategorizedExpense_SaveAndPay_Bank_WithExternalReference_AtomicPosting</code> @573, <code>U15b_CategorizedExpense_ActualReturns_Cash_Safe_Bank_RestoreLedgersAndBalances</code> @613, <code>U15c_SeparateRealAndDemoWorkspaces_DemoResetAndSeed_PreservesRealDatabaseData</code> @715, <code>U15c_IsolatedReset_RetentionAndDependencies_SalaryHistoryAndExpenses</code> @842, <code>U15c_N01_TrackingStartMonth_ProtectsHistoricalIntegrity</code> @920, <code>U15c_N02_ImmutableStatementSnapshot_PreservesHistoricalFactsAfterFutureChanges</code> @971.

## CoreLedgerHardeningTests.cs {#src-e3cdecfd5880}

<code>Software/tests/GetSeek.IntegrationTests/CoreLedgerHardeningTests.cs</code> · SHA-256 <code>f31a76923b5484a1e182a7987b770de92cfd39b2fde7014888b1ee6f4a465911</code>.

Located test declarations: <code>CloseShift_ShouldRequireSupervisorElevation_WhenVarianceExceedsThreshold</code> @38, <code>RefundSale_ShouldFail_WhenNoActiveShiftIsOpen</code> @117, <code>RefundSale_ShouldRejectInvalidProvenanceOrExceededQuantity</code> @174, <code>DoublePayment_SameCartDifferentKeys_ShouldRejectSecondAttempt</code> @249, <code>Checkout_InsufficientStock_ShouldRejectOversell_AndLeaveZeroMovements</code> @343, <code>RefundSale_DuplicateLineInSingleCommand_ShouldGroupAndEnforceOriginalLimit</code> @430, <code>RefundSale_TwoSequentialRefunds_ShouldRejectExcessCumulativeQuantity</code> @498, <code>TakePayment_ShouldRejectDuplicateCartLines_WhenCombinedStockDemandExceedsOnHand</code> @620, <code>TakePayment_ShouldBypassStockCheckAndMovement_ForUntrackedItems</code> @708, <code>TakePayment_ShouldGenerateUniqueDeviceBoundInvoiceNumbers_AcrossMultipleDevices</code> @795.

## CustomerManagementIntegrationTests.cs {#src-6f32fc0ef94d}

<code>Software/tests/GetSeek.IntegrationTests/CustomerManagementIntegrationTests.cs</code> · SHA-256 <code>9b92c5ed0e6c2077f712f57bcd6bbf5675992028fbe59d3c5d001d101e56eb50</code>.

Located test declarations: <code>CustomerMaster_CreateUpdateDeactivate_EnforcesCodeUniquenessAndAuditTrail</code> @53, <code>POS_Checkout_WithRegisteredCustomer_BindsCustomerIdAndPreservesHistoricalSnapshot</code> @150, <code>POS_Checkout_WithWalkInGuest_SucceedsWithNullCustomerIdAndGuestSnapshot</code> @269, <code>CustomerEditOrDeactivation_PreservesHistoricalInvoiceSnapshot</code> @368, <code>CustomerSearch_FiltersCorrectlyByCodeNameAndPhone</code> @480, <code>CustomerOperations_RequireManageCustomersPermission_DeniedForUnauthorizedUser</code> @529, <code>CustomerReader_EnforcesViewPermission_DeniesUnauthorizedAndAllowsAuthorized</code> @569, <code>DatabaseEnforced_CaseInsensitiveCustomerCode_BlocksCompetingConcurrentInserts</code> @629, <code>POS_Checkout_WithForgedDraftCustomerSnapshot_DerivesAuthoritativeNameFromRegisteredCustomer</code> @712.

## CustomerUiIntegrationTests.cs {#src-7de3f4e76e2b}

<code>Software/tests/GetSeek.IntegrationTests/CustomerUiIntegrationTests.cs</code> · SHA-256 <code>0cdc86d3a6843c6e822c7f37268cbb4ea46437201f2d1b482ef2ab4ea886507a</code>.

## DatabaseMigrationTests.cs {#src-894a54d0c118}

<code>Software/tests/GetSeek.IntegrationTests/DatabaseMigrationTests.cs</code> · SHA-256 <code>32b1a9507912007614db8bd077d80cd4e5b7d1ba2edebca601250121b30ff9bd</code>.

Located test declarations: <code>Migration040_UsesRetailForNewWorkspace_AndPreservesExistingCafeOperator</code> @15, <code>Migration039_FromPopulatedV38_PreservesJobsAndInvalidatesLegacyThermalVerification</code> @61, <code>Migration027_FromPopulatedV26_PreservesPricesAndLeavesLegacyPurposeUnclassified</code> @105, <code>Migration028_FromPopulatedV27_PreservesProposalsAndAllowsStaleResolution</code> @184, <code>Migration029_FromPopulatedV28_MapsLegacyCostFloorSourcesToExplicitCostBasis</code> @253, <code>Migration030_FromPopulatedV29_BackfillsExactProposalCostSnapshots</code> @311, <code>Migration026_FromPopulatedV25_PreservesPricingBatchAndAuditHistory</code> @372, <code>MigrateAsync_ShouldCreateAllCoreTablesAndVersion</code> @474, <code>MigrateAsync_ShouldUpgradePopulatedDatabase_FromEarlySchemaToV5WithoutDataLoss</code> @535, <code>MigrateAsync_ShouldUpgradePopulatedDatabase_FromV8ToV10_WithPopulatedMovements_Succeeds</code> @597, <code>MigrateAsync_ShouldPreserveMerchantEditedDefaultSupplier_WhenUpgradedFromV9_EvenWithoutMovements</code> @696, <code>MigrateAsync_ShouldPreserveContactOnlyMerchantEditedDefaultSupplier_WhenUpgradedFromV9</code> @772, <code>MigrateAsync_PopulatedV30ToV31_PreservesAllData</code> @848, <code>MigrateAsync_ShouldSupportLegacyMigration008FacilitiesAndBins_EditAndDeactivateWithRealDatabaseIdentities</code> @948, <code>MigrateAsync_ShouldUpgradePopulatedDatabase_FromV11ToV12_EnforcingCaseInsensitiveUniqueness</code> @1040, <code>MigrateAsync_ShouldUpgradePopulatedDatabase_FromV12ToV13_EnforcingItemRelationshipsAndManufacturing</code> @1135, <code>MigrateAsync_ShouldUpgradePopulatedDatabase_FromV13ToV14_AddingShiftZReportsAndPermissions</code> @1264, <code>MigrateAsync_ShouldApplyMigration019_AddingCategoryTargetTypesAndPartyUserAssociations</code> @1399, <code>Migration054_CreatesAppendOnlyItemPriceHistoryAndDecimalCostSnapshots</code> @1456.

## DateConsumerAndFilterBoundaryTests.cs {#src-64faa646b2d8}

<code>Software/tests/GetSeek.IntegrationTests/DateConsumerAndFilterBoundaryTests.cs</code> · SHA-256 <code>dae398613a804e5e1e2cd172ab661aef7409a62f01a4fd42aa60d7bfd69e2ed1</code>.

Located test declarations: <code>StoreTimeSemantics_ConvertsLocalDayToUtcBoundaries_AcrossMultipleTimezones</code> @37, <code>StoreTimeSemantics_DstSpringForward_CoversExact23HourDay</code> @64, <code>StoreTimeSemantics_DstFallBack_CoversExact25HourDay</code> @94, <code>FinancialRegister_ReverseDateRange_ThrowsArgumentException</code> @133, <code>MainViewModel_ResolveCommercialDateRangeUtcAsync_OpenEndedAndReversedRanges</code> @149, <code>ClearCommercialFiltersCommand_ClearsBothBoundaries</code> @188.

## DesktopProductionBootstrapperTests.cs {#src-386de3a7c9e5}

<code>Software/tests/GetSeek.IntegrationTests/DesktopProductionBootstrapperTests.cs</code> · SHA-256 <code>499e47bdd72cade7aa34246d2bebc9b8223e88012ca45109ee7b892acccdc52d</code>.

Located test declarations: <code>SingleRegisterStartup_DoesNotRequireDeviceIdentityFile_AndSurvivesRestart</code> @28, <code>SingleRegisterStartup_PreservesExistingDatabaseRegisterId_WithoutLocalFile</code> @56, <code>ProductionStartup_WithEmptyCatalogAndNoShift_InitializesCleanStateWithoutDemoFixtures</code> @87, <code>TerminalId_SurvivesRestart_AndRemainsStable</code> @119, <code>PersistedCatalogAndStoreConfig_LoadedWithConfiguredDecimals_AndSurviveRestart</code> @157, <code>ActiveShift_StrictlyScopedToDeviceIdentifier</code> @241, <code>StartupFailure_ProducesExplicitErrorState_AndNeverFallsBackToDemo</code> @299, <code>ProductionMode_GuardsPlaceOrder_AndPreventsFinancialExecution</code> @320, <code>ExplicitDemoMode_InitializesSampleDataAndSetsDemoFlag</code> @335, <code>Migration005_RunsOnCleanV4AndExistingV4Database</code> @350, <code>IndependentDeviceIdentity_LocalFileEnsuresDistinctOrStableIdentity</code> @406, <code>CatalogCurrencyMismatch_CausesStartupError_WithSafeMaskedMessage</code> @432, <code>InvalidDecimalPlaces_CausesStartupError_WithSafeMaskedMessage</code> @459, <code>SafeErrorMasking_NeverExposesInternalExceptionsOrFilePaths</code> @480, <code>ProductionMode_GuardsXReportAndProfileToggles</code> @498, <code>ProductionShiftSummary_DisplaysUnavailableForKpis</code> @522, <code>CopiedDatabase_BootedWithDifferentLocalIdentity_AdoptsLocalIdentityAndPreservesHistoricalShifts</code> @540, <code>DoubleReadRestart_ReadsSameSavedCatalogAndBusinessProfileTwice_WithoutMutationOrFixtureLeakage</code> @681, <code>DesktopInteraction_CoversNavigation_GuardedActions_StartupError_AndNoFixtureLeakage</code> @786, <code>MissingLocalIdentity_WithExistingDb_FailsSafelyAndRequiresProvisioning</code> @926, <code>CorruptLocalIdentity_FailsSafelyAndNeverSilentlyOverwrites</code> @1002, <code>SessionUnlock_WithProductionCashierAndSupervisorCredentials_ValidatesCorrectly</code> @1041, <code>OperationalCommands_WhenSessionLocked_AreRejectedAndDoNotExecute</code> @1131, <code>CommandPipeline_WhenSessionIsLocked_ReturnsSessionLockedFailure</code> @1178, <code>BootstrapAsync_LockAndUnlock_WithSafeConnectionLifetime_Succeeds</code> @1222, <code>SessionUnlock_WithOtherActiveUser_IsRejectedAndRemainsLocked</code> @1296, <code>DesktopAndCommandPipeline_ShareSessionState_DirectCommandsRemainBlockedWhileLocked</code> @1380, <code>TerminalTransfer_WhenLocalFileWriteFails_RollsBackDatabaseAndKeepsOriginalIdentity</code> @1467, <code>TerminalTransfer_DeterministicFailureAtCommitPoint_DetectsIncompleteTransferOnStartup_AndRecoversWithSupervisorAuth_CommitTarget</code> @1551, <code>TerminalTransfer_DeterministicFailureAtCommitPoint_RecoversWithSupervisorAuth_RollbackToPrior</code> @1696, <code>NormalBootstrapAsync_WiresOperationalCommandPipeline_SharingSessionContext_BlockingWhenLocked</code> @1783, <code>SessionLockAndStartupError_RenderedInputs_TouchNumpadAndKeyboardEnterKeybinding</code> @1876.

## ExpenseAttachmentIntegrationTests.cs {#src-71ed7b74fb5d}

<code>Software/tests/GetSeek.IntegrationTests/ExpenseAttachmentIntegrationTests.cs</code> · SHA-256 <code>6856af0bc41a0c597a9fe8525e77a0a8ba5202697372a0968c9a33050725d4f0</code>.

Located test declarations: <code>PrepareAttachment_ValidJpegAndPng_ResizesAndProducesBoundedHash</code> @133, <code>PrepareAttachment_CorruptOrNonImageInput_ReturnsExpensePhotoInvalid</code> @166, <code>PrepareAttachment_OversizedStream_ReturnsExpensePhotoTooLarge</code> @180, <code>CreateExpenseRecord_WithAttachment_PersistsAttachmentAtomically</code> @198, <code>SaveAndPayExpense_WhenAccountFundsInsufficient_RollsBackAttachmentAtomically</code> @239, <code>AttachExpensePhoto_SupersedesExistingAttachment_PreservesVersionHistory</code> @277, <code>GetCurrentAttachment_CancelledExpense_ReturnsNull</code> @346, <code>GetCurrentAttachment_WhenSessionLocked_ThrowsUnauthorizedAccessException</code> @379, <code>AttachExpensePhoto_SanitizedAuditPayload_ExcludesImageData</code> @405.

## ExpenseCategoryWorkspaceIntegrationTests.cs {#src-107c13e78206}

<code>Software/tests/GetSeek.IntegrationTests/ExpenseCategoryWorkspaceIntegrationTests.cs</code> · SHA-256 <code>9096fab089cc8becf977f60c4624d7f76a6de985eef3af4b8409712276c39c7c</code>.

Located test declarations: <code>CreateExpenseCategory_DuplicateNameCaseInsensitive_FailsWithCategoryNameExists</code> @145, <code>CreateExpenseCategory_DuplicateCodeCaseInsensitive_FailsWithCategoryCodeExists</code> @167, <code>CreateExpenseCategory_OmittedCode_GeneratesUniqueCodeStartingWithExp</code> @189, <code>UpdateExpenseCategory_StaleRevision_FailsWithStaleRevision</code> @212, <code>UpdateExpenseCategory_DuplicateNameOrCodeOnAnotherCategory_Fails</code> @248, <code>DeactivateUsedExpenseCategory_Succeeds_AndSubsequentExpenseCreationFailsWithCategoryInactive</code> @278, <code>BatchStatus_PreviewAndExecute_DeactivatesAndBumpsRevision</code> @334, <code>BatchStatus_StaleDetection_FailsWithBatchSelectionStale</code> @381, <code>PermissionSeparation_ManageCatalogVsExpensesManage</code> @425, <code>CrossDomainMismatch_ZeroWritesAndRejection</code> @470.

## ExpensePaymentIntegrationTests.cs {#src-aac2d8c7da64}

<code>Software/tests/GetSeek.IntegrationTests/ExpensePaymentIntegrationTests.cs</code> · SHA-256 <code>39fa8e69c74cc40c53370bca4f4a382c32cf11248762b3c9b038f3371c808228</code>.

Located test declarations: <code>PayExpense_PartialAndFullPayments_ProducesCorrectCostVersusOutflows</code> @147, <code>SaveAndPayExpense_AtomicSuccess_CreatesExpenseAndPaymentTogether</code> @232, <code>SaveAndPayExpense_WhenAccountFundsInsufficient_RollsBackCompletely</code> @273, <code>ReverseExpensePayment_RestoresFundsAndRemainingExpenseCost</code> @313, <code>ReplaceExpenseRecord_ReplacesZeroPaidExpenseWithLinkedRecord</code> @393, <code>PayExpense_IdempotentReplay_ReturnsSamePaymentId</code> @474.

## ExpenseRecordIntegrationTests.cs {#src-90dc3c567603}

<code>Software/tests/GetSeek.IntegrationTests/ExpenseRecordIntegrationTests.cs</code> · SHA-256 <code>466973515336103cebffffec7dc5ba1399c325d0743e3c4d6bc0c03b67563176</code>.

Located test declarations: <code>CreateExpenseCategory_ValidInput_CreatesCategoryWithCode</code> @79, <code>CreateExpenseCategory_DuplicateNameOrCode_Rejected</code> @102, <code>UpdateExpenseCategory_WhenValid_UpdatesFieldsWithRevisionCheck</code> @124, <code>CreateExpenseRecord_UnpaidDefault_CreatesRecordWithoutMovingMoney</code> @159, <code>CreateExpenseRecord_InactiveCategory_Rejected</code> @223, <code>UpdateExpenseRecord_WhenUnpaid_CanUpdateAllFields</code> @245, <code>CancelExpenseRecord_WhenUnpaid_CancelsSuccessfully</code> @287, <code>UpdateExpenseRecord_WhenPaid_FinancialFieldsAreImmutable_NotesCanBeUpdated</code> @323, <code>GetExpenses_FilteringAndPaging_SortsByOccurredDateDesc</code> @404.

## ExpensesUiIntegrationTests.cs {#src-addea91c920b}

<code>Software/tests/GetSeek.IntegrationTests/ExpensesUiIntegrationTests.cs</code> · SHA-256 <code>cd08d0d7db1ec5a74885f959de438dbef3135b67f64bef3443212f25633b6fec</code>.

## ExportServiceIntegrationTests.cs {#src-0c1684160e88}

<code>Software/tests/GetSeek.IntegrationTests/ExportServiceIntegrationTests.cs</code> · SHA-256 <code>f079119b50490da97206be44869fc2e089d174159ee0b4c570a4203d253ea9ab</code>.

Located test declarations: <code>ReceiptSelector_UsesCommittedDatabaseInvoiceAndWritesOpaquePdfCopy</code> @76, <code>SalesReportSelector_UsesBoundedDatabaseRowsAndOmitsPrivateIdentifiers</code> @96, <code>InventorySnapshotSelector_UsesDecimalLedgerAndAllowlistedColumns</code> @115, <code>ShiftZReportSelector_UsesCommittedSnapshot</code> @134, <code>ExportPermission_IsRecheckedFromDatabaseAndCallerClaimCannotGrantIt</code> @150, <code>ExportPermission_ExplicitDenyOverridesRoleGrant</code> @167, <code>ExportSelectors_RejectUnboundedDatesAndOversizedLimits</code> @194, <code>EscapeCsvContent_PreservesQuotedCommaQuotesAndMultilineCellsAndNeutralizesFormulas</code> @212.

## ImportDialogsUiIntegrationTests.cs {#src-d0defb48c3d9}

<code>Software/tests/GetSeek.IntegrationTests/ImportDialogsUiIntegrationTests.cs</code> · SHA-256 <code>42bc57debe921ba784d023efa2a146aeb43a0ab48f59fa7be4c7f2617f4e9d15</code>.

## InventoryAndThirdPartiesSearchIntegrationTests.cs {#src-d0fa582a0395}

<code>Software/tests/GetSeek.IntegrationTests/InventoryAndThirdPartiesSearchIntegrationTests.cs</code> · SHA-256 <code>fd999a73ea1ad851f7eb1e5a730d3534fcc740dd6790ee2c7977150dc8b3c252</code>.

Located test declarations: <code>Inventory_PagingSortingAndLifecycleModes</code> @152, <code>Inventory_DuplicateNames_DistinguishedBySku_Barcode_AndExactSelection</code> @203, <code>ThirdParties_Paging_Kind_Barcode_AndExactSelection</code> @250, <code>SelectionScope_ChangesWhenExactSelectionAppliedOrCleared</code> @310.

## InventoryImportIntegrationTests.cs {#src-53277371bffa}

<code>Software/tests/GetSeek.IntegrationTests/InventoryImportIntegrationTests.cs</code> · SHA-256 <code>6a4ee536b09f89298b835b23a1dc8a26b2a999cc47123a08d5b8a1dbb7819a9e</code>.

Located test declarations: <code>MasterDataExportsPreserveIdentifiersAndPrices_AndRejectUnauthorizedUsers</code> @56, <code>BlankSkuCreatesAndLinksStock_CompletedWorkbookUpdatesWithoutRepeatingStock</code> @80, <code>CreatesBarcodeDefaultsUnitsAndNumericTier_WithRollbackOnlyPreview</code> @107, <code>BlankUpdatePreservesPricesBarcodeAndTax_ExplicitClearRemovesBarcode</code> @124, <code>MultiItemPricingUsesUniqueShelfKeys_StockCostPrecedesAutomaticPricing</code> @137, <code>MissingChildOrDuplicateBarcodeRollsBackAllRows</code> @151, <code>NewNestedKitsAreOrderedChildrenFirst_ParentIntakeIsRejected</code> @161, <code>PreviewRejectsChangedStateAndExplicitReceiveDenial</code> @176, <code>TemplateFriendlyModesAndFlexibleCaseAndBooleans_AreAcceptedAndApplied</code> @186, <code>WhitespaceTiersAndSpacedPricingRules_AreAcceptedAndApplied</code> @239.

## InventoryIntegrationTests.cs {#src-afdc78fc3cca}

<code>Software/tests/GetSeek.IntegrationTests/InventoryIntegrationTests.cs</code> · SHA-256 <code>569556b4052701324a704f1235405e2e85a87aca29f8a2f18b9244890641475c</code>.

Located test declarations: <code>DoubleEntry_StockLedger_CalculatesCorrectBalances_And_ThresholdStatuses</code> @93, <code>KitAvailability_UsesAggregatedNestedLeafDemandAndAllLedgerStock</code> @146, <code>SingleShopLedger_IgnoresLegacyLocationInputs</code> @234, <code>SingleShopLedger_CombinesIncomingStockRegardlessOfLegacyDestination</code> @276, <code>LotAndSerialTracking_EnforcesPositiveSerialPresence_AndRejectsNegativeWithoutStock</code> @304, <code>ReceiveStock_CreatesIntakeMovement_AndIncreasesOnHand</code> @353, <code>AdjustStock_NegativeDelta_DecreasesOnHand_AndRejectsInsufficientStock</code> @378, <code>UntrackedItem_RejectsReceiveAndAdjust_WithItemNotTracked</code> @414, <code>PermissionDenial_And_ValidationFailure_CreatesZeroMovements</code> @447, <code>SingleSuccessfulAction_CreatesExactlyOneMovement_MatchingReaderBalance</code> @499, <code>ConcurrentStockAdjustments_WithSeparatePhysicalConnections_InWalMode_MaintainLedgerIntegrity</code> @527, <code>RestartPersistence_MaintainsStockBalances</code> @615.

## InventoryPricingNavigationTests.cs {#src-3887acb35620}

<code>Software/tests/GetSeek.IntegrationTests/InventoryPricingNavigationTests.cs</code> · SHA-256 <code>d32cf11c236769797567aef83582ec1c6ae5c140c5924dad79bdb1c7582ff748</code>.

## InventoryTraceabilityEditorIntegrationTests.cs {#src-d52916d92fa4}

<code>Software/tests/GetSeek.IntegrationTests/InventoryTraceabilityEditorIntegrationTests.cs</code> · SHA-256 <code>f077e85170e3f554de0f4d0838efa0a82848c4dd473c5cccc7bd48d09cfa4296</code>.

Located test declarations: <code>LotsHaveOptionalExpiry_RequireIdentity_AndRejectStaleCorrections</code> @64, <code>SerialsCannotBeAnonymousFractionalDuplicatedOrRemovedWhenSold</code> @87, <code>SerialRemovalIsAtomicAuditedAndIdempotent_AndPermissionsAreLive</code> @111, <code>LotPagingSortsTheWholeDataset_AndProductionExpiryIsOptional</code> @135, <code>ProductionSharesWeightedCostHistoryAndReviewPricing_WithoutChangingPurchaseOrSellingPrices</code> @163, <code>DirectInvoiceReservesUntilPartialDispatch_AndBankPaymentDoesNotMoveStock</code> @213, <code>PurchaseInvoiceAndReceiptAreSeparate_AndCostsRemainNormalized</code> @273.

## InvoiceSettlementIntegrationTests.cs {#src-c97a9646e2a0}

<code>Software/tests/GetSeek.IntegrationTests/InvoiceSettlementIntegrationTests.cs</code> · SHA-256 <code>3a6b48e57b1d80f70ab6ba1378ce54129d109750ca0047c3e8d86aaef9a0f226</code>.

Located test declarations: <code>ReturnReceipt_PreservesOriginalUnitPrice_WhenReturningMultipleUnits</code> @26, <code>InvoiceCreditSort_UsesFullCreditAcrossPages_NotNetAfterPayout</code> @43, <code>HistoricalPrecision_IsSnapshotBound_AndSettingsChangeIsRejected</code> @64, <code>Upgrade068_RecoversSavedPrecision_LeavesMissingHistoricalFactsUnknown</code> @80, <code>DeferredBankDeposit_UsesDesktopConfirmationContract_AndReplaysOnce</code> @95, <code>SerialFinancialReturn_WithoutPhysicalStock_RejectsFractionalUnit</code> @112, <code>NoPayoutReturn_RejectsUnusedBankConfirmation</code> @126, <code>BankCollection_RequiresConfirmation_StoresCanonicalReference_RejectsReuse</code> @137, <code>Discounts_RecordManualAndPromotionSeparately_ReverseOriginalCreditOnly</code> @155, <code>InventoryLoss_ConvertsEnteredUnit_ValuesOnce_AndReplays</code> @175, <code>PartialTrackedReturn_SelectsOneOriginalSerial_InspectionRequiresResolution</code> @190, <code>CollectionReceipts_ReprintSavedFacts_AndClosingSnapshotSeparatesCollections</code> @215, <code>InspectionResolution_ConcurrentConnections_CannotRestockTwice</code> @251, <code>ConcurrentCollections_AreSerializedAcrossPhysicalConnections</code> @266, <code>DeferredIssue_UsesExactTotalAndStockOnce_RejectsWalkIn</code> @284, <code>Readers_UseNewRegistersAndConsistentInvoiceBalances</code> @301, <code>Collections_AllocateBalances_KeepTaxesAndReplayExactlyOnce</code> @315, <code>ReturnCredit_PaysDebtFirst_InspectionCannotResolveTwice</code> @336, <code>NoRefund_DirectTrash_DoesNotDecreaseShelfOrReduceDebt</code> @359, <code>CashLossCorrection_ChangesRegisterOnly</code> @372.

## InvoiceWorkspaceUiTests.cs {#src-9918914a0489}

<code>Software/tests/GetSeek.IntegrationTests/InvoiceWorkspaceUiTests.cs</code> · SHA-256 <code>7ca89013b520966211ca295e34af388f251b88cec3a324bbe02fc7234b0cf317</code>.

## ItemStockHistoryIntegrationTests.cs {#src-a2e2b5d87c25}

<code>Software/tests/GetSeek.IntegrationTests/ItemStockHistoryIntegrationTests.cs</code> · SHA-256 <code>86be21681ed8e8dbd474bee1dff6d7d72ec7cbca882779e08219817b1e217bfd</code>.

Located test declarations: <code>History_UsesOneSnapshotForRowsAndDecimalRunningBalances</code> @14, <code>History_UsesIdTieBreakerAcrossPages_AndRefreshCapturesNewRows</code> @53, <code>TraceabilitySummary_ShowsLotBalancesSerialStatesAndKitsUsingItem</code> @105, <code>CheckoutCostFloor_UsesExactPurchaseUomCostUntilTheFinalSellingUnitRound</code> @148.

## KitAndCheckoutIntegrationTests.cs {#src-a8bf53c268db}

<code>Software/tests/GetSeek.IntegrationTests/KitAndCheckoutIntegrationTests.cs</code> · SHA-256 <code>212d7ab365576adc6f18399e46e57db4e60d5c95909cced8f3f7c559b5be20d3</code>.

Located test declarations: <code>Kit_CycleDetection_RejectsDirectAndTransitiveCycles</code> @85, <code>KitSale_DeductsComponentStock_AndRecordsSalesLineAllocations</code> @140, <code>KitSale_AggregateDemand_RejectsOversellingAcrossDuplicateLines</code> @254, <code>KitSale_InactiveComponent_RejectsCheckout</code> @348, <code>Refund_KitSale_RestocksConstituentComponents</code> @427, <code>Kit_ParentStockMustBeZero_RejectsKitConfigurationWhenStockOnHandGreaterThanZero</code> @529, <code>KitAndBom_MutualExclusivity_BlocksKitOnItemWithBom_AndBlocksBomOnItemWithKit</code> @568, <code>ProductionRun_RejectsExecutionWhenOutputItemIsConfiguredAsKit</code> @617, <code>Kit_QuantityGuard_RejectsDirectStockIntakeAndAdjustment_WhileKitIsActive</code> @680, <code>Kit_WhenDeactivated_BecomesEditableAgainBySystemAndUser</code> @743, <code>KitSale_EachUnitSold_ConsumesOneUnitOfChildBundle</code> @802, <code>NestedKit_MultiLevelDecomposition_CalculatesExactStockDeductionAndIntake</code> @900.

## ManufacturingExecutionEnhancementIntegrationTests.cs {#src-8e7c1eae801f}

<code>Software/tests/GetSeek.IntegrationTests/ManufacturingExecutionEnhancementIntegrationTests.cs</code> · SHA-256 <code>1763df25d14e717e7a2dcd9f4c9f3c466054daae2aab20c4f3af46a077e511aa</code>.

Located test declarations: <code>Draft_Stage_And_Complete_ProductionRun_Lifecycle</code> @66, <code>ProductionRun_ExplicitLot_Required_When_Ingredient_Tracked_By_Lot</code> @166, <code>ProductionRun_ExpiredLot_Rejected</code> @238, <code>ProductionRun_CancelDraft_Succeeds_AndRejectsCompletingCancelled</code> @301.

## ManufacturingIntegrationTests.cs {#src-679757e25f33}

<code>Software/tests/GetSeek.IntegrationTests/ManufacturingIntegrationTests.cs</code> · SHA-256 <code>e1e18e01b6ee727cc5d24054689d93d4b61888b5e7efcb8b5b7d7d57dbb4f749</code>.

Located test declarations: <code>Bom_CreateAndVersionUpdate_SucceedsAndTracksVersionIncrement</code> @68, <code>Bom_CycleDetection_RejectsDirectAndTransitiveRecipeLoops</code> @142, <code>Bom_RejectsInactiveIngredient</code> @200, <code>ExecuteProductionRun_ConsumesIngredients_ProducesFinishedStock_BalancesDoubleEntryMovements</code> @237, <code>ExecuteProductionRun_InsufficientIngredientStock_FailsAndRollsBackWithoutMutations</code> @372, <code>ExecuteProductionRun_UnauthorizedOperator_IsDeniedByRbacPermissionCheck</code> @452.

## ManufacturingUiIntegrationTests.cs {#src-38dc0821b775}

<code>Software/tests/GetSeek.IntegrationTests/ManufacturingUiIntegrationTests.cs</code> · SHA-256 <code>86d4574dffc04dc87ed0eb1b82157c5b581f1aded4a3bf87f4651dabde4b5bf8</code>.

## ManufacturingWorkspaceReaderTests.cs {#src-4a05e3bbbe9f}

<code>Software/tests/GetSeek.IntegrationTests/ManufacturingWorkspaceReaderTests.cs</code> · SHA-256 <code>c76c5be0b09b462f401ec2247266e7fead25faaad300628d47cbff4fd06d30ea</code>.

Located test declarations: <code>GetRecipesAsync_WithOver40Rows_PaginatesCorrectly_AndPopulatesIngredientsOnLaterPages</code> @134, <code>GetRecipesAsync_SortingCyclesAndDefaults_OrdersDeterministically</code> @191, <code>GetRecipesAsync_FiltersByActive_IngredientExists_OutputItem_ExactId_AndSearch</code> @264, <code>GetProductionRunsAsync_WithOver40Rows_PaginatesAndSeparatesWipFromHistory</code> @340, <code>GetProductionRunsAsync_SortingCyclesAndDefaults_HandlesDeterministicTiesAndUnknownCreationDates</code> @418, <code>ExactIdDetailReads_HydratesFullDetails_OrReturnsNull</code> @490, <code>PermissionsAndSessionEnforcement_ThrowsWhenLockedOrLackingPermission</code> @553, <code>SearchSuggestions_EnforcesEligibilityRules_NoHiddenOrIneligibleSuggestions</code> @620.

## MasterDataAndInventoryClosureIntegrationTests.cs {#src-e6d0c2b1e844}

<code>Software/tests/GetSeek.IntegrationTests/MasterDataAndInventoryClosureIntegrationTests.cs</code> · SHA-256 <code>00164e2c2148ba64d4e62fb340ea1a6ad97c1c96bb2420f60d749b10c1ffdd6c</code>.

Located test declarations: <code>LegacyItemLocations_DoNotConstrainSingleShopStockLedger</code> @83, <code>SupplierRegistry_CreateEditDeactivate_And_ReceiptLinkingWithSnapshotPreservation</code> @164, <code>Checkout_UsesCanonicalSingleShopLedger_IgnoringLegacyLocationEligibility</code> @251.

## MasterDataOperatorUiIntegrationTests.cs {#src-abf5e4f8ac09}

<code>Software/tests/GetSeek.IntegrationTests/MasterDataOperatorUiIntegrationTests.cs</code> · SHA-256 <code>cd22e9d032f63ed70d3c7dfd9dbfca96e4570e1981a3ec08a5844f1dbc85033e</code>.

Located test declarations: <code>SupplierOperatorWorkflow_ThirdPartyCreateEditDeactivate_UpdatesStateAndReceiptDropdowns</code> @70, <code>FacilitiesAndBinsOperatorWorkflow_CreateEditDeactivate_PersistsAndLoadsCorrectly</code> @131, <code>UnauthorizedUser_DeniedFromThirdPartyAndFacilityOperations</code> @413, <code>TeamsView_ClickTerminalSecurityPin_OpensChangePinModal_AndUpdatesPinInSqlite</code> @480.

## ModalActionBarLayoutTests.cs {#src-b78d2a25613f}

<code>Software/tests/GetSeek.IntegrationTests/ModalActionBarLayoutTests.cs</code> · SHA-256 <code>454b3023a7e221f0e3f00bd17197a67f9c34d7506e501d40bdc759ede5e8976a</code>.

## ModalCoordinatorTests.cs {#src-97b728aa7a07}

<code>Software/tests/GetSeek.IntegrationTests/ModalCoordinatorTests.cs</code> · SHA-256 <code>b2e3c6774f18b04a6cee9b9e822c65d05963af093b0a4f4b5466170d6fe6995f</code>.

Located test declarations: <code>EscapeDismissesOnlyTheVisibleTopmostSurface</code> @9, <code>NonDismissibleTopSurfaceConsumesEscapeWithoutDismissingUnderlyingSurface</code> @27, <code>ClosedAndUnregisteredSurfacesAreIgnored</code> @43.

## NumericInputLayoutTests.cs {#src-1fa4ee9ae7db}

<code>Software/tests/GetSeek.IntegrationTests/NumericInputLayoutTests.cs</code> · SHA-256 <code>4b64b9676f691d24e6d86c152cb2e5260bda3c50eadb0dff1a57fd336146138c</code>.

## OperatorProvisioningIntegrationTests.cs {#src-f851df10c75c}

<code>Software/tests/GetSeek.IntegrationTests/OperatorProvisioningIntegrationTests.cs</code> · SHA-256 <code>bc6fdf66940363da0139539799be1e917ef6252473d74fc33d2c6e133d4145a0</code>.

Located test declarations: <code>Bootstrap_WhenEmptyDatabase_EntersFirstRunSetup_AndAllowsInitialAdminCreation</code> @74, <code>ProvisionInitialAdmin_WhenConcurrentSetupAttempts_ProducesExactlyOneAdmin</code> @137, <code>PrivilegeEscalation_And_RoleValidation_StrictlyEnforced</code> @226, <code>ExhaustiveCredentialLeakageTest_AbsenceFromAudit_Deduplication_Logs_Errors_AndSerializedResults</code> @331, <code>ShiftValidation_EnforcedAtDomainBoundary</code> @424, <code>FullRenderedSetupWorkflow_ClickThrough_Setup_StaffCreation_ShiftOpen_AndSale</code> @525, <code>DynamicOnShiftUnlock_WithoutRestart_AndOffShiftDenial</code> @640, <code>OpenShift_ForCashier_PersistsActiveShiftAndSurvivesAppRestart</code> @715.

## PayrollMonthSelectorIntegrationTests.cs {#src-e56fcecc6498}

<code>Software/tests/GetSeek.IntegrationTests/PayrollMonthSelectorIntegrationTests.cs</code> · SHA-256 <code>3d89c0ab6320bff4146953aa24ac4554f5b96318ef952d1dbf4913a5b3309ef4</code>.

## PeopleSalaryIntegrationTests.cs {#src-0843d3507557}

<code>Software/tests/GetSeek.IntegrationTests/PeopleSalaryIntegrationTests.cs</code> · SHA-256 <code>9821473a0129a12eb655b861681125527dac484e37ca9fe98daab814280570eb</code>.

Located test declarations: <code>CreatePerson_SalaryOnlyWithoutUser_CreatesPersonRecordWithNoUserOrRole</code> @84, <code>CreatePerson_DuplicateDisplayName_AllowedAndGeneratesDistinctCodes</code> @137, <code>CreatePerson_ExplicitCodeCollision_Rejected</code> @172, <code>CreatePerson_LinkToUser_ValidAndDuplicateLinksEnforced</code> @199, <code>UpdatePerson_StaleRevision_Rejected</code> @256, <code>SaveSalaryAgreement_AppendAndOverrideTerms_IncrementsPersonRevision</code> @299, <code>CreateUserWithPerson_AtomicCreation_WhenAuthorized_CreatesBoth</code> @351, <code>CreateUserWithPerson_WhenSalaryManagePermissionDenied_RollsBackBoth</code> @392, <code>CreateUserWithPerson_WhenDatesInvalid_RollsBackBoth</code> @432, <code>SqliteSalaryReader_WhenPermissionDenied_ThrowsUnauthorizedAccessException</code> @456.

## PermissionEnforcementTests.cs {#src-c0c0149d624f}

<code>Software/tests/GetSeek.IntegrationTests/PermissionEnforcementTests.cs</code> · SHA-256 <code>cb2063e65898b70db08476b94e7942a118a005dde67803174ee1f212ef313a63</code>.

Located test declarations: <code>UnauthenticatedUser_EvenWithOpenShift_IsDeniedInCommandPipeline</code> @57, <code>UnauthorizedCaller_MissingPermission_IsDeniedInCommandPipeline</code> @101, <code>UnauthenticatedQuery_ThrowsUnauthorizedException</code> @145.

## PopulatedWorkspacesLayoutAndContainmentTests.cs {#src-685a3261a988}

<code>Software/tests/GetSeek.IntegrationTests/PopulatedWorkspacesLayoutAndContainmentTests.cs</code> · SHA-256 <code>b3cdfa93c06ae74a10126313eea2e22ae9e69e1a240c8c5d3b3188ee9ebaafab</code>.

## PosChromeUiIntegrationTests.cs {#src-20e8711e527a}

<code>Software/tests/GetSeek.IntegrationTests/PosChromeUiIntegrationTests.cs</code> · SHA-256 <code>ae3a65a6cc63e2ce347a737d00472e066fa3e750adc86a9c166f530738291561</code>.

## PriceOfferCommandsIntegrationTests.cs {#src-91e58da935f0}

<code>Software/tests/GetSeek.IntegrationTests/PriceOfferCommandsIntegrationTests.cs</code> · SHA-256 <code>958759d5814f7c69055763426e1a6c54cbeaf62a2d6bbae230b3209520370c20</code>.

Located test declarations: <code>OfferCreateUpdateAndStatusRequireCurrentVersionAndPersistDecimalTerms</code> @24.

## PricingAndActivitySearchIntegrationTests.cs {#src-3e4d859110e7}

<code>Software/tests/GetSeek.IntegrationTests/PricingAndActivitySearchIntegrationTests.cs</code> · SHA-256 <code>7527120b957c0f2d850c3420f9dab9f320b98b63c29b04914d3c920cfb90903e</code>.

Located test declarations: <code>PricingSearch_ReturnsSuggestions_AndEnforcesPermissions</code> @106, <code>ActivitySearch_ReturnsSuggestions_AndEnforcesPermissions</code> @142, <code>ViewModel_PricingAndActivitySearch_FiltersProperly</code> @178.

## PricingMassRunDurabilityIntegrationTests.cs {#src-36d032d6aafc}

<code>Software/tests/GetSeek.IntegrationTests/PricingMassRunDurabilityIntegrationTests.cs</code> · SHA-256 <code>73326240253c9ba379b3d0fd769ca81d463f3c7d2321bfac81efc19476340444</code>.

Located test declarations: <code>PricingRun_FreezesScopeRejectsChangedItemsAndConflictingIdempotency</code> @31, <code>MultiTierRun_PreviewProtectsTierInputsAndAppliesDynamicTier_WhileAutomaticRunUsesSavedFormula</code> @189.

## ProductManagementIntegrationTests.cs {#src-23dddd3ee312}

<code>Software/tests/GetSeek.IntegrationTests/ProductManagementIntegrationTests.cs</code> · SHA-256 <code>705363502e80d93a70d8de732f451ac1614495f10037a74823d08063e1787c69</code>.

Located test declarations: <code>ProductStockDraftCommitsIndividualMovements_AndInvalidDraftRollsBackProduct</code> @137, <code>ReassigningCategoryForFollowingItemCreatesReviewProposal</code> @190, <code>RegistryDelete_RejectsBuiltInAndReferencedDefinitions_ButRemovesUnusedMerchantDefinitions</code> @238, <code>RegistryBatchDelete_RequiresFreshPreviewAndDeletesOnlyUnusedDefinitions</code> @296, <code>ProductCoordinates_AreOptionalAndDoNotAffectLedgerStock</code> @358, <code>CreateProduct_Succeeds_ForFood_Ingredient_AndService</code> @390, <code>ProductPurpose_RawAndUnclassifiedItems_AreExcludedFromCatalogAndDirectSale</code> @461, <code>BuyingPriceOverride_IsEditableAndNextCommittedReceiptBecomesEffectiveSource</code> @537, <code>ProductCreate_RejectsNonInventoryCategoryInactiveUnitAndUnknownPurpose</code> @603, <code>ZeroPriceFinishedProduct_CheckoutRequiresExplicitFreeSaleAndCreatesNoTender</code> @630, <code>CreateProduct_RejectsDuplicateSku_CaseInsensitive</code> @694, <code>CreateAndEditProduct_RequiresManageCatalogPermission</code> @726, <code>UpdateProduct_PreservesHistoricalInvoices_WhenPriceChanges</code> @746, <code>ProductMetadataSave_PreservesAutomaticPrice_UntilExplicitPriceEditSwitchesToManual</code> @827, <code>ProductConfiguration_SaveIsAtomicAcrossProductKitAndPrimaryBarcode</code> @962, <code>ProductConfiguration_FollowsOnlyTheConfirmedCurrentCategoryRule</code> @1057, <code>DeactivateProduct_HidesFromCatalog_AndPreservesAuditTrail</code> @1124.

## ProductionModalModeTests.cs {#src-d50e40ef4b6f}

<code>Software/tests/GetSeek.IntegrationTests/ProductionModalModeTests.cs</code> · SHA-256 <code>59557bbce1f3b9873638434a48c2539db42b271970f441c51f3718b39e0140fa</code>.

Located test declarations: <code>NewMode_SaveDraft_CreatesPlannedRun_WithCreatedAt_AndNoInputDeduction</code> @92, <code>NewMode_CompleteNow_DeductsInputs_OutputsStock_AndMarksCompleted</code> @133, <code>StartMode_StagesRun_DeductsInputsToWip_HidesSaveDraft</code> @159, <code>FinishMode_CompletesRun_CreditsOutputStock_NoDuplicateInputDeduction</code> @194, <code>ReadOnlyMode_CompletedOrCancelledRuns_ForceReadOnly_CloseOnly_CannotExecute</code> @238, <code>PermissionEnforcement_ManageOnly_CanSaveDraftAndStart_CannotExecuteOrFinish</code> @273, <code>PermissionEnforcement_ExecuteOnly_CannotSaveDraftOrStart_CanCompleteAndFinish</code> @304, <code>DirtyTracking_EscapeAndScrimDismissalGuard</code> @322.

## ReceiptAndFinancialRegisterSearchIntegrationTests.cs {#src-0e7f3f3308c0}

<code>Software/tests/GetSeek.IntegrationTests/ReceiptAndFinancialRegisterSearchIntegrationTests.cs</code> · SHA-256 <code>e2805ffb9ccea189329cdfbe46b017facc3ea4e17646d16d210a0e46bf8c0a35</code>.

Located test declarations: <code>SqliteSearchSuggestionReader_Receipts_PermissionAndSuggestions</code> @146, <code>SqliteSearchSuggestionReader_FinancialRegister_ScopeAndSuggestions</code> @193.

## ReceiptDesignPreviewUiIntegrationTests.cs {#src-e63500136e2b}

<code>Software/tests/GetSeek.IntegrationTests/ReceiptDesignPreviewUiIntegrationTests.cs</code> · SHA-256 <code>b521fce968ebe85850c4796355551af737b343d16a2d899c917ea15f8044d453</code>.

## ReceiveStockIntakeIntegrationTests.cs {#src-30ae6688c23b}

<code>Software/tests/GetSeek.IntegrationTests/ReceiveStockIntakeIntegrationTests.cs</code> · SHA-256 <code>d8eaac2f916d93e1f913e3236efa32eedd3b6ee596649005fdce2da3ba083237</code>.

Located test declarations: <code>LotIntake_PostsOneMovementPerLine_UsesOptionalExpiry_AndReusesExistingLot</code> @139, <code>LotIntake_WithMissingLotNumber_FailsAndRollsBackEntireBatch</code> @194, <code>SerialIntake_WithDuplicateSerialInBatch_FailsAndRollsBack</code> @220, <code>SerialIntake_WithSerialAlreadyRegistered_FailsAndRollsBackEarlierLines</code> @245, <code>SerialIntake_WithHeaderQuantityNotMatchingSerialLines_FailsWithCountMismatch</code> @281, <code>SerialIntake_RegistersEachSerialAndPostsOneUnitPerLine</code> @299.

## RecipeSearchIntegrationTests.cs {#src-8413c4f9e395}

<code>Software/tests/GetSeek.IntegrationTests/RecipeSearchIntegrationTests.cs</code> · SHA-256 <code>f0440be97a5103555165caf9348a508100c3dbda2aad5be0c33dfee5dc490c43</code>.

Located test declarations: <code>RecipeOutputs_And_RecipeIngredients_EnforceDistinctEligibility_AndKitsExclusion</code> @104, <code>RecipeOutput_And_RecipeIngredient_SearchStates_RetainSelection_AndPopulateDrafts</code> @146.

## RenderUiScreenshots.cs {#src-a24d12786f3c}

<code>Software/tests/GetSeek.IntegrationTests/RenderUiScreenshots.cs</code> · SHA-256 <code>930fe4c5a7196d92c5ff5c037a898ce0141f8c13fd1a657da43b887490179351</code>.

## ReportAndShiftCloseIntegrationTests.cs {#src-288a666d19a1}

<code>Software/tests/GetSeek.IntegrationTests/ReportAndShiftCloseIntegrationTests.cs</code> · SHA-256 <code>7437819a19c062912c328286af00afb4a8d5420bcc46fce029946d5a8085eb2c</code>.

Located test declarations: <code>GetXReport_ActiveShiftWithSalesDiscountsTaxesAndRefund_ComputesAuthoritativeKpis</code> @68, <code>RefundInLaterShift_ReconcilesCashOutflowWithoutErasingOriginalShiftGrossSales</code> @185, <code>ShiftClose_WithVariance_EnforcesSupervisorElevationAndReason</code> @270, <code>GetZReport_ReturnsImmutableFrozenSnapshotEvenAfterSubsequentActivity</code> @319, <code>ReportQueriesAndCommands_EnforceRbacPermissions</code> @368.

## RestaurantOrderLifecycleIntegrationTests.cs {#src-3546dcf69070}

<code>Software/tests/GetSeek.IntegrationTests/RestaurantOrderLifecycleIntegrationTests.cs</code> · SHA-256 <code>9e148937c8a176241db0a6322e22d86f2e2ed2bfdea3fdf83a5365a958dc86ad</code>.

Located test declarations: <code>CreateAndSendToKitchen_PersistsOrderAndEnqueuesKitchenTicket</code> @91, <code>StatusProgression_SentToKitchen_To_Preparing_Ready_Served</code> @149, <code>CancelOrder_EnqueuesCancellationTicketAndMarksVoided</code> @189, <code>SettleOrder_LinksInvoiceAndSetsSettled</code> @227, <code>RestaurantOrderReader_QueriesActiveOrdersInShiftAndFullOrderDetails</code> @276, <code>AuthorizedSupervisor_CanResolveUnpaidRestaurantOrder_WithAuditAndCancellationNotice</code> @312.

## SalaryEligibilityAndExpensePresetMigrationTests.cs {#src-94fb4b3614ed}

<code>Software/tests/GetSeek.IntegrationTests/SalaryEligibilityAndExpensePresetMigrationTests.cs</code> · SHA-256 <code>d793ba7041247c6643b7ff5b717ee947d3154ec107c5f526504c8e9cd7179073</code>.

Located test declarations: <code>CleanDatabase_MigrateToLatest_AppliesMigration082Successfully</code> @14, <code>UpgradeFromV81ToV82_ExistingAgreementsDefaultToEnabled</code> @79, <code>SalaryEligibility_ZeroEnabled_Versus_DisabledSalary_AreDistinct</code> @138, <code>ExpensePresets_IdempotentReapplication_PreservesCustomNamesEditsAndInactiveStatus</code> @215.

## SalaryExpenseAuditRegressionTests.cs {#src-ebeeb512c897}

<code>Software/tests/GetSeek.IntegrationTests/SalaryExpenseAuditRegressionTests.cs</code> · SHA-256 <code>fe1c1736f294cfce8f74f63fa32b97bfedc1b013c3b5c0c804ceada68fe1240f</code>.

Located test declarations: <code>Followup_FirstMonthOpening_IsIncludedInForecastAndStatement</code> @301, <code>Followup_PriorMonthAdvanceReturned_StatementMatchesCurrentMonthReader</code> @330, <code>Followup_OpeningCarriesOnce_AndCurrentCorrectionIsFrozen</code> @356, <code>Followup_OpeningAndClose_PreserveMoneyScale</code> @378, <code>Followup_ExcessiveDeduction_IsRejectedWithoutChangingDraft</code> @407, <code>Followup_ChangesInvalidatingExistingDeduction_RollBack</code> @425, <code>Followup_HeaderOnlyPng_SaveAndPayIsRejectedWithoutFinancialEffects</code> @469, <code>Followup_FakePngWithIendWithoutIdat_SaveAndPayIsRejectedWithoutFinancialEffects_A07</code> @491, <code>Followup_N02_FrozenStatementSnapshot_ProvenanceAndReconstruction</code> @542, <code>Followup_N01_TrackingStartValidation_RejectsInvalidDraftAndPreservesHistory</code> @610, <code>Followup_R20c_ExistingInvalidDraftData_ReturnsTypedDiagnosticWithoutThrowing</code> @652, <code>DraftAdvanceForecast_DoubleSubtracted_DemonstratesDefect</code> @685, <code>SalaryPayment_ExplicitReadMoneyDeny_MustBlockPayment</code> @707, <code>SaveAndPayExpense_ExpensesManageDeny_MustBlockExecution</code> @726, <code>SalaryPayment_CurrencyMismatch_MustBeRejected</code> @755, <code>BankReversal_RequiresExternalReference_FailsContractWithoutIt</code> @787, <code>CommandKey_PayloadMismatch_MustFailConflict</code> @810, <code>PaySalary_DisabledPerson_MustAllowSettlingExistingDebt</code> @834, <code>SaveSalaryAgreement_FutureTrackingStart_MustNotThrowSqlSchemaError</code> @864, <code>ZeroNetMonth_Finalize_SucceedsWithoutZeroLedgerMovement</code> @888, <code>ExpenseAttachment_ForgedNonImageBytes_MustBeRejected</code> @916, <code>SalaryPayment_IndividualPermissionDenials_LeaveZeroSideEffects</code> @938, <code>SaveAndPayExpense_IndividualPermissionDenials_LeaveZeroSideEffects</code> @974, <code>CreateUserWithPerson_IndividualPermissionDenials_EnforcesAtomicRollback</code> @1015, <code>PermissionRevocation_BeforeReplay_BlocksCachedResult</code> @1054, <code>ExpensePayment_CurrencyMismatch_MustBeRejected</code> @1084, <code>ExpensePayment_ScaleMismatch_MustBeRejected</code> @1128, <code>SaveAndPayExpense_CurrencyMismatch_MustBeRejected</code> @1172, <code>InvalidDecimalPlaces_MustBeRejected</code> @1210, <code>SaveSalaryAgreement_CurrencyChangeWithUnsettledBalance_MustBeBlocked</code> @1236, <code>SaveSalaryAgreement_CurrencyChangeWithUnfinalizedPriorTrackingMonth_MustBeBlocked</code> @1260, <code>PayAdvance_DisabledPerson_MustBeRejected</code> @1278, <code>SaveSalaryAgreement_DisabledPerson_MustBeRejected</code> @1302, <code>UpdatePersonWithAgreement_FailedAgreementRate_LeavesProfileUnchanged</code> @1326, <code>UpdatePersonWithAgreement_KindStatusLink_RoundTripsCorrectly</code> @1369, <code>PaySalary_CallerPaidAtOverride_MustBeRejected</code> @1430, <code>PayExpense_CallerPaidAtOverride_MustBeRejected</code> @1461, <code>FinalizeSalaryPeriod_BeforeLocalPeriodEnded_MustBeRejected</code> @1491, <code>FinalizeSalaryPeriod_BeforeTrackingStartMonth_MustBeRejected</code> @1508, <code>FinalizeSalaryPeriod_UnfinalizedEarlierEligibleTrackingMonth_MustBeRejected</code> @1525, <code>StoreTimeHelper_InvalidOrUnrecognizedTimeZone_FallsBackToUtcWithoutCrash</code> @1542, <code>FinalizeSalaryPeriod_CreatesImmutableStatement_RemainsUnchangedAfterLaterChanges</code> @1558, <code>LegacySalaryPeriod_WithoutStatementJson_ReturnsIncompleteStatementSnapshot</code> @1632, <code>FinalizeSalaryPeriod_ZeroNetEarnings_FinalizesSuccessfullyWithoutZeroLedgerCredit</code> @1663, <code>SalaryProjection_AllowListedSortingAndPaging_SortsDeterministically</code> @1702, <code>SalarySummaries_MultiCurrencyGroups_AggregatesWithoutTruncation</code> @1726, <code>SalaryMonthRow_ProvidesCurrentFinalizedAvailableToPayAndPersonRevision</code> @1759, <code>SalaryPaymentReversal_Bank_RequiresUniqueReference_AndRejectsMissingOrDuplicate</code> @1783, <code>SalaryPaymentReversal_Cash_RequiresCurrentShift_AndRejectsMissingShift</code> @1835, <code>ExpensePaymentReversal_Bank_RequiresUniqueReference_AndRejectsMissingOrDuplicate</code> @1872, <code>ExpensePaymentReversal_Cash_RequiresCurrentShift_AndRejectsMissingShift</code> @1930, <code>SalaryAndExpensePayment_MoneyPolicy_Scale0_Scale2_Scale4_ConvertsAccurately</code> @1972, <code>PayExpense_Scale0AndScale4_ExecutesSuccessfullyWhenMatched</code> @1995, <code>SqliteExpenseReader_AllowListedSorting_SortsCorrectly</code> @2047, <code>SalaryHistory_InDetailModal_LoadsLedgerEntriesChronologically</code> @2112, <code>PersonForm_DirtyTracking_And_DiscardModal_Lifecycle</code> @2164, <code>ExpenseForm_DirtyTracking_And_DiscardModal_Lifecycle</code> @2207, <code>ResetFinancialWorkspace_ResetsSalaryAndExpenseState_AndClosesModals</code> @2250, <code>CentralBlockingDialog_EncompassesAllSalaryAndExpenseModals</code> @2287, <code>GenerationInvalidation_DiscardsStaleDataLoad_AcrossReset</code> @2339, <code>ExpenseAttachment_ForgedDescriptor_MismatchedDimensions_MustBeRejected</code> @2375, <code>ExpenseAttachment_WrongSignature_FakeJpeg_MustBeRejected</code> @2401, <code>ExpenseAttachment_OversizedOutput_MustBeRejected</code> @2426, <code>ExpenseAttachment_MutationAfterPreparation_DetectsChecksumMismatch</code> @2453.

## SalaryExpenseResetIntegrationTests.cs {#src-8957d25553b8}

<code>Software/tests/GetSeek.IntegrationTests/SalaryExpenseResetIntegrationTests.cs</code> · SHA-256 <code>8af97e25e5c15239f55f9dfbae7ac15e912257f9662eed75a3ac4958b1ea1e46</code>.

Located test declarations: <code>AllBusinessData_Includes_People_SalaryHistory_And_Expenses</code> @77, <code>DependencyEnforcement_SalaryHistoryPayments_RequiresOperationalHistory</code> @85, <code>DependencyEnforcement_ExpensePayments_RequiresOperationalHistory</code> @147, <code>DependencyEnforcement_PeopleAndAgreements_RequiresSalaryHistory_AndReferencedExpenses</code> @206, <code>Reset_SalaryHistory_RetainingPeople_RebasesTrackingStartMonth</code> @262, <code>Reset_Expenses_ClearsRecordsAndRestoresBuiltInCategories</code> @342, <code>DemoDataSeeder_SeedsAndResets_SalaryAndExpenses_InDisposableDemo</code> @412, <code>Reset_SalaryHistory_WithConfiguredStoreTimezone_RebasesTrackingStartMonthToStoreLocalMonth</code> @467, <code>RetainedAgreements_AfterReset_StartsCleanWithoutPhantomCarriedAmounts</code> @522.

## SalaryExpenseUiMeasuredLayoutTests.cs {#src-fee0d0fa72b6}

<code>Software/tests/GetSeek.IntegrationTests/SalaryExpenseUiMeasuredLayoutTests.cs</code> · SHA-256 <code>032775c52f8f958ea92b87de292cebb8f5687b790bf82476594cf3ba2ec614b0</code>.

## SalaryExpensesSchemaTests.cs {#src-ca9bf8db2b9f}

<code>Software/tests/GetSeek.IntegrationTests/SalaryExpensesSchemaTests.cs</code> · SHA-256 <code>a409a6aa49211a5b2d651e515d646a5d0dd92f6dddbff836ec632f8058a89e24</code>.

Located test declarations: <code>FreshDatabase_MigratesToVersion83Successfully</code> @26, <code>SchemaConstraints_Migration083_ZReportAndWasteSettings_Enforced</code> @39, <code>SchemaConstraints_Migration081_StatementColumnsAndUniqueness_Enforced</code> @86, <code>SchemaConstraints_PeopleAndAgreements_Enforced</code> @242, <code>SchemaConstraints_SalaryPeriodsAndLedger_Enforced</code> @345, <code>SchemaConstraints_ExpensesAndAttachments_Enforced</code> @421, <code>PermissionsAndRoles_SeededCorrectly_AndExplicitDenyWins</code> @461.

## SalaryExpensesSearchIntegrationTests.cs {#src-3d9ae137f57e}

<code>Software/tests/GetSeek.IntegrationTests/SalaryExpensesSearchIntegrationTests.cs</code> · SHA-256 <code>c9a6ba7bc2e8d4357b8ec1e334aa7fed4d503d6daa338731547bb8b43a265dbb</code>.

Located test declarations: <code>SalaryPeopleSearch_RequiresSalaryReadPermission</code> @134, <code>ExpensesSearch_RequiresExpensesReadPermission</code> @174, <code>SalaryPeopleSearch_RespectsActiveScopeAndRanking</code> @215, <code>ExpensesSearch_RespectsCategoryAndStateScope</code> @255, <code>MoneyAccountsSearch_MasksSalaryDetailsWhenLackingSalaryRead</code> @291, <code>SearchUsageStore_RecordsUseAndBoostsRanking</code> @335, <code>InvalidScope_ThrowsArgumentException</code> @376.

## SalaryExpensesUiTests.cs {#src-05e4f8b1b339}

<code>Software/tests/GetSeek.IntegrationTests/SalaryExpensesUiTests.cs</code> · SHA-256 <code>0c00f067b3b648247a9dd1ff21dc2cba67feeebb4ce500a5045cd73a8ae728ea</code>.

Located test declarations: <code>S14_1_ThreeLanguageLocalizationParity_AllKeysPresentAndNonEmpty</code> @41.

## SalaryPaymentIntegrationTests.cs {#src-7a621ae23a62}

<code>Software/tests/GetSeek.IntegrationTests/SalaryPaymentIntegrationTests.cs</code> · SHA-256 <code>dbfa9e3f7d171500cb3acfe1cb6cabbd060281b9e7aba6a3d2fd795b28959d4e</code>.

Located test declarations: <code>PayAdvance_ValidRequest_DeductsFromAccount_CreatesPaymentAndLedgerDebit</code> @152, <code>PayAdvance_AgainstFutureEarnings_SucceedsEvenWhenNoFinalizedBalance</code> @246, <code>PaySalary_WhenRequestedExceedsFinalizedBalance_FailsWithSalaryFinalizedBalanceInsufficient</code> @297, <code>PaySalary_WhenFinalizedBalanceAvailable_SucceedsAndDeductsFromFinalizedBalance</code> @340, <code>PaySalary_ArrearsPaidAcrossMonths_CannotDoublePaySettledBalance</code> @418, <code>ReverseSalaryPayment_RestoresAccountAndLedgerBalance</code> @484, <code>SalaryPayment_IdempotentReplay_ReturnsSamePaymentIdWithoutDuplicateOutflow</code> @605, <code>SalaryPayment_StaleRevision_Rejected</code> @670, <code>SalaryPayment_InsufficientAccountFunds_FailsWithInsufficientAccountFunds</code> @699.

## SalaryPeriodIntegrationTests.cs {#src-d75e1dd5716a}

<code>Software/tests/GetSeek.IntegrationTests/SalaryPeriodIntegrationTests.cs</code> · SHA-256 <code>2f45a3dec2fa2995f7aa1e716192610670e80db0bf8776bf994dff6ed12ea5a1</code>.

Located test declarations: <code>MissingDraftPeriod_ProjectedWithoutWritingToDatabase</code> @88, <code>AdjustmentsAndUnpaidDays_CalculatedIntoDraftEarnings</code> @123, <code>FinalizeSalaryPeriod_BeforePeriodEnded_Rejected</code> @195, <code>FinalizeSalaryPeriod_WhenPreviousEligiblePeriodOpen_RejectedWithPreviousPeriodOpen</code> @225, <code>FinalizeSalaryPeriod_ChronologicalSuccess_CreatesSingleLedgerCreditAndFreezesSnapshot</code> @255, <code>OpeningBalanceAndCorrections_RecordIntoLedgerWithRevisionGuards</code> @338.

## SalaryUiIntegrationTests.cs {#src-ed1d73fc35fd}

<code>Software/tests/GetSeek.IntegrationTests/SalaryUiIntegrationTests.cs</code> · SHA-256 <code>d6f84b0f73da2c08a35cb99475681f33f41c761829d77d43b2d89ba5705b2e8c</code>.

## SearchBomAuditRegressionTests.cs {#src-2b5dfccc5d4a}

<code>Software/tests/GetSeek.IntegrationTests/SearchBomAuditRegressionTests.cs</code> · SHA-256 <code>51a6cff30f83d7fe356149deffe670c63d4bfe6d0aa4f1efac4d698438a6e6ec</code>.

Located test declarations: <code>R01_1_OldQueryPending_TypeNewTextWithoutFlush_OldOptionNeverAvailableUnderNewText</code> @108, <code>R01_2_RealSeededOperator_WithInvoiceRead_AndPurchaseReadExplicitlyDenied_YieldsNoPurchaseOrSupplierMetadata</code> @134, <code>R01_4_AcceptedItemAdd_PersistedUsage_ChangesNextBlankQueryRanking</code> @258, <code>R02_1_ExplicitDeny_AdminWithExplicitDenyPurchases_YieldsNoPurchaseMetadata</code> @322, <code>R02_2_ReportOnly_CannotSearchMoneyAccountsOrMoneyScope</code> @370, <code>R02_3_MoneyOnly_CannotSearchFinancialReportRegister</code> @413, <code>R02_4_InspectionRegister_RequiresResolveInspectionPermission</code> @456, <code>R02_5_LockedOrNoOperator_ThrowsUnauthorizedAccessException</code> @501, <code>R02_6_ActiveFinancialTransaction_DoesNotBlockSearchSuggestions</code> @524, <code>R02_7_SearchUsageWriter_DuplicateEventId_AndEligibility_HandledCorrectly</code> @562, <code>R03_1_CommercialInvoiceSuggestions_StateMatrix_MatchesCommercialTableExactly</code> @600, <code>R04_2_ItemOutsideLoadedPage_RetrievedAndAdded</code> @848, <code>R05_1_OldSuccessOrError_AfterClearSelectionOrScopeChange_Ignored</code> @973, <code>R05_2_OperatorOrWorkspaceSwitch_StaleResponseIgnored</code> @1037, <code>R05_3_ValidSearch_LoadsUpTo20Options</code> @1071, <code>R06_1_UnconfiguredSearchPorts_ThrowsExplicitInitializationError</code> @1092, <code>R06_2_SuccessfulAcceptedSelection_RecordsUsageOnce_WithIsolatedWriter</code> @1107, <code>R06_3_FailedOrIneligibleOrNoOpSelection_RecordsNothing</code> @1192, <code>R06_4_UsageWriterFailure_DoesNotUndoOrReverseAcceptance</code> @1233, <code>R07_1_AddToCart_Action_RecordsUsage_AltersBlankRanking_PreservesCartTotals</code> @1269, <code>R07_2_SelectCustomer_RecordsUsage_BypassesWalkInAndNoOp</code> @1366, <code>R07_3_AddCommercialLine_RecordsUsage_SeparatesBuyingSelling_RejectsDuplicates</code> @1453, <code>R08_1_ProductionLifecycle_EndToEnd_UsageRecording</code> @1634, <code>R08_2_RecipeIngredient_And_Output_Selection_Usage</code> @1763, <code>R08_3_DetailOpens_RecordUsage_DeniedOrFailedOpens_RecordZero</code> @1857.

## SearchBomSchemaTests.cs {#src-9f0f3c0100ab}

<code>Software/tests/GetSeek.IntegrationTests/SearchBomSchemaTests.cs</code> · SHA-256 <code>d2cb8f1256133d8533bd7c949a0293a8eedc30287d3899453fc43300116c3c94</code>.

Located test declarations: <code>Baseline075_ToLatest077_MigrationPreservesLegacyRunsAndInitializesSearchUsage</code> @66, <code>DraftProductionRun_SetsCreatedAtUtc_AndRemainsImmutableThroughStartAndFinish</code> @144, <code>ImmediateProductionRun_SetsCreatedAtUtc</code> @206.

## SearchRankingIntegrationTests.cs {#src-68fecbaa81e6}

<code>Software/tests/GetSeek.IntegrationTests/SearchRankingIntegrationTests.cs</code> · SHA-256 <code>e64e4af74fe327a4628b2840c70fb8c3b1bdddf8172fa9050e499b6a0fc40af9</code>.

Located test declarations: <code>ExactPrefixSubstring_Precedence_OrdersSuggestionsCorrectly</code> @78, <code>DeterministicTies_AndUsageWeighting</code> @115, <code>LiteralPercentAndUnderscore_DoNotActAsWildcards</code> @178, <code>MyanmarUnicode_MatchesCorrectly</code> @212, <code>DuplicateNames_DistinguishableBySecondaryAndId</code> @237, <code>EventRetryOnce_AndMultipleItemsPerEvent</code> @264, <code>ConcurrentIncrements_AreThreadSafeAndAccurate</code> @309, <code>LockedOrUnauthorized_SessionRejected</code> @342, <code>WorkspaceIsolation_SeparateDatabasesDoNotLeakUsage</code> @370, <code>FinancialOutcomeRemainsUnchangedOnUsageFailure</code> @411.

## SearchStateIntegrationTests.cs {#src-b34aeb4a7d55}

<code>Software/tests/GetSeek.IntegrationTests/SearchStateIntegrationTests.cs</code> · SHA-256 <code>e5998b74451e1df39fc248c336c37af5214ac1c9656065d0e7362d03010bce70</code>.

Located test declarations: <code>StaleResultsIgnored_WhenNewerQueryIssued</code> @36, <code>StaleErrorsIgnored_WhenNewerQuerySucceeds</code> @81, <code>WorkspaceGuard_IgnoresResults_WhenWorkspaceSwitched</code> @123, <code>OperatorGuard_IgnoresResults_WhenSessionLocked</code> @157, <code>ExactKey_InvalidatedOnTyping</code> @190, <code>Clear_ResetsAllStateAndCancelsPendingRequest</code> @209, <code>Disposal_PreventsFurtherUpdates</code> @243.

## ServiceProtocolContractIntegrationTests.cs {#src-f138a07756da}

<code>Software/tests/GetSeek.IntegrationTests/ServiceProtocolContractIntegrationTests.cs</code> · SHA-256 <code>fa50c71bb6a6d810c2b3dc63d30594293ff3d80c8b12ce0bb3a46e642dccd97a</code>.

Located test declarations: <code>ServiceComposition_UsesDistinctFixedWorkspaceDatabasePaths</code> @14, <code>RequestFrame_RoundTripsTypedBodyAndValidatesBeforeDispatch</code> @27, <code>FrameCodec_RejectsOversizedAndUnknownDiscriminatorBeforeDispatch</code> @69, <code>ResponseFrame_RoundTripsStableErrorAndDiagnosticFields</code> @93, <code>SharedServicePipeClient_ValidatesResponseVersionAndCorrelation</code> @105, <code>ServicePipeAcl_OnlyAllowsConfiguredOperatorsAndAdministrators</code> @120, <code>ServiceSessions_AreOpaqueWorkspaceBoundAndRevocable</code> @136, <code>ServiceRouter_AuthenticatesSelectedOperatorIssuesTokenAndRevokesOnLogout</code> @157, <code>ServiceRouter_ThirdPartyPageUsesLiveAuthorizationAndRequestedFilters</code> @243.

## ServiceWorkspaceProvisioningIntegrationTests.cs {#src-16a867991c62}

<code>Software/tests/GetSeek.IntegrationTests/ServiceWorkspaceProvisioningIntegrationTests.cs</code> · SHA-256 <code>1f744f4c61216e823d8de85e8563c22fff976e5e623f8ca40a2092026dd799d4</code>.

Located test declarations: <code>ServiceProvisioning_InitializesDistinctWorkspacesAndOnlyOneAdministrator</code> @11, <code>ServiceProvisioning_RejectsDemoDatabaseAtRealPathWithoutRelabeling</code> @61.

## SettingsAndTeamsIntegrationTests.cs {#src-ce58ebffb635}

<code>Software/tests/GetSeek.IntegrationTests/SettingsAndTeamsIntegrationTests.cs</code> · SHA-256 <code>0ab5567603f009fc686596492c929c78df1194dae1018b11c04b7a7109530a23</code>.

Located test declarations: <code>ApplySettingsCommand_WhenAuthorized_PersistsSettings_AndSurvivesAppRestart</code> @45, <code>ApplySettingsCommand_WhenUnauthorized_IsDenied</code> @113, <code>SqliteStaffReader_QueriesUsersRolesAndShifts_WithAuthorization</code> @159, <code>MeasuredDiagnosticsService_ProbesDatabaseIntegrity_AndLicenseState</code> @220, <code>MainViewModel_ApplySettings_WhenAuthorized_PersistsSettings_AndSurvivesRestart</code> @255, <code>MainViewModel_ApplySettings_WhenCartHasItems_BlocksBusinessProfileSwitch</code> @316, <code>MainViewModel_TeamsAndDiagnostics_EnforcePermissionsAndProbeDatabase</code> @376, <code>ApplySettings_WhenPersistedDraftCartExists_RejectsBusinessProfileSwitchInsideTransaction</code> @445.

## ShelfLabelOutputIntegrationTests.cs {#src-cb62bd3bea84}

<code>Software/tests/GetSeek.IntegrationTests/ShelfLabelOutputIntegrationTests.cs</code> · SHA-256 <code>8d94c100927c4b912608c0d9d54bff5da2c708bac7945d9ff40ca793b8488546</code>.

Located test declarations: <code>QueueShelfLabelsRequiresEnabledVerifiedProfileAndSnapshotsSelectedRows</code> @26, <code>ScheduledOfferTransitionsQueueVersionedPriceSnapshotsOnceAndRestoreOnlyPrintedPromos</code> @99, <code>ScheduledOfferMissedEntirelyDoesNotCreateStalePromotionalLabels</code> @177, <code>ScheduledOfferCategoryTransitionProcessesBoundedBatchesAcrossRetries</code> @224, <code>ShelfLabelRendererProducesBoundedUnicodeRasterJobsWithoutCutCommand</code> @289.

## SimplifiedCafeCheckoutIntegrationTests.cs {#src-d34a5ea542d8}

<code>Software/tests/GetSeek.IntegrationTests/SimplifiedCafeCheckoutIntegrationTests.cs</code> · SHA-256 <code>47ebc147fada03e56c497f30591d07eacd0909e832dfbb4f3b832b72e0e163d4</code>.

Located test declarations: <code>CafeCashSale_PersistsInvoice_ZeroKitchenJobs_DeductsStock_AndRecordsActivity</code> @95, <code>CafeManualQrAndBankSale_CashierConfirmed_PersistsInvoice_ZeroKitchenJobs</code> @182, <code>Startup_WithSavedTableServiceInConfig_SafelyNormalizesToCounterService</code> @259, <code>UnpaidRestaurantOrders_BlockProfileSwitch_AndResolveViaAuthorizedCancel</code> @285, <code>CafeCheckout_DoubleTapAndRetry_ProducesExactlyOneInvoice</code> @386.

## SingleShopBootstrapperIntegrationTests.cs {#src-02e1d48ffcc1}

<code>Software/tests/GetSeek.IntegrationTests/SingleShopBootstrapperIntegrationTests.cs</code> · SHA-256 <code>411e9e086a861a2c9d0d09d07073fc665cde0ba542b10493e8f0273980958b84</code>.

Located test declarations: <code>CleanDatabase_BootstrapsWithoutProvisioningOrDeviceScopedTables</code> @9.

## Slice1CartPromoIntegrationTests.cs {#src-f9b3c7faf885}

<code>Software/tests/GetSeek.IntegrationTests/Slice1CartPromoIntegrationTests.cs</code> · SHA-256 <code>55b86827167c0b6ed2760a0544da0dbd2edb55a87a34527808725307eb61f457</code>.

Located test declarations: <code>DraftCartService_RoundTrip_PersistsPromoAndPreservesLineIdentityAndAllocations</code> @69, <code>TakePayment_StaleCatalogPrice_RejectsCheckoutWithoutChangingTheDraft</code> @153, <code>StaleCartPriceReview_RequiresCurrentFingerprintAndPreservesLineDiscount</code> @239, <code>TakePayment_SuccessfulPromoCheckout_PopulatesInvoiceAndLineSnapshots</code> @323, <code>DraftCartService_ClearActiveCart_GuardsAgainstClearingOtherCashier</code> @430.

## Slice2DLockScreenIntegrationTests.cs {#src-96ed53d82622}

<code>Software/tests/GetSeek.IntegrationTests/Slice2DLockScreenIntegrationTests.cs</code> · SHA-256 <code>f82cd14619f64f6cfcfcb2ab3fffcd6cb3ac55471d8361e815567cb6e9817dee</code>.

Located test declarations: <code>CandidatesQuery_ContainsOnlySafeIdentityFields_ExcludesSecretsAndInactiveUsers</code> @34, <code>ShiftScoping_DuringOpenShift_LimitsCandidatesToShiftCashierAndElevatedRoles</code> @82, <code>ClosedTerminalShift_DoesNotAuthorizeStaleCachedCashier</code> @129, <code>ExplicitPermissionDenies_RemoveElevatedOperatorFromCandidatesAndUnlock</code> @160, <code>SelectedOperatorVerification_RejectsValidPinOfDifferentUser</code> @190, <code>PinMode_RejectsNonSixDigitPins</code> @232, <code>PasswordUnlockMode_PermitsAlphanumericPasswordsWithoutAutoSubmit</code> @265, <code>LockoutThrottling_FiveFailedAttempts_TriggersPersistentLockout</code> @297, <code>LockoutThrottling_SuccessfulUnlock_ResetsFailedAttempts</code> @354, <code>DirectProductionToDemoMarkerUpdate_ThrowsInvalidOperationException</code> @399, <code>DirectDemoReset_WithDraftCartOrOpenShift_RebuildsDisposableDataset</code> @411, <code>NullSelectedOperator_AuthenticateCredential_FailsClosed</code> @459, <code>OffShiftCashier_PassedDirectlyById_FailsWithUnauthorizedShift</code> @471, <code>PinMode_SixNonAsciiNumericCharacters_FailsWithInvalidPinFormat</code> @508, <code>PasswordAndPinCrossModeChecks_StrictlySeparated_FailsCrossMode</code> @541, <code>LockoutAccounting_SimultaneousFailedAttempts_AtomicallyRecordedAcrossPhysicalConnections</code> @572, <code>LockoutAccounting_StorageFailure_FailsClosed</code> @635.

## Slice4ActionPlacementAndReceiptReprintTests.cs {#src-1e0889f2608b}

<code>Software/tests/GetSeek.IntegrationTests/Slice4ActionPlacementAndReceiptReprintTests.cs</code> · SHA-256 <code>5b946f53d1f541a381ec9cefbcbbe9b2b02fc071ecf0ab6687d7e72230e8573d</code>.

Located test declarations: <code>ReceiptReprintCommand_ThroughPipeline_CreatesPendingJobWithoutMutatingInvoice</code> @140, <code>ReceiptReprintCommand_DeniesUnauthorizedUser</code> @208, <code>SqliteReceiptReader_ReturnsCommittedInvoicesWithJobStateAndLines</code> @241, <code>ReceiptReprintService_QueueViaPipelineAsync_SuccessfullyEnqueues</code> @281.

## Slice5PagingAndBatchActionsIntegrationTests.cs {#src-08cc2b1ebaa1}

<code>Software/tests/GetSeek.IntegrationTests/Slice5PagingAndBatchActionsIntegrationTests.cs</code> · SHA-256 <code>31c6ae098b4c0e0b3fa1bac5ec486affc232bf44fc59fdc322b18863825eb498</code>.

Located test declarations: <code>GetPagedActivityInvoices_PaginatesAndSortsWithStableTieBreaker</code> @79, <code>BatchUpdateUserStatus_GuardsLastActiveAdminAndOnShiftCashier</code> @151, <code>BatchCancelBomDrafts_AllowsUnstartedDrafts_RejectsStartedRuns</code> @225, <code>BatchUpdateUnitAndCategory_GuardsInUseActiveItems</code> @285, <code>BatchCommand_WithoutServerPreview_RejectsBeforeMutation</code> @339, <code>BatchPreview_WhenMembershipChangesWithSameCount_RejectsBeforeMutation</code> @366, <code>BatchPreview_ThirdPartyKindAndSearchMatchPagedReaderScope</code> @411, <code>ThirdPartyPriceLevelCommands_ValidateActiveTierAndBatchPreviewRejectsStaleState</code> @482, <code>GetPagedInventoryItemsAsync_PaginatesAndSortsWithStableTieBreaker</code> @552, <code>InventoryClassificationReview_IsPagedAndRequiresCatalogPermission</code> @599, <code>GetPagedThirdPartiesAsync_PaginatesAndFiltersByKind</code> @654, <code>BatchCommand_WithServerPreview_UpdatesOnlySelectedRecords</code> @698, <code>BatchAssignItemPurpose_UsesPreviewAndProtectsActiveKitParents</code> @758.

## Slice6UomDimensionsAndConversionsIntegrationTests.cs {#src-b098b643c015}

<code>Software/tests/GetSeek.IntegrationTests/Slice6UomDimensionsAndConversionsIntegrationTests.cs</code> · SHA-256 <code>58cbc61b703bfd6b4ccd4502f16264e8e74550b61dd029fcd47f45995fd4ef39</code>.

Located test declarations: <code>Migration023_SeedsDimensionsPreferencesAndMeasurements</code> @61, <code>UomConversionEngine_AccurateRoundTrips</code> @111, <code>UomConversionEngine_ProhibitsCrossDimensionConversion</code> @132, <code>UomConversionEngine_ProhibitsFractionalDiscreteCount</code> @142, <code>UpdateStoreUomPreference_UpdatesPreference_LeavesExistingItemsAndLedgerIntact</code> @157.

## Slice8PricingBatchAndRulesIntegrationTests.cs {#src-e9a0da71bba7}

<code>Software/tests/GetSeek.IntegrationTests/Slice8PricingBatchAndRulesIntegrationTests.cs</code> · SHA-256 <code>6e87af9ea823fa76d19f341549c40c0795ff6411e525cddd04ce0c88506e5052</code>.

Located test declarations: <code>KitComponentCostCalculator_SumsFractionalLeafCostsBeforeCurrencyRounding</code> @77, <code>KitCostProposal_IsDeduplicatedAndBecomesStaleWhenLeafCostChanges</code> @136, <code>LeafCostChange_QueuesNestedAutomaticKitProposalsAndReviewAlerts</code> @202, <code>KitComponentCostCalculator_ResolvesDraftStockLeavesAndNestedKitCosts</code> @260, <code>Migration024_PopulatedUpgradePreservesRowsAndExpandsConstraints</code> @309, <code>SaveItemPricingCommand_SavesCostPlusAmountAndNearestHalf</code> @369, <code>SaveItemPricingCommand_UsesSelectedCostSourceAndPersistsIt</code> @420, <code>CategoryPricingRule_CreatesReviewOnlyProposals_AndApprovalIsStaleSafe</code> @481, <code>CategoryPricingRule_RejectsUnsupportedRoundingBeforeSavingRule</code> @577, <code>SaveItemPricingCommand_RejectsInvalidMarginCeilingAndInvalidInputs</code> @621, <code>ApplyBatchPricingCommand_FillEmpty_And_Overwrite_WorkDeterministically</code> @711, <code>ApplyBatchPricingCommand_ProposalOnly_CreatesProposalsWithoutMutatingCatalogPrices</code> @794, <code>ApplyBatchPricing_RequiresPreview_AndRejectsChangedPricingInputsWithoutAnyWrites</code> @851, <code>ApplyBatchPricing_WhenMembershipChanges_RejectsWithoutCreatingBatch</code> @961, <code>ApplyBatchPricing_UsesPreviewOnce_AndIdempotentRetryReturnsSameBatch</code> @1001, <code>ApplyBatchPricing_RejectsWrongOperatorAndExpiredPreview</code> @1042, <code>CreateBatchPricingPreview_RejectsOver5000AndAcceptsTheExactLimit</code> @1108, <code>CheckoutPriceResolver_HonorsCostFloorSource_MAC_vs_LBP</code> @1167, <code>SqlitePricingReader_ReturnsAccuratePreviewAndTierPrices</code> @1241.

## SliceIInventorySearchAndLocationIntegrationTests.cs {#src-6c2eeb4314ce}

<code>Software/tests/GetSeek.IntegrationTests/SliceIInventorySearchAndLocationIntegrationTests.cs</code> · SHA-256 <code>bf585b9bb5ca6091384d7b7f0aba821e23dc0589f2b7131f8d4a3d6e0643eeaa</code>.

Located test declarations: <code>SearchQuery_FindsItemAcrossPages_ResetsPagingAndMatchesCount</code> @48, <code>LocationMode_FullCatalogVsInStockAtLocation_FilterSemantics</code> @104, <code>SortKeyValidation_WhitelistedSortKeysOnly_InvalidSortThrowsArgumentException</code> @176.

## SliceP0ANestedKitProposalIntegrationTests.cs {#src-fd2f41661c0c}

<code>Software/tests/GetSeek.IntegrationTests/SliceP0ANestedKitProposalIntegrationTests.cs</code> · SHA-256 <code>86794e00211e6bf7068bd3d6b01de373296406c108614e7d09f3160fb3f996a8</code>.

Located test declarations: <code>Approval_FailsAndMarksProposalStale_WhenNestedLeafCostChanges</code> @61, <code>Approval_Succeeds_WhenFingerprintUnchanged</code> @168, <code>KitDecomposition_CycleDetection_DetectsInternalCyclesWithoutStackOverflow</code> @247.

## SliceP0BClassificationQueryDecouplingIntegrationTests.cs {#src-607df6529a2c}

<code>Software/tests/GetSeek.IntegrationTests/SliceP0BClassificationQueryDecouplingIntegrationTests.cs</code> · SHA-256 <code>0e28bd16e6f19b5573330722936807c6cb90220f0a458fe87f30b85181515fc6</code>.

Located test declarations: <code>Supervisor_WithCatalogManage_LoadsOrdinaryInventory_AndClassificationIsUnavailable</code> @47, <code>Admin_WithCatalogManage_CanReviewClassification_AndQueryUnclassifiedItems</code> @110.

## SlicePPricingProposalLifecycleIntegrationTests.cs {#src-0070eaad3de0}

<code>Software/tests/GetSeek.IntegrationTests/SlicePPricingProposalLifecycleIntegrationTests.cs</code> · SHA-256 <code>5055b8924c4eb697795826838b850d368ac7729c82b128938190333b18d00078</code>.

Located test declarations: <code>SaveCategoryPricingRuleCommand_ClosesPriorProposalsAsStale_CreatesNewVersionProposal</code> @73, <code>DeactivateCategoryPricingRuleCommand_MarksCategoryProposalsStale</code> @154, <code>SaveCategoryPricingRuleCommand_PreservesPendingIntakeCostProposal_WhenCategoryRuleUpdated</code> @199.

## SliceS4PermissionEditorUiTests.cs {#src-8965a052591a}

<code>Software/tests/GetSeek.IntegrationTests/SliceS4PermissionEditorUiTests.cs</code> · SHA-256 <code>8b24b4c9aaab89b1fb6e2db2e2e1973b97fb5b9a74a8d3fd1bc260354fa1d21b</code>.

Located test declarations: <code>PermissionEditor_OpenAndToggleOverride_UpdatesDatabaseAndViewModelState</code> @64, <code>PermissionEditor_LastAdminProtection_DisplaysErrorMessageOnSelfDeny</code> @126, <code>PermissionEditor_ProtectedPermissionGrant_DisplaysProtectedPermissionErrorMessage</code> @159, <code>PermissionEditor_SelfEscalation_DisplaysSelfEscalationErrorMessage</code> @193.

## SliceSPermissionOverridesIntegrationTests.cs {#src-5b738e5a99f7}

<code>Software/tests/GetSeek.IntegrationTests/SliceSPermissionOverridesIntegrationTests.cs</code> · SHA-256 <code>aee32fdd9910fe380d8eb0ce608756290415667dd55c85c591247ad67eff9922</code>.

Located test declarations: <code>PermissionResolver_PrecedenceRules_EnforcesDenyTrumpsWildcardAndGrants</code> @66, <code>SetUserPermissionOverrideCommand_AdminCanGrantAndDeny_LastAdminProtected</code> @117, <code>CommandPipeline_MidShiftPermissionRevocation_RejectsRestrictedActionsInstantly</code> @177.

## SqliteBackupAndRestoreTests.cs {#src-631292ebe0e0}

<code>Software/tests/GetSeek.IntegrationTests/SqliteBackupAndRestoreTests.cs</code> · SHA-256 <code>2628f6091ad34b10fe6f9ab3a321551bd3e69b79a480bae4ba7528fe2c4caf0a</code>.

Located test declarations: <code>CreateBackup_And_RestoreStaging_ShouldSucceed</code> @12.

## SqliteDemoDataSeederIntegrationTests.cs {#src-66ca006dd43c}

<code>Software/tests/GetSeek.IntegrationTests/SqliteDemoDataSeederIntegrationTests.cs</code> · SHA-256 <code>46e8fccdf277d509c602cf82672159897824d39982ef5dbefcfb989b108a5dce</code>.

Located test declarations: <code>EnsureInitialDatasetAsync_WhenPendingDemoAlreadyHasBusinessData_PreservesRowsAndRequiresReview</code> @14, <code>SeedLargeScaleDemoDataAsync_And_ResetDatabaseAsync_Execution_Succeeds</code> @55, <code>ResetDatabaseAsync_WhenSalesInvoicesExist_AtomicallyRestoresDemoBaseline</code> @235, <code>PosBootstrapper_BootstrapWithConnectionAsync_OnSeededDatabase_Succeeds</code> @281, <code>SeedLargeScaleDemoDataAsync_PreservesExistingInitialAdmin_And_ResetPreservesUsers</code> @306, <code>SeedLargeScaleDemoDataAsync_OnProductionWorkspace_ThrowsInvalidOperationException</code> @367, <code>SeedLargeScaleDemoDataAsync_WhenAdminHasExplicitSettingsDeny_RejectsAtSeederBoundary</code> @389, <code>ResetDatabaseAsync_OnProductionWorkspace_ThrowsInvalidOperationException</code> @421, <code>SeedLargeScaleDemoDataAsync_WithPreExistingDemoCashier_AllocatesDemoCashier2AndBindsRoleDirectly</code> @443, <code>SeedLargeScaleDemoDataAsync_WithPreExistingSystemUser_PreservesCredentialsAndSystemUser</code> @512.

## SystemInvariantCheckerTests.cs {#src-45d45ffaebdd}

<code>Software/tests/GetSeek.IntegrationTests/SystemInvariantCheckerTests.cs</code> · SHA-256 <code>6d17317a596a0992cb05c973f41fd61c6318a37da821434bb6dbfc58a2191eeb</code>.

Located test declarations: <code>CheckAllInvariantsAsync_ShouldPass_OnValidChain</code> @12, <code>CheckAllInvariantsAsync_ShouldFail_WhenNegativeStockExists</code> @49, <code>CheckAllInvariantsAsync_ShouldFail_WhenCashVarianceMismatchExists</code> @110.

## TaxAndCurrencyPolicyTests.cs {#src-f8a29ec379a8}

<code>Software/tests/GetSeek.IntegrationTests/TaxAndCurrencyPolicyTests.cs</code> · SHA-256 <code>f1e0cb16563c7b0e16094a88d7011c8d5a1dfef011431e384e75b01f59f6ef3c</code>.

Located test declarations: <code>TaxPolicy_FutureSalesUseUpdatedTaxPolicy_WhileHistoricalInvoicesRetainAmountsAndTaxMode</code> @38.

## TeamsPermissionsAndContractsTests.cs {#src-5640142a11bb}

<code>Software/tests/GetSeek.IntegrationTests/TeamsPermissionsAndContractsTests.cs</code> · SHA-256 <code>9396f9d54c8e9c90c7d579551dda35af71d207808a7f0d2bf1b2e56f33e447bc</code>.

Located test declarations: <code>SqliteTeamsReader_WithoutManageTeamsPermission_ThrowsUnauthorizedAccessException</code> @88, <code>SqliteTeamsReader_WithManageTeams_WithoutSalaryRead_WithholdsSalaryAmounts</code> @114, <code>SqliteTeamsReader_WithManageTeams_AndSalaryRead_DisclosesSalaryAmounts</code> @152, <code>CreateTeamMember_NonAdminAssigningAdminOrSupervisor_FailsWithPrivilegeEscalationDenied</code> @178, <code>UpdateTeamMember_ProfileOnlyWithoutSalaryManage_PreservesExistingSalaryAgreement</code> @211, <code>UpdateTeamMember_WithSalarySection_WhenCallerLacksSalaryManage_IsDeniedByPipeline</code> @264, <code>CreateTeamMember_CombinedCommand_WhenFailureOccurs_RollsBackAllTablesCleanly</code> @304, <code>CreateTeamMember_FourCombinations_SucceedAndProduceExpectedRecords</code> @339.

## TerminalTransferCrashRecoveryTest.cs {#src-5ebd0cc51081}

<code>Software/tests/GetSeek.IntegrationTests/TerminalTransferCrashRecoveryTest.cs</code> · SHA-256 <code>b49e2a24cfa50addc07982690e537e169e4b9aca570dc00c614901ce8e3568a4</code>.

Located test declarations: <code>ProcessInterruption_TerminalTransfer_CrashRecoveryVerification</code> @14.

## TerminalTransferProcessCrashTest.cs {#src-b45e1eb9a314}

<code>Software/tests/GetSeek.IntegrationTests/TerminalTransferProcessCrashTest.cs</code> · SHA-256 <code>28147eb7fce6cd7ad4560d73994324f4f560b25fce3a17b2dcd62b201a4786c0</code>.

Located test declarations: <code>ProcessTermination_DuringTerminalTransfer_SurvivesCrash_AndRecoversWithSupervisorAuth</code> @15.

## ThirdPartyAndPricingIntegrationTests.cs {#src-de63335608ea}

<code>Software/tests/GetSeek.IntegrationTests/ThirdPartyAndPricingIntegrationTests.cs</code> · SHA-256 <code>c65f3f8d0c2134bcd93b75e103b3ad9a0039a80aeaca3245f1011455f2f94cad</code>.

Located test declarations: <code>ThirdParty_CRUD_And_AutoCodeGeneration</code> @173, <code>Intake_Updates_MAC_And_LBP</code> @260, <code>PricingWaterfall_Evaluates_Overrides_Tiers_And_FloorGuard</code> @345, <code>PriceTierSettings_Sync_ActiveCount</code> @455, <code>PriceTierSettings_RecordsRuleEventOnlyForSystemTierItems</code> @516.

## ThirdPartyImportIntegrationTests.cs {#src-5cba50a9bd3b}

<code>Software/tests/GetSeek.IntegrationTests/ThirdPartyImportIntegrationTests.cs</code> · SHA-256 <code>e600e036a89616f85cec710e0f7ae472165a31bf295a972edd2a60161f83f24c</code>.

Located test declarations: <code>PossibleDuplicateWarnsWithoutRejecting_AndDoesNotWarnForOwnUpdate</code> @93, <code>ExportTemplate_ReturnsValidWorkbookWithExactHeadersAndExampleRow</code> @124, <code>OversizedFile_RejectedBeforeMutation</code> @145, <code>BlankIdentifier_GeneratesStableCodeAndCompletedWorkbook</code> @170, <code>UnicodeAndMyanmarData_RoundTripsThroughImportAndQuery</code> @210, <code>IdempotentDuplicateRetry_ReturnsPriorResultWithoutDuplicates</code> @271, <code>ExternalMappingMode_CreatesPartyThenUpdatesOnSecondImport</code> @348, <code>AtomicRollback_WhenRowFailsValidationInsideHandler</code> @445, <code>PermissionDenial_RequiresCustomerManagePermission</code> @483, <code>FlexibleBooleansAndTierFormattingAndBarcodeValidation_AreHandled</code> @520.

## TouchAndShortcutIntegrationTests.cs {#src-210552b24818}

<code>Software/tests/GetSeek.IntegrationTests/TouchAndShortcutIntegrationTests.cs</code> · SHA-256 <code>4bda8079341746f990d14ec1bfe5cb26a6df2c5ba2c33c4dba21dab45220a403</code>.

## TraceabilityCandidateReaderTests.cs {#src-f2350f08a4d0}

<code>Software/tests/GetSeek.IntegrationTests/TraceabilityCandidateReaderTests.cs</code> · SHA-256 <code>09a08ab3e2dc10ebcd65ba26022e001fc7bec1cec8aae8463de1783713042bf8</code>.

Located test declarations: <code>Candidates_AreReadOnlyManualChoices_FilteredByLocationStateAndBalance</code> @13, <code>Candidates_RejectUnauthenticatedReaders</code> @72.

## UiPreferenceTestScope.cs {#src-e8c7d62e9a21}

<code>Software/tests/GetSeek.IntegrationTests/UiPreferenceTestScope.cs</code> · SHA-256 <code>86a3801ee6dd6945cab0dadb971c1ba80dee23bba38570291846f91ea9b19da3</code>.

## UnifiedTeamCommandIntegrationTests.cs {#src-247956495a37}

<code>Software/tests/GetSeek.IntegrationTests/UnifiedTeamCommandIntegrationTests.cs</code> · SHA-256 <code>b892acd43db9aa58b85ae99f6a1765e69038376ca923d54945e2da3bb3edc52d</code>.

Located test declarations: <code>CreateTeamMember_Combination1_PersonOnly_CreatesOnlyPersonRecord</code> @90, <code>CreateTeamMember_Combination2_LoginOnly_CreatesPersonAndUserWithRole</code> @135, <code>CreateTeamMember_Combination3_SalaryOnly_CreatesPersonAndSalaryAgreement</code> @194, <code>CreateTeamMember_Combination4_Combined_CreatesAllLinkedEntitiesAtomically</code> @252, <code>CreateTeamMember_LinkExistingUser_LinksCorrectly</code> @324, <code>CreateTeamMember_LinkAlreadyLinkedUser_FailsWithUserAlreadyLinked</code> @361, <code>CreateTeamMember_LinkNonExistentUser_FailsWithUserNotFound</code> @386, <code>CreateTeamMember_BothNewLoginAndLinkExistingUser_FailsWithInvalidCombination</code> @402, <code>CreateTeamMember_DuplicateUsername_CaseInsensitive_FailsWithUsernameAlreadyExists</code> @418, <code>CreateTeamMember_DuplicatePersonCode_FailsWithPersonCodeAlreadyExists</code> @440, <code>CreateTeamMember_InvalidPin_FailsWithInvalidQuickPin</code> @459, <code>CreateTeamMember_UnrecognizedRole_FailsWithInvalidRole</code> @479, <code>CreateTeamMember_NonAdmin_AttemptingAdminOrSupervisorRole_FailsWithPrivilegeEscalationDenied</code> @494, <code>CreateTeamMember_WithoutTeamsManage_FailsWithUnauthorized</code> @519, <code>CreateTeamMember_WithSalary_WithoutSalaryManage_FailsWithUnauthorized</code> @544, <code>CreateTeamMember_InvalidTrackingMonth_FailsWithInvalidPayrollMonth</code> @569, <code>CreateTeamMember_NegativeSalaryAmount_FailsWithInvalidSalaryAmount</code> @588, <code>CreateTeamMember_AtomicRollback_LeavesZeroRowsCommittedOnFailure</code> @603, <code>CreateTeamMember_SameKeyRetry_ReturnsCachedIdempotentResultWithoutDuplication</code> @651, <code>UpdateTeamMember_ProfileOnly_PreservesExistingSalaryAndLogin</code> @688, <code>UpdateTeamMember_StaleRevision_FailsWithStaleRevision</code> @744, <code>UpdateTeamMember_EnableLoginForExistingPerson_PreservesPersonIdAndSalaryHistory</code> @766, <code>UpdateTeamMember_DisableLogin_DeactivatesUserAndBumpsSecurityRevision</code> @824, <code>UpdateTeamMember_ReenableDisabledLogin_WithoutPin_FailsWithPinRequired</code> @867, <code>UpdateTeamMember_ReenableDisabledLogin_WithValidPin_ReactivatesUser</code> @897, <code>UpdateTeamMember_DeactivateLastAdmin_FailsWithLastAdminProtected</code> @936, <code>UpdateTeamMember_DemoteLastAdmin_FailsWithLastAdminProtected</code> @953, <code>UpdateTeamMember_DeactivateOnShiftCashier_FailsWithOnShiftCashierProtected</code> @969, <code>UpdateTeamMember_NonAdmin_AttemptingPrivilegeEscalation_FailsWithPrivilegeEscalationDenied</code> @1006, <code>SalaryEligibility_FirstCreationOff_WritesNoAgreement</code> @1021, <code>SalaryEligibility_LaterEnable_WritesDatedAgreement_AndProjectsAccrualOnlyWhenEffective</code> @1048, <code>SalaryEligibility_ScheduledDisable_WritesDisabledAgreement_PreservesCarryAndHistory</code> @1093, <code>SalaryEligibility_EnabledZeroBase_AllowsZeroBaseAccrual</code> @1146, <code>SalaryEligibility_N01_TrackingStartMonth_CannotBeSetAfterExistingPayrollRecords</code> @1166, <code>SalaryEligibility_CurrencyChangeBlocked_WhenUnsettledBalanceExists</code> @1202, <code>UpdateTeamMember_SupervisorCannotGrantSelfProtectedPermissions_A01</code> @1237, <code>UpdateTeamMember_ProfileOnlyEmploymentDateChange_CannotInvalidateExistingDeductions_A03</code> @1258, <code>UpdateTeamMember_ExistingUserOnly_EnablingSalaryAtomicallyCreatesPersonAndAgreement_A04</code> @1297, <code>UpdateTeamMember_FinalizedPeriod_CannotOverwriteClosedMonthTerms_A08</code> @1335, <code>UpdateTeamMember_ExplicitNullDailyOverride_ClearsDailyOverrideRate_A10</code> @1380, <code>GetTeamMemberDetail_FutureSalaryDisable_PreservesCurrentMonthEligibility_A09</code> @1417, <code>CreateTeamMember_InvalidDecimalPlaces_ReturnsInvalidDecimalPlaces</code> @1455, <code>CreateAndUpdateTeamMember_ScaleZero_PreservesScaleZero</code> @1482.

## UnifiedTeamLifecycleAndSecurityIntegrationTests.cs {#src-1f64ba4543ce}

<code>Software/tests/GetSeek.IntegrationTests/UnifiedTeamLifecycleAndSecurityIntegrationTests.cs</code> · SHA-256 <code>61838316f07f0a54ae01838c3a2e248012be002cd3532d569a79a233d2b8b783</code>.

## UnifiedTeamReaderIntegrationTests.cs {#src-9e34cc73be21}

<code>Software/tests/GetSeek.IntegrationTests/UnifiedTeamReaderIntegrationTests.cs</code> · SHA-256 <code>b5355aedec565370b89c9c48941ebe7ce5a8993c7f65d6a542c0495e772b541f</code>.

Located test declarations: <code>GetTeamMembersAsync_UnionOfPeopleAndUnlinkedUsers_ReturnsDistinctRowKeys</code> @35, <code>GetTeamMembersAsync_SameDisplayName_PreservesDistinctRecordsWithStableRowKeys</code> @119, <code>GetTeamMembersAsync_SalaryDisclosureGating_HidesSalaryValuesWithoutSalaryRead</code> @158, <code>GetTeamMembersAsync_NoReadSideCreation_LeavesDatabaseUnchanged</code> @215, <code>GetTeamMembersAsync_CompleteDataSortingBeforePaging_ProducesStableOrderingAcrossPages</code> @260.

## UnifiedTeamUiIntegrationTests.cs {#src-8ed6ba03bb75}

<code>Software/tests/GetSeek.IntegrationTests/UnifiedTeamUiIntegrationTests.cs</code> · SHA-256 <code>3e4724c4f0ba31699e5f055963507becf8adaf9b461d57461f1d5c5d1d71a3f6</code>.

## UnifiedTeamWorkspaceIntegrationTests.cs {#src-ad82916e7744}

<code>Software/tests/GetSeek.IntegrationTests/UnifiedTeamWorkspaceIntegrationTests.cs</code> · SHA-256 <code>7e80083c530d94429de9504aecb8cc60cbf050d0ebbaea1519854ca6fb54d7bd</code>.

## WorkspacePopupPlacementTests.cs {#src-5af19db94557}

<code>Software/tests/GetSeek.IntegrationTests/WorkspacePopupPlacementTests.cs</code> · SHA-256 <code>601e50072984eb686044a8db431d500ab6c77b729a0bc952aab9bb50cb1608ac</code>.

## WorkspaceSearchBoxUiTests.cs {#src-d883f6c5025d}

<code>Software/tests/GetSeek.IntegrationTests/WorkspaceSearchBoxUiTests.cs</code> · SHA-256 <code>f01c5c5a55be12c374dd4b2c380a72e930dff3e61b756878d545d64f57187e75</code>.

## WorkspaceThemeConsistencyTests.cs {#src-b058c127f53c}

<code>Software/tests/GetSeek.IntegrationTests/WorkspaceThemeConsistencyTests.cs</code> · SHA-256 <code>42db2cb2b110a4a98fc7bec3e1679e855aa8ffe64770ff5d7a1767337e4eb7ac</code>.

## ZReportAndWasteExpenseIntegrationTests.cs {#src-50981a21ab71}

<code>Software/tests/GetSeek.IntegrationTests/ZReportAndWasteExpenseIntegrationTests.cs</code> · SHA-256 <code>e126c742243c268398f449893d12bd075f87fefbd777cbd7909a4d4ecebae6f5</code>.

Located test declarations: <code>RecordOnly_ZeroMoneyMovement_PreservesCashAndBankBalances</code> @151, <code>CashPayment_ReducesCashDrawerOnce_AndCreatesShiftCashMovement</code> @185, <code>BankPayment_UpdatesBankAccount_DoesNotTouchCashDrawer</code> @238, <code>ShiftClosingZReport_IncludesSalaryAndExpenseLines_SeparatingCashAndNonCash</code> @290, <code>AdjustStock_AutoRecordWaste_CreatesNonCashWasteExpense</code> @370, <code>AdjustStock_AutoRecordWaste_Off_DoesNotCreateWasteExpense_UntilManualCommand</code> @430, <code>RecordWasteExpense_IneligibleMovement_RejectsOrdinarySale</code> @507, <code>ReverseExpensePayment_BankRequiresVerifiedReference_AndSucceedsWithReference</code> @539, <code>NonCashWasteExpense_CannotBePaidOrCancelled_AndReportsNonCashStatusInReader</code> @591, <code>SaveAndPayExpense_RecordsShiftId_OnExpenseRecordsAndPayments</code> @662.

## Program.cs {#src-1c8113547b9c}

<code>Software/tests/GetSeek.TestCrashHelper/Program.cs</code> · SHA-256 <code>a0ddc097636ff48b294cdc3793c553b1059ff060c3b058f5f6bf5f743be02df9</code>.

## AuditJournalEntryTests.cs {#src-23aea37a5af1}

<code>Software/tests/GetSeek.UnitTests/AuditJournalEntryTests.cs</code> · SHA-256 <code>c90a9cabc286e6e326d12034b745c5419109190f88ca989e1a6cf9d92e225407</code>.

Located test declarations: <code>ComputeHash_ShouldProduceConsistentSha256</code> @9, <code>ComputeHash_ShouldChange_WhenAnyFieldIsModified</code> @29.

## CartCalculationServiceUnitTests.cs {#src-c8139098eb21}

<code>Software/tests/GetSeek.UnitTests/CartCalculationServiceUnitTests.cs</code> · SHA-256 <code>0794037b236c2fb7b333e623e33f0a7dea23c8b5adf233aaf976df16ebc39c9a</code>.

Located test declarations: <code>Calculate_EmptyCart_RejectsPromotion</code> @8, <code>Calculate_InvalidPromoValues_ReturnsError</code> @22, <code>Calculate_FixedPromoExceedsEligibleTotal_ReturnsError</code> @50, <code>Calculate_RetiredIncludedTaxInput_UsesExclusivePolicy</code> @72, <code>Calculate_TaxAddedOnTop_MatchesPlanExample</code> @101, <code>Calculate_ProportionalDiscountRemainderAllocation_SumsExactly</code> @129, <code>Calculate_ZeroDecimalCurrency_OperatesAccurately</code> @170, <code>Calculate_CostFloorBreach_RejectedWithoutSupervisorElevation</code> @199.

## CashReceiptAndSettlementUnitTests.cs {#src-346e8096813a}

<code>Software/tests/GetSeek.UnitTests/CashReceiptAndSettlementUnitTests.cs</code> · SHA-256 <code>9d389e6e508aafc1027521d7ac6ea27411071d9c9d867707e84a903839b1ce8d</code>.

Located test declarations: <code>CashRounding_RecordsSignedDiscountOrCharge</code> @10, <code>CashSettlement_IncludesServiceTaxAndThenRoundsCashDue</code> @27, <code>CashSettlement_NonCashTenderDoesNotApplyCashRounding</code> @42, <code>PaperPagination_KeepsNormalInvoiceRowsAndFinalSettlement</code> @54, <code>PaperPagination_AlwaysReturnsAHeaderAndSettlementPageForEmptyOrder</code> @67, <code>PaperPagination_DoesNotDropTheFinalNonemptyPage</code> @80, <code>PaperPagination_RejectsAnAtomicRowTallerThanPageBody</code> @98, <code>CashDisplayPrecision_DoesNotHideACommittedMinorUnitFraction</code> @108, <code>ReceiptTemplateSyntax_AcceptsOnlyBalancedAllowlistedPlainText</code> @115, <code>ThermalRasterRenderer_WrapsAndSplitsLongReceiptsIntoBoundedRasterBands</code> @127, <code>ReceiptFonts_AreBundled_AndMixedScriptsUseTheSameMeasuredRasterPath</code> @138, <code>ThermalPreviewPng_UsesTheRenderedReceiptRaster</code> @151, <code>PaperPreviewPng_RendersEveryPaginatedPage</code> @161.

## CustomerUnitTests.cs {#src-d1ebba3676f7}

<code>Software/tests/GetSeek.UnitTests/CustomerUnitTests.cs</code> · SHA-256 <code>9967c52c5cbb92b73534175f373a11561bb92cf2f6951744fc3079a4415b65a3</code>.

Located test declarations: <code>CreateCustomerCommand_RequiresManageCustomersPermission</code> @9, <code>UpdateCustomerCommand_RequiresManageCustomersPermission</code> @16, <code>DeactivateCustomerCommand_RequiresManageCustomersPermission</code> @23, <code>CustomerDomainModel_DefaultsToActive_AndGeneratesGuid</code> @30.

## ErrorReportingUnitTests.cs {#src-de9297cb0485}

<code>Software/tests/GetSeek.UnitTests/ErrorReportingUnitTests.cs</code> · SHA-256 <code>e2e71d8815c731e342b6d935e3b293e30288eb79b12ab1a312c6850fb07cf63d</code>.

Located test declarations: <code>Report_ReusesProvidedDiagnosticId_Verbatim</code> @13, <code>Report_GeneratedId_MatchesLog</code> @38, <code>Report_InPersistentDemoWorkspace_UsesSeparateWorkspaceLog</code> @57, <code>Report_WhenLogDirectoryUnwritable_ReportsLoggingUnavailable</code> @81, <code>Sanitize_RedactsPathsNumberRunsAndSecrets</code> @102, <code>LogDiagnostic_WritesOnlyStructuredFields_NoFreeFormExceptionText</code> @117.

## HardwareAndAllocationUnitTests.cs {#src-5773d1425dbf}

<code>Software/tests/GetSeek.UnitTests/HardwareAndAllocationUnitTests.cs</code> · SHA-256 <code>95a76bca979cf365251c83dce02995586e3415d775365f0ae9d9cbfbfcdd3c7f</code>.

Located test declarations: <code>BarcodeScannerWedge_ShouldParseWeighedFreshPlu</code> @9, <code>BarcodeScannerWedge_ShouldParseGs1CompoundBarcode</code> @21, <code>BarcodeScannerWedge_ShouldAcceptBurst_AndRejectSlowTyping</code> @33, <code>EscPosReceiptBuilder_ShouldEmitExpectedProtocolBytes</code> @59, <code>SerialScaleDriver_ShouldParseStableWeightFrame</code> @84.

## InventoryTierEditorTests.cs {#src-e592e8075206}

<code>Software/tests/GetSeek.UnitTests/InventoryTierEditorTests.cs</code> · SHA-256 <code>a33efe360229d8f4621d62cee80f8b25e77b5774b167ae7d1c0a1cc691faada5</code>.

Located test declarations: <code>TierEditsSelectTheMatchingMode_AndConvertAtTheCommandBoundary</code> @8, <code>LoadingAndCloningValuesDoNotChangeTheSavedMode</code> @26.

## LocalizationAndVisibleErrorsUnitTests.cs {#src-399b0189d539}

<code>Software/tests/GetSeek.UnitTests/LocalizationAndVisibleErrorsUnitTests.cs</code> · SHA-256 <code>bb78dddf9c85d63beaebc8f9d0e1e1e1e11d5a419e98fc616e39830134872f3d</code>.

Located test declarations: <code>Task17Keys_ResolveAccurately_InAllSupportedLanguages</code> @23, <code>ProductionExecuteLabel_DistinctFromStartAndFinish_InAllLanguages</code> @47, <code>SearchState_WhenReaderFails_SurfacesLocalizedErrorAndAllowsRetry</code> @68, <code>MonthNames_ResolveAccurately_InAllSupportedLanguages</code> @91, <code>UnifiedTeamsAndExpenseKeys_ResolveAccurately_InAllSupportedLanguages</code> @107, <code>PayrollMonthOptions_UpdateDisplayNames_WhenLanguagePreferenceChanges</code> @144.

## LocalizationParityUnitTests.cs {#src-066d8fbd2df9}

<code>Software/tests/GetSeek.UnitTests/LocalizationParityUnitTests.cs</code> · SHA-256 <code>c0f0842c17767d51a36f211e60fa980aa0e86835f51ee47a9b04b9284c96fca3</code>.

Located test declarations: <code>EnglishAndThaiDictionaries_HaveIdenticalKeySets</code> @12, <code>EnglishAndMyanmarDictionaries_HaveIdenticalKeySets</code> @21, <code>Localize_ResolvesThai_WhenLanguageIsTh</code> @30, <code>Localize_ResolvesMyanmar_WhenLanguageIsMyOrMyMm</code> @39, <code>PricingNavigationAndWorkspaceLabels_AreLocalizedInAllSupportedLanguages</code> @51, <code>Localize_FallsBackToEnglish_ForAnUnsupportedLanguage</code> @68, <code>Localize_ReturnsTheKey_WhenMissingFromAllDictionaries</code> @76.

## MainViewModelTestCollection.cs {#src-aa9177eb523e}

<code>Software/tests/GetSeek.UnitTests/MainViewModelTestCollection.cs</code> · SHA-256 <code>e54e436fd60c314bd9c6394feda406453399cc062d962099ca8b364193092ef6</code>.

## MainViewModelTests.cs {#src-c4e39a4e715e}

<code>Software/tests/GetSeek.UnitTests/MainViewModelTests.cs</code> · SHA-256 <code>7a990e6d165264ee25bb5bb8064c6ae1e504c6bde5be8504dd70885fa40e519d</code>.

Located test declarations: <code>InitialState_ShouldHaveNavigationDrawerOpenAndPosActive</code> @16, <code>SelectMenuCommand_ShouldUpdateActiveMenuAndActiveFlags</code> @28, <code>DrawerAndPowerCommands_ShouldExecuteAndNotify</code> @49, <code>CategorySelection_ShouldFilterProducts</code> @90, <code>CartSteppersAndTotals_ShouldCalculateAccurately</code> @103, <code>InteractivePills_ShouldCycleValues</code> @123, <code>PlaceOrderCommand_InDemoMode_ShouldClearCartAndAdvanceOrderNumber</code> @149, <code>ShortcutHints_ToggleAndDismiss_ShouldUpdateVisibility</code> @164, <code>TouchKeyboard_TypingAndBackspace_ShouldUpdateSearchQuery</code> @177, <code>TouchNumpad_TypingAndClear_ShouldUpdateNumpadValue</code> @200, <code>BusinessProfile_SwitchWithItemsInCart_ShouldBeBlocked</code> @221, <code>BusinessProfile_SwitchWithEmptyCart_ShouldSwitchAndAdaptUI</code> @234, <code>SelectMenuCommand_AllViews_ShouldActivateCorrespondingFlags</code> @266, <code>Activity_FilterAndSelectOrder_ShouldFilterAndHighlight</code> @304, <code>Inventory_SearchAndQuickAdjust_ShouldFilterAndBlockDirectAdjustment</code> @331, <code>ReportsAndSettings_Commands_ShouldPreventFalseOperationalClaims</code> @350, <code>OperationalHonesty_DiagnosticsAndDemoMode_ShouldReportUnprobedStatus</code> @384, <code>MyanmarLanguageAndKeyboard_ShouldSupportSelectionAndParity</code> @396, <code>OnKeyboardBackspace_ShouldOperateOnUnicodeGraphemeClusters</code> @436, <code>LockScreen_RequiresOperatorSelection_BeforePinAccepted</code> @465, <code>LockScreen_SixDigitPin_UnlocksOnSubmit_WhenCorrect</code> @480, <code>LockScreen_SixDigitPin_ResetsInput_And_ReportsWrongPin_WhenIncorrect</code> @499, <code>LockScreen_FiveFailedAttempts_EnforcesOneMinuteLockout</code> @516, <code>StaffCreation_RequiresMinimumSixDigitPin</code> @548, <code>ChangePin_ModalLifecycle_And_Validation</code> @571, <code>ChangePin_UpdatesUnlockPin_AndAllowsSuccessfulLogin</code> @625, <code>AdjustDeltaQuantity_UpdatesIsNegativeAdjustment_AndResetsMarkAsExpense</code> @662, <code>ThirdPartyCode_AndLabel_ReflectsEditAndNewMode</code> @685.

## ManufacturingUnitTests.cs {#src-24304977356f}

<code>Software/tests/GetSeek.UnitTests/ManufacturingUnitTests.cs</code> · SHA-256 <code>d82b0f387440f03f8715ae766b03d2d3e93c88bd18a3484c56e458ef40d7c08a</code>.

Located test declarations: <code>CycleDetection_DirectSelfReference_ReturnsTrue</code> @9, <code>CycleDetection_TwoLevelLoop_ReturnsTrue</code> @22, <code>CycleDetection_DeepChainLoop_ReturnsTrue</code> @43, <code>CycleDetection_DiamondGraph_ReturnsFalse</code> @68, <code>CycleDetection_DisjointSubtree_ReturnsFalse</code> @94, <code>Manufacturing_IngredientScrapComputation_CalculatesCorrectly</code> @121.

## MoneyTests.cs {#src-d8662bbf9796}

<code>Software/tests/GetSeek.UnitTests/MoneyTests.cs</code> · SHA-256 <code>c4f91670623b066dbf30a56ebdcab68212164ac8a8add583930a96ae53dac32d</code>.

Located test declarations: <code>FromDecimal_ShouldConvertMinorUnitsCorrectly</code> @9, <code>Addition_ShouldCalculateSum_WhenSameCurrency</code> @18, <code>Addition_ShouldThrow_WhenCurrenciesMismatch</code> @30, <code>Subtraction_ShouldCalculateDifference</code> @42, <code>Multiplication_ShouldApplyBankersRounding</code> @53, <code>Comparison_ShouldOrderCorrectly</code> @62.

## PricingCalculationEngineTests.cs {#src-250de7b10546}

<code>Software/tests/GetSeek.UnitTests/PricingCalculationEngineTests.cs</code> · SHA-256 <code>6cac0e5f6c970f96474b94b62c8fe57dd2bebdaa7bc0d127da4edb4c5f2f3186</code>.

Located test declarations: <code>Manual_method_returns_the_entered_base_price</code> @19, <code>Markup_cost_applies_target_on_cost_basis</code> @28, <code>Margin_cost_divides_cost_by_one_minus_target</code> @37, <code>Cost_plus_amount_adds_fixed_amount_to_cost_basis</code> @46, <code>Unrounded_candidate_preview_uses_the_same_formula_and_rounding_as_saved_price</code> @55, <code>Margin_cost_with_target_greater_than_or_equal_to_one_throws_invalid_margin_ceiling</code> @77, <code>Rounding_rules_snap_the_base_price</code> @86, <code>Increment_rounding_uses_ceiling_or_floor_at_the_configured_currency_step</code> @99, <code>Increment_rounding_scales_with_zero_and_three_decimal_currencies</code> @115, <code>Display_rounding_increment_must_be_exactly_representable_at_store_precision</code> @132, <code>Increment_conversion_supports_one_and_four_decimal_currencies</code> @149, <code>Increment_rounding_handles_one_and_four_decimal_currencies</code> @161, <code>Ceiling_increment_overflow_is_reported_instead_of_wrapping_minor_units</code> @174, <code>Ending_rounding_compatibility_matches_currency_precision</code> @183, <code>Nearest_half_differs_from_round_to_50_for_upper_cent_amounts</code> @194, <code>System_default_weight_is_used_for_the_tier</code> @202, <code>Tier_weight_minus_one_is_free_but_lower_weights_are_rejected</code> @212, <code>Custom_weight_overrides_the_system_default</code> @225, <code>Fixed_override_wins_over_weights</code> @235, <code>Effective_tier_clamps_inactive_tiers_to_standard</code> @245, <code>Effective_tier_keeps_an_active_tier_within_the_configured_count</code> @252, <code>Effective_tier_falls_back_to_standard_for_unknown_values</code> @259, <code>Cost_floor_adds_the_minimum_margin</code> @266, <code>Cost_floor_is_zero_before_the_first_receipt</code> @273, <code>Below_cost_is_only_flagged_against_a_non_zero_floor</code> @280, <code>Pricing_method_parsing_is_case_insensitive</code> @288, <code>Rounding_rule_parsing_is_case_insensitive</code> @299.

## PricingOffersAndMassRunUnitTests.cs {#src-5713952dda33}

<code>Software/tests/GetSeek.UnitTests/PricingOffersAndMassRunUnitTests.cs</code> · SHA-256 <code>e1900febdf15ea51cc68129a957cf3ad0bc6adf512f0ddbf4b5cc3b74b2d1556</code>.

Located test declarations: <code>OfferEvaluationEngine_Evaluates_PercentageDiscount</code> @14, <code>OfferEvaluationEngine_Evaluates_BundleQuantityDiscount_3For100</code> @47, <code>OfferEvaluationEngine_IgnoresExpiredOrInactiveOffers</code> @82, <code>OfferEvaluationEngine_RespectsCustomerTierAndEnteredQuantityUnit</code> @114, <code>CartCalculation_AppliesAutomaticOffer_AndDoesNotStackManualPromo</code> @130, <code>ReceiptDocumentBuilder_Builds_ThermalAndPaperRepresentations</code> @151.

## ProductionLotFormulaTests.cs {#src-1c7e0d504594}

<code>Software/tests/GetSeek.UnitTests/ProductionLotFormulaTests.cs</code> · SHA-256 <code>fcd394b3aec3f90bcc5f8c96cdb036fcdc52fe20a756c360f7a8e0fc238b7505</code>.

Located test declarations: <code>DateTokensAndPaddedRandomDigitsAreResolved</code> @8, <code>InvalidFormulaIsRejected</code> @20.

## QuantityTests.cs {#src-54046e64297e}

<code>Software/tests/GetSeek.UnitTests/QuantityTests.cs</code> · SHA-256 <code>d256064d63226640ee3524f55d1434739e5eef5c35de0a61871a4ff101f04896</code>.

Located test declarations: <code>BaseAmount_ShouldCalculateAccurately</code> @9, <code>Addition_ShouldCalculateSum_WhenSameUnit</code> @20, <code>Addition_ShouldThrow_WhenIncompatibleUnits</code> @32.

## SalaryCalculationTests.cs {#src-2c8b502727e5}

<code>Software/tests/GetSeek.UnitTests/SalaryCalculationTests.cs</code> · SHA-256 <code>758c50f268b1bba96a16e7f28bb0b2b38b93719e570abaad29bd78303863475b</code>.

Located test declarations: <code>RemainingBalance_UsesSignedBuckets</code> @10, <code>RemainingBalance_RejectsOverflow</code> @20, <code>Section4_4_OctoberExample_CalculatesExactProrationAndForecast</code> @27, <code>Section4_4_DailyOverride_AppliesToPartialMonth</code> @108, <code>FullMonth_ReturnsExactMonthlySalaryWithoutRounding</code> @132, <code>PartialEmployment_MidMonthStartAndEnd_CalculatesCorrectEligibleDays</code> @155, <code>UnpaidDays_ReducesPayableDaysAndEarnedBase</code> @176, <code>UnpaidDays_EqualToEligibleDays_YieldsZeroEarnings</code> @197, <code>EmploymentBeforeOrAfterMonth_YieldsZeroEligibleDays</code> @215, <code>DeductionsExceedingGross_ThrowsArgumentException</code> @245, <code>UnpaidDaysExceedingEligible_ThrowsArgumentOutOfRangeException</code> @266, <code>Overpayment_ProducesPrepaidCreditAndZeroAmountDue</code> @282, <code>FinalizedBalance_AvailableOnlyWhenPositive</code> @304.

## SearchAndManufacturingContractsUnitTests.cs {#src-87a0217105b0}

<code>Software/tests/GetSeek.UnitTests/SearchAndManufacturingContractsUnitTests.cs</code> · SHA-256 <code>299b3800b4ef4c212b9e7ede0b5a4ded6ce6e03c21b7e67659ebbb3edc86c974</code>.

Located test declarations: <code>SearchRequest_ClampsLimitCorrectly</code> @9, <code>SearchEntityKey_GuidConversionsAndFormatting</code> @31, <code>SearchOption_ToStringFormatting</code> @48, <code>ManufacturingSortKeys_ValidateAllowedSortKeys</code> @61, <code>ProductionRunSortKeys_ValidateAllowedSortKeys</code> @101.

## Slice0SharedBoundariesUnitTests.cs {#src-968737e55900}

<code>Software/tests/GetSeek.UnitTests/Slice0SharedBoundariesUnitTests.cs</code> · SHA-256 <code>8432b9b392ad8e34a66a1986939f9fc051c8120145f0f32c1f2b214840f2a39e</code>.

Located test declarations: <code>PageRequest_EnforcesAllowedPageSizes_AndMinPageNumber</code> @14, <code>PagedResult_CalculatesPagesAndNavigationCorrectly</code> @28, <code>SortKeyValidator_AllowsWhitelistedKeys_AndRejectsUnknownWithInvalidSortKey</code> @47, <code>ImportPolicy_HasExactStandardBounds</code> @78, <code>SaveItemPricingCommand_RequiresManageCatalogPermission</code> @85, <code>PagedTableState_TogglesSortAndClampsPageSize</code> @102, <code>PagedTableState_SelectionSurvivesPageAndSort_AndClearsOnScopeChange</code> @124, <code>MainViewModel_EmptyCart_HidesPromoAndDiscountLine</code> @146.

## Slice4UiAndSettingsDiagnosticsTests.cs {#src-126a455b6bf9}

<code>Software/tests/GetSeek.UnitTests/Slice4UiAndSettingsDiagnosticsTests.cs</code> · SHA-256 <code>410b931dd7525dcce9024a4d899bcd8374daa6251657ccb070ac46e21342bbe7</code>.

Located test declarations: <code>SelectMenu_SupportsAll11CanonicalDrawerItems</code> @14, <code>CopyCorrelationIdCommand_FiresClipboardEventAndStatus</code> @37, <code>ClearErrorHistory_ClearsDisplayEntriesWhileDiskLogRemainsIntact</code> @51, <code>ManageReceipts_ViewModelCommands_ToggleState</code> @90, <code>StoreUomPreferences_ConversionPreview_CalculatesCorrectly</code> @106, <code>PagedTableState_Navigation_RespectsPageBounds</code> @134.

## ThemeAndLanguageUnitTests.cs {#src-581f60c8a214}

<code>Software/tests/GetSeek.UnitTests/ThemeAndLanguageUnitTests.cs</code> · SHA-256 <code>85b1392d02ea8e015d3616f42429d1a0eaf331b7bb635f18290d6495ab03035f</code>.

Located test declarations: <code>Resolve_UnknownOrEmptyTheme_FallsBackToDefault</code> @26, <code>NextTheme_CyclesAndWraps</code> @35, <code>UiPreferences_RoundTripsThemeAndLanguage</code> @45, <code>ThemeDictionaries_DeclareEveryCanonicalKey</code> @65.

## TouchKeyboardLayoutUnitTests.cs {#src-510730dbe541}

<code>Software/tests/GetSeek.UnitTests/TouchKeyboardLayoutUnitTests.cs</code> · SHA-256 <code>23eaadd4e9498b10ed9b34371148791955dd36993a57ad090a340705e6db5c06</code>.

Located test declarations: <code>AvailableLayouts_ContainsEnglishAndBothMyanmarVariants</code> @9, <code>EnglishLayout_HasValidKeyStructureAndShiftMappings</code> @17, <code>MyanmarVisualLayout_EmitsValidMyanmarUnicodeCharacters</code> @34, <code>MyanmarPhoneticLayout_EmitsValidMyanmarUnicodeAndMultiCodepoints</code> @55, <code>Resolve_ReturnsCorrectLayoutOrFallback</code> @72, <code>GetNextLayout_CyclesThroughAllLayouts</code> @82.

## UnicodeTextHelperUnitTests.cs {#src-2cc426734c90}

<code>Software/tests/GetSeek.UnitTests/UnicodeTextHelperUnitTests.cs</code> · SHA-256 <code>ef3b13f30c1fea2e427a6088d768182a95a42dbe7469376b7cb1275af32cd03b</code>.

Located test declarations: <code>DeleteLastTextElement_EmptyOrNull_ReturnsEmpty</code> @9, <code>DeleteLastTextElement_SingleAsciiCharacter_ReturnsEmpty</code> @16, <code>DeleteLastTextElement_AsciiString_RemovesLastChar</code> @22, <code>DeleteLastTextElement_EmojiSurrogatePair_RemovesCompleteSurrogatePair</code> @28, <code>DeleteLastTextElement_MyanmarTextElements_RemovesOneElementAtATime</code> @44, <code>DeleteGraphemeAt_BackspaceMiddleOfMyanmar_RemovesPrecedingTextElement</code> @68, <code>DeleteGraphemeAt_ForwardDeleteMiddleOfMyanmar_RemovesFollowingTextElement</code> @81, <code>GetPreviousAndNextGraphemeIndex_NavigatesClusterBoundaries</code> @93.

## GetSeek.AcceptanceTests.csproj {#src-6cdeb74d9739}

<code>Software/tests/GetSeek.AcceptanceTests/GetSeek.AcceptanceTests.csproj</code> · SHA-256 <code>9b29d74a7d1a51813049320501ac7c21205b2c42901dc698a01d0db5d5b619a7</code>.

## GetSeek.IntegrationTests.csproj {#src-ae399739da40}

<code>Software/tests/GetSeek.IntegrationTests/GetSeek.IntegrationTests.csproj</code> · SHA-256 <code>74984566219e3be0c0ffd842ff18a1dbf32b9c6c37b3d77131cd2955274eb202</code>.

## GetSeek.TestCrashHelper.csproj {#src-4bee98b787c5}

<code>Software/tests/GetSeek.TestCrashHelper/GetSeek.TestCrashHelper.csproj</code> · SHA-256 <code>d21e0c6dc3f6f4a1af08d24131902a4c4925484b3801d5a16e6287f1af4f9b14</code>.

## GetSeek.UnitTests.csproj {#src-37e72309093f}

<code>Software/tests/GetSeek.UnitTests/GetSeek.UnitTests.csproj</code> · SHA-256 <code>97dd47c568297639d6329121ed417221937a3dbb70766e664097f179b9d1027d</code>.
