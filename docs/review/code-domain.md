---
id: PP-REVIEW-CODE-DOMAIN
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# GetSeek.Domain source catalogue

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.Domain.csproj:1](code-domain.md#src-451049a93604). Dependencies: none declared.

## CashLossRecord.cs {#src-8c17e1c8d0b1}

<code>Software/src/GetSeek.Domain/Cash/CashLossRecord.cs</code> · 4 lines.

SHA-256: <code>8af4ee529d223a778367fd4eb5059f45dbc68c1785e7e3aa3b83db0c90506167</code>.

Declarations: <code>CashLossKind</code> (line 3), <code>CashLossResult</code> (line 4).

## CashMovement.cs {#src-4840d15f2605}

<code>Software/src/GetSeek.Domain/Cash/CashMovement.cs</code> · 29 lines.

SHA-256: <code>5874283a3934eaf3c582173e79f4847fb27d580d7d21c607f26695f36fc91514</code>.

Declarations: <code>CashMovementType</code> (line 5), <code>CashMovement</code> (line 17).

## Shift.cs {#src-c994ce326790}

<code>Software/src/GetSeek.Domain/Cash/Shift.cs</code> · 24 lines.

SHA-256: <code>927587737ae5d3c99647bd2443046a8a746ed3e941158201ab4403891e35efde</code>.

Declarations: <code>ShiftStatus</code> (line 5), <code>Shift</code> (line 11).

## Item.cs {#src-5c82f576e8d3}

<code>Software/src/GetSeek.Domain/Catalog/Item.cs</code> · 19 lines.

SHA-256: <code>aa385f91e85797c90f709753d3b99d248bd60f52c3fc350242ef37b950eb5a99</code>.

Declarations: <code>Item</code> (line 5).

## ItemRelationship.cs {#src-ff08907e6445}

<code>Software/src/GetSeek.Domain/Catalog/ItemRelationship.cs</code> · 94 lines.

SHA-256: <code>3086bfc2c6e0c2d04efa4e2e953c9c84f5d2f9f08ba3af5b50f14caedd8937ac</code>.

Declarations: <code>ItemVariant</code> (line 3), <code>ItemKit</code> (line 13), <code>ItemKitComponent</code> (line 24), <code>BillOfMaterials</code> (line 35), <code>BomItem</code> (line 46), <code>ProductionRunStatus</code> (line 57), <code>ProductionRun</code> (line 65), <code>SalesLineKitAllocation</code> (line 83).

## Supplier.cs {#src-55c5d8d515db}

<code>Software/src/GetSeek.Domain/Catalog/Supplier.cs</code> · 17 lines.

SHA-256: <code>6490ebb26dfca0c8736fc275a08de7a844a468cd56ebfc8e714b21370f35366f</code>.

Declarations: <code>Supplier</code> (line 3).

## UnitOfMeasure.cs {#src-a1f4e0c1ce8e}

<code>Software/src/GetSeek.Domain/Catalog/UnitOfMeasure.cs</code> · 9 lines.

SHA-256: <code>6852994dc5a351c00be40878fdf17785591022556ed3ed0fb3bb4d5b32a78f21</code>.

Declarations: <code>UnitOfMeasure</code> (line 3).

## UomConversionEngine.cs {#src-21ec0e311a8a}

<code>Software/src/GetSeek.Domain/Catalog/UomConversionEngine.cs</code> · 107 lines.

SHA-256: <code>1c4030b928a23638ba5370eb3bfb5e7e5963376953ebf77f6bcb058d5e5a6b1d</code>.

Declarations: <code>UomUnitDefinition</code> (line 5), <code>UomConversionResult</code> (line 14), <code>UomConversionEngine</code> (line 23).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ced0d70c7c2b"></span><code>UomConversionEngine.Convert(decimal,UomUnitDefinition,UomUnitDefinition,int?)</code><br>68–106 | Equals @74; Round @87 | InvalidOperationException @76; ArgumentException @81; InvalidOperationException @94 |

</details>

## Barcode.cs {#src-056d8df1aee3}

<code>Software/src/GetSeek.Domain/Common/Barcode.cs</code> · 19 lines.

SHA-256: <code>f539409f76db23e6cda9895bee1833026d8d8b4e7f725e061e4b87ce99d8d6af</code>.

Declarations: <code>Barcode</code> (line 3).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-42c22ccaf7f7"></span><code>Barcode.ToString()</code><br>18–18 | — | No extracted literal effects. |

</details>

## DecimalQuantity.cs {#src-829f8bc948fa}

<code>Software/src/GetSeek.Domain/Common/DecimalQuantity.cs</code> · 220 lines.

SHA-256: <code>7b46af6e2665a3a1716405519fb3f52a062f4829fa33b20800b4e3f4a7c44352</code>.

Declarations: <code>DecimalQuantity</code> (line 13).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-af6adaa9550e"></span><code>DecimalQuantity.ToInvariant(decimal)</code><br>32–33 | ToString @33 | No extracted literal effects. |
| <span id="m-ed950bfa8e84"></span><code>DecimalQuantity.ToInvariantOrNull(decimal?)</code><br>36–37 | ToString @37 | No extracted literal effects. |
| <span id="m-dc9c383c663d"></span><code>DecimalQuantity.TryParseInvariant(string?,decimal)</code><br>40–53 | IsNullOrWhiteSpace @43; TryParse @48; Trim @49 | No extracted literal effects. |
| <span id="m-25a8b3812ad5"></span><code>DecimalQuantity.ResolveQuantity(string?,double?,decimal)</code><br>59–72 | TryParseInvariant @66 | FormatException @71 |
| <span id="m-2706399279fd"></span><code>DecimalQuantity.TryResolveQuantity(string?,double?,decimal,string?)</code><br>79–97 | TryParseInvariant @89 | No extracted literal effects. |
| <span id="m-1dced3d01264"></span><code>DecimalQuantity.ResolveFactor(string?,double?,decimal)</code><br>103–116 | TryParseInvariant @110 | FormatException @115 |
| <span id="m-e2cec2d22545"></span><code>DecimalQuantity.TryResolveFactor(string?,double?,decimal,string?)</code><br>123–142 | TryParseInvariant @133 | No extracted literal effects. |
| <span id="m-6df8f1088fe8"></span><code>DecimalQuantity.TryComputeBaseQuantity(decimal,decimal,decimal,decimal)</code><br>151–174 | Round @167 | No extracted literal effects. |
| <span id="m-c123e98af308"></span><code>DecimalQuantity.TryRoundBaseQuantity(decimal,bool,decimal,string?)</code><br>181–219 | Round @198; Truncate @212 | No extracted literal effects. |

</details>

## Money.cs {#src-76fe6aea0932}

<code>Software/src/GetSeek.Domain/Common/Money.cs</code> · 99 lines.

SHA-256: <code>5f0ea0b9f1f41f79197b6b36ce5323d54f6e7e3511f438eb75d1d363850c25ab</code>.

Declarations: <code>Money : IComparable&lt;Money&gt;</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f87818286fc6"></span><code>Money.Zero(string)</code><br>19–19 | — | No extracted literal effects. |
| <span id="m-529d6b1bb038"></span><code>Money.FromDecimal(decimal,string,int)</code><br>21–25 | ToMinorUnits @23 | No extracted literal effects. |
| <span id="m-c3007883c12b"></span><code>Money.ToDecimal(int)</code><br>27–30 | ToDisplayAmount @29 | No extracted literal effects. |
| <span id="m-1b0d88e61412"></span><code>Money.EnsureSameCurrency(Money,Money)</code><br>86–90 | — | InvalidOperationException @89 |
| <span id="m-06b72a2b6662"></span><code>Money.CompareTo(Money)</code><br>92–96 | EnsureSameCurrency @94; CompareTo @95 | No extracted literal effects. |
| <span id="m-67b6bd379e4e"></span><code>Money.ToString()</code><br>98–98 | ToDecimal @98 | No extracted literal effects. |

</details>

## MoneyPolicy.cs {#src-9807050b78b5}

<code>Software/src/GetSeek.Domain/Common/MoneyPolicy.cs</code> · 32 lines.

SHA-256: <code>1a28ede1f5a4803ebcca3fd445462a1cba53ffa21004cac374589a5d29119dc4</code>.

Declarations: <code>MoneyPolicy</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-8e7ffbe605a3"></span><code>MoneyPolicy.ScalingFactor(int)</code><br>14–23 | nameof @19 | ArgumentOutOfRangeException @18 |
| <span id="m-a23653491241"></span><code>MoneyPolicy.ToMinorUnits(decimal,int)</code><br>26–27 | Round @27; ScalingFactor @27 | No extracted literal effects. |
| <span id="m-53d1350d702b"></span><code>MoneyPolicy.ToDisplayAmount(long,int)</code><br>30–31 | ScalingFactor @31 | No extracted literal effects. |

</details>

## Quantity.cs {#src-b4dc86999368}

<code>Software/src/GetSeek.Domain/Common/Quantity.cs</code> · 74 lines.

SHA-256: <code>e0baaccb34bcd64c7ff91cbbf452dc52744d72722cde59e421c9486524e703e4</code>.

Declarations: <code>Quantity : IComparable&lt;Quantity&gt;</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-71e2ca607ed9"></span><code>Quantity.Zero(string,decimal)</code><br>26–26 | — | No extracted literal effects. |
| <span id="m-2dce83882cd4"></span><code>Quantity.EnsureSameUnit(Quantity,Quantity)</code><br>65–69 | — | InvalidOperationException @68 |
| <span id="m-4eff73de224d"></span><code>Quantity.CompareTo(Quantity)</code><br>71–71 | CompareTo @71 | No extracted literal effects. |
| <span id="m-0b275ace0e5a"></span><code>Quantity.ToString()</code><br>73–73 | — | No extracted literal effects. |

</details>

## Customer.cs {#src-caf1e6842417}

<code>Software/src/GetSeek.Domain/Customers/Customer.cs</code> · 16 lines.

SHA-256: <code>61cfe584675d3a79fa57bdf4bb1ebd6659585a8c874c8d4e513084b15f31947f</code>.

Declarations: <code>Customer</code> (line 3).

## ExpenseRecords.cs {#src-2ae47bf44bc2}

<code>Software/src/GetSeek.Domain/Expenses/ExpenseRecords.cs</code> · 58 lines.

SHA-256: <code>f80a597ee1e49880387836532337a34b03cd0aeb85007c8b6260ee634ab4042d</code>.

Declarations: <code>ExpensePaymentStatuses</code> (line 3), <code>ExpensePaymentKinds</code> (line 22), <code>ExpenseCategory</code> (line 33), <code>ExpenseRecord</code> (line 41).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-75be48ab48a0"></span><code>ExpensePaymentStatuses.DeriveStatus(long,long,bool)</code><br>10–19 | — | No extracted literal effects. |
| <span id="m-e62ce34db691"></span><code>ExpensePaymentKinds.IsValid(string)</code><br>29–30 | Contains @30 | No extracted literal effects. |

</details>

## InventoryLossRecord.cs {#src-cdbd2020e188}

<code>Software/src/GetSeek.Domain/Inventory/InventoryLossRecord.cs</code> · 5 lines.

SHA-256: <code>43db1a1bc7187e6e2eea88ff809851e761e773eafdb2793efc0bcf637da783b3</code>.

Declarations: <code>InventoryLossReason</code> (line 3), <code>InventoryLossResult</code> (line 4).

## ItemLocation.cs {#src-8de22401c448}

<code>Software/src/GetSeek.Domain/Inventory/ItemLocation.cs</code> · 14 lines.

SHA-256: <code>6a7618035c126327a24302c01a2374e4daf95ace2fcb3fc7524384c85ea665d7</code>.

Declarations: <code>ItemLocation</code> (line 3).

## StockMovement.cs {#src-9e738d8395be}

<code>Software/src/GetSeek.Domain/Inventory/StockMovement.cs</code> · 33 lines.

SHA-256: <code>80bbc115c9c5fd13ef4f48e4eeacef752dc37dcb5ed8022ca5d882e1266d726c</code>.

Declarations: <code>StockMovementType</code> (line 3), <code>StockMovement</code> (line 14).

## LicenseClaims.cs {#src-df4d3e8d57ad}

<code>Software/src/GetSeek.Domain/Licensing/LicenseClaims.cs</code> · 28 lines.

SHA-256: <code>9f8207a031cc3630406548b65cc4caceb289b1adf0db0e2d2bbeb7a27450e46c</code>.

Declarations: <code>LicenseClaims</code> (line 3).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d95f0624e6df"></span><code>LicenseClaims.IsModuleActive(string,DateTime)</code><br>15–27 | Contains @17 | No extracted literal effects. |

</details>

## RestaurantOrder.cs {#src-55d1f988647c}

<code>Software/src/GetSeek.Domain/Orders/RestaurantOrder.cs</code> · 103 lines.

SHA-256: <code>386a7ddd829b5f0d68b68f1e237d149caaea26e271e0b9b37b9722e013e58b05</code>.

Declarations: <code>RestaurantOrderStatus</code> (line 7), <code>RestaurantOrder</code> (line 18), <code>RestaurantOrderLine</code> (line 91).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-94ffe0c3aeea"></span><code>RestaurantOrder.SendToKitchen()</code><br>41–47 | — | InvalidOperationException @44 |
| <span id="m-6bfd1d53d01e"></span><code>RestaurantOrder.MarkPreparing()</code><br>49–55 | — | InvalidOperationException @52 |
| <span id="m-9f6762404971"></span><code>RestaurantOrder.MarkReady()</code><br>57–63 | — | InvalidOperationException @60 |
| <span id="m-62b36a98b3da"></span><code>RestaurantOrder.MarkServed()</code><br>65–71 | — | InvalidOperationException @68 |
| <span id="m-4bd97b6f398d"></span><code>RestaurantOrder.Settle(Guid)</code><br>73–80 | — | InvalidOperationException @76 |
| <span id="m-2f4b36326faf"></span><code>RestaurantOrder.Void()</code><br>82–88 | — | InvalidOperationException @85 |

</details>

## SalaryCalculation.cs {#src-d608586c0627}

<code>Software/src/GetSeek.Domain/Payroll/SalaryCalculation.cs</code> · 193 lines.

SHA-256: <code>c19a34363a0444d5021950217660eb977d67443331f2170007169d97171a7594</code>.

Declarations: <code>SalaryProrationResult</code> (line 6), <code>SalaryForecastResult</code> (line 24), <code>SalaryCalculationEngine</code> (line 40).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d2af5f1440da"></span><code>SalaryCalculationEngine.CalculateProration(int,int,DateOnly,DateOnly?,long,long?,int,long,long)</code><br>42–141 | nameof @54; DaysInMonth @68; Round @109 | ArgumentOutOfRangeException @54; ArgumentOutOfRangeException @56; ArgumentOutOfRangeException @58; ArgumentOutOfRangeException @60; ArgumentOutOfRangeException @62; ArgumentOutOfRangeException @64; ArgumentException @66; ArgumentOutOfRangeException @88; ArgumentException @115 |
| <span id="m-32e6f6daf686"></span><code>SalaryCalculationEngine.CalculateRemainingBalance(long,long,long,long,long)</code><br>143–146 | — | No extracted literal effects. |
| <span id="m-a8dde51bc2cd"></span><code>SalaryCalculationEngine.CalculateForecast(long,bool,long,long,long,long,long,long,long,long,long)</code><br>148–192 | CalculateRemainingBalance @163; Max @167 | No extracted literal effects. |

</details>

## SalaryRecords.cs {#src-f78dd5ac3d2d}

<code>Software/src/GetSeek.Domain/Payroll/SalaryRecords.cs</code> · 89 lines.

SHA-256: <code>a40bfa2aa90d10bf9b9433c5d70ac5ed91472cdd40e490a112a1ca96b1bd8fb7</code>.

Declarations: <code>PersonKinds</code> (line 3), <code>SalaryAdjustmentKinds</code> (line 14), <code>SalaryPaymentKinds</code> (line 25), <code>SalaryLedgerEntryTypes</code> (line 37), <code>SalaryPeriodStatuses</code> (line 60), <code>PersonRecord</code> (line 66), <code>SalaryAgreement</code> (line 80).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b48f73ee4860"></span><code>PersonKinds.IsValid(string)</code><br>10–11 | Contains @11 | No extracted literal effects. |
| <span id="m-14c38a39a426"></span><code>SalaryAdjustmentKinds.IsValid(string)</code><br>21–22 | Contains @22 | No extracted literal effects. |
| <span id="m-70523d63a0d4"></span><code>SalaryPaymentKinds.IsValid(string)</code><br>33–34 | Contains @34 | No extracted literal effects. |
| <span id="m-71a9ba243036"></span><code>SalaryLedgerEntryTypes.IsValid(string)</code><br>56–57 | Contains @57 | No extracted literal effects. |

</details>

## SalaryStatementSnapshot.cs {#src-8e246ebe0155}

<code>Software/src/GetSeek.Domain/Payroll/SalaryStatementSnapshot.cs</code> · 81 lines.

SHA-256: <code>ad06910613b9690e983d610b348a09e98742fbc7c8cf5d804f8cf28980edcfb3</code>.

Declarations: <code>SalaryStatementAdjustmentItem</code> (line 3), <code>SalaryStatementPaymentItem</code> (line 12), <code>SalaryStatementCorrectionItem</code> (line 27), <code>SalaryStatementSnapshot</code> (line 39).

## PricingCalculationEngine.cs {#src-d7d3ebe3099f}

<code>Software/src/GetSeek.Domain/Pricing/PricingCalculationEngine.cs</code> · 338 lines.

SHA-256: <code>96442e99e5a8b7348bf4a3cf388640cf0e15d86993be6740a8190eb3ba5feea1</code>.

Declarations: <code>PricingMethod</code> (line 5), <code>RoundingRule</code> (line 13), <code>TierWeightMode</code> (line 32), <code>TierDefinition</code> (line 40), <code>ItemPricingSpec</code> (line 49), <code>TierPriceSpec</code> (line 58), <code>PricingCalculationEngine</code> (line 69).

<details markdown>
<summary>Methods, calls, table effects and failures (19)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-88da3bff5a21"></span><code>PricingCalculationEngine.ResolveEffectiveBasePrice(ItemPricingSpec,long,int)</code><br>74–78 | ResolveEffectiveBasePrice @78 | No extracted literal effects. |
| <span id="m-c4dca5bf42cf"></span><code>PricingCalculationEngine.ResolveEffectiveBasePrice(ItemPricingSpec,decimal,int)</code><br>84–92 | CalculateUnroundedBasePriceMinor @89; ApplyRoundingRule @90; Round @91 | No extracted literal effects. |
| <span id="m-ff8e4293bca1"></span><code>PricingCalculationEngine.CalculateUnroundedBasePriceMinor(ItemPricingSpec,decimal,int)</code><br>99–119 | nameof @106; ScalingFactor @109 | ArgumentOutOfRangeException @106 |
| <span id="m-d9b2482207d5"></span><code>PricingCalculationEngine.ApplyRoundingRule(long,RoundingRule,int,long)</code><br>122–123 | Round @123; ApplyRoundingRule @123 | No extracted literal effects. |
| <span id="m-d5606294996b"></span><code>PricingCalculationEngine.ApplyRoundingRule(decimal,RoundingRule,int)</code><br>126–127 | ApplyRoundingRule @127 | No extracted literal effects. |
| <span id="m-8259bb3f9ed3"></span><code>PricingCalculationEngine.ApplyRoundingRule(decimal,RoundingRule,int,long)</code><br>129–168 | ScalingFactor @131; nameof @134; Ceiling @139; Floor @139; Round @160; RoundToEnding @164 | ArgumentOutOfRangeException @134 |
| <span id="m-77a7f700d66b"></span><code>PricingCalculationEngine.ResolveTierPrice(long,TierPriceSpec,TierDefinition,int)</code><br>171–186 | ApplyWeight @183; ParseStoredPercentage @184 | No extracted literal effects. |
| <span id="m-07768a060503"></span><code>PricingCalculationEngine.ResolveEffectiveTier(IReadOnlyList&lt;TierDefinition&gt;,string?,int)</code><br>192–210 | IsNullOrWhiteSpace @197; ToLowerInvariant @199; Trim @199; FirstOrDefault @201; Equals @202 | No extracted literal effects. |
| <span id="m-7e36defda1f0"></span><code>PricingCalculationEngine.ResolveCostFloor(long,decimal)</code><br>213–222 | Round @221 | No extracted literal effects. |
| <span id="m-40553425b43d"></span><code>PricingCalculationEngine.IsBelowCostFloor(long,long)</code><br>225–226 | — | No extracted literal effects. |
| <span id="m-fa631143f3ce"></span><code>PricingCalculationEngine.ParseWeight(string?)</code><br>228–231 | TryParse @229 | No extracted literal effects. |
| <span id="m-32e94cc25f3e"></span><code>PricingCalculationEngine.ParseStoredPercentage(string?,int)</code><br>237–245 | ParseWeight @239 | No extracted literal effects. |
| <span id="m-36824438793b"></span><code>PricingCalculationEngine.ParsePricingMethod(string?)</code><br>247–254 | ToLowerInvariant @248; Trim @248 | No extracted literal effects. |
| <span id="m-836509e8fb04"></span><code>PricingCalculationEngine.ParseRoundingRule(string?)</code><br>256–273 | ToLowerInvariant @257; Trim @257 | No extracted literal effects. |
| <span id="m-c735968d8d0e"></span><code>PricingCalculationEngine.IsRoundingRuleCompatible(RoundingRule,int)</code><br>275–279 | ScalingFactor @277 | No extracted literal effects. |
| <span id="m-bdab6bf061bd"></span><code>PricingCalculationEngine.TryConvertRoundingIncrement(decimal,int,long)</code><br>282–309 | ScalingFactor @292; Truncate @293; ToInt64 @298 | No extracted literal effects. |
| <span id="m-9e9468cfd655"></span><code>PricingCalculationEngine.ParseWeightMode(string?)</code><br>311–317 | ToLowerInvariant @312; Trim @312 | No extracted literal effects. |
| <span id="m-acbca5ed2ab6"></span><code>PricingCalculationEngine.ApplyWeight(long,decimal)</code><br>319–329 | Round @328 | InvalidOperationException @325 |
| <span id="m-f5fa15a9c52a"></span><code>PricingCalculationEngine.RoundToEnding(decimal,long,int)</code><br>331–337 | Floor @335 | No extracted literal effects. |

</details>

## DraftCart.cs {#src-9fd7401a5041}

<code>Software/src/GetSeek.Domain/Sales/DraftCart.cs</code> · 110 lines.

SHA-256: <code>a74ec9c478333949082b400c1253dd08e44ff6c5787bc390f24ae822342b2bff</code>.

Declarations: <code>CartStatus</code> (line 5), <code>DraftCart</code> (line 13), <code>DraftCartLine</code> (line 85).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d99453233489"></span><code>DraftCart.Recalculate(string,int)</code><br>38–76 | Zero @41; Round @57 | No extracted literal effects. |
| <span id="m-1f60d959139c"></span><code>DraftCart.CalculateSubtotal(string)</code><br>78–82 | Recalculate @80 | No extracted literal effects. |
| <span id="m-51808f0b0384"></span><code>DraftCartLine.CalculateLineTotal()</code><br>102–109 | Zero @107 | No extracted literal effects. |

</details>

## Fulfillment.cs {#src-f31c70a09bb4}

<code>Software/src/GetSeek.Domain/Sales/Fulfillment.cs</code> · 24 lines.

SHA-256: <code>932a39aab6ac4b696ae2d35030237c08786fc2b44f8b29cc2a55145f51ef6287</code>.

Declarations: <code>FulfillmentPolicy</code> (line 3), <code>ShipmentSummary</code> (line 4), <code>ReservationStock</code> (line 6), <code>ShipmentDispatchLine</code> (line 8), <code>SupplierInvoiceLineInput</code> (line 9), <code>SupplierInvoiceSummary</code> (line 11), <code>SupplierInvoiceLine</code> (line 17), <code>MoneyAccount</code> (line 19), <code>MoneyEventRow</code> (line 22).

## InvoiceSettlement.cs {#src-57835c8a7a35}

<code>Software/src/GetSeek.Domain/Sales/InvoiceSettlement.cs</code> · 17 lines.

SHA-256: <code>5f2a3fa68dc24982fd54f4c7336bd37c8a300863130c3de131040c83df59114e</code>.

Declarations: <code>PaymentState</code> (line 3), <code>InvoiceBalance</code> (line 5), <code>InvoiceCollectionAllocation</code> (line 15), <code>InvoiceCollectionResult</code> (line 16).

## SaleDiscountRecord.cs {#src-5636c49d6d6b}

<code>Software/src/GetSeek.Domain/Sales/SaleDiscountRecord.cs</code> · 3 lines.

SHA-256: <code>40ffc5cac836081bf5fd6e8426beed3293e0105b92d939fb66daab3073003d56</code>.

Declarations: <code>SaleDiscountKind</code> (line 3).

## SaleReturn.cs {#src-9f4f69e6379b}

<code>Software/src/GetSeek.Domain/Sales/SaleReturn.cs</code> · 24 lines.

SHA-256: <code>f66594155b93e079e4715209e2da6dce0d112d00a18119ae2d7bebca60e34114</code>.

Declarations: <code>ReturnFinancialMode</code> (line 3), <code>ReturnDisposition</code> (line 4), <code>InspectionResolution</code> (line 5), <code>ReturnDispositionState</code> (line 6), <code>ReturnStockAllocation</code> (line 8), <code>SaleReturnRequestLine</code> (line 10), <code>SaleReturnPreview</code> (line 12), <code>SaleReturnResult</code> (line 14), <code>InspectionResolutionResult</code> (line 15), <code>SerialLifecycle</code> (line 18).

## SalesInvoice.cs {#src-ac1a514f33ac}

<code>Software/src/GetSeek.Domain/Sales/SalesInvoice.cs</code> · 77 lines.

SHA-256: <code>fb9e8cc504cac6094674d3f8c7fd1ebaac7cfc230fafe3442f885adf5e32d163</code>.

Declarations: <code>InvoiceStatus</code> (line 5), <code>SalesInvoice</code> (line 13), <code>SalesLine</code> (line 38), <code>TenderType</code> (line 57), <code>SalesTender</code> (line 66).

## AuditJournalEntry.cs {#src-2a1272b271ec}

<code>Software/src/GetSeek.Domain/Security/AuditJournalEntry.cs</code> · 31 lines.

SHA-256: <code>bc719e297d59dd473d6ec4e979447e28abc87c70bc37b5c5ad794df84f8895eb</code>.

Declarations: <code>AuditJournalEntry</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-511ac4979c9e"></span><code>AuditJournalEntry.ComputeHash(long,Guid,string,string?,string,DateTime,string,string?,string,string)</code><br>20–23 | ComputeHash @22; ToString @22 | No extracted literal effects. |
| <span id="m-d9cf5fe42a8d"></span><code>AuditJournalEntry.ComputeHash(long,Guid,string,string?,string,string,string,string?,string,string)</code><br>25–30 | HashData @28; GetBytes @28; ToHexStringLower @29 | No extracted literal effects. |

</details>

## User.cs {#src-e893c6c105b0}

<code>Software/src/GetSeek.Domain/Security/User.cs</code> · 75 lines.

SHA-256: <code>1de2eb4192d982e04ac0ab519d9fb14daa980aac630285b1fc28972baec47a8b</code>.

Declarations: <code>User</code> (line 3), <code>Permissions</code> (line 16).

## AXAML, migrations and project inputs

### GetSeek.Domain.csproj {#src-451049a93604}

<code>Software/src/GetSeek.Domain/GetSeek.Domain.csproj</code> · 9 lines · SHA-256 <code>78d031fb03738084bdcfdb37797bd74ce1322c55a5ae6f76d7e8c882999fc86d</code>.
