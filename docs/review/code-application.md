---
id: PP-REVIEW-CODE-APPLICATION
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: []
---

# GetSeek.Application source catalogue

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.Application.csproj:1](code-application.md#src-ed9ddc91762e). Dependencies: <code>GetSeek.Domain</code>.

## CommandEnvelope.cs {#src-f6134145c44d}

<code>Software/src/GetSeek.Application/Abstractions/CommandEnvelope.cs</code> · 29 lines.

SHA-256: <code>fb1c88b9b92e28c2d68526a2cebff7214fa5f2e43cc28f57466d40e06de5478a</code>.

Declarations: <code>CommandEnvelope</code> (line 3), <code>CommandEnvelope</code> (line 13).

## CommandResult.cs {#src-09ff917bcd4c}

<code>Software/src/GetSeek.Application/Abstractions/CommandResult.cs</code> · 36 lines.

SHA-256: <code>ae12b3e9a17fa234e9dcdb5b74ea1c9aa444d0193ecf6a9393a4e5ab9c40e10b</code>.

Declarations: <code>CommandResult</code> (line 3), <code>CommandResult</code> (line 29).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5e6433fe5edc"></span><code>CommandResult.Success(T,string?)</code><br>22–23 | — | No extracted literal effects. |
| <span id="m-68609c3365af"></span><code>CommandResult.Failure(string,string,string?)</code><br>25–26 | ToString @26; NewGuid @26 | No extracted literal effects. |
| <span id="m-55a27e9627ac"></span><code>CommandResult.Success(T,string?)</code><br>31–32 | Success(T) @32 | No extracted literal effects. |
| <span id="m-88993c0be699"></span><code>CommandResult.Failure(string,string,string?)</code><br>34–35 | Failure(T) @35 | No extracted literal effects. |

</details>

## CommercialReadPorts.cs {#src-350569049712}

<code>Software/src/GetSeek.Application/Abstractions/CommercialReadPorts.cs</code> · 37 lines.

SHA-256: <code>26c764bca28752f0ef82fd28c9e2c1e888f1d9d7442a21f1a9fc75ee6a9bb08d</code>.

Declarations: <code>CommercialInvoiceRow</code> (line 4), <code>CommercialReadQuery</code> (line 7), <code>PurchaseInvoiceDetail</code> (line 8), <code>CommercialPartyChoice</code> (line 9), <code>CommercialItemChoice</code> (line 10), <code>CommercialDraftDetail</code> (line 12), <code>CommercialDraftLine</code> (line 14), <code>MoneyReadFilter</code> (line 16), <code>CommercialHistoryRow</code> (line 17), <code>UnshippedInvoiceLine</code> (line 18), <code>CommercialKitLeaf</code> (line 19), <code>ICommercialReader</code> (line 20).

<details markdown>
<summary>Methods, calls, table effects and failures (17)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7331a86f9f43"></span><code>CommercialPartyChoice.ToString()</code><br>9–9 | — | No extracted literal effects. |
| <span id="m-e20e08037f1e"></span><code>CommercialItemChoice.ToString()</code><br>11–11 | — | No extracted literal effects. |
| <span id="m-148ff27935e7"></span><code>ICommercialReader.GetInvoicesAsync(CommercialReadQuery,CancellationToken)</code><br>22–22 | — | No extracted literal effects. |
| <span id="m-7c7efa694f47"></span><code>ICommercialReader.GetPurchaseAsync(Guid,CancellationToken)</code><br>23–23 | — | No extracted literal effects. |
| <span id="m-3f9119c10adf"></span><code>ICommercialReader.GetUnshippedLinesAsync(Guid,CancellationToken)</code><br>24–24 | — | No extracted literal effects. |
| <span id="m-486d594c3e24"></span><code>ICommercialReader.GetReservationsAsync(Guid,CancellationToken)</code><br>25–25 | — | No extracted literal effects. |
| <span id="m-1f5aa7c2b15b"></span><code>ICommercialReader.GetShipmentsAsync(PageRequest,string,string,string,Guid?,CancellationToken)</code><br>26–26 | — | No extracted literal effects. |
| <span id="m-1b1bf0180303"></span><code>ICommercialReader.GetAccountsAsync(CancellationToken)</code><br>27–27 | — | No extracted literal effects. |
| <span id="m-13aea2b06557"></span><code>ICommercialReader.GetMoneyAsync(PageRequest,string,Guid?,MoneyReadFilter?,Guid?,CancellationToken)</code><br>28–28 | — | No extracted literal effects. |
| <span id="m-14e0863a36e3"></span><code>ICommercialReader.FindPartiesAsync(string,bool,CancellationToken)</code><br>29–29 | — | No extracted literal effects. |
| <span id="m-9426c42fe478"></span><code>ICommercialReader.GetPartyAsync(Guid,bool,CancellationToken)</code><br>30–30 | — | No extracted literal effects. |
| <span id="m-36d36159faa2"></span><code>ICommercialReader.GetKitLeavesAsync(Guid,decimal,string,CancellationToken)</code><br>31–31 | — | No extracted literal effects. |
| <span id="m-1e70e862f7cb"></span><code>ICommercialReader.FindItemsAsync(string,bool,CancellationToken)</code><br>32–32 | — | No extracted literal effects. |
| <span id="m-efe109683a26"></span><code>ICommercialReader.GetItemAsync(Guid,bool,CancellationToken)</code><br>33–33 | — | No extracted literal effects. |
| <span id="m-89a9682385a0"></span><code>ICommercialReader.GetSourceInvoicesAsync(Guid,string,CancellationToken)</code><br>34–34 | — | No extracted literal effects. |
| <span id="m-a6765f391186"></span><code>ICommercialReader.GetHistoryAsync(Guid,string,CancellationToken)</code><br>35–35 | — | No extracted literal effects. |
| <span id="m-1814035e33ed"></span><code>ICommercialReader.GetDraftAsync(Guid,bool,CancellationToken)</code><br>36–36 | — | No extracted literal effects. |

</details>

## CommonPorts.cs {#src-e1fe09e6338f}

<code>Software/src/GetSeek.Application/Abstractions/CommonPorts.cs</code> · 43 lines.

SHA-256: <code>91e2c7fdb9f3a59d22a09692e819c124243ad49b9cc4d8a56e1712d37100038f</code>.

Declarations: <code>IClock</code> (line 3), <code>SystemClock : IClock</code> (line 8), <code>IIdGenerator</code> (line 13), <code>ISessionContext</code> (line 19), <code>IPinHasher</code> (line 28), <code>IOperationalLogger</code> (line 40).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-346b19496d86"></span><code>IIdGenerator.NewGuid()</code><br>15–15 | — | No extracted literal effects. |
| <span id="m-18f7fcc6f5a8"></span><code>IIdGenerator.NewInvoiceNumber()</code><br>16–16 | — | No extracted literal effects. |
| <span id="m-f035b29b0e49"></span><code>ISessionContext.HasPermission(string)</code><br>24–24 | — | No extracted literal effects. |
| <span id="m-27ada265646a"></span><code>IPinHasher.HashPin(string)</code><br>30–30 | — | No extracted literal effects. |
| <span id="m-58b02b06b835"></span><code>IPinHasher.VerifyPin(string,string)</code><br>31–31 | — | No extracted literal effects. |
| <span id="m-3a318761fdd0"></span><code>IOperationalLogger.LogFailure(string,string,string,string,Exception?)</code><br>42–42 | — | No extracted literal effects. |

</details>

## ExpenseAttachmentPorts.cs {#src-fbb7356bbd3a}

<code>Software/src/GetSeek.Application/Abstractions/ExpenseAttachmentPorts.cs</code> · 42 lines.

SHA-256: <code>0e71646a550dc321503f9c8d8d20ccd3aeed0aee10f82e193d8bcd67fe75dc9e</code>.

Declarations: <code>PreparedAttachment</code> (line 3), <code>ExpenseAttachmentDetail</code> (line 10), <code>IExpenseAttachmentService</code> (line 23).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3c89ee24a14a"></span><code>IExpenseAttachmentService.PrepareAttachmentAsync(Stream,string,string?,CancellationToken)</code><br>25–29 | — | No extracted literal effects. |
| <span id="m-91e6a795ecbb"></span><code>IExpenseAttachmentService.GetCurrentAttachmentAsync(Guid,CancellationToken)</code><br>31–33 | — | No extracted literal effects. |
| <span id="m-17fc9e16bb88"></span><code>IExpenseAttachmentService.GetAttachmentByIdAsync(Guid,CancellationToken)</code><br>35–37 | — | No extracted literal effects. |
| <span id="m-d4d88cbe445a"></span><code>IExpenseAttachmentService.GetAttachmentHistoryAsync(Guid,CancellationToken)</code><br>39–41 | — | No extracted literal effects. |

</details>

## ExpenseReadPorts.cs {#src-75fbd1b57c5b}

<code>Software/src/GetSeek.Application/Abstractions/ExpenseReadPorts.cs</code> · 97 lines.

SHA-256: <code>f68a21785bcdde2ae62b83ab1a4a906df2589ea515db9122598f2e105a95b001</code>.

Declarations: <code>ExpenseReadQuery</code> (line 3), <code>ExpenseRow</code> (line 12), <code>ExpenseCategoryRow</code> (line 31), <code>ExpensePayeeChoice</code> (line 40), <code>ExpensePaymentRow</code> (line 48), <code>ExpenseDetail</code> (line 65), <code>IExpenseReader</code> (line 76).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e1835d3a13ad"></span><code>ExpensePayeeChoice.ToString()</code><br>45–45 | — | No extracted literal effects. |
| <span id="m-38f4d7898c50"></span><code>IExpenseReader.GetExpensesAsync(ExpenseReadQuery,CancellationToken)</code><br>78–80 | — | No extracted literal effects. |
| <span id="m-4832ca8ed700"></span><code>IExpenseReader.GetExpenseAsync(Guid,CancellationToken)</code><br>82–84 | — | No extracted literal effects. |
| <span id="m-e375625b041f"></span><code>IExpenseReader.GetCategoriesAsync(bool,CancellationToken)</code><br>86–88 | — | No extracted literal effects. |
| <span id="m-cf42db2921ba"></span><code>IExpenseReader.GetCategoryAsync(Guid,CancellationToken)</code><br>90–92 | — | No extracted literal effects. |
| <span id="m-bee3bd2af32c"></span><code>IExpenseReader.FindPayeesAsync(string,CancellationToken)</code><br>94–96 | — | No extracted literal effects. |

</details>

## ICommand.cs {#src-3e2467f1e295}

<code>Software/src/GetSeek.Application/Abstractions/ICommand.cs</code> · 48 lines.

SHA-256: <code>4e74857c9e63ada1e618b2e97786e1a8f496eaba650a824ecdad0820f15cd01e</code>.

Declarations: <code>ICommand</code> (line 3), <code>ICommand : ICommand</code> (line 11), <code>ISanitizedAuditPayload</code> (line 15), <code>CommandExtensions</code> (line 20).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-eec0be7c675c"></span><code>ISanitizedAuditPayload.GetSanitizedAuditPayload()</code><br>17–17 | — | No extracted literal effects. |
| <span id="m-57e7eb49777b"></span><code>CommandExtensions.GetAllRequiredPermissions(ICommand)</code><br>22–47 | IsNullOrWhiteSpace @26; Add @28; Trim @28; Trim @37; Contains @38 | No extracted literal effects. |

</details>

## IExportService.cs {#src-7209d0a91e9e}

<code>Software/src/GetSeek.Application/Abstractions/IExportService.cs</code> · 73 lines.

SHA-256: <code>31faff6b4027a806be66149621ccef756e2fa326af3bf3dd445b59271e500432</code>.

Declarations: <code>ExportDocumentType</code> (line 3), <code>ExportSelector</code> (line 12), <code>ReceiptExportSelector : ExportSelector</code> (line 17), <code>ShiftZReportExportSelector : ExportSelector</code> (line 19), <code>SalesReportExportSelector : ExportSelector</code> (line 21), <code>InventorySnapshotExportSelector : ExportSelector</code> (line 23), <code>ExportRequest</code> (line 25), <code>ExportPayload</code> (line 31), <code>ExportLine</code> (line 33), <code>ReceiptExportPayload : ExportPayload</code> (line 35), <code>ShiftReportExportPayload : ExportPayload</code> (line 50), <code>TabularExportPayload : ExportPayload</code> (line 58), <code>ExportTableRow</code> (line 62), <code>ExportResult</code> (line 64), <code>IExportService</code> (line 70).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-44605d58c8bb"></span><code>IExportService.ExportDocumentAsync(ExportRequest,CancellationToken)</code><br>72–72 | — | No extracted literal effects. |

</details>

## IPersistencePorts.cs {#src-b37728338f61}

<code>Software/src/GetSeek.Application/Abstractions/IPersistencePorts.cs</code> · 68 lines.

SHA-256: <code>3d89fdc95a5b743620dcb9527f52e7b46937852990102a85fe05c64bdedfc844</code>.

Declarations: <code>IUnitOfWork : IAsyncDisposable</code> (line 6), <code>IIdempotencyStore</code> (line 15), <code>IAuditJournalRepository</code> (line 29), <code>ILicenseService</code> (line 43), <code>HardwareJob</code> (line 50), <code>IHardwareJobRepository</code> (line 61).

<details markdown>
<summary>Methods, calls, table effects and failures (14)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-29e5791869b7"></span><code>IUnitOfWork.BeginTransactionAsync(CancellationToken)</code><br>10–10 | — | No extracted literal effects. |
| <span id="m-b31121d98741"></span><code>IUnitOfWork.CommitAsync(CancellationToken)</code><br>11–11 | — | No extracted literal effects. |
| <span id="m-58db8e4e6755"></span><code>IUnitOfWork.RollbackAsync(CancellationToken)</code><br>12–12 | — | No extracted literal effects. |
| <span id="m-a16a14f9213f"></span><code>IIdempotencyStore.CheckAsync(string,string,CancellationToken)</code><br>17–20 | — | No extracted literal effects. |
| <span id="m-a76c18080aba"></span><code>IIdempotencyStore.SaveAsync(string,string,string,CancellationToken)</code><br>22–26 | — | No extracted literal effects. |
| <span id="m-ef793a1768a3"></span><code>IAuditJournalRepository.AppendAsync(string,string?,string,string,string?,string,CancellationToken)</code><br>31–38 | — | No extracted literal effects. |
| <span id="m-efeccc5e6ea9"></span><code>IAuditJournalRepository.GetLatestEntryAsync(CancellationToken)</code><br>40–40 | — | No extracted literal effects. |
| <span id="m-90d0713e48f7"></span><code>ILicenseService.IsModuleLicensed(string)</code><br>45–45 | — | No extracted literal effects. |
| <span id="m-8e8492764fed"></span><code>ILicenseService.VerifyDeviceBinding()</code><br>46–46 | — | No extracted literal effects. |
| <span id="m-2e1b58b885e2"></span><code>ILicenseService.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>47–47 | — | No extracted literal effects. |
| <span id="m-8c997344a99a"></span><code>IHardwareJobRepository.EnqueueAsync(string,string,CancellationToken)</code><br>63–63 | — | No extracted literal effects. |
| <span id="m-47e0cc03d8a6"></span><code>IHardwareJobRepository.GetPendingAsync(int,CancellationToken)</code><br>64–64 | — | No extracted literal effects. |
| <span id="m-f054a359220c"></span><code>IHardwareJobRepository.MarkCompletedAsync(string,CancellationToken)</code><br>65–65 | — | No extracted literal effects. |
| <span id="m-1324a94f3fb0"></span><code>IHardwareJobRepository.MarkFailedAsync(string,string,CancellationToken)</code><br>66–66 | — | No extracted literal effects. |

</details>

## InvoiceAndRegisterReadPorts.cs {#src-52dfb030a0c7}

<code>Software/src/GetSeek.Application/Abstractions/InvoiceAndRegisterReadPorts.cs</code> · 33 lines.

SHA-256: <code>5d44dc77293fa558ae7c1e4b96492e284dcd86a3e0e365cf01b0d5d0ede406d7</code>.

Declarations: <code>InvoiceFilter</code> (line 6), <code>FinancialRegisterKind</code> (line 7), <code>InvoiceReadQuery</code> (line 8), <code>RegisterReadQuery</code> (line 9), <code>FinancialRegisterRow</code> (line 11), <code>ReturnableStock</code> (line 14), <code>ReturnableInvoiceLine</code> (line 16), <code>InvoiceDetail</code> (line 18), <code>RegisterMoneyTotal</code> (line 20), <code>RegisterPage</code> (line 21), <code>FinancialSourceFacts</code> (line 22), <code>IInvoiceAndRegisterReader</code> (line 25).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5592789d21ce"></span><code>IInvoiceAndRegisterReader.GetInvoicesAsync(InvoiceReadQuery,CancellationToken)</code><br>27–27 | — | No extracted literal effects. |
| <span id="m-dd9f655ac44e"></span><code>IInvoiceAndRegisterReader.GetSelectedInvoicesAsync(IReadOnlyList&lt;Guid&gt;,CancellationToken)</code><br>28–28 | — | No extracted literal effects. |
| <span id="m-95c7914650d8"></span><code>IInvoiceAndRegisterReader.GetInvoiceAsync(Guid,CancellationToken)</code><br>29–29 | — | No extracted literal effects. |
| <span id="m-804a71a7b7f3"></span><code>IInvoiceAndRegisterReader.GetRegisterAsync(RegisterReadQuery,CancellationToken)</code><br>30–30 | — | No extracted literal effects. |
| <span id="m-47fb28fa6f06"></span><code>IInvoiceAndRegisterReader.GetRegisterSourceAsync(FinancialRegisterKind,Guid,CancellationToken)</code><br>31–31 | — | No extracted literal effects. |
| <span id="m-3e06286fde03"></span><code>IInvoiceAndRegisterReader.PreviewReturnAsync(ProcessReturnCommand,CancellationToken)</code><br>32–32 | — | No extracted literal effects. |

</details>

## ManufacturingReadPorts.cs {#src-00906c4725eb}

<code>Software/src/GetSeek.Application/Abstractions/ManufacturingReadPorts.cs</code> · 105 lines.

SHA-256: <code>cd843c476a5c43f93cebaba40683578523cf249985cb4ffc9f527e81c23b736f</code>.

Declarations: <code>RecipeRow</code> (line 5), <code>ProductionRunRow</code> (line 18), <code>RecipeReadQuery</code> (line 33), <code>ProductionRunReadQuery</code> (line 45), <code>ManufacturingSortKeys</code> (line 57), <code>IManufacturingReader</code> (line 79).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7b73012b45e6"></span><code>IManufacturingReader.GetRecipesAsync(RecipeReadQuery,ISessionContext?,CancellationToken)</code><br>81–84 | — | No extracted literal effects. |
| <span id="m-9c75ec95d214"></span><code>IManufacturingReader.GetProductionRunsAsync(ProductionRunReadQuery,ISessionContext?,CancellationToken)</code><br>86–89 | — | No extracted literal effects. |
| <span id="m-4277ebc3cbf0"></span><code>IManufacturingReader.GetRecipeDetailAsync(Guid,ISessionContext?,CancellationToken)</code><br>91–94 | — | No extracted literal effects. |
| <span id="m-3a8252dd8af2"></span><code>IManufacturingReader.GetProductionRunDetailAsync(Guid,ISessionContext?,CancellationToken)</code><br>96–99 | — | No extracted literal effects. |
| <span id="m-7e373835f4a1"></span><code>IManufacturingReader.GetActiveRecipesForOutputAsync(Guid,ISessionContext?,CancellationToken)</code><br>101–104 | — | No extracted literal effects. |

</details>

## Paging.cs {#src-923e4baaa02e}

<code>Software/src/GetSeek.Application/Abstractions/Paging.cs</code> · 73 lines.

SHA-256: <code>5d208cf2457cf6de61c27e7bd18b1e5a634c11cfd1e79e89ce0c88c1a180dc78</code>.

Declarations: <code>SortDirection</code> (line 3), <code>PageRequest</code> (line 9), <code>PagedResult</code> (line 32), <code>BatchSelectionScope</code> (line 44), <code>SortKeyValidator</code> (line 46).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3b1d26e10e78"></span><code>SortKeyValidator.ResolveOrderBy(string?,SortDirection,IReadOnlyDictionary&lt;string, string&gt;,string)</code><br>54–72 | IsNullOrWhiteSpace @60; TryGetValue @65 | No extracted literal effects. |

</details>

## SalaryReadPorts.cs {#src-dadca15d7514}

<code>Software/src/GetSeek.Application/Abstractions/SalaryReadPorts.cs</code> · 176 lines.

SHA-256: <code>c0a6ff8d6bf5654f6e9929ad0309de0065f8c84fa926d97247ed79ee83aa2bbb</code>.

Declarations: <code>PersonSummaryRow</code> (line 5), <code>SalaryMonthRow</code> (line 23), <code>SalaryMonthSummary</code> (line 60), <code>SalaryAdjustmentRow</code> (line 69), <code>SalaryPaymentRow</code> (line 82), <code>SalaryLedgerRow</code> (line 99), <code>SalaryAgreementRow</code> (line 112), <code>SalaryPersonDetail</code> (line 124), <code>ISalaryReader</code> (line 132).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e170e7e12988"></span><code>ISalaryReader.GetPeopleAsync(PageRequest,string,bool?,CancellationToken)</code><br>134–138 | — | No extracted literal effects. |
| <span id="m-94f181bf8ae8"></span><code>ISalaryReader.GetPersonAsync(Guid,CancellationToken)</code><br>140–142 | — | No extracted literal effects. |
| <span id="m-3e2031ecb652"></span><code>ISalaryReader.GetMonthlyPayrollAsync(string,PageRequest,string,bool?,CancellationToken)</code><br>144–149 | — | No extracted literal effects. |
| <span id="m-8bfecdf0fac2"></span><code>ISalaryReader.GetMonthlyPayrollSummariesAsync(string,CancellationToken)</code><br>151–153 | — | No extracted literal effects. |
| <span id="m-4557090357d5"></span><code>ISalaryReader.GetPersonPayrollDetailAsync(Guid,string,CancellationToken)</code><br>155–158 | — | No extracted literal effects. |
| <span id="m-9781c2b89376"></span><code>ISalaryReader.GetAgreementsAsync(Guid,CancellationToken)</code><br>160–162 | — | No extracted literal effects. |
| <span id="m-f92bc3814453"></span><code>ISalaryReader.GetLedgerAsync(Guid,PageRequest,CancellationToken)</code><br>164–167 | — | No extracted literal effects. |
| <span id="m-a8899089f0ef"></span><code>ISalaryReader.GetSalaryStatementAsync(Guid,string,CancellationToken)</code><br>169–172 | — | No extracted literal effects. |
| <span id="m-5ec3486a9c73"></span><code>ISalaryReader.GetEarliestPayrollMonthAsync(CancellationToken)</code><br>174–175 | — | No extracted literal effects. |

</details>

## SearchReadPorts.cs {#src-f5485780db31}

<code>Software/src/GetSeek.Application/Abstractions/SearchReadPorts.cs</code> · 158 lines.

SHA-256: <code>cd1f8b7437035e56b67640938d15d4f7f9153870934c3590d556d0a3202bc9f4</code>.

Declarations: <code>SearchContext</code> (line 3), <code>SearchEntityKey</code> (line 27), <code>SearchSuggestion</code> (line 38), <code>SearchRequest</code> (line 44), <code>SearchUseRequest</code> (line 74), <code>ISearchSuggestionReader</code> (line 80), <code>ISearchUsageWriter</code> (line 87), <code>ThirdPartySearchScope</code> (line 95), <code>InventoryItemSearchScope</code> (line 101), <code>RecipeSearchScope</code> (line 110), <code>ProductionRunSearchScope</code> (line 116), <code>CommercialInvoiceSearchScope</code> (line 122), <code>ShipmentSearchScope</code> (line 131), <code>MoneySearchScope</code> (line 136), <code>FinancialRegisterSearchScope</code> (line 144), <code>SalaryPeopleSearchScope</code> (line 150), <code>ExpensesSearchScope</code> (line 154).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-44f742bdbc60"></span><code>SearchEntityKey.FromGuid(string,Guid)</code><br>29–30 | ToString @30 | No extracted literal effects. |
| <span id="m-ace1e82f40d3"></span><code>SearchEntityKey.TryGetGuid(Guid)</code><br>32–33 | TryParse @33 | No extracted literal effects. |
| <span id="m-b37cc28ab404"></span><code>SearchEntityKey.ToString()</code><br>35–35 | — | No extracted literal effects. |
| <span id="m-4b6402f4e3ad"></span><code>SearchRequest.ClampLimit(int)</code><br>67–71 | Clamp @70 | No extracted literal effects. |
| <span id="m-f650cc7e1d78"></span><code>ISearchSuggestionReader.GetSuggestionsAsync(SearchRequest,CancellationToken)</code><br>82–84 | — | No extracted literal effects. |
| <span id="m-f0049ab54bfc"></span><code>ISearchUsageWriter.RecordUseAsync(SearchUseRequest,CancellationToken)</code><br>89–91 | — | No extracted literal effects. |

</details>

## StoreTimeHelper.cs {#src-2ae52f322d89}

<code>Software/src/GetSeek.Application/Abstractions/StoreTimeHelper.cs</code> · 85 lines.

SHA-256: <code>c4dd90a8971e88975c3f1c065451275618bb2a107e0fa6dfaa4c1d8cafdcb966</code>.

Declarations: <code>StoreTimeHelper</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e84910ed149e"></span><code>StoreTimeHelper.GetStoreTimeZoneAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>8–19 | CreateCommand @13; ConfigureAwait @16; ExecuteScalarAsync @16; ToString @17; ResolveTimeZone @18 | FROM store_config @15 |
| <span id="m-ae75d495dbb4"></span><code>StoreTimeHelper.ResolveTimeZone(string?)</code><br>21–40 | IsNullOrWhiteSpace @23; FindSystemTimeZoneById @30; Trim @30 | No extracted literal effects. |
| <span id="m-5d1edf83003e"></span><code>StoreTimeHelper.ToStoreLocalTime(DateTime,TimeZoneInfo)</code><br>42–46 | SpecifyKind @44; ConvertTimeFromUtc @45 | No extracted literal effects. |
| <span id="m-69bbcbfcac51"></span><code>StoreTimeHelper.GetStoreLocalDate(DateTime,TimeZoneInfo)</code><br>48–52 | ToStoreLocalTime @50; FromDateTime @51 | No extracted literal effects. |
| <span id="m-c9b46c1043bb"></span><code>StoreTimeHelper.GetStoreLocalMonth(DateTime,TimeZoneInfo)</code><br>54–58 | ToStoreLocalTime @56; ToString @57 | No extracted literal effects. |
| <span id="m-75f96fee4ae1"></span><code>StoreTimeHelper.GetLocalMonthUtcBounds(string,TimeZoneInfo)</code><br>60–72 | Parse @62; AddMonths @66; ConvertLocalToUtc @68 | No extracted literal effects. |
| <span id="m-c86b830102fb"></span><code>StoreTimeHelper.ConvertLocalToUtc(DateTime,TimeZoneInfo)</code><br>74–84 | Equals @76; SpecifyKind @78; GetUtcOffset @81 | No extracted literal effects. |

</details>

## TeamsReadPorts.cs {#src-7e9f9df27fa4}

<code>Software/src/GetSeek.Application/Abstractions/TeamsReadPorts.cs</code> · 78 lines.

SHA-256: <code>b1535f0545894643fd5a7271e96d8e295287186231a1633e5c2d5b542f99b530</code>.

Declarations: <code>TeamMemberRow</code> (line 5), <code>UserPermissionOverrideInput</code> (line 30), <code>TeamMemberDetail</code> (line 35), <code>TeamPersonSection</code> (line 40), <code>TeamLoginSection</code> (line 49), <code>TeamSalarySection</code> (line 57), <code>ITeamsReader</code> (line 67).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a8be969f4458"></span><code>ITeamsReader.GetTeamMembersAsync(PageRequest,string,bool?,CancellationToken)</code><br>69–73 | — | No extracted literal effects. |
| <span id="m-917d2cba0f28"></span><code>ITeamsReader.GetTeamMemberDetailAsync(string,CancellationToken)</code><br>75–77 | — | No extracted literal effects. |

</details>

## BatchCommandHandler.cs {#src-c097cf593496}

<code>Software/src/GetSeek.Application/Batch/BatchCommandHandler.cs</code> · 569 lines.

SHA-256: <code>e8d5dcf16fc2e5c317fd4e968679777765ff8987f3910e9e767d9c3759dc361b</code>.

Declarations: <code>BatchCommandHandler : ICommandHandler&lt;BatchUpdateItemStatusCommand, BatchResult&gt;, ICommandHandler&lt;BatchAssignItemCategoryCommand, BatchResult&gt;, ICommandHandler&lt;BatchAssignItemPurposeCommand, BatchResult&gt;, ICommandHandler&lt;BatchUpdateThirdPartyStatusCommand, BatchResult&gt;, ICommandHandler&lt;BatchAssignThirdPartyCategoryCommand, BatchResult&gt;, ICommandHandler&lt;BatchAssignThirdPartyPriceLevelCommand, BatchResult&gt;, ICommandHandler&lt;BatchUpdateUserStatusCommand, BatchResult&gt;, ICommandHandler&lt;BatchCancelBomDraftsCommand, BatchResult&gt;, ICommandHandler&lt;BatchUpdateUnitStatusCommand, BatchResult&gt;, ICommandHandler&lt;BatchUpdateCategoryStatusCommand, BatchResult&gt;, ICommandHandler&lt;BatchUpdateExpenseCategoryStatusCommand, BatchResult&gt;, ICommandHandler&lt;BatchDeleteUnitDefinitionsCommand, BatchResult&gt;, ICommandHandler&lt;BatchDeleteCategoryDefinitionsCommand, BatchResult&gt;</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (21)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0831dacd53c6"></span><code>BatchCommandHandler.ValidatePreviewAsync(BatchSelectionScope,BatchPreviewTarget,string,bool?,string?,Guid,DateTime,CancellationToken,string?,string?)</code><br>25–37 | OperationParametersJson @31; ConfigureAwait @32; ValidateAsync @32; ToList @36 | No extracted literal effects. |
| <span id="m-71d2543de647"></span><code>BatchCommandHandler.ConsumePreviewAsync(Guid,string,DateTime,CancellationToken)</code><br>39–41 | ConsumeAsync @40; ToString @41 | No extracted literal effects. |
| <span id="m-bf46ade28a29"></span><code>BatchCommandHandler.HandleAsync(BatchUpdateItemStatusCommand,CommandEnvelope&lt;BatchUpdateItemStatusCommand&gt;,CancellationToken)</code><br>43–64 | ConfigureAwait @47; ValidatePreviewAsync @47; Failure(BatchResult) @50; Chunk @52; CreateCommand @54; BuildInClause @56; AddParam @58; ExecuteNonQueryAsync @59; ConsumePreviewAsync @62; Success(BatchResult) @63 | DYNAMIC SQL: inspect manually |
| <span id="m-1536789d0047"></span><code>BatchCommandHandler.HandleAsync(BatchAssignItemCategoryCommand,CommandEnvelope&lt;BatchAssignItemCategoryCommand&gt;,CancellationToken)</code><br>66–98 | ConfigureAwait @70; ValidatePreviewAsync @70; Failure(BatchResult) @73; CreateCommand @76; AddParam @80; ToInt64 @81; ExecuteScalarAsync @81; Chunk @86; BuildInClause @90; ExecuteNonQueryAsync @93; ConsumePreviewAsync @96; Success(BatchResult) @97 | FROM product_categories @79 · CATEGORY_INACTIVE @82 · DYNAMIC SQL: inspect manually |
| <span id="m-2a12d4cac844"></span><code>BatchCommandHandler.HandleAsync(BatchAssignItemPurposeCommand,CommandEnvelope&lt;BatchAssignItemPurposeCommand&gt;,CancellationToken)</code><br>100–129 | Trim @102; Failure(BatchResult) @104; ConfigureAwait @108; ValidatePreviewAsync @108; ContainsActiveKitParentAsync @113; Chunk @117; CreateCommand @119; BuildInClause @121; AddParam @123; ExecuteNonQueryAsync @124; ConsumePreviewAsync @127; Success(BatchResult) @128 | INVALID_PRODUCT_PURPOSE @104; KIT_PURPOSE_INVALID @114 · DYNAMIC SQL: inspect manually |
| <span id="m-43341c26fe29"></span><code>BatchCommandHandler.HandleAsync(BatchUpdateThirdPartyStatusCommand,CommandEnvelope&lt;BatchUpdateThirdPartyStatusCommand&gt;,CancellationToken)</code><br>131–157 | ConfigureAwait @135; ValidatePreviewAsync @135; Failure(BatchResult) @138; ContainsSystemWalkInAsync @139; ToString @143; Chunk @144; CreateCommand @146; BuildInClause @148; AddParam @150; ExecuteNonQueryAsync @152; ConsumePreviewAsync @155; Success(BatchResult) @156 | SYSTEM_WALK_IN_PROTECTED @140 · DYNAMIC SQL: inspect manually |
| <span id="m-b9355154b74c"></span><code>BatchCommandHandler.HandleAsync(BatchAssignThirdPartyCategoryCommand,CommandEnvelope&lt;BatchAssignThirdPartyCategoryCommand&gt;,CancellationToken)</code><br>159–183 | ConfigureAwait @163; ValidatePreviewAsync @163; Failure(BatchResult) @166; ContainsSystemWalkInAsync @167; Chunk @171; CreateCommand @173; BuildInClause @175; AddParam @177; Trim @177; ExecuteNonQueryAsync @178; ConsumePreviewAsync @181; Success(BatchResult) @182 | SYSTEM_WALK_IN_PROTECTED @168 · DYNAMIC SQL: inspect manually |
| <span id="m-e6ad5045d4b3"></span><code>BatchCommandHandler.HandleAsync(BatchAssignThirdPartyPriceLevelCommand,CommandEnvelope&lt;BatchAssignThirdPartyPriceLevelCommand&gt;,CancellationToken)</code><br>185–221 | ToLowerInvariant @189; Trim @189; ConfigureAwait @190; ValidatePreviewAsync @190; Failure(BatchResult) @193; ContainsSystemWalkInAsync @194; CreateCommand @197; AddParam @201; IsNullOrWhiteSpace @202; ToInt64 @202; ExecuteScalarAsync @202; ToString @207; Chunk @208; BuildInClause @212; ExecuteNonQueryAsync @216; ConsumePreviewAsync @219; Success(BatchResult) @220 | FROM price_level_settings @200 · SYSTEM_WALK_IN_PROTECTED @195; INVALID_PRICE_LEVEL @203 · DYNAMIC SQL: inspect manually |
| <span id="m-15aea3888154"></span><code>BatchCommandHandler.HandleAsync(BatchUpdateUserStatusCommand,CommandEnvelope&lt;BatchUpdateUserStatusCommand&gt;,CancellationToken)</code><br>223–286 | ConfigureAwait @227; ValidatePreviewAsync @227; Failure(BatchResult) @230; CreateCommand @235; ToInt64 @243; ExecuteScalarAsync @243; BuildInClause @247; ExecuteScalarAsync @254; ExecuteScalarAsync @266; Chunk @274; AddParam @280; ExecuteNonQueryAsync @281; ConsumePreviewAsync @284; Success(BatchResult) @285 | FROM users @237; JOIN user_roles @237 · LAST_ADMIN_PROTECTED @258; ON_SHIFT_CASHIER_PROTECTED @269 · DYNAMIC SQL: inspect manually |
| <span id="m-c13a520aab91"></span><code>BatchCommandHandler.HandleAsync(BatchCancelBomDraftsCommand,CommandEnvelope&lt;BatchCancelBomDraftsCommand&gt;,CancellationToken)</code><br>288–320 | ConfigureAwait @292; ValidatePreviewAsync @292; Failure(BatchResult) @295; CreateCommand @298; BuildInClause @300; ToInt64 @302; ExecuteScalarAsync @302; Chunk @309; ExecuteNonQueryAsync @315; ConsumePreviewAsync @318; Success(BatchResult) @319 | BOM_NOT_DRAFT @305 · DYNAMIC SQL: inspect manually |
| <span id="m-1553251d833e"></span><code>BatchCommandHandler.HandleAsync(BatchUpdateUnitStatusCommand,CommandEnvelope&lt;BatchUpdateUnitStatusCommand&gt;,CancellationToken)</code><br>322–366 | ConfigureAwait @326; IsActiveAdminAsync @326; Failure(BatchResult) @327; ValidatePreviewAsync @328; CreateCommand @336; BuildInClause @338; ToInt64 @347; ExecuteScalarAsync @347; Chunk @354; AddParam @360; ExecuteNonQueryAsync @361; ConsumePreviewAsync @364; Success(BatchResult) @365 | ADMIN_REQUIRED @327; UNIT_IN_USE @349 · DYNAMIC SQL: inspect manually |
| <span id="m-4fb69efebb75"></span><code>BatchCommandHandler.HandleAsync(BatchUpdateCategoryStatusCommand,CommandEnvelope&lt;BatchUpdateCategoryStatusCommand&gt;,CancellationToken)</code><br>368–405 | ConfigureAwait @372; IsActiveAdminAsync @372; Failure(BatchResult) @373; ValidatePreviewAsync @374; CreateCommand @382; BuildInClause @384; ToInt64 @386; ExecuteScalarAsync @386; Chunk @393; AddParam @399; ExecuteNonQueryAsync @400; ConsumePreviewAsync @403; Success(BatchResult) @404 | ADMIN_REQUIRED @373; CATEGORY_IN_USE @388 · DYNAMIC SQL: inspect manually |
| <span id="m-e793003a1056"></span><code>BatchCommandHandler.HandleAsync(BatchUpdateExpenseCategoryStatusCommand,CommandEnvelope&lt;BatchUpdateExpenseCategoryStatusCommand&gt;,CancellationToken)</code><br>407–438 | ConfigureAwait @411; ValidatePreviewAsync @411; Failure(BatchResult) @414; ToString @416; Chunk @418; CreateCommand @420; BuildInClause @422; AddParam @430; ToString @431; ExecuteNonQueryAsync @433; ConsumePreviewAsync @436; Success(BatchResult) @437 | DYNAMIC SQL: inspect manually |
| <span id="m-a552049bc2a9"></span><code>BatchCommandHandler.HandleAsync(BatchDeleteUnitDefinitionsCommand,CommandEnvelope&lt;BatchDeleteUnitDefinitionsCommand&gt;,CancellationToken)</code><br>440–468 | ConfigureAwait @444; IsActiveAdminAsync @444; Failure(BatchResult) @445; ValidatePreviewAsync @446; ReadRegistryDeleteStateAsync @451; Chunk @457; CreateCommand @459; BuildInClause @461; ExecuteNonQueryAsync @463; ConsumePreviewAsync @466; Success(BatchResult) @467 | ADMIN_REQUIRED @445; BATCH_SELECTION_STALE @452; UOM_BUILTIN @453; UOM_DEFINITION_IN_USE @454; BATCH_SELECTION_STALE @465 · DYNAMIC SQL: inspect manually |
| <span id="m-8296ae07e6a7"></span><code>BatchCommandHandler.HandleAsync(BatchDeleteCategoryDefinitionsCommand,CommandEnvelope&lt;BatchDeleteCategoryDefinitionsCommand&gt;,CancellationToken)</code><br>470–498 | ConfigureAwait @474; IsActiveAdminAsync @474; Failure(BatchResult) @475; ValidatePreviewAsync @476; ReadRegistryDeleteStateAsync @481; Chunk @487; CreateCommand @489; BuildInClause @491; ExecuteNonQueryAsync @493; ConsumePreviewAsync @496; Success(BatchResult) @497 | ADMIN_REQUIRED @475; BATCH_SELECTION_STALE @482; CATEGORY_BUILTIN @483; CATEGORY_IN_USE @484; BATCH_SELECTION_STALE @495 · DYNAMIC SQL: inspect manually |
| <span id="m-80112fe4c253"></span><code>BatchCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>500–508 | CreateCommand @502; AddParam @506; ToString @506; ToInt32 @507; ConfigureAwait @507; ExecuteScalarAsync @507 | FROM users @504; JOIN user_roles @504 |
| <span id="m-3d6d97138c8a"></span><code>BatchCommandHandler.BuildInClause(DbCommand,IEnumerable&lt;string&gt;,string)</code><br>510–523 | Append @516; AddParam @519; ToString @522 | No extracted literal effects. |
| <span id="m-691d131c742e"></span><code>BatchCommandHandler.ContainsSystemWalkInAsync(DbConnection,DbTransaction?,List&lt;string&gt;,CancellationToken)</code><br>525–538 | Any @527; TryParse @527; Chunk @528; CreateCommand @530; BuildInClause @532; ToInt32 @534; ConfigureAwait @534; ExecuteScalarAsync @534 | DYNAMIC SQL: inspect manually |
| <span id="m-7a934b57d0b6"></span><code>BatchCommandHandler.ContainsActiveKitParentAsync(DbConnection,DbTransaction?,List&lt;string&gt;,CancellationToken)</code><br>540–552 | Chunk @542; CreateCommand @544; BuildInClause @546; ToInt32 @548; ConfigureAwait @548; ExecuteScalarAsync @548 | DYNAMIC SQL: inspect manually |
| <span id="m-3464348508fd"></span><code>BatchCommandHandler.AddParam(DbCommand,string,object)</code><br>554–560 | CreateParameter @556; Add @559 | No extracted literal effects. |
| <span id="m-3a89faf69339"></span><code>BatchCommandHandler.Chunk(List&lt;T&gt;,int)</code><br>562–568 | GetRange @566; Min @566 | No extracted literal effects. |

</details>

## BatchCommands.cs {#src-417825b8e887}

<code>Software/src/GetSeek.Application/Batch/BatchCommands.cs</code> · 103 lines.

SHA-256: <code>0554cf67ab3ff722ab7a6bb835bbf2c8ed093ec3508bd417033bde6716c17561</code>.

Declarations: <code>BatchResult</code> (line 6), <code>BatchUpdateItemStatusCommand : ICommand&lt;BatchResult&gt;</code> (line 8), <code>BatchAssignItemCategoryCommand : ICommand&lt;BatchResult&gt;</code> (line 16), <code>BatchAssignItemPurposeCommand : ICommand&lt;BatchResult&gt;</code> (line 24), <code>BatchUpdateThirdPartyStatusCommand : ICommand&lt;BatchResult&gt;</code> (line 32), <code>BatchAssignThirdPartyCategoryCommand : ICommand&lt;BatchResult&gt;</code> (line 40), <code>BatchAssignThirdPartyPriceLevelCommand : ICommand&lt;BatchResult&gt;</code> (line 48), <code>BatchUpdateUserStatusCommand : ICommand&lt;BatchResult&gt;</code> (line 56), <code>BatchCancelBomDraftsCommand : ICommand&lt;BatchResult&gt;</code> (line 64), <code>BatchUpdateUnitStatusCommand : ICommand&lt;BatchResult&gt;</code> (line 71), <code>BatchUpdateCategoryStatusCommand : ICommand&lt;BatchResult&gt;</code> (line 79), <code>BatchDeleteUnitDefinitionsCommand : ICommand&lt;BatchResult&gt;</code> (line 87), <code>BatchDeleteCategoryDefinitionsCommand : ICommand&lt;BatchResult&gt;</code> (line 92), <code>BatchUpdateExpenseCategoryStatusCommand : ICommand&lt;BatchResult&gt;</code> (line 97).

## BatchPreview.cs {#src-6d6431af2d8b}

<code>Software/src/GetSeek.Application/Batch/BatchPreview.cs</code> · 688 lines.

SHA-256: <code>1053ef4233777a81107c51558e6f239da26f88a22f43fcdc317adf2e59decbe7</code>.

Declarations: <code>BatchPreviewTarget</code> (line 15), <code>BatchPreviewSelectionMode</code> (line 16), <code>BatchPricingOptions</code> (line 18), <code>BatchPreviewSample</code> (line 27), <code>BatchPreviewChange</code> (line 34), <code>BatchPreviewResult</code> (line 36), <code>CreateBatchPreviewCommand : ICommand&lt;BatchPreviewResult&gt;</code> (line 51), <code>BatchPreviewHasher</code> (line 73), <code>CreateBatchPreviewCommandHandler : ICommandHandler&lt;CreateBatchPreviewCommand, BatchPreviewResult&gt;</code> (line 101), <code>BatchPreviewValidation</code> (line 348), <code>BatchPreviewStore</code> (line 355), <code>RegistryDeleteState</code> (line 357), <code>CandidateResolution</code> (line 359).

<details markdown>
<summary>Methods, calls, table effects and failures (15)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-439a843fc220"></span><code>BatchPreviewHasher.HashFields(string[])</code><br>75–88 | Write @79; GetBytes @82; Flush @86; ToLowerInvariant @87; ToHexString @87; HashData @87; ToArray @87 | No extracted literal effects. |
| <span id="m-b9686a0565e3"></span><code>BatchPreviewHasher.HashSelection(string,string,string,IReadOnlyList&lt;string&gt;)</code><br>90–95 | ToString @92; AddRange @93; HashFields @94; ToArray @94 | No extracted literal effects. |
| <span id="m-01af5f0e038e"></span><code>BatchPreviewHasher.HashOperation(string,string,string)</code><br>97–98 | HashFields @98 | No extracted literal effects. |
| <span id="m-4de338edaddb"></span><code>CreateBatchPreviewCommandHandler.HandleAsync(CreateBatchPreviewCommand,CommandEnvelope&lt;CreateBatchPreviewCommand&gt;,CancellationToken)</code><br>104–345 | GetTable @109; IsSupportedOperation @110; Failure(BatchPreviewResult) @111; ConfigureAwait @122; ResolveCandidatesAsync @122; OperationParametersJson @131; HashOperation @134; ToString @134; HashSelection @135; Empty(BatchPreviewSample) @139; Empty(BatchPreviewChange) @140; CalculateAsync @145; SequenceEqual @148; Serialize @155; TryParse @161; CreateCommand @163; Add @166; ToInt64 @167; ExecuteScalarAsync @167; ToArray @175; Take @175; ToString @181; Add @182; Join @191; ExecuteReaderAsync @210; ReadAsync @212; Add @213; GetString @213; ToLowerInvariant @225; Trim @225; IsNullOrWhiteSpace @226; ExecuteScalarAsync @232; ComputeThirdPartyStateFingerprintAsync @236; Trim @258; EndsWith @273; ComputeRegistryDeleteFingerprintAsync @275; ReadRegistryDeleteStateAsync @281; Skip @296; NewGuid @310; AddMinutes @312; ToString @320; ToString @321; ToString @322; ToString @323; ToString @326; ExecuteNonQueryAsync @334; Success(BatchPreviewResult) @342 | FROM price_level_settings @230; FROM product_categories @165; INSERT INTO batch_previews @315 · BATCH_SCOPE_MISMATCH @111; BATCH_PREVIEW_REQUIRED @114; BATCH_SCOPE_MISMATCH @116; BATCH_SCOPE_MISMATCH @118; BATCH_PREVIEW_REQUIRED @128; BATCH_SELECTION_STALE @149; CATEGORY_NOT_FOUND @162; CATEGORY_INACTIVE @168; INVALID_PRODUCT_PURPOSE @172; BATCH_SCOPE_MISMATCH @221; INVALID_PRICE_LEVEL @227; INVALID_PRICE_LEVEL @233; BATCH_SCOPE_MISMATCH @274 · DYNAMIC SQL: inspect manually |
| <span id="m-4be9b935da89"></span><code>BatchPreviewStore.GetTable(BatchPreviewTarget)</code><br>361–371 | nameof @370 | No extracted literal effects. |
| <span id="m-9dcfe50e7c8f"></span><code>BatchPreviewStore.IsSupportedOperation(BatchPreviewTarget,string)</code><br>373–390 | — | No extracted literal effects. |
| <span id="m-71c9c6b038a7"></span><code>BatchPreviewStore.OperationParametersJson(BatchPreviewTarget,string,bool?,string?,BatchPricingOptions?,string?,string?)</code><br>392–407 | Serialize @393; ToString @395; ToString @396; Trim @397; ToLowerInvariant @398 | No extracted literal effects. |
| <span id="m-1ca726419f09"></span><code>BatchPreviewStore.ResolveCandidatesAsync(DbConnection,DbTransaction?,BatchPreviewTarget,BatchPreviewSelectionMode,IReadOnlyList&lt;string&gt;?,string?,string?,CancellationToken)</code><br>409–466 | GetTable @414; CreateCommand @417; ToArray(string) @421; OrderBy(string) @421; Distinct(string) @421; Select(string) @421; Where(string) @421; Empty(string) @421; IsNullOrWhiteSpace @421; Trim @421; ToString @426; Add @427; Add @428; Join @430; Serialize @431; Create @440; AddParameters @444; ToBatchFilterJson @445; ConfigureAwait @454; ExecuteReaderAsync @454; ReadAsync @456; Add @456; GetString @456; Count @459; Distinct @459; Select @459; Where @459; Sort @461; ContainsProtectedWalkInAsync @463 | FROM items @435 · DYNAMIC SQL: inspect manually |
| <span id="m-fa243973e336"></span><code>BatchPreviewStore.ComputeThirdPartyStateFingerprintAsync(DbConnection,DbTransaction?,IReadOnlyList&lt;string&gt;,CancellationToken)</code><br>468–497 | Chunk @472; CreateCommand @474; ToString @479; Add @480; Add @481; Join @484; ConfigureAwait @485; ExecuteReaderAsync @485; ReadAsync @486; Add @488; GetString @488; ToString @491; GetInt32 @491; HashFields @496; ToArray @496 | DYNAMIC SQL: inspect manually |
| <span id="m-7e05945c0cbe"></span><code>BatchPreviewStore.ComputeRegistryDeleteFingerprintAsync(DbConnection,DbTransaction?,BatchPreviewTarget,IReadOnlyList&lt;string&gt;,CancellationToken)</code><br>499–517 | ConfigureAwait @506; ReadRegistryDeleteStateAsync @506; Add @508; ToString @512; ToString @513; Insert @515; ToString @515; HashFields @516; ToArray @516 | No extracted literal effects. |
| <span id="m-4c4a5b2793b1"></span><code>BatchPreviewStore.ReadRegistryDeleteStateAsync(DbConnection,DbTransaction?,BatchPreviewTarget,string,CancellationToken)</code><br>519–567 | CreateCommand @522; Add @531; ConfigureAwait @564; ExecuteReaderAsync @564; ReadAsync @565; GetString @566; GetInt32 @566; GetInt64 @566 | FROM barcodes @543; FROM bom_items @543; FROM draft_cart_lines @543; FROM expense_categories @535; FROM expense_records @535; FROM item_kit_components @543; FROM item_price_history @543; FROM items @526; FROM items @543; FROM product_categories @526; FROM product_category_pricing_rules @526; FROM production_run_inputs @543; FROM production_run_outputs @543; FROM sales_lines @543; FROM stock_movements @543; FROM store_uom_preferences @543; FROM uom_dimensions @543; FROM uoms @543 |
| <span id="m-c8f393adfda6"></span><code>BatchPreviewStore.ContainsProtectedWalkInAsync(DbConnection,DbTransaction?,IReadOnlyList&lt;string&gt;,CancellationToken)</code><br>569–588 | Any @571; TryParse @571; Chunk @572; CreateCommand @574; ToString @579; Add @580; Add @581; Join @583; ToInt32 @584; ConfigureAwait @584; ExecuteScalarAsync @584 | DYNAMIC SQL: inspect manually |
| <span id="m-be555f90de87"></span><code>BatchPreviewStore.ValidateAsync(DbConnection,DbTransaction?,Guid?,BatchPreviewTarget,string,string,Guid,DateTime,CancellationToken)</code><br>590–671 | CreateCommand @596; Add @602; ToString @602; ConfigureAwait @606; ExecuteReaderAsync @606; ReadAsync @608; GetString @609; GetInt32 @611; IsDBNull @612; TryParse @615; ToString @616; Equals @618; HashOperation @618; TryParse @621; TryParse(BatchPreviewSelectionMode) @623; Deserialize(List&lt;string&gt;, string) @624; Parse @629; TryGetProperty @632; GetString @632; GetString @633; ResolveCandidatesAsync @636; SequenceEqual @637; HashSelection @639; TryGetProperty @647; GetString @648; IsNullOrWhiteSpace @651; ComputeThirdPartyStateFingerprintAsync @652; ComputeRegistryDeleteFingerprintAsync @667 | FROM batch_previews @598 |
| <span id="m-8729063e568f"></span><code>BatchPreviewStore.ConsumeAsync(DbConnection,DbTransaction?,Guid,string,DateTime,CancellationToken)</code><br>673–682 | CreateCommand @675; Add @678; ToString @678; ToString @680; ConfigureAwait @681; ExecuteNonQueryAsync @681 | UPDATE batch_previews @677 · InvalidOperationException @681 |
| <span id="m-9af86aa664de"></span><code>BatchPreviewStore.Add(DbCommand,string,object)</code><br>684–687 | CreateParameter @686; Add @686 | No extracted literal effects. |

</details>

## AccountPostingService.cs {#src-6165ea6142ad}

<code>Software/src/GetSeek.Application/Cash/AccountPostingService.cs</code> · 187 lines.

SHA-256: <code>03064d4c5ca4d335bdb72fb6ca3e30130f7ef48f2ca66204aa18d41666bd30bd</code>.

Declarations: <code>AccountPostingRequest</code> (line 7), <code>IAccountPostingService</code> (line 21), <code>AccountPostingService : IAccountPostingService</code> (line 43).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-2eef2e17e517"></span><code>IAccountPostingService.PostAsync(AccountPostingRequest,CancellationToken)</code><br>23–25 | — | No extracted literal effects. |
| <span id="m-7af20577388f"></span><code>IAccountPostingService.PostAsync(IReadOnlyDictionary&lt;string, object?&gt;,long,string,Guid,string,string,Guid?,Guid,string,DateTime,Guid?,Guid?,CancellationToken)</code><br>27–40 | — | No extracted literal effects. |
| <span id="m-72d17e2989be"></span><code>AccountPostingService.PostAsync(AccountPostingRequest,CancellationToken)</code><br>45–71 | ConfigureAwait @51; ReadAsync @51; Failure(Guid) @54; PostAsync @57 | FROM money_accounts @51 · ACCOUNT_NOT_FOUND @54 |
| <span id="m-475cf82911f1"></span><code>AccountPostingService.PostAsync(IReadOnlyDictionary&lt;string, object?&gt;,long,string,Guid,string,string,Guid?,Guid,string,DateTime,Guid?,Guid?,CancellationToken)</code><br>73–186 | IsNullOrWhiteSpace @88; Failure(Guid) @90; Text @95; ConfigureAwait @104; ReadAsync @104; Amount @114; Trim @127; WriteCashMovementAsync @152; Trim @163; NewGuid @167; ExecuteAsync @168; Success(Guid) @185 | FROM cash_movements @108; FROM invoice_collections @122; FROM money_events @109; FROM money_events @122; FROM sale_returns @122; FROM sales_tenders @122; FROM shifts @140; INSERT INTO money_events @168 · REASON_REQUIRED @90; BANK_CONFIRMATION_REQUIRED @99; INSUFFICIENT_ACCOUNT_FUNDS @116; DUPLICATE_PAYMENT_REFERENCE @131; SHIFT_NOT_OPEN @149 |

</details>

## CashLossCommandHandler.cs {#src-77895c61e718}

<code>Software/src/GetSeek.Application/Cash/CashLossCommandHandler.cs</code> · 65 lines.

SHA-256: <code>92cfe63f7cfb11b436e2414a56bcefa7dc628b10b156b2660808ba06341a2225</code>.

Declarations: <code>CashLossCommandHandler : ICommandHandler&lt;RecordKnownCashLossCommand,CashLossResult&gt;, ICommandHandler&lt;CorrectCashLossRecordCommand,CashLossResult&gt;</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-372540600007"></span><code>CashLossCommandHandler.HandleAsync(RecordKnownCashLossCommand,CommandEnvelope&lt;RecordKnownCashLossCommand&gt;,CancellationToken)</code><br>12–30 | IsNullOrWhiteSpace @16; Fail @16; ConfigureAwait @17; OpenShiftCurrencyAsync @17; Equals @18; ReadAsync @19; Amount @20; NewGuid @21; ExecuteAsync @22; AppendAsync @27; Success(CashLossResult) @29 | FROM cash_movements @19; INSERT INTO cash_movements @22 |
| <span id="m-0c13e8453b2f"></span><code>CashLossCommandHandler.HandleAsync(CorrectCashLossRecordCommand,CommandEnvelope&lt;CorrectCashLossRecordCommand&gt;,CancellationToken)</code><br>32–50 | ConfigureAwait @36; ReadAsync @36; Fail @37; IsNullOrWhiteSpace @38; Parse @44; Text @44; NewGuid @44; AppendAsync @45; Amount @45; Success(CashLossResult) @49 | FROM cash_loss_records @39; FROM user_roles @36; JOIN users @36 |
| <span id="m-0333da1aa4d4"></span><code>CashLossCommandHandler.AppendAsync(System.Data.Common.DbConnection,System.Data.Common.DbTransaction?,Guid,Guid,Guid?,CashLossKind,long,string,Guid?,Guid?,string,string,Guid,Guid,DateTime,CancellationToken)</code><br>52–63 | ConfigureAwait @56; ExecuteAsync @56; BusinessDateAsync @62 | INSERT INTO cash_loss_records @56 |
| <span id="m-7b4b5cdecd02"></span><code>CashLossCommandHandler.Fail(string,string)</code><br>64–64 | Failure(CashLossResult) @64 | No extracted literal effects. |

</details>

## CashLossCommands.cs {#src-7688cc0be8fa}

<code>Software/src/GetSeek.Application/Cash/CashLossCommands.cs</code> · 17 lines.

SHA-256: <code>dbad627413e62c2491add61b5bcbb8dfb702234c286e87abdefd30dd412c799b</code>.

Declarations: <code>RecordKnownCashLossCommand : ICommand&lt;CashLossResult&gt;</code> (line 7), <code>CorrectCashLossRecordCommand : ICommand&lt;CashLossResult&gt;</code> (line 13).

## ShiftCommandHandler.cs {#src-6edc723e3676}

<code>Software/src/GetSeek.Application/Cash/ShiftCommandHandler.cs</code> · 526 lines.

SHA-256: <code>58a6ae713deb3b81fb89c28cf946c5925e2ebcf7eb9b70d93aabe66795e521b0</code>.

Declarations: <code>ShiftCommandHandler : ICommandHandler&lt;OpenShiftCommand, Shift&gt;, ICommandHandler&lt;RecordCashMovementCommand, CashMovement&gt;, ICommandHandler&lt;CloseShiftCommand, Shift&gt;</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a12f36e419ba"></span><code>ShiftCommandHandler.HandleAsync(OpenShiftCommand,CommandEnvelope&lt;OpenShiftCommand&gt;,CancellationToken)</code><br>16–157 | Failure(Shift) @27; CreateCommand @31; ConfigureAwait @35; ExecuteScalarAsync @35; Equals @36; AddParam @53; ToString @53; ExecuteReaderAsync @54; ReadAsync @55; GetInt32 @59; ExecuteScalarAsync @77; NewGuid @84; ToString @88; ExecuteScalarAsync @93; ToString @94; IsNullOrWhiteSpace @95; FindSystemTimeZoneById @99; ToString @100; ConvertTimeFromUtc @100; ToString @116; ExecuteNonQueryAsync @124; ExecuteNonQueryAsync @143; Success(Shift) @156 | FROM shifts @75; FROM store_config @34; FROM store_config @92; FROM users @46; INSERT INTO cash_movements @131; INSERT INTO shifts @112; JOIN user_roles @46 · INVALID_STARTING_FLOAT @27; CURRENCY_MISMATCH @38; CASHIER_NOT_FOUND @57; CASHIER_INACTIVE @63; INVALID_CASHIER_ROLE @67; SHIFT_ALREADY_OPEN @80 |
| <span id="m-1612e5fb8c77"></span><code>ShiftCommandHandler.HandleAsync(RecordCashMovementCommand,CommandEnvelope&lt;RecordCashMovementCommand&gt;,CancellationToken)</code><br>159–222 | Failure(CashMovement) @164; CreateCommand @169; AddParam @173; ToString @173; ConfigureAwait @175; ExecuteScalarAsync @175; ToInt32 @176; NewGuid @182; ToString @192; ToString @199; ToString @200; ToString @202; ExecuteNonQueryAsync @204; Success(CashMovement) @221 | FROM shifts @172; INSERT INTO cash_movements @188 · USE_CASH_LOSS_COMMAND @164; SHIFT_NOT_OPEN @178 |
| <span id="m-a6c6fe2dfdbe"></span><code>ShiftCommandHandler.HandleAsync(CloseShiftCommand,CommandEnvelope&lt;CloseShiftCommand&gt;,CancellationToken)</code><br>224–515 | CreateCommand @238; AddParam @242; ToString @242; ConfigureAwait @244; ExecuteReaderAsync @244; ReadAsync @245; Parse @247; GetString @247; Parse @248; GetInt64 @249; Failure(Shift) @254; ExecuteReaderAsync @282; GetInt32 @285; ExecuteReaderAsync @310; ExecuteReaderAsync @334; Serialize @351; ExecuteReaderAsync @369; IsNullOrWhiteSpace @393; ReadAsync @405; Amount @406; BuildSalaryAndExpenseRecordLinesAsync @409; Serialize @411; ToString @437; NewGuid @437; ToString @439; ToString @440; ToString @441; ExecuteNonQueryAsync @466; AppendAsync @470; ExecuteNonQueryAsync @497; Success(Shift) @514 | FROM cash_movements @360; FROM invoice_collections @405; FROM sales_invoices @269; FROM sales_invoices @301; FROM sales_tenders @325; FROM shifts @241; INSERT INTO shift_z_reports @417; JOIN sales_invoices @325; UPDATE shifts @478 · SHIFT_ALREADY_CLOSED @254; SUPERVISOR_ELEVATION_REQUIRED @387; VARIANCE_REASON_REQUIRED @395 |
| <span id="m-5f5da613f124"></span><code>ShiftCommandHandler.AddParam(DbCommand,string,object)</code><br>517–523 | CreateParameter @519; Add @522 | No extracted literal effects. |

</details>

## ShiftCommands.cs {#src-d988e0aef61e}

<code>Software/src/GetSeek.Application/Cash/ShiftCommands.cs</code> · 36 lines.

SHA-256: <code>366c3624e2cf4494d9838e6d5ccf0236d4e86961b268d8390b34e6f7a7c56d23</code>.

Declarations: <code>OpenShiftCommand : ICommand&lt;Shift&gt;</code> (line 8), <code>RecordCashMovementCommand : ICommand&lt;CashMovement&gt;</code> (line 17), <code>CloseShiftCommand : ICommand&lt;Shift&gt;</code> (line 29).

## CatalogCommandHandler.cs {#src-c2d3294fc0a7}

<code>Software/src/GetSeek.Application/Catalog/CatalogCommandHandler.cs</code> · 1,476 lines.

SHA-256: <code>8f2862d1b0e5ab3aa686ba5e7b0b9e8954d0fefdeed824566c658513e85c9a83</code>.

Declarations: <code>CatalogCommandHandler : ICommandHandler&lt;CreateProductCommand, CatalogItemDto&gt;, ICommandHandler&lt;UpdateProductCommand, CatalogItemDto&gt;, ICommandHandler&lt;CreateServiceCommand, CatalogItemDto&gt;, ICommandHandler&lt;UpdateServiceCommand, CatalogItemDto&gt;, ICommandHandler&lt;DeactivateProductCommand, bool&gt;, ICommandHandler&lt;SetProductStatusCommand, bool&gt;</code> (line 11), <code>CategoryResolution</code> (line 739), <code>DefaultUnitResolution</code> (line 741).

<details markdown>
<summary>Methods, calls, table effects and failures (17)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-502eda0717e5"></span><code>CatalogCommandHandler.HandleAsync(CreateProductCommand,CommandEnvelope&lt;CreateProductCommand&gt;,CancellationToken)</code><br>19–256 | Trim @27; IsNullOrWhiteSpace @30; Failure(CatalogItemDto) @32; Equals @40; NormalizeProductPurpose @59; TryNormalizeCoordinates @65; NormalizeTrackingPolicy @78; ToUpperInvariant @84; ConfigureAwait @90; ReadUnitDefinitionAsync @90; ResolveDefaultUnitAsync @100; ResolveCategoryAsync @112; CreateCommand @119; AddParam @123; ToInt64 @124; ExecuteScalarAsync @124; NewGuid @131; ToString @133; ToString @156; Trim @163; ToInvariant @165; ToString @169; ExecuteNonQueryAsync @179; ExecuteNonQueryAsync @205; RecordAsync @208; AppendItemHistoryAsync @217; Success(CatalogItemDto) @255 | FROM items @122; INSERT INTO item_pricing @185; INSERT INTO items @137 · SKU_REQUIRED @32; NAME_REQUIRED @37; SERVICE_REGISTRATION_REQUIRED @42; INVALID_PRICE @47; INVALID_COST @52; INVALID_BUYING_PRICE @56; INVALID_PRODUCT_PURPOSE @62; INVALID_ITEM_LOCATION @68; INVALID_THRESHOLD @73; INVALID_TRACKING_POLICY @81; UOM_REQUIRED @87; UOM_NOT_FOUND @93; UOM_INACTIVE @97; DUPLICATE_SKU @127 |
| <span id="m-83ad1eb9103b"></span><code>CatalogCommandHandler.HandleAsync(UpdateProductCommand,CommandEnvelope&lt;UpdateProductCommand&gt;,CancellationToken)</code><br>258–675 | Trim @266; IsNullOrWhiteSpace @269; Failure(CatalogItemDto) @271; CreateCommand @318; AddParam @322; ToString @322; ConfigureAwait @323; ExecuteReaderAsync @323; ReadAsync @324; GetInt32 @328; GetString @329; Parse @331; IsDBNull @333; GetInt64 @337; Serialize @344; Equals @362; ExecuteReaderAsync @384; ReadAsync @385; GetString @387; IsDBNull @388; GetInt64 @389; NormalizeProductPurpose @393; TryNormalizeCoordinates @407; NormalizeTrackingPolicy @414; ToInt64 @426; ExecuteScalarAsync @426; IsWeakerTrackingPolicy @436; IsTrackingChangeBlockedAsync @438; ResolveCategoryAsync @446; ToUpperInvariant @452; ReadUnitDefinitionAsync @457; ResolveDefaultUnitAsync @467; ExecuteScalarAsync @489; ExecuteScalarAsync @506; ToString @514; ToInvariant @549; ToString @553; ExecuteNonQueryAsync @565; ExecuteNonQueryAsync @595; RecordAsync @600; AppendItemHistoryAsync @622; ToString @660; CreateCategoryReassignmentProposalAsync @662; EnqueueAffectedKitAlertsAsync @670; Success(CatalogItemDto) @674 | FROM item_kits @424; FROM item_pricing @382; FROM items @321; FROM items @503; FROM sales_lines @483; FROM stock_movements @483; INSERT INTO item_pricing @573; UPDATE items @519 · SKU_REQUIRED @271; NAME_REQUIRED @276; INVALID_PRICE @281; INVALID_COST @286; INVALID_BUYING_PRICE @290; INVALID_THRESHOLD @295; ITEM_NOT_FOUND @326; SKU_IMMUTABLE @364; ITEM_KIND_IMMUTABLE @369; ITEM_KIND_IMMUTABLE @374; INVALID_PRODUCT_PURPOSE @396; INVALID_PRODUCT_PURPOSE @400; INVALID_ITEM_LOCATION @410; INVALID_TRACKING_POLICY @417; KIT_ITEM_CANNOT_BE_TRACKED @429; TRACKING_CHANGE_BLOCKED @440; UOM_REQUIRED @455; UOM_NOT_FOUND @460; UOM_INACTIVE @464; BASE_UNIT_IMMUTABLE_WITH_MOVEMENTS @492; DUPLICATE_SKU @509 |
| <span id="m-37816510b61b"></span><code>CatalogCommandHandler.HandleAsync(DeactivateProductCommand,CommandEnvelope&lt;DeactivateProductCommand&gt;,CancellationToken)</code><br>677–682 | HandleAsync @680 | No extracted literal effects. |
| <span id="m-3a420f15c21e"></span><code>CatalogCommandHandler.HandleAsync(SetProductStatusCommand,CommandEnvelope&lt;SetProductStatusCommand&gt;,CancellationToken)</code><br>684–737 | CreateCommand @696; AddParam @700; ToString @700; ConfigureAwait @701; ExecuteReaderAsync @701; ReadAsync @702; Failure(bool) @704; GetString @706; GetInt32 @708; Serialize @709; GetInt64 @712; IsDBNull @714; ExecuteNonQueryAsync @726; AppendItemHistoryAsync @731; Success(bool) @736 | FROM items @699; UPDATE items @723 · ITEM_NOT_FOUND @704 |
| <span id="m-660e7a28d7f4"></span><code>CatalogCommandHandler.ResolveDefaultUnitAsync(DbConnection,DbTransaction?,string?,string,UnitDefinition,CancellationToken)</code><br>743–779 | IsNullOrWhiteSpace @751; ToUpperInvariant @753; Trim @753; Equals @755; ConfigureAwait @760; ReadUnitDefinitionAsync @760 | No extracted literal effects. |
| <span id="m-d8b92ef052b7"></span><code>CatalogCommandHandler.ReadUnitDefinitionAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>781–805 | TryGetUom @785; CreateCommand @788; AddParam @791; ConfigureAwait @793; ExecuteReaderAsync @793; ReadAsync @794; GetString @800; IsDBNull @801; GetInt32 @804 | FROM uoms @790 |
| <span id="m-4b7af22d8bfb"></span><code>CatalogCommandHandler.NormalizeTrackingPolicy(bool,string?,string?)</code><br>811–838 | Trim @820; Equals @821 | No extracted literal effects. |
| <span id="m-cf673d985ad1"></span><code>CatalogCommandHandler.TrackingPolicyRank(string?)</code><br>840–853 | Equals @842 | No extracted literal effects. |
| <span id="m-358646417251"></span><code>CatalogCommandHandler.IsWeakerTrackingPolicy(string?,string)</code><br>855–856 | TrackingPolicyRank @856 | No extracted literal effects. |
| <span id="m-ffc80d767ec4"></span><code>CatalogCommandHandler.NormalizeProductPurpose(string?)</code><br>858–864 | Trim @860; Equals @861 | No extracted literal effects. |
| <span id="m-1ce10e9a79f4"></span><code>CatalogCommandHandler.TryNormalizeCoordinates(string?,string?,string?,string?,string?,string?)</code><br>866–900 | Trim @880; Any @887; IsAsciiLetterOrDigit @887; ToUpperInvariant @893; IsValid @897 | No extracted literal effects. |
| <span id="m-5845db3c3228"></span><code>CatalogCommandHandler.AppendItemHistoryAsync(DbConnection,DbTransaction?,Guid,string,string,string,string?,object,CommandEnvelope&lt;TCommand&gt;,CancellationToken)</code><br>902–937 | CreateCommand @915; AddParam @926; ToString @926; NewGuid @926; ToString @927; Serialize @932; ToString @933; ToString @934; ToString @935; ConfigureAwait @936; ExecuteNonQueryAsync @936 | INSERT INTO item_change_history @917 |
| <span id="m-33c95373caa4"></span><code>CatalogCommandHandler.IsTrackingChangeBlockedAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>939–955 | CreateCommand @941; AddParam @952; ToString @952; ToInt64 @953; ConfigureAwait @953; ExecuteScalarAsync @953 | FROM bom_items @943; FROM draft_cart_lines @943; FROM draft_carts @943; FROM item_kit_components @943; FROM lots @943; FROM serials @943; FROM stock_movements @943 |
| <span id="m-43d87b7002b1"></span><code>CatalogCommandHandler.ResolveCategoryAsync(DbConnection,DbTransaction?,Guid?,string?,CancellationToken)</code><br>961–1026 | IsNullOrWhiteSpace @963; FindCategory @970; Equals @981; CreateCommand @989; AddParam @994; ToString @994; ToUpperInvariant @999; Trim @999; ConfigureAwait @1002; ExecuteReaderAsync @1002; ReadAsync @1003; Parse @1008; GetString @1008; GetInt32 @1010 | FROM product_categories @993; FROM product_categories @998 |
| <span id="m-13169f17df41"></span><code>CatalogCommandHandler.AddParam(DbCommand,string,object)</code><br>1028–1034 | CreateParameter @1030; Add @1033 | No extracted literal effects. |
| <span id="m-ec56dbb87a53"></span><code>CatalogCommandHandler.HandleAsync(CreateServiceCommand,CommandEnvelope&lt;CreateServiceCommand&gt;,CancellationToken)</code><br>1036–1240 | Trim @1044; IsNullOrWhiteSpace @1047; Failure(CatalogItemDto) @1049; ToUpperInvariant @1067; ConfigureAwait @1073; ReadUnitDefinitionAsync @1073; ResolveDefaultUnitAsync @1083; ResolveCategoryAsync @1089; CreateCommand @1096; AddParam @1100; ToInt64 @1101; ExecuteScalarAsync @1101; NewGuid @1108; ToString @1110; ToString @1136; Trim @1143; ToInvariant @1145; ToString @1146; ExecuteNonQueryAsync @1150; ExecuteNonQueryAsync @1163; ExecuteNonQueryAsync @1190; RecordAsync @1194; AppendItemHistoryAsync @1203; Success(CatalogItemDto) @1239 | FROM items @1099; INSERT INTO item_pricing @1170; INSERT INTO items @1116; INSERT INTO service_items @1157 · SKU_REQUIRED @1049; NAME_REQUIRED @1054; INVALID_PRICE @1059; INVALID_COST @1064; UOM_REQUIRED @1070; UOM_NOT_FOUND @1076; UOM_INACTIVE @1080; DUPLICATE_SKU @1104 |
| <span id="m-ea4c9a18bbae"></span><code>CatalogCommandHandler.HandleAsync(UpdateServiceCommand,CommandEnvelope&lt;UpdateServiceCommand&gt;,CancellationToken)</code><br>1242–1474 | Trim @1250; IsNullOrWhiteSpace @1253; Failure(CatalogItemDto) @1255; CreateCommand @1283; AddParam @1287; ToString @1287; ConfigureAwait @1288; ExecuteReaderAsync @1288; ReadAsync @1289; GetInt32 @1293; GetString @1294; Parse @1296; GetInt64 @1298; IsDBNull @1300; Equals @1304; ResolveCategoryAsync @1319; ToUpperInvariant @1325; ReadUnitDefinitionAsync @1330; ResolveDefaultUnitAsync @1340; ToInt64 @1353; ExecuteScalarAsync @1353; ToString @1361; ToInvariant @1387; ToString @1388; ExecuteNonQueryAsync @1392; ExecuteNonQueryAsync @1420; RecordAsync @1423; AppendItemHistoryAsync @1437; Success(CatalogItemDto) @1473 | FROM items @1286; FROM items @1350; INSERT INTO item_pricing @1400; UPDATE items @1368 · SKU_REQUIRED @1255; NAME_REQUIRED @1260; INVALID_PRICE @1265; INVALID_COST @1270; ITEM_NOT_FOUND @1291; ITEM_KIND_IMMUTABLE @1306; ITEM_KIND_IMMUTABLE @1311; SKU_IMMUTABLE @1316; UOM_REQUIRED @1328; UOM_NOT_FOUND @1333; UOM_INACTIVE @1337; DUPLICATE_SKU @1356 |

</details>

## CatalogCommands.cs {#src-8482e00dd58a}

<code>Software/src/GetSeek.Application/Catalog/CatalogCommands.cs</code> · 141 lines.

SHA-256: <code>d508f078977636a1d7a500cffc53c65a65698409ccb1bd101abfaac13aeecfba</code>.

Declarations: <code>CatalogItemDto</code> (line 6), <code>CreateProductCommand : ICommand&lt;CatalogItemDto&gt;</code> (line 34), <code>UpdateProductCommand : ICommand&lt;CatalogItemDto&gt;</code> (line 61), <code>DeactivateProductCommand : ICommand&lt;bool&gt;</code> (line 92), <code>SetProductStatusCommand : ICommand&lt;bool&gt;</code> (line 100), <code>CreateServiceCommand : ICommand&lt;CatalogItemDto&gt;</code> (line 106), <code>UpdateServiceCommand : ICommand&lt;CatalogItemDto&gt;</code> (line 123).

## CatalogRegistryCommandHandler.cs {#src-1b8d6c18449a}

<code>Software/src/GetSeek.Application/Catalog/CatalogRegistryCommandHandler.cs</code> · 867 lines.

SHA-256: <code>e1e8202a7be8d95f2ec7a11035fdceccdbc963fee91a91b6057e7a2bb8c00314</code>.

Declarations: <code>CatalogRegistryCommandHandler : ICommandHandler&lt;CreateCategoryCommand, ProductCategoryDto&gt;, ICommandHandler&lt;UpdateCategoryCommand, ProductCategoryDto&gt;, ICommandHandler&lt;DeactivateCategoryCommand, bool&gt;, ICommandHandler&lt;ReactivateCategoryCommand, bool&gt;, ICommandHandler&lt;DeleteCategoryCommand, bool&gt;, ICommandHandler&lt;CreateUomCommand, UomDefinitionDto&gt;, ICommandHandler&lt;UpdateUomCommand, UomDefinitionDto&gt;, ICommandHandler&lt;DeactivateUomCommand, bool&gt;, ICommandHandler&lt;ReactivateUomCommand, bool&gt;, ICommandHandler&lt;DeleteUomCommand, bool&gt;</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (22)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d66f4c4edaeb"></span><code>CatalogRegistryCommandHandler.HandleAsync(CreateCategoryCommand,CommandEnvelope&lt;CreateCategoryCommand&gt;,CancellationToken)</code><br>32–109 | ConfigureAwait @40; IsActiveAdminAsync @40; Failure(ProductCategoryDto) @42; ToUpperInvariant @45; Trim @45; IsNullOrWhiteSpace @48; NormalizeProfileScope @63; CategoryCodeExistsAsync @69; CategoryNameExistsAsync @74; NormalizeTargetType @79; NewGuid @80; Trim @82; CreateCommand @84; AddParam @96; ToString @96; ToString @102; ExecuteNonQueryAsync @104; Success(ProductCategoryDto) @107 | INSERT INTO product_categories @87 · ADMIN_REQUIRED @42; CATEGORY_REQUIRED @50; CATEGORY_REQUIRED @55; CATEGORY_REQUIRED @60; CATEGORY_REQUIRED @66; DUPLICATE_CATEGORY @71; DUPLICATE_CATEGORY @76 |
| <span id="m-cb797c0581eb"></span><code>CatalogRegistryCommandHandler.HandleAsync(UpdateCategoryCommand,CommandEnvelope&lt;UpdateCategoryCommand&gt;,CancellationToken)</code><br>111–175 | ConfigureAwait @119; IsActiveAdminAsync @119; Failure(ProductCategoryDto) @121; Trim @124; IsNullOrWhiteSpace @125; NormalizeProfileScope @130; ReadCategoryAsync @136; CategoryNameExistsAsync @142; Trim @148; NormalizeTargetType @149; CreateCommand @151; AddParam @163; ToString @168; ToString @169; ExecuteNonQueryAsync @170; Success(ProductCategoryDto) @173 | UPDATE product_categories @154 · ADMIN_REQUIRED @121; CATEGORY_REQUIRED @127; CATEGORY_REQUIRED @133; CATEGORY_NOT_FOUND @139; DUPLICATE_CATEGORY @144 |
| <span id="m-a7fb74fc19e0"></span><code>CatalogRegistryCommandHandler.HandleAsync(DeactivateCategoryCommand,CommandEnvelope&lt;DeactivateCategoryCommand&gt;,CancellationToken)</code><br>177–225 | ConfigureAwait @185; IsActiveAdminAsync @185; Failure(bool) @187; ReadCategoryAsync @190; Equals @196; CreateCommand @201; AddParam @205; ToString @205; ToInt64 @206; ExecuteScalarAsync @206; ToString @219; ExecuteNonQueryAsync @221; Success(bool) @224 | FROM items @204; UPDATE product_categories @218 · ADMIN_REQUIRED @187; CATEGORY_NOT_FOUND @193; CATEGORY_IN_USE @198; CATEGORY_IN_USE @209 |
| <span id="m-e0dafe188016"></span><code>CatalogRegistryCommandHandler.HandleAsync(ReactivateCategoryCommand,CommandEnvelope&lt;ReactivateCategoryCommand&gt;,CancellationToken)</code><br>227–256 | ConfigureAwait @235; IsActiveAdminAsync @235; Failure(bool) @237; ReadCategoryAsync @240; CreateCommand @246; AddParam @250; ToString @250; ToString @251; ExecuteNonQueryAsync @252; Success(bool) @255 | UPDATE product_categories @249 · ADMIN_REQUIRED @237; CATEGORY_NOT_FOUND @243 |
| <span id="m-296d2c281ff8"></span><code>CatalogRegistryCommandHandler.HandleAsync(DeleteCategoryCommand,CommandEnvelope&lt;DeleteCategoryCommand&gt;,CancellationToken)</code><br>258–291 | ConfigureAwait @265; IsActiveAdminAsync @265; Failure(bool) @266; ReadCategoryAsync @267; CreateCommand @273; AddParam @280; ToString @280; ToInt64 @281; ExecuteScalarAsync @281; ExecuteNonQueryAsync @288; Success(bool) @290 | DELETE FROM product_categories @286; FROM batch_previews @275; FROM items @275; FROM product_category_pricing_rules @275 · ADMIN_REQUIRED @266; CATEGORY_NOT_FOUND @269; CATEGORY_BUILTIN @271; CATEGORY_IN_USE @282; CATEGORY_DELETE_BLOCKED @289 |
| <span id="m-ae8d7a0b2824"></span><code>CatalogRegistryCommandHandler.HandleAsync(CreateUomCommand,CommandEnvelope&lt;CreateUomCommand&gt;,CancellationToken)</code><br>297–409 | ConfigureAwait @305; IsActiveAdminAsync @305; Failure(UomDefinitionDto) @307; ToUpperInvariant @310; Trim @310; IsNullOrWhiteSpace @313; NormalizeUnitKind @323; NormalizeDimension @335; ToInvariant @346; UomCodeExistsAsync @369; Trim @376; CreateCommand @381; AddParam @395; Trim @403; ExecuteNonQueryAsync @404; Success(UomDefinitionDto) @407 | INSERT INTO uoms @384 · ADMIN_REQUIRED @307; UOM_NOT_FOUND @315; UOM_NOT_FOUND @320; UOM_DIMENSION_MISMATCH @326; UOM_DIMENSION_MISMATCH @338; UOM_FACTOR_INVALID @343; UOM_FACTOR_INVALID @358; UOM_FACTOR_INVALID @366; DUPLICATE_UOM @371 |
| <span id="m-46f59572d6fa"></span><code>CatalogRegistryCommandHandler.HandleAsync(UpdateUomCommand,CommandEnvelope&lt;UpdateUomCommand&gt;,CancellationToken)</code><br>411–517 | ConfigureAwait @419; IsActiveAdminAsync @419; Failure(UomDefinitionDto) @421; ToUpperInvariant @424; Trim @424; IsNullOrWhiteSpace @426; ReadUomAsync @431; TryParse @463; UomIsReferencedAsync @470; ToInvariant @477; Trim @482; Trim @483; CreateCommand @485; AddParam @496; ExecuteNonQueryAsync @502; ExecuteNonQueryAsync @511; Success(UomDefinitionDto) @515 | UPDATE uoms @488; UPDATE uoms @508 · ADMIN_REQUIRED @421; UOM_NOT_FOUND @428; UOM_NOT_FOUND @434; UOM_FACTOR_INVALID @440; UOM_FACTOR_INVALID @453; UOM_FACTOR_INVALID @458; UOM_DEFINITION_IN_USE @472 |
| <span id="m-2c2bbbc7eefc"></span><code>CatalogRegistryCommandHandler.HandleAsync(DeactivateUomCommand,CommandEnvelope&lt;DeactivateUomCommand&gt;,CancellationToken)</code><br>519–564 | ConfigureAwait @527; IsActiveAdminAsync @527; Failure(bool) @529; ToUpperInvariant @532; Trim @532; ReadUomAsync @533; CreateCommand @539; AddParam @545; ToInt64 @546; ExecuteScalarAsync @546; ExecuteNonQueryAsync @560; Success(bool) @563 | FROM items @542; UPDATE uoms @558 · ADMIN_REQUIRED @529; UOM_NOT_FOUND @536; UOM_DEFINITION_IN_USE @549 |
| <span id="m-173e9cf4959c"></span><code>CatalogRegistryCommandHandler.HandleAsync(ReactivateUomCommand,CommandEnvelope&lt;ReactivateUomCommand&gt;,CancellationToken)</code><br>566–600 | ConfigureAwait @574; IsActiveAdminAsync @574; Failure(bool) @576; ToUpperInvariant @579; Trim @579; ReadUomAsync @580; CreateCommand @591; AddParam @595; ExecuteNonQueryAsync @596; Success(bool) @599 | UPDATE uoms @594 · ADMIN_REQUIRED @576; UOM_NOT_FOUND @583; UOM_DIMENSION_MISMATCH @588 |
| <span id="m-5c4e71f7e297"></span><code>CatalogRegistryCommandHandler.HandleAsync(DeleteUomCommand,CommandEnvelope&lt;DeleteUomCommand&gt;,CancellationToken)</code><br>602–646 | ConfigureAwait @609; IsActiveAdminAsync @609; Failure(bool) @610; ToUpperInvariant @611; Trim @611; ReadUomAsync @612; CreateCommand @618; AddParam @635; ToInt64 @636; ExecuteScalarAsync @636; ExecuteNonQueryAsync @643; Success(bool) @645 | DELETE FROM uoms @641; FROM barcodes @620; FROM bom_items @620; FROM draft_cart_lines @620; FROM item_kit_components @620; FROM item_price_history @620; FROM items @620; FROM production_run_inputs @620; FROM production_run_outputs @620; FROM sales_lines @620; FROM stock_movements @620; FROM store_uom_preferences @620; FROM uom_dimensions @620 · ADMIN_REQUIRED @610; UOM_NOT_FOUND @614; UOM_BUILTIN @616; UOM_DEFINITION_IN_USE @637; UOM_DELETE_BLOCKED @644 |
| <span id="m-eec94a9863fc"></span><code>CatalogRegistryCommandHandler.NormalizeProfileScope(string?)</code><br>652–666 | IsNullOrWhiteSpace @654; ToLowerInvariant @659; Trim @659 | No extracted literal effects. |
| <span id="m-c8b399312411"></span><code>CatalogRegistryCommandHandler.NormalizeUnitKind(string?)</code><br>668–682 | IsNullOrWhiteSpace @670; ToLowerInvariant @675; Trim @675 | No extracted literal effects. |
| <span id="m-47f226c14f6a"></span><code>CatalogRegistryCommandHandler.NormalizeDimension(string?)</code><br>684–700 | IsNullOrWhiteSpace @686; Equals @693; Trim @693 | No extracted literal effects. |
| <span id="m-a0a61a0f660e"></span><code>CatalogRegistryCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>702–719 | CreateCommand @709; AddParam @716; ToString @716; ToInt64 @717; ConfigureAwait @717; ExecuteScalarAsync @717 | FROM users @711; JOIN user_roles @711 |
| <span id="m-15dd37c6f6bd"></span><code>CatalogRegistryCommandHandler.CategoryCodeExistsAsync(DbConnection,DbTransaction?,string,Guid?,CancellationToken)</code><br>721–736 | CreateCommand @723; AddParam @728; ToString @731; ToInt64 @734; ConfigureAwait @734; ExecuteScalarAsync @734 | FROM product_categories @726; FROM product_categories @727 |
| <span id="m-055c7a8a4cf4"></span><code>CatalogRegistryCommandHandler.CategoryNameExistsAsync(DbConnection,DbTransaction?,string,Guid?,CancellationToken)</code><br>738–753 | CreateCommand @740; AddParam @745; ToUpperInvariant @745; ToString @748; ToInt64 @751; ConfigureAwait @751; ExecuteScalarAsync @751 | FROM product_categories @743; FROM product_categories @744 |
| <span id="m-c6e674426295"></span><code>CatalogRegistryCommandHandler.NormalizeTargetType(string?)</code><br>755–764 | IsNullOrWhiteSpace @757; Trim @758; Equals @759 | No extracted literal effects. |
| <span id="m-fa45c96d6b54"></span><code>CatalogRegistryCommandHandler.ReadCategoryAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>766–796 | CreateCommand @768; AddParam @776; ToString @776; ConfigureAwait @778; ExecuteReaderAsync @778; ReadAsync @779; Parse @785; GetString @785; GetInt32 @789; IsDBNull @790; Parse @793 | FROM product_categories @770 |
| <span id="m-50d7b2328d4e"></span><code>CatalogRegistryCommandHandler.UomCodeExistsAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>798–806 | CreateCommand @800; AddParam @803; ToInt64 @804; ConfigureAwait @804; ExecuteScalarAsync @804 | FROM uoms @802 |
| <span id="m-541750121d7a"></span><code>CatalogRegistryCommandHandler.ReadUomAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>808–836 | CreateCommand @810; AddParam @817; ConfigureAwait @819; ExecuteReaderAsync @819; ReadAsync @820; GetString @826; IsDBNull @828; GetInt32 @832 | FROM uoms @812 |
| <span id="m-ca1e2c9bf689"></span><code>CatalogRegistryCommandHandler.UomIsReferencedAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>842–858 | CreateCommand @844; AddParam @855; ToInt64 @856; ConfigureAwait @856; ExecuteScalarAsync @856 | FROM barcodes @846; FROM bom_items @846; FROM draft_cart_lines @846; FROM item_kit_components @846; FROM items @846; FROM sales_lines @846; FROM stock_movements @846 |
| <span id="m-f3d25ec02ab0"></span><code>CatalogRegistryCommandHandler.AddParam(DbCommand,string,object)</code><br>860–866 | CreateParameter @862; Add @865 | No extracted literal effects. |

</details>

## CatalogRegistryCommands.cs {#src-e1ac9f19094b}

<code>Software/src/GetSeek.Application/Catalog/CatalogRegistryCommands.cs</code> · 127 lines.

SHA-256: <code>42690348d0448201c5bc1f7e5aed0e8443d56cf31f12ad208d7e02f0c1d12528</code>.

Declarations: <code>ProductCategoryDefaults</code> (line 7), <code>ProductCategoryDto</code> (line 13), <code>UomDefinitionDto</code> (line 27), <code>CreateCategoryCommand : ICommand&lt;ProductCategoryDto&gt;</code> (line 45), <code>UpdateCategoryCommand : ICommand&lt;ProductCategoryDto&gt;</code> (line 57), <code>DeactivateCategoryCommand : ICommand&lt;bool&gt;</code> (line 69), <code>ReactivateCategoryCommand : ICommand&lt;bool&gt;</code> (line 74), <code>DeleteCategoryCommand : ICommand&lt;bool&gt;</code> (line 79), <code>CreateUomCommand : ICommand&lt;UomDefinitionDto&gt;</code> (line 88), <code>UpdateUomCommand : ICommand&lt;UomDefinitionDto&gt;</code> (line 102), <code>DeactivateUomCommand : ICommand&lt;bool&gt;</code> (line 114), <code>ReactivateUomCommand : ICommand&lt;bool&gt;</code> (line 119), <code>DeleteUomCommand : ICommand&lt;bool&gt;</code> (line 124).

## SaveProductConfigurationCommand.cs {#src-5802398b5ad9}

<code>Software/src/GetSeek.Application/Catalog/SaveProductConfigurationCommand.cs</code> · 31 lines.

SHA-256: <code>854c7a1126c0910ccfbb12f29757cfdf35f33714d2c35ebf968c6430f485ab24</code>.

Declarations: <code>SaveProductConfigurationCommand : ICommand&lt;CatalogItemDto&gt;</code> (line 12).

## SaveProductConfigurationCommandHandler.cs {#src-c24b9e05b3b2}

<code>Software/src/GetSeek.Application/Catalog/SaveProductConfigurationCommandHandler.cs</code> · 280 lines.

SHA-256: <code>0f7112b86c1fecef5b3836846e70eae630d3fe1b1178c49caaf5996c22cb6512</code>.

Declarations: <code>SaveProductConfigurationCommandHandler : ICommandHandler&lt;SaveProductConfigurationCommand, CatalogItemDto&gt;</code> (line 13).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-98f2baf362dd"></span><code>SaveProductConfigurationCommandHandler.HandleAsync(SaveProductConfigurationCommand,CommandEnvelope&lt;SaveProductConfigurationCommand&gt;,CancellationToken)</code><br>19–178 | Failure(CatalogItemDto) @29; IsNullOrWhiteSpace @43; ConfigureAwait @46; HasPermissionAsync @46; CreateChildEnvelope @58; HandleAsync @59; CopyFailure @61; CreateCommand @85; AddParam @89; ToString @89; ExecuteReaderAsync @90; ReadAsync @91; GetString @93; IsDBNull @94; Equals @95; Trim @95; HandleAsync @109; ToString @128; ToInt64 @129; ExecuteScalarAsync @129; HandleAsync @136; ApplyActiveCategoryRuleAsync @150; HandleAsync @157; SavePrimaryBarcodeAsync @164; Trim @172; Success(CatalogItemDto) @177 | FROM item_kits @127; FROM items @88 · PRODUCT_PAYLOAD_INVALID @29; SERVICE_KIT_NOT_ALLOWED @34; SERVICE_STOCK_NOT_ALLOWED @36; CANNOT_ADJUST_KIT_STOCK @42; REASON_REQUIRED @44; AUTH_UNAUTHORIZED @48; COMPONENTS_REQUIRED @52; SKU_IMMUTABLE @96; ITEM_KIND_IMMUTABLE @98; ITEM_KIND_IMMUTABLE @100; KIT_NOT_FOUND @130; CATEGORY_PRICING_RULE_NOT_FOUND @142; CATEGORY_PRICING_RULE_STALE @155; CATEGORY_PRICING_RULE_NOT_FOUND @156 |
| <span id="m-b560f7993ac1"></span><code>SaveProductConfigurationCommandHandler.ApplyActiveCategoryRuleAsync(CatalogItemDto,SaveItemPricingCommand,Guid?,int?,CancellationToken)</code><br>180–216 | CreateCommand @189; AddParam @196; ToString @196; ConfigureAwait @197; ExecuteReaderAsync @197; ReadAsync @198; TryParse @200; GetString @200; GetInt32 @200; Parse @207; GetInt64 @208; Parse @213 | FROM product_category_pricing_rules @191 |
| <span id="m-c3e2782a25a9"></span><code>SaveProductConfigurationCommandHandler.SavePrimaryBarcodeAsync(Guid,string,string?,CancellationToken)</code><br>218–256 | Trim @224; CreateCommand @230; AddParam @233; ToString @234; ToInt64 @235; ConfigureAwait @235; ExecuteScalarAsync @235; Failure(bool) @236; ExecuteNonQueryAsync @254; Success(bool) @255 | DELETE FROM barcodes @242; DELETE FROM barcodes @243; FROM barcodes @232; INSERT INTO barcodes @243 · DUPLICATE_BARCODE @236 |
| <span id="m-b265a417a9b3"></span><code>SaveProductConfigurationCommandHandler.CreateChildEnvelope(CommandEnvelope&lt;SaveProductConfigurationCommand&gt;,TChild)</code><br>258–268 | — | No extracted literal effects. |
| <span id="m-b327a3a23017"></span><code>SaveProductConfigurationCommandHandler.CopyFailure(CommandResult&lt;TIn&gt;)</code><br>270–271 | Failure(CatalogItemDto) @271 | No extracted literal effects. |
| <span id="m-fe15ef749c1c"></span><code>SaveProductConfigurationCommandHandler.AddParam(DbCommand,string,object)</code><br>273–279 | CreateParameter @275; Add @278 | No extracted literal effects. |

</details>

## StoreUomPreferenceCommandHandler.cs {#src-931326887202}

<code>Software/src/GetSeek.Application/Catalog/StoreUomPreferenceCommandHandler.cs</code> · 84 lines.

SHA-256: <code>5da34e84c5e4a8e3e4c3ef0495a73cdfe7e3aa7204355a96e6f7a04b63fafe41</code>.

Declarations: <code>StoreUomPreferenceCommandHandler : ICommandHandler&lt;UpdateStoreUomPreferenceCommand, bool&gt;</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-43ba3062b01a"></span><code>StoreUomPreferenceCommandHandler.HandleAsync(UpdateStoreUomPreferenceCommand,CommandEnvelope&lt;UpdateStoreUomPreferenceCommand&gt;,CancellationToken)</code><br>10–75 | CreateCommand @19; AddParam @23; ToInt64 @24; ExecuteScalarAsync @24; Failure(bool) @26; ExecuteScalarAsync @37; ExecuteScalarAsync @50; ExecuteNonQueryAsync @71; Success(bool) @74 | FROM uom_dimensions @22; FROM uoms @34; FROM uoms @47; INSERT INTO store_uom_preferences @60 · DIMENSION_NOT_FOUND @26; INVALID_ENTRY_UOM @39; INVALID_BASE_UOM @52 |
| <span id="m-3da35b87c9b9"></span><code>StoreUomPreferenceCommandHandler.AddParam(DbCommand,string,object)</code><br>77–83 | CreateParameter @79; Add @82 | No extracted literal effects. |

</details>

## StoreUomPreferenceCommands.cs {#src-df6632bf7490}

<code>Software/src/GetSeek.Application/Catalog/StoreUomPreferenceCommands.cs</code> · 13 lines.

SHA-256: <code>58c01a8b66cc69c00f0b32f5045304a98742017bd368723df57e7e4a1b0dd569</code>.

Declarations: <code>UpdateStoreUomPreferenceCommand : ICommand&lt;bool&gt;</code> (line 6).

## SupplierCommandHandler.cs {#src-2bdfe6e3c46f}

<code>Software/src/GetSeek.Application/Catalog/SupplierCommandHandler.cs</code> · 237 lines.

SHA-256: <code>3fa3d552a6e86b69d57adc8d10854806699d61fa4814245a004a22b9f5b74aed</code>.

Declarations: <code>SupplierCommandHandler : ICommandHandler&lt;CreateSupplierCommand, SupplierDto&gt;, ICommandHandler&lt;UpdateSupplierCommand, SupplierDto&gt;, ICommandHandler&lt;DeactivateSupplierCommand, bool&gt;</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-441821b5ef52"></span><code>SupplierCommandHandler.HandleAsync(CreateSupplierCommand,CommandEnvelope&lt;CreateSupplierCommand&gt;,CancellationToken)</code><br>13–93 | ToUpperInvariant @21; Trim @21; IsNullOrWhiteSpace @24; Failure(SupplierDto) @26; CreateCommand @35; AddParam @39; ToInt64 @40; ConfigureAwait @40; ExecuteScalarAsync @40; NewGuid @47; ToString @49; ToString @64; ExecuteNonQueryAsync @74; Success(SupplierDto) @92 | FROM third_parties @38; INSERT INTO third_parties @54 · CODE_REQUIRED @26; NAME_REQUIRED @31; DUPLICATE_CODE @43 |
| <span id="m-fe472277612b"></span><code>SupplierCommandHandler.HandleAsync(UpdateSupplierCommand,CommandEnvelope&lt;UpdateSupplierCommand&gt;,CancellationToken)</code><br>95–193 | ToUpperInvariant @103; Trim @103; IsNullOrWhiteSpace @106; Failure(SupplierDto) @108; CreateCommand @117; AddParam @121; ToString @121; ConfigureAwait @122; ExecuteScalarAsync @122; Parse @127; ToString @127; ToInt64 @137; ToString @145; ExecuteNonQueryAsync @174; Success(SupplierDto) @192 | FROM third_parties @120; FROM third_parties @134; UPDATE third_parties @150 · CODE_REQUIRED @108; NAME_REQUIRED @113; SUPPLIER_NOT_FOUND @125; DUPLICATE_CODE @140 |
| <span id="m-d42558026794"></span><code>SupplierCommandHandler.HandleAsync(DeactivateSupplierCommand,CommandEnvelope&lt;DeactivateSupplierCommand&gt;,CancellationToken)</code><br>195–228 | CreateCommand @203; AddParam @207; ToString @207; ToInt64 @208; ConfigureAwait @208; ExecuteScalarAsync @208; Failure(bool) @211; ToString @216; ExecuteNonQueryAsync @224; Success(bool) @227 | FROM third_parties @206; UPDATE third_parties @221 · SUPPLIER_NOT_FOUND @211 |
| <span id="m-8e0f95656592"></span><code>SupplierCommandHandler.AddParam(DbCommand,string,object)</code><br>230–236 | CreateParameter @232; Add @235 | No extracted literal effects. |

</details>

## SupplierCommands.cs {#src-0b51c10a2834}

<code>Software/src/GetSeek.Application/Catalog/SupplierCommands.cs</code> · 57 lines.

SHA-256: <code>74c17ec15a17e3b0a423c36c414186a32cb275ef130dc53b45095f83a176c1e9</code>.

Declarations: <code>SupplierDto</code> (line 6), <code>CreateSupplierCommand : ICommand&lt;SupplierDto&gt;</code> (line 21), <code>UpdateSupplierCommand : ICommand&lt;SupplierDto&gt;</code> (line 35), <code>DeactivateSupplierCommand : ICommand&lt;bool&gt;</code> (line 51).

## CustomerCommandHandler.cs {#src-21df28594271}

<code>Software/src/GetSeek.Application/Customers/CustomerCommandHandler.cs</code> · 304 lines.

SHA-256: <code>ce9a0beccc5a6d8db82ef38af396c1b6564a693bc6adc09ace23df83cf471e20</code>.

Declarations: <code>CustomerCommandHandler : ICommandHandler&lt;CreateCustomerCommand, CustomerDto&gt;, ICommandHandler&lt;UpdateCustomerCommand, CustomerDto&gt;, ICommandHandler&lt;DeactivateCustomerCommand, bool&gt;, ICommandHandler&lt;ReactivateCustomerCommand, bool&gt;</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-25775f41bdcc"></span><code>CustomerCommandHandler.HandleAsync(CreateCustomerCommand,CommandEnvelope&lt;CreateCustomerCommand&gt;,CancellationToken)</code><br>15–96 | ToUpperInvariant @23; Trim @23; TryNormalizePhone @25; Failure(CustomerDto) @27; IsNullOrWhiteSpace @30; CreateCommand @41; AddParam @45; ToInt64 @46; ConfigureAwait @46; ExecuteScalarAsync @46; NewGuid @53; ToString @55; ToString @68; ExecuteNonQueryAsync @78; Success(CustomerDto) @95 | FROM third_parties @44; INSERT INTO third_parties @60 · PHONE_FORMAT_INVALID @27; CODE_REQUIRED @32; NAME_REQUIRED @37; DUPLICATE_CODE @49 |
| <span id="m-b7c4e68b2da4"></span><code>CustomerCommandHandler.HandleAsync(UpdateCustomerCommand,CommandEnvelope&lt;UpdateCustomerCommand&gt;,CancellationToken)</code><br>98–211 | ToUpperInvariant @106; Trim @106; TryNormalizePhone @108; Failure(CustomerDto) @110; IsNullOrWhiteSpace @113; CreateCommand @126; AddParam @130; ToString @130; ConfigureAwait @131; ExecuteReaderAsync @131; ReadAsync @132; GetString @136; GetInt32 @137; ToInt64 @152; ExecuteScalarAsync @152; ToString @160; ExecuteNonQueryAsync @189; TryParse @192; Success(CustomerDto) @210 | FROM third_parties @129; FROM third_parties @149; UPDATE third_parties @165 · PHONE_FORMAT_INVALID @110; CODE_REQUIRED @115; NAME_REQUIRED @120; CUSTOMER_NOT_FOUND @134; SYSTEM_WALK_IN_PROTECTED @142; DUPLICATE_CODE @155 |
| <span id="m-590723502c08"></span><code>CustomerCommandHandler.HandleAsync(DeactivateCustomerCommand,CommandEnvelope&lt;DeactivateCustomerCommand&gt;,CancellationToken)</code><br>213–253 | CreateCommand @221; AddParam @225; ToString @225; ConfigureAwait @226; ExecuteReaderAsync @226; ReadAsync @227; Failure(bool) @229; GetInt32 @231; ToString @236; ExecuteNonQueryAsync @249; Success(bool) @252 | FROM third_parties @224; UPDATE third_parties @241 · CUSTOMER_NOT_FOUND @229; SYSTEM_WALK_IN_PROTECTED @232 |
| <span id="m-afe62a7587fe"></span><code>CustomerCommandHandler.HandleAsync(ReactivateCustomerCommand,CommandEnvelope&lt;ReactivateCustomerCommand&gt;,CancellationToken)</code><br>255–295 | CreateCommand @263; AddParam @267; ToString @267; ConfigureAwait @268; ExecuteReaderAsync @268; ReadAsync @269; Failure(bool) @271; GetInt32 @273; ToString @278; ExecuteNonQueryAsync @291; Success(bool) @294 | FROM third_parties @266; UPDATE third_parties @283 · CUSTOMER_NOT_FOUND @271; SYSTEM_WALK_IN_PROTECTED @274 |
| <span id="m-2b126b330e8c"></span><code>CustomerCommandHandler.AddParam(DbCommand,string,object)</code><br>297–303 | CreateParameter @299; Add @302 | No extracted literal effects. |

</details>

## CustomerCommands.cs {#src-e38bff3a5457}

<code>Software/src/GetSeek.Application/Customers/CustomerCommands.cs</code> · 61 lines.

SHA-256: <code>25fb48a6ab8dfc1fdafbeaf615e3a11575554954a81f22067eed941dc2e639d5</code>.

Declarations: <code>CustomerDto</code> (line 6), <code>CreateCustomerCommand : ICommand&lt;CustomerDto&gt;</code> (line 20), <code>UpdateCustomerCommand : ICommand&lt;CustomerDto&gt;</code> (line 33), <code>DeactivateCustomerCommand : ICommand&lt;bool&gt;</code> (line 48), <code>ReactivateCustomerCommand : ICommand&lt;bool&gt;</code> (line 56).

## ExpenseCommandHandler.cs {#src-c02b00854044}

<code>Software/src/GetSeek.Application/Expenses/ExpenseCommandHandler.cs</code> · 938 lines.

SHA-256: <code>0556244b325abde2870564177fb212032dc0492ee01a4d0198f2b762a53cce6f</code>.

Declarations: <code>ExpenseCommandHandler : ICommandHandler&lt;CreateExpenseCategoryCommand, Guid&gt;, ICommandHandler&lt;UpdateExpenseCategoryCommand, bool&gt;, ICommandHandler&lt;CreateExpenseRecordCommand, Guid&gt;, ICommandHandler&lt;UpdateExpenseRecordCommand, bool&gt;, ICommandHandler&lt;CancelExpenseRecordCommand, bool&gt;, ICommandHandler&lt;AttachExpensePhotoCommand, Guid&gt;, ICommandHandler&lt;RecordWasteExpenseCommand, Guid&gt;</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-93235f26cceb"></span><code>ExpenseCommandHandler.AddParam(DbCommand,string,object?)</code><br>17–23 | CreateParameter @19; Add @22 | No extracted literal effects. |
| <span id="m-96f0d231de4e"></span><code>ExpenseCommandHandler.HandleAsync(CreateExpenseCategoryCommand,CommandEnvelope&lt;CreateExpenseCategoryCommand&gt;,CancellationToken)</code><br>25–89 | ToString @32; Trim @34; IsNullOrWhiteSpace @35; Failure(Guid) @37; ToUpperInvariant @40; ConfigureAwait @43; GenerateUniqueCategoryCodeAsync @43; CreateCommand @47; AddParam @51; ExecuteScalarAsync @52; ExecuteScalarAsync @65; NewGuid @72; ToString @79; ToString @83; ExecuteNonQueryAsync @85; Success(Guid) @88 | FROM expense_categories @50; FROM expense_categories @63; INSERT INTO expense_categories @76 · CATEGORY_NAME_REQUIRED @37; CATEGORY_NAME_EXISTS @55; CATEGORY_CODE_EXISTS @68 |
| <span id="m-8c7802f61231"></span><code>ExpenseCommandHandler.HandleAsync(UpdateExpenseCategoryCommand,CommandEnvelope&lt;UpdateExpenseCategoryCommand&gt;,CancellationToken)</code><br>91–181 | ToString @98; Trim @100; IsNullOrWhiteSpace @101; Failure(bool) @103; ToUpperInvariant @106; CreateCommand @113; AddParam @117; ToString @117; ConfigureAwait @118; ExecuteScalarAsync @118; ToInt32 @123; ExecuteScalarAsync @138; ExecuteScalarAsync @152; ToString @174; ExecuteNonQueryAsync @177; Success(bool) @180 | FROM expense_categories @116; FROM expense_categories @135; FROM expense_categories @149; UPDATE expense_categories @162 · CATEGORY_NAME_REQUIRED @103; CATEGORY_CODE_REQUIRED @109; CATEGORY_NOT_FOUND @121; STALE_REVISION @128; CATEGORY_NAME_EXISTS @141; CATEGORY_CODE_EXISTS @155 |
| <span id="m-ae4629505dda"></span><code>ExpenseCommandHandler.HandleAsync(CreateExpenseRecordCommand,CommandEnvelope&lt;CreateExpenseRecordCommand&gt;,CancellationToken)</code><br>183–327 | ToString @190; Trim @192; IsNullOrWhiteSpace @193; Failure(Guid) @195; CreateCommand @211; AddParam @215; ToString @215; ConfigureAwait @216; ExecuteScalarAsync @216; ToInt32 @221; ToString @234; ExecuteReaderAsync @235; ReadAsync @236; GetString @240; ToUpperInvariant @244; GenerateUniqueExpenseReferenceAsync @247; ExecuteScalarAsync @255; GetStoreDefaultCurrencyAndScaleAsync @270; ValidatePreparedAttachment @276; NewGuid @280; ToString @281; ToString @298; Trim @308; ToString @310; ToString @312; ToString @313; ExecuteNonQueryAsync @315; InsertExpenseAttachmentAsync @320; Success(Guid) @326 | FROM expense_categories @214; FROM expense_records @253; FROM person_records @233; INSERT INTO expense_records @286 · NAME_REQUIRED @195; INVALID_COST @200; CATEGORY_REQUIRED @205; CATEGORY_NOT_FOUND @219; CATEGORY_INACTIVE @223; PAYEE_NOT_FOUND @238; DUPLICATE_EXPENSE_REFERENCE @258; INVALID_DECIMAL_PLACES @264 |
| <span id="m-e3f2dcc443e0"></span><code>ExpenseCommandHandler.HandleAsync(UpdateExpenseRecordCommand,CommandEnvelope&lt;UpdateExpenseRecordCommand&gt;,CancellationToken)</code><br>329–483 | ToString @336; Trim @338; IsNullOrWhiteSpace @339; Failure(bool) @341; CreateCommand @360; AddParam @367; ToString @367; ConfigureAwait @368; ExecuteReaderAsync @368; ReadAsync @369; GetInt32 @373; GetInt64 @374; Parse @375; GetString @375; IsDBNull @376; ExecuteScalarAsync @400; ToString @423; ExecuteScalarAsync @424; ToInt32 @429; ToString @442; ExecuteScalarAsync @443; ToString @448; ToString @451; Trim @475; ToString @476; ExecuteNonQueryAsync @479; Success(bool) @482 | FROM expense_categories @422; FROM expense_payments @395; FROM expense_records @363; FROM person_records @441; UPDATE expense_records @456 · NAME_REQUIRED @341; INVALID_COST @346; CATEGORY_REQUIRED @351; EXPENSE_NOT_FOUND @371; STALE_REVISION @382; EXPENSE_CANCELLED @387; EXPENSE_PAID_IMMUTABLE @412; CATEGORY_NOT_FOUND @427; CATEGORY_INACTIVE @431; PAYEE_NOT_FOUND @446 |
| <span id="m-61fec5661ff4"></span><code>ExpenseCommandHandler.HandleAsync(CancelExpenseRecordCommand,CommandEnvelope&lt;CancelExpenseRecordCommand&gt;,CancellationToken)</code><br>485–573 | ToString @492; Trim @494; IsNullOrWhiteSpace @495; Failure(bool) @497; CreateCommand @504; AddParam @508; ToString @508; ConfigureAwait @509; ExecuteReaderAsync @509; ReadAsync @510; GetInt32 @514; IsDBNull @515; GetString @515; ExecuteScalarAsync @544; ToString @566; ExecuteNonQueryAsync @569; Success(bool) @572 | FROM expense_payments @539; FROM expense_records @507; UPDATE expense_records @557 · REASON_REQUIRED @497; EXPENSE_NOT_FOUND @512; STALE_REVISION @521; EXPENSE_ALREADY_CANCELLED @526; NON_CASH_EXPENSE_CANNOT_BE_CANCELLED @531; EXPENSE_REFUND_REQUIRED @549 |
| <span id="m-900e1e41614f"></span><code>ExpenseCommandHandler.GenerateUniqueCategoryCodeAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>575–602 | ToUpperInvariant @577; ToArray @577; Take @577; Where @577; CreateCommand @580; AddParam @583; ConfigureAwait @585; ExecuteReaderAsync @585; ReadAsync @587; IsDBNull @589; Add @589; GetString @589; Contains @593; ToString @601; NewGuid @601 | FROM expense_categories @582 |
| <span id="m-0477ed6af7ea"></span><code>ExpenseCommandHandler.GenerateUniqueExpenseReferenceAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>604–627 | CreateCommand @606; ConfigureAwait @610; ExecuteReaderAsync @610; ReadAsync @612; IsDBNull @614; GetString @616; StartsWith @617; TryParse @618 | FROM expense_records @608 |
| <span id="m-52ab336b04d8"></span><code>ExpenseCommandHandler.HandleAsync(AttachExpensePhotoCommand,CommandEnvelope&lt;AttachExpensePhotoCommand&gt;,CancellationToken)</code><br>629–721 | ValidatePreparedAttachment @634; ToString @639; CreateCommand @642; AddParam @646; ToString @646; ConfigureAwait @647; ExecuteReaderAsync @647; ReadAsync @648; Failure(Guid) @650; IsDBNull @652; ExecuteReaderAsync @666; GetString @669; GetInt32 @670; NewGuid @674; ExecuteNonQueryAsync @684; InsertExpenseAttachmentAsync @688; ToString @702; ExecuteNonQueryAsync @704; ExecuteNonQueryAsync @717; Success(Guid) @720 | FROM expense_attachments @664; FROM expense_records @645; UPDATE expense_attachments @682; UPDATE expense_attachments @698; UPDATE expense_records @710 · EXPENSE_NOT_FOUND @650; EXPENSE_ALREADY_CANCELLED @654 |
| <span id="m-64776d08da35"></span><code>ExpenseCommandHandler.ValidatePreparedAttachment(PreparedAttachment?)</code><br>723–726 | ValidatePreparedAttachment @725 | No extracted literal effects. |
| <span id="m-c70c35930186"></span><code>ExpenseCommandHandler.InsertExpenseAttachmentAsync(DbConnection,DbTransaction?,Guid,Guid,int,PreparedAttachment,Guid?,string,CancellationToken)</code><br>728–764 | ToArray @739; CreateCommand @740; AddParam @752; ToString @752; ToString @753; ToString @761; ConfigureAwait @763; ExecuteNonQueryAsync @763 | INSERT INTO expense_attachments @742 |
| <span id="m-cfd75b1de925"></span><code>ExpenseCommandHandler.GetStoreDefaultCurrencyAndScaleAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>766–780 | CreateCommand @769; ConfigureAwait @772; ExecuteReaderAsync @772; ReadAsync @773; IsDBNull @775; GetString @775; GetInt32 @776 | FROM store_config @771 |
| <span id="m-299833ace8cd"></span><code>ExpenseCommandHandler.HandleAsync(RecordWasteExpenseCommand,CommandEnvelope&lt;RecordWasteExpenseCommand&gt;,CancellationToken)</code><br>782–937 | ToString @790; Failure(Guid) @794; CreateCommand @809; AddParam @819; ToString @819; ConfigureAwait @821; ExecuteReaderAsync @821; ReadAsync @822; Parse @827; GetString @827; Abs @829; Parse @829; IsDBNull @834; GetStoreDefaultCurrencyAndScaleAsync @836; IsNullOrWhiteSpace @838; GetInt64 @839; Equals @844; ToString @857; ExecuteScalarAsync @858; Pow @869; Round @881; ToString @892; ExecuteScalarAsync @893; NewGuid @900; GenerateUniqueExpenseReferenceAsync @901; Trim @903; ToString @919; ToString @929; ToString @931; ExecuteNonQueryAsync @933; Success(Guid) @936 | FROM expense_categories @891; FROM expense_records @856; FROM inventory_loss_records @812; INSERT INTO expense_records @909; JOIN items @812 · INVALID_TARGET @794; LOSS_RECORD_NOT_FOUND @824; INELIGIBLE_MOVEMENT @849; WASTE_EXPENSE_ALREADY_RECORDED @861; COST_REQUIRED @878; INVALID_COST @884; CATEGORY_NOT_FOUND @896 |

</details>

## ExpenseCommands.cs {#src-5b8093d7b8c4}

<code>Software/src/GetSeek.Application/Expenses/ExpenseCommands.cs</code> · 156 lines.

SHA-256: <code>8799ac097ab93c73ce47fb37fb023688c58471b4852f7d091100463c04cb2fe9</code>.

Declarations: <code>CreateExpenseCategoryCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 7), <code>UpdateExpenseCategoryCommand : ICommand&lt;bool&gt;, ISanitizedAuditPayload</code> (line 23), <code>CreateExpenseRecordCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 43), <code>RecordWasteExpenseCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 79), <code>UpdateExpenseRecordCommand : ICommand&lt;bool&gt;, ISanitizedAuditPayload</code> (line 100), <code>CancelExpenseRecordCommand : ICommand&lt;bool&gt;, ISanitizedAuditPayload</code> (line 124), <code>AttachExpensePhotoCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 139).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ad7d3838eee6"></span><code>CreateExpenseCategoryCommand.GetSanitizedAuditPayload()</code><br>15–20 | Serialize @15 | No extracted literal effects. |
| <span id="m-217c5d513232"></span><code>UpdateExpenseCategoryCommand.GetSanitizedAuditPayload()</code><br>33–40 | Serialize @33 | No extracted literal effects. |
| <span id="m-f97bef7e50d5"></span><code>CreateExpenseRecordCommand.GetSanitizedAuditPayload()</code><br>62–76 | Serialize @62 | No extracted literal effects. |
| <span id="m-673433f1a4d3"></span><code>RecordWasteExpenseCommand.GetSanitizedAuditPayload()</code><br>90–97 | Serialize @90 | No extracted literal effects. |
| <span id="m-4b7afa611604"></span><code>UpdateExpenseRecordCommand.GetSanitizedAuditPayload()</code><br>113–121 | Serialize @113 | No extracted literal effects. |
| <span id="m-7d8b18afbcb8"></span><code>CancelExpenseRecordCommand.GetSanitizedAuditPayload()</code><br>132–136 | Serialize @132 | No extracted literal effects. |
| <span id="m-d3fbfd050b31"></span><code>AttachExpensePhotoCommand.GetSanitizedAuditPayload()</code><br>147–155 | Serialize @147 | No extracted literal effects. |

</details>

## ExpenseImageValidator.cs {#src-479f5167e6e5}

<code>Software/src/GetSeek.Application/Expenses/ExpenseImageValidator.cs</code> · 280 lines.

SHA-256: <code>fe6d208814d890c8b8c20a5d0791b0c6e0c0b5c7fe95c2584ddf0c1e4e94c5f7</code>.

Declarations: <code>ExpenseImageValidator</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a6786079a993"></span><code>ExpenseImageValidator.ValidatePreparedAttachment(PreparedAttachment?)</code><br>14–71 | Failure(Guid) @20; ToLowerInvariant @34; ToHexString @34; HashData @34; Equals @35; TryValidatePng @43; TryValidateJpeg @55 | EXPENSE_PHOTO_INVALID @20; EXPENSE_PHOTO_TOO_LARGE @25; EXPENSE_PHOTO_INVALID @30; EXPENSE_PHOTO_INVALID @37; EXPENSE_PHOTO_INVALID @45; EXPENSE_PHOTO_INVALID @50; EXPENSE_PHOTO_INVALID @57; EXPENSE_PHOTO_INVALID @62; EXPENSE_PHOTO_INVALID @67 |
| <span id="m-47c139fc4570"></span><code>ExpenseImageValidator.TryValidatePng(byte[],int,int,string?)</code><br>73–200 | Write @153; Read @186 | No extracted literal effects. |
| <span id="m-dbadae9f24f6"></span><code>ExpenseImageValidator.TryValidateJpeg(byte[],int,int,string?)</code><br>202–279 | — | No extracted literal effects. |

</details>

## ExpensePaymentCommandHandler.cs {#src-458534a2cf6c}

<code>Software/src/GetSeek.Application/Expenses/ExpensePaymentCommandHandler.cs</code> · 859 lines.

SHA-256: <code>b94af6c76f600e549a8402837b32a63895ffdc1ed92a821373b0c0c2dc577a97</code>.

Declarations: <code>ExpensePaymentCommandHandler : ICommandHandler&lt;PayExpenseCommand, Guid&gt;, ICommandHandler&lt;SaveAndPayExpenseCommand, Guid&gt;, ICommandHandler&lt;ReverseExpensePaymentCommand, Guid&gt;, ICommandHandler&lt;ReplaceExpenseRecordCommand, Guid&gt;</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-71d74bb2a4bf"></span><code>ExpensePaymentCommandHandler.AddParam(DbCommand,string,object?)</code><br>18–24 | CreateParameter @20; Add @23 | No extracted literal effects. |
| <span id="m-0d05dba96a5d"></span><code>ExpensePaymentCommandHandler.HandleAsync(PayExpenseCommand,CommandEnvelope&lt;PayExpenseCommand&gt;,CancellationToken)</code><br>26–221 | ToString @34; Failure(Guid) @38; Trim @51; IsNullOrWhiteSpace @52; CreateCommand @67; AddParam @71; ToString @71; ConfigureAwait @72; ExecuteReaderAsync @72; ReadAsync @73; GetInt32 @77; GetInt64 @78; IsDBNull @79; GetString @79; ToString @107; ExecuteReaderAsync @108; Equals @122; ExecuteScalarAsync @137; Max @140; NewGuid @153; ToString @155; PostAsync @170; ToString @194; ToString @199; Trim @201; ToString @202; ToString @204; ExecuteNonQueryAsync @207; ExecuteNonQueryAsync @217; Success(Guid) @220 | FROM expense_payments @132; FROM expense_records @70; FROM money_accounts @106; INSERT INTO expense_payments @184; UPDATE expense_records @214 · INVALID_EXPENSE_ID @38; INVALID_ACCOUNT_ID @43; INVALID_AMOUNT @48; REASON_REQUIRED @54; EXPENSE_NOT_FOUND @75; STALE_REVISION @87; EXPENSE_CANCELLED @92; NON_CASH_EXPENSE_CANNOT_BE_PAID @97; ACCOUNT_NOT_FOUND @111; ACCOUNT_NOT_FOUND @118; CURRENCY_MISMATCH @124; EXPENSE_OVERPAYMENT @143; PAID_AT_OVERRIDE_NOT_PERMITTED @150 |
| <span id="m-69191fb4b330"></span><code>ExpensePaymentCommandHandler.HandleAsync(SaveAndPayExpenseCommand,CommandEnvelope&lt;SaveAndPayExpenseCommand&gt;,CancellationToken)</code><br>223–467 | ToString @231; Trim @233; IsNullOrWhiteSpace @234; Failure(Guid) @236; CreateCommand @273; AddParam @277; ToString @277; ConfigureAwait @278; ExecuteScalarAsync @278; ToInt32 @283; ToString @296; ExecuteReaderAsync @297; ReadAsync @298; GetString @302; ToUpperInvariant @306; GenerateUniqueExpenseReferenceAsync @309; ExecuteScalarAsync @317; ValidatePreparedAttachment @326; ToString @342; ExecuteReaderAsync @343; GetInt32 @349; Equals @357; NewGuid @367; ToString @370; ToString @371; PostAsync @386; ToString @410; Trim @420; ToString @422; ToString @424; ExecuteNonQueryAsync @425; InsertExpenseAttachmentAsync @430; ToString @450; Trim @457; ToString @458; ExecuteNonQueryAsync @463; Success(Guid) @466 | FROM expense_categories @276; FROM expense_records @315; FROM money_accounts @341; FROM person_records @295; INSERT INTO expense_payments @440; INSERT INTO expense_records @400 · NAME_REQUIRED @236; INVALID_COST @241; INVALID_AMOUNT @246; EXPENSE_OVERPAYMENT @251; CATEGORY_REQUIRED @256; INVALID_ACCOUNT_ID @261; CATEGORY_NOT_FOUND @281; CATEGORY_INACTIVE @285; PAYEE_NOT_FOUND @300; DUPLICATE_EXPENSE_REFERENCE @320; INVALID_DECIMAL_PLACES @332; ACCOUNT_NOT_FOUND @346; ACCOUNT_NOT_FOUND @353; CURRENCY_MISMATCH @359; PAID_AT_OVERRIDE_NOT_PERMITTED @364 |
| <span id="m-ad30dabc5ae0"></span><code>ExpensePaymentCommandHandler.HandleAsync(ReverseExpensePaymentCommand,CommandEnvelope&lt;ReverseExpensePaymentCommand&gt;,CancellationToken)</code><br>469–665 | ToString @477; Trim @479; IsNullOrWhiteSpace @480; Failure(Guid) @482; CreateCommand @496; AddParam @503; ToString @503; ConfigureAwait @504; ExecuteReaderAsync @504; ReadAsync @505; Parse @510; GetString @510; GetInt64 @512; IsDBNull @514; Equals @524; ExecuteScalarAsync @535; ToString @548; ExecuteScalarAsync @549; ToInt32 @554; ToString @568; ExecuteReaderAsync @569; GetInt32 @575; NewGuid @597; Trim @606; PostAsync @613; ToString @637; ToString @642; ToString @645; ToString @647; ExecuteNonQueryAsync @651; ExecuteNonQueryAsync @661; Success(Guid) @664 | FROM expense_payments @499; FROM expense_payments @533; FROM expense_records @547; FROM money_accounts @567; INSERT INTO expense_payments @627; UPDATE expense_records @658 · REASON_REQUIRED @482; PAYMENT_NOT_FOUND @507; EXPENSE_MISMATCH @521; CANNOT_REVERSE_A_REVERSAL @526; PAYMENT_ALREADY_REVERSED @538; EXPENSE_NOT_FOUND @552; STALE_REVISION @559; ACCOUNT_NOT_FOUND @572; ACCOUNT_NOT_FOUND @578; BANK_CONFIRMATION_REQUIRED @586; SHIFT_NOT_OPEN @593 |
| <span id="m-1517e55bae26"></span><code>ExpensePaymentCommandHandler.HandleAsync(ReplaceExpenseRecordCommand,CommandEnvelope&lt;ReplaceExpenseRecordCommand&gt;,CancellationToken)</code><br>667–833 | ToString @675; Trim @677; IsNullOrWhiteSpace @678; Failure(Guid) @680; CreateCommand @702; AddParam @706; ToString @706; ConfigureAwait @707; ExecuteReaderAsync @707; ReadAsync @708; GetInt32 @712; IsDBNull @713; GetString @713; ExecuteScalarAsync @736; ToString @751; ExecuteScalarAsync @752; ToInt32 @753; ToString @766; ExecuteScalarAsync @767; ToString @772; GenerateUniqueExpenseReferenceAsync @775; NewGuid @776; ToString @777; ToString @794; Trim @804; ToString @806; ExecuteNonQueryAsync @808; ExecuteNonQueryAsync @829; Success(Guid) @832 | FROM expense_categories @750; FROM expense_payments @731; FROM expense_records @705; FROM person_records @765; INSERT INTO expense_records @784; UPDATE expense_records @815 · REASON_REQUIRED @680; NAME_REQUIRED @686; INVALID_COST @691; INVALID_DECIMAL_PLACES @696; EXPENSE_NOT_FOUND @710; STALE_REVISION @718; EXPENSE_ALREADY_CANCELLED @723; EXPENSE_REFUND_REQUIRED @741; CATEGORY_NOT_FOUND @755; PAYEE_NOT_FOUND @770 |
| <span id="m-4bde50ed2fc9"></span><code>ExpensePaymentCommandHandler.GenerateUniqueExpenseReferenceAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>835–858 | CreateCommand @837; ConfigureAwait @841; ExecuteReaderAsync @841; ReadAsync @843; IsDBNull @845; GetString @847; StartsWith @848; TryParse @849 | FROM expense_records @839 |

</details>

## ExpensePaymentCommands.cs {#src-38ab4a4f4fb9}

<code>Software/src/GetSeek.Application/Expenses/ExpensePaymentCommands.cs</code> · 121 lines.

SHA-256: <code>4828aea63448b77b5435af4ef3e486ff08eb317283af73c7fadd3e58dfa90266</code>.

Declarations: <code>PayExpenseCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 7), <code>SaveAndPayExpenseCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 33), <code>ReverseExpensePaymentCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 72), <code>ReplaceExpenseRecordCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 95).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-cc6803b7cfc0"></span><code>PayExpenseCommand.GetSanitizedAuditPayload()</code><br>22–30 | Serialize @22; IsNullOrWhiteSpace @29 | No extracted literal effects. |
| <span id="m-cfe645bdde92"></span><code>SaveAndPayExpenseCommand.GetSanitizedAuditPayload()</code><br>56–69 | Serialize @56; IsNullOrWhiteSpace @65 | No extracted literal effects. |
| <span id="m-ae0aa9c46afe"></span><code>ReverseExpensePaymentCommand.GetSanitizedAuditPayload()</code><br>85–92 | Serialize @85; IsNullOrWhiteSpace @91 | No extracted literal effects. |
| <span id="m-c620b40fbe20"></span><code>ReplaceExpenseRecordCommand.GetSanitizedAuditPayload()</code><br>113–120 | Serialize @113 | No extracted literal effects. |

</details>

## ReprintReceiptCommandHandler.cs {#src-f881cdbb15da}

<code>Software/src/GetSeek.Application/Hardware/ReprintReceiptCommandHandler.cs</code> · 120 lines.

SHA-256: <code>386395f77100eb20cd8c527c266dbd0c87dec786591dd7a34a4e482251bdb0ba</code>.

Declarations: <code>QueueReceiptReprintCommand : ICommand&lt;string&gt;</code> (line 10), <code>QueueReceiptReprintCommandHandler : ICommandHandler&lt;QueueReceiptReprintCommand, string&gt;</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-49d7caffe325"></span><code>QueueReceiptReprintCommandHandler.HandleAsync(QueueReceiptReprintCommand,CommandEnvelope&lt;QueueReceiptReprintCommand&gt;,CancellationToken)</code><br>18–111 | IsNullOrWhiteSpace @20; Failure(string) @21; CreateCommand @25; Add @28; ToString @28; ToInt64 @29; ExecuteScalarAsync @29; Trim @41; ExecuteReaderAsync @42; ReadAsync @43; GetString @45; ExecuteReaderAsync @67; IsDBNull @72; GetInt32 @75; Parse @82; EnqueueAsync @90; ToJsonString @90; ExecuteNonQueryAsync @108; Success(string) @110 | FROM hardware_jobs @58; FROM invoice_collections @36; FROM sale_returns @36; FROM sales_invoices @36; FROM users @27; JOIN user_roles @27; UPDATE hardware_jobs @94 · INVOICE_REQUIRED @21; AUTH_UNAUTHORIZED @30; INVOICE_NOT_FOUND @44; RECEIPT_SNAPSHOT_MISSING @69; RECEIPT_SNAPSHOT_INVALID @87 |
| <span id="m-7ee6f1e899c9"></span><code>QueueReceiptReprintCommandHandler.Add(DbCommand,string,object)</code><br>113–119 | CreateParameter @115; Add @118 | No extracted literal effects. |

</details>

## ImportCommands.cs {#src-60301a99263c}

<code>Software/src/GetSeek.Application/Imports/ImportCommands.cs</code> · 69 lines.

SHA-256: <code>ddadf347f0aa02681e099bdfc5f382101a1a549982b3d7245034230e2013599a</code>.

Declarations: <code>ImportProductRow</code> (line 6), <code>ImportStockRow</code> (line 22), <code>ImportIssue</code> (line 33), <code>ProductImportPreview</code> (line 36), <code>ImportProductsCommand : ICommand&lt;ImportProductsResult&gt;</code> (line 53), <code>ImportProductsResult</code> (line 69).

## ImportDatabaseState.cs {#src-cb21b9739067}

<code>Software/src/GetSeek.Application/Imports/ImportDatabaseState.cs</code> · 277 lines.

SHA-256: <code>a178bc2241933382249dfcca05bad7604a4ac2fc24751379bd75be9891cb5af4</code>.

Declarations: <code>ImportDatabaseState</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-dd1ff44747e4"></span><code>ImportDatabaseState.RecordAsync(DbConnection,DbTransaction?,string,string?,CancellationToken)</code><br>10–20 | CreateCommand @13; CreateParameter @14; Add @14; ConfigureAwait @15; ExecuteReaderAsync @15; ReadAsync @17; GetName @18; IsDBNull @18; ToString @18; GetValue @18 | No extracted literal effects. |
| <span id="m-3613bb998b92"></span><code>ImportDatabaseState.ContextAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>22–26 | ConfigureAwait @24; RecordAsync @24; GetValueOrDefault @25; Parse @25 | FROM store_config @24 |
| <span id="m-1bdcb4d70b3b"></span><code>ImportDatabaseState.ActiveTiersAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>28–35 | CreateCommand @30; ConfigureAwait @32; ExecuteReaderAsync @32; ReadAsync @33; Add @33; GetInt32 @33 | FROM price_level_settings @31; FROM store_config @31 |
| <span id="m-5f8aaaff8c19"></span><code>ImportDatabaseState.FingerprintAsync(DbConnection,DbTransaction?,IEnumerable&lt;string&gt;?,IEnumerable&lt;string&gt;?,CancellationToken)</code><br>37–276 | CreateHash @47; CreateCommand @51; CreateParameter @52; Add @52; AppendData @53; GetBytes @53; ConfigureAwait @54; ExecuteReaderAsync @54; ReadAsync @55; IsDBNull @58; ToString @58; GetValue @58; ToString @59; CreateCommand @78; ToString @83; Join @90; Append @103; ToList @106; Order @106; Distinct @106; Min @123; GetRange @124; CreateInCommand @125; ReadAsync @127; GetString @129; ContainsKey @131; Add @134; TryGetValue @136; IsDBNull @144; GetValue @144; Add @146; GetRange @160; GetOrdinal @166; TryGetValue @170; Add @178; TryGetValue @190; TryGetValue @210; AppendRows @227; GetValueOrDefault @227; GetValueOrDefault @228; GetValueOrDefault @229; GetValueOrDefault @230; GetValueOrDefault @231; GetRange @247; TryGetValue @254; GetValueOrDefault @269; ToHexString @275; GetHashAndReset @275 | FROM barcodes @164; FROM barcodes @42; FROM item_kit_components @236; FROM item_kits @235; FROM item_price_levels @204; FROM item_price_levels @44; FROM item_pricing @184; FROM item_pricing @43; FROM items @114; FROM items @41; FROM items @42; FROM items @43; FROM items @44; FROM price_level_settings @97; FROM product_categories @99; FROM product_category_pricing_rules @100; FROM store_config @96; FROM third_parties @248; FROM third_parties @45; FROM third_party_external_mappings @273; FROM uoms @98; JOIN item_kit_components @118; JOIN item_kit_components @41; JOIN item_kits @117; JOIN item_kits @41; JOIN items @119 |

</details>

## ImportPolicy.cs {#src-2b2491e08f3f}

<code>Software/src/GetSeek.Application/Imports/ImportPolicy.cs</code> · 12 lines.

SHA-256: <code>4996e5537e24feb78b439cb8f3eead27640595173d67e22a989b15c709cdf092</code>.

Declarations: <code>ImportPolicy</code> (line 8).

## ImportProductConfiguration.cs {#src-14918ebf4662}

<code>Software/src/GetSeek.Application/Imports/ImportProductConfiguration.cs</code> · 183 lines.

SHA-256: <code>945a984652a30083c5587eab960c954a74cbdfa6462f822ef5cb846b10fe16bd</code>.

Declarations: <code>ImportProductConfiguration</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-46f1bbc7024c"></span><code>ImportProductConfiguration.SaveAsync(ImportProductRow,IReadOnlyList&lt;ImportKitComponent&gt;,CommandEnvelope&lt;ImportProductsCommand&gt;,ImportWorkbookContext,CancellationToken)</code><br>16–92 | ConfigureAwait @19; RecordAsync @19; Merge @20; GetValueOrDefault @20; Parse @21; TryParseBool @22; GetValueOrDefault @23; Money @24; D @24; Parse @24; ToString @24; Parse @25; Failure(CatalogItemDto) @27; ToString @29; B @30; Where @35; Equals @35; Add @39; IsNullOrWhiteSpace @39; CreateCommand @44; CreateParameter @46; Add @46; ExecuteReaderAsync @47; ReadAsync @48; GetString @48; IsDBNull @48; ToDecimal @48; GetValue @48; GetValueOrDefault @51; M @52; L @55; ToLowerInvariant @57; Trim @57; NormalizePurpose @63; ToString @68; ToString @68; ToString @69; GetValueOrDefault @78; HandleAsync @81; Success(CatalogItemDto) @89 | FROM barcodes @50; FROM item_kit_components @45; FROM item_kits @29; FROM items @19; FROM items @37; JOIN product_categories @19 · IMPORT_SKU_EXISTS @27; IMPORT_SKU_NOT_FOUND @28; IMPORT_CHILD_NOT_FOUND @38 |
| <span id="m-7367d0a4cbf6"></span><code>ImportProductConfiguration.PriceAsync(Guid,string,ImportProductRow?,ImportPricingRule?,IReadOnlyList&lt;ImportTierPrice&gt;,CommandEnvelope&lt;ImportProductsCommand&gt;,ImportWorkbookContext,bool,CancellationToken)</code><br>94–182 | ConfigureAwait @97; RecordAsync @97; ToString @97; Merge @99; GetValueOrDefault @99; Parse @100; TryParseBool @101; GetValueOrDefault @102; D @102; ToLowerInvariant @103; Trim @103; ToUpperInvariant @134; NormalizeMethod @147; M @147; Failure(bool) @150; B @153; Money @156; Parse @156; ActiveTiersAsync @157; Where @159; Equals @159; Contains @161; Add @162; NormalizeTierMode @162; ToDisplayAmount @166; P @167; NormalizeRoundingRule @167; GetValueOrDefault @169; NormalizeCostFloor @169; NormalizeCostBasis @170; GetValueOrDefault @177; Parse @178; Parse @178; HandleAsync @181 | FROM item_pricing @97; FROM items @98; FROM product_category_pricing_rules @174; JOIN items @174 · IMPORT_PRICE_CONFLICT @150; IMPORT_CATEGORY_APPROVAL_REQUIRED @154; INVALID_PRICE_LEVEL @161; CATEGORY_PRICING_RULE_NOT_FOUND @175 |

</details>

## ImportProductsCommandHandler.cs {#src-2c8d126a7c07}

<code>Software/src/GetSeek.Application/Imports/ImportProductsCommandHandler.cs</code> · 445 lines.

SHA-256: <code>742684104bee7336eb467a3473cc0370c0af377059ca1a75c203ae99d4fa6be4</code>.

Declarations: <code>ImportProductsCommandHandler : ICommandHandler&lt;ImportProductsCommand, ImportProductsResult&gt;</code> (line 18).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-c862b652239a"></span><code>ImportProductsCommandHandler.HandleAsync(ImportProductsCommand,CommandEnvelope&lt;ImportProductsCommand&gt;,CancellationToken)</code><br>21–287 | Failure(ImportProductsResult) @28; ConfigureAwait @31; HasActivePermissionAsync @31; ContextAsync @44; ToArray @47; Concat @47; Select @47; Select @47; SelectMany @47; Select @48; FingerprintAsync @49; Any @51; GroupBy @51; Count @51; GroupBy @52; ToUpperInvariant @53; Where @55; GetValueOrDefault @55; IsNullOrWhiteSpace @55; Trim @56; Contains @60; Any @62; Equals @62; Any @65; TryGetValue @91; Add @96; TryGetValue @105; LoadAsync @114; BuildOrderAsync @120; Empty(ImportKitComponent) @133; SaveAsync @134; TryGetValue @147; TryGetValue @163; ResolveItemIdAsync @165; TryGetValue @175; RecordAsync @177; ToString @181; TryGetValue @197; TryGetSupplierId @199; TryGetValue @210; GetValueOrDefault @218; BuildLines @223; HandleAsync @244; Distinct @256; GetValueOrDefault @267; GetValueOrDefault @268; Empty(ImportTierPrice) @271; PriceAsync @273; Success(ImportProductsResult) @286 | FROM item_kits @180; FROM items @215 · IMPORT_EMPTY @28; AUTH_UNAUTHORIZED @33; AUTH_UNAUTHORIZED @39; IMPORT_TOO_LARGE @43; IMPORT_CURRENCY_MISMATCH @46; IMPORT_PREVIEW_STALE @50; IMPORT_DUPLICATE_ROW @54; IMPORT_DUPLICATE_ROW @57; IMPORT_CLEAR_NOT_ALLOWED @61; IMPORT_UNKNOWN_COLUMN @63; IMPORT_CLEAR_NOT_ALLOWED @66; IMPORT_ORPHAN_COMPONENT @150; IMPORT_SKU_NOT_FOUND @168; IMPORT_KIT_STOCK @189; SUPPLIER_NOT_FOUND @201; IMPORT_SKU_NOT_FOUND @263 |
| <span id="m-7ca1ff9bcf79"></span><code>ImportProductsCommandHandler.BuildOrderAsync(IReadOnlyList&lt;ImportProductRow&gt;,IReadOnlyList&lt;ImportKitComponent&gt;?)</code><br>289–314 | TryGetValue @304; Add @309; BuildOrderAsync @313 | No extracted literal effects. |
| <span id="m-09e6f9be8a2e"></span><code>ImportProductsCommandHandler.BuildOrderAsync(IReadOnlyList&lt;ImportProductRow&gt;,IReadOnlyDictionary&lt;string, List&lt;ImportKitComponent&gt;&gt;,IReadOnlyDictionary&lt;string, ImportProductRow&gt;)</code><br>316–322 | FromResult @321; BuildOrder @321 | No extracted literal effects. |
| <span id="m-7a9c2a4e77e5"></span><code>ImportProductsCommandHandler.BuildOrder(IReadOnlyList&lt;ImportProductRow&gt;,IReadOnlyDictionary&lt;string, List&lt;ImportKitComponent&gt;&gt;,IReadOnlyDictionary&lt;string, ImportProductRow&gt;)</code><br>324–408 | Success(IReadOnlyList&lt;ImportProductRow&gt;, ImportProductRow) @332; TryAdd @338; Failure(IReadOnlyList&lt;ImportProductRow&gt;, ImportProductRow) @340; TryGetValue @354; TryGetValue @359; Add @365; Add @372; Enqueue @382; Dequeue @389; Add @390 | IMPORT_DUPLICATE_ROW @340; KIT_CYCLE_DETECTED @363; KIT_CYCLE_DETECTED @404 |
| <span id="m-2dc6aa184df1"></span><code>ImportProductsCommandHandler.BuildLines(ImportStockRow)</code><br>410–423 | — | No extracted literal effects. |
| <span id="m-be92b93116e9"></span><code>ImportProductsCommandHandler.ResolveItemIdAsync(string,CancellationToken)</code><br>425–439 | CreateCommand @427; CreateParameter @430; Add @433; ConfigureAwait @435; ExecuteScalarAsync @435; TryParse @436; ToString @436 | FROM items @429 |
| <span id="m-5f31b55f7530"></span><code>ImportProductsCommandHandler.HasActivePermissionAsync(Guid,string,CancellationToken)</code><br>441–444 | HasPermissionAsync @443 | No extracted literal effects. |

</details>

## ImportWorkbookSchema.cs {#src-65d435d492aa}

<code>Software/src/GetSeek.Application/Imports/ImportWorkbookSchema.cs</code> · 140 lines.

SHA-256: <code>8ffd7c992c7d1c531bd3cce19f209ae8e0eb6afe62a77e3d0eeceb97c590efba</code>.

Declarations: <code>ImportFieldAction</code> (line 6), <code>ImportField</code> (line 8), <code>ImportWorkbookContext</code> (line 15), <code>ImportChoice</code> (line 17), <code>ImportColumn</code> (line 18), <code>ImportSheet</code> (line 19), <code>ImportRowPreview</code> (line 20), <code>ImportKitComponent</code> (line 21), <code>ImportPricingRule</code> (line 22), <code>ImportTierPrice</code> (line 23), <code>ImportWorkbookSchema</code> (line 26).

<details markdown>
<summary>Methods, calls, table effects and failures (10)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e495d4f70c48"></span><code>ImportField.Keep()</code><br>10–10 | — | No extracted literal effects. |
| <span id="m-33178e89f4c6"></span><code>ImportField.Clear()</code><br>11–11 | — | No extracted literal effects. |
| <span id="m-e4072967fdb5"></span><code>ImportField.Set(T)</code><br>12–12 | — | No extracted literal effects. |
| <span id="m-72becb82eabc"></span><code>ImportWorkbookSchema.C(string,string)</code><br>30–30 | — | No extracted literal effects. |
| <span id="m-c54f5abcc139"></span><code>ImportWorkbookSchema.Sheets(string)</code><br>99–100 | — | No extracted literal effects. |
| <span id="m-a76ed3b7508e"></span><code>ImportWorkbookSchema.Fields(IReadOnlyDictionary&lt;string, string&gt;)</code><br>102–104 | ToDictionary @103; IsNullOrWhiteSpace @103; Keep(string) @103; Trim @104; Clear(string) @104; Set(string) @104 | No extracted literal effects. |
| <span id="m-9f6f54100b3e"></span><code>ImportWorkbookSchema.Merge(IReadOnlyDictionary&lt;string, ImportField&lt;string&gt;&gt;?,string,string?)</code><br>106–108 | TryGetValue @107 | No extracted literal effects. |
| <span id="m-f3a5b0aea9de"></span><code>ImportWorkbookSchema.ResolveTier(string?,IReadOnlySet&lt;int&gt;)</code><br>110–120 | IsNullOrWhiteSpace @112; Trim @113; StartsWith @114; Trim @115; TryParse @118; Contains @118 | No extracted literal effects. |
| <span id="m-2144d375a623"></span><code>ImportWorkbookSchema.TryParseBool(string?,bool)</code><br>122–137 | IsNullOrWhiteSpace @124; ToLowerInvariant @125; Trim @125 | No extracted literal effects. |
| <span id="m-bd8a5b478d35"></span><code>ImportWorkbookSchema.Money(decimal,ImportWorkbookContext)</code><br>139–139 | ToMinorUnits @139 | No extracted literal effects. |

</details>

## IntakeCostProcessor.cs {#src-d5d88567add8}

<code>Software/src/GetSeek.Application/Inventory/IntakeCostProcessor.cs</code> · 241 lines.

SHA-256: <code>abe1fab67bed941b8479c4dce46812c3bc01d482506bca743a357975ba21ceef</code>.

Declarations: <code>IntakeCostProcessor</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a9b36dd4f666"></span><code>IntakeCostProcessor.ApplyAsync(DbConnection,DbTransaction?,Guid,decimal,long,DateTime,CancellationToken,decimal?,string?,decimal?,string?,string?,Guid?,bool,string?)</code><br>17–207 | ToString @41; ToString @42; CreateCommand @49; AddParam @53; ConfigureAwait @54; ExecuteReaderAsync @54; ReadAsync @55; IsDBNull @60; GetInt64 @60; TryParseInvariant @62; GetString @62; GetPhysicalOnHandAsync @69; ToMinor @83; ToInvariant @106; ExecuteNonQueryAsync @110; RecordAsync @113; EnqueueAffectedKitAlertsAsync @122; ExecuteReaderAsync @152; ParsePricingMethod @158; ParseStoredPercentage @159; GetInt32 @159; ParseRoundingRule @161; ReadDecimalPlacesAsync @177; ResolveEffectiveBasePrice @199; CreateAsync @201; Parse @204 | FROM item_pricing @141; FROM items @52; JOIN items @141; UPDATE items @93 |
| <span id="m-32c1db4c1d2e"></span><code>IntakeCostProcessor.ToMinor(decimal)</code><br>209–213 | Round @211 | No extracted literal effects. |
| <span id="m-62664b544d15"></span><code>IntakeCostProcessor.ReadDecimalPlacesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>215–231 | CreateCommand @220; ConfigureAwait @223; ExecuteScalarAsync @223; ToInt32 @229 | FROM store_config @222 |
| <span id="m-201193b4b654"></span><code>IntakeCostProcessor.AddParam(DbCommand,string,object)</code><br>233–239 | CreateParameter @235; Add @238 | No extracted literal effects. |

</details>

## InventoryCommandHandler.cs {#src-43bee33cf642}

<code>Software/src/GetSeek.Application/Inventory/InventoryCommandHandler.cs</code> · 868 lines.

SHA-256: <code>8265eed9be27a86658aa05bd3e7dcb3c76c4b6103d55e1e55fb14bfe00a7907d</code>.

Declarations: <code>InventoryCommandHandler : ICommandHandler&lt;ReceiveStockCommand, StockMovement&gt;, ICommandHandler&lt;AdjustStockCommand, StockMovement&gt;</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-88ca70a84a0a"></span><code>InventoryCommandHandler.HandleAsync(ReceiveStockCommand,CommandEnvelope&lt;ReceiveStockCommand&gt;,CancellationToken)</code><br>14–456 | Failure(StockMovement) @24; IsNullOrWhiteSpace @40; TryGetSupplierById @50; CreateCommand @61; AddParam @64; ToString @64; ConfigureAwait @65; ExecuteReaderAsync @65; ReadAsync @66; GetInt32 @70; ToString @85; ExecuteReaderAsync @86; IsDBNull @94; GetString @94; Equals @96; GetActiveKitInfoAsync @111; DecomposeToLeavesAsync @114; ToString @123; ToString @134; ToString @135; ExecuteScalarAsync @135; NewGuid @140; ToString @159; ToString @167; Join @168; ToInvariant @172; ExecuteNonQueryAsync @175; Success(StockMovement) @196; ToUpperInvariant @222; Trim @222; LoadStoredConversionFactorAsync @227; Equals @240; AddRange @249; Add @253; Sum @266; Trim @301; ResolveOrCreateLotAsync @310; ReadLotAsync @319; Add @339; SerialExistsAsync @344; TryRoundBaseQuantity @350; ToString @379; Trim @386; ToString @387; ToString @391; ToString @395; ExecuteNonQueryAsync @401; ExecuteNonQueryAsync @416; ApplyAsync @444 | FROM items @133; FROM items @84; FROM third_parties @63; INSERT INTO serials @409; INSERT INTO stock_movements @143; INSERT INTO stock_movements @363 · INVALID_QUANTITY @24; INVALID_UNIT_COST @28; INVALID_UNIT_COST @31; REFERENCE_REQUIRED @42; SUPPLIER_NOT_FOUND @52; SUPPLIER_INACTIVE @56; SUPPLIER_NOT_FOUND @68; SUPPLIER_INACTIVE @72; ITEM_NOT_FOUND @89; ITEM_CURRENCY_MISMATCH @97; ITEM_INACTIVE @101; SERVICE_STOCK_NOT_ALLOWED @107; COMPONENT_TRACEABILITY_REQUIRED @137; ITEM_NOT_TRACKED @217; UNKNOWN_UOM_CONVERSION @236; LOT_REQUIRED @257; SERIAL_REQUIRED @262; INVALID_QUANTITY @269; INVALID_UOM_CONVERSION @276; SERIAL_COUNT_MISMATCH @281; INVALID_QUANTITY @297; LOT_NUMBER_REQUIRED @307; LOT_CREATE_FAILED @313; LOT_NOT_FOUND @320; LOT_NOT_AVAILABLE @322; UNEXPECTED_SERIAL @325; SERIAL_REQUIRED @331; INVALID_QUANTITY @336; SERIAL_ALREADY_EXISTS @341; SERIAL_ALREADY_EXISTS @346 |
| <span id="m-66bd2a90feb2"></span><code>InventoryCommandHandler.HandleAsync(AdjustStockCommand,CommandEnvelope&lt;AdjustStockCommand&gt;,CancellationToken)</code><br>458–790 | Failure(StockMovement) @468; IsNullOrWhiteSpace @475; Equals @479; Trim @479; Split @479; Contains @480; IndexOf @480; CreateCommand @487; AddParam @491; ToString @491; ConfigureAwait @492; ExecuteReaderAsync @492; ReadAsync @493; GetInt32 @498; IsDBNull @500; GetString @500; ToInt64 @520; ExecuteScalarAsync @520; ToUpperInvariant @534; Trim @534; LoadStoredConversionFactorAsync @539; TryRoundBaseQuantity @554; Abs @554; Equals @563; ReadLotAsync @573; ReadSerialAsync @593; GetLocationBalanceAsync @603; GetLotLocationBalanceAsync @614; SerialIsHeldOrReservedAsync @619; Trim @631; ExecuteScalarAsync @633; NewGuid @641; ToString @679; ToString @686; ToString @688; ToString @690; ToInvariant @694; ExecuteNonQueryAsync @698; CurrentCostAsync @723; TryParse(InventoryLossReason) @724; RecordAsync @726; ExecuteAsync @729; ExecuteScalarAsync @736; ToInt32 @737; ExecuteScalarAsync @746; Round @753; ToString @757; ToString @773; ToString @784; ExecuteNonQueryAsync @785; Success(StockMovement) @789 | FROM item_kits @518; FROM items @490; FROM stock_movements @623; FROM store_config @735; FROM store_config @745; INSERT INTO stock_movements @663; INSERT OR IGNORE INTO expense_records @763; UPDATE serials @730 · INVALID_QUANTITY @468; REASON_REQUIRED @477; REASON_REQUIRED @481; ITEM_NOT_FOUND @495; ITEM_INACTIVE @505; SERVICE_STOCK_NOT_ALLOWED @511; CANNOT_ADJUST_KIT_STOCK @523; ITEM_NOT_TRACKED @529; UNKNOWN_UOM_CONVERSION @548; LOT_REQUIRED @568; LOT_NOT_FOUND @574; LOT_NOT_AVAILABLE @576; INVALID_UOM_CONVERSION @581; SERIAL_REQUIRED @584; INVALID_QUANTITY @589; USE_SERIAL_RECEIPT @592; SERIAL_NOT_AVAILABLE @595; UNEXPECTED_SERIAL @598; INSUFFICIENT_STOCK @608; INSUFFICIENT_LOT_BALANCE @615; SERIAL_RESERVED @620; SERIAL_NOT_FOUND @636 |
| <span id="m-793a9560917e"></span><code>InventoryCommandHandler.LoadStoredConversionFactorAsync(DbConnection,DbTransaction?,Guid,string,string,CancellationToken)</code><br>797–801 | ConfigureAwait @799; ResolveFactorAsync @799 | No extracted literal effects. |
| <span id="m-5b53dba16221"></span><code>InventoryCommandHandler.ResolveOrCreateLotAsync(DbConnection,DbTransaction?,Guid,string,DateTime?,DateTime,CancellationToken)</code><br>812–847 | CreateCommand @821; AddParam @825; ToString @825; ConfigureAwait @827; ExecuteScalarAsync @827; TryParse @830; ToString @830; NewGuid @834; ToString @840; ToString @844; ExecuteNonQueryAsync @845 | FROM lots @824; INSERT INTO lots @837 |
| <span id="m-c5d5cc75528a"></span><code>InventoryCommandHandler.SerialExistsAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>850–858 | CreateCommand @852; AddParam @855; ToInt64 @856; ConfigureAwait @856; ExecuteScalarAsync @856 | FROM serials @854 |
| <span id="m-c697cfcf9357"></span><code>InventoryCommandHandler.AddParam(DbCommand,string,object)</code><br>860–866 | CreateParameter @862; Add @865 | No extracted literal effects. |

</details>

## InventoryCommands.cs {#src-85c6e1df3363}

<code>Software/src/GetSeek.Application/Inventory/InventoryCommands.cs</code> · 56 lines.

SHA-256: <code>b3225b381ba62b62bdea04be6999f764512e9fdcece09dbe95cc29ec76f32382</code>.

Declarations: <code>ReceiptLine</code> (line 12), <code>ReceiveStockCommand : ICommand&lt;StockMovement&gt;</code> (line 19), <code>AdjustStockCommand : ICommand&lt;StockMovement&gt;</code> (line 42).

## InventoryLossCommandHandler.cs {#src-ad1ac7eca868}

<code>Software/src/GetSeek.Application/Inventory/InventoryLossCommandHandler.cs</code> · 32 lines.

SHA-256: <code>9fa28390769c4a3aa19ac7d77d1721b5fcf92c133520f180afddfb47c6ef0651</code>.

Declarations: <code>InventoryLossCommandHandler : ICommandHandler&lt;RecordInventoryLossCommand,InventoryLossResult&gt;</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-435d0a757769"></span><code>InventoryLossCommandHandler.HandleAsync(RecordInventoryLossCommand,CommandEnvelope&lt;RecordInventoryLossCommand&gt;,CancellationToken)</code><br>10–31 | ConfigureAwait @13; ReadAsync @13; Equals @14; Text @14; Failure(InventoryLossResult) @15; IsDefined @17; IsNullOrWhiteSpace @18; HandleAsync @24; Success(InventoryLossResult) @29; Parse @29; Amount @30 | FROM inventory_loss_records @27; FROM items @13 · SERVICE_STOCK_NOT_ALLOWED @15; INVALID_LOSS @19 |

</details>

## InventoryLossCommands.cs {#src-b3991f732d77}

<code>Software/src/GetSeek.Application/Inventory/InventoryLossCommands.cs</code> · 12 lines.

SHA-256: <code>2577b19e702b2ae69c60bf7c361977c282fc90d11db66e0678727db6bd67a5e7</code>.

Declarations: <code>RecordInventoryLossCommand : ICommand&lt;InventoryLossResult&gt;</code> (line 7).

## InventoryLossWriter.cs {#src-9575bf742ae3}

<code>Software/src/GetSeek.Application/Inventory/InventoryLossWriter.cs</code> · 78 lines.

SHA-256: <code>d58bcd24b870822c70a7e6c652d7b7d40931117be0c925484ef06e528956bbb2</code>.

Declarations: <code>InventoryLossWriter</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-da6277bffa07"></span><code>InventoryLossWriter.RecordAsync(DbConnection,DbTransaction?,StockMovement,string,string,decimal?,InventoryLossReason,Guid,CancellationToken)</code><br>9–42 | ConfigureAwait @12; ReadAsync @12; Equals @13; Text @13; NewGuid @16; Round @16; BusinessDateAsync @25; ExecuteAsync @26; ToString @34 | FROM items @12; FROM return_disposition_resolutions @17; FROM sale_returns @17; INSERT INTO inventory_loss_records @26; JOIN return_dispositions @17; JOIN sale_return_lines @17; JOIN sale_returns @17; UPDATE inventory_loss_records @39 · InvalidOperationException @14 |
| <span id="m-0b1fb964f5d8"></span><code>InventoryLossWriter.CurrentCostAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>44–55 | ConfigureAwait @46; ReadAsync @46; Amount @52; QuantityValue @53; Text @54 | FROM item_price_history @46; FROM items @46 · InvalidOperationException @51 |
| <span id="m-29e8b8c31c56"></span><code>InventoryLossWriter.MoveAsync(DbConnection,DbTransaction?,Guid,decimal,string,string,string,Guid?,string?,string,Guid,Guid,DateTime,string,CancellationToken,StockMovementType)</code><br>57–77 | ConfigureAwait @61; ReadAsync @61; Equals @62; Text @62; NewGuid @65; ExecuteAsync @66; ToString @75 | FROM items @61; INSERT INTO stock_movements @66 · InvalidOperationException @63 |

</details>

## InventoryTraceabilityCommands.cs {#src-1e2a68301de6}

<code>Software/src/GetSeek.Application/Inventory/InventoryTraceabilityCommands.cs</code> · 76 lines.

SHA-256: <code>77d337938bd2bd60b5aced45b211793f8b481a2569c9aad34f63130c2a3c503a</code>.

Declarations: <code>SetLotStockQuantityCommand : ICommand&lt;LotStockRow&gt;</code> (line 8), <code>UpdateLotExpiryCommand : ICommand&lt;LotStockRow&gt;</code> (line 10), <code>SerialRemovalSelection</code> (line 12), <code>RemoveInventorySerialsCommand : ICommand&lt;int&gt;</code> (line 13), <code>InventoryTraceabilityCommandHandler : ICommandHandler&lt;SetLotStockQuantityCommand, LotStockRow&gt;, ICommandHandler&lt;UpdateLotExpiryCommand, LotStockRow&gt;, ICommandHandler&lt;RemoveInventorySerialsCommand, int&gt;</code> (line 16).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-07cdbc10b980"></span><code>InventoryTraceabilityCommandHandler.HandleAsync(SetLotStockQuantityCommand,CommandEnvelope&lt;SetLotStockQuantityCommand&gt;,CancellationToken)</code><br>21–38 | Failure(LotStockRow) @23; ConfigureAwait @24; ReadLotAsync @24; IsNullOrWhiteSpace @27; Trim @31; ConfigureAwait(AdjustStockCommand) @32; HandleAsync @32; NewGuid @33; Success(LotStockRow) @37 | INVALID_QUANTITY @23; LOT_NOT_FOUND @25; TRACEABILITY_STALE @26; REASON_REQUIRED @27 |
| <span id="m-cae97948113a"></span><code>InventoryTraceabilityCommandHandler.HandleAsync(UpdateLotExpiryCommand,CommandEnvelope&lt;UpdateLotExpiryCommand&gt;,CancellationToken)</code><br>40–53 | ConfigureAwait @42; ReadLotAsync @42; Failure(LotStockRow) @43; IsNullOrWhiteSpace @46; CreateCommand @47; Add @49; ToString @49; ToString @50; ToString @50; ExecuteNonQueryAsync @51; Success(LotStockRow) @52 | UPDATE lots @48 · LOT_NOT_FOUND @43; TRACEABILITY_STALE @45; REASON_REQUIRED @46 |
| <span id="m-e067a0efc2fc"></span><code>InventoryTraceabilityCommandHandler.HandleAsync(RemoveInventorySerialsCommand,CommandEnvelope&lt;RemoveInventorySerialsCommand&gt;,CancellationToken)</code><br>55–75 | Count @57; Distinct @57; Select @57; Trim @57; Failure(int) @58; IsNullOrWhiteSpace @59; ConfigureAwait @62; ReadSerialAsync @62; Trim @68; ConfigureAwait(AdjustStockCommand) @69; HandleAsync @69; NewGuid @70; Success(int) @74 | INVALID_SERIAL_SELECTION @58; REASON_REQUIRED @59; SERIAL_NOT_AVAILABLE @63; TRACEABILITY_STALE @64 |

</details>

## InventoryTraceabilityState.cs {#src-4453c1947c24}

<code>Software/src/GetSeek.Application/Inventory/InventoryTraceabilityState.cs</code> · 74 lines.

SHA-256: <code>da6e1498e8c243dc990f2ee831d415bd2bdd3c8c9679724a65c6ee1c761e68f0</code>.

Declarations: <code>LotStockRow</code> (line 10), <code>SerialStockRow</code> (line 11), <code>InventoryTraceabilityState</code> (line 13).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a30e8227c9c1"></span><code>InventoryTraceabilityState.ReadLotAsync(DbConnection,DbTransaction?,Guid,Guid,CancellationToken)</code><br>15–31 | CreateCommand @18; Add @22; ToString @22; ToString @22; ConfigureAwait @23; ExecuteReaderAsync @23; ReadAsync @24; GetString @25; Parse @27; GetLotLocationBalanceAsync @28; LastMovementAsync @29; Hash @30 | FROM lots @21 |
| <span id="m-e943dd91f0a5"></span><code>InventoryTraceabilityState.ReadSerialAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>33–62 | CreateCommand @36; Add @40; ToString @40; Trim @40; ConfigureAwait @41; ExecuteReaderAsync @41; ReadAsync @42; GetString @43; IsDBNull @54; GetDecimal @54; Parse @54; Equals @55; LastMovementAsync @59; Equals @60; Hash @61 | FROM serials @39; FROM stock_movements @49 |
| <span id="m-c152f3b3afbc"></span><code>InventoryTraceabilityState.Hash(object)</code><br>64–64 | ToHexString @64; HashData @64; GetBytes @64; Serialize @64 | No extracted literal effects. |
| <span id="m-dd2ead31971b"></span><code>InventoryTraceabilityState.LastMovementAsync(DbConnection,DbTransaction?,Guid,string,bool,CancellationToken)</code><br>65–71 | CreateCommand @67; Add @69; ToString @69; ToInt64 @70; ConfigureAwait @70; ExecuteScalarAsync @70 | FROM stock_movements @68 |
| <span id="m-03ef65c6fcc5"></span><code>InventoryTraceabilityState.Add(DbCommand,string,object?)</code><br>72–73 | CreateParameter @73; Add @73 | No extracted literal effects. |

</details>

## KitDecompositionEngine.cs {#src-9cbc6e2603e3}

<code>Software/src/GetSeek.Application/Inventory/KitDecompositionEngine.cs</code> · 397 lines.

SHA-256: <code>23e4892cace7a9e393990d68841f01b75acc7e78b760d1e8e814d75e1a978979</code>.

Declarations: <code>DecomposedKitLeaf</code> (line 7), <code>KitComponentHierarchyNode</code> (line 20), <code>KitDecompositionEngine</code> (line 31), <code>KitDecompositionResult</code> (line 377).

<details markdown>
<summary>Methods, calls, table effects and failures (8)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-8d1d7a98496f"></span><code>KitDecompositionEngine.GetActiveKitInfoAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>38–57 | CreateCommand @44; AddParam @47; ToString @47; ConfigureAwait @48; ExecuteReaderAsync @48; ReadAsync @49; Parse @51; GetString @51; GetInt32 @52 | FROM item_kits @46 |
| <span id="m-c5ad622940d8"></span><code>KitDecompositionEngine.DecomposeToLeavesAsync(DbConnection,DbTransaction?,Guid,decimal,CancellationToken)</code><br>63–270 | CreateCommand @70; AddParam @74; ToString @74; ConfigureAwait @75; ExecuteScalarAsync @75; Equals @76; ToString @76; Failure @78; GetActiveKitInfoAsync @82; ExecuteScalarAsync @97; ToString @98; Enqueue @102; ThrowIfCancellationRequested @106; Dequeue @107; ToString @134; ExecuteReaderAsync @135; ReadAsync @136; GetInt32 @138; GetString @139; IsDBNull @147; GetDouble @154; TryResolveQuantity @155; TryResolveFactor @162; Add @170; Parse @171; Last @187; Contains @192; ToString @218; ExecuteReaderAsync @219; ReadAsync @220; GetString @222; GetInt32 @225; IsDBNull @226; TryRoundBaseQuantity @237; TryGetValue @245; ToList @256; Select @256; Success @269 | FROM item_kit_components @124; FROM items @217; FROM items @73; FROM items @95; JOIN items @124 · SERVICE_KIT_NOT_ALLOWED @78; NOT_A_KIT @85; MAX_DEPTH_EXCEEDED @111; COMPONENT_INACTIVE @144; SERVICE_KIT_NOT_ALLOWED @150; EMPTY_KIT @187; CYCLIC_RELATIONSHIP @194; SERVICE_KIT_NOT_ALLOWED @230; INVALID_SERIAL_QUANTITY_FRACTIONAL @239 |
| <span id="m-2fddc37ae2e0"></span><code>KitDecompositionEngine.FormatDecompositionSummary(string,decimal,IReadOnlyList&lt;DecomposedKitLeaf&gt;)</code><br>276–281 | Select @279; ToLowerInvariant @279; Join @280 | No extracted literal effects. |
| <span id="m-fae4f809043f"></span><code>KitDecompositionEngine.BuildBreakdownSummaryAsync(DbConnection,DbTransaction?,Guid,decimal,CancellationToken)</code><br>288–302 | ConfigureAwait @295; GetActiveKitInfoAsync @295; GetChildSummariesRecursiveAsync @298; Join @301 | No extracted literal effects. |
| <span id="m-282199fc3d00"></span><code>KitDecompositionEngine.GetChildSummariesRecursiveAsync(DbConnection,DbTransaction?,Guid,decimal,HashSet&lt;Guid&gt;,int,CancellationToken)</code><br>304–366 | CreateCommand @316; AddParam @327; ToString @327; ConfigureAwait @328; ExecuteReaderAsync @328; ReadAsync @329; Parse @331; GetString @331; IsDBNull @333; GetDouble @334; TryResolveQuantity @335; TryResolveFactor @339; Add @341; GetActiveKitInfoAsync @349; Contains @351; GetChildSummariesRecursiveAsync @354; Add @357; Join @357 | FROM item_kit_components @319; JOIN items @319 |
| <span id="m-fca99b54a2d7"></span><code>KitDecompositionEngine.AddParam(DbCommand,string,object?)</code><br>368–374 | CreateParameter @370; Add @373 | No extracted literal effects. |
| <span id="m-e04b65923145"></span><code>KitDecompositionResult.Success(IReadOnlyList&lt;DecomposedKitLeaf&gt;)</code><br>392–393 | — | No extracted literal effects. |
| <span id="m-36566c5d784f"></span><code>KitDecompositionResult.Failure(string,string)</code><br>395–396 | — | No extracted literal effects. |

</details>

## LocationCommandHandler.cs {#src-a5752d2091f0}

<code>Software/src/GetSeek.Application/Inventory/LocationCommandHandler.cs</code> · 539 lines.

SHA-256: <code>631675c0149a5bcf4197aee026d668adac5406dfc2f5f06dd2c1f8d8a7d970f8</code>.

Declarations: <code>LocationCommandHandler : ICommandHandler&lt;CreateFacilityCommand, FacilityDto&gt;, ICommandHandler&lt;UpdateFacilityCommand, FacilityDto&gt;, ICommandHandler&lt;DeactivateFacilityCommand, bool&gt;, ICommandHandler&lt;CreateLocationBinCommand, BinLocationDto&gt;, ICommandHandler&lt;UpdateLocationBinCommand, BinLocationDto&gt;, ICommandHandler&lt;DeactivateLocationBinCommand, bool&gt;, ICommandHandler&lt;SetItemLocationEligibilityCommand, ItemLocationDto&gt;, ICommandHandler&lt;RemoveItemLocationEligibilityCommand, bool&gt;</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-df91c4003dce"></span><code>LocationCommandHandler.HandleAsync(CreateFacilityCommand,CommandEnvelope&lt;CreateFacilityCommand&gt;,CancellationToken)</code><br>18–74 | ToUpperInvariant @26; Trim @26; IsNullOrWhiteSpace @29; Failure(FacilityDto) @31; CreateCommand @39; AddParam @43; ToInt64 @44; ConfigureAwait @44; ExecuteScalarAsync @44; ToString @51; NewGuid @51; Trim @62; ExecuteNonQueryAsync @64; Success(FacilityDto) @67 | FROM facilities @42; INSERT INTO facilities @55 · CODE_REQUIRED @31; NAME_REQUIRED @36; DUPLICATE_CODE @47 |
| <span id="m-38510a8f429d"></span><code>LocationCommandHandler.HandleAsync(UpdateFacilityCommand,CommandEnvelope&lt;UpdateFacilityCommand&gt;,CancellationToken)</code><br>76–149 | ToUpperInvariant @84; Trim @84; IsNullOrWhiteSpace @87; Failure(FacilityDto) @89; CreateCommand @97; AddParam @101; ToInt64 @102; ConfigureAwait @102; ExecuteScalarAsync @102; ExecuteScalarAsync @115; Trim @135; ExecuteNonQueryAsync @139; Success(FacilityDto) @142 | FROM facilities @100; FROM facilities @112; UPDATE facilities @125 · CODE_REQUIRED @89; NAME_REQUIRED @94; FACILITY_NOT_FOUND @105; DUPLICATE_CODE @118 |
| <span id="m-53c69375e9a6"></span><code>LocationCommandHandler.HandleAsync(DeactivateFacilityCommand,CommandEnvelope&lt;DeactivateFacilityCommand&gt;,CancellationToken)</code><br>151–180 | CreateCommand @159; AddParam @163; ToInt64 @164; ConfigureAwait @164; ExecuteScalarAsync @164; Failure(bool) @167; ExecuteNonQueryAsync @176; Success(bool) @179 | FROM facilities @162; UPDATE facilities @174 · FACILITY_NOT_FOUND @167 |
| <span id="m-d32cea7d7bd3"></span><code>LocationCommandHandler.HandleAsync(CreateLocationBinCommand,CommandEnvelope&lt;CreateLocationBinCommand&gt;,CancellationToken)</code><br>182–256 | Trim @190; IsNullOrWhiteSpace @191; Failure(BinLocationDto) @193; CreateCommand @197; AddParam @201; ConfigureAwait @202; ExecuteScalarAsync @202; ToInt32 @207; ToInt64 @220; ExecuteScalarAsync @220; ToString @227; NewGuid @227; ExecuteNonQueryAsync @243; Success(BinLocationDto) @246 | FROM bins @217; FROM facilities @200; INSERT INTO bins @231 · CODE_REQUIRED @193; FACILITY_NOT_FOUND @205; FACILITY_INACTIVE @209; DUPLICATE_CODE @223 |
| <span id="m-99e9ab387b2d"></span><code>LocationCommandHandler.HandleAsync(UpdateLocationBinCommand,CommandEnvelope&lt;UpdateLocationBinCommand&gt;,CancellationToken)</code><br>258–348 | Trim @266; IsNullOrWhiteSpace @267; Failure(BinLocationDto) @269; CreateCommand @272; AddParam @276; ToInt64 @277; ConfigureAwait @277; ExecuteScalarAsync @277; ExecuteScalarAsync @290; ExecuteScalarAsync @305; ExecuteNonQueryAsync @335; Success(BinLocationDto) @338 | FROM bins @275; FROM bins @301; FROM facilities @288; UPDATE bins @315 · CODE_REQUIRED @269; BIN_NOT_FOUND @280; FACILITY_NOT_FOUND @293; DUPLICATE_CODE @308 |
| <span id="m-dc8cae9c46fa"></span><code>LocationCommandHandler.HandleAsync(DeactivateLocationBinCommand,CommandEnvelope&lt;DeactivateLocationBinCommand&gt;,CancellationToken)</code><br>350–379 | CreateCommand @358; AddParam @362; ToInt64 @363; ConfigureAwait @363; ExecuteScalarAsync @363; Failure(bool) @366; ExecuteNonQueryAsync @375; Success(bool) @378 | FROM bins @361; UPDATE bins @373 · BIN_NOT_FOUND @366 |
| <span id="m-9c7ea12506b5"></span><code>LocationCommandHandler.HandleAsync(SetItemLocationEligibilityCommand,CommandEnvelope&lt;SetItemLocationEligibilityCommand&gt;,CancellationToken)</code><br>381–495 | Trim @389; IsNullOrWhiteSpace @390; Failure(ItemLocationDto) @392; CreateCommand @396; AddParam @400; ToString @400; ConfigureAwait @401; ExecuteScalarAsync @401; ToInt32 @406; ExecuteScalarAsync @418; ExecuteNonQueryAsync @436; ExecuteNonQueryAsync @446; NewGuid @449; ToString @451; ToString @472; ExecuteNonQueryAsync @481; Success(ItemLocationDto) @484 | FROM bins @416; FROM items @399; INSERT INTO item_locations @456; UPDATE item_locations @434; UPDATE item_locations @444 · LOCATION_REQUIRED @392; ITEM_NOT_FOUND @404; ITEM_INACTIVE @408; LOCATION_NOT_FOUND @421; LOCATION_INACTIVE @425 |
| <span id="m-6fd38c96bfec"></span><code>LocationCommandHandler.HandleAsync(RemoveItemLocationEligibilityCommand,CommandEnvelope&lt;RemoveItemLocationEligibilityCommand&gt;,CancellationToken)</code><br>497–530 | Trim @505; CreateCommand @507; AddParam @511; ToString @511; ToInt64 @513; ConfigureAwait @513; ExecuteScalarAsync @513; Failure(bool) @516; ExecuteNonQueryAsync @526; Success(bool) @529 | DELETE FROM item_locations @523; FROM item_locations @510 · LOCATION_ELIGIBILITY_NOT_FOUND @516 |
| <span id="m-68fb56f879c0"></span><code>LocationCommandHandler.AddParam(DbCommand,string,object)</code><br>532–538 | CreateParameter @534; Add @537 | No extracted literal effects. |

</details>

## LocationCommands.cs {#src-7a24e4740ac8}

<code>Software/src/GetSeek.Application/Inventory/LocationCommands.cs</code> · 115 lines.

SHA-256: <code>3340048d26eb96854c11bfc4013ab121958d24d737795ee6706fd718f1b89a10</code>.

Declarations: <code>FacilityDto</code> (line 6), <code>CreateFacilityCommand : ICommand&lt;FacilityDto&gt;</code> (line 14), <code>UpdateFacilityCommand : ICommand&lt;FacilityDto&gt;</code> (line 23), <code>DeactivateFacilityCommand : ICommand&lt;bool&gt;</code> (line 34), <code>BinLocationDto</code> (line 41), <code>CreateLocationBinCommand : ICommand&lt;BinLocationDto&gt;</code> (line 52), <code>UpdateLocationBinCommand : ICommand&lt;BinLocationDto&gt;</code> (line 64), <code>DeactivateLocationBinCommand : ICommand&lt;bool&gt;</code> (line 78), <code>ItemLocationDto</code> (line 85), <code>SetItemLocationEligibilityCommand : ICommand&lt;ItemLocationDto&gt;</code> (line 97), <code>RemoveItemLocationEligibilityCommand : ICommand&lt;bool&gt;</code> (line 109).

## PhysicalUnitResolver.cs {#src-e054e263d20d}

<code>Software/src/GetSeek.Application/Inventory/PhysicalUnitResolver.cs</code> · 194 lines.

SHA-256: <code>2467643bc19c1777e36b2a9d08b29acb88148229613497fff1a6e96fdc0e0c39</code>.

Declarations: <code>PhysicalUnitResolver</code> (line 16).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5672ff32fb3e"></span><code>PhysicalUnitResolver.ResolveFactor(ReferenceSnapshot,string,string,Guid?)</code><br>18–71 | IsNullOrWhiteSpace @24; Equals @29; Trim @29; Trim @29; ToUpperInvariant @34; TryGetUom @37; TryParse @61 | No extracted literal effects. |
| <span id="m-5dfe32530006"></span><code>PhysicalUnitResolver.ResolveFactorAsync(DbConnection,DbTransaction?,string,string,Guid?,CancellationToken)</code><br>73–80 | ResolveFactorAsync @80 | No extracted literal effects. |
| <span id="m-99db0db7a63a"></span><code>PhysicalUnitResolver.ResolveFactorAsync(DbConnection,DbTransaction?,string,string,Guid?,ReferenceSnapshot?,CancellationToken)</code><br>82–193 | ResolveFactor @93; IsNullOrWhiteSpace @96; Equals @101; Trim @101; Trim @101; ToUpperInvariant @106; CreateCommand @110; CreateParameter @118; Add @121; ConfigureAwait @134; ExecuteReaderAsync @134; ReadAsync @136; GetString @138; IsDBNull @139; GetInt32 @142; TryParse @182 | FROM uoms @113 |

</details>

## StockAvailability.cs {#src-8d6feb481072}

<code>Software/src/GetSeek.Application/Inventory/StockAvailability.cs</code> · 50 lines.

SHA-256: <code>1912cc929458ab6d2672624afd213c2ea65facb1a1b8d229a4c8c4232649c588</code>.

Declarations: <code>StockAvailability</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (8)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-90ab2e02b10c"></span><code>StockAvailability.GetLocationBalanceAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>11–12 | GetLocationBalanceAsync @12 | No extracted literal effects. |
| <span id="m-bf5adde9e9aa"></span><code>StockAvailability.GetLocationBalanceAsync(DbConnection,DbTransaction?,Guid,string,Guid?,CancellationToken)</code><br>13–18 | ConfigureAwait @16; GetLocationBalanceAsync @16; Equals @17; ReservedAsync @17; HeldAsync @17 | No extracted literal effects. |
| <span id="m-6c78c51e38a3"></span><code>StockAvailability.GetLotLocationBalanceAsync(DbConnection,DbTransaction?,Guid,Guid,string,CancellationToken)</code><br>19–19 | GetLotLocationBalanceAsync @19 | No extracted literal effects. |
| <span id="m-a2485db9051f"></span><code>StockAvailability.GetLotLocationBalanceAsync(DbConnection,DbTransaction?,Guid,Guid,string,Guid?,CancellationToken)</code><br>20–25 | ConfigureAwait @23; GetLotLocationBalanceAsync @23; Equals @24; ReservedAsync @24; HeldAsync @24 | No extracted literal effects. |
| <span id="m-a9e04ecfade3"></span><code>StockAvailability.SerialIsReservedAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>26–28 | ConfigureAwait @28; ReservedAsync @28 | No extracted literal effects. |
| <span id="m-902c85a6d8e9"></span><code>StockAvailability.SerialIsHeldOrReservedAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>30–34 | ConfigureAwait @32; SerialIsReservedAsync @32; ReadAsync @33 | FROM pending_allocations @33 |
| <span id="m-5be2bf4239e1"></span><code>StockAvailability.HeldAsync(DbConnection,DbTransaction?,Guid,Guid?,Guid?,CancellationToken)</code><br>35–39 | ConfigureAwait @37; ReadAsync @37; Sum @38; Parse @38; Text @38 | FROM pending_allocations @37 |
| <span id="m-6c576c180d74"></span><code>StockAvailability.ReservedAsync(DbConnection,DbTransaction?,Guid,Guid?,string?,CancellationToken)</code><br>40–49 | ConfigureAwait @43; ReadAsync @43; Sum @48; Parse @48; Text @48 | FROM invoice_stock_reservations @43 |

</details>

## StockBalanceCalculator.cs {#src-8defdbb6a1cd}

<code>Software/src/GetSeek.Application/Inventory/StockBalanceCalculator.cs</code> · 242 lines.

SHA-256: <code>dee916615c9109ec1dc960f548a2ab11d94d0ce39081b0aec2873f0e2a772c7f</code>.

Declarations: <code>StockBalanceCalculator</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (8)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a8337ef1261e"></span><code>StockBalanceCalculator.GetLocationBalanceAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>21–66 | IsNullOrWhiteSpace @28; Trim @33; CreateCommand @35; AddText @43; ToString @43; ConfigureAwait @47; ExecuteReaderAsync @47; ReadAsync @48; ReadQuantity @50; GetString @51; Equals @54 | FROM stock_movements @37 |
| <span id="m-485f902c58a0"></span><code>StockBalanceCalculator.GetLotLocationBalanceAsync(DbConnection,DbTransaction?,Guid,Guid,string,CancellationToken)</code><br>73–112 | IsNullOrWhiteSpace @81; Trim @86; CreateCommand @87; AddText @96; ToString @96; ToString @97; ConfigureAwait @101; ExecuteReaderAsync @101; ReadAsync @102; ReadQuantity @104; GetString @105; Equals @107 | FROM stock_movements @89 |
| <span id="m-9de6165bba5d"></span><code>StockBalanceCalculator.GetPhysicalOnHandAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>118–123 | ConfigureAwait @123; GetPhysicalOnHandAsync @123 | No extracted literal effects. |
| <span id="m-20e0adb6b0ef"></span><code>StockBalanceCalculator.GetPhysicalOnHandAsync(DbConnection,DbTransaction?,Guid,long?,CancellationToken)</code><br>129–170 | CreateCommand @136; AddText @144; ToString @144; CreateParameter @145; Add @148; ConfigureAwait @151; ExecuteReaderAsync @151; ReadAsync @152; ReadQuantity @154; GetString @155; IsVirtualLocation @158 | FROM stock_movements @138 |
| <span id="m-d9b5f4fc5878"></span><code>StockBalanceCalculator.GetPhysicalOnHandByItemsAsync(DbConnection,DbTransaction?,IReadOnlyCollection&lt;Guid&gt;,CancellationToken)</code><br>177–212 | ToDictionary @183; Distinct @183; ToArray @184; ToArray @188; Take @188; Skip @188; CreateCommand @189; Select @191; Join @195; AddText @198; ToString @198; ConfigureAwait @200; ExecuteReaderAsync @200; ReadAsync @201; Parse @203; GetString @203; ReadQuantity @204; IsVirtualLocation @207 | DYNAMIC SQL: inspect manually |
| <span id="m-d21561314bf7"></span><code>StockBalanceCalculator.ReadQuantity(DbDataReader,int,int)</code><br>214–219 | IsDBNull @216; GetString @216; GetDouble @217; ResolveQuantity @218 | No extracted literal effects. |
| <span id="m-8f63deb26938"></span><code>StockBalanceCalculator.IsVirtualLocation(string)</code><br>221–233 | IsNullOrWhiteSpace @223; Trim @228; StartsWith @229 | No extracted literal effects. |
| <span id="m-c568ce5028a8"></span><code>StockBalanceCalculator.AddText(DbCommand,string,string)</code><br>235–241 | CreateParameter @237; Add @240 | No extracted literal effects. |

</details>

## StockLedgerLocations.cs {#src-2ca2d4ef5c24}

<code>Software/src/GetSeek.Application/Inventory/StockLedgerLocations.cs</code> · 17 lines.

SHA-256: <code>50971e64f025e4ebfacf009090fd93d9c5059af22fee7e92db020951290b26e7</code>.

Declarations: <code>StockLedgerLocations</code> (line 7).

## CycleDetectionEngine.cs {#src-d4c31fbdcfb2}

<code>Software/src/GetSeek.Application/Manufacturing/CycleDetectionEngine.cs</code> · 102 lines.

SHA-256: <code>424312603c04c2a99090f4afafcc1ebb56a09485c7f039416c04d92a2d78d51d</code>.

Declarations: <code>CycleDetectionEngine</code> (line 3).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-6e7dd2a50232"></span><code>CycleDetectionEngine.DetectCycleAsync(Guid,IEnumerable&lt;Guid&gt;,Func&lt;Guid, Task&lt;IEnumerable&lt;Guid&gt;&gt;&gt;,CancellationToken)</code><br>5–53 | Enqueue @20; ThrowIfCancellationRequested @25; Dequeue @26; Add @33; ConfigureAwait @38; getChildrenFunc @38; Contains @45 | No extracted literal effects. |
| <span id="m-09077ed391a1"></span><code>CycleDetectionEngine.DetectCycleInMemory(Guid,IEnumerable&lt;Guid&gt;,Func&lt;Guid, IEnumerable&lt;Guid&gt;&gt;)</code><br>55–101 | Enqueue @69; Dequeue @74; Add @81; getChildrenFunc @86; Contains @93 | No extracted literal effects. |

</details>

## ManufacturingCommandHandler.cs {#src-e469f680f9bb}

<code>Software/src/GetSeek.Application/Manufacturing/ManufacturingCommandHandler.cs</code> · 1,730 lines.

SHA-256: <code>041160fae1957af9d2bfc38ecd85cf66cfab90c9bf952600c084220bba5faa7a</code>.

Declarations: <code>ManufacturingCommandHandler : ICommandHandler&lt;CreateItemVariantCommand, ItemVariantDto&gt;, ICommandHandler&lt;RemoveItemVariantCommand, bool&gt;, ICommandHandler&lt;CreateKitCommand, ItemKitDto&gt;, ICommandHandler&lt;UpdateKitCommand, ItemKitDto&gt;, ICommandHandler&lt;DeactivateKitCommand, bool&gt;, ICommandHandler&lt;CreateBomCommand, BomDto&gt;, ICommandHandler&lt;UpdateBomCommand, BomDto&gt;, ICommandHandler&lt;DeactivateBomCommand, bool&gt;, ICommandHandler&lt;ExecuteProductionRunCommand, ProductionRunDto&gt;, ICommandHandler&lt;CreateProductionDraftCommand, ProductionRunDto&gt;, ICommandHandler&lt;StageProductionRunCommand, ProductionRunDto&gt;, ICommandHandler&lt;CompleteProductionRunCommand, ProductionRunDto&gt;, ICommandHandler&lt;CancelProductionRunCommand, bool&gt;</code> (line 13).

<details markdown>
<summary>Methods, calls, table effects and failures (18)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5227a4c7e32f"></span><code>ManufacturingCommandHandler.HandleAsync(CreateItemVariantCommand,CommandEnvelope&lt;CreateItemVariantCommand&gt;,CancellationToken)</code><br>28–116 | Failure(ItemVariantDto) @38; Trim @41; IsNullOrWhiteSpace @44; CreateCommand @50; AddParam @54; ToString @54; ToInt64 @55; ConfigureAwait @55; ExecuteScalarAsync @55; ToString @68; ExecuteReaderAsync @69; ReadAsync @70; GetString @72; NewGuid @81; ToString @94; ToString @99; ExecuteNonQueryAsync @101; Success(ItemVariantDto) @115 | FROM items @53; FROM items @67; INSERT INTO item_variants @87 · PARENT_CANNOT_BE_VARIANT @38; OPTION_REQUIRED @46; PARENT_ITEM_NOT_FOUND @57; VARIANT_ITEM_NOT_FOUND @77 |
| <span id="m-004d2b130c9f"></span><code>ManufacturingCommandHandler.HandleAsync(RemoveItemVariantCommand,CommandEnvelope&lt;RemoveItemVariantCommand&gt;,CancellationToken)</code><br>118–134 | CreateCommand @126; AddParam @129; ToString @129; ToString @130; ConfigureAwait @131; ExecuteNonQueryAsync @131; Success(bool) @133 | DELETE FROM item_variants @128 |
| <span id="m-f6c0f76b3ec8"></span><code>ManufacturingCommandHandler.HandleAsync(CreateKitCommand,CommandEnvelope&lt;CreateKitCommand&gt;,CancellationToken)</code><br>136–149 | ConfigureAwait @141; CreateOrUpdateKitInternalAsync @141 | No extracted literal effects. |
| <span id="m-de55ac15d61c"></span><code>ManufacturingCommandHandler.HandleAsync(UpdateKitCommand,CommandEnvelope&lt;UpdateKitCommand&gt;,CancellationToken)</code><br>151–164 | ConfigureAwait @156; CreateOrUpdateKitInternalAsync @156 | No extracted literal effects. |
| <span id="m-b8fa04917f75"></span><code>ManufacturingCommandHandler.HandleAsync(DeactivateKitCommand,CommandEnvelope&lt;DeactivateKitCommand&gt;,CancellationToken)</code><br>166–181 | CreateCommand @174; AddParam @177; ToString @177; ConfigureAwait @178; ExecuteNonQueryAsync @178; Success(bool) @180 | UPDATE item_kits @176 |
| <span id="m-63049f36f6ae"></span><code>ManufacturingCommandHandler.HandleAsync(CreateBomCommand,CommandEnvelope&lt;CreateBomCommand&gt;,CancellationToken)</code><br>183–198 | ConfigureAwait @188; CreateOrUpdateBomInternalAsync @188 | No extracted literal effects. |
| <span id="m-9f106ee245b2"></span><code>ManufacturingCommandHandler.HandleAsync(UpdateBomCommand,CommandEnvelope&lt;UpdateBomCommand&gt;,CancellationToken)</code><br>200–215 | ConfigureAwait @205; CreateOrUpdateBomInternalAsync @205 | No extracted literal effects. |
| <span id="m-851734501c25"></span><code>ManufacturingCommandHandler.HandleAsync(DeactivateBomCommand,CommandEnvelope&lt;DeactivateBomCommand&gt;,CancellationToken)</code><br>217–232 | CreateCommand @225; AddParam @228; ToString @228; ConfigureAwait @229; ExecuteNonQueryAsync @229; Success(bool) @231 | UPDATE boms @227 |
| <span id="m-9c5de1eeeb47"></span><code>ManufacturingCommandHandler.HandleAsync(ExecuteProductionRunCommand,CommandEnvelope&lt;ExecuteProductionRunCommand&gt;,CancellationToken)</code><br>234–238 | ConfigureAwait @238; ExecuteProductionCoreAsync @238 | No extracted literal effects. |
| <span id="m-62cdd0de17ec"></span><code>ManufacturingCommandHandler.ExecuteProductionCoreAsync(ExecuteProductionRunCommand,CommandEnvelope&lt;ExecuteProductionRunCommand&gt;,CancellationToken,ProductionRunDto?,bool)</code><br>240–871 | Failure(ProductionRunDto) @253; Resolve @267; CreateCommand @278; AddParam @287; ToString @287; ConfigureAwait @289; ExecuteReaderAsync @289; ReadAsync @290; Parse @292; GetString @292; GetDecimal @293; GetInt32 @294; IsDBNull @298; Equals @299; ToString @319; ToInt64 @320; ExecuteScalarAsync @320; ExecuteReaderAsync @343; ResolveQuantity @352; GetDouble @354; ResolveFactor @355; Add @360; IsNullOrWhiteSpace @386; Trim @386; Trim @387; GroupBy @390; Where @390; First @392; Sum @393; GetLocationBalanceAsync @395; NewGuid @408; ToString @410; ToUpperInvariant @411; ToString @411; ExecuteReaderAsync @427; ReadAsync @428; IsDBNull @430; GetString @430; GetInt32 @431; Parse @444; AddDays @452; ExecuteScalarAsync @464; ToString @468; ReadLotAsync @469; ToString @484; ToString @488; ExecuteNonQueryAsync @489; ToString @501; ExecuteScalarAsync @502; ToString @505; TryGetValue @509; ToString @524; ExecuteReaderAsync @526; ReadAsync @527; GetString @531; CloseAsync @542; Sum @543; GetLotLocationBalanceAsync @545; ToString @572; ToInvariant @578; ToString @582; Trim @587; ExecuteNonQueryAsync @607; ExecuteReaderAsync @623; ReadAsync @624; Parse @627; GetString @627; IsDBNull @627; GetInt64 @627; ExecuteScalarAsync @650; ToString @651; Round @651; ToString @671; ExecuteNonQueryAsync @689; ToString @707; ExecuteNonQueryAsync @721; ExecuteAsync @722; Add @724; Success(ProductionRunDto) @747; ToString @768; ExecuteNonQueryAsync @784; ToString @804; ExecuteNonQueryAsync @816; ApplyAsync @829; MoveAsync @837; CurrentCostAsync @841; RecordAsync @842 | FROM bom_items @334; FROM boms @281; FROM item_kits @318; FROM items @419; FROM items @500; FROM items @648; FROM lots @461; FROM lots @523; FROM production_run_inputs @619; INSERT INTO lots @480; INSERT INTO production_run_inputs @695; INSERT INTO production_run_outputs @792; INSERT INTO production_run_scrap @838; INSERT INTO production_runs @558; INSERT INTO stock_movements @657; INSERT INTO stock_movements @754; JOIN bom_outputs @419; JOIN items @281; JOIN items @334; UPDATE production_run_inputs @722; UPDATE production_runs @592; UPDATE stock_movements @722 · INVALID_QUANTITY @253; INVALID_YIELD @258; INVALID_SCRAP @263; INVALID_LOT_FORMULA @268; SERVICE_STOCK_NOT_ALLOWED @301; BOM_NOT_FOUND @306; BOM_INACTIVE @312; CANNOT_PRODUCE_KIT @323; SERVICE_STOCK_NOT_ALLOWED @349; BOM_NO_INGREDIENTS @375; COMPONENT_INACTIVE @382; INSUFFICIENT_INGREDIENT_STOCK @401; SERIAL_PRODUCTION_UNSUPPORTED @437; OUTPUT_LOT_REQUIRED @439; LOT_NOT_AVAILABLE @471; LOT_EXPIRED @473; SERIAL_PRODUCTION_UNSUPPORTED @511; EXPLICIT_LOT_REQUIRED @514; LOT_NOT_FOUND @529; LOT_NOT_AVAILABLE @535; LOT_EXPIRED @540; INSUFFICIENT_LOT_STOCK @548; RUN_STATE_CHANGED @608; RUN_INPUTS_MISSING @630 |
| <span id="m-f3945c1d6e7e"></span><code>ManufacturingCommandHandler.HandleAsync(CreateProductionDraftCommand,CommandEnvelope&lt;CreateProductionDraftCommand&gt;,CancellationToken)</code><br>873–996 | ToString @881; Failure(ProductionRunDto) @885; Resolve @888; CreateCommand @899; AddParam @908; ToString @908; ConfigureAwait @909; ExecuteReaderAsync @909; ReadAsync @910; Parse @912; GetString @912; GetDecimal @913; GetInt32 @914; IsDBNull @918; Equals @919; NewGuid @935; ToUpperInvariant @936; ToString @936; IsNullOrWhiteSpace @937; Trim @937; Trim @938; ToString @957; ToInvariant @961; ToString @962; Trim @966; ExecuteNonQueryAsync @969; Success(ProductionRunDto) @995 | FROM boms @902; INSERT INTO production_runs @943; JOIN items @902 · INVALID_QUANTITY @885; INVALID_LOT_FORMULA @889; SERVICE_STOCK_NOT_ALLOWED @921; BOM_NOT_FOUND @926; BOM_INACTIVE @932 |
| <span id="m-d88e4ed45202"></span><code>ManufacturingCommandHandler.HandleAsync(StageProductionRunCommand,CommandEnvelope&lt;StageProductionRunCommand&gt;,CancellationToken)</code><br>998–1018 | ConfigureAwait @1003; LoadProductionRunByIdAsync @1003; Failure(ProductionRunDto) @1004; NewGuid @1014; ExecuteProductionCoreAsync @1017 | RUN_NOT_FOUND @1004; RUN_NOT_PLANNED @1005; UNSUPPORTED_OUTPUT_ALLOCATION @1007; UNSUPPORTED_INPUT_ALLOCATION @1009 |
| <span id="m-eada56fe976e"></span><code>ManufacturingCommandHandler.HandleAsync(CompleteProductionRunCommand,CommandEnvelope&lt;CompleteProductionRunCommand&gt;,CancellationToken)</code><br>1020–1069 | ToString @1028; ConfigureAwait @1030; LoadProductionRunByIdAsync @1030; Failure(ProductionRunDto) @1033; Equals @1036; NewGuid @1059; ExecuteProductionCoreAsync @1068 | RUN_NOT_FOUND @1033; RUN_ALREADY_COMPLETED @1038; RUN_ALREADY_CANCELLED @1042 |
| <span id="m-4e8a2227ebb2"></span><code>ManufacturingCommandHandler.HandleAsync(CancelProductionRunCommand,CommandEnvelope&lt;CancelProductionRunCommand&gt;,CancellationToken)</code><br>1071–1118 | ToString @1079; CreateCommand @1082; AddParam @1086; ToString @1086; ConfigureAwait @1087; ExecuteScalarAsync @1087; Failure(bool) @1090; ToString @1092; Equals @1095; Trim @1112; ExecuteNonQueryAsync @1114; Success(bool) @1117 | FROM production_runs @1085; UPDATE production_runs @1106 · RUN_NOT_FOUND @1090; CANNOT_CANCEL_COMPLETED_RUN @1097; CANNOT_CANCEL_STARTED_RUN @1101 |
| <span id="m-8114ff5ae044"></span><code>ManufacturingCommandHandler.LoadProductionRunByIdAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>1120–1161 | CreateCommand @1122; AddParam @1135; ToString @1135; ConfigureAwait @1136; ExecuteReaderAsync @1136; ReadAsync @1137; Parse @1140; GetString @1140; GetDecimal @1146; IsDBNull @1147; Parse @1155 | FROM production_runs @1124; JOIN boms @1124; JOIN items @1124; JOIN lots @1124 |
| <span id="m-8e59724fd864"></span><code>ManufacturingCommandHandler.CreateOrUpdateKitInternalAsync(Guid,string,bool,IReadOnlyList&lt;KitComponentInput&gt;,DateTime,CancellationToken)</code><br>1163–1440 | Trim @1174; IsNullOrWhiteSpace @1175; Failure(ItemKitDto) @1177; CreateCommand @1189; AddParam @1193; ToString @1193; ConfigureAwait @1194; ExecuteReaderAsync @1194; ReadAsync @1195; GetString @1197; GetInt32 @1199; IsDBNull @1203; Equals @1204; GetPhysicalOnHandAsync @1217; ToInt64 @1238; ExecuteScalarAsync @1238; ToList @1248; Distinct @1248; Select @1248; ConfigureAwait(Guid) @1250; DetectCycleAsync @1250; ToString @1264; ExecuteReaderAsync @1265; ReadAsync @1266; Add @1268; Parse @1268; GetString @1268; ToString @1298; ExecuteReaderAsync @1299; ToUpperInvariant @1324; Trim @1324; ResolveFactorAsync @1329; TryRoundBaseQuantity @1340; Add @1349; NewGuid @1350; ExecuteNonQueryAsync @1366; ToInt32 @1375; ExecuteScalarAsync @1375; ToString @1380; ToString @1389; ExecuteNonQueryAsync @1396; ToString @1408; ToString @1410; ToInvariant @1415; ExecuteNonQueryAsync @1418; EnqueueAffectedKitAlertsAsync @1424; Success(ItemKitDto) @1439 | FROM boms @1236; FROM item_kits @1258; FROM item_kits @1373; FROM items @1192; FROM items @1297; INSERT INTO item_kit_components @1403; INSERT INTO item_kits @1385; JOIN item_kit_components @1258; UPDATE item_kits @1364 · NAME_REQUIRED @1177; COMPONENTS_REQUIRED @1182; ITEM_INACTIVE @1201; SERVICE_KIT_NOT_ALLOWED @1206; ITEM_NOT_FOUND @1212; KIT_PARENT_STOCK_MUST_BE_ZERO @1220; KIT_PARENT_MUST_BE_UNTRACKED @1227; ITEM_HAS_BOM @1241; CYCLIC_RELATIONSHIP @1277; INVALID_QUANTITY @1285; SERVICE_KIT_NOT_ALLOWED @1310; COMPONENT_NOT_FOUND @1315; COMPONENT_INACTIVE @1321 |
| <span id="m-89c8dd55e8cc"></span><code>ManufacturingCommandHandler.CreateOrUpdateBomInternalAsync(Guid,string,decimal,bool,IReadOnlyList&lt;BomItemInput&gt;,DateTime,string?,CancellationToken)</code><br>1442–1720 | Resolve @1455; Failure(BomDto) @1456; Trim @1458; IsNullOrWhiteSpace @1459; CreateCommand @1477; AddParam @1481; ToString @1481; ConfigureAwait @1482; ExecuteReaderAsync @1482; ReadAsync @1483; GetString @1485; GetInt32 @1487; IsDBNull @1491; Equals @1492; ToInt64 @1509; ExecuteScalarAsync @1509; ToList @1519; Distinct @1519; Select @1519; ConfigureAwait(Guid) @1521; DetectCycleAsync @1521; ToString @1535; ExecuteReaderAsync @1536; ReadAsync @1537; Add @1539; Parse @1539; GetString @1539; ToString @1573; ExecuteReaderAsync @1574; ToUpperInvariant @1598; Trim @1598; ResolveFactorAsync @1603; Add @1613; NewGuid @1614; ExecuteNonQueryAsync @1631; ToInt32 @1640; ExecuteScalarAsync @1640; ToString @1652; ExecuteNonQueryAsync @1659; ToString @1675; ToInvariant @1679; ToString @1681; ExecuteNonQueryAsync @1682; ToString @1694; ToString @1696; ExecuteNonQueryAsync @1704; Success(BomDto) @1719 | FROM boms @1529; FROM boms @1638; FROM item_kits @1507; FROM items @1480; FROM items @1572; INSERT INTO bom_items @1689; INSERT INTO bom_outputs @1665; INSERT INTO boms @1648; JOIN bom_items @1529; UPDATE boms @1629 · INVALID_LOT_FORMULA @1456; NAME_REQUIRED @1461; INVALID_YIELD @1466; INGREDIENTS_REQUIRED @1471; ITEM_INACTIVE @1489; SERVICE_STOCK_NOT_ALLOWED @1494; ITEM_NOT_FOUND @1499; ITEM_IS_KIT @1512; CYCLIC_RELATIONSHIP @1548; INVALID_QUANTITY @1556; INVALID_SCRAP_FACTOR @1561; SERVICE_STOCK_NOT_ALLOWED @1584; INGREDIENT_NOT_FOUND @1589; COMPONENT_INACTIVE @1595 |
| <span id="m-651f9bf2e671"></span><code>ManufacturingCommandHandler.AddParam(DbCommand,string,object)</code><br>1722–1728 | CreateParameter @1724; Add @1727 | No extracted literal effects. |

</details>

## ManufacturingCommands.cs {#src-98743155dc28}

<code>Software/src/GetSeek.Application/Manufacturing/ManufacturingCommands.cs</code> · 327 lines.

SHA-256: <code>5e221784e575a2e9f28b1768ea5a2f862481572195589fa34dfd7d307921cda9</code>.

Declarations: <code>ItemVariantDto</code> (line 8), <code>KitComponentDto</code> (line 19), <code>ItemKitDto</code> (line 29), <code>BomItemDto</code> (line 41), <code>BomOutputDto</code> (line 52), <code>BomDto</code> (line 65), <code>ProductionRunInputDto</code> (line 78), <code>ProductionRunOutputDto</code> (line 98), <code>ProductionRunScrapDto</code> (line 117), <code>ProductionRunDto</code> (line 130), <code>ProductionRunInputAllocation</code> (line 156), <code>ProductionRunOutputAllocation</code> (line 169), <code>KitComponentInput</code> (line 181), <code>BomItemInput</code> (line 187), <code>CreateItemVariantCommand : ICommand&lt;ItemVariantDto&gt;</code> (line 195), <code>RemoveItemVariantCommand : ICommand&lt;bool&gt;</code> (line 205), <code>CreateKitCommand : ICommand&lt;ItemKitDto&gt;</code> (line 213), <code>UpdateKitCommand : ICommand&lt;ItemKitDto&gt;</code> (line 222), <code>DeactivateKitCommand : ICommand&lt;bool&gt;</code> (line 232), <code>CreateBomCommand : ICommand&lt;BomDto&gt;</code> (line 239), <code>UpdateBomCommand : ICommand&lt;BomDto&gt;</code> (line 250), <code>DeactivateBomCommand : ICommand&lt;bool&gt;</code> (line 262), <code>ExecuteProductionRunCommand : ICommand&lt;ProductionRunDto&gt;</code> (line 269), <code>CreateProductionDraftCommand : ICommand&lt;ProductionRunDto&gt;</code> (line 285), <code>StageProductionRunCommand : ICommand&lt;ProductionRunDto&gt;</code> (line 297), <code>CompleteProductionRunCommand : ICommand&lt;ProductionRunDto&gt;</code> (line 307), <code>CancelProductionRunCommand : ICommand&lt;bool&gt;</code> (line 321).

## ProductionLotFormula.cs {#src-1bc8ed78332e}

<code>Software/src/GetSeek.Application/Manufacturing/ProductionLotFormula.cs</code> · 25 lines.

SHA-256: <code>4b767d2857f4e1343b60651b71630a5746b1d64c2cbcf54f25ec0cf4575534b5</code>.

Declarations: <code>ProductionLotFormula</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e80b41fde762"></span><code>ProductionLotFormula.Resolve(string?,DateTime)</code><br>9–24 | IsNullOrWhiteSpace @11; Replace @13; Trim @13; ToString @16; ToString @17; GetInt32 @17; Contains @22 | ArgumentException @12; ArgumentException @20; ArgumentException @22 |

</details>

## RestaurantOrderCommandHandler.cs {#src-b930bdf2056c}

<code>Software/src/GetSeek.Application/Orders/RestaurantOrderCommandHandler.cs</code> · 411 lines.

SHA-256: <code>a80c799c5f6a3ec759b8a53c6381d8951b5704b22a7ce2e734bbb9d768a52c74</code>.

Declarations: <code>RestaurantOrderCommandHandler : ICommandHandler&lt;CreateRestaurantOrderCommand, RestaurantOrder&gt;, ICommandHandler&lt;SendOrderToKitchenCommand, RestaurantOrder&gt;, ICommandHandler&lt;UpdateRestaurantOrderStatusCommand, RestaurantOrder&gt;, ICommandHandler&lt;CancelRestaurantOrderCommand, RestaurantOrder&gt;, ICommandHandler&lt;SettleRestaurantOrderCommand, RestaurantOrder&gt;</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-66cac9aca0aa"></span><code>RestaurantOrderCommandHandler.HandleAsync(CreateRestaurantOrderCommand,CommandEnvelope&lt;CreateRestaurantOrderCommand&gt;,CancellationToken)</code><br>23–139 | Failure(RestaurantOrder) @33; NewGuid @36; CreateCommand @39; AddParam @52; ToString @52; ToString @54; ToString @55; ToString @66; ToString @67; ConfigureAwait @70; ExecuteNonQueryAsync @70; Add @90; ToString @102; ToString @105; ExecuteNonQueryAsync @113; Success(RestaurantOrder) @138 | INSERT INTO restaurant_order_lines @94; INSERT INTO restaurant_orders @42 · EMPTY_ORDER @33 |
| <span id="m-93af95f2f9c1"></span><code>RestaurantOrderCommandHandler.HandleAsync(SendOrderToKitchenCommand,CommandEnvelope&lt;SendOrderToKitchenCommand&gt;,CancellationToken)</code><br>141–197 | ConfigureAwait @149; LoadOrderAsync @149; Failure(RestaurantOrder) @152; CreateCommand @161; AddParam @165; ToString @166; ToString @167; ExecuteNonQueryAsync @168; Serialize @175; ConvertAll @185; EnqueueAsync @194; Success(RestaurantOrder) @196 | UPDATE restaurant_orders @164 · ORDER_NOT_FOUND @152; INVALID_STATUS @157 |
| <span id="m-cc0c2ea16a9e"></span><code>RestaurantOrderCommandHandler.HandleAsync(UpdateRestaurantOrderStatusCommand,CommandEnvelope&lt;UpdateRestaurantOrderStatusCommand&gt;,CancellationToken)</code><br>199–233 | ConfigureAwait @207; LoadOrderAsync @207; Failure(RestaurantOrder) @210; CreateCommand @219; AddParam @223; ToString @224; ToString @225; ExecuteNonQueryAsync @226; Success(RestaurantOrder) @232 | UPDATE restaurant_orders @222 · ORDER_NOT_FOUND @210; INVALID_STATUS @215 |
| <span id="m-38d044c06b45"></span><code>RestaurantOrderCommandHandler.HandleAsync(CancelRestaurantOrderCommand,CommandEnvelope&lt;CancelRestaurantOrderCommand&gt;,CancellationToken)</code><br>235–287 | ConfigureAwait @243; LoadOrderAsync @243; Failure(RestaurantOrder) @246; CreateCommand @255; AddParam @259; ToString @260; ToString @261; ExecuteNonQueryAsync @262; Serialize @270; EnqueueAsync @280; Success(RestaurantOrder) @286 | UPDATE restaurant_orders @258 · ORDER_NOT_FOUND @246; ORDER_ALREADY_SETTLED @251 |
| <span id="m-1ace6b54b045"></span><code>RestaurantOrderCommandHandler.HandleAsync(SettleRestaurantOrderCommand,CommandEnvelope&lt;SettleRestaurantOrderCommand&gt;,CancellationToken)</code><br>289–325 | ConfigureAwait @297; LoadOrderAsync @297; Failure(RestaurantOrder) @300; CreateCommand @309; AddParam @313; ToString @314; ToString @315; ToString @316; ExecuteNonQueryAsync @317; Success(RestaurantOrder) @324 | UPDATE restaurant_orders @312 · ORDER_NOT_FOUND @300; ORDER_VOIDED @305 |
| <span id="m-14d1b799a2c6"></span><code>RestaurantOrderCommandHandler.LoadOrderAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>327–402 | CreateCommand @334; AddParam @342; ToString @342; ConfigureAwait @344; ExecuteReaderAsync @344; ReadAsync @345; GetString @347; Parse @350; IsDBNull @354; GetInt32 @358; GetInt64 @359; Parse @366; ExecuteReaderAsync @382; ReadAsync @383; Add @385; GetString @387; GetInt32 @389; GetDecimal @392; GetInt64 @393; IsDBNull @395 | FROM restaurant_order_lines @376; FROM restaurant_orders @337 |
| <span id="m-f60043d2c1c6"></span><code>RestaurantOrderCommandHandler.AddParam(DbCommand,string,object?)</code><br>404–410 | CreateParameter @406; Add @409 | No extracted literal effects. |

</details>

## RestaurantOrderCommands.cs {#src-6ec4352e1907}

<code>Software/src/GetSeek.Application/Orders/RestaurantOrderCommands.cs</code> · 105 lines.

SHA-256: <code>5fb55ea55b576f7244a0e08231f0ff507e8f8cd45c371f91e7670cfd4c339054</code>.

Declarations: <code>RestaurantOrderLineInput</code> (line 9), <code>CreateRestaurantOrderCommand : ICommand&lt;RestaurantOrder&gt;, ISanitizedAuditPayload</code> (line 18), <code>SendOrderToKitchenCommand : ICommand&lt;RestaurantOrder&gt;, ISanitizedAuditPayload</code> (line 53), <code>UpdateRestaurantOrderStatusCommand : ICommand&lt;RestaurantOrder&gt;, ISanitizedAuditPayload</code> (line 67), <code>CancelRestaurantOrderCommand : ICommand&lt;RestaurantOrder&gt;, ISanitizedAuditPayload</code> (line 81), <code>SettleRestaurantOrderCommand : ICommand&lt;RestaurantOrder&gt;, ISanitizedAuditPayload</code> (line 94).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-af8acecb2f0f"></span><code>CreateRestaurantOrderCommand.GetSanitizedAuditPayload()</code><br>37–50 | Serialize @39 | No extracted literal effects. |
| <span id="m-4d44324a9044"></span><code>SendOrderToKitchenCommand.GetSanitizedAuditPayload()</code><br>61–64 | Serialize @63 | No extracted literal effects. |
| <span id="m-09ea47c32176"></span><code>UpdateRestaurantOrderStatusCommand.GetSanitizedAuditPayload()</code><br>75–78 | Serialize @77 | No extracted literal effects. |
| <span id="m-13c9a5974af5"></span><code>CancelRestaurantOrderCommand.GetSanitizedAuditPayload()</code><br>88–91 | Serialize @90 | No extracted literal effects. |
| <span id="m-cd9194f7fc44"></span><code>SettleRestaurantOrderCommand.GetSanitizedAuditPayload()</code><br>101–104 | Serialize @103 | No extracted literal effects. |

</details>

## PersonCommandHandler.cs {#src-8317fb4c0e84}

<code>Software/src/GetSeek.Application/Payroll/PersonCommandHandler.cs</code> · 808 lines.

SHA-256: <code>4fe15ca4f38d4d0bfce436450b7b1b54ee23460f936dbfdbd7eabd9e781a4c01</code>.

Declarations: <code>PersonCommandHandler : ICommandHandler&lt;CreatePersonCommand, Guid&gt;, ICommandHandler&lt;UpdatePersonCommand, bool&gt;, ICommandHandler&lt;SaveSalaryAgreementCommand, Guid&gt;, ICommandHandler&lt;UpdatePersonWithAgreementCommand, bool&gt;</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (10)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-85430579a4af"></span><code>PersonCommandHandler.MonthRegexGenerated()</code><br>18–19 | — | No extracted literal effects. |
| <span id="m-deb43e4c3c67"></span><code>PersonCommandHandler.AddParam(DbCommand,string,object?)</code><br>21–27 | CreateParameter @23; Add @26 | No extracted literal effects. |
| <span id="m-25b195fac183"></span><code>PersonCommandHandler.HandleAsync(CreatePersonCommand,CommandEnvelope&lt;CreatePersonCommand&gt;,CancellationToken)</code><br>29–195 | ToString @37; Trim @39; IsNullOrWhiteSpace @40; Failure(Guid) @42; ToLowerInvariant @45; IsNullOrEmpty @62; IsMatch @62; CreateCommand @69; AddParam @72; ToString @72; ConfigureAwait @73; ExecuteScalarAsync @73; ExecuteScalarAsync @83; ToUpperInvariant @90; GenerateUniquePersonCodeAsync @93; ExecuteScalarAsync @101; NewGuid @108; ToString @123; ToString @127; ToString @128; ToString @132; ExecuteNonQueryAsync @135; GetStoreDefaultCurrencyAndScaleAsync @166; ToString @182; ExecuteNonQueryAsync @191; Success(Guid) @194 | FROM person_records @81; FROM person_records @99; FROM users @71; INSERT INTO person_records @113; INSERT INTO salary_agreements @174 · INVALID_DISPLAY_NAME @42; INVALID_PERSON_KIND @48; INVALID_EMPLOYMENT_DATES @53; INVALID_EMPLOYMENT_DATES @58; INVALID_PAYROLL_MONTH @64; USER_NOT_FOUND @76; USER_ALREADY_LINKED @86; PERSON_CODE_ALREADY_EXISTS @104; INVALID_SALARY_AMOUNT @144; INVALID_SALARY_AMOUNT @149; INVALID_PAYROLL_MONTH @155; INVALID_DECIMAL_PLACES @160 |
| <span id="m-5e1f3b91faaa"></span><code>PersonCommandHandler.HandleAsync(UpdatePersonCommand,CommandEnvelope&lt;UpdatePersonCommand&gt;,CancellationToken)</code><br>197–325 | ToString @205; Trim @207; IsNullOrWhiteSpace @208; Failure(bool) @210; ToLowerInvariant @213; IsNullOrEmpty @230; IsMatch @230; CreateCommand @238; AddParam @242; ToString @242; ConfigureAwait @243; ExecuteReaderAsync @243; ReadAsync @244; GetInt32 @248; IsDBNull @249; GetString @249; TryParse @257; ToString @262; ExecuteScalarAsync @263; ExecuteScalarAsync @274; CheckTrackingStartAllowedAsync @281; ToString @306; ToString @307; ToString @311; ExecuteNonQueryAsync @315; ValidateAsync @322; Success(bool) @324 | FROM person_records @241; FROM person_records @271; FROM users @261; UPDATE person_records @290 · INVALID_DISPLAY_NAME @210; INVALID_PERSON_KIND @216; INVALID_EMPLOYMENT_DATES @221; INVALID_EMPLOYMENT_DATES @226; INVALID_PAYROLL_MONTH @232; PERSON_NOT_FOUND @246; STALE_REVISION @254; USER_NOT_FOUND @266; USER_ALREADY_LINKED @277; TRACKING_START_EXCLUDES_EXISTING_PAYROLL @284; STALE_REVISION @318; INVALID_SALARY_DRAFT @323 |
| <span id="m-575cc713e4b8"></span><code>PersonCommandHandler.HandleAsync(SaveSalaryAgreementCommand,CommandEnvelope&lt;SaveSalaryAgreementCommand&gt;,CancellationToken)</code><br>327–488 | ToString @335; Trim @337; IsMatch @338; Failure(Guid) @340; ToUpperInvariant @358; IsNullOrWhiteSpace @359; ConfigureAwait @361; GetStoreDefaultCurrencyAndScaleAsync @361; CreateCommand @369; AddParam @373; ToString @373; ExecuteReaderAsync @374; ReadAsync @375; GetInt32 @379; CheckCurrencyChangeAllowedAsync @394; ExecuteScalarAsync @409; TryParse @410; ToString @410; NewGuid @418; ToString @436; ToString @441; ExecuteNonQueryAsync @443; ExecuteNonQueryAsync @466; ExecuteNonQueryAsync @482; ValidateAsync @485; Success(Guid) @487 | FROM person_records @372; FROM salary_agreements @406; INSERT INTO salary_agreements @449; UPDATE person_records @473; UPDATE salary_agreements @426 · INVALID_PAYROLL_MONTH @340; INVALID_SALARY_AMOUNT @345; INVALID_SALARY_AMOUNT @350; INVALID_DECIMAL_PLACES @355; PERSON_NOT_FOUND @377; PERSON_DISABLED @385; STALE_REVISION @390; CURRENCY_CHANGE_NOT_PERMITTED @397; INVALID_SALARY_DRAFT @486 |
| <span id="m-9394fefd3660"></span><code>PersonCommandHandler.HandleAsync(UpdatePersonWithAgreementCommand,CommandEnvelope&lt;UpdatePersonWithAgreementCommand&gt;,CancellationToken)</code><br>490–742 | ToString @498; Trim @500; IsNullOrWhiteSpace @501; Failure(bool) @503; ToLowerInvariant @506; IsNullOrEmpty @523; IsMatch @523; CreateCommand @531; AddParam @535; ToString @535; ConfigureAwait @536; ExecuteReaderAsync @536; ReadAsync @537; GetInt32 @541; IsDBNull @542; GetString @542; TryParse @550; ToString @555; ExecuteScalarAsync @556; ExecuteScalarAsync @567; CheckTrackingStartAllowedAsync @574; ToUpperInvariant @613; GetStoreDefaultCurrencyAndScaleAsync @616; CheckCurrencyChangeAllowedAsync @624; ToString @651; ToString @652; ToString @656; ExecuteNonQueryAsync @660; ExecuteScalarAsync @678; ToString @679; NewGuid @687; ToString @705; ExecuteNonQueryAsync @712; ExecuteNonQueryAsync @735; ValidateAsync @739; Success(bool) @741 | FROM person_records @534; FROM person_records @564; FROM salary_agreements @675; FROM users @554; INSERT INTO salary_agreements @718; UPDATE person_records @635; UPDATE salary_agreements @695 · INVALID_DISPLAY_NAME @503; INVALID_PERSON_KIND @509; INVALID_EMPLOYMENT_DATES @514; INVALID_EMPLOYMENT_DATES @519; INVALID_PAYROLL_MONTH @525; PERSON_NOT_FOUND @539; STALE_REVISION @547; USER_NOT_FOUND @559; USER_ALREADY_LINKED @570; TRACKING_START_EXCLUDES_EXISTING_PAYROLL @577; PERSON_DISABLED @588; INVALID_PAYROLL_MONTH @594; INVALID_SALARY_AMOUNT @599; INVALID_SALARY_AMOUNT @604; INVALID_DECIMAL_PLACES @610; CURRENCY_CHANGE_NOT_PERMITTED @627; STALE_REVISION @663; INVALID_SALARY_DRAFT @740 |
| <span id="m-203137eda8d4"></span><code>PersonCommandHandler.CheckCurrencyChangeAllowedAsync(DbConnection,DbTransaction?,Guid,string,int,string,CancellationToken)</code><br>744–752 | CheckCurrencyChangeAllowedAsync @752 | No extracted literal effects. |
| <span id="m-68005f399ef0"></span><code>PersonCommandHandler.GenerateUniquePersonCodeAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>754–783 | CreateCommand @756; ConfigureAwait @760; ExecuteReaderAsync @760; ReadAsync @762; IsDBNull @764; Add @766; GetString @766; StartsWith @774; TryParse @775 | FROM person_records @758 |
| <span id="m-9cba60261b04"></span><code>PersonCommandHandler.GetStoreDefaultCurrencyAndScaleAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>785–799 | CreateCommand @788; ConfigureAwait @791; ExecuteReaderAsync @791; ReadAsync @792; IsDBNull @794; GetString @794; GetInt32 @795 | FROM store_config @790 |
| <span id="m-93dc82476f51"></span><code>PersonCommandHandler.CheckTrackingStartAllowedAsync(DbConnection,DbTransaction?,Guid,string?,CancellationToken)</code><br>801–807 | CheckTrackingStartAllowedAsync @807 | No extracted literal effects. |

</details>

## PersonCommands.cs {#src-4520c918be9b}

<code>Software/src/GetSeek.Application/Payroll/PersonCommands.cs</code> · 125 lines.

SHA-256: <code>836c8c58d11871b019e6a14bf4e234a7561587d17152fb3d802802a55698c290</code>.

Declarations: <code>CreatePersonCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 7), <code>UpdatePersonCommand : ICommand&lt;bool&gt;, ISanitizedAuditPayload</code> (line 39), <code>SaveSalaryAgreementCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 67), <code>UpdatePersonWithAgreementCommand : ICommand&lt;bool&gt;, ISanitizedAuditPayload</code> (line 90).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-367ecc58b518"></span><code>CreatePersonCommand.GetSanitizedAuditPayload()</code><br>25–36 | Serialize @25 | No extracted literal effects. |
| <span id="m-9bc44c13f6ca"></span><code>UpdatePersonCommand.GetSanitizedAuditPayload()</code><br>53–64 | Serialize @53 | No extracted literal effects. |
| <span id="m-f3c2470ff882"></span><code>SaveSalaryAgreementCommand.GetSanitizedAuditPayload()</code><br>79–87 | Serialize @79 | No extracted literal effects. |
| <span id="m-8a49d29597d6"></span><code>UpdatePersonWithAgreementCommand.GetSanitizedAuditPayload()</code><br>110–124 | Serialize @110 | No extracted literal effects. |

</details>

## SalaryBalanceFacts.cs {#src-ca4b21883f9d}

<code>Software/src/GetSeek.Application/Payroll/SalaryBalanceFacts.cs</code> · 36 lines.

SHA-256: <code>aa264ee1799a2c44086f2d90ba90f96c35998d6ebedea0be780187b792d9cb30</code>.

Declarations: <code>SalaryBalanceFacts</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-938ab0f357d9"></span><code>SalaryBalanceFacts.ReadAsync(DbConnection,DbTransaction?,Guid,string,string,int,DateTime?,CancellationToken)</code><br>9–35 | CreateCommand @12; ToString @24; ToString @25; CreateParameter @27; Add @30; ConfigureAwait @32; ExecuteReaderAsync @32; ReadAsync @33; GetInt64 @34 | FROM salary_ledger_entries @14 |

</details>

## SalaryDraftValidator.cs {#src-21ae39535173}

<code>Software/src/GetSeek.Application/Payroll/SalaryDraftValidator.cs</code> · 68 lines.

SHA-256: <code>77c6b689e1caff1fdefe3e4d9d72500d940ba4b5ca2e9822042dd1a1bea594e7</code>.

Declarations: <code>SalaryDraftValidator</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5e3188007744"></span><code>SalaryDraftValidator.ValidateAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>10–56 | Create @14; ConfigureAwait @19; ExecuteReaderAsync @19; ReadAsync @20; Add @20; GetString @20; ReadAsync @33; IsDBNull @34; GetString @34; IsNullOrEmpty @35; CompareOrdinal @35; GetInt64 @36; CalculateProration @40; Parse @40; ParseExact @42; GetInt32 @44 | FROM person_records @24; FROM salary_adjustments @14; FROM salary_adjustments @24; FROM salary_agreements @24; FROM salary_periods @14; FROM salary_periods @24 |
| <span id="m-f73d07c5d893"></span><code>SalaryDraftValidator.Create(DbConnection,DbTransaction?,Guid,string?,string)</code><br>58–67 | CreateCommand @60; CreateParameter @61; ToString @61; Add @61 | No extracted literal effects. |

</details>

## SalaryPaymentCommandHandler.cs {#src-c26df3332168}

<code>Software/src/GetSeek.Application/Payroll/SalaryPaymentCommandHandler.cs</code> · 806 lines.

SHA-256: <code>8d8b14e58041325dae5fbe3a1cdc4cc49e502bd1bbf31c9100f517d542e3fd40</code>.

Declarations: <code>SalaryPaymentCommandHandler : ICommandHandler&lt;PayAdvanceCommand, Guid&gt;, ICommandHandler&lt;PaySalaryCommand, Guid&gt;, ICommandHandler&lt;ReverseSalaryPaymentCommand, Guid&gt;</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-aa8322662c52"></span><code>SalaryPaymentCommandHandler.AddParam(DbCommand,string,object?)</code><br>17–23 | CreateParameter @19; Add @22 | No extracted literal effects. |
| <span id="m-b97b339d7e38"></span><code>SalaryPaymentCommandHandler.HandleAsync(PayAdvanceCommand,CommandEnvelope&lt;PayAdvanceCommand&gt;,CancellationToken)</code><br>25–271 | ToString @33; Failure(Guid) @37; Trim @50; IsNullOrWhiteSpace @51; CreateCommand @60; AddParam @64; ToString @64; ConfigureAwait @65; ExecuteReaderAsync @65; ReadAsync @66; GetInt32 @70; ToString @90; ExecuteReaderAsync @91; GetString @96; NewGuid @110; ToString @112; GetStoreTimeZoneAsync @113; GetStoreLocalMonth @114; ExecuteReaderAsync @130; ReadAsync @131; GetString @133; GetInt32 @134; CloseAsync @138; ExecuteReaderAsync @143; ReadAsync @144; GetString @146; GetInt32 @147; CloseAsync @151; ExecuteReaderAsync @157; ReadAsync @158; GetString @160; GetInt32 @161; Equals @173; PostAsync @191; ToString @215; ToString @220; Trim @222; ToString @224; ToString @225; ExecuteNonQueryAsync @228; ToString @245; ExecuteNonQueryAsync @257; ExecuteNonQueryAsync @267; Success(Guid) @270 | FROM money_accounts @89; FROM person_records @63; FROM salary_agreements @122; FROM salary_agreements @141; FROM salary_ledger_entries @155; INSERT INTO salary_ledger_entries @235; INSERT INTO salary_payments @205; UPDATE person_records @264 · INVALID_PERSON_ID @37; INVALID_ACCOUNT_ID @42; INVALID_AMOUNT @47; REASON_REQUIRED @53; PERSON_NOT_FOUND @68; PERSON_DISABLED @74; STALE_REVISION @80; ACCOUNT_NOT_FOUND @94; ACCOUNT_NOT_FOUND @101; PAID_AT_OVERRIDE_NOT_PERMITTED @107; CURRENCY_MISMATCH @175 |
| <span id="m-4969cfdaa69b"></span><code>SalaryPaymentCommandHandler.HandleAsync(PaySalaryCommand,CommandEnvelope&lt;PaySalaryCommand&gt;,CancellationToken)</code><br>273–534 | ToString @281; Failure(Guid) @285; Trim @298; IsNullOrWhiteSpace @299; CreateCommand @308; AddParam @312; ToString @312; ConfigureAwait @313; ExecuteReaderAsync @313; ReadAsync @314; GetInt32 @318; ToString @333; ExecuteReaderAsync @334; GetString @339; NewGuid @353; ToString @355; GetStoreTimeZoneAsync @356; GetStoreLocalMonth @357; ExecuteReaderAsync @373; ReadAsync @374; GetString @376; GetInt32 @377; CloseAsync @381; ExecuteReaderAsync @386; ReadAsync @387; GetString @389; GetInt32 @390; CloseAsync @394; ExecuteReaderAsync @400; ReadAsync @401; GetString @403; GetInt32 @404; Equals @414; ExecuteScalarAsync @431; Max @438; PostAsync @454; ToString @478; ToString @483; Trim @485; ToString @487; ToString @488; ExecuteNonQueryAsync @491; ToString @508; ExecuteNonQueryAsync @520; ExecuteNonQueryAsync @530; Success(Guid) @533 | FROM money_accounts @332; FROM person_records @311; FROM salary_agreements @365; FROM salary_agreements @384; FROM salary_ledger_entries @398; FROM salary_ledger_entries @424; INSERT INTO salary_ledger_entries @498; INSERT INTO salary_payments @468; UPDATE person_records @527 · INVALID_PERSON_ID @285; INVALID_ACCOUNT_ID @290; INVALID_AMOUNT @295; REASON_REQUIRED @301; PERSON_NOT_FOUND @316; STALE_REVISION @323; ACCOUNT_NOT_FOUND @337; ACCOUNT_NOT_FOUND @344; PAID_AT_OVERRIDE_NOT_PERMITTED @350; NO_SALARY_AGREEMENT @408; CURRENCY_MISMATCH @416; SALARY_FINALIZED_BALANCE_INSUFFICIENT @436 |
| <span id="m-8b736e7638f4"></span><code>SalaryPaymentCommandHandler.HandleAsync(ReverseSalaryPaymentCommand,CommandEnvelope&lt;ReverseSalaryPaymentCommand&gt;,CancellationToken)</code><br>536–789 | ToString @544; Trim @546; IsNullOrWhiteSpace @547; Failure(Guid) @549; CreateCommand @563; AddParam @570; ToString @570; ConfigureAwait @571; ExecuteReaderAsync @571; ReadAsync @572; Parse @577; GetString @577; GetInt64 @579; IsDBNull @580; Equals @591; ExecuteScalarAsync @602; ToString @615; ExecuteScalarAsync @616; ToInt32 @621; GetStoreDefaultCurrencyAndScaleAsync @631; ToString @642; ExecuteReaderAsync @643; GetInt32 @650; Trim @679; PostAsync @686; ExecuteReaderAsync @704; ReadAsync @705; GetString @707; GetInt32 @709; NewGuid @713; GetStoreTimeZoneAsync @714; GetStoreLocalMonth @715; ToString @731; ToString @736; ToString @740; ToString @741; ExecuteNonQueryAsync @745; ToString @762; ToString @773; ExecuteNonQueryAsync @775; ExecuteNonQueryAsync @785; Success(Guid) @788 | FROM money_accounts @641; FROM person_records @614; FROM salary_ledger_entries @702; FROM salary_payments @566; FROM salary_payments @600; INSERT INTO salary_ledger_entries @752; INSERT INTO salary_payments @721; UPDATE person_records @782 · REASON_REQUIRED @549; PAYMENT_NOT_FOUND @574; PERSON_MISMATCH @588; CANNOT_REVERSE_A_REVERSAL @593; PAYMENT_ALREADY_REVERSED @605; PERSON_NOT_FOUND @619; STALE_REVISION @626; ACCOUNT_NOT_FOUND @646; ACCOUNT_NOT_FOUND @654; BANK_CONFIRMATION_REQUIRED @662; SHIFT_NOT_OPEN @669 |
| <span id="m-54686ddbdee6"></span><code>SalaryPaymentCommandHandler.GetStoreDefaultCurrencyAndScaleAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>791–805 | CreateCommand @794; ConfigureAwait @797; ExecuteReaderAsync @797; ReadAsync @798; IsDBNull @800; GetString @800; GetInt32 @801 | FROM store_config @796 |

</details>

## SalaryPaymentCommands.cs {#src-b35b5fef12bc}

<code>Software/src/GetSeek.Application/Payroll/SalaryPaymentCommands.cs</code> · 80 lines.

SHA-256: <code>92563761fee82a305887e20acee5909b18ae8a42f25147680dd43421fb4e1fb8</code>.

Declarations: <code>PayAdvanceCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 7), <code>PaySalaryCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 33), <code>ReverseSalaryPaymentCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 59).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ccddacf261df"></span><code>PayAdvanceCommand.GetSanitizedAuditPayload()</code><br>22–30 | Serialize @22; IsNullOrWhiteSpace @29 | No extracted literal effects. |
| <span id="m-9efc5455115f"></span><code>PaySalaryCommand.GetSanitizedAuditPayload()</code><br>48–56 | Serialize @48; IsNullOrWhiteSpace @55 | No extracted literal effects. |
| <span id="m-330208c6ad4f"></span><code>ReverseSalaryPaymentCommand.GetSanitizedAuditPayload()</code><br>72–79 | Serialize @72; IsNullOrWhiteSpace @78 | No extracted literal effects. |

</details>

## SalaryPeriodCommandHandler.cs {#src-4b1c23ddb697}

<code>Software/src/GetSeek.Application/Payroll/SalaryPeriodCommandHandler.cs</code> · 1,009 lines.

SHA-256: <code>165ee29f1148d4d1e1e6ecb6d82eda4c58f87d0b16df65c5d1c480c7d17c6b18</code>.

Declarations: <code>SalaryPeriodCommandHandler : ICommandHandler&lt;RecordSalaryAdjustmentCommand, Guid&gt;, ICommandHandler&lt;RecordUnpaidDaysCommand, bool&gt;, ICommandHandler&lt;FinalizeSalaryPeriodCommand, Guid&gt;, ICommandHandler&lt;RecordSalaryOpeningBalanceCommand, Guid&gt;, ICommandHandler&lt;RecordSalaryCorrectionCommand, Guid&gt;</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (8)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4218a074c727"></span><code>SalaryPeriodCommandHandler.MonthRegexGenerated()</code><br>20–21 | — | No extracted literal effects. |
| <span id="m-4800dc539ff5"></span><code>SalaryPeriodCommandHandler.AddParam(DbCommand,string,object?)</code><br>23–29 | CreateParameter @25; Add @28 | No extracted literal effects. |
| <span id="m-e95dba3f35b5"></span><code>SalaryPeriodCommandHandler.HandleAsync(RecordSalaryAdjustmentCommand,CommandEnvelope&lt;RecordSalaryAdjustmentCommand&gt;,CancellationToken)</code><br>31–142 | ToString @39; Trim @41; IsMatch @42; Failure(Guid) @44; ToLowerInvariant @47; IsNullOrWhiteSpace @59; CreateCommand @66; AddParam @70; ToString @70; ConfigureAwait @71; ExecuteScalarAsync @71; ToInt32 @76; ExecuteScalarAsync @91; Equals @92; ToString @92; NewGuid @98; ToString @110; ToString @115; ToString @117; ExecuteNonQueryAsync @120; ExecuteNonQueryAsync @136; ValidateAsync @139; Success(Guid) @141 | FROM person_records @69; FROM salary_periods @88; INSERT INTO salary_adjustments @102; UPDATE person_records @127 · INVALID_PAYROLL_MONTH @44; INVALID_ADJUSTMENT_KIND @50; INVALID_ADJUSTMENT_AMOUNT @55; REASON_REQUIRED @61; PERSON_NOT_FOUND @74; STALE_REVISION @81; PERIOD_ALREADY_FINALIZED @94; INVALID_SALARY_DRAFT @140 |
| <span id="m-19db365247cb"></span><code>SalaryPeriodCommandHandler.HandleAsync(RecordUnpaidDaysCommand,CommandEnvelope&lt;RecordUnpaidDaysCommand&gt;,CancellationToken)</code><br>144–266 | ToString @152; Trim @154; IsMatch @155; Failure(bool) @157; CreateCommand @169; AddParam @173; ToString @173; ConfigureAwait @174; ExecuteReaderAsync @174; ReadAsync @175; GetInt32 @179; ParseExact @180; GetString @180; IsDBNull @181; ExecuteScalarAsync @196; Equals @197; ToString @197; Parse @203; DaysInMonth @205; ToString @238; NewGuid @238; IsNullOrWhiteSpace @242; Trim @242; ExecuteNonQueryAsync @244; ToString @259; ExecuteNonQueryAsync @260; ValidateAsync @263; Success(bool) @265 | FROM person_records @172; FROM salary_periods @193; INSERT INTO salary_periods @229; UPDATE person_records @251 · INVALID_PAYROLL_MONTH @157; INVALID_UNPAID_DAYS @162; PERSON_NOT_FOUND @177; STALE_REVISION @186; PERIOD_ALREADY_FINALIZED @199; INVALID_UNPAID_DAYS @222; INVALID_SALARY_DRAFT @264 |
| <span id="m-c2090465ef7c"></span><code>SalaryPeriodCommandHandler.HandleAsync(FinalizeSalaryPeriodCommand,CommandEnvelope&lt;FinalizeSalaryPeriodCommand&gt;,CancellationToken)</code><br>268–734 | ToString @276; Trim @278; IsMatch @279; Failure(Guid) @281; CreateCommand @290; AddParam @294; ToString @294; ConfigureAwait @295; ExecuteReaderAsync @295; ReadAsync @296; GetInt32 @300; ParseExact @301; GetString @301; IsDBNull @302; ExecuteReaderAsync @315; ReadAsync @316; GetString @318; Equals @319; Success(Guid) @322; Parse @322; Parse @332; DaysInMonth @334; IsNullOrEmpty @339; CompareOrdinal @339; GetStoreTimeZoneAsync @345; GetStoreLocalDate @346; ToString @366; ExecuteScalarAsync @379; ToString @380; AddMonths @385; ExecuteReaderAsync @404; ReadAsync @405; GetInt32 @409; GetInt64 @410; IsDBNull @411; GetString @412; ExecuteReaderAsync @425; ReadAsync @426; GetInt32 @428; IsDBNull @429; GetString @429; ExecuteReaderAsync @446; ReadAsync @447; GetString @449; GetInt64 @451; Parse @452; Add @455; ExecuteReaderAsync @476; ReadAsync @479; GetString @481; GetInt64 @483; IsDBNull @485; GetInt32 @492; Add @494; Add @495; GetStoreLocalMonth @499; Add @502; Contains @503; ReadAsync @515; ExecuteReaderAsync @536; ReadAsync @537; GetString @539; GetInt64 @542; GetInt32 @544; IsDBNull @546; Add @548; CalculateProration @553; CalculateRemainingBalance @562; Max @564; Serialize @567; NewGuid @569; Round @593; ToString @653; ToString @660; ExecuteNonQueryAsync @670; ExecuteScalarAsync @680; TryParse @681; ToString @681; ToString @702; ExecuteNonQueryAsync @714; ExecuteNonQueryAsync @730 | FROM person_records @293; FROM salary_adjustments @440; FROM salary_agreements @396; FROM salary_ledger_entries @524; FROM salary_payments @468; FROM salary_periods @312; FROM salary_periods @376; FROM salary_periods @422; FROM salary_periods @677; INSERT INTO salary_periods @619; INSERT OR IGNORE INTO salary_ledger_entries @692; JOIN salary_ledger_entries @468; UPDATE person_records @721 · INVALID_PAYROLL_MONTH @281; PERSON_NOT_FOUND @298; STALE_REVISION @329; SALARY_PERIOD_BEFORE_TRACKING @341; SALARY_PERIOD_NOT_ENDED @350; SALARY_PREVIOUS_PERIOD_OPEN @382; NO_SALARY_AGREEMENT @407 |
| <span id="m-b2b08a84d6b9"></span><code>SalaryPeriodCommandHandler.HandleAsync(RecordSalaryOpeningBalanceCommand,CommandEnvelope&lt;RecordSalaryOpeningBalanceCommand&gt;,CancellationToken)</code><br>736–855 | ToString @744; Failure(Guid) @748; Trim @751; IsNullOrWhiteSpace @752; IsMatch @758; ToUpperInvariant @768; ConfigureAwait @771; GetStoreDefaultCurrencyAndScaleAsync @771; CreateCommand @778; AddParam @782; ToString @782; ExecuteScalarAsync @783; ToInt32 @788; ExecuteScalarAsync @802; NewGuid @809; ToString @823; ToString @833; ExecuteNonQueryAsync @835; ExecuteNonQueryAsync @851; Success(Guid) @854 | FROM person_records @781; FROM salary_ledger_entries @800; INSERT INTO salary_ledger_entries @813; UPDATE person_records @842 · INVALID_AMOUNT @748; REASON_REQUIRED @754; INVALID_PAYROLL_MONTH @760; INVALID_DECIMAL_PLACES @765; PERSON_NOT_FOUND @786; STALE_REVISION @793; OPENING_BALANCE_ALREADY_EXISTS @805 |
| <span id="m-7e448db67b04"></span><code>SalaryPeriodCommandHandler.HandleAsync(RecordSalaryCorrectionCommand,CommandEnvelope&lt;RecordSalaryCorrectionCommand&gt;,CancellationToken)</code><br>857–992 | ToString @865; ToLowerInvariant @867; Trim @867; Failure(Guid) @870; IsNullOrWhiteSpace @879; IsMatch @885; CreateCommand @892; AddParam @896; ToString @896; ConfigureAwait @897; ExecuteScalarAsync @897; ToInt32 @902; ExecuteReaderAsync @918; ReadAsync @919; GetString @921; GetInt32 @922; CloseAsync @926; ExecuteReaderAsync @931; ReadAsync @932; GetString @934; GetInt32 @935; GetStoreDefaultCurrencyAndScaleAsync @939; NewGuid @946; ToString @960; ToString @970; ExecuteNonQueryAsync @972; ExecuteNonQueryAsync @988; Success(Guid) @991 | FROM person_records @895; FROM salary_agreements @916; FROM salary_ledger_entries @929; INSERT INTO salary_ledger_entries @950; UPDATE person_records @979 · INVALID_CORRECTION_TYPE @870; INVALID_AMOUNT @875; REASON_REQUIRED @881; INVALID_PAYROLL_MONTH @887; PERSON_NOT_FOUND @900; STALE_REVISION @907 |
| <span id="m-b1e2c70a7d51"></span><code>SalaryPeriodCommandHandler.GetStoreDefaultCurrencyAndScaleAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>994–1008 | CreateCommand @997; ConfigureAwait @1000; ExecuteReaderAsync @1000; ReadAsync @1001; IsDBNull @1003; GetString @1003; GetInt32 @1004 | FROM store_config @999 |

</details>

## SalaryPeriodCommands.cs {#src-8ce44973b846}

<code>Software/src/GetSeek.Application/Payroll/SalaryPeriodCommands.cs</code> · 104 lines.

SHA-256: <code>aac345b4fed8fc1c4a0d2d4341aac6fc60b34c6c3959dc1c607785cae6cd059a</code>.

Declarations: <code>RecordSalaryAdjustmentCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 7), <code>RecordUnpaidDaysCommand : ICommand&lt;bool&gt;, ISanitizedAuditPayload</code> (line 29), <code>FinalizeSalaryPeriodCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 48), <code>RecordSalaryOpeningBalanceCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 64), <code>RecordSalaryCorrectionCommand : ICommand&lt;Guid&gt;, ISanitizedAuditPayload</code> (line 86).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-762948cf5f6a"></span><code>RecordSalaryAdjustmentCommand.GetSanitizedAuditPayload()</code><br>19–26 | Serialize @19 | No extracted literal effects. |
| <span id="m-8b3ed6d5e43e"></span><code>RecordUnpaidDaysCommand.GetSanitizedAuditPayload()</code><br>39–45 | Serialize @39 | No extracted literal effects. |
| <span id="m-5325d0f631ee"></span><code>FinalizeSalaryPeriodCommand.GetSanitizedAuditPayload()</code><br>56–61 | Serialize @56 | No extracted literal effects. |
| <span id="m-bc764f3a4bf6"></span><code>RecordSalaryOpeningBalanceCommand.GetSanitizedAuditPayload()</code><br>76–83 | Serialize @76 | No extracted literal effects. |
| <span id="m-901aa0f90640"></span><code>RecordSalaryCorrectionCommand.GetSanitizedAuditPayload()</code><br>97–103 | Serialize @97 | No extracted literal effects. |

</details>

## CommandPipeline.cs {#src-b29270acda74}

<code>Software/src/GetSeek.Application/Pipeline/CommandPipeline.cs</code> · 296 lines.

SHA-256: <code>a21a8c9176e916f7ed7bde36439a87e18604a6fcc0423463d1d5b3e0dffabfaa</code>.

Declarations: <code>ICommandHandler</code> (line 10), <code>CommandPipeline : IDisposable</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5b79cf26590f"></span><code>ICommandHandler.HandleAsync(TCommand,CommandEnvelope&lt;TCommand&gt;,CancellationToken)</code><br>12–12 | — | No extracted literal effects. |
| <span id="m-bc4a7c68e225"></span><code>CommandPipeline.ExecuteAsync(TCommand,ICommandHandler&lt;TCommand, TResult&gt;,string?,string?,Guid?,CancellationToken)</code><br>27–289 | Failure(TResult) @38; ConfigureAwait @51; WaitAsync @51; IsNullOrWhiteSpace @78; Equals @80; Trim @80; Trim @80; ToString @96; NewGuid @96; GetAllRequiredPermissions @110; HasPermissionAsync @114; HasPermission @115; IsNullOrEmpty @124; IsModuleLicensed @124; CheckClockTamperAsync @130; Serialize @137; ToHexStringLower @138; HashData @138; GetBytes @138; CheckAsync @141; Deserialize(TResult) @151; Success(TResult) @153; BeginTransactionAsync @158; RollbackAsync @165; HandleAsync @199; GetSanitizedAuditPayload @208; AppendAsync @211; ToString @212; SaveAsync @223; CommitAsync @226; LogFailure @250; DisposeAsync @281; Release @287 | SESSION_LOCKED @38; AUTH_UNAUTHORIZED @45; OPERATION_CANCELLED @55; SESSION_LOCKED @66; AUTH_UNAUTHORIZED @71; IDEMPOTENCY_CONFLICT @82; AUTH_UNAUTHORIZED @119; LICENSE_EXPIRED @126; SECURITY_CLOCK_TAMPER @133; IDEMPOTENCY_CONFLICT @146; IDEMPOTENCY_CONFLICT @167; IDEMPOTENCY_RESULT_UNAVAILABLE @170; AUTH_UNAUTHORIZED @182; AUTH_UNAUTHORIZED @193; OPERATION_CANCELLED @243; SYSTEM_TRANSACTION_ERROR @272 |
| <span id="m-175447f85e5d"></span><code>CommandPipeline.Dispose()</code><br>291–295 | Dispose @293; SuppressFinalize @294 | No extracted literal effects. |

</details>

## ApplyBatchPricingCommandHandler.cs {#src-b18b22aba44c}

<code>Software/src/GetSeek.Application/Pricing/ApplyBatchPricingCommandHandler.cs</code> · 209 lines.

SHA-256: <code>f541fdb989bcf53a04f3efe2367031ff1e147f401eef9862dc932992dd09c295</code>.

Declarations: <code>ApplyBatchPricingCommandHandler : ICommandHandler&lt;ApplyBatchPricingCommand, BatchPricingResult&gt;</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-1993964377ca"></span><code>ApplyBatchPricingCommandHandler.HandleAsync(ApplyBatchPricingCommand,CommandEnvelope&lt;ApplyBatchPricingCommand&gt;,CancellationToken)</code><br>12–203 | ToString @19; OperationParametersJson @22; ConfigureAwait @24; ValidateAsync @24; Failure(BatchPricingResult) @28; CalculateAsync @30; CreateCommand @35; ExecuteScalarAsync @39; ToInt32 @41; ParseRoundingRule @44; TryConvertRoundingIncrement @46; SequenceEqual @53; Equals @55; NewGuid @58; Add @68; Add @76; Equals @93; ToUpperInvariant @94; Add @100; ToLowerInvariant @101; Trim @101; ToString @102; Trim @103; ExecuteNonQueryAsync @111; ExecuteNonQueryAsync @120; RecordAsync @125; Parse @126; ToString @129; ToString @130; Trim @144; Trim @145; ToString @152; ToString @156; ExecuteNonQueryAsync @158; ToString @168; ExecuteNonQueryAsync @178; ExecuteNonQueryAsync @196; ConsumeAsync @199; Success(BatchPricingResult) @201 | FROM store_config @38; INSERT INTO item_pricing @84; INSERT INTO pricing_batch_items @165; INSERT INTO pricing_batch_proposals @185; INSERT INTO pricing_batches @139; UPDATE items @117 · INVALID_ROUNDING_INCREMENT @48; BATCH_SELECTION_STALE @54; PRICING_PREVIEW_STALE @56; BATCH_SELECTION_STALE @121 |
| <span id="m-6e9a7663107c"></span><code>ApplyBatchPricingCommandHandler.Add(DbCommand,string,object)</code><br>205–208 | CreateParameter @207; Add @207 | No extracted literal effects. |

</details>

## BatchPricingPreviewCalculator.cs {#src-61172a3202c7}

<code>Software/src/GetSeek.Application/Pricing/BatchPricingPreviewCalculator.cs</code> · 181 lines.

SHA-256: <code>7605cc7d53137ab2312e29b9d74dde153e38c886bd5f591b0353cc2943713efe</code>.

Declarations: <code>BatchPricingCandidate</code> (line 10), <code>BatchPricingDecision</code> (line 14), <code>BatchPricingCalculation</code> (line 18), <code>BatchPricingPreviewCalculator</code> (line 24).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-53a58d09a3c2"></span><code>BatchPricingPreviewCalculator.CalculateAsync(DbConnection,DbTransaction?,BatchPricingOptions,CancellationToken,IReadOnlyList&lt;string&gt;?)</code><br>28–180 | ToLowerInvariant @32; Trim @32; Trim @33; Trim @34; Trim @35; CreateCommand @53; ConfigureAwait @57; ExecuteReaderAsync @57; ReadAsync @58; GetInt32 @60; Join @61; GetString @61; ToString @61; ToString @61; GetValue @61; ParseRoundingRule @66; IsRoundingRuleCompatible @67; TryConvertRoundingIncrement @71; Add @84; Select @84; Range @84; ToArray @94; OrderBy @94; Distinct @94; Where @94; IsNullOrWhiteSpace @94; Trim @94; ToString @101; Add @102; Add @103; Add @121; GetInt64 @122; SequenceEqual @126; Select @126; ParsePricingMethod @131; Add @152; ResolveEffectiveBasePrice @157; ToString @164; OperationParametersJson @165; AddRange @167; OrderBy @168; Add @169; ToString @169; ToString @170; ToString @170; ToString @171; HashFields @172; ToArray @172; Count @173; Take @176 | FROM price_level_settings @81; FROM store_config @56 · DYNAMIC SQL: inspect manually |

</details>

## CategoryPricingRuleCommandHandler.cs {#src-4883c67861e2}

<code>Software/src/GetSeek.Application/Pricing/CategoryPricingRuleCommandHandler.cs</code> · 334 lines.

SHA-256: <code>495e35dee22116e1265d1e22a735a1287b383d5a7b6748774b7a5836661245bd</code>.

Declarations: <code>CategoryPricingRuleCommandHandler : ICommandHandler&lt;SaveCategoryPricingRuleCommand, CategoryPricingRuleSaveResult&gt;, ICommandHandler&lt;DeactivateCategoryPricingRuleCommand, bool&gt;</code> (line 14), <code>AffectedItem</code> (line 285).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3d5f70979b42"></span><code>CategoryPricingRuleCommandHandler.HandleAsync(SaveCategoryPricingRuleCommand,CommandEnvelope&lt;SaveCategoryPricingRuleCommand&gt;,CancellationToken)</code><br>25–198 | ConfigureAwait @32; IsActiveAdminAsync @32; Failure(CategoryPricingRuleSaveResult) @34; ToLowerInvariant @37; Trim @37; Contains @48; ReadDecimalPlacesAsync @62; ParseRoundingRule @63; IsRoundingRuleCompatible @64; TryConvertRoundingIncrement @71; IsActiveInventoryCategoryAsync @77; NextRuleVersionAsync @82; NewGuid @83; ToString @84; CreateCommand @86; AddParam @96; ToString @97; ToString @98; ExecuteNonQueryAsync @99; ExecuteNonQueryAsync @107; ToString @118; ToString @123; ToString @127; ExecuteNonQueryAsync @132; ReadAffectedItemsAsync @135; CalculateAsync @143; ReadItemCostAsync @154; ParsePricingMethod @166; ResolveEffectiveBasePrice @172; CreateAsync @184; Success(CategoryPricingRuleSaveResult) @196 | FROM items @89; INSERT INTO product_category_pricing_rules @113; UPDATE price_change_proposals @89; UPDATE product_category_pricing_rules @105 · ADMIN_REQUIRED @34; INVALID_COST_BASIS_SOURCE @42; INVALID_PRICING_METHOD @46; INVALID_ROUNDING_RULE @50; INVALID_PRICING_PARAMETER @55; INVALID_MARGIN_CEILING @59; ROUNDING_PRECISION_UNSUPPORTED @66; INVALID_ROUNDING_INCREMENT @73; CATEGORY_NOT_ELIGIBLE @79; PRICING_CALCULATION_OVERFLOW @176 |
| <span id="m-a6e3a0a26ffa"></span><code>CategoryPricingRuleCommandHandler.HandleAsync(DeactivateCategoryPricingRuleCommand,CommandEnvelope&lt;DeactivateCategoryPricingRuleCommand&gt;,CancellationToken)</code><br>200–243 | ConfigureAwait @207; IsActiveAdminAsync @207; Failure(bool) @209; IsActiveInventoryCategoryAsync @211; ToString @216; CreateCommand @217; AddParam @221; ToString @221; ExecuteNonQueryAsync @222; ToString @237; ExecuteNonQueryAsync @239; Success(bool) @242 | FROM product_category_pricing_rules @231; UPDATE price_change_proposals @231; UPDATE product_category_pricing_rules @220 · ADMIN_REQUIRED @209; CATEGORY_NOT_ELIGIBLE @213; CATEGORY_PRICING_RULE_NOT_FOUND @224 |
| <span id="m-115dbdc2a6ff"></span><code>CategoryPricingRuleCommandHandler.IsActiveAdminAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>245–255 | CreateCommand @247; AddParam @253; ToString @253; ToInt64 @254; ConfigureAwait @254; ExecuteScalarAsync @254 | FROM users @249; JOIN roles @249; JOIN user_roles @249 |
| <span id="m-7b7d2b093986"></span><code>CategoryPricingRuleCommandHandler.IsActiveInventoryCategoryAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>257–264 | CreateCommand @259; AddParam @262; ToString @262; ToInt64 @263; ConfigureAwait @263; ExecuteScalarAsync @263 | FROM product_categories @261 |
| <span id="m-55d2f609188e"></span><code>CategoryPricingRuleCommandHandler.ReadDecimalPlacesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>266–274 | CreateCommand @268; ConfigureAwait @271; ExecuteScalarAsync @271; ToInt32 @272 | FROM store_config @270 |
| <span id="m-1ce8062013f9"></span><code>CategoryPricingRuleCommandHandler.NextRuleVersionAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>276–283 | CreateCommand @278; AddParam @281; ToString @281; ToInt32 @282; ConfigureAwait @282; ExecuteScalarAsync @282 | FROM product_category_pricing_rules @280 |
| <span id="m-185eaa758002"></span><code>CategoryPricingRuleCommandHandler.ReadAffectedItemsAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>287–304 | CreateCommand @290; AddParam @299; ToString @299; ConfigureAwait @300; ExecuteReaderAsync @300; ReadAsync @301; Add @302; Parse @302; GetString @302; GetInt64 @302; GetInt32 @302 | FROM item_kits @292; FROM items @292; JOIN item_pricing @292 |
| <span id="m-f035bbb12640"></span><code>CategoryPricingRuleCommandHandler.ReadItemCostAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>306–325 | CreateCommand @308; AddParam @311; ToString @311; ConfigureAwait @312; ExecuteReaderAsync @312; ReadAsync @313; GetInt64 @314; IsDBNull @317 | FROM items @310 |
| <span id="m-d8c109831da3"></span><code>CategoryPricingRuleCommandHandler.AddParam(DbCommand,string,object)</code><br>327–333 | CreateParameter @329; Add @332 | No extracted literal effects. |

</details>

## CategoryPricingRuleCommands.cs {#src-2f398be5fc10}

<code>Software/src/GetSeek.Application/Pricing/CategoryPricingRuleCommands.cs</code> · 44 lines.

SHA-256: <code>e8b7c1b3002e42884ebb0e3c7abe93ca7383407305c6fdda765bcfe44bd00fb3</code>.

Declarations: <code>SaveCategoryPricingRuleCommand : ICommand&lt;CategoryPricingRuleSaveResult&gt;</code> (line 6), <code>DeactivateCategoryPricingRuleCommand : ICommand&lt;bool&gt;</code> (line 19), <code>CategoryPricingRuleSaveResult</code> (line 24), <code>CategoryPricingRuleSummary</code> (line 32).

## ItemPriceHistoryRecorder.cs {#src-2c26209c7f4c}

<code>Software/src/GetSeek.Application/Pricing/ItemPriceHistoryRecorder.cs</code> · 95 lines.

SHA-256: <code>2f10ff7ccb3363b0e2114d5fd10f4038aa819141ebaa0af9995a86558b54f516</code>.

Declarations: <code>ItemPriceHistoryRecorder</code> (line 8), <code>Entry</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-33cfb57d5708"></span><code>ItemPriceHistoryRecorder.RecordAsync(DbConnection,DbTransaction?,Entry,CancellationToken)</code><br>32–85 | CreateCommand @37; Add @41; ToString @41; ConfigureAwait @42; ExecuteReaderAsync @42; ReadAsync @43; GetString @44; ToString @61; NewGuid @61; ToInvariantOrNull @72; ToString @82; ExecuteNonQueryAsync @84 | FROM items @40; INSERT INTO item_price_history @51 |
| <span id="m-02c152f6bf65"></span><code>ItemPriceHistoryRecorder.Add(DbCommand,string,object?)</code><br>87–93 | CreateParameter @89; Add @92 | No extracted literal effects. |

</details>

## KitComponentCostCalculator.cs {#src-686835232a2b}

<code>Software/src/GetSeek.Application/Pricing/KitComponentCostCalculator.cs</code> · 221 lines.

SHA-256: <code>c204d00b8b484f2b2c9f4f77d35388ff6bebab3ba247e3956e5ecc29209a5b10</code>.

Declarations: <code>KitComponentCostLine</code> (line 8), <code>KitComponentCostResult</code> (line 19), <code>KitComponentCostCalculator</code> (line 31).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5cdc1ffbc5f5"></span><code>KitComponentCostCalculator.CalculateItemOrKitAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>34–89 | ConfigureAwait @41; GetActiveKitInfoAsync @41; CalculateAsync @44; NormalizeCostBasis @46; CreateCommand @50; AddParam @59; ToString @59; ExecuteReaderAsync @60; ReadAsync @61; GetInt64 @64; ReadExactCost @65; IsDBNull @67; GetString @81; ToMinor @85 | FROM items @52 |
| <span id="m-95603a9da0b6"></span><code>KitComponentCostCalculator.CalculateAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>91–191 | ConfigureAwait @98; DecomposeToLeavesAsync @98; NormalizeCostBasis @105; CreateCommand @123; AddParam @136; ToString @136; ExecuteReaderAsync @137; ReadAsync @138; Add @140; Add @141; GetInt64 @146; ReadExactCost @147; IsDBNull @149; ToMinor @181 | FROM items @126 |
| <span id="m-00fd462c5916"></span><code>KitComponentCostCalculator.AddParam(DbCommand,string,object)</code><br>193–199 | CreateParameter @195; Add @198 | No extracted literal effects. |
| <span id="m-f2c51f448926"></span><code>KitComponentCostCalculator.NormalizeCostBasis(string)</code><br>201–207 | ToLowerInvariant @201; Trim @201 | No extracted literal effects. |
| <span id="m-6b0a33402ddb"></span><code>KitComponentCostCalculator.ReadExactCost(DbDataReader,int,int)</code><br>209–218 | IsDBNull @211; TryParseInvariant @212; GetString @212; GetInt64 @217 | No extracted literal effects. |
| <span id="m-72090da13f25"></span><code>KitComponentCostCalculator.ToMinor(decimal)</code><br>220–220 | Round @220 | No extracted literal effects. |

</details>

## KitPriceAlertCommands.cs {#src-4faee8fa1e75}

<code>Software/src/GetSeek.Application/Pricing/KitPriceAlertCommands.cs</code> · 37 lines.

SHA-256: <code>3f8862e4d1640505b2563acc861175fcbd0333d461243a9c9419d42468174209</code>.

Declarations: <code>ResolveKitPriceAlertCommand : ICommand&lt;bool&gt;</code> (line 7), <code>ResolveKitPriceAlertCommandHandler : ICommandHandler&lt;ResolveKitPriceAlertCommand, bool&gt;</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e7c7d8c5187a"></span><code>ResolveKitPriceAlertCommandHandler.HandleAsync(ResolveKitPriceAlertCommand,CommandEnvelope&lt;ResolveKitPriceAlertCommand&gt;,CancellationToken)</code><br>14–33 | ToLowerInvariant @17; Trim @17; Failure(bool) @20; CreateCommand @21; Add @27; Create @27; ToString @27; ToString @28; ToString @29; ConfigureAwait @30; ExecuteNonQueryAsync @30; Success(bool) @31 | UPDATE kit_price_review_alerts @22 · KIT_ALERT_RESOLUTION_INVALID @20; KIT_ALERT_STALE @32 |
| <span id="m-30ff630645c9"></span><code>ResolveKitPriceAlertCommandHandler.Create(System.Data.Common.DbCommand,string,object)</code><br>35–36 | CreateParameter @36 | No extracted literal effects. |

</details>

## OfferEvaluationEngine.cs {#src-f18b3b49b3f0}

<code>Software/src/GetSeek.Application/Pricing/OfferEvaluationEngine.cs</code> · 94 lines.

SHA-256: <code>30a355df24ecf38296ab3579ff19019813dad981014279f2c14e86c1fb579549</code>.

Declarations: <code>PriceOfferDto</code> (line 5), <code>OfferEvaluationEngine</code> (line 25).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-829e3dec53a8"></span><code>OfferEvaluationEngine.EvaluateLineOffer(Guid,Guid?,decimal,long,long,IReadOnlyList&lt;PriceOfferDto&gt;,DateTime,string?,string?)</code><br>27–65 | ToList @40; Where @40; Where @40; Equals @41; IsNullOrWhiteSpace @46; First @57; ThenBy @57; ThenByDescending @57; OrderByDescending @57; Select @57; Select @57; CalculateDiscount @57; Clamp @58 | No extracted literal effects. |
| <span id="m-ebf965cfaa13"></span><code>OfferEvaluationEngine.CalculateDiscount(PriceOfferDto,decimal,long,long)</code><br>67–93 | Floor @72; Round @74; Max @76 | No extracted literal effects. |

</details>

## PriceChangeProposalCommands.cs {#src-e9a59f73b4f4}

<code>Software/src/GetSeek.Application/Pricing/PriceChangeProposalCommands.cs</code> · 30 lines.

SHA-256: <code>f42d6fc9c9a101adeb5f338a8d6e5810ae9e03d14de853f9637cd83dd90905d3</code>.

Declarations: <code>PriceChangeProposalDto</code> (line 5), <code>ResolvePriceChangeProposalCommand : ICommand&lt;bool&gt;</code> (line 24).

## PriceOfferCommands.cs {#src-96b68fcbfd04}

<code>Software/src/GetSeek.Application/Pricing/PriceOfferCommands.cs</code> · 167 lines.

SHA-256: <code>81a986d433f35dd012db0dbcd9f09caf9a4598add73c1d478abcfacbed6a46c5</code>.

Declarations: <code>SavePriceOfferCommand : ICommand&lt;Guid&gt;</code> (line 9), <code>SetPriceOfferStatusCommand : ICommand&lt;bool&gt;</code> (line 30), <code>PriceOfferCommandHandler : ICommandHandler&lt;SavePriceOfferCommand, Guid&gt;, ICommandHandler&lt;SetPriceOfferStatusCommand, bool&gt;</code> (line 35).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4ef83743558d"></span><code>PriceOfferCommandHandler.HandleAsync(SavePriceOfferCommand,CommandEnvelope&lt;SavePriceOfferCommand&gt;,CancellationToken)</code><br>39–147 | Trim @42; ToLowerInvariant @43; ToUpperInvariant @46; IsNullOrWhiteSpace @47; Trim @47; Failure(Guid) @51; Truncate @58; TryParse @64; CreateCommand @74; Add @76; ToString @77; ConfigureAwait @77; ExecuteScalarAsync @77; TryParse @78; ToString @84; ToInt32 @85; ExecuteScalarAsync @85; ExecuteScalarAsync @91; Trim @98; ExecuteScalarAsync @99; ToString @107; ExecuteScalarAsync @108; NewGuid @114; ToString @115; ToString @133; ToString @134; ToUniversalTime @134; ToUniversalTime @135; ToString @138; ToString @140; Round @141; ExecuteNonQueryAsync @144; Success(Guid) @146 | FROM items @75; FROM price_level_settings @97; FROM price_offers @107; FROM product_categories @83; FROM uoms @90; INSERT INTO price_offers @127; UPDATE price_offers @119 · OFFER_CONFIGURATION_INVALID @51; OFFER_SCOPE_INVALID @55; OFFER_RULE_INVALID @63; OFFER_DATES_INVALID @67; OFFER_ITEM_NOT_FOUND @78; OFFER_CATEGORY_INVALID @86; OFFER_UNIT_INVALID @92; OFFER_TIER_INVALID @100; OFFER_NOT_FOUND @109; OFFER_VERSION_STALE @111; OFFER_VERSION_STALE @145 |
| <span id="m-71f01a823c9f"></span><code>PriceOfferCommandHandler.HandleAsync(SetPriceOfferStatusCommand,CommandEnvelope&lt;SetPriceOfferStatusCommand&gt;,CancellationToken)</code><br>149–161 | ToLowerInvariant @152; Trim @152; Failure(bool) @153; CreateCommand @154; Add @156; ToString @156; ToString @157; ConfigureAwait @158; ExecuteNonQueryAsync @158; Success(bool) @159 | UPDATE price_offers @155 · OFFER_STATUS_INVALID @153; OFFER_VERSION_STALE @160 |
| <span id="m-baac0d96f012"></span><code>PriceOfferCommandHandler.Add(DbCommand,string,object?)</code><br>163–166 | CreateParameter @165; Add @165 | No extracted literal effects. |

</details>

## PriceProposalStateFingerprint.cs {#src-0be05f62386f}

<code>Software/src/GetSeek.Application/Pricing/PriceProposalStateFingerprint.cs</code> · 161 lines.

SHA-256: <code>3617e6b077dd15e4448d70d84040104bdac29ce185fed8ead2a412f6d825faeb</code>.

Declarations: <code>PriceProposalStateFingerprint</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-8ae2a3391e92"></span><code>PriceProposalStateFingerprint.ComputeAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>16–120 | ConfigureAwait @23; AppendQueryAsync @23; ToString @41; GetActiveKitInfoAsync @59; DecomposeToLeavesAsync @62; ToList @68; OrderBy @68; Append @71; Append @71; ToString @71; ToString @72; ToHexString @119; HashData @119; GetBytes @119; ToString @119 | FROM item_kits @102; FROM item_kits @23; FROM item_price_levels @55; FROM items @23; FROM items @75; FROM price_level_settings @51; FROM store_config @47; JOIN item_kit_components @102; JOIN item_pricing @102; JOIN item_pricing @23; JOIN item_pricing @75; JOIN items @102; JOIN product_categories @23; JOIN product_categories @75; JOIN product_category_pricing_rules @23; JOIN product_category_pricing_rules @75 |
| <span id="m-081b2cd910a3"></span><code>PriceProposalStateFingerprint.AppendQueryAsync(DbConnection,DbTransaction?,StringBuilder,string,string?,CancellationToken)</code><br>122–160 | CreateCommand @130; CreateParameter @135; Add @138; ConfigureAwait @142; ExecuteReaderAsync @142; ReadAsync @143; Append @145; Append @145; ToString @145; IsDBNull @148; ToString @150; GetValue @150; ToString @151 | No extracted literal effects. |

</details>

## PricingCommands.cs {#src-110703c52a80}

<code>Software/src/GetSeek.Application/Pricing/PricingCommands.cs</code> · 144 lines.

SHA-256: <code>991fe6e42899ef3725918a81f9a3e6f9fe9028fc5a5259a19ea43552bfb0924c</code>.

Declarations: <code>ItemTierPricingInput</code> (line 7), <code>SaveItemPricingCommand : ICommand&lt;bool&gt;</code> (line 14), <code>BatchPricingResult</code> (line 35), <code>ApplyBatchPricingCommand : ICommand&lt;BatchPricingResult&gt;</code> (line 43), <code>CreatePricingMassRunCommand : ICommand&lt;Guid&gt;</code> (line 57), <code>PricingMassRunPreviewRow</code> (line 82), <code>PricingTierRunOperation</code> (line 94), <code>PricingMassRunTierPreview</code> (line 104), <code>PricingMassRunPreviewDto</code> (line 108), <code>PreviewPricingMassRunCommand : ICommand&lt;PricingMassRunPreviewDto&gt;</code> (line 117), <code>ProcessPricingMassRunCycleCommand : ICommand&lt;PricingMassRunCycleResult&gt;</code> (line 122), <code>SetPricingMassRunControlCommand : ICommand&lt;bool&gt;</code> (line 130), <code>PricingMassRunCycleResult</code> (line 135).

## PricingMassRunCommandHandler.cs {#src-f557bef172d1}

<code>Software/src/GetSeek.Application/Pricing/PricingMassRunCommandHandler.cs</code> · 1,243 lines.

SHA-256: <code>2a4736600e04c98d00dd27881e08522fd2eef70d432adc38c306fa90438ea115</code>.

Declarations: <code>PricingMassRunCommandHandler : ICommandHandler&lt;CreatePricingMassRunCommand, Guid&gt;, ICommandHandler&lt;PreviewPricingMassRunCommand, PricingMassRunPreviewDto&gt;, ICommandHandler&lt;ProcessPricingMassRunCycleCommand, PricingMassRunCycleResult&gt;, ICommandHandler&lt;SetPricingMassRunControlCommand, bool&gt;</code> (line 13), <code>RunCandidate</code> (line 21), <code>AutomaticStrategy</code> (line 28), <code>PreviewCandidate</code> (line 890), <code>CurrentTier</code> (line 992).

<details markdown>
<summary>Methods, calls, table effects and failures (22)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-1a2974493dbb"></span><code>PricingMassRunCommandHandler.TryParseAutomaticStrategy(string,AutomaticStrategy)</code><br>31–45 | Split @34; TryParse @36; TryParse @37 | No extracted literal effects. |
| <span id="m-493b9107613b"></span><code>PricingMassRunCommandHandler.HandleAsync(CreatePricingMassRunCommand,CommandEnvelope&lt;CreatePricingMassRunCommand&gt;,CancellationToken)</code><br>47–214 | ToString @54; NewGuid @55; IsNullOrWhiteSpace @57; Trim @59; Failure(Guid) @62; ToLowerInvariant @65; Trim @65; ConfigureAwait @88; ValidateTierOperationsAsync @88; ToArray(Guid) @92; OrderBy(Guid) @92; Distinct(Guid) @92; Select(Guid) @92; Where(Guid) @92; Empty(Guid) @92; ToString @93; ComputeConfigurationFingerprint @99; CreateCommand @103; AddParam @106; ExecuteReaderAsync @107; ReadAsync @108; Equals @110; GetString @110; Success(Guid) @112; Parse @112; ValidatePreviewAsync @119; ToString @129; ToInt32 @130; ExecuteScalarAsync @130; ReadDecimalPlacesAsync @134; TryConvertRoundingIncrement @135; ToString @162; Trim @163; ToString @165; ToString @172; Serialize @183; ExecuteNonQueryAsync @184; SnapshotCandidatesAsync @187; ExecuteNonQueryAsync @199; ToString @208; ExecuteNonQueryAsync @209 | FROM pricing_mass_runs @105; FROM product_categories @128; INSERT INTO pricing_mass_runs @146; UPDATE pricing_mass_run_previews @205; UPDATE pricing_mass_runs @196 · IDEMPOTENCY_KEY_INVALID @62; PRICING_POLICY_INVALID @67; PRICING_CYCLE_SIZE_INVALID @69; PRICE_NEGATIVE @71; PRICING_CONFIGURATION_INVALID @75; COST_BASIS_INVALID @78; ROUNDING_RULE_INVALID @82; PRICING_RUN_KIND_INVALID @87; PRICING_TIER_OPERATION_INVALID @91; BATCH_CAP_EXCEEDED @95; BATCH_SELECTION_STALE @97; IDEMPOTENCY_CONFLICT @111; PRICING_PREVIEW_REQUIRED @117; CATEGORY_INACTIVE @131; INVALID_ROUNDING_INCREMENT @138; PRICING_SCOPE_EMPTY @190; BATCH_SELECTION_STALE @192; PRICING_PREVIEW_STALE @210 |
| <span id="m-9bbb7433b331"></span><code>PricingMassRunCommandHandler.HandleAsync(PreviewPricingMassRunCommand,CommandEnvelope&lt;PreviewPricingMassRunCommand&gt;,CancellationToken)</code><br>216–342 | ToArray(Guid) @222; OrderBy(Guid) @222; Distinct(Guid) @222; Select(Guid) @222; Where(Guid) @222; Empty(Guid) @222; ToString @223; Failure(PricingMassRunPreviewDto) @225; ToLowerInvariant @229; Trim @229; ConfigureAwait @244; ValidateTierOperationsAsync @244; ComputeConfigurationFingerprint @250; CreateCommand @255; AddParam @257; ToString @257; ToInt32 @258; ExecuteScalarAsync @258; ReadPreviewCandidatesAsync @262; SequenceEqual @266; OrderBy @266; Select @266; Any @269; ReadDecimalPlacesAsync @272; TryConvertRoundingIncrement @273; ParsePricingMethod @275; ParseRoundingRule @276; Take @279; TryParseAutomaticStrategy @281; ResolveCost @283; Equals @286; ResolveEffectiveBasePrice @298; PreviewTierOperationsAsync @299; Any @301; Add @303; ResolveCostSource @303; Skip @305; Any @316; HashCandidateRecords @318; NewGuid @319; AddMinutes @320; Serialize @321; ToArray @321; ToString @330; ToString @330; ToString @331; ToString @332; ExecuteNonQueryAsync @336; IsNullOrWhiteSpace @340; Success(PricingMassRunPreviewDto) @341 | FROM product_categories @256; INSERT INTO pricing_mass_run_previews @327 · BATCH_SELECTION_STALE @225; PRICING_CONFIGURATION_INVALID @228; PRICING_CONFIGURATION_INVALID @239; PRICING_RUN_KIND_INVALID @243; PRICING_TIER_OPERATION_INVALID @247; CATEGORY_INACTIVE @259; PRICING_SCOPE_EMPTY @265; BATCH_SELECTION_STALE @267; ZERO_PRICE_CONFIRMATION_REQUIRED @270; INVALID_ROUNDING_INCREMENT @274 |
| <span id="m-6f1c4e9a205c"></span><code>PricingMassRunCommandHandler.HandleAsync(SetPricingMassRunControlCommand,CommandEnvelope&lt;SetPricingMassRunControlCommand&gt;,CancellationToken)</code><br>344–403 | ToLowerInvariant @349; Trim @349; Failure(bool) @351; CreateCommand @356; AddParam @360; ToString @360; ConfigureAwait @361; ExecuteReaderAsync @361; ReadAsync @362; GetString @364; GetInt32 @365; Success(bool) @369; ToString @383; ExecuteNonQueryAsync @385; ExecuteNonQueryAsync @394; ExecuteNonQueryAsync @400 | FROM pricing_mass_runs @359; UPDATE pricing_mass_run_candidates @391; UPDATE pricing_mass_runs @379; UPDATE pricing_mass_runs @380; UPDATE pricing_mass_runs @381; UPDATE pricing_mass_runs @397 · PRICING_RUN_ACTION_INVALID @351; RUN_NOT_FOUND @363; PRICING_RUN_CLOSED @368; PRICING_RUN_STATE_INVALID @371; PRICING_RUN_CLOSED @373; PRICING_RUN_STATE_INVALID @386 |
| <span id="m-e74d5cadfea2"></span><code>PricingMassRunCommandHandler.HandleAsync(ProcessPricingMassRunCycleCommand,CommandEnvelope&lt;ProcessPricingMassRunCycleCommand&gt;,CancellationToken)</code><br>405–815 | ToString @412; CreateCommand @436; AddParam @448; ToString @448; ConfigureAwait @449; ExecuteReaderAsync @449; ReadAsync @450; Failure(PricingMassRunCycleResult) @452; GetString @455; Parse @457; GetInt64 @458; GetInt32 @461; IsDBNull @462; Parse @462; Deserialize(PricingTierRunOperation[]) @475; Success(PricingMassRunCycleResult) @480; ExecuteReaderAsync @511; Add @514; ReadDecimalPlacesAsync @529; Equals @538; MarkCandidateAsync @546; InsertRunItemAsync @548; TryParseAutomaticStrategy @562; ParsePricingMethod @578; ParseRoundingRule @579; ToString @629; NewGuid @629; BuildInputFingerprint @634; ToFingerprintTuple @634; ExecuteNonQueryAsync @638; ResolveEffectiveBasePrice @644; CreateAsync @648; ExecuteNonQueryAsync @665; ToString @701; ExecuteNonQueryAsync @711; RecordAsync @716; ToString @720; ExecuteNonQueryAsync @737; ApplyTierOperationsAsync @741; ToInt32 @783; ExecuteScalarAsync @783; ExecuteNonQueryAsync @810 | FROM pricing_mass_run_candidates @781; FROM pricing_mass_runs @439; INSERT INTO item_pricing @674; INSERT INTO pending_shelf_labels @723; INSERT INTO pricing_mass_run_items @621; INSERT INTO pricing_mass_run_items @748; UPDATE item_pricing @671; UPDATE items @662; UPDATE pricing_mass_runs @791 · RUN_NOT_FOUND @452; PRICING_RUN_CONFIGURATION_INVALID @476; PRICING_CYCLE_SIZE_INVALID @489 · DYNAMIC SQL: inspect manually |
| <span id="m-dd3cc8e69752"></span><code>PricingMassRunCommandHandler.AddParam(DbCommand,string,object)</code><br>817–823 | CreateParameter @819; Add @822 | No extracted literal effects. |
| <span id="m-afb0709bc7c8"></span><code>PricingMassRunCommandHandler.ComputeConfigurationFingerprint(CreatePricingMassRunCommand,string,string,string[])</code><br>825–849 | Trim @829; ToLowerInvariant @830; Trim @830; ToString @831; ToString @832; Trim @833; Trim @834; ToString @835; ToString @836; ToString @838; Join @841; ToUpperInvariant @842; Trim @844; Serialize @845; ToHexString @848; HashData @848; GetBytes @848 | No extracted literal effects. |
| <span id="m-e567707599e0"></span><code>PricingMassRunCommandHandler.SnapshotCandidatesAsync(DbConnection,DbTransaction?,Guid,Guid?,string[],string?,bool,CancellationToken)</code><br>851–888 | CreateCommand @855; ToString @863; Add @864; AddParam @865; Join @867; IsNullOrWhiteSpace @870; ToString @884; ToString @885; Trim @886; ConfigureAwait @887; ExecuteNonQueryAsync @887 | FROM product_categories @871 · DYNAMIC SQL: inspect manually |
| <span id="m-a45d71ab2155"></span><code>PricingMassRunCommandHandler.ResolveCost(PreviewCandidate,string)</code><br>894–899 | — | No extracted literal effects. |
| <span id="m-f05f452719a8"></span><code>PricingMassRunCommandHandler.ResolveCostSource(PreviewCandidate,string)</code><br>901–910 | — | No extracted literal effects. |
| <span id="m-6f3b73c4a746"></span><code>PricingMassRunCommandHandler.ReadPreviewCandidatesAsync(DbConnection,DbTransaction?,Guid?,string[],string?,bool,CancellationToken)</code><br>912–943 | CreateCommand @915; ToString @920; Add @920; AddParam @920; Join @921; IsNullOrWhiteSpace @924; Replace @931; ToString @934; Trim @935; ConfigureAwait @937; ExecuteReaderAsync @937; ReadAsync @938; Add @939; GetString @939; GetInt64 @939; IsDBNull @940; GetInt32 @941 | FROM product_categories @925 · DYNAMIC SQL: inspect manually |
| <span id="m-07ca75c9a433"></span><code>PricingMassRunCommandHandler.HashCandidateRecords(IEnumerable&lt;PreviewCandidate&gt;)</code><br>945–952 | Select @947; OrderBy @947; Join @947; ToString @948; ToString @948; ToString @949; ToString @949; ToLowerInvariant @951; ToHexString @951; HashData @951; GetBytes @951 | No extracted literal effects. |
| <span id="m-812a19b640eb"></span><code>PricingMassRunCommandHandler.ValidateTierOperationsAsync(DbConnection,DbTransaction?,string,IReadOnlyList&lt;PricingTierRunOperation&gt;?,CancellationToken)</code><br>954–990 | ConfigureAwait @960; ReadDecimalPlacesAsync @960; CreateCommand @962; ExecuteReaderAsync @965; ReadAsync @966; Add @966; GetString @966; IsNullOrWhiteSpace @971; Contains @971; Add @972; ParseRoundingRule @982; IsRoundingRuleCompatible @983; TryConvertRoundingIncrement @985; Any @988 | FROM price_level_settings @964 |
| <span id="m-d762faabd555"></span><code>PricingMassRunCommandHandler.PreviewTierOperationsAsync(DbConnection,DbTransaction?,string,long,IReadOnlyList&lt;PricingTierRunOperation&gt;?,int,CancellationToken)</code><br>995–1060 | CreateCommand @1001; AddParam @1008; ConfigureAwait @1009; ExecuteReaderAsync @1009; ReadAsync @1010; IsDBNull @1012; Parse @1012; GetString @1012; GetInt64 @1013; GetInt32 @1014; TryGetValue @1020; ResolveTierPrice @1022; MakeTierSpec @1023; TryConvertRoundingIncrement @1042; ApplyRoundingRule @1044; ParseRoundingRule @1044; Round @1045; Add @1056 | FROM price_level_settings @1004; JOIN item_price_levels @1004 |
| <span id="m-a476ee40f1cb"></span><code>PricingMassRunCommandHandler.MakeTierSpec(string,decimal?,long?)</code><br>1062–1067 | — | No extracted literal effects. |
| <span id="m-9aa2aaf21788"></span><code>PricingMassRunCommandHandler.ApplyTierOperationsAsync(DbConnection,DbTransaction?,Guid,long,IReadOnlyList&lt;PricingTierRunOperation&gt;,int,string,Guid,Guid,Guid,DateTime,string,CancellationToken)</code><br>1069–1126 | ConfigureAwait @1079; PreviewTierOperationsAsync @1079; ToString @1079; CreateCommand @1086; AddParam @1090; ExecuteReaderAsync @1091; ReadAsync @1092; GetString @1094; IsDBNull @1094; Parse @1094; GetInt64 @1095; ToString @1115; ExecuteNonQueryAsync @1117; RecordAsync @1119; ToString @1122; ToString @1122 | FROM item_price_levels @1089; INSERT INTO item_price_levels @1110 |
| <span id="m-46938df44e36"></span><code>PricingMassRunCommandHandler.ValidatePreviewAsync(DbConnection,DbTransaction?,CreatePricingMassRunCommand,Guid,string,Guid,DateTime,CancellationToken)</code><br>1128–1161 | CreateCommand @1134; AddParam @1138; ToString @1138; ConfigureAwait @1139; ExecuteReaderAsync @1139; ReadAsync @1140; GetString @1141; IsDBNull @1142; Equals @1144; ToString @1144; TryParse @1146; Deserialize(string[]) @1151; ToArray(Guid) @1153; OrderBy(Guid) @1153; Distinct(Guid) @1153; Select(Guid) @1153; Where(Guid) @1153; Empty(Guid) @1153; ToString @1153; ReadPreviewCandidatesAsync @1155; SequenceEqual @1157; Select @1157; HashCandidateRecords @1158 | FROM pricing_mass_run_previews @1137 |
| <span id="m-79739250b4f7"></span><code>PricingMassRunCommandHandler.BuildInputFingerprint((string Id, long BasePriceMinor, long Lbp, long Mac, long ManualCost, string TrackingPolicy),string,string,decimal,long,string,long)</code><br>1163–1176 | Join @1172; ToString @1173; ToHexString @1175; HashData @1175; GetBytes @1175 | No extracted literal effects. |
| <span id="m-0f1e12d147e1"></span><code>PricingMassRunCommandHandler.ToFingerprintTuple(RunCandidate)</code><br>1178–1179 | — | No extracted literal effects. |
| <span id="m-1c80ce5ab12e"></span><code>PricingMassRunCommandHandler.MarkCandidateAsync(DbConnection,DbTransaction?,Guid,string,string,long?,long?,long?,string?,string?,string,CancellationToken)</code><br>1181–1203 | CreateCommand @1186; AddParam @1192; ToString @1199; ConfigureAwait @1201; ExecuteNonQueryAsync @1201 | UPDATE pricing_mass_run_candidates @1188 · InvalidOperationException @1202 |
| <span id="m-8644d794ab78"></span><code>PricingMassRunCommandHandler.InsertRunItemAsync(DbConnection,DbTransaction?,Guid,RunCandidate,long,long,string,long,string,string,string,string,CancellationToken)</code><br>1205–1229 | CreateCommand @1210; AddParam @1216; ToString @1216; NewGuid @1216; ToString @1217; BuildInputFingerprint @1222; ToFingerprintTuple @1222; ConfigureAwait @1228; ExecuteNonQueryAsync @1228 | INSERT INTO pricing_mass_run_items @1212 |
| <span id="m-d9f726827fad"></span><code>PricingMassRunCommandHandler.ReadDecimalPlacesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>1231–1242 | CreateCommand @1236; ConfigureAwait @1239; ExecuteScalarAsync @1239; ToInt32 @1240; Clamp @1241 | FROM store_config @1238 |

</details>

## PricingProposalGenerator.cs {#src-0b4076865ac4}

<code>Software/src/GetSeek.Application/Pricing/PricingProposalGenerator.cs</code> · 323 lines.

SHA-256: <code>982e1cd50f8ff603e86e82394a2a887b891c4b7041408c5cc19dd37f6ed8f55b</code>.

Declarations: <code>PricingProposalGenerator</code> (line 9), <code>Request</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b89150f54e96"></span><code>PricingProposalGenerator.CreateAsync(DbConnection,DbTransaction?,Request,CancellationToken)</code><br>29–101 | nameof @36; ConfigureAwait @40; ComputeAsync @40; IsNullOrWhiteSpace @42; ToString @45; CreateCommand @46; Add @55; ToString @56; ExecuteNonQueryAsync @59; ToString @81; NewGuid @81; ToString @89; ToInt64 @98; Round @98; ToString @99; ExecuteNonQueryAsync @100 | INSERT INTO price_change_proposals @70; UPDATE price_change_proposals @49 · ArgumentOutOfRangeException @36; ArgumentOutOfRangeException @38 |
| <span id="m-7aae1a4e59b0"></span><code>PricingProposalGenerator.CreateKitCostProposalAsync(DbConnection,DbTransaction?,Guid,DateTime,CancellationToken)</code><br>104–213 | CreateCommand @125; Add @137; ToString @137; ConfigureAwait @138; ExecuteReaderAsync @138; ReadAsync @139; GetString @141; IsDBNull @142; GetInt32 @144; ParseStoredPercentage @145; GetInt64 @147; Equals @157; CalculateAsync @159; ExecuteScalarAsync @168; ToInt32 @170; ParseRoundingRule @172; Equals @174; TryParse @175; ToString @181; ExecuteReaderAsync @183; ReadAsync @184; GetString @186; Parse @188; GetInt64 @189; IsDBNull @191; IsRoundingRuleCompatible @192; TryConvertRoundingIncrement @196; ParsePricingMethod @198; ResolveEffectiveBasePrice @200; CreateAsync @201 | FROM item_pricing @128; FROM product_category_pricing_rules @179; FROM store_config @167; JOIN item_kits @128; JOIN items @128 |
| <span id="m-ba54b930e87d"></span><code>PricingProposalGenerator.CreateCategoryReassignmentProposalAsync(DbConnection,DbTransaction?,Guid,DateTime,CancellationToken)</code><br>216–314 | CreateCommand @235; Add @242; ToString @242; ConfigureAwait @243; ExecuteReaderAsync @243; ReadAsync @244; IsDBNull @245; GetString @245; GetInt64 @247; Equals @253; ExecuteReaderAsync @265; Parse @267; Parse @271; GetActiveKitInfoAsync @278; CalculateAsync @281; ExecuteScalarAsync @300; ToInt32 @301; ParseRoundingRule @303; IsRoundingRuleCompatible @304; TryConvertRoundingIncrement @307; ParsePricingMethod @308; ResolveEffectiveBasePrice @310; CreateAsync @311 | FROM items @238; FROM product_category_pricing_rules @262; FROM store_config @299; JOIN item_pricing @238 |
| <span id="m-9c878cca6ef1"></span><code>PricingProposalGenerator.Add(DbCommand,string,object)</code><br>316–322 | CreateParameter @318; Add @321 | No extracted literal effects. |

</details>

## ResolvePriceChangeProposalCommandHandler.cs {#src-16f124637658}

<code>Software/src/GetSeek.Application/Pricing/ResolvePriceChangeProposalCommandHandler.cs</code> · 321 lines.

SHA-256: <code>0c0fcd1422a1429fa494fab27fefb4f8926193c189f487d37a10ec750b9cc428</code>.

Declarations: <code>ResolvePriceChangeProposalCommandHandler : ICommandHandler&lt;ResolvePriceChangeProposalCommand, bool&gt;</code> (line 10), <code>CategoryRuleSnapshot</code> (line 258).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b35a2eef1f26"></span><code>ResolvePriceChangeProposalCommandHandler.HandleAsync(ResolvePriceChangeProposalCommand,CommandEnvelope&lt;ResolvePriceChangeProposalCommand&gt;,CancellationToken)</code><br>13–248 | ToString @20; CreateCommand @30; AddParam @39; ToString @39; ConfigureAwait @40; ExecuteReaderAsync @40; ReadAsync @41; Failure(bool) @43; GetString @46; IsDBNull @47; GetInt64 @47; Equals @56; ComputeAsync @63; Parse @64; IsMatchingFingerprint @66; ToString @78; ExecuteNonQueryAsync @80; Success(bool) @81; Equals @90; TryParse @93; ReadCategoryRuleAsync @98; ReadDecimalPlacesAsync @104; ParseRoundingRule @106; IsRoundingRuleCompatible @107; TryParse @113; TryConvertRoundingIncrement @114; ExecuteNonQueryAsync @160; ExecuteNonQueryAsync @185; ExecuteNonQueryAsync @198; RecordAsync @205; ToString @209; ToString @219; NewGuid @219; ExecuteNonQueryAsync @226; ExecuteNonQueryAsync @244 | FROM price_change_proposals @33; INSERT INTO item_pricing @122; INSERT INTO pending_shelf_labels @212; UPDATE item_pricing @166; UPDATE items @195; UPDATE price_change_proposals @233; UPDATE price_change_proposals @71 · PROPOSAL_NOT_FOUND @43; PROPOSAL_ALREADY_RESOLVED @58; PROPOSAL_RULE_MISSING @95; PROPOSAL_RULE_MISSING @101; ROUNDING_PRECISION_UNSUPPORTED @109; INVALID_ROUNDING_INCREMENT @116; PRICING_STRATEGY_CHANGED @190; ITEM_NOT_FOUND @200 |
| <span id="m-65fb41993c92"></span><code>ResolvePriceChangeProposalCommandHandler.AddParam(DbCommand,string,object)</code><br>250–256 | CreateParameter @252; Add @255 | No extracted literal effects. |
| <span id="m-43a1af55f6ce"></span><code>ResolvePriceChangeProposalCommandHandler.ReadCategoryRuleAsync(DbConnection,DbTransaction?,Guid,long,CancellationToken)</code><br>266–288 | CreateCommand @273; AddParam @281; ToString @281; ConfigureAwait @283; ExecuteReaderAsync @283; ReadAsync @284; GetString @285; GetInt64 @286; IsDBNull @286 | FROM product_category_pricing_rules @275 |
| <span id="m-6e65f1ff089e"></span><code>ResolvePriceChangeProposalCommandHandler.ReadDecimalPlacesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>290–301 | CreateCommand @295; ConfigureAwait @298; ExecuteScalarAsync @298; ToInt32 @299 | FROM store_config @297 |
| <span id="m-c6a9fd38f7e0"></span><code>ResolvePriceChangeProposalCommandHandler.IsMatchingFingerprint(string,string?)</code><br>303–320 | IsNullOrWhiteSpace @305; FromHexString @312; FixedTimeEquals @314 | No extracted literal effects. |

</details>

## SaveItemPricingCommandHandler.cs {#src-eb108abd205b}

<code>Software/src/GetSeek.Application/Pricing/SaveItemPricingCommandHandler.cs</code> · 504 lines.

SHA-256: <code>b4871163c0052ebf5f4af7104aa393b5eaaf90d814df3f48b38618419352827c</code>.

Declarations: <code>SaveItemPricingCommandHandler : ICommandHandler&lt;SaveItemPricingCommand, bool&gt;</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-24d43c4f5793"></span><code>SaveItemPricingCommandHandler.HandleAsync(SaveItemPricingCommand,CommandEnvelope&lt;SaveItemPricingCommand&gt;,CancellationToken)</code><br>25–345 | ToString @32; ToString @33; IsNullOrWhiteSpace @36; Contains @36; Trim @36; Failure(bool) @38; ToLowerInvariant @41; Trim @55; Contains @57; ParseRoundingRule @61; ToUpperInvariant @66; Trim @66; Trim @75; Trim @81; ConfigureAwait @87; MatchesActiveCategoryRuleAsync @87; CreateCommand @97; ExecuteScalarAsync @101; ToInt32 @104; TryConvertRoundingIncrement @110; AddParam @130; ExecuteReaderAsync @131; ReadAsync @132; IsDBNull @134; GetInt64 @134; ParsePricingMethod @154; IsRoundingRuleCompatible @155; GetActiveKitInfoAsync @161; CalculateAsync @165; ResolveEffectiveBasePrice @185; ToString @221; ToString @228; ToString @230; ExecuteNonQueryAsync @236; ExecuteNonQueryAsync @245; RecordAsync @250; NewGuid @267; ToString @268; ToString @273; ExecuteNonQueryAsync @274; EnqueueAffectedKitAlertsAsync @276; ExecuteReaderAsync @306; ReadAsync @307; GetString @309; IsDBNull @310; GetInt64 @310; ToString @329; Equals @334; Success(bool) @344 | FROM item_price_levels @303; FROM items @129; FROM store_config @100; INSERT INTO item_price_levels @316; INSERT INTO item_pricing @191; INSERT INTO pending_shelf_labels @260; UPDATE items @242 · INVALID_PRICING_METHOD @38; INVALID_PRICING_PERCENTAGE @45; INVALID_MARGIN_CEILING @49; INVALID_ROUNDING_RULE @59; INVALID_COST_FLOOR_SOURCE @70; INVALID_COST_BASIS_SOURCE @78; INVALID_PRICE_SOURCE @83; CATEGORY_PRICING_RULE_STALE @88; INVALID_PRICE_SOURCE @92; INVALID_ROUNDING_INCREMENT @112; ITEM_NOT_FOUND @142; ROUNDING_PRECISION_UNSUPPORTED @157; INVALID_TIER_PRICING @287; INVALID_TIER_WEIGHT @291; INVALID_TIER_PRICE @295 |
| <span id="m-3c1e4dc5361a"></span><code>SaveItemPricingCommandHandler.AddParam(DbCommand,string,object)</code><br>347–353 | CreateParameter @349; Add @352 | No extracted literal effects. |
| <span id="m-8f7a7d90c6ce"></span><code>SaveItemPricingCommandHandler.MatchesActiveCategoryRuleAsync(DbConnection,DbTransaction?,SaveItemPricingCommand,CancellationToken)</code><br>355–387 | CreateCommand @361; AddParam @377; ToString @377; ToString @378; ToLowerInvariant @380; Trim @380; Trim @381; ToString @382; Trim @384; ToString @385; ToInt64 @386; ConfigureAwait @386; ExecuteScalarAsync @386 | FROM product_category_pricing_rules @363; JOIN items @363 |
| <span id="m-4adf484b0536"></span><code>SaveItemPricingCommandHandler.EnqueueAffectedKitAlertsAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken,string)</code><br>389–502 | CreateCommand @401; AddParam @434; ToString @434; ConfigureAwait @435; ExecuteReaderAsync @435; ReadAsync @436; TryParse @438; GetString @438; Add @440; GetInt64 @440; CalculateAsync @447; CreateKitCostProposalAsync @449; Parse @451; Round @454; ToString @470; ToInt64 @471; ExecuteScalarAsync @471; ToString @492; NewGuid @492; ExecuteNonQueryAsync @500 | FROM item_kits @404; FROM item_kits @461; FROM kit_price_review_alerts @481; INSERT INTO kit_price_review_alerts @481; JOIN item_kit_components @404; JOIN item_kit_components @461; JOIN item_kits @404; JOIN items @404; JOIN items @461 |

</details>

## ShelfLabelCommands.cs {#src-590c68d05298}

<code>Software/src/GetSeek.Application/Pricing/ShelfLabelCommands.cs</code> · 146 lines.

SHA-256: <code>e55060d631e5fe6c975eb58bf64e85cd7e1dbbd482920a2a70a5a211c235bb76</code>.

Declarations: <code>ShelfLabelVersion</code> (line 10), <code>QueueShelfLabelPrintCommand : ICommand&lt;string&gt;</code> (line 12), <code>QueueShelfLabelPrintCommandHandler : ICommandHandler&lt;QueueShelfLabelPrintCommand, string&gt;</code> (line 17), <code>LabelSnapshot</code> (line 19), <code>SetShelfLabelStatusCommand : ICommand&lt;int&gt;</code> (line 104), <code>SetShelfLabelStatusCommandHandler : ICommandHandler&lt;SetShelfLabelStatusCommand, int&gt;</code> (line 112).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-cbc484ac38a3"></span><code>QueueShelfLabelPrintCommandHandler.HandleAsync(QueueShelfLabelPrintCommand,CommandEnvelope&lt;QueueShelfLabelPrintCommand&gt;,CancellationToken)</code><br>22–90 | ToArray(ShelfLabelVersion) @25; Select(ShelfLabelVersion) @25; GroupBy(ShelfLabelVersion) @25; Where(ShelfLabelVersion) @25; Empty(ShelfLabelVersion) @25; First @26; Failure(string) @28; ConfigureAwait @29; IsActiveAdminAsync @29; CreateCommand @34; ExecuteReaderAsync @36; ReadAsync @37; GetString @39; IsDBNull @41; GetInt32 @41; DisposeAsync @46; IsNullOrWhiteSpace @47; Add @63; ToString @63; ExecuteReaderAsync @64; ReadAsync @65; Add @67; GetString @67; GetInt32 @67; GetInt64 @68; ToString @71; NewGuid @71; Serialize @72; ToString @77; ExecuteNonQueryAsync @79; ExecuteNonQueryAsync @86; Success(string) @89 | FROM barcodes @56; FROM output_device_config @35; FROM pending_shelf_labels @56; INSERT INTO hardware_jobs @76; JOIN items @56; JOIN store_config @56; UPDATE pending_shelf_labels @84 · SHELF_LABEL_SELECTION_INVALID @28; ADMIN_REQUIRED @30; SHELF_LABEL_PROFILE_MISSING @38; SHELF_LABEL_OUTPUT_DISABLED @48; SHELF_LABEL_PRINTER_UNVERIFIED @50; SHELF_LABEL_SELECTION_STALE @66; SHELF_LABEL_SELECTION_STALE @87 |
| <span id="m-1d52f2e5a8a4"></span><code>QueueShelfLabelPrintCommandHandler.IsActiveAdminAsync(Guid,CancellationToken)</code><br>92–98 | CreateCommand @94; Add @96; ToString @96; ToInt64 @97; ConfigureAwait @97; ExecuteScalarAsync @97 | FROM users @95; JOIN user_roles @95 |
| <span id="m-537836a05bf5"></span><code>QueueShelfLabelPrintCommandHandler.Add(DbCommand,string,object)</code><br>100–101 | CreateParameter @101; Add @101 | No extracted literal effects. |
| <span id="m-4a4c4f3271bc"></span><code>SetShelfLabelStatusCommandHandler.HandleAsync(SetShelfLabelStatusCommand,CommandEnvelope&lt;SetShelfLabelStatusCommand&gt;,CancellationToken)</code><br>114–142 | ToLowerInvariant @117; Trim @117; ToArray(ShelfLabelVersion) @118; Select(ShelfLabelVersion) @118; GroupBy(ShelfLabelVersion) @118; Where(ShelfLabelVersion) @118; Empty(ShelfLabelVersion) @118; First @119; Failure(int) @121; Equals @124; CreateCommand @131; Add @136; ToString @136; ToString @137; ToString @137; ConfigureAwait @138; ExecuteNonQueryAsync @138; Success(int) @141 | UPDATE pending_shelf_labels @132 · SHELF_LABEL_STATUS_INVALID @121; SHELF_LABEL_SELECTION_INVALID @123; SHELF_LABEL_CONFIRMATION_REQUIRED @125; SHELF_LABEL_SELECTION_STALE @139 |
| <span id="m-b48a2289b359"></span><code>SetShelfLabelStatusCommandHandler.Add(DbCommand,string,object)</code><br>144–145 | CreateParameter @145; Add @145 | No extracted literal effects. |

</details>

## LifecycleStatusScope.cs {#src-a9082bf99a27}

<code>Software/src/GetSeek.Application/ReadServices/LifecycleStatusScope.cs</code> · 9 lines.

SHA-256: <code>8dc55cc22a141d525b9f011a487108f0b20ecb961afe990c66fae26fa0e43696</code>.

Declarations: <code>LifecycleStatusScope</code> (line 4).

## ReadProjections.cs {#src-f3a0ea7fd9d1}

<code>Software/src/GetSeek.Application/ReadServices/ReadProjections.cs</code> · 279 lines.

SHA-256: <code>29bd2c58a85aed8ae3322637df1a62bfb2aa94bc2f9da5b7ef25ae986643452e</code>.

Declarations: <code>StoreProfileProjection</code> (line 3), <code>CatalogItemProjection</code> (line 19), <code>ActiveShiftProjection</code> (line 46), <code>ActivityOrderProjection</code> (line 56), <code>DraftCartLineProjection</code> (line 74), <code>DraftCartProjection</code> (line 92), <code>InventoryItemProjection</code> (line 106), <code>KitAvailabilityProjection</code> (line 134), <code>ItemLotBalanceProjection</code> (line 141), <code>ItemSerialStateCountProjection</code> (line 142), <code>ItemKitUsageProjection</code> (line 143), <code>ItemTraceabilitySummaryProjection</code> (line 144), <code>ItemStockHistoryRow</code> (line 152), <code>ItemStockHistoryPage</code> (line 177), <code>ItemPriceHistoryRow</code> (line 192), <code>LotCandidateProjection</code> (line 219), <code>SerialCandidateProjection</code> (line 234), <code>RestaurantOrderLineProjection</code> (line 246), <code>RestaurantOrderProjection</code> (line 258).

## ReferenceSnapshot.cs {#src-7a2c51dec98f}

<code>Software/src/GetSeek.Application/ReferenceSnapshot.cs</code> · 204 lines.

SHA-256: <code>9bc779eabfaab44d19a35c047e7a32426d1241a5b60b6dc7a6fbbbd27e698717</code>.

Declarations: <code>UnitDefinition</code> (line 9), <code>CategoryRecord</code> (line 16), <code>SupplierRecord</code> (line 23), <code>ReferenceSnapshot</code> (line 32).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a5b951333974"></span><code>ReferenceSnapshot.TryGetUom(string?,UnitDefinition)</code><br>59–68 | IsNullOrWhiteSpace @61; TryGetValue @67; Trim @67 | No extracted literal effects. |
| <span id="m-f6eb69fde29c"></span><code>ReferenceSnapshot.FindCategory(Guid?,string?)</code><br>70–83 | TryGetValue @74; IsNullOrWhiteSpace @77; TryGetValue @82; Trim @82 | No extracted literal effects. |
| <span id="m-4aabbaff0c6f"></span><code>ReferenceSnapshot.TryGetSupplierId(string?,Guid)</code><br>85–100 | IsNullOrWhiteSpace @88; TryGetValue @93; Trim @93 | No extracted literal effects. |
| <span id="m-07140a5fa76f"></span><code>ReferenceSnapshot.TryGetSupplierById(Guid,SupplierRecord)</code><br>102–105 | TryGetValue @104 | No extracted literal effects. |
| <span id="m-0f6e189fbf37"></span><code>ReferenceSnapshot.LoadAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>107–203 | CreateCommand @114; ConfigureAwait @118; ExecuteReaderAsync @118; ReadAsync @119; GetString @121; IsDBNull @122; GetInt32 @125; Add @140; Parse @154; IsNullOrWhiteSpace @162; TryAdd @164; Trim @164; Trim @168 | FROM price_level_settings @136; FROM product_categories @150; FROM store_config @136; FROM third_parties @179; FROM uoms @117 |

</details>

## GetStockBalanceQuery.cs {#src-fe18fc631cf9}

<code>Software/src/GetSeek.Application/Reports/GetStockBalanceQuery.cs</code> · 76 lines.

SHA-256: <code>30b3bbbe375485bad3e3d1763e080576c78318951ccbe5e3ac9fe9656ce001db</code>.

Declarations: <code>StockBalanceResult</code> (line 7), <code>StockBalanceQueryHandler</code> (line 16).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-44adda65c03e"></span><code>StockBalanceQueryHandler.ExecuteAsync(Guid,string,Guid?,ISessionContext?,CancellationToken)</code><br>18–75 | HasPermission @27; CreateCommand @32; CreateParameter @42; ToString @44; Add @45; ToString @54; ConfigureAwait @60; ExecuteReaderAsync @60; ReadAsync @61; GetDecimal @63 | FROM stock_movements @33 · UnauthorizedAccessException @29 |

</details>

## GetXReportQuery.cs {#src-354461e57f05}

<code>Software/src/GetSeek.Application/Reports/GetXReportQuery.cs</code> · 230 lines.

SHA-256: <code>c03b934583345c4249f6304477d968030a738cc40119d405aa28271d959d0bfd</code>.

Declarations: <code>XReportResult</code> (line 8), <code>GetXReportQueryHandler</code> (line 31).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-649f39a486d1"></span><code>GetXReportQueryHandler.ExecuteAsync(Guid,ISessionContext,CancellationToken)</code><br>33–228 | HasPermission @37; CreateCommand @47; CreateParameter @54; ToString @56; Add @57; ConfigureAwait @59; ExecuteReaderAsync @59; ReadAsync @60; Parse @62; GetString @62; Parse @63; GetInt64 @64; GetInt32 @102; ReadAsync @176; Amount @177 | FROM cash_movements @184; FROM invoice_collections @176; FROM sales_invoices @117; FROM sales_invoices @83; FROM sales_tenders @145; FROM shifts @49; JOIN sales_invoices @145 · UnauthorizedAccessException @39; InvalidOperationException @69 |

</details>

## GetZReportQuery.cs {#src-3104c5445d0f}

<code>Software/src/GetSeek.Application/Reports/GetZReportQuery.cs</code> · 450 lines.

SHA-256: <code>da581a63e1691503800d6e86ad5136fc98c64c9a399c2a22ead47e843debe578</code>.

Declarations: <code>ZReportFinancialRecordLine</code> (line 9), <code>ZReportResult</code> (line 29), <code>GetZReportQueryHandler</code> (line 59).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-150873f5a324"></span><code>GetZReportQueryHandler.ExecuteAsync(Guid,ISessionContext,CancellationToken)</code><br>61–277 | HasPermission @65; CreateCommand @71; CreateParameter @86; ToString @88; Add @89; ConfigureAwait @91; ExecuteReaderAsync @91; ReadAsync @92; Parse @94; GetString @94; Parse @95; GetInt64 @98; GetInt32 @99; IsDBNull @113; ToDictionary(Dictionary&lt;string,long&gt;, string, long) @118; Deserialize(Dictionary&lt;string,long&gt;, string, long) @118; IsNullOrWhiteSpace @121; Deserialize(List&lt;ZReportFinancialRecordLine&gt;, ZReportFinancialRecordLine) @125; Deserialize(Dictionary&lt;string, long&gt;, string, long) @139; CreateParameter @189; Add @192; ExecuteScalarAsync @194; ToInt32 @200; ExecuteAsync @209; BuildSalaryAndExpenseRecordLinesAsync @247 | FROM shift_z_reports @73; FROM shifts @188; FROM shifts @219 · UnauthorizedAccessException @67; InvalidOperationException @197; InvalidOperationException @203 |
| <span id="m-a18bcd4c377b"></span><code>GetZReportQueryHandler.BuildSalaryAndExpenseRecordLinesAsync(DbConnection,DbTransaction?,Guid,Guid,DateTime,DateTime,string,CancellationToken)</code><br>279–447 | ToString @290; ToString @291; CreateCommand @294; CreateParameter @307; ToString @309; Add @310; ConfigureAwait @312; ExecuteReaderAsync @312; ReadAsync @313; GetString @315; GetInt64 @318; Equals @321; Add @324; ToString @417; GetInt32 @427; IsDBNull @427 | FROM expense_payments @344; FROM expense_payments @392; FROM expense_records @392; FROM salary_payments @297; JOIN expense_records @344; JOIN money_accounts @297; JOIN money_accounts @344; JOIN person_records @297 |

</details>

## CartAllocationCommandHandler.cs {#src-46ba4855fda6}

<code>Software/src/GetSeek.Application/Sales/CartAllocationCommandHandler.cs</code> · 166 lines.

SHA-256: <code>8c128a1d20f86614962771610616802c351afa8664673317d8080934df303b9e</code>.

Declarations: <code>CartAllocationCommandHandler : ICommandHandler&lt;SelectLotForCartLineCommand, bool&gt;, ICommandHandler&lt;SelectSerialForCartLineCommand, bool&gt;</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ee0fab044b83"></span><code>CartAllocationCommandHandler.HandleAsync(SelectLotForCartLineCommand,CommandEnvelope&lt;SelectLotForCartLineCommand&gt;,CancellationToken)</code><br>19–49 | Equals @26; Failure(bool) @27; TryRoundBaseQuantity @33; ConfigureAwait @37; GetLotLocationBalanceAsync @37; InsertPendingAsync @44; Success(bool) @48 | LOCATION_NOT_SELLABLE @27; INVALID_QUANTITY @30; INSUFFICIENT_LOT_BALANCE @41 |
| <span id="m-a881109dcdae"></span><code>CartAllocationCommandHandler.HandleAsync(SelectSerialForCartLineCommand,CommandEnvelope&lt;SelectSerialForCartLineCommand&gt;,CancellationToken)</code><br>51–120 | Equals @58; Failure(bool) @59; IsNullOrWhiteSpace @61; TryRoundBaseQuantity @65; Trim @69; ConfigureAwait @70; SerialIsReservedAsync @70; CreateCommand @75; Add @79; ToString @79; ExecuteReaderAsync @81; ReadAsync @82; IsDBNull @84; GetString @84; ToString @97; ExecuteNonQueryAsync @97; PendingSerialExistsAsync @99; InsertPendingAsync @105; Success(bool) @119 | DELETE FROM pending_allocations @97; FROM serials @78 · LOCATION_NOT_SELLABLE @59; SERIAL_SELECTION_REQUIRED @62; INVALID_SERIAL_QUANTITY_FRACTIONAL @66; SERIAL_RESERVED @71; SERIAL_NOT_FOUND @90; SERIAL_NOT_AVAILABLE @92; SERIAL_WRONG_LOCATION @95; SERIAL_ALREADY_COMMITTED @100; SERIAL_ALREADY_COMMITTED @115 |
| <span id="m-2abddf84e322"></span><code>CartAllocationCommandHandler.PendingSerialExistsAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>122–130 | CreateCommand @124; Add @127; ToString @127; ConfigureAwait @129; ExecuteScalarAsync @129 | FROM pending_allocations @126 |
| <span id="m-603bcd406d76"></span><code>CartAllocationCommandHandler.InsertPendingAsync(DbConnection,DbTransaction?,Guid,Guid,string?,Guid?,string?,decimal,DateTime,CancellationToken)</code><br>132–155 | CreateCommand @135; Add @145; ToString @145; NewGuid @145; ToString @146; ToString @147; ToInvariant @151; AddMinutes @152; ToString @153; ConfigureAwait @154; ExecuteNonQueryAsync @154 | INSERT INTO pending_allocations @137 |
| <span id="m-e020c2b9448c"></span><code>CartAllocationCommandHandler.Add(DbCommand,string,object)</code><br>157–163 | CreateParameter @159; Add @162 | No extracted literal effects. |

</details>

## CartCalculationService.cs {#src-32a44e0155db}

<code>Software/src/GetSeek.Application/Sales/CartCalculationService.cs</code> · 385 lines.

SHA-256: <code>1f0bc17024c353be060e060b909ac1613fccb27ddd2d6426b3acb13a99d5f7be</code>.

Declarations: <code>PromoType</code> (line 6), <code>CartCalculationLine</code> (line 13), <code>CartCalculationRequest</code> (line 26), <code>CartCalculationLineResult</code> (line 40), <code>CartCalculationResult</code> (line 53), <code>CartCalculationService</code> (line 81).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9a20cb475de9"></span><code>CartCalculationResult.Failure(string,string)</code><br>77–78 | Empty(CartCalculationLineResult) @78 | No extracted literal effects. |
| <span id="m-c6fae087787e"></span><code>CartCalculationService.Calculate(CartCalculationRequest)</code><br>89–383 | IsNullOrWhiteSpace @91; Equals @98; Failure @103; Empty(CartCalculationLineResult) @123; Any @133; Round @139; Add @140; ToList @146; OrderBy @146; Where @146; Sum @150; ToLowerInvariant @154; Trim @154; ToMinorUnits @179; Trim @207; ToDictionary @211; Clamp @213; Floor @220; GetValueOrDefault @221; Sum @239; Sum @239; Add @269; GroupBy @276; Where @276; Sum @283; Add @299; ThenBy @305; OrderByDescending @305; GetValueOrDefault @320; Add @323; Sum @337; Sum @343; Calculate @348 | No extracted literal effects. |

</details>

## CashFinancialSettings.cs {#src-b0b1815ac331}

<code>Software/src/GetSeek.Application/Sales/CashFinancialSettings.cs</code> · 88 lines.

SHA-256: <code>6a5859de5b5d7ab617dacb0bcabf68d96e75e81b3bca71f07d66df714fcead88</code>.

Declarations: <code>CashFinancialSettings</code> (line 4), <code>CashSettlementBreakdown</code> (line 23), <code>CashSettlementCalculator</code> (line 32).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a32ee5094006"></span><code>CashFinancialSettings.Defaults(int)</code><br>18–20 | Clamp @19 | No extracted literal effects. |
| <span id="m-977ebee9ceb6"></span><code>CashSettlementCalculator.Calculate(long,long,long,decimal,int,CashFinancialSettings,bool,string)</code><br>34–87 | Equals @48; Max @53; Round @54; ToLowerInvariant @71; Ceiling @74; Floor @75; Abs @84 | No extracted literal effects. |

</details>

## CheckoutPriceResolver.cs {#src-15f8ac37a8a8}

<code>Software/src/GetSeek.Application/Sales/CheckoutPriceResolver.cs</code> · 220 lines.

SHA-256: <code>3655e47cad764bb6fb24a37194dcdd1824773faeee5565e370a797f3af3fb72e</code>.

Declarations: <code>CheckoutPriceResult</code> (line 7), <code>CheckoutPriceResolver</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ade06f62d3d9"></span><code>CheckoutPriceResolver.ResolveAsync(DbConnection,DbTransaction?,Guid,Guid,long,decimal,long?,string?,Guid?,CancellationToken)</code><br>17–199 | CreateCommand @32; ConfigureAwait @36; ExecuteReaderAsync @36; ReadAsync @37; IsDBNull @39; GetInt32 @39; ExecuteReaderAsync @55; Add @58; GetString @60; AddParam @79; ToString @79; ExecuteScalarAsync @80; ToString @83; IsNullOrWhiteSpace @87; ToLowerInvariant @89; Trim @89; ResolveEffectiveTier @91; FirstOrDefault @92; Equals @92; ToString @101; ExecuteScalarAsync @102; ToInt64 @105; ExecuteReaderAsync @120; ParseWeightMode @123; ParseStoredPercentage @124; GetInt64 @125; ResolveTierPrice @130; Round @132; ExecuteReaderAsync @143; Equals @156; ExecuteReaderAsync @160; ReadDecimalCost @163; IsBelowCostFloor @177; IsAuthorizedAsync @179 | FROM draft_carts @73; FROM item_price_levels @117; FROM item_pricing @100; FROM item_pricing @141; FROM items @157; FROM items @158; FROM price_level_settings @54; FROM store_config @35; JOIN third_parties @73 |
| <span id="m-5966905d0cdf"></span><code>CheckoutPriceResolver.ReadDecimalCost(DbDataReader,int,int)</code><br>201–210 | IsDBNull @203; TryParse @204; GetString @204; GetInt64 @209 | No extracted literal effects. |
| <span id="m-931444bce8f1"></span><code>CheckoutPriceResolver.AddParam(DbCommand,string,object)</code><br>212–218 | CreateParameter @214; Add @217 | No extracted literal effects. |

</details>

## CommercialDocumentCommands.cs {#src-85955b820e22}

<code>Software/src/GetSeek.Application/Sales/CommercialDocumentCommands.cs</code> · 50 lines.

SHA-256: <code>4119cfe79a5bbe040e7e1817eda3c0ccbe5f036abadcdf947c511caf4cebd2ba</code>.

Declarations: <code>QueueCommercialDocumentCommand : ICommand&lt;Guid&gt;</code> (line 9), <code>CommercialDocumentCommandHandler : ICommandHandler&lt;QueueCommercialDocumentCommand,Guid&gt;</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-942ca257bb03"></span><code>CommercialDocumentCommandHandler.HandleAsync(QueueCommercialDocumentCommand,CommandEnvelope&lt;QueueCommercialDocumentCommand&gt;,CancellationToken)</code><br>14–43 | Failure(Guid) @17; ConfigureAwait @18; HasActivePermissionAsync @18; ReadAsync @19; EnqueueAsync @22; Text @22; Parse @23; PersistAsync @23; Success(Guid) @23; Parse @23; Serialize @40; Amount @40; Select @40; Parse @40; IsNullOrEmpty @41 | FROM hardware_jobs @19; FROM shipment_allocations @36; FROM shipments @28; FROM store_config @39; FROM supplier_invoice_lines @27; FROM supplier_invoice_lines @35; FROM supplier_invoices @27; FROM supplier_payments @27; FROM supplier_return_lines @37; FROM supplier_returns @29; JOIN output_device_config @39; JOIN receipt_designs @39; JOIN sales_invoices @28; JOIN sales_line_kit_allocations @36; JOIN store_legal_identity @39; JOIN supplier_invoice_lines @37; JOIN supplier_invoices @29; JOIN third_parties @27; JOIN third_parties @29; JOIN users @39 · DOCUMENT_INVALID @17; AUTH_UNAUTHORIZED @18; DOCUMENT_NOT_FOUND @31 |
| <span id="m-fa532c7baac1"></span><code>CommercialDocumentCommandHandler.PersistAsync(string,JsonElement,CancellationToken)</code><br>44–49 | Parse @46; GetString @46; GetProperty @46; ConfigureAwait @47; ExecuteAsync @47; GetProperty @47; GetInt32 @47 | UPDATE hardware_jobs @47 · InvalidOperationException @48 |

</details>

## CommercialLifecycleCommands.cs {#src-ad6a9468d7c1}

<code>Software/src/GetSeek.Application/Sales/CommercialLifecycleCommands.cs</code> · 167 lines.

SHA-256: <code>f39908b066705e8d4e12af0001403305fd30ea8d5342d664c0536df30afa5583</code>.

Declarations: <code>SavePurchaseDraftCommand : ICommand&lt;Guid&gt;</code> (line 10), <code>CancelInvoiceLine</code> (line 12), <code>CancelInvoiceRemainderCommand : ICommand&lt;Guid&gt;</code> (line 13), <code>RequestReturnShipmentCommand : ICommand&lt;Guid&gt;</code> (line 15), <code>ReceiveReturnShipmentCommand : ICommand&lt;Guid&gt;</code> (line 17), <code>CancelReturnShipmentRequestCommand : ICommand&lt;Guid&gt;</code> (line 21), <code>CommercialLifecycleCommandHandler : ICommandHandler&lt;SavePurchaseDraftCommand,Guid&gt;, ICommandHandler&lt;CancelInvoiceRemainderCommand,Guid&gt;, ICommandHandler&lt;CancelReturnShipmentRequestCommand,Guid&gt;, ICommandHandler&lt;RequestReturnShipmentCommand,Guid&gt;, ICommandHandler&lt;ReceiveReturnShipmentCommand,Guid&gt;</code> (line 24).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0ea17aed1fac"></span><code>CommercialLifecycleCommandHandler.HandleAsync(SavePurchaseDraftCommand,CommandEnvelope&lt;SavePurchaseDraftCommand&gt;,CancellationToken)</code><br>28–39 | Any @30; Bad @30; NewGuid @31; ConfigureAwait @34; ExecuteAsync @34; Serialize @34; Success(Guid) @38 | INSERT INTO purchase_invoice_drafts @37; UPDATE purchase_invoice_drafts @34 |
| <span id="m-48b697a42924"></span><code>CommercialLifecycleCommandHandler.HandleAsync(CancelInvoiceRemainderCommand,CommandEnvelope&lt;CancelInvoiceRemainderCommand&gt;,CancellationToken)</code><br>40–89 | IsNullOrWhiteSpace @43; Bad @43; ConfigureAwait @44; ReadAsync @44; Amount @45; ToList @47; Select @47; Parse @47; Text @47; Max @47; Allocate @48; Any @49; Count @49; Distinct @49; Select @49; Any @49; ToString @49; NewGuid @50; Parse @53; Min @56; GroupBy @56; Sum @56; FirstOrDefault @57; Any @60; Sum @62; Entitlement @64; Add @65; ExecuteAsync @68; Trim @68; GroupBy @73; Sum @75; Where @76; Min @78; IsNullOrEmpty @80; Success(Guid) @88 | FROM invoice_cancelled_lines @61; FROM invoice_stock_reservations @54; FROM invoice_stock_reservations @72; FROM sale_return_lines @61; FROM sales_invoices @44; FROM sales_lines @46; INSERT INTO invoice_cancellations @68; INSERT INTO invoice_cancelled_lines @71; JOIN invoice_fulfillment @44; UPDATE invoice_fulfillment @87; UPDATE invoice_stock_reservations @82; UPDATE sales_invoices @87 |
| <span id="m-42142a30d538"></span><code>CommercialLifecycleCommandHandler.HandleAsync(RequestReturnShipmentCommand,CommandEnvelope&lt;RequestReturnShipmentCommand&gt;,CancellationToken)</code><br>90–111 | ConfigureAwait @92; HasActivePermissionAsync @92; Bad @92; PreviewAsync @93; ReadAsync @95; ToList(ProcessReturnCommand) @96; SelectMany(ProcessReturnCommand) @96; Where(ProcessReturnCommand) @96; Select @96; Deserialize(ProcessReturnCommand) @96; Text @96; ToList @99; Select @99; GroupBy @99; Concat @99; Sum @99; Where @102; SelectMany @102; Sum @106; Parse @106; NewGuid @109; ExecuteAsync @109; Serialize @109; Success(Guid) @110 | FROM return_dispositions @105; FROM return_shipment_requests @95; FROM sales_line_kit_allocations @104; INSERT INTO return_shipment_requests @109 |
| <span id="m-3c371240d17c"></span><code>CommercialLifecycleCommandHandler.HandleAsync(ReceiveReturnShipmentCommand,CommandEnvelope&lt;ReceiveReturnShipmentCommand&gt;,CancellationToken)</code><br>112–159 | ConfigureAwait @114; ReadAsync @114; Bad @115; Deserialize(ProcessReturnCommand) @116; Text @116; HasActivePermissionAsync @117; ReadBalanceAsync @118; Count @122; Distinct @122; Select @122; FirstOrDefault @126; Add @127; GroupBy @130; Sum @132; Sum @133; Where @133; Add @135; Any @137; Any @137; Any @141; Any @141; PreviewAsync @146; Round @149; NewGuid @154; HandleAsync @155; ExecuteAsync @157; Serialize @157; Success(Guid) @158 | FROM return_shipment_requests @114; INSERT INTO return_shipment_receipts @157; UPDATE return_shipment_requests @157 |
| <span id="m-d630f1c0f394"></span><code>CommercialLifecycleCommandHandler.HandleAsync(CancelReturnShipmentRequestCommand,CommandEnvelope&lt;CancelReturnShipmentRequestCommand&gt;,CancellationToken)</code><br>160–165 | IsNullOrWhiteSpace @162; Bad @162; ConfigureAwait @163; ExecuteAsync @163; Success(Guid) @164 | UPDATE return_shipment_requests @163 |
| <span id="m-eaa449ac42c6"></span><code>CommercialLifecycleCommandHandler.Bad(string,string)</code><br>166–166 | Failure(Guid) @166 | No extracted literal effects. |

</details>

## FinancialReceiptJobs.cs {#src-de80764eabf6}

<code>Software/src/GetSeek.Application/Sales/FinancialReceiptJobs.cs</code> · 74 lines.

SHA-256: <code>7605a15eebd3c9bd3aa7a914a3dbf6e475a0b825f95c36b88e0aafbba8ebae26</code>.

Declarations: <code>FinancialReceiptRow</code> (line 7), <code>FinancialReceiptJobs</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ddcdaf733fa9"></span><code>FinancialReceiptJobs.EnqueueAsync(IUnitOfWork,IHardwareJobRepository,Guid,string,string,long,long,string,IEnumerable&lt;FinancialReceiptRow&gt;,Guid,DateTime,CancellationToken)</code><br>11–70 | ConfigureAwait @14; ReadAsync @14; Text @24; Amount @29; ToString @30; ToDecimal @30; ToString @31; ReadBalanceAsync @39; Parse @39; Add @40; Format @40; Serialize @51; ToString @52; Select @57; EnqueueAsync @61; IsNullOrEmpty @62; ExecuteAsync @63 | FROM invoice_collection_allocations @34; FROM invoice_collections @26; FROM invoice_collections @35; FROM return_dispositions @48; FROM sale_returns @27; FROM sale_returns @45; FROM store_config @14; JOIN items @48; JOIN lots @48; JOIN output_device_config @14; JOIN receipt_designs @14; JOIN sale_return_lines @48; JOIN sales_invoices @45; JOIN store_legal_identity @14; JOIN users @14; UPDATE hardware_jobs @63 · InvalidOperationException @23; InvalidOperationException @28 |

</details>

## InvoiceCollectionPlanner.cs {#src-02826350800a}

<code>Software/src/GetSeek.Application/Sales/InvoiceCollectionPlanner.cs</code> · 39 lines.

SHA-256: <code>21c775760656912d5095b16f63ffbb33ec2080a469a308f65121e989f7d5553f</code>.

Declarations: <code>InvoiceCollectionPlanner</code> (line 5).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-26dde05d208b"></span><code>InvoiceCollectionPlanner.Validate(IReadOnlyList&lt;InvoiceBalance&gt;,IReadOnlyList&lt;InvoiceCollectionAllocation&gt;,long)</code><br>7–21 | ThrowIfNegativeOrZero @9; Count @10; Distinct @10; Select @10; Select @11; Any @11; Aggregate @12; SingleOrDefault @16; Sum @20 | InvalidOperationException @13; InvalidOperationException @18 |
| <span id="m-a828ff33bca0"></span><code>InvoiceCollectionPlanner.AllocateOldestFirst(IEnumerable&lt;InvoiceBalance&gt;,long)</code><br>22–37 | ThrowIfNegativeOrZero @24; ToArray @25; ThenBy @25; OrderBy @25; Where @25; Count @26; Distinct @26; Select @26; Min @31; Add @32 | InvalidOperationException @27; InvalidOperationException @35 |

</details>

## InvoiceLedger.cs {#src-7b6296dfe88f}

<code>Software/src/GetSeek.Application/Sales/InvoiceLedger.cs</code> · 123 lines.

SHA-256: <code>e92cea82fe454c820380eacd07b84074ace9e29815179d7cb1c3cbfedbbdc9e9</code>.

Declarations: <code>InvoiceLedger</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (11)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4c223f8e273b"></span><code>InvoiceLedger.HasActivePermissionAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>10–21 | ConfigureAwait @12; ReadAsync @12; Amount @18 | FROM user_permission_overrides @12; FROM user_roles @12; FROM users @12; JOIN role_permissions @12 |
| <span id="m-5db92608952b"></span><code>InvoiceLedger.ReadBalanceAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>22–52 | ConfigureAwait @25; ReadAsync @25; Amount @46; Text @47; NullableGuid @47; Parse @49; TryParse @50 | FROM bank_invoice_collections @25; FROM cancellation_refunds @25; FROM cash_movements @25; FROM invoice_cancellations @25; FROM invoice_collection_allocations @25; FROM sale_returns @25; FROM sales_invoices @25; FROM sales_tenders @25; FROM store_config @25; JOIN invoice_payment_terms @25 |
| <span id="m-39e7cb97d00c"></span><code>InvoiceLedger.ExecuteAsync(DbConnection,DbTransaction?,string,CancellationToken,(string Name, object? Value)[])</code><br>54–59 | Create @57; ConfigureAwait @58; ExecuteNonQueryAsync @58 | No extracted literal effects. |
| <span id="m-97f70e981b32"></span><code>InvoiceLedger.ReadAsync(DbConnection,DbTransaction?,string,CancellationToken,(string Name, object? Value)[])</code><br>61–74 | Create @64; ConfigureAwait @65; ExecuteReaderAsync @65; ReadAsync @67; GetName @70; IsDBNull @70; GetValue @70; Add @71 | No extracted literal effects. |
| <span id="m-4c8fa2c857a1"></span><code>InvoiceLedger.Create(DbConnection,DbTransaction?,string,(string Name, object? Value)[])</code><br>76–88 | CreateCommand @79; CreateParameter @82; ToString @83; ToString @83; Add @85 | No extracted literal effects. |
| <span id="m-ba8e4583cc28"></span><code>InvoiceLedger.Text(IReadOnlyDictionary&lt;string,object?&gt;,string)</code><br>90–91 | TryGetValue @91; ToString @91 | No extracted literal effects. |
| <span id="m-95e0a7b1b48f"></span><code>InvoiceLedger.Amount(IReadOnlyDictionary&lt;string,object?&gt;,string)</code><br>92–93 | TryGetValue @93; ToInt64 @93 | No extracted literal effects. |
| <span id="m-3975a43cab5a"></span><code>InvoiceLedger.QuantityValue(IReadOnlyDictionary&lt;string,object?&gt;,string,string)</code><br>94–95 | Parse @95; IsNullOrEmpty @95; Text @95 | No extracted literal effects. |
| <span id="m-66f9e9c6b074"></span><code>InvoiceLedger.NullableGuid(IReadOnlyDictionary&lt;string,object?&gt;,string)</code><br>96–96 | TryParse @96; Text @96 | No extracted literal effects. |
| <span id="m-6623556b2865"></span><code>InvoiceLedger.OpenShiftCurrencyAsync(DbConnection,DbTransaction?,Guid,Guid,CancellationToken)</code><br>98–106 | ConfigureAwait @101; ReadAsync @101; Text @105 | FROM shifts @101; FROM user_roles @101 |
| <span id="m-ea5b32adad77"></span><code>InvoiceLedger.BusinessDateAsync(DbConnection,DbTransaction?,Guid?,DateTime,CancellationToken)</code><br>108–121 | ConfigureAwait @111; ReadAsync @111; IsNullOrEmpty @112; Text @112; IsNullOrWhiteSpace @114; ConvertTimeFromUtc @116; SpecifyKind @116; FindSystemTimeZoneById @116; ToString @120 | FROM shifts @111; FROM store_config @113 |

</details>

## InvoiceSettlementCommandHandler.cs {#src-616fa131d5cf}

<code>Software/src/GetSeek.Application/Sales/InvoiceSettlementCommandHandler.cs</code> · 97 lines.

SHA-256: <code>4af241db791be01ac3151c94c4e1b431c38cc1b31a9be57ba30c6a00462f5341</code>.

Declarations: <code>InvoiceSettlementCommandHandler : ICommandHandler&lt;ReceiveInvoicePaymentCommand,InvoiceCollectionResult&gt;</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-6bf6102851f1"></span><code>InvoiceSettlementCommandHandler.HandleAsync(ReceiveInvoicePaymentCommand,CommandEnvelope&lt;ReceiveInvoicePaymentCommand&gt;,CancellationToken)</code><br>11–64 | Any @16; Count @16; Distinct @16; Select @16; Aggregate @17; Fail @18; ConfigureAwait @20; OpenShiftCurrencyAsync @20; Equals @21; ReadAsync @23; ReadBalanceAsync @29; Amount @30; ValidateManualPaymentAsync @37; NewGuid @40; BusinessDateAsync @40; ExecuteAsync @41; Trim @46; WriteCashMovementAsync @58; EnqueueAsync @60; ToString @61; Success(InvoiceCollectionResult) @63 | FROM shifts @26; FROM third_parties @23; INSERT INTO invoice_collection_allocations @54; INSERT INTO invoice_collections @41; UPDATE sales_invoices @52 |
| <span id="m-c6e5f5574643"></span><code>InvoiceSettlementCommandHandler.ValidateManualPaymentAsync(System.Data.Common.DbConnection,System.Data.Common.DbTransaction?,TenderType,long,string,ManualPaymentConfirmation?,Guid,Guid,DateTime,CancellationToken)</code><br>66–87 | Equals @71; IsNullOrWhiteSpace @72; AddMinutes @73; ConfigureAwait @74; ReadAsync @74; Trim @85 | FROM invoice_collections @80; FROM manual_payment_display @77; FROM manual_payment_display @78; FROM money_events @80; FROM sale_returns @80; FROM sales_tenders @80; FROM shifts @74 |
| <span id="m-985d64bca81d"></span><code>InvoiceSettlementCommandHandler.WriteCashMovementAsync(System.Data.Common.DbConnection,System.Data.Common.DbTransaction?,Guid,int,long,string,string,Guid,Guid,DateTime,string,CancellationToken)</code><br>89–95 | ExecuteAsync @91; NewGuid @94 | INSERT INTO cash_movements @91 |
| <span id="m-51bb8cd1fb33"></span><code>InvoiceSettlementCommandHandler.Fail(string,string)</code><br>96–96 | Failure(InvoiceCollectionResult) @96 | No extracted literal effects. |

</details>

## InvoiceSettlementCommands.cs {#src-a52f4feeda06}

<code>Software/src/GetSeek.Application/Sales/InvoiceSettlementCommands.cs</code> · 28 lines.

SHA-256: <code>1109054f9d64cf1ea30baa7a9be99f303946848e4674783d4e8102fab4a0fad9</code>.

Declarations: <code>IssueOrderInvoiceCommand : ICommand&lt;SalesInvoice&gt;</code> (line 7), <code>OrderInvoicePreview</code> (line 12), <code>PreviewOrderInvoiceCommand : ICommand&lt;OrderInvoicePreview&gt;</code> (line 13), <code>IssueDeferredInvoiceCommand : ICommand&lt;SalesInvoice&gt;</code> (line 16), <code>ReceiveInvoicePaymentCommand : ICommand&lt;InvoiceCollectionResult&gt;</code> (line 23).

## LegacyReturnAdapter.cs {#src-a364c6f04785}

<code>Software/src/GetSeek.Application/Sales/LegacyReturnAdapter.cs</code> · 58 lines.

SHA-256: <code>63cbd548108c3957c25eec502eca52dcd510a3de3522a51d49b4937592800919</code>.

Declarations: <code>LegacyReturnAdapter</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-43cab2a25b3f"></span><code>LegacyReturnAdapter.ExecuteAsync(IUnitOfWork,IHardwareJobRepository,RefundSaleCommand,CommandEnvelope&lt;RefundSaleCommand&gt;,CancellationToken)</code><br>10–56 | ConfigureAwait @14; ReadBalanceAsync @14; Fail @15; Equals @16; ReadAsync @17; GroupBy @20; Sum @22; QuantityValue @25; Text @32; Amount @33; Add @34; Parse @34; Add @43; HandleAsync @49; NullableGuid @52; Success(SalesInvoice) @53; ToString @53 | FROM items @32; FROM items @38; FROM sale_returns @51; FROM sales_line_kit_allocations @26; FROM sales_lines @23; FROM shifts @17 |
| <span id="m-3334e6eb9587"></span><code>LegacyReturnAdapter.Fail(string,string)</code><br>57–57 | Failure(SalesInvoice) @57 | No extracted literal effects. |

</details>

## PurchaseAndMoneyCommands.cs {#src-b2413dd4b01c}

<code>Software/src/GetSeek.Application/Sales/PurchaseAndMoneyCommands.cs</code> · 227 lines.

SHA-256: <code>9b5929036e27a42b7683fd095917de3aea3ea1a851edc04b5e4020cf6114ddbc</code>.

Declarations: <code>RecordSupplierInvoiceCommand : ICommand&lt;Guid&gt;</code> (line 13), <code>PurchaseReceiptInput</code> (line 16), <code>ReceivePurchaseGoodsCommand : ICommand&lt;Guid&gt;</code> (line 17), <code>PaySupplierInvoiceCommand : ICommand&lt;Guid&gt;</code> (line 20), <code>CollectBankInvoiceCommand : ICommand&lt;Guid&gt;</code> (line 23), <code>CreateMoneyAccountCommand : ICommand&lt;Guid&gt;</code> (line 26), <code>RecordAccountOpeningCommand : ICommand&lt;Guid&gt;</code> (line 28), <code>RefundCancelledInvoiceCommand : ICommand&lt;Guid&gt;</code> (line 30), <code>TransferMoneyCommand : ICommand&lt;Guid&gt;</code> (line 33), <code>PurchaseAndMoneyCommandHandler : ICommandHandler&lt;RecordSupplierInvoiceCommand, Guid&gt;, ICommandHandler&lt;ReceivePurchaseGoodsCommand, Guid&gt;, ICommandHandler&lt;PaySupplierInvoiceCommand, Guid&gt;, ICommandHandler&lt;CollectBankInvoiceCommand, Guid&gt;, ICommandHandler&lt;CreateMoneyAccountCommand, Guid&gt;, ICommandHandler&lt;TransferMoneyCommand, Guid&gt;, ICommandHandler&lt;RecordAccountOpeningCommand, Guid&gt;, ICommandHandler&lt;RefundCancelledInvoiceCommand,Guid&gt;</code> (line 37).

<details markdown>
<summary>Methods, calls, table effects and failures (12)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f1ba27b7b958"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(RecordSupplierInvoiceCommand,CommandEnvelope&lt;RecordSupplierInvoiceCommand&gt;,CancellationToken)</code><br>42–84 | ConfigureAwait @48; ReadAsync @48; Bad @49; IsNullOrWhiteSpace @51; Text @54; Trim @54; ResolveFactorAsync @64; Calculate @66; Add @69; NewGuid @71; ToString @71; ToUpperInvariant @71; ToString @71; ExecuteAsync @72; Amount @75; ToString @76; Success(Guid) @83 | FROM item_kits @61; FROM items @61; FROM purchase_invoice_drafts @48; FROM store_config @56; FROM supplier_invoices @54; FROM third_parties @52; INSERT INTO supplier_invoice_lines @77; INSERT INTO supplier_invoices @72; UPDATE purchase_invoice_drafts @82 |
| <span id="m-6fbf10e0e8d2"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(ReceivePurchaseGoodsCommand,CommandEnvelope&lt;ReceivePurchaseGoodsCommand&gt;,CancellationToken)</code><br>86–126 | Count @90; Distinct @90; Select @90; IsNullOrWhiteSpace @90; Bad @90; ConfigureAwait @91; ReadAsync @91; Amount @92; HasActivePermissionAsync @93; NewGuid @94; ExecuteAsync @95; Trim @96; Any @100; Sum @101; Sum @103; Parse @103; Text @103; Parse @104; ResolveFactorAsync @105; ToString @107; ToString @107; HandleAsync @112; Sum @122; Success(Guid) @125 | FROM purchase_receipt_lines @102; FROM purchase_receipt_lines @121; FROM supplier_invoice_credit_lines @102; FROM supplier_invoice_credit_lines @121; FROM supplier_invoice_lines @117; FROM supplier_invoice_lines @99; FROM supplier_invoices @91; INSERT INTO purchase_receipt_lines @114; INSERT INTO purchase_receipts @95; JOIN items @99; UPDATE supplier_invoices @124 |
| <span id="m-7fc2e4cba9a2"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(PaySupplierInvoiceCommand,CommandEnvelope&lt;PaySupplierInvoiceCommand&gt;,CancellationToken)</code><br>128–144 | ConfigureAwait @132; ReadAsync @132; Amount @133; Bad @133; AccountAsync @134; Text @135; NewGuid @136; PostAsync @137; ExecuteAsync @140; Success(Guid) @143 | FROM supplier_invoice_credits @132; FROM supplier_invoices @132; FROM supplier_payments @132; FROM supplier_refunds @132; FROM supplier_returns @132; INSERT INTO supplier_payments @140; UPDATE supplier_invoices @142 |
| <span id="m-d58f24dfc315"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(CollectBankInvoiceCommand,CommandEnvelope&lt;CollectBankInvoiceCommand&gt;,CancellationToken)</code><br>146–160 | ConfigureAwait @149; ReadBalanceAsync @149; Bad @150; AccountAsync @151; Text @152; Amount @152; NewGuid @153; PostAsync @154; ExecuteAsync @156; Success(Guid) @159 | INSERT INTO bank_invoice_collections @156; UPDATE sales_invoices @158 |
| <span id="m-fe0e796766cc"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(CreateMoneyAccountCommand,CommandEnvelope&lt;CreateMoneyAccountCommand&gt;,CancellationToken)</code><br>162–174 | IsNullOrWhiteSpace @165; Bad @165; ConfigureAwait @166; ReadAsync @166; Trim @168; Text @168; NewGuid @170; ExecuteAsync @171; Amount @172; Success(Guid) @173 | FROM money_accounts @167; FROM store_config @166; INSERT INTO money_accounts @171 |
| <span id="m-614a96e577d8"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(TransferMoneyCommand,CommandEnvelope&lt;TransferMoneyCommand&gt;,CancellationToken)</code><br>176–186 | ConfigureAwait @179; AccountAsync @179; Text @180; Amount @180; Bad @180; NewGuid @181; PostAsync @182; Success(Guid) @185 | No extracted literal effects. |
| <span id="m-0c550ea7e283"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(RecordAccountOpeningCommand,CommandEnvelope&lt;RecordAccountOpeningCommand&gt;,CancellationToken)</code><br>188–196 | ConfigureAwait @191; AccountAsync @191; Text @192; Bad @192; ReadAsync @193; PostAsync @195 | FROM money_events @193 |
| <span id="m-48e4165e94c4"></span><code>PurchaseAndMoneyCommandHandler.AccountAsync(Guid,CancellationToken)</code><br>198–202 | ConfigureAwait @200; ReadAsync @200 | FROM money_accounts @200 |
| <span id="m-426228bae305"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(RefundCancelledInvoiceCommand,CommandEnvelope&lt;RefundCancelledInvoiceCommand&gt;,CancellationToken)</code><br>203–215 | ConfigureAwait @206; ReadBalanceAsync @206; Bad @207; AccountAsync @208; Text @209; Amount @209; NewGuid @210; PostAsync @210; ExecuteAsync @212; Success(Guid) @214 | INSERT INTO cancellation_refunds @212; UPDATE sales_invoices @213 |
| <span id="m-e0c7cfd8d329"></span><code>PurchaseAndMoneyCommandHandler.PostAsync(Dictionary&lt;string, object?&gt;,long,string,Guid,string,string,Guid?,Guid,string,DateTime,CancellationToken)</code><br>218–220 | PostAsync @220 | No extracted literal effects. |
| <span id="m-c708a2271b31"></span><code>PurchaseAndMoneyCommandHandler.PostAsync(Dictionary&lt;string, object?&gt;,long,string,Guid,string,string,Guid?,Guid,string,DateTime,Guid?,Guid?,CancellationToken)</code><br>222–224 | PostAsync @224 | No extracted literal effects. |
| <span id="m-a47f44ed23a7"></span><code>PurchaseAndMoneyCommandHandler.Bad(string,string)</code><br>226–226 | Failure(Guid) @226 | No extracted literal effects. |

</details>

## PurchaseCalculationService.cs {#src-dcb2b3d929a5}

<code>Software/src/GetSeek.Application/Sales/PurchaseCalculationService.cs</code> · 23 lines.

SHA-256: <code>2db56dca423a1c6e222e4cab80f4a4fc1e9de5e20521d7668eca1874eb80da1a</code>.

Declarations: <code>PurchaseLineCalculation</code> (line 4), <code>PurchaseInvoiceCalculation</code> (line 5), <code>PurchaseCalculationService</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-550858d6a577"></span><code>PurchaseCalculationService.Preview(IReadOnlyList&lt;SupplierInvoiceLineInput&gt;)</code><br>8–14 | Failure(PurchaseInvoiceCalculation) @10; Calculate @12; Success(PurchaseInvoiceCalculation) @13 | INVALID_LINES @10 |
| <span id="m-a39abf9179bf"></span><code>PurchaseCalculationService.Calculate(SupplierInvoiceLineInput)</code><br>15–22 | Failure(PurchaseLineCalculation) @17; Round @18; Success(PurchaseLineCalculation) @21 | INVALID_PURCHASE_LINE @17; INVALID_DISCOUNT @19 |

</details>

## ReceiptManagementDto.cs {#src-d339072c951d}

<code>Software/src/GetSeek.Application/Sales/ReceiptManagementDto.cs</code> · 44 lines.

SHA-256: <code>70000d070274596c2610da249d03a41c87e3032e1a7432bfa980bd38359d98b0</code>.

Declarations: <code>ReceiptLineDto</code> (line 5), <code>ReceiptManagementDto</code> (line 15).

## SaleCommandHandler.cs {#src-b90bee551ece}

<code>Software/src/GetSeek.Application/Sales/SaleCommandHandler.cs</code> · 1,487 lines.

SHA-256: <code>4f3041a16f706d0bd3f6bdad77381f259b1f450e0e655c48198f5ed904bb811f</code>.

Declarations: <code>SaleCommandHandler : ICommandHandler&lt;AddSaleLineCommand, DraftCart&gt;, ICommandHandler&lt;VoidSaleLineCommand, DraftCart&gt;, ICommandHandler&lt;TakePaymentCommand, SalesInvoice&gt;, ICommandHandler&lt;IssueDeferredInvoiceCommand, SalesInvoice&gt;, ICommandHandler&lt;IssueOrderInvoiceCommand, SalesInvoice&gt;, ICommandHandler&lt;PreviewOrderInvoiceCommand, OrderInvoicePreview&gt;, ICommandHandler&lt;RefundSaleCommand, SalesInvoice&gt;</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (14)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-899ec17ecc86"></span><code>SaleCommandHandler.HandleAsync(AddSaleLineCommand,CommandEnvelope&lt;AddSaleLineCommand&gt;,CancellationToken)</code><br>26–186 | CreateCommand @44; AddParam @48; ToString @48; ConfigureAwait @50; ExecuteReaderAsync @50; ReadAsync @51; GetString @53; GetInt64 @56; IsDBNull @58; ToDecimal @59; GetDouble @59; Parse @60; GetInt32 @61; Failure(DraftCart) @66; Equals @74; IsNullOrWhiteSpace @78; ResolveFactorAsync @95; TryRoundBaseQuantity @116; ResolveAsync @125; Round @137; NewGuid @141; ToString @161; ToString @162; ToInvariant @174; Trim @178; ExecuteNonQueryAsync @180; LoadCartAsync @183; ExecuteAsync @184; Success(DraftCart) @185 | FROM items @47; INSERT INTO draft_cart_lines @146; UPDATE draft_cart_lines @184 · ITEM_NOT_FOUND @66; ITEM_INACTIVE @72; ITEM_NOT_SELLABLE @76; PRICE_OVERRIDE_REASON_REQUIRED @79; FORGED_CONVERSION_FACTOR @87; FORGED_CONVERSION_FACTOR @108 |
| <span id="m-dbef8767a6fa"></span><code>SaleCommandHandler.HandleAsync(VoidSaleLineCommand,CommandEnvelope&lt;VoidSaleLineCommand&gt;,CancellationToken)</code><br>188–212 | CreateCommand @196; AddParam @200; ToString @200; ToString @201; ConfigureAwait @203; ExecuteNonQueryAsync @203; Failure(DraftCart) @206; LoadCartAsync @210; Success(DraftCart) @211 | DELETE FROM draft_cart_lines @199 · LINE_NOT_FOUND @206 |
| <span id="m-bec1ebd1e944"></span><code>SaleCommandHandler.HandleAsync(TakePaymentCommand,CommandEnvelope&lt;TakePaymentCommand&gt;,CancellationToken)</code><br>214–218 | IssueAsync @218 | No extracted literal effects. |
| <span id="m-b858907fb800"></span><code>SaleCommandHandler.HandleAsync(IssueDeferredInvoiceCommand,CommandEnvelope&lt;IssueDeferredInvoiceCommand&gt;,CancellationToken)</code><br>220–228 | ToList @223; IssueAsync @227 | No extracted literal effects. |
| <span id="m-0e238eefdd64"></span><code>SaleCommandHandler.HandleAsync(IssueOrderInvoiceCommand,CommandEnvelope&lt;IssueOrderInvoiceCommand&gt;,CancellationToken)</code><br>230–241 | ConfigureAwait @233; ReadAsync @233; Text @235; Failure(SalesInvoice) @236; IssueAsync @240 | FROM draft_carts @234 · INVOICE_DRAFT_REQUIRED @236 |
| <span id="m-2096456a136d"></span><code>SaleCommandHandler.HandleAsync(PreviewOrderInvoiceCommand,CommandEnvelope&lt;PreviewOrderInvoiceCommand&gt;,CancellationToken)</code><br>243–252 | ConfigureAwait @246; ReadAsync @246; Failure(OrderInvoicePreview) @247; IssueAsync @250; Success(OrderInvoicePreview) @251 | FROM draft_carts @246 · INVOICE_DRAFT_REQUIRED @247 |
| <span id="m-491906686e55"></span><code>SaleCommandHandler.IssueAsync(TakePaymentCommand,CommandEnvelope&lt;TakePaymentCommand&gt;,bool,DateOnly?,CancellationToken,FulfillmentPolicy,string?,Action&lt;OrderInvoicePreview&gt;?)</code><br>254–1234 | ConfigureAwait @262; LoadCartAsync @262; ReadAsync @265; Failure(SalesInvoice) @269; Any @271; Equals @273; CreateCommand @284; AddParam @294; ToString @294; ToInt64 @295; ExecuteScalarAsync @295; HasActivePermissionAsync @310; IsNullOrWhiteSpace @313; ToString @326; ExecuteReaderAsync @327; ReadAsync @328; GetInt64 @330; IsDBNull @331; ToDecimal @331; GetDouble @331; Parse @331; GetString @331; ResolveAsync @335; Defaults @346; ExecuteReaderAsync @360; ReadAsync @361; GetInt32 @363; Clamp @366; GetString @366; GetInt64 @366; TryParse @367; LoadActiveOffersAsync @373; ToString @379; ExecuteScalarAsync @380; ToString @381; LoadItemCategoriesAsync @383; Select @383; Round @387; EvaluateLineOffer @388; GetValueOrDefault @390; ToUniversalTime @395; FirstOrDefault @400; ToList @408; GetValueOrDefault @415; Calculate @429; Order @438; Distinct @438; Add @438; ComputeAsync @438; ToHexString @439; HashData @439; GetBytes @439; Serialize @439; Select @444; First @444; previewCallback @445; Success(SalesInvoice) @445; ExecuteReaderAsync @460; ReadAsync @461; Add @463; GetString @463; ExecuteScalarAsync @474; ToString @475; Sum @503; Trim @524; AddMinutes @527; ToString @540; ToString @541; ExecuteScalarAsync @542; ExecuteScalarAsync @550; ExecuteScalarAsync @557; ExecuteScalarAsync @575; ToInt32 @582; ToString @597; ToString @598; ExecuteNonQueryAsync @599; GetActiveKitInfoAsync @611; DecomposeToLeavesAsync @614; TryGetValue @630; TryGetValue @634; ExecuteScalarAsync @652; Add @677; ResolveActiveSellingLocationAsync @679; IsNullOrEmpty @680; GetLocationBalanceAsync @689; Select @706; Text @710; Contains @710; PlanAsync @713; ExecuteScalarAsync @725; ToString @726; TryParse @728; ToString @730; ExecuteScalarAsync @749; ToString @765; ExecuteReaderAsync @767; ReadAsync @768; GetString @770; GetInt32 @771; NewGuid @792; ToString @819; ToString @822; ToString @823; Trim @832; ToString @834; ExecuteNonQueryAsync @849; ExecuteAsync @854; ToString @856; FirstOrDefault @862; CalculateLineTotal @863; ToString @885; ToInvariant @897; ExecuteNonQueryAsync @907; TryGetValue @911; ToString @924; Serialize @929; ExecuteNonQueryAsync @943; RecordLineAsync @946; MoveAsync @965; ContainsKey @982; CurrentCostAsync @984; Add @988; RecordRoundingAsync @1005; ToString @1026; ExecuteNonQueryAsync @1037; ExecuteNonQueryAsync @1066; ExecuteReaderAsync @1094; ReadAsync @1095; GetString @1097; IsDBNull @1098; GetInt32 @1100; Join @1141; Select @1141; ToString @1141; EnqueueAsync @1148; ExecuteNonQueryAsync @1167; ExecuteScalarAsync @1175; ExecuteNonQueryAsync @1188; ExecuteNonQueryAsync @1230 | DELETE FROM pending_allocations @1228; FROM draft_cart_lines @287; FROM draft_cart_lines @910; FROM invoice_collections @555; FROM items @325; FROM items @650; FROM items @709; FROM manual_payment_display @548; FROM manual_payment_display @549; FROM output_device_config @1091; FROM output_device_config @1174; FROM pending_allocations @458; FROM sale_returns @555; FROM sales_tenders @555; FROM serials @471; FROM shifts @539; FROM shifts @573; FROM shifts @580; FROM shifts @723; FROM stock_movements @1220; FROM store_config @350; FROM third_parties @266; FROM third_parties @378; FROM third_parties @764; INSERT INTO cash_movements @1047; INSERT INTO invoice_fulfillment @855; INSERT INTO invoice_payment_terms @1218; INSERT INTO invoice_sequences @739; INSERT INTO invoice_stock_reservations @956; INSERT INTO sale_line_offers @915; INSERT INTO sales_invoices @798; INSERT INTO sales_line_kit_allocations @968; INSERT INTO sales_lines @870; INSERT INTO sales_tenders @1016; JOIN business_profile_config @350; JOIN items @287; JOIN receipt_designs @1091; JOIN store_config @1091; JOIN store_legal_identity @1091; JOIN third_parties @1091; JOIN users @1091; UPDATE draft_carts @592; UPDATE hardware_jobs @1159; UPDATE hardware_jobs @1182; UPDATE sales_lines @910; UPDATE sales_lines @985; UPDATE serials @1220; UPDATE serials @977 · CUSTOMER_NOT_ELIGIBLE @269; INVALID_TENDER @276; CART_EMPTY @279; CART_CONTAINS_UNSELLABLE_ITEM @298; CART_REVISION_STALE @304; DISCOUNT_UNAUTHORIZED @310; PRICE_OVERRIDE_REASON_REQUIRED @314; PRICE_OVERRIDE_UNAUTHORIZED @316; CART_PRICE_STALE @329; CART_TAX_STALE @334; CART_PRICE_STALE @340; INVOICE_PREVIEW_STALE @440; SERIAL_ALREADY_COMMITTED @478; FREE_SALE_CONFIRMATION_REQUIRED @490; FREE_SALE_MUST_NOT_HAVE_TENDER @494; TENDER_REQUIRED @499; TENDER_AMOUNT_MISMATCH @506; UNVERIFIED_PAYMENT_TENDER @531; AUTH_UNAUTHORIZED @543; PAYMENT_METHOD_NOT_CONFIGURED @551; DUPLICATE_PAYMENT_REFERENCE @558; UNVERIFIED_PAYMENT_TENDER @562; NO_ACTIVE_SHIFT @578; MONETARY_SCALE_UNRESOLVED @583; CART_ALREADY_SETTLED_OR_INVALID @602; NO_ACTIVE_SELLING_LOCATION @682; INSUFFICIENT_STOCK @694; CUSTOMER_INACTIVE @774; CUSTOMER_NOT_FOUND @781; SERIAL_ALREADY_COMMITTED @979 |
| <span id="m-93e1f02fb10a"></span><code>SaleCommandHandler.HandleAsync(RefundSaleCommand,CommandEnvelope&lt;RefundSaleCommand&gt;,CancellationToken)</code><br>1236–1238 | ExecuteAsync @1238 | No extracted literal effects. |
| <span id="m-93a9118a4f7b"></span><code>SaleCommandHandler.LoadCartAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>1239–1366 | CreateCommand @1251; AddParam @1259; ToString @1259; ConfigureAwait @1261; ExecuteReaderAsync @1261; ReadAsync @1262; Parse @1264; GetString @1264; IsDBNull @1266; TryParse @1267; TryParse @1273; GetInt32 @1278; ExecuteReaderAsync @1288; ReadAsync @1289; GetInt32 @1291; ExecuteReaderAsync @1309; ResolveQuantity @1316; GetDouble @1316; ResolveFactor @1318; GetInt64 @1319; ToDecimal @1324; Parse @1325; Add @1329; Recalculate @1364 | FROM draft_cart_lines @1300; FROM draft_carts @1254; FROM store_config @1287 |
| <span id="m-2b553d830c33"></span><code>SaleCommandHandler.LoadActiveOffersAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>1368–1426 | CreateCommand @1373; ConfigureAwait @1383; ExecuteReaderAsync @1383; ReadAsync @1384; TryParse @1386; GetString @1386; IsDBNull @1391; TryParse @1393; ToUniversalTime @1394; TryParse @1401; ToDecimal @1403; GetValue @1403; Add @1405; ParseUtc @1410; ParseGuid @1412; ParseDecimal @1414; GetInt64 @1417; GetInt32 @1418 | FROM price_offers @1375 |
| <span id="m-7590f6c36125"></span><code>SaleCommandHandler.LoadItemCategoriesAsync(DbConnection,DbTransaction?,IEnumerable&lt;Guid&gt;,CancellationToken)</code><br>1428–1448 | Distinct @1435; CreateCommand @1437; AddParam @1440; ToString @1440; ConfigureAwait @1441; ExecuteScalarAsync @1441; TryParse @1442; ToString @1442 | FROM items @1439 |
| <span id="m-ce8271347489"></span><code>SaleCommandHandler.ResolveActiveSellingLocationAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>1450–1456 | FromResult(string?) @1455 | No extracted literal effects. |
| <span id="m-37703c7bf951"></span><code>SaleCommandHandler.HasActivePermissionAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>1458–1472 | CreateCommand @1461; AddParam @1467; ToString @1467; ConfigureAwait @1468; ExecuteReaderAsync @1468; ReadAsync @1469; GetInt32 @1469 | FROM user_permission_overrides @1462; FROM user_roles @1462; FROM users @1462; JOIN role_permissions @1462 |
| <span id="m-394b13c56723"></span><code>SaleCommandHandler.AddParam(DbCommand,string,object?)</code><br>1474–1480 | CreateParameter @1476; Add @1479 | No extracted literal effects. |

</details>

## SaleCommands.cs {#src-5208d9e05ff3}

<code>Software/src/GetSeek.Application/Sales/SaleCommands.cs</code> · 86 lines.

SHA-256: <code>f7c0a90fa23a0772c60b9f608f652a66c47273088fef173fe907dc2e6c416081</code>.

Declarations: <code>AddSaleLineCommand : ICommand&lt;DraftCart&gt;</code> (line 8), <code>VoidSaleLineCommand : ICommand&lt;DraftCart&gt;</code> (line 21), <code>TakePaymentCommand : ICommand&lt;SalesInvoice&gt;</code> (line 30), <code>ManualPaymentConfirmation</code> (line 43), <code>RefundSaleCommand : ICommand&lt;SalesInvoice&gt;</code> (line 50), <code>SelectLotForCartLineCommand : ICommand&lt;bool&gt;</code> (line 63), <code>SelectSerialForCartLineCommand : ICommand&lt;bool&gt;</code> (line 77).

## SaleDiscountWriter.cs {#src-5fd746deb587}

<code>Software/src/GetSeek.Application/Sales/SaleDiscountWriter.cs</code> · 76 lines.

SHA-256: <code>7fc9d8aed3c34c155453c719403907f5f790da6e81faf7bf36e1594c8bf8eecb</code>.

Declarations: <code>SaleDiscountWriter</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5019ad7b3bf7"></span><code>SaleDiscountWriter.RecordLineAsync(IUnitOfWork,Guid,Guid,Guid,string,long,long,bool,decimal,long,Guid,DateTime,CancellationToken)</code><br>9–29 | Min @12; ConfigureAwait @13; AppendAsync @13; ReadAsync @15; Amount @16; Round @25; Max @25 | FROM draft_cart_lines @15; FROM draft_cart_lines @21 |
| <span id="m-67508ddc55b9"></span><code>SaleDiscountWriter.RecordRoundingAsync(IUnitOfWork,Guid,long,string,Guid,DateTime,CancellationToken)</code><br>31–33 | AppendAsync @32 | No extracted literal effects. |
| <span id="m-b8dfa2267394"></span><code>SaleDiscountWriter.ReverseAsync(IUnitOfWork,Guid,Guid,IReadOnlyList&lt;(Guid LineId,decimal OriginalQuantity,decimal ReturnedQuantity,long Eligible,long Credit)&gt;,Guid,DateTime,CancellationToken)</code><br>35–60 | ConfigureAwait @40; ReadAsync @40; ReadBalanceAsync @41; Parse @44; Text @44; NullableGuid @44; FirstOrDefault @47; Sum @50; Amount @50; QuantityValue @50; Min @51; Round @55; AppendAsync @57 | FROM sale_discount_records @40; FROM sale_discount_records @54; FROM sale_return_lines @49 |
| <span id="m-aa3244866b0a"></span><code>SaleDiscountWriter.AppendAsync(IUnitOfWork,Guid,Guid?,SaleDiscountKind,long,long?,string,Guid?,Guid?,string,string,Guid,DateTime,CancellationToken)</code><br>62–74 | ConfigureAwait @65; ReadAsync @65; NullableGuid @66; ExecuteAsync @67; NewGuid @71; BusinessDateAsync @73 | FROM sales_invoices @65; INSERT INTO sale_discount_records @67 |

</details>

## SaleReturnCalculationService.cs {#src-9bf4263959ff}

<code>Software/src/GetSeek.Application/Sales/SaleReturnCalculationService.cs</code> · 50 lines.

SHA-256: <code>9b246922d943bda5ec3d8ce8c4f9df7a4f54cefd8435ce9aa16fe50bd4004de9</code>.

Declarations: <code>ReturnMoneyParts</code> (line 3), <code>SaleReturnCalculationService</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-931f4a732760"></span><code>SaleReturnCalculationService.Allocate(long,IReadOnlyList&lt;(Guid Id,decimal Weight)&gt;)</code><br>12–27 | Any @15; Count @15; Distinct @15; Select @15; nameof @15; Sum @16; ToList @18; Abs @19; Floor @20; Sum @22; ToDictionary @23; Take @24; ThenBy @24; OrderByDescending @24; ToArray @25 | ArgumentException @15 |
| <span id="m-e5f41138c4e1"></span><code>SaleReturnCalculationService.Entitlement(ReturnMoneyParts,decimal,decimal,decimal)</code><br>29–40 | nameof @32; Round @33; Portion @37 | ArgumentOutOfRangeException @32 |
| <span id="m-0554c1d87160"></span><code>SaleReturnCalculationService.ScaleCredit(ReturnMoneyParts,long)</code><br>42–49 | nameof @44; Round @46; Scale @47 | ArgumentOutOfRangeException @44 |

</details>

## SaleReturnCommandHandler.cs {#src-47b58b729be1}

<code>Software/src/GetSeek.Application/Sales/SaleReturnCommandHandler.cs</code> · 334 lines.

SHA-256: <code>400f01b01cefa5e6200deccd975f830e01c02196e2f8621b80ca2c2a383dc0ab</code>.

Declarations: <code>SaleReturnCommandHandler : ICommandHandler&lt;ProcessReturnCommand,SaleReturnResult&gt;, ICommandHandler&lt;ResolveInspectionCommand,InspectionResolutionResult&gt;</code> (line 12), <code>PreparedLine</code> (line 15), <code>PreparedReturn</code> (line 17).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9c8b887bb194"></span><code>SaleReturnCommandHandler.PreviewAsync(ProcessReturnCommand,CancellationToken)</code><br>19–24 | ConfigureAwait @21; PrepareAsync @21; Success(SaleReturnPreview) @22; Failure(SaleReturnPreview) @23 | No extracted literal effects. |
| <span id="m-266a85bbc3b2"></span><code>SaleReturnCommandHandler.PrepareAsync(ProcessReturnCommand,CancellationToken)</code><br>26–130 | IsDefined @28; Count @29; Distinct @29; Select @29; IsNullOrWhiteSpace @29; Bad @30; ConfigureAwait @32; ReadBalanceAsync @32; ReadAsync @36; ToList @39; Select @39; Parse @39; Text @39; Max @39; Amount @39; Allocate @41; FirstOrDefault @47; ToString @47; QuantityValue @49; Sum @55; Parse @55; Min @59; GroupBy @59; Sum @60; IsNullOrEmpty @67; Equals @67; Any @67; Truncate @68; GroupBy @70; Any @72; TryRoundBaseQuantity @73; FirstOrDefault @75; ToString @75; Sum @83; Count @86; First @86; ToString @94; CanRestockAsync @97; NullableGuid @97; GroupBy @102; ToHashSet @104; Select @104; Sum @105; Where @105; Contains @105; Where @107; Sum @108; Sum @116; Add @117; Entitlement @117; Sum @119; Min @125; Success(PreparedReturn) @129 | FROM invoice_cancelled_lines @115; FROM invoice_stock_reservations @56; FROM items @89; FROM refund_lines @50; FROM return_dispositions @81; FROM sale_return_lines @50; FROM sale_returns @50; FROM sales_invoices @36; FROM sales_line_kit_allocations @66; FROM sales_lines @37; FROM serials @93 |
| <span id="m-9ee05f638173"></span><code>SaleReturnCommandHandler.HandleAsync(ProcessReturnCommand,CommandEnvelope&lt;ProcessReturnCommand&gt;,CancellationToken)</code><br>132–203 | ConfigureAwait @134; PrepareAsync @134; Failure(SaleReturnResult) @135; NewGuid @136; HasActivePermissionAsync @138; Equals @143; OpenShiftCurrencyAsync @143; ReadAsync @145; Amount @146; ValidateManualPaymentAsync @148; ExecuteAsync @157; Allocate @159; ToList @159; Select @159; ToDictionary @160; ScaleCredit @160; BusinessDateAsync @162; WriteCreditInvoiceAsync @163; Trim @172; Text @182; WriteDispositionAsync @184; WriteCashMovementAsync @187; Sum @194; Parse @194; QuantityValue @194; ReverseAsync @197; EnqueueAsync @199; ToString @200; Success(SaleReturnResult) @202 | FROM cash_movements @153; FROM refund_lines @193; FROM sale_return_lines @193; FROM sales_lines @189; FROM shifts @145; INSERT INTO sale_return_lines @177; INSERT INTO sale_returns @164; UPDATE sales_invoices @157; UPDATE sales_invoices @196 · AUTH_UNAUTHORIZED @139; SHIFT_NOT_OPEN @144; MONETARY_SCALE_UNRESOLVED @147; INSUFFICIENT_DRAWER_CASH @154; INVOICE_BALANCE_STALE @158 |
| <span id="m-1730ee0bb709"></span><code>SaleReturnCommandHandler.CanRestockAsync(Guid,Guid?,CancellationToken)</code><br>205–213 | ConfigureAwait @207; ReadAsync @207 | FROM items @207; FROM lots @207 |
| <span id="m-fcc6c49c63bf"></span><code>SaleReturnCommandHandler.WriteCreditInvoiceAsync(ProcessReturnCommand,CommandEnvelope&lt;ProcessReturnCommand&gt;,PreparedReturn,Dictionary&lt;Guid,ReturnMoneyParts&gt;,Guid,CancellationToken)</code><br>215–248 | ConfigureAwait @219; ExecuteAsync @219; ToString @228; Sum @229; Min @232; Max @233; NewGuid @245 | FROM sales_invoices @219; FROM sales_lines @238; INSERT INTO sales_invoices @219; INSERT INTO sales_lines @238 |
| <span id="m-4b80ed816bcc"></span><code>SaleReturnCommandHandler.WriteDispositionAsync(ReturnStockAllocation,PreparedLine,Guid,Guid,string,CommandEnvelope&lt;ProcessReturnCommand&gt;,CancellationToken)</code><br>250–282 | First @254; Text @254; ToString @254; Parse @256; NullableGuid @257; IsNullOrWhiteSpace @258; ConfigureAwait @259; ReadAsync @259; QuantityValue @260; Amount @261; NewGuid @262; MoveAsync @265; ExecuteAsync @267; RecordAsync @280; ToString @280 | FROM items @259; INSERT INTO return_dispositions @267; UPDATE serials @276 |
| <span id="m-b85f7f3b55ff"></span><code>SaleReturnCommandHandler.HandleAsync(ResolveInspectionCommand,CommandEnvelope&lt;ResolveInspectionCommand&gt;,CancellationToken)</code><br>284–329 | IsDefined @288; IsNullOrWhiteSpace @288; TryRoundBaseQuantity @289; Failure(InspectionResolutionResult) @290; ConfigureAwait @291; ReadAsync @291; Stale @295; QuantityValue @296; Parse @297; Text @297; NullableGuid @297; IsNullOrEmpty @297; CanRestockAsync @299; GetLotLocationBalanceAsync @306; GetLocationBalanceAsync @307; ExecuteAsync @310; NewGuid @313; MoveAsync @314; RecordAsync @326; Success(InspectionResolutionResult) @328 | FROM return_dispositions @291; FROM serials @303; INSERT INTO return_disposition_resolutions @316; JOIN sale_return_lines @291; JOIN sale_returns @291; UPDATE return_dispositions @310; UPDATE serials @323 · INVALID_RESOLUTION @290; RETURN_STOCK_QUARANTINED @300 |
| <span id="m-080e71d531f1"></span><code>SaleReturnCommandHandler.Stale()</code><br>331–331 | Failure(InspectionResolutionResult) @331 | RETURN_DISPOSITION_STALE @331 |
| <span id="m-5eecf696823e"></span><code>SaleReturnCommandHandler.Bad(string,string)</code><br>332–332 | Failure(PreparedReturn) @332 | No extracted literal effects. |

</details>

## SaleReturnCommands.cs {#src-69127d19034a}

<code>Software/src/GetSeek.Application/Sales/SaleReturnCommands.cs</code> · 22 lines.

SHA-256: <code>6b5a05ce49d7d0ac0e3ac3d4f518ae186326478099fda1b9838da328c70dc477</code>.

Declarations: <code>ProcessReturnCommand : ICommand&lt;SaleReturnResult&gt;</code> (line 7), <code>ResolveInspectionCommand : ICommand&lt;InspectionResolutionResult&gt;</code> (line 17).

## SaleStockAllocationPlanner.cs {#src-ccc9ba71e2d3}

<code>Software/src/GetSeek.Application/Sales/SaleStockAllocationPlanner.cs</code> · 90 lines.

SHA-256: <code>d8467506c0d625b76ae34fc47a2efc943a8fcdd38937dc20523ad6b5ae0f1c47</code>.

Declarations: <code>SaleLeafDemand</code> (line 11), <code>SaleLeafAllocation</code> (line 12), <code>SaleStockAllocationPlanner</code> (line 14), <code>Bucket</code> (line 16).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-985b96b7d6dd"></span><code>SaleStockAllocationPlanner.PlanAsync(DbConnection,DbTransaction?,Guid,Dictionary&lt;Guid,List&lt;SaleLeafDemand&gt;&gt;,DateTime,CancellationToken)</code><br>21–87 | GroupBy @25; Where @25; SelectMany @25; ConfigureAwait @27; CurrentCostAsync @27; ReadAsync @28; Text @29; StartsWith @29; Fail @32; Parse @36; NullableGuid @36; IsNullOrEmpty @37; TryParse @39; SerialIsReservedAsync @43; Add @57; Sum @59; Sum @59; Where @60; GetLotLocationBalanceAsync @62; Sum @63; TryGetValue @74; Add @74; Where @76; Min @78; Success(Dictionary&lt;Guid,List&lt;SaleLeafAllocation&gt;&gt;, Guid, List&lt;SaleLeafAllocation&gt;, SaleLeafAllocation) @86 | FROM items @28; FROM lots @54; FROM pending_allocations @31; FROM serials @46 |
| <span id="m-c9150591e539"></span><code>SaleStockAllocationPlanner.Fail(string,string)</code><br>89–89 | Failure(Dictionary&lt;Guid,List&lt;SaleLeafAllocation&gt;&gt;, Guid, List&lt;SaleLeafAllocation&gt;, SaleLeafAllocation) @89 | No extracted literal effects. |

</details>

## ShippingCommands.cs {#src-4772ecb3181e}

<code>Software/src/GetSeek.Application/Sales/ShippingCommands.cs</code> · 241 lines.

SHA-256: <code>381096aeae46d7cc0cb308ee6785c4506cca37241e1dcb98459a977471f1077e</code>.

Declarations: <code>OrderDraftStockSelection</code> (line 14), <code>OrderDraftLine</code> (line 15), <code>SaveOrderDraftCommand : ICommand&lt;Guid&gt;</code> (line 16), <code>DispatchShipmentCommand : ICommand&lt;Guid&gt;</code> (line 20), <code>ConfirmShipmentDeliveryCommand : ICommand&lt;bool&gt;</code> (line 25), <code>UpdateShipmentTrackingCommand : ICommand&lt;bool&gt;</code> (line 30), <code>ReplaceInvoiceReservationCommand : ICommand&lt;bool&gt;</code> (line 33), <code>ShippingCommandHandler : ICommandHandler&lt;SaveOrderDraftCommand, Guid&gt;, ICommandHandler&lt;DispatchShipmentCommand, Guid&gt;, ICommandHandler&lt;ConfirmShipmentDeliveryCommand, bool&gt;, ICommandHandler&lt;UpdateShipmentTrackingCommand,bool&gt;, ICommandHandler&lt;ReplaceInvoiceReservationCommand,bool&gt;</code> (line 36).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5cc732b936bf"></span><code>ShippingCommandHandler.HandleAsync(SaveOrderDraftCommand,CommandEnvelope&lt;SaveOrderDraftCommand&gt;,CancellationToken)</code><br>40–116 | Any @44; Count @44; Distinct @44; Select @44; Bad @44; ConfigureAwait @45; ReadAsync @45; NewGuid @49; ExecuteAsync @54; Text @54; HasActivePermissionAsync @65; HandleAsync @70; IsNullOrWhiteSpace @73; Trim @75; ResolveFactorAsync @78; Parse @80; HandleAsync @81; Split @84; DecomposeToLeavesAsync @94; Any @97; Trim @100; Split @104; Serialize @114; Success(Guid) @115 | DELETE FROM draft_cart_lines @54; DELETE FROM pending_allocations @54; FROM draft_carts @52; FROM items @77; FROM items @92; FROM lots @100; FROM lots @75; FROM shifts @45; FROM third_parties @47; INSERT INTO draft_carts @56; INSERT INTO invoice_draft_options @114; UPDATE draft_carts @54 |
| <span id="m-770a4dedaff2"></span><code>ShippingCommandHandler.HandleAsync(DispatchShipmentCommand,CommandEnvelope&lt;DispatchShipmentCommand&gt;,CancellationToken)</code><br>118–192 | IsNullOrWhiteSpace @122; Any @122; Count @122; Distinct @122; Select @122; Bad @123; ConfigureAwait @124; ReadAsync @124; Amount @125; Parse @131; Text @131; Parse @132; NullableGuid @132; ReadLotAsync @135; GetLocationBalanceAsync @138; ReadSerialAsync @142; Add @145; GroupBy @147; Select @147; Sum @149; Where @151; GetLotLocationBalanceAsync @152; Sum @152; Select @154; Where @154; ToList @157; GroupBy @157; Sum @162; Where @162; Any @162; ToString @162; NewGuid @167; ExecuteAsync @168; Trim @169; Trim @169; Trim @169; MoveAsync @173; Success(Guid) @191 | FROM invoice_fulfillment @124; FROM invoice_stock_reservations @129; FROM invoice_stock_reservations @156; INSERT INTO sales_line_kit_allocations @177; INSERT INTO shipment_allocations @183; INSERT INTO shipments @168; JOIN items @129; UPDATE invoice_fulfillment @190; UPDATE invoice_stock_reservations @186; UPDATE serials @188 |
| <span id="m-ad068d3e8f16"></span><code>ShippingCommandHandler.HandleAsync(ConfirmShipmentDeliveryCommand,CommandEnvelope&lt;ConfirmShipmentDeliveryCommand&gt;,CancellationToken)</code><br>194–204 | IsNullOrWhiteSpace @197; Failure(bool) @197; ConfigureAwait @198; ExecuteAsync @198; NewGuid @202; Trim @202; Success(bool) @203 | INSERT INTO shipment_events @201; UPDATE shipments @198 · REASON_REQUIRED @197; SHIPMENT_STALE @200 |
| <span id="m-af9bb6bb7459"></span><code>ShippingCommandHandler.HandleAsync(UpdateShipmentTrackingCommand,CommandEnvelope&lt;UpdateShipmentTrackingCommand&gt;,CancellationToken)</code><br>205–213 | IsNullOrWhiteSpace @207; Failure(bool) @207; ConfigureAwait @209; ExecuteAsync @209; Trim @209; Trim @209; NewGuid @211; Serialize @211; Success(bool) @212 | INSERT INTO commercial_shipping_events @211 · REASON_REQUIRED @207; SHIPMENT_STALE @210 |
| <span id="m-444be3598ac4"></span><code>ShippingCommandHandler.HandleAsync(ReplaceInvoiceReservationCommand,CommandEnvelope&lt;ReplaceInvoiceReservationCommand&gt;,CancellationToken)</code><br>214–239 | IsNullOrWhiteSpace @217; Failure(bool) @217; ConfigureAwait @218; ReadAsync @218; Amount @219; Parse @220; Text @220; Parse @220; StartsWith @221; Trim @223; NullableGuid @224; ReadLotAsync @225; GetLotLocationBalanceAsync @226; Trim @230; Equals @230; ReadSerialAsync @231; SerialIsReservedAsync @233; ExecuteAsync @237; Success(bool) @238 | FROM invoice_stock_reservations @218; FROM lots @223; FROM pending_allocations @232; FROM serials @234; JOIN invoice_fulfillment @218; JOIN items @218; UPDATE invoice_fulfillment @237; UPDATE invoice_stock_reservations @237 · REASON_REQUIRED @217; RESERVATION_STALE @219; LOT_REQUIRED @223; NO_CHANGE @224; LOT_UNAVAILABLE @226; SERIAL_REQUIRED @230; SERIAL_UNAVAILABLE @233; SUBSTITUTION_NOT_NEEDED @236 |
| <span id="m-242c2be7fc9c"></span><code>ShippingCommandHandler.Bad(string,string)</code><br>240–240 | Failure(Guid) @240 | No extracted literal effects. |

</details>

## StaleCartPriceReview.cs {#src-f9958eaccdf4}

<code>Software/src/GetSeek.Application/Sales/StaleCartPriceReview.cs</code> · 179 lines.

SHA-256: <code>2ecd50e4756a0f94f9e76d9b76ec403b4c366e75cc320267e94b24a2bd0222dd</code>.

Declarations: <code>StaleCartPriceReviewLine</code> (line 11), <code>StaleCartPriceReview</code> (line 15), <code>ReviewStaleCartPricesCommand : ICommand&lt;StaleCartPriceReview&gt;</code> (line 21), <code>AcceptStaleCartPriceReviewCommand : ICommand&lt;StaleCartPriceReview&gt;</code> (line 26), <code>StaleCartPriceReviewCommandHandler : ICommandHandler&lt;ReviewStaleCartPricesCommand, StaleCartPriceReview&gt;, ICommandHandler&lt;AcceptStaleCartPriceReviewCommand, StaleCartPriceReview&gt;</code> (line 32), <code>PersistedLine</code> (line 36), <code>ResolvedLine</code> (line 40).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d9c53582c750"></span><code>StaleCartPriceReviewCommandHandler.HandleAsync(ReviewStaleCartPricesCommand,CommandEnvelope&lt;ReviewStaleCartPricesCommand&gt;,CancellationToken)</code><br>42–50 | ConfigureAwait @45; BuildReviewAsync @45; Failure(StaleCartPriceReview) @48; Success(StaleCartPriceReview) @49 | No extracted literal effects. |
| <span id="m-4ee802676bed"></span><code>StaleCartPriceReviewCommandHandler.HandleAsync(AcceptStaleCartPriceReviewCommand,CommandEnvelope&lt;AcceptStaleCartPriceReviewCommand&gt;,CancellationToken)</code><br>52–87 | ConfigureAwait @55; BuildReviewAsync @55; Failure(StaleCartPriceReview) @58; Equals @61; CreateCommand @66; Add @70; ToString @70; ToString @71; ExecuteNonQueryAsync @72; ToString @81; ToString @82; ExecuteNonQueryAsync @83; Success(StaleCartPriceReview) @86 | UPDATE draft_cart_lines @79; UPDATE draft_carts @69 · CART_REVIEW_NO_CHANGES @60; CART_REVIEW_STALE @62; CART_REVISION_STALE @73; CART_LINE_STALE @84 |
| <span id="m-12f239f1bd12"></span><code>StaleCartPriceReviewCommandHandler.BuildReviewAsync(Guid,int,Guid,Guid?,CancellationToken)</code><br>89–156 | CreateCommand @94; Add @97; ToString @97; ConfigureAwait @98; ExecuteReaderAsync @98; ReadAsync @99; GetInt32 @100; ExecuteReaderAsync @115; Add @118; Parse @118; GetString @118; ParseDecimal @119; GetInt64 @119; GetDecimal @120; ToString @133; ExecuteReaderAsync @134; IsDBNull @137; Equals @139; ResolveAsync @145; Add @150; Fingerprint @154; ToArray @155; Select @155 | FROM draft_cart_lines @108; FROM draft_carts @96; FROM items @132 |
| <span id="m-79b78a9f6cef"></span><code>StaleCartPriceReviewCommandHandler.Fingerprint(Guid,int,IReadOnlyList&lt;ResolvedLine&gt;)</code><br>158–172 | Append @160; ToString @160; OrderBy @161; Append @162; ToString @162; ToString @164; ToString @165; ToString @166; ToString @167; ToString @168; ToHexStringLower @171; HashData @171; GetBytes @171; ToString @171 | No extracted literal effects. |
| <span id="m-f25efddc3c40"></span><code>StaleCartPriceReviewCommandHandler.ParseDecimal(string)</code><br>174–175 | TryParse @174 | No extracted literal effects. |
| <span id="m-4663914ce693"></span><code>StaleCartPriceReviewCommandHandler.Add(DbCommand,string,object)</code><br>177–178 | CreateParameter @178; Add @178 | No extracted literal effects. |

</details>

## SupervisorElevationGuard.cs {#src-c94e4dec1b49}

<code>Software/src/GetSeek.Application/Sales/SupervisorElevationGuard.cs</code> · 49 lines.

SHA-256: <code>15e693acc97367f4ef60cad0bd08572acae8579910d29d7325e9d715175ca790</code>.

Declarations: <code>SupervisorElevationGuard</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-13a1b0e8ad46"></span><code>SupervisorElevationGuard.IsAuthorizedAsync(DbConnection,DbTransaction?,Guid?,CancellationToken)</code><br>9–40 | CreateCommand @14; AddParameter @37; ToString @37; ToInt32 @39; ConfigureAwait @39; ExecuteScalarAsync @39 | FROM user_permission_overrides @16; FROM user_roles @16; FROM users @16; JOIN role_permissions @16 |
| <span id="m-21f16b3116d5"></span><code>SupervisorElevationGuard.AddParameter(DbCommand,string,object)</code><br>42–48 | CreateParameter @44; Add @47 | No extracted literal effects. |

</details>

## SupplierReturnCommands.cs {#src-0bb0722d3c5e}

<code>Software/src/GetSeek.Application/Sales/SupplierReturnCommands.cs</code> · 122 lines.

SHA-256: <code>b22552e1172fbae7971fbb00edb8870e12f02ad64d97076a38fc42d5da6d6c80</code>.

Declarations: <code>ReturnSupplierGoodsCommand : ICommand&lt;Guid&gt;</code> (line 10), <code>ReceiveSupplierRefundCommand : ICommand&lt;Guid&gt;</code> (line 12), <code>ConfirmSupplierReturnDeliveryCommand : ICommand&lt;bool&gt;</code> (line 14), <code>ReverseMoneyTransferCommand : ICommand&lt;Guid&gt;</code> (line 16), <code>CancelSupplierInvoiceLinesCommand : ICommand&lt;Guid&gt;</code> (line 19), <code>PurchaseAndMoneyCommandHandler : ICommandHandler&lt;CancelSupplierInvoiceLinesCommand,Guid&gt;, ICommandHandler&lt;ReturnSupplierGoodsCommand,Guid&gt;, ICommandHandler&lt;ReceiveSupplierRefundCommand,Guid&gt;, ICommandHandler&lt;ConfirmSupplierReturnDeliveryCommand,bool&gt;, ICommandHandler&lt;ReverseMoneyTransferCommand,Guid&gt;</code> (line 22).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-6a20b216316a"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(CancelSupplierInvoiceLinesCommand,CommandEnvelope&lt;CancelSupplierInvoiceLinesCommand&gt;,CancellationToken)</code><br>24–46 | Count @27; Distinct @27; Select @27; Any @27; IsNullOrWhiteSpace @27; Bad @27; ConfigureAwait @28; ReadAsync @28; Amount @28; Sum @35; Quantity @35; Sum @36; Entitlement @38; Sum @38; Add @39; NewGuid @41; ExecuteAsync @41; Trim @41; Text @44; Sum @44; Success(Guid) @45 | FROM purchase_receipt_lines @34; FROM purchase_receipt_lines @44; FROM supplier_invoice_credit_lines @33; FROM supplier_invoice_credit_lines @44; FROM supplier_invoice_lines @32; FROM supplier_invoice_lines @43; FROM supplier_invoices @28; FROM supplier_return_lines @37; INSERT INTO supplier_invoice_credit_lines @42; INSERT INTO supplier_invoice_credits @41; UPDATE supplier_invoices @45 |
| <span id="m-96a310a3dffd"></span><code>PurchaseAndMoneyCommandHandler.Quantity(Dictionary&lt;string,object?&gt;,string)</code><br>47–47 | Parse @47; Text @47 | No extracted literal effects. |
| <span id="m-bc4d2643eb60"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(ReturnSupplierGoodsCommand,CommandEnvelope&lt;ReturnSupplierGoodsCommand&gt;,CancellationToken)</code><br>48–98 | Count @51; Distinct @51; Select @51; IsNullOrWhiteSpace @51; Bad @51; ConfigureAwait @52; HasActivePermissionAsync @52; ReadAsync @53; Amount @54; NewGuid @55; Any @60; Parse @61; Text @61; Quantity @61; Sum @65; Sum @65; Sum @66; Trim @70; StartsWith @71; Trim @72; ReadSerialAsync @74; SerialIsHeldOrReservedAsync @74; NullableGuid @76; Sum @81; Where @81; Sum @82; Sum @82; GetLotLocationBalanceAsync @84; GetLocationBalanceAsync @84; MoveAsync @86; Trim @86; ExecuteAsync @87; Add @88; Entitlement @91; Sum @91; Add @92; Trim @94; Trim @94; Success(Guid) @97 | FROM lots @72; FROM purchase_receipt_lines @62; FROM serials @76; FROM stock_movements @79; FROM supplier_invoice_credit_lines @64; FROM supplier_invoice_lines @59; FROM supplier_invoices @53; FROM supplier_return_allocations @80; FROM supplier_return_lines @63; INSERT INTO supplier_return_allocations @96; INSERT INTO supplier_return_lines @96; INSERT INTO supplier_returns @94; JOIN items @59; JOIN purchase_receipt_lines @79; JOIN supplier_return_lines @80; UPDATE serials @87; UPDATE supplier_invoices @97 |
| <span id="m-c6a36def9602"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(ReceiveSupplierRefundCommand,CommandEnvelope&lt;ReceiveSupplierRefundCommand&gt;,CancellationToken)</code><br>99–106 | ConfigureAwait @101; ReadAsync @101; Amount @102; Bad @102; AccountAsync @103; Text @103; NewGuid @104; PostAsync @104; ExecuteAsync @105; Success(Guid) @105 | FROM supplier_invoice_credits @101; FROM supplier_invoices @101; FROM supplier_payments @101; FROM supplier_refunds @101; FROM supplier_returns @101; INSERT INTO supplier_refunds @105; UPDATE supplier_invoices @105 |
| <span id="m-56e88b5a3a34"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(ConfirmSupplierReturnDeliveryCommand,CommandEnvelope&lt;ConfirmSupplierReturnDeliveryCommand&gt;,CancellationToken)</code><br>107–112 | IsNullOrWhiteSpace @109; Failure(bool) @109; ConfigureAwait @110; ExecuteAsync @110; NewGuid @111; Success(bool) @111 | INSERT INTO commercial_shipping_events @111; UPDATE supplier_returns @110 · REASON_REQUIRED @109; RETURN_STALE @110 |
| <span id="m-66868fbc9384"></span><code>PurchaseAndMoneyCommandHandler.HandleAsync(ReverseMoneyTransferCommand,CommandEnvelope&lt;ReverseMoneyTransferCommand&gt;,CancellationToken)</code><br>113–121 | ConfigureAwait @115; ReadAsync @115; Bad @116; NewGuid @118; OrderByDescending @118; Amount @118; AccountAsync @119; Parse @119; Text @119; PostAsync @119; Success(Guid) @120 | FROM money_events @115; FROM money_events @117 |

</details>

## CreateUserWithPersonCommand.cs {#src-96eb7e988fa6}

<code>Software/src/GetSeek.Application/Security/CreateUserWithPersonCommand.cs</code> · 45 lines.

SHA-256: <code>387802618d367fe594f1b1c4ce8ab9afc2d5c10179c5af26958ac9d10f8bae50</code>.

Declarations: <code>CreateUserWithPersonCommand : ICommand&lt;CreateUserWithPersonResult&gt;, ISanitizedAuditPayload</code> (line 7), <code>CreateUserWithPersonResult</code> (line 42).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a9998ae44f0e"></span><code>CreateUserWithPersonCommand.GetSanitizedAuditPayload()</code><br>28–39 | Serialize @28; IsNullOrEmpty @38 | No extracted literal effects. |

</details>

## IPermissionResolver.cs {#src-510f301dcba8}

<code>Software/src/GetSeek.Application/Security/IPermissionResolver.cs</code> · 22 lines.

SHA-256: <code>3a9a5d74556310a5691cde17f542f17d66c416a2f2d6a45a19da8465b0108a33</code>.

Declarations: <code>UserPermissionEvaluation</code> (line 5), <code>IPermissionResolver</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-07c2fd8fd58a"></span><code>IPermissionResolver.ResolveEffectivePermissionsAsync(DbConnection,Guid,CancellationToken)</code><br>17–17 | — | No extracted literal effects. |
| <span id="m-f03eb6735225"></span><code>IPermissionResolver.HasPermissionAsync(DbConnection,Guid,string,CancellationToken)</code><br>18–18 | — | No extracted literal effects. |
| <span id="m-ecb8f652856a"></span><code>IPermissionResolver.HasPermissionAsync(DbConnection,DbTransaction,Guid,string,CancellationToken)</code><br>19–20 | HasPermissionAsync @20 | No extracted literal effects. |
| <span id="m-bbf8cd84d02c"></span><code>IPermissionResolver.GetSecurityRevisionAsync(DbConnection,Guid,CancellationToken)</code><br>21–21 | — | No extracted literal effects. |

</details>

## SetUserPermissionOverrideCommands.cs {#src-c7905080003f}

<code>Software/src/GetSeek.Application/Security/SetUserPermissionOverrideCommands.cs</code> · 162 lines.

SHA-256: <code>a1912334f65e60f92657ae9f0b32fac39a622f776ef881368a8b04a0cf239c01</code>.

Declarations: <code>SetUserPermissionOverrideCommand : ICommand&lt;bool&gt;</code> (line 9), <code>SetUserPermissionOverrideCommandHandler : ICommandHandler&lt;SetUserPermissionOverrideCommand, bool&gt;</code> (line 19).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9a1f02732077"></span><code>SetUserPermissionOverrideCommandHandler.HandleAsync(SetUserPermissionOverrideCommand,CommandEnvelope&lt;SetUserPermissionOverrideCommand&gt;,CancellationToken)</code><br>29–153 | ToString @36; CreateCommand @39; CreateParameter @50; ToString @52; Add @53; ToInt64 @55; ConfigureAwait @55; ExecuteScalarAsync @55; Failure(bool) @58; Contains @69; Equals @75; CreateParameter @89; Add @92; ToString @96; ExecuteScalarAsync @99; AddParam @119; ExecuteNonQueryAsync @124; ExecuteNonQueryAsync @133; ExecuteNonQueryAsync @149; Success(bool) @152 | DELETE FROM user_permission_overrides @130; FROM users @42; FROM users @79; INSERT INTO user_permission_overrides @111; INSERT INTO user_security_revisions @140; JOIN roles @42; JOIN user_permission_overrides @79; JOIN user_roles @42; JOIN user_roles @79 · AUTH_UNAUTHORIZED @58; SELF_ESCALATION_DENIED @65; PROTECTED_PERMISSION_DENIED @71; LAST_ADMIN_PROTECTION @102 |
| <span id="m-4d4977103016"></span><code>SetUserPermissionOverrideCommandHandler.AddParam(DbCommand,string,object)</code><br>155–161 | CreateParameter @157; Add @160 | No extracted literal effects. |

</details>

## UserCommandHandler.cs {#src-12dc7e3f2868}

<code>Software/src/GetSeek.Application/Security/UserCommandHandler.cs</code> · 764 lines.

SHA-256: <code>8adca55977efc077773864641fc14751fe11db9e145ebed6c4ffae57a8e6ce6e</code>.

Declarations: <code>UserCommandHandler : ICommandHandler&lt;ProvisionInitialAdminCommand, User&gt;, ICommandHandler&lt;CreateUserCommand, User&gt;, ICommandHandler&lt;UpdateUserQuickPinCommand, bool&gt;, ICommandHandler&lt;CreateUserWithPersonCommand, CreateUserWithPersonResult&gt;</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e25aed584719"></span><code>UserCommandHandler.AddParam(DbCommand,string,object?)</code><br>18–24 | CreateParameter @20; Add @23 | No extracted literal effects. |
| <span id="m-2ea4de08df45"></span><code>UserCommandHandler.HandleAsync(ProvisionInitialAdminCommand,CommandEnvelope&lt;ProvisionInitialAdminCommand&gt;,CancellationToken)</code><br>26–115 | CreateCommand @35; ConfigureAwait @39; ExecuteScalarAsync @39; Failure(User) @42; Trim @47; IsNullOrWhiteSpace @51; IsValidPin @61; EnsureDefaultRolesAndPermissionsAsync @67; HashPin @70; NewGuid @72; AddParam @83; ToString @83; ToString @87; ExecuteNonQueryAsync @89; ExecuteNonQueryAsync @98; GetAllAdminPermissions @111; Success(User) @114 | FROM users @38; INSERT INTO user_roles @96; INSERT INTO users @79 · SETUP_ALREADY_COMPLETED @42; INVALID_USERNAME @53; INVALID_DISPLAY_NAME @58; INVALID_QUICK_PIN @63 |
| <span id="m-659137d5ea8e"></span><code>UserCommandHandler.HandleAsync(CreateUserCommand,CommandEnvelope&lt;CreateUserCommand&gt;,CancellationToken)</code><br>117–224 | Trim @125; IsValidRole @131; Failure(User) @133; ConfigureAwait @140; IsUserInRoleAsync @140; IsNullOrWhiteSpace @147; IsValidPin @157; CreateCommand @163; AddParam @167; ExecuteScalarAsync @168; EnsureDefaultRolesAndPermissionsAsync @176; HashPin @178; NewGuid @180; ToString @190; ToString @195; ToString @196; ExecuteNonQueryAsync @198; ExecuteNonQueryAsync @207; GetPermissionsForRole @220; Success(User) @223 | FROM users @166; INSERT INTO user_roles @204; INSERT INTO users @186 · INVALID_ROLE @133; PRIVILEGE_ESCALATION_DENIED @143; INVALID_USERNAME @149; INVALID_DISPLAY_NAME @154; INVALID_QUICK_PIN @159; USERNAME_ALREADY_EXISTS @171 |
| <span id="m-227fa8a0bc5d"></span><code>UserCommandHandler.HandleAsync(CreateUserWithPersonCommand,CommandEnvelope&lt;CreateUserWithPersonCommand&gt;,CancellationToken)</code><br>226–440 | ToString @234; ConfigureAwait @237; HasPermissionAsync @237; Failure(CreateUserWithPersonResult) @240; Trim @244; IsValidRole @249; IsUserInRoleAsync @256; IsNullOrWhiteSpace @263; IsValidPin @273; CreateCommand @278; AddParam @282; ExecuteScalarAsync @283; ToLowerInvariant @291; FromDateTime @297; IsNullOrEmpty @304; IsMatch @304; ToUpperInvariant @309; GenerateUniquePersonCodeAsync @312; ExecuteScalarAsync @320; EnsureDefaultRolesAndPermissionsAsync @338; HashPin @339; NewGuid @340; ToString @348; ToString @354; ExecuteNonQueryAsync @355; ExecuteNonQueryAsync @364; ToString @382; ToString @386; ToString @387; ToString @391; ExecuteNonQueryAsync @394; Trim @401; Clamp @402; ToString @415; ExecuteNonQueryAsync @424; GetPermissionsForRole @436; Success(CreateUserWithPersonResult) @439 | FROM person_records @318; FROM users @281; INSERT INTO person_records @372; INSERT INTO salary_agreements @407; INSERT INTO user_roles @361; INSERT INTO users @345 · AUTH_UNAUTHORIZED @240; INVALID_ROLE @251; PRIVILEGE_ESCALATION_DENIED @259; INVALID_USERNAME @265; INVALID_DISPLAY_NAME @270; INVALID_QUICK_PIN @275; USERNAME_ALREADY_EXISTS @286; INVALID_PERSON_KIND @294; INVALID_EMPLOYMENT_DATES @300; INVALID_PAYROLL_MONTH @306; PERSON_CODE_ALREADY_EXISTS @323; INVALID_SALARY_AMOUNT @329; INVALID_SALARY_AMOUNT @334 |
| <span id="m-8648b311bf10"></span><code>UserCommandHandler.IsValidPin(string)</code><br>442–443 | All @443 | No extracted literal effects. |
| <span id="m-e4f8dbb4adb2"></span><code>UserCommandHandler.HandleAsync(UpdateUserQuickPinCommand,CommandEnvelope&lt;UpdateUserQuickPinCommand&gt;,CancellationToken)</code><br>445–511 | Trim @453; All @454; Failure(bool) @456; ConfigureAwait @461; IsUserInRoleAsync @461; CreateCommand @472; AddParam @476; ToString @476; ExecuteScalarAsync @477; HashPin @485; ExecuteNonQueryAsync @493; ExecuteNonQueryAsync @503; Success(bool) @510 | DELETE FROM sign_in_lockout_state @501; FROM users @475; UPDATE users @490 · INVALID_QUICK_PIN @456; PRIVILEGE_ESCALATION_DENIED @467; USER_NOT_FOUND @480 |
| <span id="m-4978232c8fe4"></span><code>UserCommandHandler.IsValidRole(string,string)</code><br>513–533 | Equals @515 | No extracted literal effects. |
| <span id="m-6dfb01dd06c6"></span><code>UserCommandHandler.IsUserInRoleAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>535–546 | CreateCommand @539; AddParam @542; ToString @542; ConfigureAwait @544; ExecuteScalarAsync @544 | FROM user_roles @541 |
| <span id="m-e7ea0d1d59fd"></span><code>UserCommandHandler.GetAllAdminPermissions()</code><br>548–608 | — | No extracted literal effects. |
| <span id="m-5ece0149cecb"></span><code>UserCommandHandler.GetPermissionsForRole(string)</code><br>610–645 | GetAllAdminPermissions @614 | No extracted literal effects. |
| <span id="m-508e00e19780"></span><code>UserCommandHandler.EnsureDefaultRolesAndPermissionsAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>647–693 | CreateCommand @652; AddParam @655; ConfigureAwait @657; ExecuteNonQueryAsync @657; GetAllAdminPermissions @660 | FROM roles @686; INSERT OR IGNORE INTO permissions @665; INSERT OR IGNORE INTO role_permissions @676; INSERT OR IGNORE INTO role_permissions @686; INSERT OR IGNORE INTO roles @654 |
| <span id="m-1c2e462024a0"></span><code>UserCommandHandler.HasPermissionAsync(DbConnection,DbTransaction?,IPermissionResolver?,Guid,string,CancellationToken)</code><br>695–732 | ConfigureAwait @706; HasPermissionAsync @706; CreateCommand @710; AddParam @713; ToString @713; ExecuteScalarAsync @715; ToInt64 @718; ExecuteScalarAsync @730 | FROM role_permissions @724; FROM user_permission_overrides @712; JOIN user_roles @724 |
| <span id="m-8769a42953c7"></span><code>UserCommandHandler.GenerateUniquePersonCodeAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>734–763 | CreateCommand @736; ConfigureAwait @740; ExecuteReaderAsync @740; ReadAsync @742; IsDBNull @744; Add @746; GetString @746; StartsWith @754; TryParse @755 | FROM person_records @738 |

</details>

## UserCommands.cs {#src-2442f8313db3}

<code>Software/src/GetSeek.Application/Security/UserCommands.cs</code> · 67 lines.

SHA-256: <code>fcccc816be4d323c91d5f1c71426e962bc1267cf27a7c4aa8eecb0c838f821da</code>.

Declarations: <code>ProvisionInitialAdminCommand : ICommand&lt;User&gt;, ISanitizedAuditPayload</code> (line 7), <code>CreateUserCommand : ICommand&lt;User&gt;, ISanitizedAuditPayload</code> (line 26), <code>UpdateUserQuickPinCommand : ICommand&lt;bool&gt;, ISanitizedAuditPayload</code> (line 51).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e0dac97542d0"></span><code>ProvisionInitialAdminCommand.GetSanitizedAuditPayload()</code><br>15–23 | Serialize @17; IsNullOrEmpty @21 | No extracted literal effects. |
| <span id="m-74908d9703c9"></span><code>CreateUserCommand.GetSanitizedAuditPayload()</code><br>37–48 | Serialize @39; IsNullOrEmpty @46 | No extracted literal effects. |
| <span id="m-d9cf7490e4f6"></span><code>UpdateUserQuickPinCommand.GetSanitizedAuditPayload()</code><br>58–65 | Serialize @60; IsNullOrEmpty @63 | No extracted literal effects. |

</details>

## ApplySettingsCommand.cs {#src-a56b2ff06b35}

<code>Software/src/GetSeek.Application/Settings/ApplySettingsCommand.cs</code> · 20 lines.

SHA-256: <code>d0388b06310ce5f19ab0a2bb7ff6653504a759a5220be7ac9ff24135e1e65d3f</code>.

Declarations: <code>ApplySettingsCommand : ICommand&lt;bool&gt;</code> (line 5).

## ApplySettingsCommandHandler.cs {#src-87133587a4b1}

<code>Software/src/GetSeek.Application/Settings/ApplySettingsCommandHandler.cs</code> · 177 lines.

SHA-256: <code>18a23c0c4e2ed073b2e9d9832739f3e5cc9f7c713c7f246ce0a1c0e2f2be588e</code>.

Declarations: <code>ApplySettingsCommandHandler : ICommandHandler&lt;ApplySettingsCommand, bool&gt;</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0875a2f0acb6"></span><code>ApplySettingsCommandHandler.HandleAsync(ApplySettingsCommand,CommandEnvelope&lt;ApplySettingsCommand&gt;,CancellationToken)</code><br>9–168 | IsNullOrWhiteSpace @14; Failure(bool) @15; CreateCommand @31; AddParam @37; ToString @37; ConfigureAwait @38; ExecuteScalarAsync @38; ExecuteScalarAsync @51; ToString @81; ExecuteNonQueryAsync @83; ExecuteScalarAsync @92; ToString @95; IsNullOrEmpty @99; Equals @99; ExecuteScalarAsync @108; ToInt64 @111; ExecuteScalarAsync @125; Success(bool) @167 | FROM business_profile_config @91; FROM draft_carts @107; FROM items @45; FROM restaurant_orders @128; FROM sales_invoices @45; FROM shifts @45; FROM stock_movements @45; FROM store_config @45; FROM users @35; JOIN user_roles @35; UPDATE business_profile_config @151; UPDATE store_config @58 · INVALID_STORE_NAME @15; INVALID_TAX_RATE @18; INVALID_DECIMAL_PLACES @21; INVALID_PRICE_LEVEL_COUNT @24; AUTH_UNAUTHORIZED @39; MONETARY_IDENTITY_IN_USE @52; OPEN_WORK_EXISTS @140 |
| <span id="m-1f6cdbb379ee"></span><code>ApplySettingsCommandHandler.AddParam(System.Data.Common.DbCommand,string,object)</code><br>170–176 | CreateParameter @172; Add @175 | No extracted literal effects. |

</details>

## CashFinancialSettingsCommands.cs {#src-dc0f9914df25}

<code>Software/src/GetSeek.Application/Settings/CashFinancialSettingsCommands.cs</code> · 133 lines.

SHA-256: <code>016d31abcb093974116014b66610aaa49fe5e9aec01bd48a94a816e0b9e3da79</code>.

Declarations: <code>UpdateCashFinancialSettingsCommand : ICommand&lt;CashFinancialSettings&gt;</code> (line 8), <code>UpdateCashFinancialSettingsCommandHandler : ICommandHandler&lt;UpdateCashFinancialSettingsCommand, CashFinancialSettings&gt;</code> (line 22).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-111036292e3c"></span><code>UpdateCashFinancialSettingsCommandHandler.HandleAsync(UpdateCashFinancialSettingsCommand,CommandEnvelope&lt;UpdateCashFinancialSettingsCommand&gt;,CancellationToken)</code><br>25–124 | Failure(CashFinancialSettings) @31; Contains @32; Equals @42; CreateCommand @50; ToInt32 @54; ConfigureAwait @54; ExecuteScalarAsync @54; ToInt64 @63; ExecuteScalarAsync @63; ExecuteScalarAsync @79; Add @99; ToLowerInvariant @100; Trim @100; Trim @102; ToString @104; Trim @105; Trim @106; Trim @107; ToString @109; ExecuteNonQueryAsync @110; Success(CashFinancialSettings) @113 | FROM draft_carts @62; FROM restaurant_orders @67; FROM store_config @53; FROM store_config @78; UPDATE store_config @84 · INVALID_CASH_DISPLAY_DECIMALS @31; INVALID_CASH_ROUNDING_MODE @33; INVALID_CASH_ROUNDING_TIE_RULE @35; INVALID_CASH_ROUNDING_INCREMENT @37; INVALID_SERVICE_CHARGE @39; INVALID_SERVICE_CHARGE_SCOPE @41; INVALID_SERVICE_CHARGE_BASIS @43; INVALID_SERVICE_CHARGE_TAX_MODE @45; CASH_DISPLAY_PRECISION_EXCEEDED @57; OPEN_WORK_EXISTS @72 |
| <span id="m-faff6bce2618"></span><code>UpdateCashFinancialSettingsCommandHandler.Add(System.Data.Common.DbCommand,string,object)</code><br>126–132 | CreateParameter @128; Add @131 | No extracted literal effects. |

</details>

## OutputDeviceCommands.cs {#src-bbf9d29f8bdc}

<code>Software/src/GetSeek.Application/Settings/OutputDeviceCommands.cs</code> · 123 lines.

SHA-256: <code>38fafa8a9f93272112bf00e21940fb50e8739936d1f30baa1ba24529d6ac5568</code>.

Declarations: <code>UpdateOutputDeviceSettingsCommand : ICommand&lt;bool&gt;</code> (line 7), <code>RecordThermalTestSpoolAcceptedCommand : ICommand&lt;bool&gt;</code> (line 22), <code>ConfirmThermalPhysicalOutputCommand : ICommand&lt;bool&gt;</code> (line 27), <code>OutputDeviceCommandHandler : ICommandHandler&lt;UpdateOutputDeviceSettingsCommand, bool&gt;, ICommandHandler&lt;RecordThermalTestSpoolAcceptedCommand, bool&gt;, ICommandHandler&lt;ConfirmThermalPhysicalOutputCommand, bool&gt;</code> (line 32).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a04cc1af2dfe"></span><code>OutputDeviceCommandHandler.HandleAsync(UpdateOutputDeviceSettingsCommand,CommandEnvelope&lt;UpdateOutputDeviceSettingsCommand&gt;,CancellationToken)</code><br>37–78 | Trim @40; ToLowerInvariant @41; Contains @43; Fail @43; ConfigureAwait @53; IsActiveAdminAsync @53; CreateCommand @56; Add @70; ToString @73; ToString @75; ExecuteNonQueryAsync @76; Success(bool) @77 | UPDATE output_device_config @58 |
| <span id="m-9c80dc7d5eaf"></span><code>OutputDeviceCommandHandler.HandleAsync(RecordThermalTestSpoolAcceptedCommand,CommandEnvelope&lt;RecordThermalTestSpoolAcceptedCommand&gt;,CancellationToken)</code><br>80–92 | ValidFingerprint @83; Fail @83; ConfigureAwait @84; IsActiveAdminAsync @84; CreateCommand @85; Add @88; ToString @88; ToString @89; ExecuteNonQueryAsync @90; Success(bool) @91 | UPDATE output_device_config @87 |
| <span id="m-7dd40ed62d92"></span><code>OutputDeviceCommandHandler.HandleAsync(ConfirmThermalPhysicalOutputCommand,CommandEnvelope&lt;ConfirmThermalPhysicalOutputCommand&gt;,CancellationToken)</code><br>94–106 | ValidFingerprint @97; Fail @97; ConfigureAwait @98; IsActiveAdminAsync @98; CreateCommand @99; Add @102; ToString @102; ToString @103; ExecuteNonQueryAsync @104; Success(bool) @105 | UPDATE output_device_config @101 |
| <span id="m-36ab9b284c0d"></span><code>OutputDeviceCommandHandler.IsActiveAdminAsync(Guid,CancellationToken)</code><br>108–115 | CreateCommand @110; Add @113; ToString @113; ToInt64 @114; ConfigureAwait @114; ExecuteScalarAsync @114 | FROM users @112; JOIN user_roles @112 |
| <span id="m-87f72b5d6e9e"></span><code>OutputDeviceCommandHandler.ValidFingerprint(string)</code><br>117–117 | IsNullOrWhiteSpace @117 | No extracted literal effects. |
| <span id="m-f074e9503d31"></span><code>OutputDeviceCommandHandler.Fail(string,string)</code><br>118–118 | Failure(bool) @118 | No extracted literal effects. |
| <span id="m-a7b11bf4e352"></span><code>OutputDeviceCommandHandler.Add(System.Data.Common.DbCommand,string,object)</code><br>119–122 | CreateParameter @121; Add @121 | No extracted literal effects. |

</details>

## PriceTierSettingsCommandHandler.cs {#src-5251d2a718d0}

<code>Software/src/GetSeek.Application/Settings/PriceTierSettingsCommandHandler.cs</code> · 206 lines.

SHA-256: <code>34b271356f3076a2c499e7329ba38cfac71d301a7b9e9035355042d80dbec7f7</code>.

Declarations: <code>PriceTierSettingsCommandHandler : ICommandHandler&lt;UpdatePriceTierSettingsCommand, bool&gt;</code> (line 9), <code>TierState</code> (line 197).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-2bbca65b6079"></span><code>PriceTierSettingsCommandHandler.HandleAsync(UpdatePriceTierSettingsCommand,CommandEnvelope&lt;UpdatePriceTierSettingsCommand&gt;,CancellationToken)</code><br>15–124 | Failure(bool) @22; ToString @29; CreateCommand @32; AddParam @38; ToString @38; ConfigureAwait @39; ExecuteScalarAsync @39; ReadTierStatesAsync @48; IsNullOrWhiteSpace @55; TryParse @60; Trim @76; ToString @77; ToLowerInvariant @79; Trim @79; ExecuteNonQueryAsync @80; ExecuteNonQueryAsync @96; ExecuteNonQueryAsync @110; TryGetValue @116; RecordAffectedSystemTierItemsAsync @119; Success(bool) @123 | FROM users @36; JOIN user_roles @36; UPDATE price_level_settings @103; UPDATE price_level_settings @68; UPDATE store_config @88 · INVALID_PRICE_LEVEL_COUNT @22; AUTH_UNAUTHORIZED @41; INVALID_TIER_WEIGHT @63 |
| <span id="m-891875aacc7e"></span><code>PriceTierSettingsCommandHandler.ReadTierStatesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>126–148 | CreateCommand @131; ConfigureAwait @137; ExecuteReaderAsync @137; ReadAsync @138; GetString @140; GetInt32 @144 | FROM price_level_settings @133 |
| <span id="m-855fbfc74b8b"></span><code>PriceTierSettingsCommandHandler.RecordAffectedSystemTierItemsAsync(DbConnection,DbTransaction?,string,TierState,TierState,CommandEnvelope&lt;UpdatePriceTierSettingsCommand&gt;,CancellationToken)</code><br>150–192 | CreateCommand @160; AddParam @169; ConfigureAwait @170; ExecuteReaderAsync @170; ReadAsync @171; TryParse @173; GetString @173; Add @174; DescribeTier @178; RecordAsync @182; ToString @189 | FROM items @163; JOIN item_price_levels @163 |
| <span id="m-f23fccc56b8f"></span><code>PriceTierSettingsCommandHandler.DescribeTier(TierState)</code><br>194–195 | — | No extracted literal effects. |
| <span id="m-31bfff363a35"></span><code>PriceTierSettingsCommandHandler.AddParam(DbCommand,string,object)</code><br>199–205 | CreateParameter @201; Add @204 | No extracted literal effects. |

</details>

## PriceTierSettingsCommands.cs {#src-96fee6b3d872}

<code>Software/src/GetSeek.Application/Settings/PriceTierSettingsCommands.cs</code> · 30 lines.

SHA-256: <code>a65b0e6d8b83e741ce587e794fa6539e6e27f48cc9e69090d29d21af5c3a5bc3</code>.

Declarations: <code>PriceTierEdit</code> (line 6), <code>PriceLevelSettingDto</code> (line 12), <code>UpdatePriceTierSettingsCommand : ICommand&lt;bool&gt;</code> (line 24).

## ReceiptDesignCommands.cs {#src-c85e5e7f37c8}

<code>Software/src/GetSeek.Application/Settings/ReceiptDesignCommands.cs</code> · 109 lines.

SHA-256: <code>b3138e2de340dfcc548139ad25015a06515b2e178b3e3d54b8be722e264eb286</code>.

Declarations: <code>ReceiptDesignDocument</code> (line 10), <code>SaveReceiptDesignCommand : ICommand&lt;long&gt;</code> (line 20), <code>SaveReceiptDesignCommandHandler : ICommandHandler&lt;SaveReceiptDesignCommand, long&gt;</code> (line 27).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9f50da09c2da"></span><code>SaveReceiptDesignCommandHandler.HandleAsync(SaveReceiptDesignCommand,CommandEnvelope&lt;SaveReceiptDesignCommand&gt;,CancellationToken)</code><br>30–103 | ToLowerInvariant @35; Trim @35; Failure(long) @37; Validate @47; Contains @50; Serialize @56; ToHexStringLower @57; HashData @57; GetBytes @57; ToString @60; CreateCommand @61; Add @65; ToString @65; ToInt64 @66; ConfigureAwait @66; ExecuteScalarAsync @66; ExecuteScalarAsync @75; ToString @75; NewGuid @79; ExecuteNonQueryAsync @84; ExecuteScalarAsync @92; ExecuteNonQueryAsync @100; Success(long) @102 | FROM receipt_design_versions @90; FROM receipt_designs @73; FROM users @64; INSERT INTO receipt_design_versions @98; INSERT INTO receipt_designs @82; JOIN user_roles @64; UPDATE receipt_designs @98 · INVALID_RECEIPT_MEDIA_FAMILY @37; RECEIPT_DESIGN_REQUIRED @39; INVALID_RECEIPT_DESIGN @43; ADMIN_REQUIRED @67 |
| <span id="m-b77b924cf060"></span><code>SaveReceiptDesignCommandHandler.Add(System.Data.Common.DbCommand,string,object)</code><br>105–108 | CreateParameter @107; Add @107 | No extracted literal effects. |

</details>

## ReceiptTemplateSyntax.cs {#src-21cc833dd9ad}

<code>Software/src/GetSeek.Application/Settings/ReceiptTemplateSyntax.cs</code> · 54 lines.

SHA-256: <code>4f286f4765c6fe055a7dfc61fad926c7ceabd426561cd5f206cfc5b1b80605ee</code>.

Declarations: <code>ReceiptTemplateSyntax</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f51db0618efa"></span><code>ReceiptTemplateSyntax.Validate(string)</code><br>17–53 | ThrowIfNull @19; Contains @21; Replace @24; Contains @25; Matches @29; StartsWith @33; Equals @42; Contains @48; IsMatch @49 | InvalidDataException @20; InvalidDataException @22; InvalidDataException @26; InvalidDataException @36; InvalidDataException @43; InvalidDataException @48; InvalidDataException @50; InvalidDataException @52 |

</details>

## SaveManualPaymentDisplayCommand.cs {#src-89b0251a9781}

<code>Software/src/GetSeek.Application/Settings/SaveManualPaymentDisplayCommand.cs</code> · 16 lines.

SHA-256: <code>d410b6a22032cc68298ea261d567b220af26b810cef62035b38c5005eb728caa</code>.

Declarations: <code>SaveManualPaymentDisplayCommand : ICommand&lt;bool&gt;</code> (line 5).

## TeamCommandHandler.cs {#src-691edb662577}

<code>Software/src/GetSeek.Application/Teams/TeamCommandHandler.cs</code> · 803 lines.

SHA-256: <code>45693e05a5654830110faf71c68b1f4aee432fcfa47700f1e8c7722b673eb11f</code>.

Declarations: <code>TeamCommandHandler : ICommandHandler&lt;CreateTeamMemberCommand, CreateTeamMemberResult&gt;, ICommandHandler&lt;UpdateTeamMemberCommand, UpdateTeamMemberResult&gt;</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (8)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-65c47fa2f7ce"></span><code>TeamCommandHandler.AddParam(DbCommand,string,object?)</code><br>30–36 | CreateParameter @32; Add @35 | No extracted literal effects. |
| <span id="m-2401aa2dbe1e"></span><code>TeamCommandHandler.HandleAsync(CreateTeamMemberCommand,CommandEnvelope&lt;CreateTeamMemberCommand&gt;,CancellationToken)</code><br>38–243 | ToString @46; ConfigureAwait @49; HasPermissionAsync @49; Failure(CreateTeamMemberResult) @52; Trim @72; IsNullOrWhiteSpace @73; ToLowerInvariant @78; FromDateTime @84; ToUpperInvariant @90; GenerateUniquePersonCodeAsync @93; PersonCodeExistsAsync @97; IsValidRole @115; IsUserInRoleAsync @122; IsValidPin @130; UsernameExistsAsync @135; NewGuid @140; ValidatePermissionOverridesAsync @143; HashPin @152; InsertUserAccountAsync @153; AssignRoleAsync @154; UpsertPermissionOverridesAsync @158; UserExistsAsync @164; IsUserLinkedToPersonAsync @169; GetUsernameByIdAsync @174; IsNullOrEmpty @191; IsMatch @191; Trim @198; InsertPersonAsync @208; ToString @216; Trim @217; UpsertSalaryAgreementAsync @224; ValidateAsync @229; Success(CreateTeamMemberResult) @236 | AUTH_UNAUTHORIZED @52; AUTH_UNAUTHORIZED @60; INVALID_COMBINATION @67; INVALID_DISPLAY_NAME @75; INVALID_PERSON_KIND @81; INVALID_EMPLOYMENT_DATES @87; PERSON_CODE_ALREADY_EXISTS @99; INVALID_USERNAME @111; INVALID_ROLE @117; PRIVILEGE_ESCALATION_DENIED @125; INVALID_QUICK_PIN @132; USERNAME_ALREADY_EXISTS @137; USER_NOT_FOUND @166; USER_ALREADY_LINKED @171; INVALID_SALARY_AMOUNT @183; INVALID_SALARY_AMOUNT @187; INVALID_PAYROLL_MONTH @193; INVALID_PAYROLL_MONTH @201; INVALID_DECIMAL_PLACES @220; INVALID_SALARY_DRAFT @232 |
| <span id="m-397002ae99a5"></span><code>TeamCommandHandler.HandleAsync(UpdateTeamMemberCommand,CommandEnvelope&lt;UpdateTeamMemberCommand&gt;,CancellationToken)</code><br>245–765 | ToString @253; ConfigureAwait @259; HasPermissionAsync @259; Failure(UpdateTeamMemberResult) @262; CreateCommand @284; AddParam @288; ToString @288; ExecuteScalarAsync @289; Parse @292; ToString @292; Trim @298; IsNullOrWhiteSpace @299; ExecuteScalarAsync @305; ToString @306; ToLowerInvariant @316; FromDateTime @322; IsNullOrEmpty @330; IsMatch @330; GenerateUniquePersonCodeAsync @336; NewGuid @337; InsertPersonAsync @340; ToString @360; ExecuteReaderAsync @361; ReadAsync @362; GetInt32 @366; GetString @367; IsDBNull @368; ToString @419; ToString @420; ToString @424; ExecuteNonQueryAsync @426; ExecuteNonQueryAsync @435; GetUserActiveStatusAsync @449; UserHasActiveShiftAsync @453; GetUserRoleAsync @459; Equals @460; CountActiveAdminsAsync @462; ExecuteNonQueryAsync @473; BumpUserSecurityRevisionAsync @475; IsValidRole @491; Trim @491; IsUserInRoleAsync @498; AssignRoleAsync @515; IsValidPin @522; Trim @522; HashPin @526; ExecuteNonQueryAsync @532; ExecuteNonQueryAsync @542; ValidatePermissionOverridesAsync @550; UpsertPermissionOverridesAsync @557; UsernameExistsAsync @571; InsertUserAccountAsync @612; ToString @624; ExecuteNonQueryAsync @626; UserExistsAsync @638; IsUserLinkedToPersonAsync @643; ToString @651; ExecuteScalarAsync @683; Trim @692; CheckTrackingStartAllowedAsync @698; ExecuteNonQueryAsync @711; GetValueOrDefault @714; ToUpperInvariant @716; Trim @716; ExecuteReaderAsync @729; ReadAsync @730; GetInt64 @732; IsDBNull @733; GetString @733; CheckCurrencyChangeAllowedAsync @737; UpsertSalaryAgreementAsync @743; ValidateAsync @751; Success(UpdateTeamMemberResult) @759 | FROM person_records @287; FROM person_records @359; FROM salary_agreements @726; FROM salary_periods @680; FROM users @303; UPDATE person_records @406; UPDATE person_records @623; UPDATE person_records @650; UPDATE person_records @706; UPDATE users @432; UPDATE users @471; UPDATE users @529; UPDATE users @540 · AUTH_UNAUTHORIZED @262; AUTH_UNAUTHORIZED @271; INVALID_EMPLOYMENT_DATES @326; INVALID_PAYROLL_MONTH @332; PERSON_NOT_FOUND @364; STALE_REVISION @373; INVALID_DISPLAY_NAME @387; INVALID_PERSON_KIND @394; INVALID_EMPLOYMENT_DATES @400; ON_SHIFT_CASHIER_PROTECTED @455; LAST_ADMIN_PROTECTED @465; PIN_REQUIRED @485; INVALID_ROLE @493; PRIVILEGE_ESCALATION_DENIED @501; LAST_ADMIN_PROTECTED @511; INVALID_QUICK_PIN @524; INVALID_USERNAME @568; USERNAME_ALREADY_EXISTS @573; INVALID_QUICK_PIN @579; INVALID_ROLE @585; PRIVILEGE_ESCALATION_DENIED @593; USER_NOT_FOUND @640; USER_ALREADY_LINKED @645; INVALID_SALARY_AMOUNT @664; INVALID_SALARY_AMOUNT @668; INVALID_EFFECTIVE_MONTH @674; PERIOD_ALREADY_FINALIZED @686; INVALID_PAYROLL_MONTH @695; TRACKING_START_EXCLUDES_EXISTING_PAYROLL @701; INVALID_DECIMAL_PLACES @719; CURRENCY_CHANGE_NOT_ALLOWED @740; INVALID_SALARY_DRAFT @754 |
| <span id="m-9dd3ab68c26f"></span><code>TeamCommandHandler.IsValidRole(string,string)</code><br>767–774 | Equals @769 | No extracted literal effects. |
| <span id="m-e166b54b0176"></span><code>TeamCommandHandler.IsValidPin(string)</code><br>776–777 | IsNullOrEmpty @777; IsMatch @777 | No extracted literal effects. |
| <span id="m-4e20a587e291"></span><code>TeamCommandHandler.IsUserInRoleAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>779–788 | CreateCommand @781; AddParam @784; ToString @784; ConfigureAwait @786; ExecuteScalarAsync @786 | FROM user_roles @783 |
| <span id="m-389d98a83d85"></span><code>TeamCommandHandler.HasPermissionAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>790–799 | ConfigureAwait @795; HasPermissionAsync @795 | No extracted literal effects. |
| <span id="m-c6a8bd255da2"></span><code>TeamCommandHandler.GenerateUniquePersonCodeAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>801–802 | GenerateUniquePersonCodeAsync @802 | No extracted literal effects. |

</details>

## TeamCommands.cs {#src-c83e7d5dd8f2}

<code>Software/src/GetSeek.Application/Teams/TeamCommands.cs</code> · 96 lines.

SHA-256: <code>9be81bbe9db84f6c3b86e387a3fd4cb2c6d4129fb451b986ea7a4947df044be6</code>.

Declarations: <code>CreateTeamMemberCommand : ICommand&lt;CreateTeamMemberResult&gt;, ISanitizedAuditPayload</code> (line 7), <code>CreateTeamMemberResult</code> (line 41), <code>UpdateTeamMemberCommand : ICommand&lt;UpdateTeamMemberResult&gt;, ISanitizedAuditPayload</code> (line 49), <code>UpdateTeamMemberResult</code> (line 91).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-22ae561b7ab4"></span><code>CreateTeamMemberCommand.GetSanitizedAuditPayload()</code><br>21–38 | Serialize @21; IsNullOrEmpty @31 | No extracted literal effects. |
| <span id="m-83a19e95d465"></span><code>UpdateTeamMemberCommand.GetSanitizedAuditPayload()</code><br>69–88 | Serialize @69; IsNullOrEmpty @82 | No extracted literal effects. |

</details>

## TeamPrimitives.cs {#src-7c15dd8ae675}

<code>Software/src/GetSeek.Application/Teams/TeamPrimitives.cs</code> · 627 lines.

SHA-256: <code>9149302fe058c54a5703216867057a6b110af3a03be3bbb6d28f04591436154f</code>.

Declarations: <code>TeamPrimitives</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (23)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-94e954d7a5e8"></span><code>TeamPrimitives.IsValidPin(string?)</code><br>14–15 | IsNullOrEmpty @15; IsMatch @15; Trim @15 | No extracted literal effects. |
| <span id="m-52ecd0586651"></span><code>TeamPrimitives.AddParam(DbCommand,string,object?)</code><br>17–23 | CreateParameter @19; Add @22 | No extracted literal effects. |
| <span id="m-182b02352913"></span><code>TeamPrimitives.GenerateUniquePersonCodeAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>25–52 | CreateCommand @30; ConfigureAwait @33; ExecuteScalarAsync @33; ToString @37; Match @38; TryParse @39; PersonCodeExistsAsync @46 | FROM person_records @32 |
| <span id="m-7f49849abc9d"></span><code>TeamPrimitives.PersonCodeExistsAsync(DbConnection,DbTransaction?,string,Guid?,CancellationToken)</code><br>54–75 | CreateCommand @61; AddParam @66; ToString @66; Trim @72; ConfigureAwait @73; ExecuteScalarAsync @73 | FROM person_records @65; FROM person_records @70 |
| <span id="m-c4aa6f858e40"></span><code>TeamPrimitives.UsernameExistsAsync(DbConnection,DbTransaction?,string,Guid?,CancellationToken)</code><br>77–98 | CreateCommand @84; AddParam @89; ToString @89; Trim @95; ConfigureAwait @96; ExecuteScalarAsync @96 | FROM users @88; FROM users @93 |
| <span id="m-9ee1a51451dc"></span><code>TeamPrimitives.RoleExistsAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>100–112 | CreateCommand @106; AddParam @109; Trim @109; ConfigureAwait @110; ExecuteScalarAsync @110 | FROM roles @108 |
| <span id="m-6239b0877221"></span><code>TeamPrimitives.UserExistsAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>114–126 | CreateCommand @120; AddParam @123; ToString @123; ConfigureAwait @124; ExecuteScalarAsync @124 | FROM users @122 |
| <span id="m-20de1e7b545f"></span><code>TeamPrimitives.GetUsernameByIdAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>128–139 | CreateCommand @134; AddParam @137; ToString @137; ConfigureAwait @138; ExecuteScalarAsync @138; ToString @138 | FROM users @136 |
| <span id="m-080fb7440100"></span><code>TeamPrimitives.IsUserLinkedToPersonAsync(DbConnection,DbTransaction?,Guid,Guid?,CancellationToken)</code><br>141–162 | CreateCommand @148; AddParam @153; ToString @153; ToString @159; ConfigureAwait @160; ExecuteScalarAsync @160 | FROM person_records @152; FROM person_records @157 |
| <span id="m-b931d1add6ab"></span><code>TeamPrimitives.PermissionKeyExistsAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>164–176 | CreateCommand @170; AddParam @173; Trim @173; ConfigureAwait @174; ExecuteScalarAsync @174 | FROM permissions @172 |
| <span id="m-028f6bcb76a7"></span><code>TeamPrimitives.BumpUserSecurityRevisionAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>178–196 | CreateCommand @185; AddParam @193; ToString @193; ConfigureAwait @195; ExecuteNonQueryAsync @195 | INSERT INTO user_security_revisions @187 |
| <span id="m-28999c97b79a"></span><code>TeamPrimitives.CountActiveAdminsAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>198–211 | CreateCommand @203; ToInt64 @210; ConfigureAwait @210; ExecuteScalarAsync @210 | FROM users @205; JOIN user_roles @205 |
| <span id="m-3075dfed678d"></span><code>TeamPrimitives.UserHasActiveShiftAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>213–225 | CreateCommand @219; AddParam @222; ToString @222; ToInt64 @223; ConfigureAwait @223; ExecuteScalarAsync @223 | FROM shifts @221 |
| <span id="m-93683db71df3"></span><code>TeamPrimitives.GetUserActiveStatusAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>227–240 | CreateCommand @233; AddParam @236; ToString @236; ConfigureAwait @237; ExecuteScalarAsync @237; ToInt32 @239 | FROM users @235 |
| <span id="m-d7e5dc4c3b13"></span><code>TeamPrimitives.GetUserRoleAsync(DbConnection,DbTransaction?,Guid,CancellationToken)</code><br>242–253 | CreateCommand @248; AddParam @251; ToString @251; ConfigureAwait @252; ExecuteScalarAsync @252; ToString @252 | FROM user_roles @250 |
| <span id="m-94bfcb337bd0"></span><code>TeamPrimitives.InsertPersonAsync(DbConnection,DbTransaction?,Guid,string,string,string,DateOnly,DateOnly?,string?,bool,Guid?,Guid,string,CancellationToken)</code><br>255–296 | CreateCommand @271; AddParam @283; ToString @283; ToString @287; ToString @288; IsNullOrWhiteSpace @289; Trim @289; ToString @291; ToString @292; ConfigureAwait @295; ExecuteNonQueryAsync @295 | INSERT INTO person_records @273 |
| <span id="m-918279749cf4"></span><code>TeamPrimitives.InsertUserAccountAsync(DbConnection,DbTransaction?,Guid,string,string,string,bool,string,CancellationToken)</code><br>298–324 | CreateCommand @309; AddParam @317; ToString @317; ConfigureAwait @323; ExecuteNonQueryAsync @323 | INSERT INTO users @311 |
| <span id="m-246a4a6c1068"></span><code>TeamPrimitives.AssignRoleAsync(DbConnection,DbTransaction?,Guid,string,CancellationToken)</code><br>326–341 | CreateCommand @333; AddParam @338; ToString @338; ConfigureAwait @340; ExecuteNonQueryAsync @340 | DELETE FROM user_roles @335; INSERT INTO user_roles @335 |
| <span id="m-8e58775df40a"></span><code>TeamPrimitives.ValidatePermissionOverridesAsync(DbConnection,DbTransaction?,Guid,Guid,IReadOnlyList&lt;UserPermissionOverrideInput&gt;,CancellationToken)</code><br>350–423 | CreateCommand @359; AddParam @370; ToString @370; ToInt64 @371; ConfigureAwait @371; ExecuteScalarAsync @371; PermissionKeyExistsAsync @380; Contains @392; Equals @398; ToString @413; ExecuteScalarAsync @414 | FROM users @362; FROM users @402; JOIN roles @362; JOIN user_permission_overrides @402; JOIN user_roles @362; JOIN user_roles @402 |
| <span id="m-f2031b928ad2"></span><code>TeamPrimitives.UpsertPermissionOverridesAsync(DbConnection,DbTransaction?,Guid,IReadOnlyList&lt;UserPermissionOverrideInput&gt;,Guid,string,CancellationToken)</code><br>425–451 | CreateCommand @436; AddParam @444; ToString @444; ToString @447; ConfigureAwait @449; ExecuteNonQueryAsync @449 | INSERT OR REPLACE INTO user_permission_overrides @438 |
| <span id="m-9dfb026f9c2d"></span><code>TeamPrimitives.UpsertSalaryAgreementAsync(DbConnection,DbTransaction?,Guid,string,long,long?,string,int,bool,Guid,string,CancellationToken)</code><br>453–497 | NewGuid @467; CreateCommand @468; AddParam @486; ToString @486; ToString @487; ToString @494; ConfigureAwait @496; ExecuteNonQueryAsync @496 | INSERT INTO salary_agreements @470 |
| <span id="m-55e485e22f34"></span><code>TeamPrimitives.CheckTrackingStartAllowedAsync(DbConnection,DbTransaction?,Guid,string?,CancellationToken)</code><br>499–531 | IsNullOrEmpty @506; CreateCommand @508; AddParam @516; ToString @516; ConfigureAwait @518; ExecuteReaderAsync @518; ReadAsync @519; GetInt64 @521 | FROM salary_adjustments @510; FROM salary_ledger_entries @510; FROM salary_payments @510; FROM salary_periods @510 |
| <span id="m-949518813b6d"></span><code>TeamPrimitives.CheckCurrencyChangeAllowedAsync(DbConnection,DbTransaction?,Guid,string,int,string,CancellationToken)</code><br>533–626 | CreateCommand @542; AddParam @545; ToString @545; ConfigureAwait @546; ExecuteReaderAsync @546; ReadAsync @547; GetString @549; GetInt32 @550; Equals @552; CloseAsync @554; ExecuteScalarAsync @561; ExecuteScalarAsync @568; ExecuteReaderAsync @577; ReadAsync @578; ParseExact @580; GetString @580; IsDBNull @581; IsNullOrWhiteSpace @584; CompareOrdinal @584; CloseAsync @586; ToString @592; DaysInMonth @593; ExecuteScalarAsync @605; AddMonths @612 | FROM person_records @575; FROM salary_agreements @544; FROM salary_ledger_entries @559; FROM salary_periods @566; FROM salary_periods @602 |

</details>

## ImportThirdPartiesCommandHandler.cs {#src-7bb9c4e66dce}

<code>Software/src/GetSeek.Application/ThirdParties/ImportThirdPartiesCommandHandler.cs</code> · 511 lines.

SHA-256: <code>3f1ad6606847eb116c39b2c35abbc434fb04d67af26a77b916a584e10cb6970c</code>.

Declarations: <code>ImportThirdPartiesCommandHandler : ICommandHandler&lt;ImportThirdPartiesCommand, ImportThirdPartiesResult&gt;</code> (line 17).

<details markdown>
<summary>Methods, calls, table effects and failures (10)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7085a9c8a444"></span><code>ImportThirdPartiesCommandHandler.HandleAsync(ImportThirdPartiesCommand,CommandEnvelope&lt;ImportThirdPartiesCommand&gt;,CancellationToken)</code><br>25–358 | Failure(ImportThirdPartiesResult) @32; ConfigureAwait @39; CheckPriorImportAsync @39; Success(ImportThirdPartiesResult) @42; FingerprintAsync @47; Select @47; TryGetValue @52; TryParseBool @53; Any @55; Contains @55; ResolveTier @58; ActiveTiersAsync @58; Add @60; MergeAsync @60; LoadCategoriesAsync @65; LoadActivePriceTiersAsync @66; LoadExistingPartyCodesAsync @67; LoadExistingExternalMappingsAsync @68; IsNullOrWhiteSpace @78; Contains @83; TryNormalizePhone @88; IsValidStateCode @96; ContainsKey @106; ToHashSet @111; Select @111; Parse @111; ToLowerInvariant @112; Trim @112; Contains @113; Trim @118; ToUpperInvariant @119; Trim @119; Trim @120; Trim @121; Add @122; Add @127; Add @132; TryGetValue @137; TryGetValue @138; Equals @139; IsSystemWalkInAsync @150; ToString @158; NormalizeDbValue @162; Trim @168; NormalizeStateCode @169; TryGetValue @170; RecordAsync @191; IsAvailableAsync @193; CreateCommand @196; AddParam @223; Trim @225; Trim @229; ExecuteNonQueryAsync @245; ContainsKey @250; InsertExternalMappingAsync @252; ToString @261; NewGuid @261; GenerateNextCodeAsync @262; ExecuteNonQueryAsync @307; ToString @342; ExecuteNonQueryAsync @345 | FROM third_parties @191; INSERT INTO third_parties @270; INSERT INTO third_party_imports @326; UPDATE third_parties @199 · IMPORT_EMPTY @32; IMPORT_TOO_LARGE @46; IMPORT_PREVIEW_STALE @48; INVALID_IS_ACTIVE @54; IMPORT_CLEAR_NOT_ALLOWED @56; INVALID_PRICE_LEVEL @59; NAME_REQUIRED @80; INVALID_KIND @85; PHONE_FORMAT_INVALID @93; STATE_REGION_INVALID @98; MISSING_IDENTIFIER @103; CATEGORY_NOT_FOUND @108; INVALID_PRICE_LEVEL @115; DUPLICATE_CODE_IN_FILE @124; DUPLICATE_EXTERNAL_KEY_IN_FILE @129; DUPLICATE_BARCODE_IN_FILE @134; IDENTIFIER_CONFLICT @141; IDENTIFIER_CONFLICT @146; SYSTEM_WALK_IN_PROTECTED @151; BARCODE_ALREADY_EXISTS @194; THIRD_PARTY_NOT_FOUND @246; BARCODE_ALREADY_EXISTS @266 |
| <span id="m-131de9dfb2f4"></span><code>ImportThirdPartiesCommandHandler.CheckPriorImportAsync(DbConnection,DbTransaction?,string,string,CancellationToken)</code><br>360–390 | CreateCommand @367; AddParam @375; ConfigureAwait @377; ExecuteReaderAsync @377; ReadAsync @378; GetString @381; GetInt32 @382 | FROM third_party_imports @369 |
| <span id="m-994f0a107a4b"></span><code>ImportThirdPartiesCommandHandler.InsertExternalMappingAsync(DbConnection,DbTransaction?,string,string,string,string,CancellationToken)</code><br>392–417 | CreateCommand @401; AddParam @412; ConfigureAwait @416; ExecuteNonQueryAsync @416 | INSERT INTO third_party_external_mappings @403 |
| <span id="m-49966866d1c7"></span><code>ImportThirdPartiesCommandHandler.GenerateNextCodeAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>419–435 | CreateCommand @424; ConfigureAwait @431; ExecuteScalarAsync @431; ToInt64 @432 | FROM third_parties @426 |
| <span id="m-0dc126592c6c"></span><code>ImportThirdPartiesCommandHandler.LoadCategoriesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>437–449 | CreateCommand @440; ConfigureAwait @443; ExecuteReaderAsync @443; ReadAsync @444; GetString @446 | FROM product_categories @442 |
| <span id="m-590000a1728f"></span><code>ImportThirdPartiesCommandHandler.LoadActivePriceTiersAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>451–463 | CreateCommand @454; ConfigureAwait @457; ExecuteReaderAsync @457; ReadAsync @458; Add @460; GetString @460 | FROM price_level_settings @456; FROM store_config @456 |
| <span id="m-59b051731bb1"></span><code>ImportThirdPartiesCommandHandler.LoadExistingPartyCodesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>465–477 | CreateCommand @468; ConfigureAwait @471; ExecuteReaderAsync @471; ReadAsync @472; GetString @474 | FROM third_parties @470 |
| <span id="m-cfc661d4aa69"></span><code>ImportThirdPartiesCommandHandler.LoadExistingExternalMappingsAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>479–491 | CreateCommand @482; ConfigureAwait @485; ExecuteReaderAsync @485; ReadAsync @486; ToUpperInvariant @488; GetString @488 | FROM third_party_external_mappings @484 |
| <span id="m-71b31cd84032"></span><code>ImportThirdPartiesCommandHandler.IsSystemWalkInAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>493–502 | TryParse @495; CreateCommand @496; AddParam @499; ConfigureAwait @500; ExecuteScalarAsync @500; ToInt32 @501 | FROM third_parties @498 |
| <span id="m-560f5e970ab5"></span><code>ImportThirdPartiesCommandHandler.AddParam(DbCommand,string,object)</code><br>504–510 | CreateParameter @506; Add @509 | No extracted literal effects. |

</details>

## ImportThirdPartiesCommands.cs {#src-26c060baba90}

<code>Software/src/GetSeek.Application/ThirdParties/ImportThirdPartiesCommands.cs</code> · 79 lines.

SHA-256: <code>995ccca1096216886e0fcb7bec5f6226638fef85dec000b691bafdb4c83e6b42</code>.

Declarations: <code>ImportThirdPartyRow</code> (line 7), <code>ThirdPartyImportRowPreview</code> (line 34), <code>ThirdPartyImportPreview</code> (line 45), <code>ImportThirdPartiesCommand : ICommand&lt;ImportThirdPartiesResult&gt;</code> (line 61), <code>ImportThirdPartiesResult</code> (line 72).

## ThirdPartyBarcodePolicy.cs {#src-f0a99428cb73}

<code>Software/src/GetSeek.Application/ThirdParties/ThirdPartyBarcodePolicy.cs</code> · 16 lines.

SHA-256: <code>68532aff9edc0b02aad334f249427ba40d8571f06a4c1ef1d80f3ee2917db0ef</code>.

Declarations: <code>ThirdPartyBarcodePolicy</code> (line 5).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a9642cbb5425"></span><code>ThirdPartyBarcodePolicy.IsAvailableAsync(DbConnection,DbTransaction?,string?,string?,CancellationToken)</code><br>7–15 | IsNullOrWhiteSpace @9; CreateCommand @10; CreateParameter @12; Trim @12; Add @12; ToInt64 @14; ConfigureAwait @14; ExecuteScalarAsync @14 | FROM third_parties @11 |

</details>

## ThirdPartyCommandHandler.cs {#src-b2b033d6711b}

<code>Software/src/GetSeek.Application/ThirdParties/ThirdPartyCommandHandler.cs</code> · 448 lines.

SHA-256: <code>57ee3d94fef8d3c291d472952432320962ef53edf936f820aa97c327d5d9c494</code>.

Declarations: <code>ThirdPartyCommandHandler : ICommandHandler&lt;CreateThirdPartyCommand, ThirdPartyDto&gt;, ICommandHandler&lt;UpdateThirdPartyCommand, ThirdPartyDto&gt;, ICommandHandler&lt;DeactivateThirdPartyCommand, bool&gt;, ICommandHandler&lt;ReactivateThirdPartyCommand, bool&gt;, ICommandHandler&lt;SetThirdPartyPriceLevelCommand, bool&gt;</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (12)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e3e4b695a83f"></span><code>ThirdPartyCommandHandler.HandleAsync(CreateThirdPartyCommand,CommandEnvelope&lt;CreateThirdPartyCommand&gt;,CancellationToken)</code><br>17–129 | Trim @25; IsNullOrWhiteSpace @26; Failure(ThirdPartyDto) @28; TryNormalizePhones @31; IsValidStateCode @34; NormalizeDbValue @37; NormalizeTier @38; NormalizeNullable @39; NormalizeStateCode @40; ConfigureAwait @44; ValidateActiveTierAsync @44; GenerateNextCodeAsync @51; IsBarcodeAvailableAsync @53; NewGuid @56; ToString @58; CreateCommand @60; AddParam @77; ToString @77; ToString @97; ExecuteNonQueryAsync @99; Success(ThirdPartyDto) @128 | INSERT INTO third_parties @63 · NAME_REQUIRED @28; PHONE_FORMAT_INVALID @33; STATE_REGION_INVALID @35; INVALID_PRICE_LEVEL @47; DUPLICATE_BARCODE @54 |
| <span id="m-da62f735756b"></span><code>ThirdPartyCommandHandler.HandleAsync(UpdateThirdPartyCommand,CommandEnvelope&lt;UpdateThirdPartyCommand&gt;,CancellationToken)</code><br>131–277 | Trim @139; IsNullOrWhiteSpace @140; Failure(ThirdPartyDto) @142; TryNormalizePhones @145; IsValidStateCode @148; NormalizeDbValue @151; NormalizeTier @152; NormalizeNullable @153; NormalizeStateCode @154; CreateCommand @161; AddParam @165; ToString @165; ConfigureAwait @166; ExecuteReaderAsync @166; ReadAsync @167; GetString @172; Parse @173; GetInt32 @174; IsBarcodeAvailableAsync @184; ValidateActiveTierAsync @188; ToString @195; ToString @242; ExecuteNonQueryAsync @246; Success(ThirdPartyDto) @276 | FROM third_parties @164; UPDATE third_parties @200 · NAME_REQUIRED @142; PHONE_FORMAT_INVALID @147; STATE_REGION_INVALID @149; THIRD_PARTY_NOT_FOUND @169; SYSTEM_WALK_IN_PROTECTED @179; DUPLICATE_BARCODE @185; INVALID_PRICE_LEVEL @191; THIRD_PARTY_NOT_FOUND @247 |
| <span id="m-599566bc0d8c"></span><code>ThirdPartyCommandHandler.HandleAsync(DeactivateThirdPartyCommand,CommandEnvelope&lt;DeactivateThirdPartyCommand&gt;,CancellationToken)</code><br>279–316 | CreateCommand @287; AddParam @291; ToString @291; ConfigureAwait @292; ExecuteScalarAsync @292; Failure(bool) @295; ToInt32 @297; ToString @302; ExecuteNonQueryAsync @311; Success(bool) @315 | FROM third_parties @290; UPDATE third_parties @308 · THIRD_PARTY_NOT_FOUND @295; SYSTEM_WALK_IN_PROTECTED @298; THIRD_PARTY_NOT_FOUND @312 |
| <span id="m-fec6a8dfa150"></span><code>ThirdPartyCommandHandler.HandleAsync(ReactivateThirdPartyCommand,CommandEnvelope&lt;ReactivateThirdPartyCommand&gt;,CancellationToken)</code><br>318–340 | CreateCommand @324; AddParam @327; ToString @327; ToString @328; ConfigureAwait @329; ExecuteNonQueryAsync @329; ExecuteScalarAsync @335; Failure(bool) @336; Success(bool) @339 | FROM third_parties @333; UPDATE third_parties @326 |
| <span id="m-e177b1388efc"></span><code>ThirdPartyCommandHandler.HandleAsync(SetThirdPartyPriceLevelCommand,CommandEnvelope&lt;SetThirdPartyPriceLevelCommand&gt;,CancellationToken)</code><br>342–384 | Failure(bool) @348; NormalizeTier @350; ConfigureAwait @351; ValidateActiveTierAsync @351; CreateCommand @355; AddParam @358; ToString @358; ExecuteReaderAsync @361; ReadAsync @363; IsDBNull @365; GetString @365; GetInt32 @366; Equals @370; Trim @370; ToString @378; ExecuteNonQueryAsync @381; Success(bool) @383 | FROM third_parties @357; UPDATE third_parties @375 · THIRD_PARTY_NOT_FOUND @348; INVALID_PRICE_LEVEL @353; THIRD_PARTY_NOT_FOUND @364; SYSTEM_WALK_IN_PROTECTED @369; THIRD_PARTY_STALE @371; THIRD_PARTY_STALE @382 |
| <span id="m-678802e1b615"></span><code>ThirdPartyCommandHandler.NormalizeNullable(string?)</code><br>386–386 | IsNullOrWhiteSpace @386; Trim @386 | No extracted literal effects. |
| <span id="m-2341d95868f3"></span><code>ThirdPartyCommandHandler.TryNormalizePhones(string?,string?,string?,string?,string?,string?,string?,string?)</code><br>388–396 | TryNormalizePhone @391 | No extracted literal effects. |
| <span id="m-f80469ebcbe6"></span><code>ThirdPartyCommandHandler.NormalizeTier(string?)</code><br>398–399 | IsNullOrWhiteSpace @399; ToLowerInvariant @399; Trim @399 | No extracted literal effects. |
| <span id="m-b3ff10e7df5d"></span><code>ThirdPartyCommandHandler.GenerateNextCodeAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>401–421 | CreateCommand @406; ConfigureAwait @413; ExecuteScalarAsync @413; ToInt64 @414 | FROM third_parties @408 |
| <span id="m-31cbb75f3ca6"></span><code>ThirdPartyCommandHandler.IsBarcodeAvailableAsync(DbConnection,DbTransaction?,string?,Guid?,CancellationToken)</code><br>423–424 | IsAvailableAsync @424; ToString @424 | No extracted literal effects. |
| <span id="m-381be67db2ed"></span><code>ThirdPartyCommandHandler.ValidateActiveTierAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>425–439 | CreateCommand @431; AddParam @434; ToInt64 @435; ConfigureAwait @435; ExecuteScalarAsync @435 | FROM price_level_settings @433 |
| <span id="m-efcb8358bbc5"></span><code>ThirdPartyCommandHandler.AddParam(DbCommand,string,object)</code><br>441–447 | CreateParameter @443; Add @446 | No extracted literal effects. |

</details>

## ThirdPartyCommands.cs {#src-29524979389b}

<code>Software/src/GetSeek.Application/ThirdParties/ThirdPartyCommands.cs</code> · 133 lines.

SHA-256: <code>f0cbbff7d6af177939e2a0e510359e9c89ae8c3b9170a9983294abc2791d7721</code>.

Declarations: <code>ThirdPartyKind</code> (line 7), <code>ThirdPartyKindExtensions</code> (line 14), <code>ThirdPartyDto</code> (line 34), <code>CreateThirdPartyCommand : ICommand&lt;ThirdPartyDto&gt;</code> (line 66), <code>UpdateThirdPartyCommand : ICommand&lt;ThirdPartyDto&gt;</code> (line 90), <code>DeactivateThirdPartyCommand : ICommand&lt;bool&gt;</code> (line 116), <code>ReactivateThirdPartyCommand : ICommand&lt;bool&gt;</code> (line 124), <code>SetThirdPartyPriceLevelCommand : ICommand&lt;bool&gt;</code> (line 130).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d175126c6b27"></span><code>ThirdPartyKindExtensions.ToDbValue(ThirdPartyKind)</code><br>16–21 | — | No extracted literal effects. |
| <span id="m-f5571a4a1994"></span><code>ThirdPartyKindExtensions.Parse(string?)</code><br>23–28 | ToLowerInvariant @23; Trim @23 | No extracted literal effects. |
| <span id="m-0fcc52278e47"></span><code>ThirdPartyKindExtensions.NormalizeDbValue(string?)</code><br>31–31 | ToDbValue @31; Parse @31 | No extracted literal effects. |

</details>

## ThirdPartyFieldPolicy.cs {#src-04927ce7e1ed}

<code>Software/src/GetSeek.Application/ThirdParties/ThirdPartyFieldPolicy.cs</code> · 92 lines.

SHA-256: <code>d80b713af4d90d20992ffffe20f033716d76b4738cff57bd985b3cccec25163c</code>.

Declarations: <code>ThirdPartyFieldPolicy</code> (line 6), <code>RegionOption</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-2936c855bdb1"></span><code>ThirdPartyFieldPolicy.GetMyanmarRegionName(string?)</code><br>33–34 | FirstOrDefault @34; Equals @34 | No extracted literal effects. |
| <span id="m-f48d3f524f2c"></span><code>ThirdPartyFieldPolicy.IsValidStateCode(string?)</code><br>36–37 | IsNullOrWhiteSpace @37; Contains @37; ToLowerInvariant @37; Trim @37 | No extracted literal effects. |
| <span id="m-49614880d1eb"></span><code>ThirdPartyFieldPolicy.NormalizeStateCode(string?)</code><br>39–40 | IsNullOrWhiteSpace @40; ToLowerInvariant @40; Trim @40 | No extracted literal effects. |
| <span id="m-efeea1ba342f"></span><code>ThirdPartyFieldPolicy.FilterPhoneInput(string?)</code><br>42–54 | IsNullOrEmpty @44; Append @49; ToString @53 | No extracted literal effects. |
| <span id="m-e192df6a1ef7"></span><code>ThirdPartyFieldPolicy.TryNormalizePhone(string?,string?)</code><br>56–89 | IsNullOrWhiteSpace @59; Trim @61; Append @67; ToString @80; Split @81; Any @83; Count @84; Contains @84 | No extracted literal effects. |
| <span id="m-59e11972f237"></span><code>ThirdPartyFieldPolicy.NormalizeAlias(string?)</code><br>91–91 | Trim @91 | No extracted literal effects. |

</details>

## ThirdPartyFilterSpecification.cs {#src-253115f0a207}

<code>Software/src/GetSeek.Application/ThirdParties/ThirdPartyFilterSpecification.cs</code> · 92 lines.

SHA-256: <code>053a46dffab90964e079390ec4237b5911c3872b57681574b9f2480a2ef4cb81</code>.

Declarations: <code>ThirdPartyFilterSpecification</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-eac28fa8572c"></span><code>ThirdPartyFilterSpecification.Create(string?,string?,LifecycleStatusScope,bool,Guid?)</code><br>10–11 | NormalizeKind @11; Trim @11 | No extracted literal effects. |
| <span id="m-3d50693366f1"></span><code>ThirdPartyFilterSpecification.AddParameters(DbCommand)</code><br>48–62 | Add @50; ToString @53 | No extracted literal effects. |
| <span id="m-7a1e0d590c88"></span><code>ThirdPartyFilterSpecification.ToBatchFilterJson()</code><br>64–71 | Serialize @64; ToString @69 | No extracted literal effects. |
| <span id="m-a32cdef03428"></span><code>ThirdPartyFilterSpecification.NormalizeKind(string?)</code><br>73–83 | ToLowerInvariant @75; Trim @75 | No extracted literal effects. |
| <span id="m-5ba78064c54a"></span><code>ThirdPartyFilterSpecification.Add(DbCommand,string,object)</code><br>85–91 | CreateParameter @87; Add @90 | No extracted literal effects. |

</details>

## ThirdPartyImportMerge.cs {#src-cff353afe1f2}

<code>Software/src/GetSeek.Application/ThirdParties/ThirdPartyImportMerge.cs</code> · 60 lines.

SHA-256: <code>8b77abb73878f328e91768ff152f756a689dc751311a515b1fac231f581ed87a</code>.

Declarations: <code>ThirdPartyImportMerge</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f9092fb58b70"></span><code>ThirdPartyImportMerge.MergeAsync(ImportThirdPartyRow,DbConnection,DbTransaction?,CancellationToken)</code><br>15–57 | IsNullOrWhiteSpace @19; ConfigureAwait @21; RecordAsync @21; ToUpperInvariant @23; Merge @27; GetValueOrDefault @27; ResolveTier @29; M @29; TryParseBool @53 | FROM third_parties @21; FROM third_parties @23; FROM third_party_external_mappings @23; JOIN product_categories @21; JOIN product_categories @23 |

</details>

## WalkInCustomerIdentity.cs {#src-ecb2b9475d5c}

<code>Software/src/GetSeek.Application/ThirdParties/WalkInCustomerIdentity.cs</code> · 11 lines.

SHA-256: <code>6d164880e65bd8810a4c0ad36f773beb9ad412204f410791bba8350b1d7046d9</code>.

Declarations: <code>WalkInCustomerIdentity</code> (line 4).

## AXAML, migrations and project inputs

### GetSeek.Application.csproj {#src-ed9ddc91762e}

<code>Software/src/GetSeek.Application/GetSeek.Application.csproj</code> · 13 lines · SHA-256 <code>c956c9329a6233aa06171ceee4ab3a4574621f2d85c37926cfbb222d6b66e40f</code>.
