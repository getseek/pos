---
id: PP-REVIEW-CODE-INFRASTRUCTURE
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: []
---

# GetSeek.Infrastructure source catalogue

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.Infrastructure.csproj:1](code-infrastructure.md#src-2a58abaee0e2). Dependencies: <code>GetSeek.Application</code>, <code>GetSeek.Domain</code>.

## SqliteBackupService.cs {#src-5d8691cafdb2}

<code>Software/src/GetSeek.Infrastructure/Backup/SqliteBackupService.cs</code> · 95 lines.

SHA-256: <code>69cba2246f74ab8c85007001fd8687af33f356f95f9e3c1f99f3181a55b928ad</code>.

Declarations: <code>BackupManifest</code> (line 8), <code>SqliteBackupService</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7481ec5826fa"></span><code>SqliteBackupService.CreateBackupAsync(string,string,CancellationToken)</code><br>19–59 | CreateDirectory @24; NewGuid @25; ToString @26; Combine @28; ConfigureAwait @35; OpenAsync @35; OpenAsync @36; BackupDatabase @38; CloseAsync @39; CloseAsync @40; ClearAllPools @42; ReadAllBytesAsync @45; ToHexStringLower @46; HashData @46; Serialize @55; WriteAllTextAsync @56 | No extracted literal effects. |
| <span id="m-acabc1903b90"></span><code>SqliteBackupService.VerifyAndRestoreStagingAsync(string,string,string,CancellationToken)</code><br>61–94 | Exists @67; ConfigureAwait @71; ReadAllBytesAsync @71; ToHexStringLower @72; HashData @72; Equals @73; Copy @77; OpenAsync @83; CreateCommand @85; ExecuteScalarAsync @87; ToString @88; CloseAsync @89; ClearAllPools @91 | No extracted literal effects. |

</details>

## MeasuredDiagnosticsService.cs {#src-fb36b5fd2a02}

<code>Software/src/GetSeek.Infrastructure/Diagnostics/MeasuredDiagnosticsService.cs</code> · 126 lines.

SHA-256: <code>fb6ae4e43eead0d0dc353614d0528e4460f1d95563b62994602505a7cea28bbf</code>.

Declarations: <code>DiagnosticState</code> (line 11), <code>DiagnosticProbeResult</code> (line 19), <code>MeasuredDiagnosticsService</code> (line 27).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-321c9d8bbdec"></span><code>MeasuredDiagnosticsService.ProbeDatabaseAsync(DbConnection,CancellationToken)</code><br>29–59 | StartNew @31; CreateCommand @34; ToString @36; ConfigureAwait @36; ExecuteScalarAsync @36; Stop @37; Equals @39 | No extracted literal effects. |
| <span id="m-06e5845bea79"></span><code>MeasuredDiagnosticsService.ProbeLicense(ILicenseService?)</code><br>66–110 | StartNew @79; VerifyDeviceBinding @84; IsModuleLicensed @85; Stop @89 | No extracted literal effects. |
| <span id="m-8b7447c71776"></span><code>MeasuredDiagnosticsService.ProbeHardwareStubs()</code><br>116–125 | — | No extracted literal effects. |

</details>

## OperationalLogger.cs {#src-8047f70ae92f}

<code>Software/src/GetSeek.Infrastructure/Diagnostics/OperationalLogger.cs</code> · 20 lines.

SHA-256: <code>2c1c52bbf8322f177896c70e0b75be10a2e47913e35ab2c14519f53368dfbb59</code>.

Declarations: <code>OperationalLogger : IOperationalLogger</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7f0901a0be06"></span><code>OperationalLogger.LogFailure(string,string,string,string,Exception?)</code><br>18–19 | LogDiagnostic @19 | No extracted literal effects. |

</details>

## RuntimeErrorLogger.cs {#src-ef7cd82deec2}

<code>Software/src/GetSeek.Infrastructure/Diagnostics/RuntimeErrorLogger.cs</code> · 140 lines.

SHA-256: <code>c4616e55d35d6fe8e8aee9baf8592dd15c23054640d4f8f029c2cc650fc78f1e</code>.

Declarations: <code>RuntimeErrorLogger</code> (line 13).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-286c4995cb4e"></span><code>RuntimeErrorLogger.Log(string,string,string,Exception?)</code><br>34–35 | WriteLine @35 | No extracted literal effects. |
| <span id="m-33db44d0d9a6"></span><code>RuntimeErrorLogger.LogAction(string,string,string,string,Exception?)</code><br>37–38 | WriteLine @38 | No extracted literal effects. |
| <span id="m-840f0fc92e12"></span><code>RuntimeErrorLogger.LogDiagnostic(string,string,string,string,Exception?,string?)</code><br>44–45 | WriteLine @45 | No extracted literal effects. |
| <span id="m-19c235d5c9ed"></span><code>RuntimeErrorLogger.WriteLine(string,string,string,string,string?,Exception?,string?)</code><br>47–99 | CreateDirectory @58; Combine @65; RotateIfNeeded @66; Append @69; Append @69; ToString @69; IsNullOrEmpty @71; GetType @87; AppendAllText @91; ToString @91 | No extracted literal effects. |
| <span id="m-596f91b5f5d8"></span><code>RuntimeErrorLogger.RotateIfNeeded(string)</code><br>101–116 | Copy @108; Delete @109 | No extracted literal effects. |
| <span id="m-4fbd224894fe"></span><code>RuntimeErrorLogger.Sanitize(string)</code><br>122–139 | IsNullOrEmpty @124; Replace @130 | No extracted literal effects. |

</details>

## SqliteExportService.cs {#src-ae1722989210}

<code>Software/src/GetSeek.Infrastructure/Exporting/SqliteExportService.cs</code> · 559 lines.

SHA-256: <code>b608048a32eee4a0628480c069ba844098ff19493a73459bd225b7db4df01e20</code>.

Declarations: <code>SqliteExportService : IExportService</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (21)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e47a857334ac"></span><code>SqliteExportService.ExportDocumentAsync(ExportRequest,CancellationToken)</code><br>47–128 | IsNullOrWhiteSpace @57; ConfigureAwait @64; OpenAsync @64; BeginTransaction @65; HasCurrentExportPermissionAsync @66; ResolveSourceAsync @69; HasSafeBounds @73; Commit @76; ToString @80; ToString @81; NewGuid @81; TrimEnd @83; GetFullPath @83; Combine @85; StartsWith @86; BuildPdfContent @94; Render @95; SanitizedExportContent @95; BuildCsv @99; GetBytes @100; WriteAllBytesAsync @105; Move @106; Exists @115; Delete @115; ToUpperInvariant @125 | No extracted literal effects. |
| <span id="m-a85d9fea345b"></span><code>SqliteExportService.HasCurrentExportPermissionAsync(SqliteConnection,SqliteTransaction,Guid,CancellationToken)</code><br>130–152 | CreateCommand @133; AddWithValue @150; ToString @150; ToInt32 @151; ConfigureAwait @151; ExecuteScalarAsync @151 | FROM user_permission_overrides @135; FROM user_roles @135; FROM users @135; JOIN role_permissions @135 |
| <span id="m-0d196c9752de"></span><code>SqliteExportService.ResolveSourceAsync(SqliteConnection,SqliteTransaction,ExportSelector,CancellationToken)</code><br>154–169 | ConfigureAwait @160; LoadReceiptPayloadAsync @160; LoadShiftReportPayloadAsync @162; LoadSalesReportPayloadAsync @164; LoadInventorySnapshotPayloadAsync @166 | No extracted literal effects. |
| <span id="m-de3c8ce7a032"></span><code>SqliteExportService.LoadReceiptPayloadAsync(SqliteConnection,SqliteTransaction,Guid,CancellationToken)</code><br>171–219 | CreateCommand @180; AddWithValue @184; ToString @184; ConfigureAwait @185; ExecuteReaderAsync @185; ReadAsync @186; GetString @187; Parse @188; IsDBNull @189; GetInt64 @190; ToInt32 @197; ExecuteScalarAsync @197; ToString @199; Pow @199; Clamp @199; AddWithValue @205; ExecuteReaderAsync @206; Add @208; Money @209; ToString @215 | FROM sales_invoices @183; FROM sales_lines @204; FROM store_config @196; FROM store_config @214 |
| <span id="m-23b1c3806882"></span><code>SqliteExportService.LoadShiftReportPayloadAsync(SqliteConnection,SqliteTransaction,Guid,CancellationToken)</code><br>221–265 | CreateCommand @224; AddWithValue @234; ToString @234; ConfigureAwait @239; ExecuteReaderAsync @239; ReadAsync @241; Parse @242; GetString @242; GetInt64 @245; GetInt32 @246; ToInt32 @254; ExecuteScalarAsync @254; ToString @259; ToString @260; AddRange @262; Select @262; Money @262 | FROM shift_z_reports @226; FROM store_config @253 |
| <span id="m-84384d1b1e0a"></span><code>SqliteExportService.LoadSalesReportPayloadAsync(SqliteConnection,SqliteTransaction,SalesReportExportSelector,CancellationToken)</code><br>267–302 | FromDays @271; ConfigureAwait @274; ReadDecimalPlacesAsync @274; CreateCommand @275; AddWithValue @284; ToString @284; ToString @285; ExecuteReaderAsync @288; ReadAsync @289; Add @291; GetString @292; Money @293; GetInt64 @293; StatusLabel @299; GetInt32 @299 | FROM sales_invoices @277 · InvalidDataException @273 |
| <span id="m-61e5783faa8b"></span><code>SqliteExportService.LoadInventorySnapshotPayloadAsync(SqliteConnection,SqliteTransaction,InventorySnapshotExportSelector,CancellationToken)</code><br>304–336 | CreateCommand @309; Trim @318; AddWithValue @319; EscapeLike @320; ConfigureAwait @323; ExecuteReaderAsync @323; ReadAsync @325; Add @326; Parse @326; GetString @326; GetInt32 @327; GetPhysicalOnHandByItemsAsync @329; ToArray @330; Select @330; ToString @333; GetValueOrDefault @333 | FROM items @311; JOIN product_categories @311 · InvalidDataException @308 |
| <span id="m-61afc8f15a80"></span><code>SqliteExportService.ReadDecimalPlacesAsync(SqliteConnection,SqliteTransaction,CancellationToken)</code><br>338–344 | CreateCommand @340; Clamp @343; ToInt32 @343; ConfigureAwait @343; ExecuteScalarAsync @343 | FROM store_config @342 |
| <span id="m-3bd1b7a8891f"></span><code>SqliteExportService.Money(long,string,int)</code><br>346–347 | ToString @347; Pow @347; Clamp @347 | No extracted literal effects. |
| <span id="m-84d552fb786c"></span><code>SqliteExportService.StatusLabel(int)</code><br>349–356 | — | No extracted literal effects. |
| <span id="m-829fdc5f9e1e"></span><code>SqliteExportService.EscapeLike(string)</code><br>358–359 | Replace @358; Replace @358 | No extracted literal effects. |
| <span id="m-d35cbff31e4e"></span><code>SqliteExportService.PayloadMatchesType(ExportDocumentType,ExportPayload)</code><br>361–367 | — | No extracted literal effects. |
| <span id="m-3c4179bab3bc"></span><code>SqliteExportService.HasSafeBounds(ExportPayload)</code><br>369–402 | Select @373; Select @374; Select @375 | No extracted literal effects. |
| <span id="m-b3071e90c354"></span><code>SqliteExportService.BuildPdfContent(ExportPayload)</code><br>404–445 | Clamp @408; Pow @409; ToString @410; IsNullOrWhiteSpace @423; Add @423; AddRange @425; Select @425; Money @426; Join @432; AddRange @443; Select @443 | InvalidDataException @416; InvalidDataException @436 |
| <span id="m-e4b9be2bf504"></span><code>SqliteExportService.BuildCsv(ExportDocumentType,TabularExportPayload)</code><br>447–463 | Any @449; ToArray @451; AddRange @452; Select @452; ToArray @452; Contains @456; Any @457; MaskPhone @460; EscapeCsvContent @462; Join @462; Select @462; Select @462 | InvalidDataException @450 |
| <span id="m-909746621205"></span><code>SqliteExportService.MaskPhone(string)</code><br>465–469 | ToArray @467; Where @467; Min @468 | No extracted literal effects. |
| <span id="m-126c4f015355"></span><code>SqliteExportService.SanitizedExportContent(string)</code><br>471–493 | IsNullOrEmpty @473; Replace @478 | No extracted literal effects. |
| <span id="m-b3a4e1085c10"></span><code>SqliteExportService.EscapeCsvContent(string)</code><br>495–515 | IsNullOrEmpty @497; ParseCsvRecords @498; IsWhiteSpace @507; IsControl @507; QuoteCsvCell @509; Append @511; Join @511; ToString @514 | No extracted literal effects. |
| <span id="m-682780f95601"></span><code>SqliteExportService.ParseCsvRecords(string)</code><br>517–548 | Append @529; Add @535; ToString @535; Clear @535; Add @540 | No extracted literal effects. |
| <span id="m-f3314e7ad7d4"></span><code>SqliteExportService.QuoteCsvCell(string)</code><br>550–553 | IndexOfAny @551; Equals @551; Trim @551; Replace @552 | No extracted literal effects. |
| <span id="m-81ece5078a46"></span><code>SqliteExportService.RenderMinimalPdfBytes(string,string)</code><br>555–558 | Render @557 | No extracted literal effects. |

</details>

## UnicodePdfRenderer.cs {#src-6c55a001c290}

<code>Software/src/GetSeek.Infrastructure/Exporting/UnicodePdfRenderer.cs</code> · 117 lines.

SHA-256: <code>c467aeb400f83ef4e3145b2e605d3e7edda97420d8055f6725075719338c53e5</code>.

Declarations: <code>UnicodePdfRenderer</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-61580907a98f"></span><code>UnicodePdfRenderer.Render(string,string)</code><br>23–72 | FromFamilyName @25; Split @31; Wrap @33; AddRange @34; Max @38; Floor @38; Ceiling @39; CreatePdf @43; Clear @52; DrawShapedText @53; Min @55; Flush @61; FromBitmap @64; BeginPage @65; DrawImage @66; EndPage @67; Close @69; ToArray @71 | InvalidDataException @40 |
| <span id="m-35fbb0883055"></span><code>UnicodePdfRenderer.Wrap(string,float,SKShaper,SKPaint)</code><br>74–113 | IsNullOrEmpty @76; Split @79; Measure @82; Append @84; Add @90; ToString @90; Clear @91; SubstringByTextElements @102 | No extracted literal effects. |
| <span id="m-d19cbd15f2a8"></span><code>UnicodePdfRenderer.Measure(string,SKShaper,SKPaint)</code><br>115–116 | Shape @116 | No extracted literal effects. |

</details>

## BarcodeRasterizer.cs {#src-0a006ec021e6}

<code>Software/src/GetSeek.Infrastructure/Hardware/BarcodeRasterizer.cs</code> · 95 lines.

SHA-256: <code>e8350901482460eadadfa80268c576a45e7ea18fae77763d96bd972f27047a6b</code>.

Declarations: <code>BarcodeSymbology</code> (line 9), <code>BarcodeRasterizer</code> (line 19).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b668439f4c6b"></span><code>BarcodeRasterizer.RenderPng(string,BarcodeSymbology,int,int)</code><br>21–44 | Normalize @23; nameof @25; ToZxingFormat @29; Write @38; Copy @40; GetPixels @40; FromBitmap @41; Encode @42; ToArray @43 | ArgumentOutOfRangeException @25 |
| <span id="m-bf72cba03cd7"></span><code>BarcodeRasterizer.DefaultFor(string)</code><br>47–47 | — | No extracted literal effects. |
| <span id="m-d1cb134f091d"></span><code>BarcodeRasterizer.ToZxingFormat(BarcodeSymbology)</code><br>49–58 | nameof @57 | No extracted literal effects. |
| <span id="m-604e18463a64"></span><code>BarcodeRasterizer.Normalize(string?,BarcodeSymbology)</code><br>60–74 | Trim @62; nameof @64; NormalizeGs1 @68; All @71 | ArgumentException @64 |
| <span id="m-5e9bf2b82963"></span><code>BarcodeRasterizer.NormalizeGs1(string,int,int,string)</code><br>76–86 | All @78; CalculateMod10CheckDigit @82 | ArgumentException @79; ArgumentException @84 |
| <span id="m-8ad0e8240c6f"></span><code>BarcodeRasterizer.CalculateMod10CheckDigit(string)</code><br>88–94 | — | No extracted literal effects. |

</details>

## BarcodeScannerWedgeFilter.cs {#src-ef1b946b6193}

<code>Software/src/GetSeek.Infrastructure/Hardware/BarcodeScannerWedgeFilter.cs</code> · 135 lines.

SHA-256: <code>8fabfd00ba2740aa9f31cf86cc390d7f97912b072ba29445180e4094fb5a1da7</code>.

Declarations: <code>BarcodeScanType</code> (line 7), <code>ParsedBarcode</code> (line 14), <code>BarcodeScannerWedgeFilter</code> (line 24).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4a309811d07f"></span><code>BarcodeScannerWedgeFilter.ProcessKeyStroke(char,long)</code><br>32–72 | Clear @41; Trim @52; ToString @52; IsNullOrEmpty @55; ParseBarcode @57; Invoke @58; IsControl @66; Append @68 | No extracted literal effects. |
| <span id="m-c375d198e157"></span><code>BarcodeScannerWedgeFilter.ParseBarcode(string)</code><br>74–98 | Contains @77; ParseGs1 @79; StartsWith @85; All @85; Substring @87; TryParse @89 | No extracted literal effects. |
| <span id="m-9276e9e0c69b"></span><code>BarcodeScannerWedgeFilter.ParseGs1(string)</code><br>100–134 | Match @107; TryParseExact @117; SpecifyKind @119 | No extracted literal effects. |

</details>

## EscPosRasterizer.cs {#src-f966d960ba3c}

<code>Software/src/GetSeek.Infrastructure/Hardware/EscPosRasterizer.cs</code> · 49 lines.

SHA-256: <code>9bb285b8e2465858d5b5d64e753771a69a742f566a3ae019c56644f1185fdc70</code>.

Declarations: <code>EscPosRasterizer</code> (line 3).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-88533d9f03ca"></span><code>EscPosRasterizer.RasterizeBitmap(bool[,],int,int)</code><br>11–48 | WriteByte @21; ToArray @47 | No extracted literal effects. |

</details>

## EscPosReceiptBuilder.cs {#src-2a7cca5e09b8}

<code>Software/src/GetSeek.Infrastructure/Hardware/EscPosReceiptBuilder.cs</code> · 146 lines.

SHA-256: <code>0122514f88b4615e97f68da6fa123dfceb39f63bdb851cdd7472d952d73aa0ee</code>.

Declarations: <code>EscPosAlignment</code> (line 5), <code>PaperCutMode</code> (line 12), <code>EscPosReceiptBuilder : IDisposable</code> (line 18).

<details markdown>
<summary>Methods, calls, table effects and failures (14)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3534c2497c05"></span><code>EscPosReceiptBuilder.Dispose()</code><br>22–26 | Dispose @24; SuppressFinalize @25 | No extracted literal effects. |
| <span id="m-1db1b43df68c"></span><code>EscPosReceiptBuilder.Initialize()</code><br>28–34 | WriteByte @31 | No extracted literal effects. |
| <span id="m-2244a06a6f90"></span><code>EscPosReceiptBuilder.SetAlignment(EscPosAlignment)</code><br>36–43 | WriteByte @39 | No extracted literal effects. |
| <span id="m-979c22410dc4"></span><code>EscPosReceiptBuilder.SetBold(bool)</code><br>45–52 | WriteByte @48 | No extracted literal effects. |
| <span id="m-c63d176c7236"></span><code>EscPosReceiptBuilder.SetDoubleSize(bool,bool)</code><br>54–64 | WriteByte @60 | No extracted literal effects. |
| <span id="m-8f04d4184296"></span><code>EscPosReceiptBuilder.WriteText(string)</code><br>66–71 | GetBytes @68; Write @69 | No extracted literal effects. |
| <span id="m-dc313e3b7bd9"></span><code>EscPosReceiptBuilder.WriteLine(string)</code><br>73–81 | IsNullOrEmpty @75; WriteText @77; WriteByte @79 | No extracted literal effects. |
| <span id="m-0d16f311bb92"></span><code>EscPosReceiptBuilder.WriteKeyValue(string,string,int)</code><br>83–92 | WriteLine @90 | No extracted literal effects. |
| <span id="m-5ef5c932abd6"></span><code>EscPosReceiptBuilder.WriteDivider(char,int)</code><br>94–98 | WriteLine @96 | No extracted literal effects. |
| <span id="m-4cb390f3b663"></span><code>EscPosReceiptBuilder.FeedLines(int)</code><br>100–107 | WriteByte @104 | No extracted literal effects. |
| <span id="m-0649d09ff703"></span><code>EscPosReceiptBuilder.CutPaper(PaperCutMode)</code><br>109–118 | FeedLines @112; WriteByte @114 | No extracted literal effects. |
| <span id="m-a32b834a9e40"></span><code>EscPosReceiptBuilder.KickDrawer(byte,byte,byte)</code><br>120–130 | WriteByte @124 | No extracted literal effects. |
| <span id="m-2e20a9ba2e98"></span><code>EscPosReceiptBuilder.QueryRealTimeStatus(byte)</code><br>132–140 | WriteByte @136 | No extracted literal effects. |
| <span id="m-9f1db6e25c16"></span><code>EscPosReceiptBuilder.Build()</code><br>142–145 | ToArray @144 | No extracted literal effects. |

</details>

## FinancialReceiptRenderer.cs {#src-2b8172a68ae6}

<code>Software/src/GetSeek.Infrastructure/Hardware/FinancialReceiptRenderer.cs</code> · 43 lines.

SHA-256: <code>360d28fd56445229b3dcaf3f475eb21de83473ca8bac9d2ee5cdd81ee601bda1</code>.

Declarations: <code>FinancialReceiptRenderer</code> (line 10), <code>Document</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b79bd34fa9eb"></span><code>FinancialReceiptRenderer.BuildAsync(SqliteConnection,string,bool,CancellationToken)</code><br>13–37 | Parse @15; GetString @16; GetProperty @16; TryGetProperty @17; ToString @17; TryGetInt64 @18; Text @20; Number @20; IsNullOrWhiteSpace @21; ToString @22; ToDecimal @22; MoneyText @23; TryGetProperty @25; CreateCommand @27; AddWithValue @27; GetString @27; ConfigureAwait @28; ExecuteScalarAsync @28; Deserialize(ReceiptDesignDocument) @29; ToList @32; Select @32; EnumerateArray @32; GetProperty @32; GetProperty @32; GetDecimal @32; GetInt64 @32; Insert @34; EnumerateArray @35; Add @35; GetString @35; Split @36; Render @36 | FROM receipt_design_versions @27 · InvalidDataException @21 |
| <span id="m-b8075485e560"></span><code>FinancialReceiptRenderer.Thermal(Document,OutputDeviceSettings)</code><br>38–42 | Add @40; AddRange @40; Render @41 | No extracted literal effects. |

</details>

## OutputDeviceSettings.cs {#src-1316566065d4}

<code>Software/src/GetSeek.Infrastructure/Hardware/OutputDeviceSettings.cs</code> · 202 lines.

SHA-256: <code>0c82016fc9b1711ea1e525c490a2d860fe4dc676e8231471bba32034b7e31e1e</code>.

Declarations: <code>OutputDeviceSettings</code> (line 7), <code>OutputDeviceSettingsStore</code> (line 23).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-28bc61d2bdfa"></span><code>OutputDeviceSettingsStore.MarkThermalTestSpoolAcceptedAsync(DbConnection,ISessionContext,string,CancellationToken)</code><br>25–53 | HasPermission @31; IsNullOrWhiteSpace @33; nameof @34; ConfigureAwait @35; BeginTransactionAsync @35; CreateCommand @36; CreateParameter @40; ToString @40; Add @40; ToInt64 @41; ExecuteScalarAsync @41; Add @47; ToString @47; ExecuteNonQueryAsync @50; CommitAsync @52 | FROM users @39; JOIN user_roles @39; UPDATE output_device_config @46 · UnauthorizedAccessException @32; ArgumentException @34; UnauthorizedAccessException @42; InvalidOperationException @51 |
| <span id="m-aa56424d4d57"></span><code>OutputDeviceSettingsStore.ConfirmThermalPhysicalTestAsync(DbConnection,ISessionContext,string,CancellationToken)</code><br>55–81 | HasPermission @61; ConfigureAwait @63; BeginTransactionAsync @63; CreateCommand @64; Add @68; ToString @68; ToInt64 @69; ExecuteScalarAsync @69; ToString @75; ExecuteNonQueryAsync @78; CommitAsync @80 | FROM users @67; JOIN user_roles @67; UPDATE output_device_config @74 · UnauthorizedAccessException @62; UnauthorizedAccessException @70; InvalidOperationException @79 |
| <span id="m-256a6888852a"></span><code>OutputDeviceSettingsStore.InvalidateThermalVerificationAsync(DbConnection,CancellationToken)</code><br>83–88 | CreateCommand @85; ConfigureAwait @87; ExecuteNonQueryAsync @87 | UPDATE output_device_config @86 |
| <span id="m-8e4517a1cdcd"></span><code>OutputDeviceSettingsStore.Add(DbCommand,string,object)</code><br>90–93 | CreateParameter @92; Add @92 | No extracted literal effects. |
| <span id="m-fb485e0e9572"></span><code>OutputDeviceSettingsStore.ReadAsync(DbConnection,CancellationToken)</code><br>95–117 | CreateCommand @97; ConfigureAwait @108; ExecuteReaderAsync @108; ReadAsync @109; GetString @110; GetInt32 @110; IsDBNull @111 | FROM output_device_config @98 |
| <span id="m-3fe299e10676"></span><code>OutputDeviceSettingsStore.SaveAsync(DbConnection,ISessionContext,OutputDeviceSettings,CancellationToken)</code><br>119–201 | HasPermission @125; Trim @128; Contains @129; nameof @130; ConfigureAwait @144; BeginTransactionAsync @144; CreateCommand @145; CreateParameter @153; ToString @155; Add @156; ToInt64 @157; ExecuteScalarAsync @157; ToString @189; CreateParameter @193; Add @196; ExecuteNonQueryAsync @198; CommitAsync @200 | FROM users @148; JOIN user_roles @148; UPDATE output_device_config @164 · UnauthorizedAccessException @126; ArgumentException @130; ArgumentException @132; ArgumentException @134; ArgumentException @136; ArgumentException @138; ArgumentException @140; ArgumentException @142; UnauthorizedAccessException @158 |

</details>

## OutputDeviceWorker.cs {#src-64d2e3097e9f}

<code>Software/src/GetSeek.Infrastructure/Hardware/OutputDeviceWorker.cs</code> · 651 lines.

SHA-256: <code>09dbbf92536f697c1fff7b5f358b4034352a985794d3b8c5d31c213c3029a84c</code>.

Declarations: <code>OutputDeviceWorker</code> (line 11), <code>ClaimedJob</code> (line 20).

<details markdown>
<summary>Methods, calls, table effects and failures (15)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-92be3a5e34c4"></span><code>OutputDeviceWorker.RunAsync(CancellationToken)</code><br>24–64 | ConfigureAwait @26; CreateWriteConnectionAsync @26; CreateCommand @28; ExecuteNonQueryAsync @42; ProcessOneAsync @49; ReportCycleErrorIfDistinct @60; Delay @62 | FROM hardware_jobs @29; UPDATE hardware_jobs @29; UPDATE pending_shelf_labels @29 |
| <span id="m-ebd9f037231a"></span><code>OutputDeviceWorker.ReportCycleErrorIfDistinct(Exception)</code><br>66–88 | GetType @73; Equals @74; cycleErrorLogger @82 | No extracted literal effects. |
| <span id="m-377e45aa6813"></span><code>OutputDeviceWorker.ProcessOneAsync(CancellationToken)</code><br>90–253 | ConfigureAwait @92; CreateWriteConnectionAsync @92; ProcessAsync @95; ReadAsync @97; CreateCommand @100; AddWithValue @109; ToString @109; ExecuteNonQueryAsync @110; ClaimAsync @113; IsNullOrWhiteSpace @118; SetResultAsync @120; Equals @129; TryReadGeometry @138; ComputeCapabilityFingerprint @141; InvalidateThermalVerificationAsync @147; ReadSnapshotValue @158; GetOrAdd @164; WaitAsync @165; BuildPaperReceiptAsync @170; Empty(byte) @172; BuildThermalReceiptAsync @176; Release @181; Render @188; Build @194; KickDrawer @194; Run @214; Send @214; WhenAny @215; Delay @215; FromSeconds @215; ReleaseQueueGateWhenSendCompletesAsync @226; ConfigureAwait @230; GetType @247 | FROM output_device_config @102; UPDATE hardware_jobs @102 |
| <span id="m-4ed5a445de57"></span><code>OutputDeviceWorker.ClaimAsync(SqliteConnection,bool,bool,CancellationToken)</code><br>255–286 | CreateCommand @257; AddWithValue @274; ToString @274; ConfigureAwait @277; ExecuteReaderAsync @277; ReadAsync @278; GetString @279; IsDBNull @280; GetInt32 @284 | FROM hardware_jobs @258; UPDATE hardware_jobs @258 |
| <span id="m-3773e39d6c2b"></span><code>OutputDeviceWorker.ReleaseQueueGateWhenSendCompletesAsync(Task,SemaphoreSlim)</code><br>288–293 | ConfigureAwait @290; Release @292 | No extracted literal effects. |
| <span id="m-de351ffc808e"></span><code>OutputDeviceWorker.SetResultAsync(SqliteConnection,string,string,string?,CancellationToken)</code><br>295–314 | ConfigureAwait @297; BeginTransactionAsync @297; CreateCommand @298; AddWithValue @301; ExecuteNonQueryAsync @304; AddWithValue @310; ExecuteNonQueryAsync @311; CommitAsync @313 | UPDATE hardware_jobs @300; UPDATE pending_shelf_labels @309 |
| <span id="m-847c6cc4fac8"></span><code>OutputDeviceWorker.BuildReceiptAsync(SqliteConnection,string,CancellationToken)</code><br>316–377 | Parse @318; GetString @319; GetProperty @319; CreateCommand @320; AddWithValue @327; ConfigureAwait @328; ExecuteReaderAsync @328; ReadAsync @329; GetString @331; GetInt64 @333; GetInt32 @339; DisposeAsync @341; ToString @344; Replace @345; Replace @345; WriteDivider @348; SetAlignment @348; WriteLine @348; SetBold @348; Initialize @348; Safe @348; AddWithValue @353; ExecuteReaderAsync @354; ReadAsync @356; WriteLine @358; GetString @358; WriteKeyValue @359; GetDouble @359; Amount @359; GetInt64 @359; WriteKeyValue @362; WriteDivider @362; AddWithValue @367; ExecuteReaderAsync @368; ReadAsync @370; GetInt32 @372; GetInt64 @373; Build @376; CutPaper @376 | FROM sales_invoices @321; FROM sales_lines @352; FROM sales_tenders @366; JOIN store_config @321 · InvalidDataException @330; InvalidDataException @340 |
| <span id="m-8bd59cf30513"></span><code>OutputDeviceWorker.BuildThermalReceiptAsync(SqliteConnection,string,OutputDeviceSettings,CancellationToken)</code><br>379–480 | Parse @381; GetString @382; GetProperty @382; TryGetProperty @383; GetString @384; ReadReceiptSnapshotValues @385; ContainsKey @385; ConfigureAwait @387; BuildAsync @387; Thermal @388; CreateCommand @401; AddWithValue @410; ExecuteReaderAsync @411; ReadAsync @412; GetString @413; GetInt64 @413; GetInt32 @415; TryGetValue @417; IsNullOrWhiteSpace @417; ReadSnapshotInt @418; FormatReceiptMoney @421; Snapshot @424; Amount @433; Min @435; Max @435; ReadSnapshotLong @437; AddWithValue @447; ExecuteScalarAsync @448; ToString @449; Deserialize(ReceiptDesignDocument) @451; AddRange @458; Split @458; Render @458; AddWithValue @462; ExecuteReaderAsync @463; Add @466; GetDouble @467; Render @479 | FROM receipt_design_versions @446; FROM sales_invoices @403; FROM sales_lines @461; JOIN store_config @403 · InvalidDataException @412; InvalidDataException @420; InvalidDataException @450; InvalidDataException @452 |
| <span id="m-5696f8c0696b"></span><code>OutputDeviceWorker.BuildPaperReceiptAsync(SqliteConnection,string,string,CancellationToken)</code><br>482–585 | IsWindows @484; Parse @485; GetString @486; GetProperty @486; TryGetProperty @487; GetString @488; ReadReceiptSnapshotValues @489; ContainsKey @489; ConfigureAwait @491; BuildAsync @491; TryReadGeometry @492; PrintShipping @492; Print @492; Empty(byte) @492; CreateCommand @501; AddWithValue @504; ExecuteReaderAsync @505; ReadAsync @506; Add @507; GetString @507; GetInt64 @508; GetInt32 @508; TryGetValue @510; IsNullOrWhiteSpace @510; ReadSnapshotInt @511; FormatReceiptMoney @513; Snapshot @516; Amount @525; Min @527; Max @527; ReadSnapshotLong @529; AddWithValue @538; ExecuteScalarAsync @539; ToString @540; Deserialize(ReceiptDesignDocument) @543; Clear @546; AddRange @547; Split @547; Render @547; AddRange @548; AddWithValue @555; ExecuteReaderAsync @556; Add @558; GetDouble @558; Add @561; AddWithValue @568; ExecuteReaderAsync @569; AddRange @579; Empty(string) @582; Print @583 | FROM receipt_design_versions @537; FROM sales_invoices @503; FROM sales_lines @554; FROM sales_tenders @567; JOIN store_config @503 · PlatformNotSupportedException @484; InvalidDataException @506 |
| <span id="m-526716c7c800"></span><code>OutputDeviceWorker.ReadSnapshotValue(string?,string)</code><br>587–598 | IsNullOrWhiteSpace @589; Parse @592; TryGetProperty @593; GetString @594 | No extracted literal effects. |
| <span id="m-8d4b6dca47e0"></span><code>OutputDeviceWorker.ReadReceiptSnapshotValues(JsonElement)</code><br>600–623 | TryGetProperty @603; IsNullOrWhiteSpace @604; GetString @604; Parse @607; EnumerateObject @608; GetString @612; GetRawText @613 | InvalidDataException @621 |
| <span id="m-92b28dc7292b"></span><code>OutputDeviceWorker.Snapshot(Dictionary&lt;string, string?&gt;,string,string)</code><br>625–626 | TryGetValue @626 | No extracted literal effects. |
| <span id="m-96607a0b6ae2"></span><code>OutputDeviceWorker.ReadSnapshotInt(Dictionary&lt;string, string?&gt;,string)</code><br>628–630 | TryGetValue @629; TryParse @629 | No extracted literal effects. |
| <span id="m-29e8d28b7ac0"></span><code>OutputDeviceWorker.ReadSnapshotLong(Dictionary&lt;string, string?&gt;,string)</code><br>632–634 | TryGetValue @633; TryParse @633 | No extracted literal effects. |
| <span id="m-62ba85ca800d"></span><code>OutputDeviceWorker.FormatReceiptMoney(long,string,int,int,bool)</code><br>636–648 | ScalingFactor @643; ToString @647 | InvalidDataException @639 |

</details>

## PaperReceiptLayoutEngine.cs {#src-034b6af6f231}

<code>Software/src/GetSeek.Infrastructure/Hardware/PaperReceiptLayoutEngine.cs</code> · 60 lines.

SHA-256: <code>036906ff21b79030c241b91e92450d577aa1ea532cb759490b391045c9502cc1</code>.

Declarations: <code>PaperReceiptRow</code> (line 3), <code>PaperReceiptPage</code> (line 4), <code>PaperReceiptLayoutEngine</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5657c4beddb4"></span><code>PaperReceiptLayoutEngine.Paginate(PrinterGeometry,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;PaperReceiptRow&gt;,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;string&gt;,int)</code><br>11–59 | nameof @21; Floor @22; Max @23; Add @39; Add @43; ToArray(string) @55; Select @55; ToArray @56; Append @56; Append(string) @57; Concat @57; Empty(string) @57 | ArgumentException @21; InvalidOperationException @26; InvalidOperationException @35; InvalidOperationException @51 |

</details>

## PaperReceiptSpooler.cs {#src-a3313efb1713}

<code>Software/src/GetSeek.Infrastructure/Hardware/PaperReceiptSpooler.cs</code> · 321 lines.

SHA-256: <code>6485af2f0e6f64f4f354d7ac9c192a790d2962be5c5106a17c2362c19c6d7a35</code>.

Declarations: <code>PaperReceiptSpooler</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-45b142ad5b69"></span><code>PaperReceiptSpooler.PrintShipping(string,PrinterGeometry,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;PaperReceiptRow&gt;,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;string&gt;,CancellationToken)</code><br>17–19 | PrintCore @19 | No extracted literal effects. |
| <span id="m-8e875e387680"></span><code>PaperReceiptSpooler.Print(string,PrinterGeometry,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;PaperReceiptRow&gt;,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;string&gt;,CancellationToken)</code><br>20–29 | PrintCore @29 | No extracted literal effects. |
| <span id="m-f8238973f606"></span><code>PaperReceiptSpooler.PrintCore(string,PrinterGeometry,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;PaperReceiptRow&gt;,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;string&gt;,bool,CancellationToken)</code><br>31–156 | IsWindows @34; ThrowIfCancellationRequested @35; MeasureRows @38; MeasureAndWrapLines @39; Paginate @42; Max @56; Round @56; Floor @58; Clear @62; Resolve @66; Max @79; DrawCell @93; Wrap @101; Draw @103; StartsWith @122; Flush @129; SetResolution @131; LockBits @132; GetPixel @140; Add @145; Copy @146; UnlockBits @149; DrawImage @150; Print @154 | PlatformNotSupportedException @34; InvalidOperationException @36; InvalidOperationException @44; InvalidOperationException @50; InvalidOperationException @155 |
| <span id="m-9acaa0cd12d8"></span><code>PaperReceiptSpooler.RenderPreviewPngPages(PrinterGeometry,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;PaperReceiptRow&gt;,IReadOnlyList&lt;string&gt;,IReadOnlyList&lt;string&gt;)</code><br>162–188 | nameof @171; MeasureRows @173; MeasureAndWrapLines @174; Paginate @177; RenderPreviewPage @182; FromBitmap @183; Encode @184; Add @185; ToArray @185 | ArgumentException @171 |
| <span id="m-13ff321970bb"></span><code>PaperReceiptSpooler.RenderPreviewPage(PrinterGeometry,PaperReceiptPage)</code><br>190–269 | Clear @199; Resolve @203; Max @216; DrawCell @231; Wrap @239; Draw @241; Max @255; StartsWith @260; Flush @267 | InvalidOperationException @194 |
| <span id="m-d014f8382433"></span><code>PaperReceiptSpooler.MeasureRows(PrinterGeometry,IReadOnlyList&lt;PaperReceiptRow&gt;)</code><br>271–284 | Resolve @274; Max @277; ToArray @278; Select @278; Wrap @280; Ceiling @281; Max @282 | No extracted literal effects. |
| <span id="m-5e5f65891d5c"></span><code>PaperReceiptSpooler.MeasureAndWrapLines(PrinterGeometry,IReadOnlyList&lt;string&gt;)</code><br>286–292 | Resolve @288; ToArray @291; SelectMany @291; Wrap @291 | No extracted literal effects. |
| <span id="m-8b15649a5ff3"></span><code>PaperReceiptSpooler.Wrap(string,float,SKShaper,SKPaint)</code><br>294–312 | IsNullOrEmpty @296; GetTextElementEnumerator @299; MoveNext @300; GetTextElement @302; Append @303; Measure @304; ToString @304; Add @307; Clear @308 | InvalidDataException @306 |
| <span id="m-3b7344ce6962"></span><code>PaperReceiptSpooler.DrawCell(SKCanvas,SKShaper,SKPaint,string,float,float,float,float,bool)</code><br>314–320 | Measure @317; Max @318; Draw @319 | No extracted literal effects. |

</details>

## ReceiptDocumentBuilder.cs {#src-7cb694daaa86}

<code>Software/src/GetSeek.Infrastructure/Hardware/ReceiptDocumentBuilder.cs</code> · 260 lines.

SHA-256: <code>111923c2084096d3d389b532464c8567076d0f199f46eae7f12fa1572608d1b6</code>.

Declarations: <code>ReceiptLineItem</code> (line 7), <code>ReceiptTenderItem</code> (line 15), <code>ReceiptDocumentData</code> (line 19), <code>ReceiptDocumentBuilder</code> (line 48).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b7e5a653c137"></span><code>ReceiptDocumentBuilder.CreateSampleData(string?,string,int,int)</code><br>50–87 | IsNullOrWhiteSpace @57 | No extracted literal effects. |
| <span id="m-36783bda81f9"></span><code>ReceiptDocumentBuilder.BuildTemplateContext(ReceiptDocumentData)</code><br>89–127 | ToDisplayAmount @94; ToString @95; Join @99; Select @99; ToString @109; FormatMoney @115; Min @120; Max @121 | No extracted literal effects. |
| <span id="m-092e5398ff35"></span><code>ReceiptDocumentBuilder.BuildThermalLines(ReceiptDocumentData,string,string)</code><br>129–190 | BuildTemplateContext @134; Render @136; ToDisplayAmount @142; ToString @143; Split @147; Add @149; TrimEnd @149; FormatMoney @155; IsNullOrWhiteSpace @156; Split @184; TrimEnd @186 | No extracted literal effects. |
| <span id="m-513d1596a7f6"></span><code>ReceiptDocumentBuilder.BuildPaperDocument(ReceiptDocumentData,string,string)</code><br>192–259 | BuildTemplateContext @197; Render @199; ToDisplayAmount @205; ToString @206; ToList @209; Select @209; Split @209; TrimEnd @209; IsNullOrWhiteSpace @215; Add @219; ToString @221; FormatMoney @223; Add @234; Split @256; TrimEnd @256 | No extracted literal effects. |

</details>

## ReceiptReprintService.cs {#src-95f4236bbb2f}

<code>Software/src/GetSeek.Infrastructure/Hardware/ReceiptReprintService.cs</code> · 86 lines.

SHA-256: <code>b8ff84c24c0a42324e02f07bee1655dcdbda67e77d016c617010ff765b9267a8</code>.

Declarations: <code>ReceiptReprintService</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-08f7ed409259"></span><code>ReceiptReprintService.QueueAsync(DbConnection,ISessionContext,string,CancellationToken)</code><br>9–63 | IsNullOrWhiteSpace @17; nameof @18; ConfigureAwait @20; BeginTransactionAsync @20; CreateCommand @21; CreateParameter @28; ToString @30; Add @31; ToInt64 @32; ExecuteScalarAsync @32; ToString @36; NewGuid @36; ToString @50; Trim @51; CreateParameter @54; Add @57; ExecuteNonQueryAsync @59; CommitAsync @61 | FROM sales_invoices @39; FROM users @24; INSERT INTO hardware_jobs @39; JOIN user_roles @24 · UnauthorizedAccessException @16; ArgumentException @18; UnauthorizedAccessException @33; InvalidOperationException @60 |
| <span id="m-4fce60652214"></span><code>ReceiptReprintService.QueueViaPipelineAsync(GetSeek.Application.Pipeline.CommandPipeline,IUnitOfWork,string,CancellationToken)</code><br>65–85 | ConfigureAwait(GetSeek.Application.Hardware.QueueReceiptReprintCommand, string) @75; ExecuteAsync(GetSeek.Application.Hardware.QueueReceiptReprintCommand, string) @75; IsNullOrWhiteSpace @80 | InvalidOperationException @82 |

</details>

## ReceiptTemplateEngine.cs {#src-0a5fe53cb222}

<code>Software/src/GetSeek.Infrastructure/Hardware/ReceiptTemplateEngine.cs</code> · 58 lines.

SHA-256: <code>283bb8eb1de432e562deff1b5dd65d66160458308502cb9c466c572eca5fcb00</code>.

Declarations: <code>ReceiptTemplateContext</code> (line 6), <code>ReceiptTemplateEngine</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-676a50f53c8a"></span><code>ReceiptTemplateEngine.Render(string,ReceiptTemplateContext)</code><br>20–47 | ThrowIfNull @22; Validate @23; Match @30; EnsureAllowed @33; TryGetValue @34; Insert @35; Remove @35; IsNullOrWhiteSpace @35; Matches @38; Replace @46 | InvalidDataException @44 |
| <span id="m-549e17234851"></span><code>ReceiptTemplateEngine.Validate(string)</code><br>49–52 | Validate @51 | No extracted literal effects. |
| <span id="m-ec1ef073e87b"></span><code>ReceiptTemplateEngine.EnsureAllowed(string)</code><br>54–57 | Contains @56 | InvalidDataException @56 |

</details>

## ScheduledOfferShelfLabelTransitionProcessor.cs {#src-1026d36880c1}

<code>Software/src/GetSeek.Infrastructure/Hardware/ScheduledOfferShelfLabelTransitionProcessor.cs</code> · 346 lines.

SHA-256: <code>f76fd4211449b3b38a010b213ec0fe52219227ef63f5fb21f67efe94dbc7d949</code>.

Declarations: <code>ScheduledOfferShelfLabelTransitionProcessor</code> (line 14), <code>Transition</code> (line 18), <code>Item</code> (line 19), <code>Offer</code> (line 20), <code>TierOverride</code> (line 23).

<details markdown>
<summary>Methods, calls, table effects and failures (19)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-010742e65901"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ProcessAsync(SqliteConnection,DateTimeOffset,CancellationToken)</code><br>25–136 | ThrowIfNull @28; ToString @29; ToUniversalTime @29; ConfigureAwait @30; BeginTransactionAsync @30; DiscoverDueTransitionsAsync @33; ReadNextTransitionAsync @34; CommitAsync @37; ReadOfferAsync @41; SkipTransitionAsync @44; ReadPendingItemsAsync @58; CompleteTransitionAsync @61; ReadActiveTiersAsync @66; ReadActiveOffersAsync @67; ToArray @68; Select @68; ReadTierOverridesAsync @70; ReadDecimalPlacesAsync @71; ToUniversalTime @72; Parse @72; AddTicks @73; HasPossiblyPrintedStartLabelAsync @79; DiscardUnprintedStartLabelAsync @81; MarkItemAsync @82; IsNullOrWhiteSpace @88; Equals @89; TryGetValue @92; BuildTierSpec @95; ResolveTierPrice @96; ResolvePromoPrice @97; EventKey @101; CreateCommand @102; Add @111; NewGuid @111; ToString @111; ToString @115; ExecuteNonQueryAsync @116; ToInt32 @127; ExecuteScalarAsync @127; SetTransitionProcessingAsync @131 | FROM price_offer_label_transition_items @125; FROM store_config @103; INSERT OR IGNORE INTO pending_shelf_labels @103 |
| <span id="m-ad4861d6d7d1"></span><code>ScheduledOfferShelfLabelTransitionProcessor.DiscoverDueTransitionsAsync(SqliteConnection,SqliteTransaction,string,CancellationToken)</code><br>138–155 | CreateCommand @140; Add @153; ConfigureAwait @154; ExecuteNonQueryAsync @154 | FROM price_offers @141; INSERT OR IGNORE INTO price_offer_label_transitions @141 |
| <span id="m-4bb00c833d97"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ReadNextTransitionAsync(SqliteConnection,SqliteTransaction,CancellationToken)</code><br>157–169 | CreateCommand @159; ConfigureAwait @165; ExecuteReaderAsync @165; ReadAsync @166; GetString @167; GetInt32 @167 | FROM price_offer_label_transitions @160 |
| <span id="m-780fa7fdcf45"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ReadOfferAsync(SqliteConnection,SqliteTransaction,string,CancellationToken)</code><br>171–190 | CreateCommand @173; Add @180; ConfigureAwait @181; ExecuteReaderAsync @181; ReadAsync @182; IsDBNull @183; TryParse @183; GetString @183; TryParse @184; ToUniversalTime @184; TryParse @185; Parse @186; DateAt @187; GuidAt @187; DecimalAt @187; GetInt64 @188; GetInt32 @188 | FROM price_offers @174 |
| <span id="m-0dc7880141d8"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ReadPendingItemsAsync(SqliteConnection,SqliteTransaction,string,CancellationToken)</code><br>192–213 | CreateCommand @195; Add @204; ConfigureAwait @205; ExecuteReaderAsync @205; ReadAsync @206; IsDBNull @208; TryParse @208; GetString @208; Add @209; Parse @209; GetInt64 @210 | FROM price_offer_label_transition_items @196; JOIN item_pricing @196; JOIN items @196 |
| <span id="m-75c6525f4f78"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ReadActiveTiersAsync(SqliteConnection,SqliteTransaction,CancellationToken)</code><br>215–231 | CreateCommand @218; ToInt32 @221; ConfigureAwait @221; ExecuteScalarAsync @221; Add @226; ExecuteReaderAsync @227; ReadAsync @228; Add @229; GetInt32 @229; GetString @229 | FROM price_level_settings @225; FROM store_config @220 |
| <span id="m-cb6284555f32"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ReadActiveOffersAsync(SqliteConnection,SqliteTransaction,CancellationToken)</code><br>233–250 | CreateCommand @236; ConfigureAwait @238; ExecuteReaderAsync @238; ReadAsync @239; IsDBNull @241; TryParse @241; GetString @241; TryParse @242; ToUniversalTime @242; TryParse @243; Add @244; Parse @244; DateAt @245; GuidAt @245; DecimalAt @245; GetInt64 @246; GetInt32 @246 | FROM price_offers @237 |
| <span id="m-6d30377e0423"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ReadTierOverridesAsync(SqliteConnection,SqliteTransaction,Guid[],List&lt;TierDefinition&gt;,CancellationToken)</code><br>252–267 | CreateCommand @257; Add @259; Add @259; ToString @259; Add @261; Join @262; ConfigureAwait @263; ExecuteReaderAsync @263; ReadAsync @264; Parse @265; GetString @265; IsDBNull @265; GetInt64 @265; GetInt32 @265 | DYNAMIC SQL: inspect manually |
| <span id="m-04bf81f4ee6a"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ReadDecimalPlacesAsync(SqliteConnection,SqliteTransaction,CancellationToken)</code><br>269–273 | CreateCommand @271; ToInt32 @272; ConfigureAwait @272; ExecuteScalarAsync @272 | FROM store_config @271 |
| <span id="m-ccd86d321f3f"></span><code>ScheduledOfferShelfLabelTransitionProcessor.BuildTierSpec(TierOverride)</code><br>275–280 | ParseWeightMode @277; ParseStoredPercentage @278 | No extracted literal effects. |
| <span id="m-ce7f0a3138e6"></span><code>ScheduledOfferShelfLabelTransitionProcessor.ResolvePromoPrice(Item,string,long,IReadOnlyList&lt;PriceOfferDto&gt;,DateTime)</code><br>282–287 | EvaluateLineOffer @284; Max @286 | No extracted literal effects. |
| <span id="m-c0e21e368ac5"></span><code>ScheduledOfferShelfLabelTransitionProcessor.HasPossiblyPrintedStartLabelAsync(SqliteConnection,SqliteTransaction,Transition,Guid,CancellationToken)</code><br>289–296 | CreateCommand @291; Add @293; ToString @293; ToInt32 @295; ConfigureAwait @295; ExecuteScalarAsync @295 | FROM pending_shelf_labels @292 |
| <span id="m-9d9890bbcd69"></span><code>ScheduledOfferShelfLabelTransitionProcessor.DiscardUnprintedStartLabelAsync(SqliteConnection,SqliteTransaction,Transition,Guid,CancellationToken)</code><br>298–305 | CreateCommand @300; Add @302; ToString @302; ConfigureAwait @304; ExecuteNonQueryAsync @304 | UPDATE pending_shelf_labels @301 |
| <span id="m-39c9354fe554"></span><code>ScheduledOfferShelfLabelTransitionProcessor.MarkItemAsync(SqliteConnection,SqliteTransaction,string,Guid,string,CancellationToken)</code><br>307–313 | CreateCommand @309; Add @311; ToString @311; ConfigureAwait @312; ExecuteNonQueryAsync @312 | UPDATE price_offer_label_transition_items @310 |
| <span id="m-10745402e5e3"></span><code>ScheduledOfferShelfLabelTransitionProcessor.SkipTransitionAsync(SqliteConnection,SqliteTransaction,string,string,bool,CancellationToken)</code><br>315–326 | CreateCommand @319; Add @321; ConfigureAwait @321; ExecuteNonQueryAsync @321; ExecuteNonQueryAsync @325 | FROM price_offer_label_transitions @320; UPDATE pending_shelf_labels @320; UPDATE price_offer_label_transition_items @324; UPDATE price_offer_label_transitions @324 |
| <span id="m-7f279a923f5f"></span><code>ScheduledOfferShelfLabelTransitionProcessor.CompleteTransitionAsync(SqliteConnection,SqliteTransaction,string,string,CancellationToken)</code><br>328–333 | CreateCommand @330; Add @332; ConfigureAwait @332; ExecuteNonQueryAsync @332 | UPDATE price_offer_label_transition_items @331; UPDATE price_offer_label_transitions @331 |
| <span id="m-933a1a97b1e0"></span><code>ScheduledOfferShelfLabelTransitionProcessor.SetTransitionProcessingAsync(SqliteConnection,SqliteTransaction,string,CancellationToken)</code><br>335–339 | CreateCommand @337; Add @338; ConfigureAwait @338; ExecuteNonQueryAsync @338 | UPDATE price_offer_label_transitions @337 |
| <span id="m-7d4306d018b1"></span><code>ScheduledOfferShelfLabelTransitionProcessor.EventKey(Guid,int,string,Guid,string)</code><br>341–342 | — | No extracted literal effects. |
| <span id="m-25b9bf909f18"></span><code>ScheduledOfferShelfLabelTransitionProcessor.Add(SqliteCommand,string,object?)</code><br>344–345 | AddWithValue @345 | No extracted literal effects. |

</details>

## SerialScaleDriver.cs {#src-a9e673c286e8}

<code>Software/src/GetSeek.Infrastructure/Hardware/SerialScaleDriver.cs</code> · 65 lines.

SHA-256: <code>194ba3a5199d77ca5c68c50a40be2d72edb138c54a81a2dc76e9a82b02360028</code>.

Declarations: <code>ScaleReadingStatus</code> (line 5), <code>ScaleReading</code> (line 14), <code>SerialScaleDriver</code> (line 21).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-840d2760b89d"></span><code>SerialScaleDriver.ParseNciFrame(string)</code><br>29–64 | IsNullOrWhiteSpace @31; Trim @36; Contains @38; Any @44; ToArray @48; Where @48; IsDigit @48; Where @49; IsNullOrEmpty @50; TryParse @53; ToLowerInvariant @61 | No extracted literal effects. |

</details>

## ShelfLabelRenderer.cs {#src-f06368a9e09f}

<code>Software/src/GetSeek.Infrastructure/Hardware/ShelfLabelRenderer.cs</code> · 102 lines.

SHA-256: <code>1aa809f0c9700852fad2e3a1f1f11aef7337e832313f71cca4ca2071d9b4d3c3</code>.

Declarations: <code>ShelfLabelRenderer</code> (line 9), <code>LabelSnapshot</code> (line 12), <code>LabelPayload</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-62fff773803f"></span><code>ShelfLabelRenderer.Render(string)</code><br>16–39 | Deserialize(LabelPayload) @18; Write @24; RenderLabel @27; GetPixel @32; RasterizeBitmap @35; ToArray @38 | InvalidDataException @21 |
| <span id="m-2989525928e4"></span><code>ShelfLabelRenderer.RenderLabel(LabelSnapshot,int,int)</code><br>41–76 | Clear @46; FromFamilyName @47; Take @51; Wrap @51; DrawShapedText @53; Clamp @57; RenderPng @59; Decode @60; Min @62; DrawBitmap @63; FormatMinor @69; IsNullOrWhiteSpace @69; Shape @72; Max @73; Flush @74 | No extracted literal effects. |
| <span id="m-ba39ba58290b"></span><code>ShelfLabelRenderer.Wrap(string,float,SKShaper,SKPaint)</code><br>78–93 | Trim @80; Replace @80; Replace @80; Split @84; Shape @87; Clear @87; Append @87; Add @88; ToString @88 | No extracted literal effects. |
| <span id="m-6594c69ed1fb"></span><code>ShelfLabelRenderer.FormatMinor(long,string,int)</code><br>95–101 | ToString @100 | InvalidDataException @97 |

</details>

## ThermalReceiptRenderer.cs {#src-c32dccbb23d1}

<code>Software/src/GetSeek.Infrastructure/Hardware/ThermalReceiptRenderer.cs</code> · 157 lines.

SHA-256: <code>66cc3b7effc618b78ffa5d63abf396dc1b0d61dfe8a32e546ff2c05284745eb4</code>.

Declarations: <code>ThermalReceiptDocument</code> (line 7), <code>ThermalReceiptRenderer</code> (line 18).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9cf614a6106f"></span><code>ThermalReceiptRenderer.Render(ThermalReceiptDocument)</code><br>20–81 | nameof @22; Resolve @27; Max @33; Replace @41; Replace @41; AddRange @42; WrapByShapedGrapheme @42; Add @44; Ceiling @45; Max @50; Min @53; Clear @57; Draw @61; Flush @64; GetPixel @70; RasterizeBitmap @73; Write @74; WriteByte @78; ToArray @80 | InvalidDataException @47 |
| <span id="m-e9a4952184e5"></span><code>ThermalReceiptRenderer.RenderPreviewPng(ThermalReceiptDocument)</code><br>88–134 | Render @91; Add @111; Erase @117; SetPixel @126; FromBitmap @131; Encode @132; ToArray @133 | InvalidDataException @100; InvalidDataException @107; InvalidDataException @110; InvalidDataException @115 |
| <span id="m-ce8131a56095"></span><code>ThermalReceiptRenderer.WrapByShapedGrapheme(string,float,SKShaper,SKPaint)</code><br>136–156 | IsNullOrEmpty @138; GetTextElementEnumerator @141; MoveNext @142; GetTextElement @144; Append @145; Measure @146; ToString @146; Add @150; Clear @151 | InvalidDataException @149 |

</details>

## UnicodeTypefaceResolver.cs {#src-94e096b5ea67}

<code>Software/src/GetSeek.Infrastructure/Hardware/UnicodeTypefaceResolver.cs</code> · 53 lines.

SHA-256: <code>8fdb94b215fac27cab7af78325e387cb8d6f6e2fb7b0060237000a62c6d40237</code>.

Declarations: <code>UnicodeTypefaceResolver</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9ccbf6318f04"></span><code>UnicodeTypefaceResolver.Load(string)</code><br>13–14 | FromFile @13; Combine @13 | No extracted literal effects. |
| <span id="m-873e37a8e39f"></span><code>UnicodeTypefaceResolver.Resolve(string?)</code><br>15–15 | Contains @15 | No extracted literal effects. |
| <span id="m-8f2711ea9144"></span><code>UnicodeTypefaceResolver.ResolveText(string)</code><br>16–16 | Any @16 | No extracted literal effects. |
| <span id="m-53384b4ebae2"></span><code>UnicodeTypefaceResolver.Measure(string,SKPaint)</code><br>17–27 | Runs @20; Clone @22; Shape @24 | No extracted literal effects. |
| <span id="m-821578e4f1fb"></span><code>UnicodeTypefaceResolver.Draw(SKCanvas,string,float,float,SKPaint)</code><br>28–37 | Runs @30; Clone @32; DrawShapedText @34; Shape @35 | No extracted literal effects. |
| <span id="m-5a4591942ab8"></span><code>UnicodeTypefaceResolver.Runs(string)</code><br>39–52 | GetTextElementEnumerator @41; ResolveText @42; MoveNext @43; GetTextElement @45; Any @46; ToString @48; Clear @48; Append @49 | No extracted literal effects. |

</details>

## WindowsPrinterQueueReader.cs {#src-de6ffd7eacce}

<code>Software/src/GetSeek.Infrastructure/Hardware/WindowsPrinterQueueReader.cs</code> · 127 lines.

SHA-256: <code>10fc2277f3d550bbf5798583404d87995889683ba26b641dbf26d64163f31438</code>.

Declarations: <code>PrinterQueueInfo</code> (line 7), <code>PrinterGeometry</code> (line 9), <code>WindowsPrinterQueueReader</code> (line 22), <code>NativePrinterInfo2</code> (line 34).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3f168fde161c"></span><code>WindowsPrinterQueueReader.EnumPrinters(uint,string?,uint,IntPtr,uint,uint,uint)</code><br>60–61 | — | No extracted literal effects. |
| <span id="m-f17259381596"></span><code>WindowsPrinterQueueReader.CreateDC(string,string,string?,IntPtr)</code><br>63–64 | — | No extracted literal effects. |
| <span id="m-90029ea97c9c"></span><code>WindowsPrinterQueueReader.GetDeviceCaps(IntPtr,int)</code><br>66–67 | — | No extracted literal effects. |
| <span id="m-abc258b35952"></span><code>WindowsPrinterQueueReader.DeleteDC(IntPtr)</code><br>69–70 | — | No extracted literal effects. |
| <span id="m-ea15f067813d"></span><code>WindowsPrinterQueueReader.Enumerate()</code><br>72–95 | IsWindows @74; Empty(PrinterQueueInfo) @74; EnumPrinters @75; AllocHGlobal @77; SizeOf(NativePrinterInfo2) @82; PtrToStructure(NativePrinterInfo2) @86; Add @86; Add @87; PtrToStringUni @88; ToArray @92; Where @92; IsNullOrWhiteSpace @92; FreeHGlobal @94 | No extracted literal effects. |
| <span id="m-36ac35a1d7ea"></span><code>WindowsPrinterQueueReader.TryReadGeometry(string)</code><br>97–118 | IsWindows @99; IsNullOrWhiteSpace @99; CreateDC @100; GetDeviceCaps @104; DeleteDC @117 | No extracted literal effects. |
| <span id="m-d5d02441cc32"></span><code>WindowsPrinterQueueReader.ComputeCapabilityFingerprint(string,PrinterGeometry,int?)</code><br>120–126 | Join @122; Trim @122; ToString @124; ToHexStringLower @125; HashData @125; GetBytes @125 | No extracted literal effects. |

</details>

## WindowsRawPrinter.cs {#src-e4a1dd5d4384}

<code>Software/src/GetSeek.Infrastructure/Hardware/WindowsRawPrinter.cs</code> · 71 lines.

SHA-256: <code>ce1872bbcb4096b887fb420321f06c69a35c5a75cb9852b7ee44cdc01c904e4d</code>.

Declarations: <code>WindowsRawPrinter</code> (line 7), <code>DocInfo</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (8)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-e881494bf7f9"></span><code>WindowsRawPrinter.OpenPrinter(string,IntPtr,IntPtr)</code><br>17–18 | — | No extracted literal effects. |
| <span id="m-b02a46b29020"></span><code>WindowsRawPrinter.ClosePrinter(IntPtr)</code><br>20–21 | — | No extracted literal effects. |
| <span id="m-b217034538f4"></span><code>WindowsRawPrinter.StartDocPrinter(IntPtr,int,DocInfo)</code><br>23–24 | — | No extracted literal effects. |
| <span id="m-5e5fa9f3d21c"></span><code>WindowsRawPrinter.EndDocPrinter(IntPtr)</code><br>26–27 | — | No extracted literal effects. |
| <span id="m-ba72b1fe6d89"></span><code>WindowsRawPrinter.StartPagePrinter(IntPtr)</code><br>29–30 | — | No extracted literal effects. |
| <span id="m-f48cbfbc802b"></span><code>WindowsRawPrinter.EndPagePrinter(IntPtr)</code><br>32–33 | — | No extracted literal effects. |
| <span id="m-f3d930a3395f"></span><code>WindowsRawPrinter.WritePrinter(IntPtr,IntPtr,int,int)</code><br>35–36 | — | No extracted literal effects. |
| <span id="m-fa57e5d24a07"></span><code>WindowsRawPrinter.Send(string,byte[],string)</code><br>38–70 | IsWindows @40; OpenPrinter @42; GetLastWin32Error @43; StartDocPrinter @48; StartPagePrinter @52; AllocCoTaskMem @56; Copy @59; WritePrinter @60; FreeCoTaskMem @63; EndPagePrinter @65; EndDocPrinter @67; ClosePrinter @69 | PlatformNotSupportedException @41; Win32Exception @43; Win32Exception @49; Win32Exception @53; Win32Exception @61 |

</details>

## ImportPreviewService.cs {#src-9b8064464865}

<code>Software/src/GetSeek.Infrastructure/Imports/ImportPreviewService.cs</code> · 252 lines.

SHA-256: <code>1a49fec61223fe2986b5aca8f7fded963ee63cae842648fd57bb546df9214d5e</code>.

Declarations: <code>ImportPreviewService</code> (line 23).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-52a08701a406"></span><code>ImportPreviewService.ValidateInventoryAsync(ProductImportPreview,string,Guid,CancellationToken)</code><br>27–79 | ConfigureAwait @33; CreateWriteConnectionAsync @33; BeginTransactionAsync @37; Concat @43; Select @43; Select @43; SelectMany @43; Select @45; FingerprintAsync @47; Any @49; GetValueOrDefault @49; Distinct @51; FirstOrDefault @55; Equals @55; GetValueOrDefault @57; RecordAsync @59; GetValueOrDefault @61; NewGuid @67; HandleAsync @69; ToArray @73; Append @73; RollbackAsync @77 | FROM item_pricing @59; JOIN items @59 |
| <span id="m-df143dd30442"></span><code>ImportPreviewService.ReadThirdPartiesAsync(byte[],string,string,string,string,CancellationToken)</code><br>83–93 | ConfigureAwait @87; CreateReadConnectionAsync @87; BeginTransaction @89; ReadAsync @91 | No extracted literal effects. |
| <span id="m-0bd27fa31efc"></span><code>ImportPreviewService.ValidateThirdPartiesAsync(ThirdPartyImportPreview,string,Guid,CancellationToken)</code><br>97–125 | ConfigureAwait @103; CreateWriteConnectionAsync @103; BeginTransactionAsync @107; NewGuid @115; HandleAsync @117; ToArray @119; Append @119; RollbackAsync @123 | No extracted literal effects. |
| <span id="m-a77c9c317aee"></span><code>ImportPreviewService.TemplateContextAsync(string,string,CancellationToken)</code><br>129–137 | ConfigureAwait @133; CreateReadConnectionAsync @133; TemplateContextAsync @135 | No extracted literal effects. |
| <span id="m-afdac18e364a"></span><code>ImportPreviewService.TemplateContextAsync(DbConnection,string,CancellationToken)</code><br>141–249 | ConfigureAwait @145; ContextAsync @145; CreateCommand @153; ExecuteReaderAsync @155; ReadAsync @157; Add @157; ToString @157; GetValue @157; GetString @157; Load @161; AddRange @173; Select @243 | FROM price_level_settings @161; FROM product_categories @163; FROM store_config @161; FROM third_parties @171; FROM uoms @169 |

</details>

## XlsxImportWorkbook.cs {#src-16a4d298fe01}

<code>Software/src/GetSeek.Infrastructure/Imports/XlsxImportWorkbook.cs</code> · 265 lines.

SHA-256: <code>6427c9b69bb7fc4443905e262d16f766d91100f6a1b6b47c4aa7c45d1a11c3c8</code>.

Declarations: <code>XlsxImportRow</code> (line 9), <code>XlsxImportWorkbook</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-41b1672060cd"></span><code>XlsxImportWorkbook.HasSheet(string)</code><br>18–18 | ContainsKey @18 | No extracted literal effects. |
| <span id="m-1916b1d1b560"></span><code>XlsxImportWorkbook.Load(byte[],string,ImportWorkbookContext?)</code><br>20–91 | Sum @25; GetEntry @28; Open @29; Create @30; Load @31; ToArray @33; Select @33; Descendants @33; ReadXml @33; Concat @34; Descendants @34; ToDictionary @35; Elements @35; Attribute @35; Attribute @39; StartsWith @41; TrimStart @41; Contains @42; Attribute @46; Elements @48; Attribute @50; TakeWhile @52; ToUpperInvariant @52; ToUpperInvariant @54; Descendants @55; Element @55; Parse @56; Any @57; Sheets @57; Equals @57; TryAdd @59; TryAdd @61; TryAdd @63; ContainsKey @65; Rows @66; Cell @66; GetValueOrDefault @67; ToString @70; HasSheet @75; ToHashSet @76; Select @76; TryGetValue @78; Any @79; Any @79; Equals @79; GetValueOrDefault @79; Any @83; Contains @83; Where @84; Contains @84; TryGetValue @85; IsNullOrEmpty @85; ToString @85; GetValueOrDefault @85; ToUpperInvariant @85 | InvalidDataException @22; InvalidDataException @25; InvalidDataException @42; InvalidDataException @58; InvalidDataException @59; InvalidDataException @61; InvalidDataException @63; InvalidDataException @65; InvalidDataException @69; InvalidDataException @71; InvalidDataException @80; InvalidDataException @83; InvalidDataException @86; InvalidDataException @87 |
| <span id="m-3723384b16ab"></span><code>XlsxImportWorkbook.AssignAutomaticIdentifiers(string,string)</code><br>93–126 | ToHexString @95; HashData @95; GetBytes @95; TryGetValue @97; Single @98; Equals @98; Column @99; Where @101; Any @101; IsNullOrWhiteSpace @101; GetValueOrDefault @103; Equals @105; ToUpperInvariant @110; Where @114; Any @114; Sheets @114; ToArray @116; Select @116; Where @116; Where @117; Trim @120; StartsWith @121; TryGetValue @122 | InvalidDataException @122 |
| <span id="m-8d60bbc269f0"></span><code>XlsxImportWorkbook.CompletedWorkbook(byte[],string,string,ImportWorkbookContext)</code><br>128–139 | Load @130; AssignAutomaticIdentifiers @131; ToDictionary @132; Sheets @132; ToArray @133; Select @133; Rows @133; Empty(IDictionary&lt;string, object&gt;, string, object) @137; Write @138 | No extracted literal effects. |
| <span id="m-eacbc905a98c"></span><code>XlsxImportWorkbook.FailedWorkbook(byte[]?,string,IReadOnlyList&lt;ImportIssue&gt;,string)</code><br>143–180 | Load @150; ToHashSet @151; Append @151; Select @151; Sheets @151; ToDictionary @152; Where @152; Contains @152; Select @161; Add @162; Take @167; ToArray @170; Where @170; Any @170; Join @171; Select @171; TryGetValue @171; TryGetValue @171; Where @172; GetValueOrDefault @172; ToString @173; WriteSheets @176; FailedWorkbook @178 | InvalidDataException @149 |
| <span id="m-38fbea4c3f3a"></span><code>XlsxImportWorkbook.Rows(string,int)</code><br>182–195 | TryGetValue @184; TryGetValue @185; ToDictionary @186; Trim @186; Any @187; Count @187; Distinct @187; Where @189; All @191; Any @192; ContainsKey @192; IsNullOrWhiteSpace @192; ToDictionary @193; GetValueOrDefault @193 | InvalidDataException @185; InvalidDataException @188; InvalidDataException @192 |
| <span id="m-70c90a9aab1f"></span><code>XlsxImportWorkbook.Cell(IDictionary&lt;string, object&gt;,string)</code><br>197–198 | TryGetValue @197; ToString @198; Trim @198 | No extracted literal effects. |
| <span id="m-1653613c233e"></span><code>XlsxImportWorkbook.Write(string,ImportWorkbookContext,IReadOnlyDictionary&lt;string, IReadOnlyList&lt;IDictionary&lt;string, object&gt;&gt;&gt;?)</code><br>200–216 | ToString @204; Sheets @205; ToList @207; Select @207; TryGetValue @208; AddRange @209; Select @209; Cell @209; AddRange @213; Select @213; WriteSheets @215; ToDictionary @215; ToDictionary @215; Select @215; Select @215 | No extracted literal effects. |
| <span id="m-f91b4b784ee9"></span><code>XlsxImportWorkbook.WriteSheets(Dictionary&lt;string, SortedDictionary&lt;int, Dictionary&lt;int, string&gt;&gt;&gt;)</code><br>218–263 | Open @223; CreateEntry @223; Write @223; Add @225; Get @227; Add @231; Override @232; Add @237; Element @237; Add @238; Add @243; Add @251; ToString @254; ToString @260; ToString @260; ToString @260; ToArray @262 | No extracted literal effects. |

</details>

## XlsxMasterDataExportService.cs {#src-d02afc67a786}

<code>Software/src/GetSeek.Infrastructure/Imports/XlsxMasterDataExportService.cs</code> · 100 lines.

SHA-256: <code>086d3993a612b9c7caafbf23fa75a7c56eb733c6f10a35371eef0565fa508aff</code>.

Declarations: <code>XlsxMasterDataExportService</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4a1e2763d1e1"></span><code>XlsxMasterDataExportService.ExportAsync(string,string,Guid,CancellationToken)</code><br>12–99 | nameof @14; ConfigureAwait @16; OpenAsync @16; BeginTransaction @17; HasPermissionAsync @20; ContextAsync @22; CreateCommand @26; ExecuteReaderAsync @27; ReadAsync @29; GetName @32; IsDBNull @32; ToString @32; GetValue @32; Add @33; TryGetValue @39; TryParse @39; ToString @39; ToString @40; ToDisplayAmount @40; TryParse @44; Query @49; Money @74; Percent @74; CommitAsync @97; Write @98 | FROM item_kits @61; FROM item_price_levels @86; FROM item_pricing @76; FROM items @61; FROM third_parties @49; JOIN barcodes @61; JOIN item_pricing @61; JOIN items @76; JOIN items @86; JOIN product_categories @49; JOIN product_categories @61 · ArgumentException @14; UnauthorizedAccessException @21 |

</details>

## XlsxProductImportReader.cs {#src-2b8eea2eb4f9}

<code>Software/src/GetSeek.Infrastructure/Imports/XlsxProductImportReader.cs</code> · 158 lines.

SHA-256: <code>42f5fbfa6d8fdf26db831be770c4bf1797fe79567dd7249b3cda34dbb2151da7</code>.

Declarations: <code>XlsxProductImportReader</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0ee4ad5fd8ae"></span><code>XlsxProductImportReader.ExportTemplate(ImportWorkbookContext)</code><br>12–12 | Write @12 | No extracted literal effects. |
| <span id="m-49114112edf1"></span><code>XlsxProductImportReader.Read(byte[],string,string,ImportWorkbookContext?)</code><br>14–157 | IsNullOrWhiteSpace @26; TryParse @27; Add @28; Number @33; Money @35; TryParseBool @40; Load @46; AssignAutomaticIdentifiers @47; Rows @48; Cell @50; ToLowerInvariant @51; Trim @51; C @51; Flag @56; Money @57; ToLowerInvariant @59; ToLowerInvariant @68; ToDictionary @79; Fields @83; Optional @85; Add @86; Add @89; Add @96; Add @103; StartsWith @110; TryParse @112; Add @127; TryParse @137; Add @141; Where @145; GroupBy @145; Count @145; Last @145; GroupBy @146; Where @146; GetValueOrDefault @146; GroupBy @148; GroupBy @149; ToUpperInvariant @149; Where @150; StartsWith @154; Split @154 | No extracted literal effects. |

</details>

## XlsxThirdPartyImportReader.cs {#src-d4334f0c2e06}

<code>Software/src/GetSeek.Infrastructure/Imports/XlsxThirdPartyImportReader.cs</code> · 465 lines.

SHA-256: <code>10858523fa60b3a6045c3ea61bec3cfe32de17d220585a46cf8723886d8557c2</code>.

Declarations: <code>XlsxThirdPartyImportReader</code> (line 17).

<details markdown>
<summary>Methods, calls, table effects and failures (11)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b57c34eddaa7"></span><code>XlsxThirdPartyImportReader.ReadAsync(byte[],string,string,string,DbConnection,DbTransaction?,CancellationToken)</code><br>28–345 | Add @43; Load @51; ConfigureAwait @51; ContextAsync @51; AssignAutomaticIdentifiers @52; HasSheet @53; StartsWith @57; Split @57; LoadCategoriesAsync @62; LoadActivePriceTiersAsync @63; LoadExistingPartyCodesAsync @64; LoadExistingExternalMappingsAsync @65; LoadExistingBarcodesAsync @66; Rows @78; Fields @82; ToDictionary @82; Cell @82; MergeAsync @83; NullIfEmpty @84; Any @87; Contains @87; IsNullOrWhiteSpace @92; ResolveTier @92; ToHashSet @92; Select @92; Parse @92; Add @96; TryParseBool @99; StartsWith @108; ToString @112; ToUpperInvariant @125; ParseBool @158; TryGetValue @165; TryGetValue @170; TryNormalizePhone @181; IsValidStateCode @190; Contains @196; ContainsKey @208; Contains @214; Add @220; Add @226; Add @232; TryGetValue @238; Equals @239; NormalizeStateCode @301; FindPossibleDuplicatesAsync @307; Join @309; Add @323; FingerprintAsync @343; Select @343 | InvalidDataException @53 |
| <span id="m-80e12431ae7e"></span><code>XlsxThirdPartyImportReader.ExportTemplate(ImportWorkbookContext?)</code><br>347–348 | Write @348 | No extracted literal effects. |
| <span id="m-944fd0bf08ef"></span><code>XlsxThirdPartyImportReader.LoadCategoriesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>350–364 | CreateCommand @353; ConfigureAwait @356; ExecuteReaderAsync @356; ReadAsync @357; GetString @359 | FROM product_categories @355 |
| <span id="m-e258a0a87d6a"></span><code>XlsxThirdPartyImportReader.LoadActivePriceTiersAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>366–378 | CreateCommand @369; ConfigureAwait @372; ExecuteReaderAsync @372; ReadAsync @373; Add @375; GetString @375 | FROM price_level_settings @371; FROM store_config @371 |
| <span id="m-8bd162fc036b"></span><code>XlsxThirdPartyImportReader.LoadExistingPartyCodesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>380–394 | CreateCommand @383; ConfigureAwait @386; ExecuteReaderAsync @386; ReadAsync @387; GetString @389 | FROM third_parties @385 |
| <span id="m-47d287ba0b24"></span><code>XlsxThirdPartyImportReader.LoadExistingExternalMappingsAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>396–411 | CreateCommand @399; ConfigureAwait @402; ExecuteReaderAsync @402; ReadAsync @403; ToUpperInvariant @405; GetString @405 | FROM third_party_external_mappings @401 |
| <span id="m-0a31d63641ef"></span><code>XlsxThirdPartyImportReader.LoadExistingBarcodesAsync(DbConnection,DbTransaction?,CancellationToken)</code><br>413–427 | CreateCommand @416; ConfigureAwait @419; ExecuteReaderAsync @419; ReadAsync @420; GetString @422 | FROM third_parties @418 |
| <span id="m-aa0678d925e8"></span><code>XlsxThirdPartyImportReader.Cell(IDictionary&lt;string, object&gt;,string)</code><br>429–434 | TryGetValue @431; ToString @432; Trim @432 | No extracted literal effects. |
| <span id="m-44c62813fb52"></span><code>XlsxThirdPartyImportReader.FindPossibleDuplicatesAsync(ImportThirdPartyRow,string?,DbConnection,DbTransaction?,CancellationToken)</code><br>436–458 | ToHashSet @439; Where @439; Select @439; SelectMany @439; Where @439; IsNullOrWhiteSpace @440; Split @440; ToArray @441; Where @441; Phones @443; CreateCommand @446; CreateParameter @449; Trim @449; Add @449; ConfigureAwait @450; ExecuteReaderAsync @450; ReadAsync @451; Equals @453; GetString @453; Range @454; IsDBNull @454; Overlaps @455; Add @455 | FROM third_parties @448 |
| <span id="m-ba6a09e3e06d"></span><code>XlsxThirdPartyImportReader.NullIfEmpty(string)</code><br>460–461 | IsNullOrWhiteSpace @461; Trim @461 | No extracted literal effects. |
| <span id="m-18e7b217de20"></span><code>XlsxThirdPartyImportReader.ParseBool(string,bool)</code><br>463–464 | TryParseBool @464 | No extracted literal effects. |

</details>

## Ed25519LicenseValidator.cs {#src-ce4ed4a3dae2}

<code>Software/src/GetSeek.Infrastructure/Licensing/Ed25519LicenseValidator.cs</code> · 84 lines.

SHA-256: <code>c8274b5ecfc80b16d2dfbdc0306d93b01cf49fa3d2f89997cdfdb72074f57926</code>.

Declarations: <code>Ed25519LicenseValidator : ILicenseService</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-70d36ebbda73"></span><code>Ed25519LicenseValidator.IsModuleLicensed(string)</code><br>14–20 | IsModuleActive @19 | No extracted literal effects. |
| <span id="m-17b69fd1330c"></span><code>Ed25519LicenseValidator.VerifyDeviceBinding()</code><br>22–29 | ComputeLocalDeviceBinding @27; Equals @28 | No extracted literal effects. |
| <span id="m-d193d653bf4c"></span><code>Ed25519LicenseValidator.VerifyAndLoadClaims(string,string)</code><br>31–46 | GetBytes @33; FromHexString @34; Verify @37; Deserialize(LicenseClaims) @40 | No extracted literal effects. |
| <span id="m-e9ff388c06e2"></span><code>Ed25519LicenseValidator.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>48–76 | CreateCommand @51; ConfigureAwait @61; ExecuteScalarAsync @61; ToString @64; IsNullOrEmpty @65; TryParse @65; AddMinutes @68 | FROM immutable_audit_journal @53; FROM sales_invoices @53 |
| <span id="m-49fb18ed38c9"></span><code>Ed25519LicenseValidator.ComputeLocalDeviceBinding()</code><br>78–83 | ToHexStringLower @82; HashData @82; GetBytes @82 | No extracted literal effects. |

</details>

## ProductionLicenseService.cs {#src-06a0ffcacd9c}

<code>Software/src/GetSeek.Infrastructure/Licensing/ProductionLicenseService.cs</code> · 59 lines.

SHA-256: <code>cf8f252518384dd5abd63e32ef4d22cf644f2570db1778f2c790e5e6ddb0eb73</code>.

Declarations: <code>ProductionLicenseService : ILicenseService</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ec7609625521"></span><code>ProductionLicenseService.IsModuleLicensed(string)</code><br>13–17 | — | No extracted literal effects. |
| <span id="m-1d4b85f050e8"></span><code>ProductionLicenseService.VerifyDeviceBinding()</code><br>19–22 | — | No extracted literal effects. |
| <span id="m-2aba0af27c45"></span><code>ProductionLicenseService.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>24–52 | CreateCommand @27; ConfigureAwait @37; ExecuteScalarAsync @37; ToString @40; IsNullOrEmpty @41; TryParse @41; AddMinutes @44 | FROM immutable_audit_journal @29; FROM sales_invoices @29 |
| <span id="m-1ff105ebbcba"></span><code>ProductionLicenseService.ComputeLocalDeviceBinding()</code><br>54–58 | ToHexStringLower @57; HashData @57; GetBytes @57 | No extracted literal effects. |

</details>

## SqliteExpenseAttachmentService.cs {#src-87a2fd6ad020}

<code>Software/src/GetSeek.Infrastructure/Persistence/Attachments/SqliteExpenseAttachmentService.cs</code> · 405 lines.

SHA-256: <code>e3594c7a2960763372c80fbb196c2a89b7b726f674d704915e4dd30c46bd9cff</code>.

Declarations: <code>SqliteExpenseAttachmentService : IExpenseAttachmentService</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (8)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-8cc99e1a0253"></span><code>SqliteExpenseAttachmentService.GetConnectionAsync(string,CancellationToken)</code><br>38–76 | ConfigureAwait @55; OpenAsync @55; HasPermissionAsync @61; DisposeAsync @72 | UnauthorizedAccessException @42; UnauthorizedAccessException @64; rethrow @74 |
| <span id="m-3987b34e2ea4"></span><code>SqliteExpenseAttachmentService.PrepareAttachmentAsync(Stream,string,string?,CancellationToken)</code><br>78–250 | FromResult @86; Failure(PreparedAttachment) @86; Read @96; ThrowIfCancellationRequested @98; Write @104; ToArray @112; HasPrefix @115; Create @124; Decode @144; Max @151; Round @158; Resize @161; FromBitmap @177; Encode @187; ToArray @193; ToArray @201; ToArray @212; ToLowerInvariant @222; ToHexString @222; HashData @222; Success(PreparedAttachment) @232; Dispose @238 | EXPENSE_PHOTO_INVALID @86; EXPENSE_PHOTO_TOO_LARGE @102; EXPENSE_PHOTO_INVALID @109; EXPENSE_PHOTO_INVALID @120; EXPENSE_PHOTO_INVALID @127; EXPENSE_PHOTO_INVALID @135; EXPENSE_PHOTO_TOO_LARGE @140; EXPENSE_PHOTO_INVALID @147; EXPENSE_PHOTO_INVALID @164; EXPENSE_PHOTO_INVALID @180; EXPENSE_PHOTO_INVALID @190; EXPENSE_PHOTO_TOO_LARGE @219; EXPENSE_PHOTO_INVALID @248 · rethrow @244 |
| <span id="m-d354ca59e26e"></span><code>SqliteExpenseAttachmentService.GetCurrentAttachmentAsync(Guid,CancellationToken)</code><br>252–285 | ConfigureAwait @256; GetConnectionAsync @256; CreateCommand @259; AddParam @268; ToString @268; ExecuteReaderAsync @270; ReadAsync @271; ReadAttachmentDetail @276; DisposeAsync @282 | FROM expense_attachments @260; JOIN expense_records @260 |
| <span id="m-ac71b791ec94"></span><code>SqliteExpenseAttachmentService.GetAttachmentByIdAsync(Guid,CancellationToken)</code><br>287–320 | ConfigureAwait @291; GetConnectionAsync @291; CreateCommand @294; AddParam @303; ToString @303; ExecuteReaderAsync @305; ReadAsync @306; ReadAttachmentDetail @311; DisposeAsync @317 | FROM expense_attachments @295; JOIN expense_records @295 |
| <span id="m-ec7206c46a3a"></span><code>SqliteExpenseAttachmentService.GetAttachmentHistoryAsync(Guid,CancellationToken)</code><br>322–357 | ConfigureAwait @326; GetConnectionAsync @326; CreateCommand @329; AddParam @339; ToString @339; ExecuteReaderAsync @342; ReadAsync @343; Add @345; ReadAttachmentDetail @345; DisposeAsync @354 | FROM expense_attachments @330; JOIN expense_records @330 |
| <span id="m-2a01b1a1c80f"></span><code>SqliteExpenseAttachmentService.ReadAttachmentDetail(DbDataReader)</code><br>359–386 | Parse @361; GetString @361; GetInt32 @363; Parse @371 | No extracted literal effects. |
| <span id="m-32185352f0da"></span><code>SqliteExpenseAttachmentService.HasPrefix(byte[],byte[])</code><br>388–396 | — | No extracted literal effects. |
| <span id="m-d9d9597f0b1b"></span><code>SqliteExpenseAttachmentService.AddParam(DbCommand,string,object?)</code><br>398–404 | CreateParameter @400; Add @403 | No extracted literal effects. |

</details>

## DatabaseMigrator.cs {#src-03c231a85247}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/DatabaseMigrator.cs</code> · 191 lines.

SHA-256: <code>8fd8e901f985c97a5fd0d1d71312e22e6359b744e144cc4818f2e8e09882600e</code>.

Declarations: <code>DatabaseMigrator</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5e7d439b37d5"></span><code>DatabaseMigrator.MigrateAsync(SqliteConnection,CancellationToken)</code><br>99–100 | MigrateToVersionAsync @100 | No extracted literal effects. |
| <span id="m-e9ed3dc69611"></span><code>DatabaseMigrator.MigrateToVersionAsync(SqliteConnection,int,CancellationToken)</code><br>103–172 | nameof @106; CreateCommand @108; ConfigureAwait @117; ExecuteNonQueryAsync @117; ExecuteScalarAsync @125; ToInt64 @128; LoadMigrationScriptAsync @138; BeginTransactionAsync @140; AddWithValue @157; ToString @158; CommitAsync @163; RollbackAsync @167 | CREATE TABLE IF NOT EXISTS  schema_version @110; FROM schema_version @124; INSERT INTO schema_version @153 · ArgumentOutOfRangeException @106; rethrow @168 |
| <span id="m-b5d711cc1dbc"></span><code>DatabaseMigrator.LoadMigrationScriptAsync(string,CancellationToken)</code><br>174–190 | Combine @176; Exists @178; ConfigureAwait @180; ReadAllTextAsync @180; GetFullPath @183 | FileNotFoundException @189 |

</details>

## CommercialInvoiceSql.cs {#src-49490b18c42a}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/CommercialInvoiceSql.cs</code> · 55 lines.

SHA-256: <code>ad761a71c7333a07f89d840c159c18a33dd97cc5fa534d9700fbcefdefb2f78e</code>.

Declarations: <code>CommercialInvoiceSql</code> (line 3).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-dde1a9fa9e58"></span><code>CommercialInvoiceSql.BuildConditions(string,string?)</code><br>38–54 | — | DYNAMIC SQL: inspect manually |

</details>

## SqliteActivityReader.cs {#src-0df1402e7d93}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteActivityReader.cs</code> · 259 lines.

SHA-256: <code>9741d01a316b58631355b7298a99b1119f7c9b933da42e8de6bbb3ecb4c48394</code>.

Declarations: <code>SqliteActivityReader</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-39427223b21c"></span><code>SqliteActivityReader.GetActivityInvoicesAsync(DbConnection,ISessionContext,Guid?,CancellationToken)</code><br>10–112 | HasPermission @21; CreateCommand @41; CreateParameter @68; ToString @70; Add @71; ConfigureAwait @73; ExecuteReaderAsync @73; ReadAsync @74; Parse @76; GetString @76; IsDBNull @80; GetInt64 @81; GetInt32 @86; Parse @87; Add @92 | FROM sales_invoices @42; FROM sales_lines @42; FROM sales_tenders @42; JOIN users @42 · UnauthorizedAccessException @18; UnauthorizedAccessException @27; UnauthorizedAccessException @37 |
| <span id="m-2f645bd8b072"></span><code>SqliteActivityReader.GetPagedActivityInvoicesAsync(DbConnection,ISessionContext,PageRequest,Guid?,CancellationToken)</code><br>122–258 | HasPermission @134; ResolveOrderBy @153; nameof @161; CreateCommand @165; CreateParameter @168; ToString @170; Add @171; ToInt32 @172; ConfigureAwait @172; ExecuteScalarAsync @172; CreateParameter @204; Add @207; ExecuteReaderAsync @219; ReadAsync @220; Parse @222; GetString @222; IsDBNull @226; GetInt64 @227; GetInt32 @232; Parse @233; Add @238 | FROM sales_invoices @167 · UnauthorizedAccessException @131; UnauthorizedAccessException @140; UnauthorizedAccessException @150; ArgumentException @161 · DYNAMIC SQL: inspect manually |

</details>

## SqliteCommercialReader.cs {#src-4b0839d79887}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteCommercialReader.cs</code> · 255 lines.

SHA-256: <code>7950bc9639f959e57ff876ecb65b075d8e1c64202837c3be486b76f8ad9a2ba6</code>.

Declarations: <code>SqliteCommercialReader : ICommercialReader</code> (line 13).

<details markdown>
<summary>Methods, calls, table effects and failures (19)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d128b9ab9bf0"></span><code>SqliteCommercialReader.OpenAsync(string,CancellationToken)</code><br>15–26 | ConfigureAwait @21; OpenAsync @21; HasPermissionAsync @22; DisposeAsync @25 | UnauthorizedAccessException @17; UnauthorizedAccessException @22; rethrow @25 |
| <span id="m-d0d345e2b67c"></span><code>SqliteCommercialReader.Date(Dictionary&lt;string, object?&gt;,string)</code><br>27–27 | Parse @27; Text @27 | No extracted literal effects. |
| <span id="m-f3ef58fd155b"></span><code>SqliteCommercialReader.GetInvoicesAsync(CommercialReadQuery,CancellationToken)</code><br>28–39 | ConfigureAwait @30; OpenAsync @30; BeginTransaction @30; HasActivePermissionAsync @31; BuildConditions @33; Order @34; Trim @35; ToString @35; ReadAsync @36; ToArray @37; Concat @37; ToList @38; Select @38; Parse @38; Text @38; Amount @38; Date @38; NullableGuid @38 | FROM invoice_fulfillment @37 · UnauthorizedAccessException @31 |
| <span id="m-cd12807a164a"></span><code>SqliteCommercialReader.GetPurchaseAsync(Guid,CancellationToken)</code><br>40–55 | ConfigureAwait @42; OpenAsync @42; BeginTransaction @42; ReadAsync @43; Text @49; Add @52; Parse @52; Parse @52; Sum @52; Amount @52; Sum @52; Sum @52; Date @54; TryParse @54 | FROM purchase_receipt_lines @49; FROM supplier_invoice_credit_lines @51; FROM supplier_invoice_credits @43; FROM supplier_invoice_lines @45; FROM supplier_invoices @43; FROM supplier_payments @43; FROM supplier_refunds @43; FROM supplier_return_lines @50; FROM supplier_returns @43; JOIN items @45; JOIN third_parties @43 |
| <span id="m-92a20ab85fb6"></span><code>SqliteCommercialReader.GetUnshippedLinesAsync(Guid,CancellationToken)</code><br>56–67 | ConfigureAwait @58; OpenAsync @58; BeginTransaction @58; ReadAsync @59; Text @62; Min @63; GroupBy @63; Sum @63; Parse @63; Add @64; Parse @64 | FROM invoice_stock_reservations @62; FROM sales_lines @59 |
| <span id="m-c448b4e94a02"></span><code>SqliteCommercialReader.GetReservationsAsync(Guid,CancellationToken)</code><br>68–73 | ConfigureAwait @70; OpenAsync @70; ReadAsync @71; ToList @72; Select @72; Parse @72; Text @72; Parse @72; NullableGuid @72 | FROM invoice_stock_reservations @71; JOIN items @71; JOIN lots @71 |
| <span id="m-3394cb0361d7"></span><code>SqliteCommercialReader.GetShipmentsAsync(PageRequest,string,string,string,Guid?,CancellationToken)</code><br>74–87 | ConfigureAwait @76; OpenAsync @76; BeginTransaction @76; ReadAsync @84; Trim @84; ToString @84; Order @85; ToList @86; Select @86; Parse @86; Text @86; Date @86; IsNullOrEmpty @86; Amount @86 | FROM shipments @77; FROM supplier_returns @77; JOIN invoice_fulfillment @77; JOIN sales_invoices @77; JOIN supplier_invoices @77; JOIN third_parties @77 |
| <span id="m-0501ef8391e4"></span><code>SqliteCommercialReader.GetAccountsAsync(CancellationToken)</code><br>102–107 | ConfigureAwait @104; OpenAsync @104; ReadAsync @105; ToList @106; Select @106; Parse @106; Text @106; Amount @106 | FROM cash_movements @105; FROM money_accounts @105; FROM money_events @105; FROM shifts @105 |
| <span id="m-47560051fb51"></span><code>SqliteCommercialReader.GetMoneyAsync(PageRequest,string,Guid?,MoneyReadFilter?,Guid?,CancellationToken)</code><br>108–116 | ConfigureAwait @110; OpenAsync @110; BeginTransaction @110; ReadAsync @113; Trim @113; ToString @113; Order @114; ToList @115; Select @115; Parse @115; Text @115; Amount @115; Date @115 | FROM cash_movements @114; FROM money_accounts @114; JOIN cash_movements @114 |
| <span id="m-d80faa06eb1c"></span><code>SqliteCommercialReader.Order(PageRequest,Dictionary&lt;string,string&gt;,string)</code><br>117–122 | TryGetValue @119 | No extracted literal effects. |
| <span id="m-eb570856664b"></span><code>SqliteCommercialReader.GetReturnRequestAsync(Guid,CancellationToken)</code><br>123–128 | ConfigureAwait @125; OpenAsync @125; ReadAsync @126; Deserialize(ProcessReturnCommand) @127; Text @127 | FROM return_shipment_requests @126 |
| <span id="m-2769ad3c48e4"></span><code>SqliteCommercialReader.GetPartyAsync(Guid,bool,CancellationToken)</code><br>129–134 | ConfigureAwait @131; OpenAsync @131; ReadAsync @132; Parse @133; Text @133 | FROM third_parties @132 |
| <span id="m-90150914e5cd"></span><code>SqliteCommercialReader.FindPartiesAsync(string,bool,CancellationToken)</code><br>135–140 | ConfigureAwait @137; OpenAsync @137; ReadAsync @138; Trim @138; ToList @139; Select @139; Parse @139; Text @139 | FROM third_parties @138 |
| <span id="m-8b0a8beab672"></span><code>SqliteCommercialReader.GetItemAsync(Guid,bool,CancellationToken)</code><br>141–163 | ConfigureAwait @143; OpenAsync @143; ReadAsync @144; Parse @156; Text @156; Amount @156; IsNullOrEmpty @157; TryParse @157; ResolveFactorAsync @159; Round @162 | FROM item_kits @144; FROM items @144; JOIN item_pricing @144 |
| <span id="m-e3b4c4446833"></span><code>SqliteCommercialReader.FindItemsAsync(string,bool,CancellationToken)</code><br>164–191 | ConfigureAwait @166; OpenAsync @166; ReadAsync @167; Trim @178; Parse @182; Text @182; Amount @182; IsNullOrEmpty @183; TryParse @183; ResolveFactorAsync @185; Add @188; Round @188 | FROM barcodes @167; FROM item_kits @167; FROM items @167; JOIN item_pricing @167 |
| <span id="m-38a6a771786c"></span><code>SqliteCommercialReader.GetKitLeavesAsync(Guid,decimal,string,CancellationToken)</code><br>192–200 | ConfigureAwait @194; OpenAsync @194; BeginTransaction @194; ReadAsync @195; ResolveFactorAsync @196; Text @196; DecomposeToLeavesAsync @197; Where @198; Add @199 | FROM items @195; FROM items @199 · InvalidOperationException @195; InvalidOperationException @196; InvalidOperationException @197 |
| <span id="m-06f8d00c2105"></span><code>SqliteCommercialReader.GetDraftAsync(Guid,bool,CancellationToken)</code><br>201–219 | ConfigureAwait @203; OpenAsync @203; ReadAsync @206; Deserialize(RecordSupplierInvoiceCommand) @207; Text @207; Add @209; Deserialize(SaveOrderDraftCommand) @215; FirstOrDefault @217; ToString @217; Add @217; Parse @217; Parse @217; Amount @217; Join @217; Where @217; Select @217 | FROM draft_cart_lines @213; FROM draft_carts @212; FROM invoice_draft_options @214; FROM item_kits @213; FROM items @209; FROM pending_allocations @217; FROM purchase_invoice_drafts @206; JOIN items @213; JOIN lots @217; JOIN third_parties @206 |
| <span id="m-a1b21ad54c28"></span><code>SqliteCommercialReader.GetSourceInvoicesAsync(Guid,string,CancellationToken)</code><br>220–240 | ConfigureAwait @222; OpenAsync @222; BeginTransaction @222; HasActivePermissionAsync @223; ReadAsync @238; ToList @239; Select @239; Parse @239; Text @239; Amount @239; Date @239 | FROM bank_invoice_collections @229; FROM cancellation_refunds @232; FROM invoice_collection_allocations @228; FROM invoice_fulfillment @238; FROM sale_returns @233; FROM shipments @234; FROM supplier_payments @230; FROM supplier_refunds @231; FROM supplier_returns @235 |
| <span id="m-468ea2d10f97"></span><code>SqliteCommercialReader.GetHistoryAsync(Guid,string,CancellationToken)</code><br>241–253 | ConfigureAwait @244; OpenAsync @244; ReadAsync @251; ToList @252; Select @252; Text @252; Date @252 | FROM commercial_shipping_events @248; FROM invoice_cancellations @249; FROM purchase_receipts @247; FROM return_shipment_requests @249; FROM shipment_events @248; FROM shipments @249; FROM supplier_invoice_credits @247; FROM supplier_payments @247; FROM supplier_refunds @247; FROM supplier_returns @247; JOIN money_events @247; JOIN users @247; JOIN users @248; JOIN users @249 |

</details>

## SqliteCustomerReader.cs {#src-8e7b644b5763}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteCustomerReader.cs</code> · 327 lines.

SHA-256: <code>bd9faa9814599346305bda9951d7de30271920f38527cecd065b4bd20a4ca1ff</code>.

Declarations: <code>SqliteCustomerReader</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-bc56f68c6a47"></span><code>SqliteCustomerReader.GetCustomersAsync(DbConnection,string?,bool,ISessionContext?,CancellationToken)</code><br>17–101 | HasPermission @31; CreateCommand @43; IsNullOrWhiteSpace @51; CreateParameter @54; Trim @56; Add @57; ConfigureAwait @68; ExecuteReaderAsync @68; ReadAsync @69; TryParse @71; GetString @71; NewGuid @71; IsDBNull @74; GetInt32 @78; Parse @80; Add @85 | FROM third_parties @44 · UnauthorizedAccessException @28; UnauthorizedAccessException @37 |
| <span id="m-62c448c54d53"></span><code>SqliteCustomerReader.GetCustomerByIdAsync(DbConnection,Guid,ISessionContext?,CancellationToken)</code><br>103–172 | HasPermission @116; CreateCommand @126; CreateParameter @134; ToString @136; Add @137; ConfigureAwait @139; ExecuteReaderAsync @139; ReadAsync @140; TryParse @142; GetString @142; NewGuid @142; IsDBNull @145; GetInt32 @149; Parse @151 | FROM third_parties @127 · UnauthorizedAccessException @113; UnauthorizedAccessException @122 |
| <span id="m-f697ebc9f057"></span><code>SqliteCustomerReader.GetPagedThirdPartiesAsync(DbConnection,PageRequest,string?,string?,LifecycleStatusScope,ISessionContext?,Guid?,CancellationToken)</code><br>188–326 | HasPermission @205; ResolveOrderBy @215; nameof @223; Create @226; CreateCommand @230; AddParameters @233; ToInt32 @235; ConfigureAwait @235; ExecuteScalarAsync @235; CreateParameter @255; Add @258; ExecuteReaderAsync @265; ReadAsync @266; TryParse @268; GetString @268; NewGuid @268; IsDBNull @271; GetInt32 @284; Parse @285; Add @296 | UnauthorizedAccessException @202; UnauthorizedAccessException @211; ArgumentException @223 · DYNAMIC SQL: inspect manually |

</details>

## SqliteExpenseReader.cs {#src-f5bb61f5e17f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteExpenseReader.cs</code> · 534 lines.

SHA-256: <code>b85ed81a37c5c4fc3a8e2d902ac8f09802144fc64432af45cdd5f767bd5eb621</code>.

Declarations: <code>SqliteExpenseReader : IExpenseReader</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-053acf5ef36a"></span><code>SqliteExpenseReader.GetConnectionAsync(string,CancellationToken)</code><br>29–67 | ConfigureAwait @46; OpenAsync @46; HasPermissionAsync @52; DisposeAsync @63 | UnauthorizedAccessException @33; UnauthorizedAccessException @55; rethrow @65 |
| <span id="m-fa7975b263da"></span><code>SqliteExpenseReader.AddParam(DbCommand,string,object?)</code><br>69–75 | CreateParameter @71; Add @74 | No extracted literal effects. |
| <span id="m-e2f650bdb9b2"></span><code>SqliteExpenseReader.GetExpensesAsync(ExpenseReadQuery,CancellationToken)</code><br>77–252 | ConfigureAwait @81; GetConnectionAsync @81; Add @89; Add @90; ToString @90; ToString @96; ToString @102; ToString @108; IsNullOrWhiteSpace @111; Trim @114; ToLowerInvariant @117; Trim @117; Join @139; CreateCommand @154; AddParam @157; ExecuteScalarAsync @158; ExecuteReaderAsync @218; ReadAsync @219; Add @221; Parse @222; GetString @222; GetInt64 @227; GetInt32 @231; Parse @234; IsDBNull @235; DisposeAsync @249 | DYNAMIC SQL: inspect manually |
| <span id="m-93b8b924a539"></span><code>SqliteExpenseReader.GetExpenseAsync(Guid,CancellationToken)</code><br>254–400 | ConfigureAwait @258; GetConnectionAsync @258; CreateCommand @270; AddParam @302; ToString @302; ExecuteReaderAsync @304; ReadAsync @305; Parse @311; GetString @311; GetInt64 @316; GetInt32 @320; Parse @323; IsDBNull @324; ExecuteReaderAsync @358; ReadAsync @359; Add @361; GetString @362; GetInt64 @365; IsDBNull @368; DisposeAsync @397 | FROM expense_payments @272; FROM expense_payments @346; FROM expense_records @272; JOIN expense_attachments @272; JOIN expense_categories @272; JOIN money_accounts @346; JOIN person_records @272; JOIN users @346 |
| <span id="m-9dd9ece90c18"></span><code>SqliteExpenseReader.GetCategoriesAsync(bool,CancellationToken)</code><br>402–448 | ConfigureAwait @406; GetConnectionAsync @406; CreateCommand @409; AddParam @422; ExecuteReaderAsync @425; ReadAsync @426; Add @428; Parse @429; GetString @429; GetInt32 @432; Parse @435; DisposeAsync @445 | FROM expense_categories @410; FROM expense_records @410 |
| <span id="m-8586adced3c7"></span><code>SqliteExpenseReader.GetCategoryAsync(Guid,CancellationToken)</code><br>450–494 | ConfigureAwait @454; GetConnectionAsync @454; CreateCommand @457; AddParam @469; ToString @469; ExecuteReaderAsync @471; ReadAsync @472; Parse @478; GetString @478; GetInt32 @481; Parse @484; DisposeAsync @491 | FROM expense_categories @458; FROM expense_records @458 |
| <span id="m-02a8ef07fad4"></span><code>SqliteExpenseReader.FindPayeesAsync(string,CancellationToken)</code><br>496–533 | ConfigureAwait @500; GetConnectionAsync @500; CreateCommand @503; AddParam @510; Trim @510; ExecuteReaderAsync @514; ReadAsync @515; Add @517; Parse @518; GetString @518; DisposeAsync @530 | FROM person_records @504 |

</details>

## SqliteInventoryReader.cs {#src-a98e04a6dd02}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteInventoryReader.cs</code> · 681 lines.

SHA-256: <code>db5f8f8f63f12bb863705ec8d1a25700438c8d2bdd531d92ffb989428132d61a</code>.

Declarations: <code>SqliteInventoryReader</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-fe3b6bc0d7ee"></span><code>SqliteInventoryReader.GetKitAvailabilityAsync(DbConnection,Guid?,IReadOnlyList&lt;KitComponentInput&gt;,ISessionContext,CancellationToken)</code><br>13–132 | ConfigureAwait @23; BeginTransactionAsync @23; DecomposeToLeavesAsync @29; CreateCommand @43; AddParameter @46; ToString @46; ExecuteReaderAsync @47; ReadAsync @48; GetString @50; GetInt32 @53; Equals @55; DisposeAsync @56; IsNullOrWhiteSpace @60; ResolveFactorAsync @61; GetActiveKitInfoAsync @67; AddDemand @76; ToArray @86; Select @86; GetLocationBalanceAsync @101; ToString @115; ToString @117; ToInt64 @118; ExecuteScalarAsync @118; Min @119; Max @122 | FROM items @45; FROM pending_allocations @107; FROM serials @107 · UnauthorizedAccessException @21 |
| <span id="m-1e4d462c50ab"></span><code>SqliteInventoryReader.GetInventoryItemsAsync(DbConnection,string,int,ISessionContext,string?,bool,CancellationToken)</code><br>134–300 | IsNullOrWhiteSpace @149; Equals @150; CreateCommand @177; CreateParameter @212; Add @215; ConfigureAwait @217; ExecuteReaderAsync @217; ReadAsync @218; IsDBNull @220; GetString @220; TryParse @222; Add @227; Parse @228; GetInt64 @233; GetInt32 @236; ToDecimal @238; GetDouble @238; TryParse @244; GetLocationBalanceAsync @262; GetPhysicalOnHandAsync @265; Add @270 | FROM items @182; JOIN product_categories @182 · UnauthorizedAccessException @145 |
| <span id="m-cd53d59a93b2"></span><code>SqliteInventoryReader.GetStockBalanceAsync(DbConnection,Guid,string,CancellationToken)</code><br>302–313 | ConfigureAwait @310; GetLocationBalanceAsync @310 | No extracted literal effects. |
| <span id="m-aee040e64835"></span><code>SqliteInventoryReader.AddDemand(Dictionary&lt;Guid, (string Sku, string Name, decimal Quantity, string BaseUnit, bool Tracked, bool Serial)&gt;,Guid,string,string,decimal,string,bool,bool)</code><br>315–323 | TryGetValue @319 | No extracted literal effects. |
| <span id="m-d791f80d410f"></span><code>SqliteInventoryReader.AddParameter(DbCommand,string,object)</code><br>325–331 | CreateParameter @327; Add @330 | No extracted literal effects. |
| <span id="m-dec79a3b4b28"></span><code>SqliteInventoryReader.GetPagedInventoryItemsAsync(DbConnection,string,int,ISessionContext,PageRequest,string?,LifecycleStatusScope,bool,string?,string?,string?,Guid?,CancellationToken)</code><br>345–626 | ConfigureAwait @364; HasActiveCatalogAdminAsync @364; ResolveOrderBy @369; nameof @377; IsNullOrWhiteSpace @380; Equals @381; Equals @383; Add @390; Equals @408; Join @419; CreateParameter @423; Add @426; ToString @432; Trim @439; Trim @449; CreateCommand @463; AddFilterParameters @468; ToInt32 @469; ExecuteScalarAsync @469; ExecuteReaderAsync @542; ReadAsync @543; IsDBNull @545; GetString @545; TryParse @547; Add @552; Parse @553; GetInt64 @558; GetInt32 @561; ToDecimal @563; GetDouble @563; TryParse @569; GetLocationBalanceAsync @588; GetPhysicalOnHandAsync @591; Add @596 | FROM barcodes @404; FROM stock_movements @416 · UnauthorizedAccessException @362; UnauthorizedAccessException @366; ArgumentException @377 · DYNAMIC SQL: inspect manually |
| <span id="m-4d93ab3bcbd2"></span><code>SqliteInventoryReader.CanReviewClassificationAsync(DbConnection,ISessionContext,CancellationToken)</code><br>628–638 | ConfigureAwait @637; HasActiveCatalogAdminAsync @637 | No extracted literal effects. |
| <span id="m-5b988e985147"></span><code>SqliteInventoryReader.GetActiveUnclassifiedInventoryItemCountAsync(DbConnection,ISessionContext,CancellationToken)</code><br>640–658 | ConfigureAwait @649; HasActiveCatalogAdminAsync @649; CreateCommand @654; ToInt32 @657; ExecuteScalarAsync @657 | FROM items @655 · UnauthorizedAccessException @647; UnauthorizedAccessException @651 |
| <span id="m-cca1e7a4e3b7"></span><code>SqliteInventoryReader.HasActiveCatalogAdminAsync(DbConnection,ISessionContext,CancellationToken)</code><br>660–680 | HasPermission @665; CreateCommand @670; CreateParameter @675; ToString @677; Add @678; ToInt64 @679; ConfigureAwait @679; ExecuteScalarAsync @679 | FROM users @671; JOIN roles @671; JOIN user_roles @671 |

</details>

## SqliteInventoryTraceabilityReader.cs {#src-af35f0520c07}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteInventoryTraceabilityReader.cs</code> · 66 lines.

SHA-256: <code>ee4d7210de8fae6ca55788bca9c01ef7cc4bc28ce21cd392381f98e75022902c</code>.

Declarations: <code>SqliteInventoryTraceabilityReader</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-807da3b23cb5"></span><code>SqliteInventoryTraceabilityReader.GetLotsAsync(DbConnection,ISessionContext,Guid,PageRequest,CancellationToken)</code><br>11–36 | EnsureSession @13; BeginTransaction @15; CreateCommand @18; Add @22; ToString @22; ToInt32 @23; ConfigureAwait @23; ExecuteScalarAsync @23; ExecuteReaderAsync @26; ReadAsync @27; Add @27; Parse @27; GetString @27; ReadLotAsync @32; Add @33; Commit @35 | FROM lots @21; FROM lots @24 · InvalidOperationException @14 |
| <span id="m-be5014354c4d"></span><code>SqliteInventoryTraceabilityReader.GetSerialsAsync(DbConnection,ISessionContext,Guid,PageRequest,CancellationToken)</code><br>38–63 | EnsureSession @40; BeginTransaction @42; CreateCommand @45; Add @49; ToString @49; ToInt32 @50; ConfigureAwait @50; ExecuteScalarAsync @50; ExecuteReaderAsync @53; ReadAsync @54; Add @54; GetString @54; ReadSerialAsync @59; Add @60; Commit @62 | FROM serials @48; FROM serials @51 · InvalidOperationException @41 |
| <span id="m-8026ee43d51a"></span><code>SqliteInventoryTraceabilityReader.EnsureSession(ISessionContext)</code><br>64–65 | — | UnauthorizedAccessException @65 |

</details>

## SqliteInvoiceAndRegisterReader.cs {#src-d3a055c736d8}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteInvoiceAndRegisterReader.cs</code> · 184 lines.

SHA-256: <code>4a9f8575aef1c4feb6a930c49c55f26a65158846048cc788caf3ae177fe3ef21</code>.

Declarations: <code>SqliteInvoiceAndRegisterReader : IInvoiceAndRegisterReader</code> (line 12), <code>NoJobs : IHardwareJobRepository</code> (line 162), <code>ReadOnlyWork : IUnitOfWork</code> (line 169), <code>InvoicePageDirection</code> (line 179).

<details markdown>
<summary>Methods, calls, table effects and failures (17)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-760b784a07b2"></span><code>SqliteInvoiceAndRegisterReader.OpenAsync(string,CancellationToken)</code><br>14–26 | ConfigureAwait @20; OpenAsync @20; HasPermissionAsync @21; DisposeAsync @25 | UnauthorizedAccessException @16; UnauthorizedAccessException @22; rethrow @25 |
| <span id="m-74aa6fd2162a"></span><code>SqliteInvoiceAndRegisterReader.GetInvoicesAsync(InvoiceReadQuery,CancellationToken)</code><br>45–63 | ResolveOrderBy @50; nameof @51; ConfigureAwait @52; OpenAsync @52; BeginTransaction @52; Trim @56; BusinessDateAsync @56; ReadAsync @57; IsDescending @58; ToArray @59; Concat @59; ReadBalanceAsync @61; Parse @61; Text @61; Add @61; Amount @62 | FROM sale_returns @49 · ArgumentException @51 |
| <span id="m-fe242dd5f2b1"></span><code>SqliteInvoiceAndRegisterReader.GetSelectedInvoicesAsync(IReadOnlyList&lt;Guid&gt;,CancellationToken)</code><br>65–73 | Count @67; Distinct @67; nameof @67; ConfigureAwait @68; OpenAsync @68; BeginTransaction @69; ReadBalanceAsync @70; Add @70; Any @71; Distinct @71; Select @71 | ArgumentException @67; InvalidOperationException @70; InvalidOperationException @71 |
| <span id="m-2bf590316e9f"></span><code>SqliteInvoiceAndRegisterReader.GetInvoiceAsync(Guid,CancellationToken)</code><br>74–106 | ConfigureAwait @76; OpenAsync @76; BeginTransaction @76; ReadBalanceAsync @77; ReadAsync @78; Parse @82; Text @82; QuantityValue @82; Sum @84; Parse @84; Min @88; GroupBy @88; Sum @88; Max @89; ToList @92; Select @92; Where @92; Amount @92; NullableGuid @93; Add @94; Add @95; Select @104; When @104 | FROM bank_invoice_collections @97; FROM invoice_collections @97; FROM invoice_stock_reservations @85; FROM refund_lines @83; FROM sale_return_lines @83; FROM sale_returns @97; FROM sales_line_kit_allocations @91; FROM sales_lines @78; JOIN invoice_collection_allocations @97; JOIN items @78; JOIN items @91; JOIN lots @78; JOIN lots @91; JOIN money_accounts @97; JOIN money_events @97 |
| <span id="m-e476fc7c74cc"></span><code>SqliteInvoiceAndRegisterReader.GetRegisterAsync(RegisterReadQuery,CancellationToken)</code><br>108–134 | nameof @110; ConfigureAwait @111; OpenAsync @111; BeginTransaction @112; ResolveOrderBy @121; Trim @122; Trim @122; Trim @122; Trim @122; ReadAsync @124; ToArray @128; Concat @128; ToList @129; Select @129; Parse @129; Text @129; When @129; NullableGuid @130; Amount @130; IsNullOrEmpty @131; QuantityValue @131; ToDictionary @133; GroupBy @133; Sum @133; Select @133 | FROM cash_loss_records @115; FROM inventory_loss_records @114; FROM return_disposition_resolutions @114; FROM return_dispositions @117; FROM sale_discount_records @116; FROM sale_returns @114; FROM sales_invoices @114; FROM store_config @126; FROM third_parties @119; FROM users @114; FROM users @115; FROM users @116; FROM users @117; JOIN items @114; JOIN items @117; JOIN return_dispositions @114; JOIN sale_return_lines @114; JOIN sale_return_lines @117; JOIN sale_returns @114; JOIN sale_returns @117; JOIN sales_invoices @116; JOIN sales_invoices @117; JOIN sales_lines @116 · ArgumentException @110; ArgumentException @121 |
| <span id="m-54dddb8ec712"></span><code>SqliteInvoiceAndRegisterReader.GetRegisterSourceAsync(FinancialRegisterKind,Guid,CancellationToken)</code><br>136–152 | ConfigureAwait @138; OpenAsync @138; BeginTransaction @139; nameof @145; ReadAsync @147; Amount @150; Text @151; NullableGuid @151 | FROM cash_loss_records @142; FROM inventory_loss_records @143; FROM return_disposition_resolutions @143; FROM return_dispositions @143; FROM sale_discount_records @144; JOIN sale_return_lines @143; JOIN sale_returns @143; JOIN sales_invoices @144; JOIN sales_lines @144; JOIN shift_z_reports @142 |
| <span id="m-16e0107b5104"></span><code>SqliteInvoiceAndRegisterReader.PreviewReturnAsync(ProcessReturnCommand,CancellationToken)</code><br>154–160 | ConfigureAwait @156; OpenAsync @156; BeginTransaction @157; PreviewAsync @159 | No extracted literal effects. |
| <span id="m-2106c750665f"></span><code>SqliteInvoiceAndRegisterReader.When(Dictionary&lt;string,object?&gt;)</code><br>161–161 | Parse @161; Text @161 | No extracted literal effects. |
| <span id="m-06ec805bf51f"></span><code>NoJobs.EnqueueAsync(string,string,CancellationToken)</code><br>164–164 | — | No extracted literal effects. |
| <span id="m-e53a6e42e55f"></span><code>NoJobs.GetPendingAsync(int,CancellationToken)</code><br>165–165 | — | No extracted literal effects. |
| <span id="m-617755e0e1ee"></span><code>NoJobs.MarkCompletedAsync(string,CancellationToken)</code><br>166–166 | — | No extracted literal effects. |
| <span id="m-088bc81dbb1b"></span><code>NoJobs.MarkFailedAsync(string,string,CancellationToken)</code><br>167–167 | — | No extracted literal effects. |
| <span id="m-81e67aad988b"></span><code>ReadOnlyWork.BeginTransactionAsync(CancellationToken)</code><br>172–172 | — | No extracted literal effects. |
| <span id="m-fa34f009d896"></span><code>ReadOnlyWork.CommitAsync(CancellationToken)</code><br>173–173 | — | No extracted literal effects. |
| <span id="m-ee8f7e05d7e7"></span><code>ReadOnlyWork.RollbackAsync(CancellationToken)</code><br>174–174 | — | No extracted literal effects. |
| <span id="m-eb8a67243eb0"></span><code>ReadOnlyWork.DisposeAsync()</code><br>175–175 | — | No extracted literal effects. |
| <span id="m-524649348bbf"></span><code>InvoicePageDirection.IsDescending(PageRequest)</code><br>181–181 | — | No extracted literal effects. |

</details>

## SqliteItemPriceHistoryReader.cs {#src-b2e0674865c9}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteItemPriceHistoryReader.cs</code> · 66 lines.

SHA-256: <code>795867e941323aec63547cbffe1e2f3840bd4f16737f52f47e1c258a994bddb0</code>.

Declarations: <code>SqliteItemPriceHistoryReader</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0d08e267bc0d"></span><code>SqliteItemPriceHistoryReader.GetHistoryAsync(DbConnection,ISessionContext,Guid,string,PageRequest,CancellationToken)</code><br>12–54 | Contains @24; Max @25; Equals @26; CreateCommand @30; Add @32; ToString @32; ToInt32 @33; ConfigureAwait @33; ExecuteScalarAsync @33; Min @34; Ceiling @34; ExecuteReaderAsync @51; ReadAsync @52; Add @52; Read @52 | UnauthorizedAccessException @21; InvalidOperationException @23 · DYNAMIC SQL: inspect manually |
| <span id="m-cbcca02e5050"></span><code>SqliteItemPriceHistoryReader.Read(DbDataReader)</code><br>56–60 | Parse @57; GetString @57; Text @57; Long @58; DecimalValue @58; ToUniversalTime @60; Parse @60 | No extracted literal effects. |
| <span id="m-6e4ebfab0827"></span><code>SqliteItemPriceHistoryReader.Text(DbDataReader,int)</code><br>62–62 | IsDBNull @62; GetString @62 | No extracted literal effects. |
| <span id="m-6e52e6a843ab"></span><code>SqliteItemPriceHistoryReader.Long(DbDataReader,int)</code><br>63–63 | IsDBNull @63; GetInt64 @63 | No extracted literal effects. |
| <span id="m-bf0563e40d07"></span><code>SqliteItemPriceHistoryReader.DecimalValue(DbDataReader,int)</code><br>64–64 | IsDBNull @64; TryParse @64; GetString @64 | No extracted literal effects. |
| <span id="m-98b9f90b8bb6"></span><code>SqliteItemPriceHistoryReader.Add(DbCommand,string,object)</code><br>65–65 | CreateParameter @65; Add @65 | No extracted literal effects. |

</details>

## SqliteManualPaymentDisplay.cs {#src-9b4adc7a5d02}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteManualPaymentDisplay.cs</code> · 91 lines.

SHA-256: <code>ca667002fd835b470c443c07fa254102f9dd427b822758102ad482ae3f21aa48</code>.

Declarations: <code>ManualPaymentDisplay</code> (line 8), <code>SqliteManualPaymentDisplay</code> (line 17), <code>SaveManualPaymentDisplayHandler : ICommandHandler&lt;SaveManualPaymentDisplayCommand, bool&gt;</code> (line 33).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-275c52028714"></span><code>SqliteManualPaymentDisplay.LoadAsync(DbConnection,CancellationToken)</code><br>19–30 | CreateCommand @21; ConfigureAwait @23; ExecuteReaderAsync @23; ReadAsync @24; GetString @27; IsDBNull @27; GetValue @27 | FROM manual_payment_display @22 |
| <span id="m-711bf042b1db"></span><code>SaveManualPaymentDisplayHandler.HandleAsync(SaveManualPaymentDisplayCommand,CommandEnvelope&lt;SaveManualPaymentDisplayCommand&gt;,CancellationToken)</code><br>35–71 | CreateCommand @38; Add @42; ToString @42; ConfigureAwait @43; ExecuteScalarAsync @43; Failure(bool) @44; ValidImage @49; Trim @59; Trim @62; Trim @63; Trim @64; ToString @67; ExecuteNonQueryAsync @69; Success(bool) @70 | FROM users @41; JOIN user_roles @41; UPDATE manual_payment_display @54 · AUTH_UNAUTHORIZED @44; INVALID_PAYMENT_DETAILS @48; INVALID_PAYMENT_IMAGE @50 |
| <span id="m-82ec30f00b2c"></span><code>SaveManualPaymentDisplayHandler.ValidImage(byte[]?,string?)</code><br>73–82 | SequenceEqual @78; AsSpan @78 | No extracted literal effects. |
| <span id="m-99fb78c81996"></span><code>SaveManualPaymentDisplayHandler.Add(DbCommand,string,object)</code><br>84–90 | CreateParameter @86; Add @89 | No extracted literal effects. |

</details>

## SqliteManufacturingReader.cs {#src-e6b335397326}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteManufacturingReader.cs</code> · 1,174 lines.

SHA-256: <code>d67350397501584d2a185662e8dc18a1aa51cd476831516cc3b87cd18dfca54c</code>.

Declarations: <code>SqliteManufacturingReader : IManufacturingReader</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (14)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f7f133fcb1d7"></span><code>SqliteManufacturingReader.GetBomsAsync(ISessionContext?,PageRequest?,bool,CancellationToken)</code><br>10–143 | HasPermission @21; CreateCommand @31; IndexOf @42; AddPaging @45; ConfigureAwait @48; ExecuteReaderAsync @48; ReadAsync @50; Add @52; Parse @53; GetString @53; GetInt32 @57; GetDecimal @59; CloseAsync @63; CreateParameter @75; ToString @77; Add @78; ExecuteReaderAsync @80; ReadAsync @81; Add @83; GetString @84; GetDecimal @88; CreateParameter @104; Add @107; ExecuteReaderAsync @109; ReadAsync @110; GetString @112; TryParse @113; NewGuid @113; Add @114; GetDecimal @121; Parse @122; IsDBNull @123; GetInt32 @123; Add @128 | FROM bom_items @69; FROM bom_outputs @97; FROM boms @32; JOIN items @32; JOIN items @69; JOIN items @97 · UnauthorizedAccessException @18; UnauthorizedAccessException @25 |
| <span id="m-b9e976bace6a"></span><code>SqliteManufacturingReader.GetKitsAsync(ISessionContext?,CancellationToken)</code><br>145–234 | HasPermission @156; CreateCommand @166; ConfigureAwait @174; ExecuteReaderAsync @174; ReadAsync @176; Add @178; Parse @179; GetString @179; GetInt32 @183; Parse @186; CloseAsync @189; CreateParameter @201; ToString @203; Add @204; ExecuteReaderAsync @206; ReadAsync @207; Add @209; GetString @210; GetDecimal @214; Add @220 | FROM item_kit_components @195; FROM item_kits @167; JOIN items @167; JOIN items @195 · UnauthorizedAccessException @153; UnauthorizedAccessException @160 |
| <span id="m-908e5aeda7a8"></span><code>SqliteManufacturingReader.GetProductionRunsAsync(ISessionContext?,PageRequest?,bool,CancellationToken)</code><br>236–466 | HasPermission @247; CreateCommand @258; IndexOf @274; AddPaging @277; ConfigureAwait @287; ExecuteReaderAsync @287; ReadAsync @288; Add @290; Parse @291; GetString @291; GetDecimal @297; IsDBNull @298; Parse @306; CloseAsync @313; CreateParameter @331; ToString @333; Add @334; ExecuteReaderAsync @336; ReadAsync @337; Add @339; GetString @340; IsDBNull @342; GetDecimal @347; Parse @350; GetInt64 @355; CreateParameter @375; Add @378; ExecuteReaderAsync @380; ReadAsync @381; Add @383; GetString @384; IsDBNull @386; GetDecimal @391; GetInt64 @398; CreateParameter @415; Add @418; ExecuteReaderAsync @420; ReadAsync @421; Add @423; GetString @424; IsDBNull @431; GetInt64 @432; Add @438 | FROM production_run_inputs @320; FROM production_run_outputs @364; FROM production_run_scrap @407; FROM production_runs @259; JOIN boms @259; JOIN items @259; JOIN items @320; JOIN items @364; JOIN items @407; JOIN lots @259; JOIN lots @320; JOIN lots @364 · UnauthorizedAccessException @244; UnauthorizedAccessException @252 |
| <span id="m-ede2cd3bf4d2"></span><code>SqliteManufacturingReader.AddPaging(DbCommand,PageRequest)</code><br>467–471 | CreateParameter @470; Add @470 | No extracted literal effects. |
| <span id="m-07e91cfaf545"></span><code>SqliteManufacturingReader.GetPagedBomsAsync(ISessionContext,PageRequest)</code><br>473–478 | ConfigureAwait @475; GetBomsAsync @475; CreateCommand @476; ToInt32 @477; ExecuteScalarAsync @477 | FROM boms @476 |
| <span id="m-c16ef8403aee"></span><code>SqliteManufacturingReader.GetPagedRunsAsync(ISessionContext,PageRequest,bool)</code><br>480–485 | ConfigureAwait @482; GetProductionRunsAsync @482; CreateCommand @483; ToInt32 @484; ExecuteScalarAsync @484 | FROM production_runs @483 |
| <span id="m-92c4f9466ca6"></span><code>SqliteManufacturingReader.ValidateSessionForBoms(ISessionContext?)</code><br>487–503 | HasPermission @496 | UnauthorizedAccessException @493; UnauthorizedAccessException @500 |
| <span id="m-57b810d9459e"></span><code>SqliteManufacturingReader.ValidateSessionForProductionRuns(ISessionContext?)</code><br>505–522 | HasPermission @514 | UnauthorizedAccessException @511; UnauthorizedAccessException @519 |
| <span id="m-0bdf58826832"></span><code>SqliteManufacturingReader.AddParam(DbCommand,string,object)</code><br>524–530 | CreateParameter @526; Add @529 | No extracted literal effects. |
| <span id="m-6ca231f0c96e"></span><code>SqliteManufacturingReader.GetRecipesAsync(RecipeReadQuery,ISessionContext?,CancellationToken)</code><br>532–667 | ThrowIfNull @537; ValidateSessionForBoms @538; ConfigureAwait @542; OpenAsync @542; ResolveOrderBy @546; nameof @554; CreateCommand @558; Add @562; AddParam @563; ToString @563; ToString @574; ToString @580; IsNullOrWhiteSpace @583; NormalizeQuery @585; IsNullOrEmpty @586; ToSubstringPattern @594; Join @598; ToInt32 @607; ExecuteScalarAsync @607; ExecuteReaderAsync @648; ReadAsync @649; Add @651; Parse @652; GetString @652; GetInt32 @654; IsDBNull @658; GetDecimal @659 | FROM bom_items @579; FROM bom_items @588; JOIN items @588 · ArgumentException @554 · DYNAMIC SQL: inspect manually |
| <span id="m-cd65d3df639f"></span><code>SqliteManufacturingReader.GetProductionRunsAsync(ProductionRunReadQuery,ISessionContext?,CancellationToken)</code><br>669–804 | ThrowIfNull @674; ValidateSessionForProductionRuns @675; ConfigureAwait @679; OpenAsync @679; ResolveOrderBy @683; nameof @691; CreateCommand @695; Add @699; AddParam @700; ToString @700; IsNullOrWhiteSpace @703; Equals @703; ToString @720; NormalizeQuery @725; IsNullOrEmpty @726; ToSubstringPattern @733; Join @737; ToInt32 @747; ExecuteScalarAsync @747; ExecuteReaderAsync @783; ReadAsync @784; Add @786; Parse @787; GetString @787; GetDecimal @793; IsDBNull @794; Parse @796 | ArgumentException @691 · DYNAMIC SQL: inspect manually |
| <span id="m-f2a737a45b8d"></span><code>SqliteManufacturingReader.GetRecipeDetailAsync(Guid,ISessionContext?,CancellationToken)</code><br>806–926 | ValidateSessionForBoms @811; ConfigureAwait @815; OpenAsync @815; CreateCommand @818; AddParam @825; ToString @825; ExecuteReaderAsync @836; ReadAsync @838; Parse @843; GetString @843; GetInt32 @847; GetDecimal @849; ToString @863; ExecuteReaderAsync @865; ReadAsync @866; Add @868; GetString @869; GetDecimal @873; ExecuteReaderAsync @894; ReadAsync @895; GetString @897; TryParse @898; NewGuid @898; Add @899; GetDecimal @906; Parse @907; IsDBNull @908; GetInt32 @908 | FROM bom_items @856; FROM bom_outputs @884; FROM boms @819; JOIN items @819; JOIN items @856; JOIN items @884 |
| <span id="m-39f3f794dc4d"></span><code>SqliteManufacturingReader.GetProductionRunDetailAsync(Guid,ISessionContext?,CancellationToken)</code><br>928–1130 | ValidateSessionForProductionRuns @933; ConfigureAwait @937; OpenAsync @937; CreateCommand @940; AddParam @953; ToString @953; ExecuteReaderAsync @964; ReadAsync @966; Parse @971; GetString @971; GetDecimal @977; IsDBNull @978; Parse @986; ToString @1007; ExecuteReaderAsync @1009; ReadAsync @1010; Add @1012; GetString @1013; IsDBNull @1015; GetDecimal @1020; Parse @1023; GetInt64 @1028; ExecuteReaderAsync @1050; ReadAsync @1051; Add @1053; GetString @1054; IsDBNull @1056; GetDecimal @1061; GetInt64 @1068; ExecuteReaderAsync @1087; ReadAsync @1088; Add @1090; GetString @1091; IsDBNull @1098; GetInt64 @1099 | FROM production_run_inputs @996; FROM production_run_outputs @1037; FROM production_run_scrap @1077; FROM production_runs @941; JOIN boms @941; JOIN items @1037; JOIN items @1077; JOIN items @941; JOIN items @996; JOIN lots @1037; JOIN lots @941; JOIN lots @996 |
| <span id="m-dda9aa3deb15"></span><code>SqliteManufacturingReader.GetActiveRecipesForOutputAsync(Guid,ISessionContext?,CancellationToken)</code><br>1132–1173 | ValidateSessionForBoms @1137; ConfigureAwait @1141; OpenAsync @1141; CreateCommand @1145; AddParam @1152; ToString @1152; ExecuteReaderAsync @1155; ReadAsync @1157; Add @1159; Parse @1159; GetString @1159; GetRecipeDetailAsync @1165; Add @1168 | FROM boms @1146 |

</details>

## SqlitePricingReader.cs {#src-35c754a3f892}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqlitePricingReader.cs</code> · 218 lines.

SHA-256: <code>bd5cd9af314d754bf26ba24186c919b157da4aa60f56fef36753dbc2baa2459a</code>.

Declarations: <code>PricingPreviewItem</code> (line 8), <code>SqlitePricingReader</code> (line 21).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f2e25a942e57"></span><code>SqlitePricingReader.GetPricingPreviewAsync(DbConnection,string,string,string,decimal,long,string,IReadOnlyList&lt;Guid&gt;?,decimal,CancellationToken)</code><br>23–217 | CreateCommand @37; ConfigureAwait @40; ExecuteReaderAsync @40; ReadAsync @41; GetInt32 @43; ExecuteReaderAsync @52; Add @55; GetString @57; IsDBNull @59; ParsePricingMethod @66; ParseRoundingRule @67; TryConvertRoundingIncrement @70; Add @84; CreateParameter @85; ToString @87; Add @88; Join @95; ExecuteReaderAsync @112; Add @115; Parse @116; GetInt64 @119; Add @134; ToLowerInvariant @142; ResolveEffectiveBasePrice @197; Round @200; Where @204; ResolveTierPrice @207 | FROM items @101; FROM price_level_settings @51; FROM store_config @39; JOIN item_pricing @101 · DYNAMIC SQL: inspect manually |

</details>

## SqliteProductionReaders.cs {#src-212da8ad4eb4}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteProductionReaders.cs</code> · 472 lines.

SHA-256: <code>6ae8388e1a2114097991fa94748b5a7db18325a317da7d2fe78248c4e0a8b95e</code>.

Declarations: <code>SqliteStoreProfileReader</code> (line 11), <code>SqliteCatalogReader</code> (line 104), <code>SqliteShiftReader</code> (line 422).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a38b54dd5796"></span><code>SqliteStoreProfileReader.GetStoreProfileAsync(DbConnection,CancellationToken)</code><br>13–101 | CreateCommand @32; ConfigureAwait @41; ExecuteReaderAsync @41; ReadAsync @42; GetString @44; GetInt32 @47; GetDecimal @48; IsDBNull @50; Equals @79 | FROM business_profile_config @61; FROM store_config @34 · InvalidOperationException @56 |
| <span id="m-a91e3305763a"></span><code>SqliteCatalogReader.GetActiveItemsAsync(DbConnection,string,int,CancellationToken)</code><br>110–117 | GetActiveItemsAsync @116 | No extracted literal effects. |
| <span id="m-f102c4464340"></span><code>SqliteCatalogReader.GetActiveItemsAsync(DbConnection,string,int,DateTime?,CancellationToken)</code><br>119–288 | Pow @153; CreateCommand @155; ConfigureAwait @172; ExecuteReaderAsync @172; ReadAsync @173; Parse @175; GetString @175; IsDBNull @178; GetInt64 @179; GetInt32 @182; TryParse @193; Equals @198; Add @207; ReadBarcodeFactsAsync @215; ReadGrossSoldQuantities30DaysAsync @224; TryGetValue @246; GetValueOrDefault @256; Add @259 | FROM items @157; JOIN product_categories @157 · InvalidOperationException @128; InvalidOperationException @200 |
| <span id="m-bb99bce66d4e"></span><code>SqliteCatalogReader.ReadBarcodeFactsAsync(DbConnection,CancellationToken)</code><br>290–327 | CreateCommand @295; ConfigureAwait @305; ExecuteReaderAsync @305; ReadAsync @306; TryParse @308; GetString @308; Trim @310; TryGetValue @311; Contains @318; Add @320 | FROM barcodes @296 |
| <span id="m-dd5a508f8236"></span><code>SqliteCatalogReader.ReadGrossSoldQuantities30DaysAsync(DbConnection,DateTime,CancellationToken)</code><br>329–418 | AddDays @335; CreateCommand @337; CreateParameter @359; ToString @361; Add @362; ToString @366; ConfigureAwait @369; ExecuteReaderAsync @369; ReadAsync @370; TryParse @372; GetString @372; IsDBNull @378; TryParseInvariant @381; GetDouble @389; TryResolveQuantity @390; TryResolveFactor @397; TryRoundBaseQuantity @403; GetValueOrDefault @413 | FROM refund_lines @338; FROM sale_returns @338; FROM sales_lines @338; JOIN sales_invoices @338 · FormatException @383; FormatException @392; FormatException @399; InvalidOperationException @405 |
| <span id="m-78b3f67eba3c"></span><code>SqliteShiftReader.GetActiveShiftAsync(DbConnection,int,CancellationToken)</code><br>424–471 | Pow @431; CreateCommand @433; ConfigureAwait @445; ExecuteReaderAsync @445; ReadAsync @446; Parse @448; GetString @448; GetInt64 @451; Parse @453; GetInt32 @454 | FROM shifts @435; JOIN users @435 · InvalidOperationException @428 |

</details>

## SqliteReceiptReader.cs {#src-3df779d2480e}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteReceiptReader.cs</code> · 254 lines.

SHA-256: <code>61f8012e58f86495465ee171b417b4a52ed56c91edb3132b3166232051b06295</code>.

Declarations: <code>SqliteReceiptReader</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0faa0d042a18"></span><code>SqliteReceiptReader.GetReceiptsAsync(DbConnection,string?,int,string?,CancellationToken)</code><br>13–152 | CreateCommand @21; IsNullOrWhiteSpace @24; CreateParameter @27; Trim @29; Add @30; Trim @37; Clamp @85; ConfigureAwait @88; ExecuteReaderAsync @88; ReadAsync @89; GetString @91; Parse @93; IsDBNull @95; GetInt64 @96; Add @106; DisposeAsync @124; Add @137; ExecuteReaderAsync @139; ReadAsync @140; Parse @142; GetString @142; GetString @144; GetProperty @144; GetDateTime @145; TryGetProperty @145; GetString @145; GetInt64 @146; ToArray @151; Take @151; ThenBy @151; OrderByDescending @151 | FROM hardware_jobs @126 · DYNAMIC SQL: inspect manually |
| <span id="m-18fd42a74696"></span><code>SqliteReceiptReader.GetReceiptLinesAsync(DbConnection,string,CancellationToken)</code><br>154–209 | CreateCommand @160; Add @163; ConfigureAwait @164; ExecuteScalarAsync @164; Parse @166; EnumerateArray @167; GetProperty @167; Add @168; GetString @168; GetProperty @168; GetDecimal @168; GetInt64 @168; CreateParameter @179; Add @182; ExecuteReaderAsync @184; ReadAsync @185; GetString @187; IsDBNull @188; GetValue @192; TryParse @193; GetInt64 @201 | FROM hardware_jobs @162; FROM sales_lines @173 |
| <span id="m-2bc7c7c229fb"></span><code>SqliteReceiptReader.GetFinancialPreviewAsync(DbConnection,string,CancellationToken)</code><br>211–223 | CreateCommand @213; Add @215; ConfigureAwait @216; ExecuteReaderAsync @216; ReadAsync @217; GetString @218; DisposeAsync @219; nameof @220; BuildAsync @221; ToArray @222; Concat @222; Concat @222; Select @222 | FROM hardware_jobs @214 · ArgumentException @220 |
| <span id="m-1453b9838d69"></span><code>SqliteReceiptReader.GetFinancialPreviewImagesAsync(DbConnection,string,CancellationToken)</code><br>225–248 | CreateCommand @227; Add @229; ConfigureAwait @230; ExecuteReaderAsync @230; ReadAsync @231; GetString @232; DisposeAsync @233; nameof @234; BuildAsync @235; Parse @236; TryGetProperty @239; GetString @239; TryReadGeometry @240; RenderPreviewPngPages @243; TryGetInt32 @245; ToArray @246; Concat @246; Concat @246; SelectMany @246; RenderPreviewPng @247 | FROM hardware_jobs @228 · ArgumentException @234 |
| <span id="m-ed500da74424"></span><code>SqliteReceiptReader.Add(DbCommand,string,object)</code><br>250–253 | CreateParameter @252; Add @252 | No extracted literal effects. |

</details>

## SqliteRestaurantOrderReader.cs {#src-5ba4b65621a5}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteRestaurantOrderReader.cs</code> · 269 lines.

SHA-256: <code>86e3f9cb455ce2ef5b2f59d215a122c15111cf539db884a85a5aa1f98d53eac9</code>.

Declarations: <code>SqliteRestaurantOrderReader</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f089febab3b6"></span><code>SqliteRestaurantOrderReader.GetActiveOrdersAsync(DbConnection,ISessionContext,Guid?,CancellationToken)</code><br>14–113 | ValidatePermission @20; CreateCommand @24; CreateParameter @52; ToString @54; Add @55; ConfigureAwait @57; ExecuteReaderAsync @57; ReadAsync @60; Parse @62; GetString @62; IsDBNull @67; GetInt32 @71; GetInt64 @72; Parse @79; Add @82; LoadOrderLinesAsync @108; Add @109 | FROM restaurant_orders @25; JOIN users @25 |
| <span id="m-42fced0f46f1"></span><code>SqliteRestaurantOrderReader.GetOrderByIdAsync(DbConnection,ISessionContext,Guid,CancellationToken)</code><br>115–204 | ValidatePermission @121; CreateCommand @123; CreateParameter @149; ToString @151; Add @152; ConfigureAwait @154; ExecuteReaderAsync @154; ReadAsync @155; Parse @160; GetString @160; IsDBNull @165; GetInt32 @169; GetInt64 @170; Parse @177; LoadOrderLinesAsync @180 | FROM restaurant_orders @124; JOIN users @124 |
| <span id="m-96ac9b561950"></span><code>SqliteRestaurantOrderReader.LoadOrderLinesAsync(DbConnection,Guid,CancellationToken)</code><br>206–251 | CreateCommand @213; CreateParameter @229; ToString @231; Add @232; ConfigureAwait @234; ExecuteReaderAsync @234; ReadAsync @235; Add @237; Parse @238; GetString @238; GetInt32 @240; GetDecimal @243; GetInt64 @244; IsDBNull @246 | FROM restaurant_order_lines @214 |
| <span id="m-8d7cb5b36e5f"></span><code>SqliteRestaurantOrderReader.ValidatePermission(ISessionContext)</code><br>253–268 | HasPermission @260 | UnauthorizedAccessException @257; UnauthorizedAccessException @266 |

</details>

## SqliteSalaryReader.cs {#src-387c4517a73a}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteSalaryReader.cs</code> · 1,328 lines.

SHA-256: <code>0f8f55f8c8154824629dc9d489c6a60e3f9acb38871a0453acf4ce71a56db141</code>.

Declarations: <code>SqliteSalaryReader : ISalaryReader</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (16)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ea8848bceb99"></span><code>SqliteSalaryReader.GetConnectionAsync(string,CancellationToken)</code><br>30–68 | ConfigureAwait @47; OpenAsync @47; HasPermissionAsync @53; DisposeAsync @64 | UnauthorizedAccessException @34; UnauthorizedAccessException @56; rethrow @66 |
| <span id="m-e5c37e5f5ee5"></span><code>SqliteSalaryReader.AddParam(DbCommand,string,object?)</code><br>70–76 | CreateParameter @72; Add @75 | No extracted literal effects. |
| <span id="m-bda71def23cd"></span><code>SqliteSalaryReader.GetPeopleAsync(PageRequest,string,bool?,CancellationToken)</code><br>78–166 | ConfigureAwait @84; GetConnectionAsync @84; Trim @87; CreateCommand @90; AddParam @97; ToInt32 @100; ExecuteScalarAsync @100; IsNullOrWhiteSpace @104; ToLowerInvariant @107; ExecuteReaderAsync @149; ReadAsync @151; Add @153; MapPersonSummary @153; DisposeAsync @163 | FROM person_records @91; JOIN users @91 · DYNAMIC SQL: inspect manually |
| <span id="m-148756915426"></span><code>SqliteSalaryReader.GetPersonAsync(Guid,CancellationToken)</code><br>168–213 | ConfigureAwait @172; GetConnectionAsync @172; CreateCommand @175; AddParam @196; ToString @196; ExecuteReaderAsync @198; ReadAsync @199; MapPersonSummary @201; DisposeAsync @210 | FROM person_records @176; FROM salary_agreements @176; JOIN users @176 |
| <span id="m-410866d40046"></span><code>SqliteSalaryReader.GetAgreementsAsync(Guid,CancellationToken)</code><br>215–260 | ConfigureAwait @219; GetConnectionAsync @219; CreateCommand @222; AddParam @229; ToString @229; ExecuteReaderAsync @232; ReadAsync @234; Add @236; Parse @237; GetString @237; GetInt64 @240; IsDBNull @241; GetInt32 @243; Parse @245; DisposeAsync @257 | FROM salary_agreements @223 |
| <span id="m-22404b6ea7bb"></span><code>SqliteSalaryReader.GetMonthlyPayrollAsync(string,PageRequest,string,bool?,CancellationToken)</code><br>262–333 | ConfigureAwait @269; GetConnectionAsync @269; Trim @272; CreateCommand @275; AddParam @299; ExecuteReaderAsync @305; ReadAsync @307; Add @309; MapPersonSummary @309; ProjectSalaryMonthAsync @316; Add @317; ApplySalaryMonthSorting @320; ToList @322; Take @322; Skip @322; DisposeAsync @330 | FROM person_records @276; FROM salary_agreements @276; JOIN users @276 |
| <span id="m-98e5d171580f"></span><code>SqliteSalaryReader.GetMonthlyPayrollSummariesAsync(string,CancellationToken)</code><br>335–407 | ConfigureAwait @339; GetConnectionAsync @339; CreateCommand @342; AddParam @364; ExecuteReaderAsync @367; ReadAsync @369; Add @371; MapPersonSummary @371; ProjectSalaryMonthAsync @378; Add @379; GroupBy @382; Add @387; Sum @390; DisposeAsync @404 | FROM person_records @343; FROM salary_agreements @343; JOIN users @343 |
| <span id="m-f989ac1e5109"></span><code>SqliteSalaryReader.ApplySalaryMonthSorting(List&lt;SalaryMonthRow&gt;,string?,SortDirection)</code><br>409–446 | IsNullOrWhiteSpace @414; ToLowerInvariant @420; ToList @422; ThenBy @422; OrderBy @422; OrderByDescending @423; ThenByDescending @431 | No extracted literal effects. |
| <span id="m-ffb89672a3e5"></span><code>SqliteSalaryReader.GetPersonPayrollDetailAsync(Guid,string,CancellationToken)</code><br>448–559 | ConfigureAwait @453; GetConnectionAsync @453; GetPersonAsync @456; ProjectSalaryMonthAsync @459; GetAgreementsAsync @460; CreateCommand @464; AddParam @474; ToString @474; ExecuteReaderAsync @476; ReadAsync @477; Add @479; Parse @480; GetString @480; GetInt64 @484; Parse @486; IsDBNull @489; GetStoreTimeZoneAsync @495; GetLocalMonthUtcBounds @496; ToString @497; ToString @498; ExecuteReaderAsync @517; Add @520; GetLedgerAsync @541; DisposeAsync @556 | FROM salary_adjustments @466; FROM salary_payments @504; JOIN money_accounts @504; JOIN users @466; JOIN users @504 |
| <span id="m-5c2fc75b60b0"></span><code>SqliteSalaryReader.GetLedgerAsync(Guid,PageRequest,CancellationToken)</code><br>561–633 | ConfigureAwait @566; GetConnectionAsync @566; CreateCommand @569; AddParam @571; ToString @571; ToInt32 @572; ExecuteScalarAsync @572; IsNullOrWhiteSpace @576; ToLowerInvariant @579; ExecuteReaderAsync @604; ReadAsync @606; Add @608; Parse @609; GetString @609; GetInt64 @612; IsDBNull @617; Parse @619; DisposeAsync @630 | FROM salary_ledger_entries @570 · DYNAMIC SQL: inspect manually |
| <span id="m-b0de8647f1aa"></span><code>SqliteSalaryReader.MapPersonSummary(DbDataReader)</code><br>635–655 | Parse @638; GetString @638; ParseExact @642; IsDBNull @643; GetInt32 @645; GetInt64 @648; Parse @653 | No extracted literal effects. |
| <span id="m-e6e93daa63d5"></span><code>SqliteSalaryReader.ProjectSalaryMonthAsync(SqliteConnection,PersonSummaryRow,string,CancellationToken)</code><br>657–1029 | Parse @663; DaysInMonth @665; ConfigureAwait @667; GetStoreTimeZoneAsync @667; GetLocalMonthUtcBounds @668; ToString @669; ToString @670; CreateCommand @673; AddParam @679; ToString @679; ExecuteReaderAsync @683; ReadAsync @685; GetString @687; GetInt32 @688; Equals @690; Parse @692; IsDBNull @694; IsNullOrWhiteSpace @699; Deserialize(SalaryStatementSnapshot) @701; Deserialize(SalaryProrationResult) @710; CloseAsync @712; ReadAsync @714; ExecuteScalarAsync @730; Max @732; ReadPaymentsAsync @735; CalculateRemainingBalance @737; ExecuteReaderAsync @798; ReadAsync @799; GetInt32 @801; GetInt64 @802; IsDBNull @803; GetString @804; ExecuteReaderAsync @822; ReadAsync @823; GetString @825; GetInt64 @826; IsNullOrEmpty @834; CompareOrdinal @835; CalculateProration @843; ExecuteReaderAsync @910; ReadAsync @911; Add @913; GetString @913; ToString @924; Contains @925; CalculateDraftMonthEarningsAsync @928; AddMonths @931; ExecuteReaderAsync @955; ReadAsync @956; GetString @958; GetInt64 @959; CalculateForecast @980 | FROM salary_adjustments @816; FROM salary_agreements @790; FROM salary_ledger_entries @723; FROM salary_ledger_entries @947; FROM salary_periods @674; FROM salary_periods @904 |
| <span id="m-440c757bb132"></span><code>SqliteSalaryReader.CalculateDraftMonthEarningsAsync(SqliteConnection,PersonSummaryRow,string,CancellationToken)</code><br>1031–1117 | Parse @1037; CreateCommand @1042; AddParam @1050; ToString @1050; ConfigureAwait @1052; ExecuteReaderAsync @1052; ReadAsync @1053; GetInt32 @1055; GetInt64 @1056; IsDBNull @1057; ExecuteReaderAsync @1073; ReadAsync @1074; GetString @1076; GetInt64 @1077; Equals @1078; ExecuteScalarAsync @1092; ToInt32 @1095; CalculateProration @1101; DaysInMonth @1113; Max @1115 | FROM salary_adjustments @1067; FROM salary_agreements @1044; FROM salary_periods @1086 |
| <span id="m-8303f1e863f1"></span><code>SqliteSalaryReader.ReadPaymentsAsync(SqliteConnection,Guid,string,string,CancellationToken)</code><br>1119–1193 | CreateCommand @1126; AddParam @1138; ToString @1138; ConfigureAwait @1148; ExecuteReaderAsync @1148; ReadAsync @1149; GetString @1151; GetInt64 @1152; IsDBNull @1153; Equals @1156; IsNullOrEmpty @1166; CompareOrdinal @1167; Max @1188 | FROM salary_payments @1127; JOIN salary_payments @1127 |
| <span id="m-37884a35289d"></span><code>SqliteSalaryReader.GetSalaryStatementAsync(Guid,string,CancellationToken)</code><br>1195–1294 | ConfigureAwait @1200; GetConnectionAsync @1200; CreateCommand @1203; AddParam @1209; ToString @1209; ExecuteReaderAsync @1211; ReadAsync @1212; GetString @1216; Equals @1217; IsDBNull @1223; Deserialize(SalaryStatementSnapshot) @1226; Deserialize(SalaryProrationResult) @1234; Parse @1237; Parse @1238; GetInt32 @1241; Round @1269; Max @1280; Empty(SalaryStatementAdjustmentItem) @1283; Empty(SalaryStatementPaymentItem) @1284; DisposeAsync @1292 | FROM salary_periods @1204 |
| <span id="m-96893b9459b2"></span><code>SqliteSalaryReader.GetEarliestPayrollMonthAsync(CancellationToken)</code><br>1296–1327 | ConfigureAwait @1298; GetConnectionAsync @1298; CreateCommand @1301; ExecuteScalarAsync @1314; ToString @1316; Trim @1316; IsNullOrWhiteSpace @1317; IsMatch @1317; DisposeAsync @1325 | FROM person_records @1302; FROM salary_adjustments @1302; FROM salary_agreements @1302; FROM salary_ledger_entries @1302; FROM salary_periods @1302 |

</details>

## SqliteSearchPatternHelper.cs {#src-ad5991ea7b6f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteSearchPatternHelper.cs</code> · 25 lines.

SHA-256: <code>157a550f82b716d112642f133bd384226cb0325058032b412e38a28aef09407f</code>.

Declarations: <code>SqliteSearchPatternHelper</code> (line 3).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0b2c5782f126"></span><code>SqliteSearchPatternHelper.NormalizeQuery(string?)</code><br>8–9 | Trim @9 | No extracted literal effects. |
| <span id="m-be4b17009f8e"></span><code>SqliteSearchPatternHelper.EscapeLikePattern(string)</code><br>11–18 | IsNullOrEmpty @13; Replace @14; Replace @14 | No extracted literal effects. |
| <span id="m-e6367d4db1b6"></span><code>SqliteSearchPatternHelper.ToPrefixPattern(string)</code><br>20–21 | EscapeLikePattern @21 | No extracted literal effects. |
| <span id="m-6b9f817312c7"></span><code>SqliteSearchPatternHelper.ToSubstringPattern(string)</code><br>23–24 | EscapeLikePattern @24 | No extracted literal effects. |

</details>

## SqliteSearchSuggestionReader.cs {#src-ce74d33c68f5}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteSearchSuggestionReader.cs</code> · 1,459 lines.

SHA-256: <code>3e6ada72da0d785270f7da8beab41ac27acf43aa9ce934cf915fd52fabeb7a12</code>.

Declarations: <code>SqliteSearchSuggestionReader : ISearchSuggestionReader</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ebe63abd96c3"></span><code>SqliteSearchSuggestionReader.CheckPermissionAsync(SqliteConnection,string,CancellationToken)</code><br>26–60 | HasPermission @32; CreateCommand @35; CreateParameter @37; ToString @39; Add @40; ConfigureAwait @42; ExecuteScalarAsync @42; ToInt32 @46; ResolveEffectivePermissionsAsync @52; Contains @53; Contains @54; Contains @55 | FROM users @36 |
| <span id="m-eb0e7d1137bd"></span><code>SqliteSearchSuggestionReader.GetSuggestionsAsync(SearchRequest,CancellationToken)</code><br>62–272 | ThrowIfNull @66; ConfigureAwait @82; OpenAsync @82; CheckPermissionAsync @84; Equals @106; Equals @121; GetType @131; Equals @152; ClampLimit @236; GetItemSuggestionsAsync @246; GetThirdPartySuggestionsAsync @250; GetRecipeSuggestionsAsync @252; GetProductionRunSuggestionsAsync @254; GetCommercialInvoiceSuggestionsAsync @256; GetShipmentSuggestionsAsync @258; GetMoneySuggestionsAsync @261; GetReceiptSuggestionsAsync @264; GetSalaryPeopleSuggestionsAsync @266; GetExpenseSuggestionsAsync @268 | UnauthorizedAccessException @72; UnauthorizedAccessException @77; UnauthorizedAccessException @94; UnauthorizedAccessException @102; UnauthorizedAccessException @109; UnauthorizedAccessException @117; UnauthorizedAccessException @124; ArgumentException @131; UnauthorizedAccessException @137; UnauthorizedAccessException @147; UnauthorizedAccessException @156; UnauthorizedAccessException @163; ArgumentException @169; UnauthorizedAccessException @175; UnauthorizedAccessException @185; UnauthorizedAccessException @193; UnauthorizedAccessException @200; UnauthorizedAccessException @207; ArgumentException @214; UnauthorizedAccessException @219; ArgumentException @226; UnauthorizedAccessException @231 |
| <span id="m-2a05b3877415"></span><code>SqliteSearchSuggestionReader.GetItemSuggestionsAsync(SqliteConnection,SearchRequest,int,CancellationToken)</code><br>274–393 | CreateCommand @280; Add @286; IsNullOrWhiteSpace @316; Equals @316; AddParam @319; ToString @327; NormalizeQuery @330; IsNullOrEmpty @333; ToPrefixPattern @353; ToSubstringPattern @354; Join @373; ConfigureAwait @383; ExecuteReaderAsync @383; ReadAsync @384; Parse @386; GetString @386; Add @389; FromGuid @389 | FROM barcodes @346; FROM barcodes @356; FROM item_kits @292; FROM item_kits @298; FROM item_kits @304; FROM item_kits @315 · DYNAMIC SQL: inspect manually |
| <span id="m-1fc13acaf3c0"></span><code>SqliteSearchSuggestionReader.GetThirdPartySuggestionsAsync(SqliteConnection,SearchRequest,int,CancellationToken)</code><br>395–510 | CreateCommand @401; Add @406; IsNullOrWhiteSpace @425; Equals @425; ToLowerInvariant @427; AddParam @434; ToString @442; NormalizeQuery @445; IsNullOrEmpty @448; ToPrefixPattern @470; ToSubstringPattern @471; Join @490; ConfigureAwait @500; ExecuteReaderAsync @500; ReadAsync @501; Parse @503; GetString @503; Add @506; FromGuid @506 | DYNAMIC SQL: inspect manually |
| <span id="m-dce30a902847"></span><code>SqliteSearchSuggestionReader.GetRecipeSuggestionsAsync(SqliteConnection,SearchRequest,int,CancellationToken)</code><br>512–604 | CreateCommand @518; Add @525; AddParam @526; ToString @526; ToString @531; ToString @535; NormalizeQuery @538; IsNullOrEmpty @541; ToPrefixPattern @562; ToSubstringPattern @563; Join @583; ConfigureAwait @594; ExecuteReaderAsync @594; ReadAsync @595; Parse @597; GetString @597; Add @600; FromGuid @600 | FROM bom_items @530; FROM bom_items @554; FROM bom_items @565; JOIN items @554; JOIN items @565 · DYNAMIC SQL: inspect manually |
| <span id="m-f56c4255c5d2"></span><code>SqliteSearchSuggestionReader.GetProductionRunSuggestionsAsync(SqliteConnection,SearchRequest,int,CancellationToken)</code><br>606–711 | CreateCommand @612; Add @619; IsNullOrWhiteSpace @621; Equals @621; AddParam @624; ToString @634; ToString @642; NormalizeQuery @645; IsNullOrEmpty @648; ToPrefixPattern @668; ToSubstringPattern @669; Join @688; ConfigureAwait @700; ExecuteReaderAsync @700; ReadAsync @701; Parse @703; GetString @703; Add @707; FromGuid @707 | DYNAMIC SQL: inspect manually |
| <span id="m-9f5ba9dc23b3"></span><code>SqliteSearchSuggestionReader.GetCommercialInvoiceSuggestionsAsync(SqliteConnection,SearchRequest,int,bool,CancellationToken)</code><br>713–819 | CreateCommand @720; IsNullOrWhiteSpace @731; AddParam @739; ToString @739; ToString @741; ToString @741; BuildConditions @749; NormalizeQuery @751; IsNullOrEmpty @754; Add @767; ToPrefixPattern @773; ToSubstringPattern @774; Join @793; ConfigureAwait @804; ExecuteReaderAsync @804; ReadAsync @805; Parse @807; GetString @807; Add @815; FromGuid @815 | DYNAMIC SQL: inspect manually |
| <span id="m-6005632c21e7"></span><code>SqliteSearchSuggestionReader.GetShipmentSuggestionsAsync(SqliteConnection,SearchRequest,int,bool,CancellationToken)</code><br>821–926 | CreateCommand @828; Add @833; Equals @838; Equals @843; AddParam @849; ToString @849; NormalizeQuery @852; IsNullOrEmpty @855; ToPrefixPattern @876; ToSubstringPattern @877; Join @896; ConfigureAwait @913; ExecuteReaderAsync @913; ReadAsync @914; Parse @916; GetString @916; Add @922; FromGuid @922 | DYNAMIC SQL: inspect manually |
| <span id="m-884d310ecd7b"></span><code>SqliteSearchSuggestionReader.GetMoneySuggestionsAsync(SqliteConnection,SearchRequest,int,CancellationToken)</code><br>928–1156 | CreateCommand @934; IsNullOrWhiteSpace @939; Equals @939; Add @941; AddParam @942; ToString @955; NormalizeQuery @958; IsNullOrEmpty @961; ToPrefixPattern @981; ToSubstringPattern @982; Join @1001; ConfigureAwait @1024; ExecuteReaderAsync @1024; ReadAsync @1025; GetString @1027; Add @1035; Add @1047; ToString @1048; Equals @1050; CheckPermissionAsync @1118; ReadAsync @1143; Parse @1145; GetString @1145; Add @1152; FromGuid @1152 | DYNAMIC SQL: inspect manually |
| <span id="m-cc38887a0fff"></span><code>SqliteSearchSuggestionReader.GetSalaryPeopleSuggestionsAsync(SqliteConnection,SearchRequest,int,CancellationToken)</code><br>1158–1238 | CreateCommand @1165; Add @1170; AddParam @1173; ToString @1173; NormalizeQuery @1176; IsNullOrEmpty @1179; ToPrefixPattern @1198; ToSubstringPattern @1199; Join @1216; ConfigureAwait @1226; ExecuteReaderAsync @1226; ReadAsync @1227; Parse @1229; GetString @1229; Add @1234; FromGuid @1234 | DYNAMIC SQL: inspect manually |
| <span id="m-708c73f37ba2"></span><code>SqliteSearchSuggestionReader.GetExpenseSuggestionsAsync(SqliteConnection,SearchRequest,int,CancellationToken)</code><br>1240–1353 | CreateCommand @1247; Add @1252; AddParam @1253; ToString @1253; ToLowerInvariant @1256; Trim @1256; ToString @1274; NormalizeQuery @1277; IsNullOrEmpty @1280; ToPrefixPattern @1300; ToSubstringPattern @1301; Join @1318; ConfigureAwait @1340; ExecuteReaderAsync @1340; ReadAsync @1341; Parse @1343; GetString @1343; Add @1349; FromGuid @1349 | DYNAMIC SQL: inspect manually |
| <span id="m-8aeed350c505"></span><code>SqliteSearchSuggestionReader.GetReceiptSuggestionsAsync(SqliteConnection,SearchRequest,int,CancellationToken)</code><br>1355–1450 | CreateCommand @1361; AddParam @1364; ToString @1364; NormalizeQuery @1367; IsNullOrEmpty @1370; Add @1383; ToPrefixPattern @1391; ToSubstringPattern @1392; Join @1412; ConfigureAwait @1431; ExecuteReaderAsync @1431; ReadAsync @1432; GetString @1434; GetInt64 @1439; ToString @1443; Add @1446 | DYNAMIC SQL: inspect manually |
| <span id="m-f68ccdf815c2"></span><code>SqliteSearchSuggestionReader.AddParam(DbCommand,string,object?)</code><br>1452–1458 | CreateParameter @1454; Add @1457 | No extracted literal effects. |

</details>

## SqliteStaffReader.cs {#src-e48df4c9b3cc}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteStaffReader.cs</code> · 78 lines.

SHA-256: <code>6d51a51023026a14d17b8c0b1a6dfe2bd7b774deb23afebabc0812c78e09bffa</code>.

Declarations: <code>StaffMemberProjection</code> (line 6), <code>SqliteStaffReader</code> (line 18).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-56d932e6ec07"></span><code>SqliteStaffReader.GetStaffMembersAsync(DbConnection,ISessionContext?,CancellationToken)</code><br>20–77 | HasPermission @27; CreateCommand @35; ConfigureAwait @51; ExecuteReaderAsync @51; ReadAsync @52; Parse @54; GetString @54; GetInt32 @58; IsDBNull @59; Add @63; IsNullOrEmpty @69 | FROM shifts @36; FROM users @36; JOIN product_categories @36; JOIN user_roles @36 · UnauthorizedAccessException @29 |

</details>

## SqliteStockMovementHistoryReader.cs {#src-511aa38c5d1f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteStockMovementHistoryReader.cs</code> · 297 lines.

SHA-256: <code>8838723dc2037d66d441f8abf3901c1df98f75bcd8f180c5535f4764dff22980</code>.

Declarations: <code>SqliteStockMovementHistoryReader</code> (line 15), <code>RawMovement</code> (line 273).

<details markdown>
<summary>Methods, calls, table effects and failures (14)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d23e9f5ebc92"></span><code>SqliteStockMovementHistoryReader.GetTraceabilitySummaryAsync(DbConnection,ISessionContext,Guid,CancellationToken)</code><br>17–114 | ThrowIfNull @23; BeginTransaction @30; CreateCommand @33; Add @37; ToString @37; ToInt32 @38; ConfigureAwait @38; ExecuteScalarAsync @38; ExecuteReaderAsync @51; ReadAsync @53; TryParse @55; GetString @55; Add @57; Parse @57; Take @60; GetLotLocationBalanceAsync @62; Add @64; Add @79; GetInt32 @79; Add @108; CommitAsync @111; ToArray @113; Take @113 | FROM item_kit_components @86; FROM item_kit_components @97; FROM lots @36; FROM lots @43; FROM serials @72; JOIN item_kits @86; JOIN item_kits @97; JOIN items @97 · UnauthorizedAccessException @26; InvalidOperationException @28 |
| <span id="m-72d782464838"></span><code>SqliteStockMovementHistoryReader.GetItemStockHistoryAsync(DbConnection,ISessionContext,Guid,PageRequest,long?,CancellationToken)</code><br>116–167 | ThrowIfNull @124; Contains @131; Max @134; BeginTransaction @136; ConfigureAwait @137; ReadItemAsync @137; ReadSnapshotRowIdAsync @141; ReadCountAsync @147; Ceiling @148; Min @149; ReadPageAsync @151; GetPhysicalOnHandAsync @152; ReadNewerDeltaAsync @156; Add @161; ToProjection @161; CommitAsync @165 | UnauthorizedAccessException @127; InvalidOperationException @129; KeyNotFoundException @139 |
| <span id="m-21a69a45b8d0"></span><code>SqliteStockMovementHistoryReader.ReadItemAsync(SqliteConnection,SqliteTransaction,Guid,CancellationToken)</code><br>169–181 | CreateCommand @171; Add @177; ToString @177; ConfigureAwait @178; ExecuteReaderAsync @178; ReadAsync @179; GetString @180; GetInt32 @180 | FROM item_kits @173; FROM items @173 |
| <span id="m-65310fb0a21f"></span><code>SqliteStockMovementHistoryReader.ReadSnapshotRowIdAsync(SqliteConnection,SqliteTransaction,Guid,CancellationToken)</code><br>183–191 | CreateCommand @185; Add @188; ToString @188; ConfigureAwait @189; ExecuteScalarAsync @189; ToInt64 @190 | FROM stock_movements @187 |
| <span id="m-bab9c5aac25c"></span><code>SqliteStockMovementHistoryReader.ReadCountAsync(SqliteConnection,SqliteTransaction,Guid,long,CancellationToken)</code><br>193–201 | CreateCommand @195; Add @198; ToString @198; ToInt32 @200; ConfigureAwait @200; ExecuteScalarAsync @200 | FROM stock_movements @197 |
| <span id="m-8e0791918fa4"></span><code>SqliteStockMovementHistoryReader.ReadPageAsync(SqliteConnection,SqliteTransaction,Guid,long,int,int,CancellationToken)</code><br>203–228 | CreateCommand @205; Add @220; ToString @220; ConfigureAwait @225; ExecuteReaderAsync @225; ReadAsync @226; Add @226; From @226 | FROM stock_movements @207; JOIN lots @207; JOIN third_parties @207; JOIN users @207 |
| <span id="m-747a374e7119"></span><code>SqliteStockMovementHistoryReader.ReadNewerDeltaAsync(SqliteConnection,SqliteTransaction,Guid,long,RawMovement,CancellationToken)</code><br>230–251 | CreateCommand @232; Add @239; ToString @239; ToString @241; ToString @242; ConfigureAwait @244; ExecuteReaderAsync @244; ReadAsync @245; ResolveQuantity @247; ReadNullableString @247; IsDBNull @247; GetDouble @247; CalculatePhysicalDelta @248; GetString @248 | FROM stock_movements @234 |
| <span id="m-6a01f191c927"></span><code>SqliteStockMovementHistoryReader.CalculatePhysicalDelta(decimal,string,string)</code><br>253–259 | IsVirtualLocation @256 | No extracted literal effects. |
| <span id="m-9bc31593bece"></span><code>SqliteStockMovementHistoryReader.Add(DbCommand,string,object)</code><br>261–267 | CreateParameter @263; Add @266 | No extracted literal effects. |
| <span id="m-811c00156b03"></span><code>SqliteStockMovementHistoryReader.ReadNullableString(DbDataReader,int)</code><br>269–269 | IsDBNull @269; GetString @269 | No extracted literal effects. |
| <span id="m-07da9014b761"></span><code>SqliteStockMovementHistoryReader.ReadGuid(DbDataReader,int)</code><br>270–270 | IsDBNull @270; TryParse @270; GetString @270 | No extracted literal effects. |
| <span id="m-ce86685b2b6e"></span><code>SqliteStockMovementHistoryReader.ReadUtc(string)</code><br>271–271 | ToUniversalTime @271; Parse @271 | No extracted literal effects. |
| <span id="m-cd221d2e3b7d"></span><code>RawMovement.From(DbDataReader)</code><br>281–290 | ResolveQuantity @283; ReadNullableString @283; IsDBNull @283; GetDouble @283; ResolveFactor @285; Parse @286; GetString @286; ReadUtc @286; GetInt32 @286; ReadGuid @287 | No extracted literal effects. |
| <span id="m-61bc60e9df4d"></span><code>RawMovement.ToProjection(decimal)</code><br>292–295 | — | No extracted literal effects. |

</details>

## SqliteTeamsReader.cs {#src-4f7a8b1a0ccc}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteTeamsReader.cs</code> · 518 lines.

SHA-256: <code>55f219394193345b5413bbb353116db9e76a40bec482fdd17ba3f1dfe5bf8991</code>.

Declarations: <code>SqliteTeamsReader : ITeamsReader</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3e6239e56287"></span><code>SqliteTeamsReader.GetConnectionAndAuthorizeAsync(CancellationToken,bool)</code><br>28–78 | ConfigureAwait @47; OpenAsync @47; HasPermission @54; HasPermissionAsync @55; DisposeAsync @74 | UnauthorizedAccessException @34; UnauthorizedAccessException @61; UnauthorizedAccessException @65; rethrow @76 |
| <span id="m-31c3637b6019"></span><code>SqliteTeamsReader.GetTeamMembersAsync(PageRequest,string,bool?,CancellationToken)</code><br>80–236 | ConfigureAwait @86; GetConnectionAndAuthorizeAsync @86; ToString @90; CreateCommand @93; CreateParameter @131; Add @134; ExecuteReaderAsync @136; ReadAsync @137; Add @139; ReadPersonRow @139; ExecuteReaderAsync @158; Parse @161; GetString @161; GetInt32 @164; IsDBNull @165; IsNullOrWhiteSpace @198; Trim @200; Where @201; Contains @202; Contains @203; Contains @204; ToList @215; ThenBy @215; OrderBy @215; Max @221; ToList @224; Take @225; Skip @225; DisposeAsync @233 | FROM person_records @146; FROM person_records @95; FROM salary_agreements @95; FROM shifts @146; FROM shifts @95; FROM users @146; JOIN user_roles @146; JOIN user_roles @95; JOIN users @95 |
| <span id="m-a5d2b78c7ce0"></span><code>SqliteTeamsReader.GetTeamMemberDetailAsync(string,CancellationToken)</code><br>238–464 | IsNullOrWhiteSpace @242; ConfigureAwait @244; GetConnectionAndAuthorizeAsync @244; Trim @247; StartsWith @251; TryParse @253; AsSpan @253; ToString @260; CreateCommand @265; CreateParameter @302; ToString @304; Add @305; ExecuteReaderAsync @311; ReadAsync @312; ReadPersonRow @314; ToString @359; CreateParameter @386; Add @389; ExecuteReaderAsync @391; ReadAsync @392; Parse @394; GetString @394; GetInt32 @397; IsDBNull @398; CreateParameter @440; ToString @442; Add @443; ExecuteReaderAsync @445; ReadAsync @446; Add @448; GetString @449; GetInt32 @450; DisposeAsync @461 | FROM person_records @266; FROM person_records @321; FROM salary_agreements @266; FROM salary_agreements @321; FROM shifts @266; FROM shifts @321; FROM shifts @375; FROM user_permission_overrides @436; FROM users @375; JOIN user_roles @266; JOIN user_roles @321; JOIN user_roles @375; JOIN users @266; JOIN users @321 |
| <span id="m-e6fc3104145d"></span><code>SqliteTeamsReader.ReadPersonRow(DbDataReader,bool)</code><br>466–517 | Parse @468; GetString @468; ParseExact @472; IsDBNull @473; GetInt32 @475; GetInt64 @483 | No extracted literal effects. |

</details>

## SqliteTraceabilityCandidateReader.cs {#src-dc71bf3dc631}

<code>Software/src/GetSeek.Infrastructure/Persistence/Readers/SqliteTraceabilityCandidateReader.cs</code> · 128 lines.

SHA-256: <code>542866d0a468aac8f8f92301db356e7c0906f08c4d361fee2a2aa9c9739b4d70</code>.

Declarations: <code>SqliteTraceabilityCandidateReader</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4ed94b811aec"></span><code>SqliteTraceabilityCandidateReader.GetLotCandidatesAsync(DbConnection,Guid,string,ISessionContext,CancellationToken)</code><br>18–62 | EnsureCanReadTraceability @25; CreateCommand @27; Add @36; ToString @36; ToString @37; ConfigureAwait @38; ExecuteReaderAsync @38; ReadAsync @39; TryParse @41; GetString @41; TryParse @42; Add @44; GetLotLocationBalanceAsync @52; Add @57 | FROM lots @29 |
| <span id="m-96dfe00e3720"></span><code>SqliteTraceabilityCandidateReader.GetSerialCandidatesAsync(DbConnection,Guid,string,ISessionContext,CancellationToken)</code><br>64–105 | EnsureCanReadTraceability @71; CreateCommand @73; Add @82; ToString @82; Trim @83; ToString @84; ConfigureAwait @85; ExecuteReaderAsync @85; ReadAsync @86; IsDBNull @88; GetString @88; TryParse @89; TryParse @92; Add @99; Equals @102 | FROM serials @74; JOIN lots @74 |
| <span id="m-7b98a5de898a"></span><code>SqliteTraceabilityCandidateReader.EnsureCanReadTraceability(ISessionContext)</code><br>107–119 | HasPermission @111 | UnauthorizedAccessException @117 |
| <span id="m-744dce51c472"></span><code>SqliteTraceabilityCandidateReader.Add(DbCommand,string,object)</code><br>121–127 | CreateParameter @123; Add @126 | No extracted literal effects. |

</details>

## SqliteAuditJournalRepository.cs {#src-ad9047c13ed4}

<code>Software/src/GetSeek.Infrastructure/Persistence/Repositories/SqliteAuditJournalRepository.cs</code> · 135 lines.

SHA-256: <code>65a0b4c62bbcafa72dddabddf3075638bc827b8d948fb595bf445a1b1d463d19</code>.

Declarations: <code>SqliteAuditJournalRepository : IAuditJournalRepository</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a77cc242824c"></span><code>SqliteAuditJournalRepository.AppendAsync(string,string?,string,string,string?,string,CancellationToken)</code><br>12–100 | CreateCommand @28; ConfigureAwait @37; ExecuteReaderAsync @37; ReadAsync @38; GetInt64 @40; GetString @41; NewGuid @46; ComputeHash @49; AddWithValue @71; ToString @72; ToString @76; ExecuteNonQueryAsync @83 | FROM immutable_audit_journal @31; INSERT INTO immutable_audit_journal @65 |
| <span id="m-12424c6c01c2"></span><code>SqliteAuditJournalRepository.GetLatestEntryAsync(CancellationToken)</code><br>102–134 | CreateCommand @105; ConfigureAwait @114; ExecuteReaderAsync @114; ReadAsync @115; GetInt64 @119; Parse @120; GetString @120; IsDBNull @122; Parse @124 | FROM immutable_audit_journal @107 |

</details>

## SqliteHardwareJobRepository.cs {#src-c2d11040fda4}

<code>Software/src/GetSeek.Infrastructure/Persistence/Repositories/SqliteHardwareJobRepository.cs</code> · 98 lines.

SHA-256: <code>4f6940a0809d01177d7ee7058ea5ef2371f12e7f3c1c881b2fa73209765c896e</code>.

Declarations: <code>SqliteHardwareJobRepository : IHardwareJobRepository</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-81b299c07358"></span><code>SqliteHardwareJobRepository.EnqueueAsync(string,string,CancellationToken)</code><br>9–31 | ToString @14; NewGuid @14; CreateCommand @17; AddWithValue @23; ToString @26; ConfigureAwait @28; ExecuteNonQueryAsync @28 | INSERT INTO hardware_jobs @19 |
| <span id="m-312fba70c3ff"></span><code>SqliteHardwareJobRepository.GetPendingAsync(int,CancellationToken)</code><br>33–64 | CreateCommand @36; AddWithValue @45; ConfigureAwait @48; ExecuteReaderAsync @48; ReadAsync @49; Add @51; GetString @52; GetInt32 @56; Parse @57; IsDBNull @58 | FROM hardware_jobs @38 |
| <span id="m-dd0a98c73b80"></span><code>SqliteHardwareJobRepository.MarkCompletedAsync(string,CancellationToken)</code><br>66–80 | CreateCommand @69; AddWithValue @76; ToString @77; ConfigureAwait @79; ExecuteNonQueryAsync @79 | UPDATE hardware_jobs @71 |
| <span id="m-580677770c45"></span><code>SqliteHardwareJobRepository.MarkFailedAsync(string,string,CancellationToken)</code><br>82–97 | CreateCommand @85; AddWithValue @92; ToString @94; ConfigureAwait @96; ExecuteNonQueryAsync @96 | UPDATE hardware_jobs @87 |

</details>

## SqliteIdempotencyStore.cs {#src-0f474af1bb75}

<code>Software/src/GetSeek.Infrastructure/Persistence/Repositories/SqliteIdempotencyStore.cs</code> · 54 lines.

SHA-256: <code>8982d830eaa0a0d47d365d64d2c9767de9bbeb3627732d8bbf9ddca983a17d36</code>.

Declarations: <code>SqliteIdempotencyStore : IIdempotencyStore</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0b5e3908c056"></span><code>SqliteIdempotencyStore.CheckAsync(string,string,CancellationToken)</code><br>8–32 | CreateCommand @14; AddWithValue @21; ConfigureAwait @23; ExecuteReaderAsync @23; ReadAsync @24; GetString @26 | FROM command_deduplication @16 |
| <span id="m-c38c2c67aa51"></span><code>SqliteIdempotencyStore.SaveAsync(string,string,string,CancellationToken)</code><br>34–53 | CreateCommand @41; AddWithValue @47; ToString @50; ConfigureAwait @52; ExecuteNonQueryAsync @52 | INSERT INTO command_deduplication @43 |

</details>

## SqliteSearchUsageStore.cs {#src-9c5f82b4e823}

<code>Software/src/GetSeek.Infrastructure/Persistence/Repositories/SqliteSearchUsageStore.cs</code> · 174 lines.

SHA-256: <code>4f7dcfefe3adb3cf31ec5a84fa0a0e4de2e9aee43eec5334c2e210fc6b93daf3</code>.

Declarations: <code>SqliteSearchUsageStore : ISearchUsageWriter</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-8cf4412a8596"></span><code>SqliteSearchUsageStore.RecordUseAsync(SearchUseRequest,CancellationToken)</code><br>36–118 | ThrowIfNull @38; IsEligibleEntity @53; ToString @58; ConfigureAwait @63; OpenAsync @63; BeginTransaction @65; CreateCommand @68; AddParam @75; ToString @76; ExecuteNonQueryAsync @81; ExecuteNonQueryAsync @100; CommitAsync @103; LogFailure @115 | INSERT INTO search_usage @88; INSERT OR IGNORE INTO search_usage_events @71 · UnauthorizedAccessException @44; UnauthorizedAccessException @49; ArgumentException @55; rethrow @107; rethrow @111; rethrow @116 |
| <span id="m-57ed9e3c3aed"></span><code>SqliteSearchUsageStore.IsEligibleEntity(SearchContext,SearchEntityKey)</code><br>120–165 | IsNullOrWhiteSpace @122; TryParse @125; Equals @135 | No extracted literal effects. |
| <span id="m-a6675bbbefa7"></span><code>SqliteSearchUsageStore.AddParam(DbCommand,string,object)</code><br>167–173 | CreateParameter @169; Add @172 | No extracted literal effects. |

</details>

## SqliteRealWorkspaceResetService.cs {#src-fd68b42fd4fb}

<code>Software/src/GetSeek.Infrastructure/Persistence/Resetting/SqliteRealWorkspaceResetService.cs</code> · 494 lines.

SHA-256: <code>bcf6fb283c931557e6d1c33ff52582fd915d418368e038f9b0c0de2bce8a9fef</code>.

Declarations: <code>RealResetGroups</code> (line 12), <code>RealResetPreview</code> (line 27), <code>SqliteRealWorkspaceResetService</code> (line 37).

<details markdown>
<summary>Methods, calls, table effects and failures (21)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-446de89a8365"></span><code>SqliteRealWorkspaceResetService.PreviewAsync(DbConnection,CancellationToken)</code><br>76–103 | ConfigureAwait @78; EnsureOpenAsync @78; Concat @84; Distinct @85; TableExistsAsync @87; TableFingerprintAsync @88; Add @90; CountAsync @95; ToHexString @101; HashData @101; GetBytes @101; Join @101 | FROM hardware_jobs @96; FROM production_runs @97; FROM shifts @95 |
| <span id="m-9d63b9966474"></span><code>SqliteRealWorkspaceResetService.ExecuteAsync(DbConnection,Guid,string,RealResetGroups,string,string,string,CancellationToken)</code><br>105–183 | IsNullOrWhiteSpace @117; Trim @117; Equals @119; Trim @119; ConfigureAwait @122; EnsureOpenAsync @122; BeginTransactionAsync @123; RequireAuthorizedAdminAsync @126; ScalarStringAsync @127; PreviewInTransactionAsync @131; RequireDependenciesAsync @137; CreateCommand @138; ExecuteNonQueryAsync @142; Distinct @157; DeleteIfExistsAsync @158; ResetStoreConfigurationAsync @162; RestoreBuiltInCategoriesAsync @165; RestoreBuiltInExpenseCategoriesAsync @168; RebaseSalaryTrackingStartAsync @171; EnsureWalkInCustomerAsync @173; EnsureForeignKeysValidAsync @174; AppendAuditAsync @175; CommitAsync @176; RollbackAsync @180 | FROM workspace_classification @127 · InvalidOperationException @116; InvalidOperationException @118; InvalidOperationException @120; UnauthorizedAccessException @129; InvalidOperationException @133; InvalidOperationException @135; rethrow @181 |
| <span id="m-b05474ae35f9"></span><code>SqliteRealWorkspaceResetService.PreviewInTransactionAsync(DbConnection,DbTransaction,CancellationToken)</code><br>185–208 | Concat @192; Distinct @193; ConfigureAwait @195; TableExistsAsync @195; TableFingerprintAsync @196; Add @198; CountAsync @202; ToHexString @206; HashData @206; GetBytes @206; Join @206 | FROM hardware_jobs @203; FROM production_runs @204; FROM shifts @202 |
| <span id="m-a67ba90d2fee"></span><code>SqliteRealWorkspaceResetService.RequireDependenciesAsync(DbConnection,DbTransaction,RealResetGroups,RealResetPreview,CancellationToken)</code><br>210–279 | GetValueOrDefault @212; ConfigureAwait @232; TableExistsAsync @232; CountAsync @233 | FROM expense_payments @245; FROM expense_records @262; FROM production_runs @277; FROM salary_payments @233 · InvalidOperationException @219; InvalidOperationException @221; InvalidOperationException @223; InvalidOperationException @225; InvalidOperationException @227; InvalidOperationException @229; InvalidOperationException @238; InvalidOperationException @240; InvalidOperationException @250; InvalidOperationException @252; InvalidOperationException @258; InvalidOperationException @265; InvalidOperationException @271; InvalidOperationException @273; InvalidOperationException @278 |
| <span id="m-effd0eb40779"></span><code>SqliteRealWorkspaceResetService.ResetStoreConfigurationAsync(DbConnection,DbTransaction,Guid,CancellationToken)</code><br>281–301 | ToString @283; ConfigureAwait @284; ExecuteAsync @284; ToString @285 | DELETE FROM store_uom_preferences @289; FROM store_config @290; INSERT INTO store_uom_preferences @291; INSERT OR IGNORE INTO money_accounts @290; UPDATE business_profile_config @285; UPDATE manual_payment_display @286; UPDATE output_device_config @287; UPDATE price_level_settings @300; UPDATE store_config @284; UPDATE store_legal_identity @288 |
| <span id="m-41dfce6a1b8b"></span><code>SqliteRealWorkspaceResetService.EnsureWalkInCustomerAsync(DbConnection,DbTransaction,CancellationToken)</code><br>303–307 | ConfigureAwait @305; TableExistsAsync @305; ExecuteAsync @306; ToString @306 | INSERT OR IGNORE INTO third_parties @306 |
| <span id="m-2a03f61428ee"></span><code>SqliteRealWorkspaceResetService.RestoreBuiltInCategoriesAsync(DbConnection,DbTransaction,CancellationToken)</code><br>309–315 | ToString @311; ConfigureAwait @313; ExecuteAsync @313 | INSERT OR IGNORE INTO product_categories @313 |
| <span id="m-fe8a62fd8a86"></span><code>SqliteRealWorkspaceResetService.RestoreBuiltInExpenseCategoriesAsync(DbConnection,DbTransaction,CancellationToken)</code><br>317–337 | ToString @319; ConfigureAwait @332; ExecuteAsync @332 | INSERT OR IGNORE INTO expense_categories @332 |
| <span id="m-b49041c1c143"></span><code>SqliteRealWorkspaceResetService.RebaseSalaryTrackingStartAsync(DbConnection,DbTransaction,CancellationToken)</code><br>339–352 | ToString @341; ConfigureAwait @342; GetStoreTimeZoneAsync @342; GetStoreLocalMonth @343; ExecuteAsync @344 | UPDATE person_records @344 |
| <span id="m-3b5c4dbd8f80"></span><code>SqliteRealWorkspaceResetService.RequireAuthorizedAdminAsync(DbConnection,DbTransaction,Guid,string,CancellationToken)</code><br>354–369 | CreateCommand @356; Add @358; ToString @358; ConfigureAwait @359; ExecuteReaderAsync @359; ReadAsync @360; GetInt32 @360; IsDBNull @362; GetString @362; All @363; VerifyPin @363; DisposeAsync @365; HasPermissionAsync @366 | FROM user_roles @357; FROM users @357 · UnauthorizedAccessException @361; UnauthorizedAccessException @364; UnauthorizedAccessException @368 |
| <span id="m-f376ae24264f"></span><code>SqliteRealWorkspaceResetService.HasPermissionAsync(DbConnection,DbTransaction,Guid,string,CancellationToken)</code><br>371–382 | CreateCommand @373; Add @375; ToString @375; ConfigureAwait @376; ExecuteScalarAsync @376; ToInt32 @377; ExecuteScalarAsync @381 | FROM user_permission_overrides @374; FROM user_roles @379; JOIN role_permissions @379 |
| <span id="m-3f9a12b5b3b0"></span><code>SqliteRealWorkspaceResetService.AppendAuditAsync(DbConnection,DbTransaction,Guid,string,RealResetGroups,CancellationToken)</code><br>384–401 | CreateCommand @387; ConfigureAwait @390; ExecuteReaderAsync @390; ReadAsync @391; GetInt64 @391; GetString @391; NewGuid @394; ToString @394; Serialize @395; ToArray(RealResetGroups) @395; Select(RealResetGroups) @395; Where(RealResetGroups) @395; GetValues(RealResetGroups) @395; ToString @395; ComputeHash @396; Add @399; ToString @399; ToString @399; ExecuteNonQueryAsync @400 | FROM immutable_audit_journal @389; INSERT INTO immutable_audit_journal @398 |
| <span id="m-537b7fd68aaa"></span><code>SqliteRealWorkspaceResetService.EnsureForeignKeysValidAsync(DbConnection,DbTransaction,CancellationToken)</code><br>403–408 | CreateCommand @405; ConfigureAwait @406; ExecuteReaderAsync @406; ReadAsync @407 | InvalidOperationException @407 |
| <span id="m-bad8cdb8f868"></span><code>SqliteRealWorkspaceResetService.DeleteIfExistsAsync(DbConnection,DbTransaction,string,CancellationToken)</code><br>410–416 | ConfigureAwait @412; TableExistsAsync @412; ExecuteAsync @413 | DYNAMIC SQL: inspect manually |
| <span id="m-c287a02d03d1"></span><code>SqliteRealWorkspaceResetService.TableFingerprintAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>418–457 | CreateCommand @421; ConfigureAwait @424; ExecuteReaderAsync @424; ReadAsync @425; GetInt32 @427; GetString @428; ToArray @431; Join @432; Select @432; Replace @432; CreateHash @434; ExecuteReaderAsync @436; ReadAsync @437; IsDBNull @442; AppendData @444; GetValue @447; GetBytes @450; GetType @450; ToString @450; GetBytes @452; ToHexString @456; GetHashAndReset @456 | DYNAMIC SQL: inspect manually |
| <span id="m-397c8398c0b3"></span><code>SqliteRealWorkspaceResetService.TableExistsAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>459–463 | CreateCommand @461; Add @461; ConfigureAwait @462; ExecuteScalarAsync @462 | No extracted literal effects. |
| <span id="m-a471c22b170e"></span><code>SqliteRealWorkspaceResetService.CountAsync(DbConnection,DbTransaction?,string,CancellationToken)</code><br>465–469 | CreateCommand @467; ToInt64 @468; ConfigureAwait @468; ExecuteScalarAsync @468 | No extracted literal effects. |
| <span id="m-d120a8b51713"></span><code>SqliteRealWorkspaceResetService.ScalarStringAsync(DbConnection,DbTransaction,string,CancellationToken)</code><br>471–475 | CreateCommand @473; ConfigureAwait @474; ExecuteScalarAsync @474; ToString @474 | No extracted literal effects. |
| <span id="m-5112312b4807"></span><code>SqliteRealWorkspaceResetService.ExecuteAsync(DbConnection,DbTransaction,string,CancellationToken,(string Name, object Value)[])</code><br>477–482 | CreateCommand @479; Add @480; ConfigureAwait @481; ExecuteNonQueryAsync @481 | No extracted literal effects. |
| <span id="m-1aaabc513fec"></span><code>SqliteRealWorkspaceResetService.Add(DbCommand,string,object)</code><br>484–487 | CreateParameter @486; Add @486 | No extracted literal effects. |
| <span id="m-ded36f3d1298"></span><code>SqliteRealWorkspaceResetService.EnsureOpenAsync(DbConnection,CancellationToken)</code><br>489–492 | ConfigureAwait @491; OpenAsync @491 | No extracted literal effects. |

</details>

## SqliteDemoDataSeeder.cs {#src-b064594c8984}

<code>Software/src/GetSeek.Infrastructure/Persistence/Seeding/SqliteDemoDataSeeder.cs</code> · 1,287 lines.

SHA-256: <code>5129aad0bd490c93b34fc960b32c68df3585db00e34247b4cddd33b98d0b3546</code>.

Declarations: <code>DemoSeededUser</code> (line 10), <code>DemoDatasetLoadResult</code> (line 12), <code>SqliteDemoDataSeeder</code> (line 22).

<details markdown>
<summary>Methods, calls, table effects and failures (20)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0303862821ff"></span><code>SqliteDemoDataSeeder.SeedLargeScaleDemoDataAsync(DbConnection,Guid,IProgress&lt;string&gt;?,CancellationToken)</code><br>68–75 | ConfigureAwait @74; EnsureInitialDatasetAsync @74 | No extracted literal effects. |
| <span id="m-9e9733ac9ff5"></span><code>SqliteDemoDataSeeder.EnsureInitialDatasetAsync(DbConnection,Guid,IProgress&lt;string&gt;?,CancellationToken)</code><br>77–124 | ConfigureAwait @84; OpenAsync @84; BeginTransactionAsync @86; RequireDisposableDemoWorkspaceAsync @89; RequireActiveAdminAsync @90; HasEffectivePermissionAsync @91; ReadDatasetStateAsync @94; Equals @95; CountRowsAsync @97; CommitAsync @98; HasBusinessDataAsync @107; SetDatasetStateAsync @109; SeedLargeScaleDemoDataCoreAsync @114; RollbackAsync @121 | UnauthorizedAccessException @92; rethrow @122 |
| <span id="m-01eb18d64854"></span><code>SqliteDemoDataSeeder.SeedLargeScaleDemoDataCoreAsync(DbConnection,Guid,IProgress&lt;string&gt;?,DbTransaction?,CancellationToken)</code><br>126–859 | ConfigureAwait @135; OpenAsync @135; Report @138; BeginTransactionAsync @144; ToString @154; RequireDisposableDemoWorkspaceAsync @157; RequireActiveAdminAsync @161; CreateCommand @164; ToInt64 @168; ExecuteScalarAsync @168; ExecuteScalarAsync @179; ExecuteScalarAsync @191; ExecuteScalarAsync @202; ExecuteScalarAsync @213; ExecuteScalarAsync @224; TableExistsAsync @233; ExecuteScalarAsync @237; ExecuteScalarAsync @245; ExecuteScalarAsync @255; ToString @258; ToString @262; NewGuid @262; AddParam @270; ExecuteNonQueryAsync @272; Add @283; ToString @289; ToUpperInvariant @290; ExecuteNonQueryAsync @293; AppendLine @305; Min @307; Add @312; Append @318; ToString @324; AppendLine @333; Append @340; ToString @345; ExecuteNonQueryAsync @346; AppendLine @360; AppendLine @361; AppendLine @362; Add @371; Round @376; NextDouble @376; ToString @377; Append @387; Append @388; Append @389; ToString @395; ToString @396; ToString @397; AppendLine @410; Add @419; Append @434; ToString @442; Add @457; ToString @463; AppendLine @489; AppendLine @490; AppendLine @491; Append @505; Append @506; Append @518; ToString @525; ToString @526; ToString @527; AppendLine @534; Append @543; ToString @549; AppendLine @558; Append @567; ToString @573; ToString @589; ToString @590; ExecuteNonQueryAsync @592; Add @604; ToString @610; ToString @612; ExecuteNonQueryAsync @614; ToInt64 @619; Round @619; Sum @620; ToString @629; ExecuteNonQueryAsync @634; ToString @644; ExecuteNonQueryAsync @649; ExecuteNonQueryAsync @666; ToString @681; ToString @682; ToString @684; ExecuteNonQueryAsync @691; ToString @703; ExecuteNonQueryAsync @711; ExecuteReaderAsync @736; ReadAsync @737; GetString @739; AllocateNextAvailableUsernameAsync @747; HashPin @749; ExecuteNonQueryAsync @767; IsNullOrWhiteSpace @770; Add @772; ExecuteNonQueryAsync @784; ToString @804; ExecuteNonQueryAsync @806; ExecuteNonQueryAsync @831; CountRowsAsync @834; ToArray @838; Select @838; Where @838; CommitAsync @844; RollbackAsync @851; DisposeAsync @857 | FROM demo_seeded_users @734; FROM draft_carts @201; FROM items @167; FROM restaurant_orders @212; FROM sales_invoices @178; FROM shifts @190; FROM stock_movements @223; FROM third_parties @244; FROM users @254; INSERT INTO bom_items @607; INSERT INTO boms @586; INSERT INTO demo_seeded_users @753; INSERT INTO item_kit_components @491; INSERT INTO item_kits @490; INSERT INTO items @305; INSERT INTO items @360; INSERT INTO items @409; INSERT INTO items @460; INSERT INTO items @489; INSERT INTO lots @361; INSERT INTO production_run_inputs @696; INSERT INTO production_run_outputs @655; INSERT INTO production_runs @626; INSERT INTO serials @410; INSERT INTO stock_movements @333; INSERT INTO stock_movements @362; INSERT INTO stock_movements @411; INSERT INTO stock_movements @473; INSERT INTO stock_movements @641; INSERT INTO stock_movements @676; INSERT INTO third_parties @534; INSERT INTO third_parties @558; INSERT INTO user_roles @265; INSERT INTO user_roles @753; INSERT INTO users @265; INSERT INTO users @753; INSERT OR IGNORE INTO expense_categories @813; INSERT OR IGNORE INTO expense_records @813; INSERT OR IGNORE INTO person_records @791; INSERT OR IGNORE INTO product_categories @286; INSERT OR IGNORE INTO salary_agreements @791; INSERT OR IGNORE INTO third_parties @778 · InvalidOperationException @171; InvalidOperationException @182; InvalidOperationException @194; InvalidOperationException @205; InvalidOperationException @216; InvalidOperationException @227; InvalidOperationException @238; InvalidOperationException @246; InvalidOperationException @771; rethrow @852 · DYNAMIC SQL: inspect manually |
| <span id="m-d7bf5ce60300"></span><code>SqliteDemoDataSeeder.ResetDatabaseAsync(DbConnection,Guid,CancellationToken)</code><br>861–908 | ConfigureAwait @868; OpenAsync @868; BeginTransactionAsync @871; RequireDisposableDemoWorkspaceAsync @874; RequireActiveAdminAsync @876; HasEffectivePermissionAsync @877; CreateCommand @881; ExecuteNonQueryAsync @885; TableExistsAsync @890; DeleteIfExistsAsync @892; ResetStoreConfigurationAsync @895; SeedLargeScaleDemoDataCoreAsync @896; SetDatasetStateAsync @897; AppendDemoResetAuditAsync @898; EnsureForeignKeysValidAsync @899; CommitAsync @900; RollbackAsync @905 | UnauthorizedAccessException @879; rethrow @906 |
| <span id="m-20d3ca4e3040"></span><code>SqliteDemoDataSeeder.GetDatasetStateAsync(DbConnection,CancellationToken)</code><br>910–933 | ConfigureAwait @915; OpenAsync @915; BeginTransactionAsync @917; ReadDatasetStateAsync @920; CountRowsAsync @921; CommitAsync @925; Equals @926; RollbackAsync @930 | rethrow @931 |
| <span id="m-8c694ca98963"></span><code>SqliteDemoDataSeeder.RequireDisposableDemoWorkspaceAsync(DbConnection,DbTransaction,CancellationToken)</code><br>935–946 | CreateCommand @940; ConfigureAwait @943; ExecuteScalarAsync @943; ToString @943; Equals @944 | FROM workspace_classification @942 · InvalidOperationException @945 |
| <span id="m-675ad65dcb88"></span><code>SqliteDemoDataSeeder.ReadDatasetStateAsync(DbConnection,DbTransaction,CancellationToken)</code><br>948–957 | CreateCommand @953; ConfigureAwait @956; ExecuteScalarAsync @956; ToString @956 | FROM demo_dataset_state @955 |
| <span id="m-e6541b12631b"></span><code>SqliteDemoDataSeeder.SetDatasetStateAsync(DbConnection,DbTransaction,string,string?,CancellationToken)</code><br>959–980 | CreateCommand @966; AddParam @976; ToString @978; ConfigureAwait @979; ExecuteNonQueryAsync @979 | INSERT INTO demo_dataset_state @968 |
| <span id="m-63b4c62f6102"></span><code>SqliteDemoDataSeeder.HasBusinessDataAsync(DbConnection,DbTransaction,CancellationToken)</code><br>982–1001 | ConfigureAwait @987; CountRowsAsync @987; TableExistsAsync @992; CreateCommand @997; ToInt64 @1000; ExecuteScalarAsync @1000 | FROM third_parties @999 |
| <span id="m-3ef9947b747f"></span><code>SqliteDemoDataSeeder.CountRowsAsync(DbConnection,DbTransaction,string,CancellationToken)</code><br>1003–1015 | ConfigureAwait @1009; TableExistsAsync @1009; CreateCommand @1011; ToInt32 @1014; ExecuteScalarAsync @1014 | DYNAMIC SQL: inspect manually |
| <span id="m-bc30e67956e7"></span><code>SqliteDemoDataSeeder.TableExistsAsync(DbConnection,DbTransaction,string,CancellationToken)</code><br>1017–1024 | CreateCommand @1019; AddParam @1022; ConfigureAwait @1023; ExecuteScalarAsync @1023 | No extracted literal effects. |
| <span id="m-f2977f0e13bf"></span><code>SqliteDemoDataSeeder.AppendDemoResetAuditAsync(DbConnection,DbTransaction,Guid,CancellationToken)</code><br>1026–1068 | CreateCommand @1030; ConfigureAwait @1034; ExecuteReaderAsync @1034; ReadAsync @1035; GetInt64 @1037; GetString @1038; NewGuid @1045; Serialize @1046; ToString @1048; ComputeHash @1049; AddParam @1057; ToString @1058; ToString @1061; ExecuteNonQueryAsync @1067 | FROM immutable_audit_journal @1033; INSERT INTO immutable_audit_journal @1053 |
| <span id="m-1a0cf4ebad14"></span><code>SqliteDemoDataSeeder.EnsureForeignKeysValidAsync(DbConnection,DbTransaction,CancellationToken)</code><br>1070–1078 | CreateCommand @1072; ConfigureAwait @1075; ExecuteReaderAsync @1075; ReadAsync @1076 | InvalidOperationException @1077 |
| <span id="m-8ded7038c87e"></span><code>SqliteDemoDataSeeder.MarkAsDisposableDemoWorkspaceAsync(DbConnection,CancellationToken)</code><br>1084–1110 | ConfigureAwait @1088; OpenAsync @1088; CreateCommand @1091; ExecuteScalarAsync @1093; Equals @1094; ToString @1094; ExecuteNonQueryAsync @1105 | FROM workspace_classification @1092; INSERT INTO workspace_classification @1100 · InvalidOperationException @1096; InvalidOperationException @1108 |
| <span id="m-c905686e9f51"></span><code>SqliteDemoDataSeeder.InitializeDisposableDemoWorkspaceAsync(DbConnection,CancellationToken)</code><br>1115–1169 | ConfigureAwait @1119; OpenAsync @1119; BeginTransactionAsync @1122; CreateCommand @1125; ToInt64 @1128; ExecuteScalarAsync @1128; ExecuteScalarAsync @1135; ToString @1135; Equals @1136; ExecuteScalarAsync @1144; ExecuteNonQueryAsync @1159; CommitAsync @1162; RollbackAsync @1166 | CREATE TABLE  workspace_classification @1150; FROM workspace_classification @1134; INSERT INTO workspace_classification @1150 · InvalidOperationException @1137; InvalidOperationException @1146; rethrow @1167 |
| <span id="m-215440449458"></span><code>SqliteDemoDataSeeder.GetWorkspaceEnvironmentAsync(DbConnection,CancellationToken)</code><br>1171–1182 | ConfigureAwait @1175; OpenAsync @1175; CreateCommand @1178; ExecuteScalarAsync @1180; ToString @1181 | FROM workspace_classification @1179 |
| <span id="m-8a7c4787a964"></span><code>SqliteDemoDataSeeder.AllocateNextAvailableUsernameAsync(DbConnection,DbTransaction,string,CancellationToken)</code><br>1184–1202 | CreateCommand @1190; AddParam @1193; ToInt64 @1194; ConfigureAwait @1194; ExecuteScalarAsync @1194 | FROM users @1192 |
| <span id="m-d88360318f8c"></span><code>SqliteDemoDataSeeder.RequireActiveAdminAsync(DbConnection,DbTransaction,Guid,CancellationToken)</code><br>1204–1240 | CreateCommand @1215; AddParam @1224; ToString @1224; ConfigureAwait @1225; ExecuteScalarAsync @1225; HasEffectivePermissionAsync @1231 | FROM users @1217; JOIN user_roles @1217 · UnauthorizedAccessException @1212; UnauthorizedAccessException @1228; UnauthorizedAccessException @1238 |
| <span id="m-6470cf4b60aa"></span><code>SqliteDemoDataSeeder.HasEffectivePermissionAsync(DbConnection,DbTransaction,Guid,string,CancellationToken)</code><br>1242–1277 | CreateCommand @1249; AddParam @1256; ToString @1256; ConfigureAwait @1258; ExecuteScalarAsync @1258; ToInt32 @1261; ExecuteScalarAsync @1276 | FROM user_permission_overrides @1252; FROM user_roles @1267; JOIN role_permissions @1267 |
| <span id="m-715d4c408805"></span><code>SqliteDemoDataSeeder.AddParam(DbCommand,string,object)</code><br>1279–1285 | CreateParameter @1281; Add @1284 | No extracted literal effects. |

</details>

## SqliteConnectionFactory.cs {#src-fc5b46af45ca}

<code>Software/src/GetSeek.Infrastructure/Persistence/SqliteConnectionFactory.cs</code> · 12 lines.

SHA-256: <code>63b3c615d4efbe33376dd8d28ffbadc3a6818daabac3ae7fedc76b1beb8a63ac</code>.

Declarations: <code>SqliteConnectionFactory</code> (line 5).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-cbdf6612a61f"></span><code>SqliteConnectionFactory.CreateWriteConnectionAsync(CancellationToken)</code><br>7–8 | CreateWriteConnectionAsync @8 | No extracted literal effects. |
| <span id="m-456bc1c45b22"></span><code>SqliteConnectionFactory.CreateReadConnectionAsync(CancellationToken)</code><br>10–11 | CreateReadConnectionAsync @11 | No extracted literal effects. |

</details>

## SqliteConnectionPolicy.cs {#src-4b435878ecef}

<code>Software/src/GetSeek.Infrastructure/Persistence/SqliteConnectionPolicy.cs</code> · 63 lines.

SHA-256: <code>76dc302ca3ce1fd36096b62179264f03cdb3c90205fdb256be735cdcdbbfa5c0</code>.

Declarations: <code>SqliteConnectionPolicy</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-bf2957aefcf7"></span><code>SqliteConnectionPolicy.CreateWriteConnectionAsync(string,CancellationToken)</code><br>13–21 | ConfigureAwait @18; ApplyWritePolicyAsync @18 | No extracted literal effects. |
| <span id="m-82a13447ec45"></span><code>SqliteConnectionPolicy.ApplyWritePolicyAsync(SqliteConnection,CancellationToken)</code><br>29–45 | ConfigureAwait @34; OpenAsync @34; CreateCommand @36; ExecuteNonQueryAsync @44 | No extracted literal effects. |
| <span id="m-02ad95d58bb7"></span><code>SqliteConnectionPolicy.CreateReadConnectionAsync(string,CancellationToken)</code><br>47–62 | ConfigureAwait @52; OpenAsync @52; CreateCommand @54; ExecuteNonQueryAsync @59 | No extracted literal effects. |

</details>

## SqliteDraftCartService.cs {#src-8582f93279dc}

<code>Software/src/GetSeek.Infrastructure/Persistence/SqliteDraftCartService.cs</code> · 361 lines.

SHA-256: <code>0f65983d96837ca95981a0c1916304d89b80cb4252f87e6d1d8c1fb8e53ef575</code>.

Declarations: <code>SqliteDraftCartService</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-fde302d7d822"></span><code>SqliteDraftCartService.SaveActiveCartAsync(DbConnection,Guid,Guid,Guid,string?,IReadOnlyList&lt;DraftCartLineProjection&gt;,Guid?,string?,string?,decimal?,string?,int?,DbTransaction?,CancellationToken)</code><br>9–192 | ToString @25; ConfigureAwait @27; BeginTransactionAsync @27; CreateCommand @35; AddParam @38; ToString @38; ExecuteScalarAsync @39; ToInt32 @42; ToString @73; ToString @74; ToString @76; ToString @79; ExecuteNonQueryAsync @84; ToString @91; Add @92; ToString @132; ToString @142; ToString @143; ToString @144; ExecuteNonQueryAsync @150; Add @163; Join @166; ExecuteNonQueryAsync @168; ExecuteNonQueryAsync @176; CommitAsync @181; RollbackAsync @188 | DELETE FROM draft_cart_lines @174; FROM draft_carts @37; INSERT INTO draft_cart_lines @96; INSERT INTO draft_carts @50 · rethrow @190 · DYNAMIC SQL: inspect manually |
| <span id="m-8de672f8c457"></span><code>SqliteDraftCartService.GetActiveCartAsync(DbConnection,Guid,Guid,CancellationToken)</code><br>194–307 | CreateCommand @209; AddParam @219; ToString @219; ToString @220; ConfigureAwait @222; ExecuteReaderAsync @222; ReadAsync @223; Parse @225; GetString @225; IsDBNull @226; TryParse @227; TryParse @233; GetInt32 @238; ToString @256; ExecuteReaderAsync @258; ReadAsync @259; IsDBNull @261; GetString @261; ToDecimal @263; GetDouble @263; GetInt64 @267; Add @274; GetInt32 @288 | FROM draft_cart_lines @249; FROM draft_carts @211 |
| <span id="m-001efec945d8"></span><code>SqliteDraftCartService.ClearActiveCartAsync(DbConnection,Guid,Guid?,DbTransaction?,CancellationToken)</code><br>309–352 | ToString @316; ConfigureAwait @318; BeginTransactionAsync @318; CreateCommand @322; AddParam @333; ToString @333; ToString @334; ExecuteNonQueryAsync @336; CommitAsync @341; RollbackAsync @348 | DELETE FROM draft_cart_lines @325; FROM draft_carts @325; UPDATE draft_carts @325 · rethrow @350 |
| <span id="m-e38a3f87b6f2"></span><code>SqliteDraftCartService.AddParam(DbCommand,string,object?)</code><br>354–360 | CreateParameter @356; Add @359 | No extracted literal effects. |

</details>

## SqliteUnitOfWork.cs {#src-ddaa7bd9f9ed}

<code>Software/src/GetSeek.Infrastructure/Persistence/SqliteUnitOfWork.cs</code> · 71 lines.

SHA-256: <code>0057571b1753ef13f61e7c6099d3bae8228d56db8be0c71f2834112c428fc96a</code>.

Declarations: <code>SqliteUnitOfWork : IUnitOfWork</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-edbf245ab4e2"></span><code>SqliteUnitOfWork.CreateAsync(SqliteConnectionFactory,CancellationToken)</code><br>21–25 | ConfigureAwait @23; CreateWriteConnectionAsync @23 | No extracted literal effects. |
| <span id="m-dc7500d03338"></span><code>SqliteUnitOfWork.BeginTransactionAsync(CancellationToken)</code><br>27–35 | ConfigureAwait @33; BeginTransactionAsync @33 | InvalidOperationException @30 |
| <span id="m-db1b34dc2b9a"></span><code>SqliteUnitOfWork.CommitAsync(CancellationToken)</code><br>37–45 | ConfigureAwait @42; CommitAsync @42; DisposeAsync @43 | InvalidOperationException @40 |
| <span id="m-a994abcc5cf0"></span><code>SqliteUnitOfWork.RollbackAsync(CancellationToken)</code><br>47–55 | ConfigureAwait @51; RollbackAsync @51; DisposeAsync @52 | No extracted literal effects. |
| <span id="m-86ee9f02e25d"></span><code>SqliteUnitOfWork.DisposeAsync()</code><br>57–70 | ConfigureAwait @63; DisposeAsync @63; DisposeAsync @66; SuppressFinalize @69 | No extracted literal effects. |

</details>

## SystemInvariantChecker.cs {#src-85cc3ba5b2b7}

<code>Software/src/GetSeek.Infrastructure/Persistence/SystemInvariantChecker.cs</code> · 128 lines.

SHA-256: <code>13ba0ff7b6b79de47aaf8248c8ebe8d673c6db3da9261e9cc6483d28c7c13025</code>.

Declarations: <code>InvariantCheckResult</code> (line 5), <code>SystemInvariantChecker</code> (line 13).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ca748179db55"></span><code>SystemInvariantChecker.CheckAllInvariantsAsync(DateTime,CancellationToken)</code><br>15–127 | CreateCommand @18; ConfigureAwait @25; ExecuteReaderAsync @25; ReadAsync @28; GetInt64 @30; Parse @31; GetString @31; IsDBNull @33; ComputeHash @47; ExecuteScalarAsync @63; Parse @66; ToString @66; AddMinutes @67; ToInt64 @79 | FROM cash_movements @118; FROM immutable_audit_journal @20; FROM immutable_audit_journal @60; FROM shifts @107; FROM stock_movements @78; FROM stock_movements @86 |

</details>

## Argon2idPinHasher.cs {#src-a20ec2da0853}

<code>Software/src/GetSeek.Infrastructure/Security/Argon2idPinHasher.cs</code> · 53 lines.

SHA-256: <code>8d606ec78ad044d0956ba64e06d0d808830849b610c308d2bd509ef02dfd8376</code>.

Declarations: <code>Argon2idPinHasher : IPinHasher</code> (line 9).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-6f702f8be962"></span><code>Argon2idPinHasher.HashPin(string)</code><br>11–11 | HashPin @11 | No extracted literal effects. |
| <span id="m-155ec1bd9eaa"></span><code>Argon2idPinHasher.VerifyPin(string,string)</code><br>12–12 | VerifyPin @12 | No extracted literal effects. |
| <span id="m-67b23bd1f5bf"></span><code>Argon2idPinHasher.HashPin(string)</code><br>20–27 | GetBytes @22; HashInternal @23; ToBase64String @26 | No extracted literal effects. |
| <span id="m-40dab34a0d6c"></span><code>Argon2idPinHasher.VerifyPin(string,string)</code><br>29–40 | Split @31; FromBase64String @35; HashInternal @38; FixedTimeEquals @39 | No extracted literal effects. |
| <span id="m-415be648f353"></span><code>Argon2idPinHasher.HashInternal(string,byte[])</code><br>42–52 | GetBytes @44; GetBytes @51 | No extracted literal effects. |

</details>

## SecuritySessionContext.cs {#src-e20d161c07b6}

<code>Software/src/GetSeek.Infrastructure/Security/SecuritySessionContext.cs</code> · 55 lines.

SHA-256: <code>284a8dcc2ba0ed691879ba419b2e1e53b794d27fee969286ef4903a201c9da96</code>.

Declarations: <code>SecuritySessionContext : ISessionContext</code> (line 5).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-38e0b0f09b15"></span><code>SecuritySessionContext.Initialize(Guid,string,IEnumerable&lt;string&gt;)</code><br>16–22 | AsReadOnly @20; ToList @20 | No extracted literal effects. |
| <span id="m-6cef8ac21ea4"></span><code>SecuritySessionContext.Initialize(Guid,string,string,IEnumerable&lt;string&gt;)</code><br>26–27 | Initialize @27 | No extracted literal effects. |
| <span id="m-b61b07a6e848"></span><code>SecuritySessionContext.Lock()</code><br>29–32 | — | No extracted literal effects. |
| <span id="m-4947138c7bff"></span><code>SecuritySessionContext.Unlock()</code><br>34–37 | — | No extracted literal effects. |
| <span id="m-42dd6be9b450"></span><code>SecuritySessionContext.HasPermission(string)</code><br>39–54 | IsNullOrEmpty @44; Contains @47 | No extracted literal effects. |

</details>

## SessionUnlockContracts.cs {#src-66bd43333053}

<code>Software/src/GetSeek.Infrastructure/Security/SessionUnlockContracts.cs</code> · 41 lines.

SHA-256: <code>4d343242b2bd032b99cb29f7d9ab07e9ec947e2201088254c47299eb40d3cae4</code>.

Declarations: <code>UnlockCandidateDto</code> (line 3), <code>SessionUnlockAuthResult</code> (line 14), <code>ISessionUnlockValidator</code> (line 34).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-86b3dcbd42c6"></span><code>SessionUnlockAuthResult.Failed(bool,int,int,string?)</code><br>26–31 | — | No extracted literal effects. |
| <span id="m-7e884f9f048d"></span><code>ISessionUnlockValidator.ValidateCredential(string)</code><br>36–36 | — | No extracted literal effects. |
| <span id="m-62519abdf39c"></span><code>ISessionUnlockValidator.AuthenticateCredential(string)</code><br>37–37 | — | No extracted literal effects. |
| <span id="m-0ebbb3ca039a"></span><code>ISessionUnlockValidator.AuthenticateSelectedUser(Guid,string)</code><br>38–38 | — | No extracted literal effects. |
| <span id="m-8f4885955a2a"></span><code>ISessionUnlockValidator.GetUnlockCandidates()</code><br>39–39 | — | No extracted literal effects. |
| <span id="m-c34d85d30430"></span><code>ISessionUnlockValidator.SetActiveCashier(Guid?)</code><br>40–40 | — | No extracted literal effects. |

</details>

## SqlitePermissionResolver.cs {#src-b2a56743ce1e}

<code>Software/src/GetSeek.Infrastructure/Security/SqlitePermissionResolver.cs</code> · 188 lines.

SHA-256: <code>1de50021a9646d445afed9cac6491a4d7c81a2cbcb5fb913f58320cb7ba28447</code>.

Declarations: <code>SqlitePermissionResolver : IPermissionResolver</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b0ebaa74a4cb"></span><code>SqlitePermissionResolver.ResolveEffectivePermissionsAsync(DbConnection,Guid,CancellationToken)</code><br>9–9 | ResolveCoreAsync @9 | No extracted literal effects. |
| <span id="m-91622b57f3d9"></span><code>SqlitePermissionResolver.ResolveCoreAsync(DbConnection,Guid,DbTransaction?,CancellationToken)</code><br>10–138 | CreateCommand @22; CreateParameter @26; ToString @28; Add @29; ConfigureAwait @31; ExecuteScalarAsync @31; ToInt32 @36; GetRevisionCoreAsync @45; CreateParameter @58; Add @61; ExecuteReaderAsync @63; ReadAsync @64; Add @66; GetString @66; CreateParameter @81; Add @84; ExecuteReaderAsync @86; GetInt32 @90; Add @93; Add @97; Contains @111; Add @113; Contains @118 | FROM role_permissions @52; FROM user_permission_overrides @76; FROM users @25; JOIN user_roles @52 |
| <span id="m-0150222e2793"></span><code>SqlitePermissionResolver.HasPermissionAsync(DbConnection,Guid,string,CancellationToken)</code><br>140–161 | IsNullOrWhiteSpace @146; ConfigureAwait @147; ResolveEffectivePermissionsAsync @147; Contains @151; Contains @154; Contains @157 | No extracted literal effects. |
| <span id="m-aaff2b26d9d6"></span><code>SqlitePermissionResolver.GetSecurityRevisionAsync(DbConnection,Guid,CancellationToken)</code><br>163–163 | GetRevisionCoreAsync @163 | No extracted literal effects. |
| <span id="m-0efc29dd2bba"></span><code>SqlitePermissionResolver.GetRevisionCoreAsync(DbConnection,Guid,DbTransaction?,CancellationToken)</code><br>164–180 | CreateCommand @170; CreateParameter @173; ToString @175; Add @176; ConfigureAwait @178; ExecuteScalarAsync @178; ToInt64 @179 | FROM user_security_revisions @172 |
| <span id="m-66fd71a6c64f"></span><code>SqlitePermissionResolver.HasPermissionAsync(DbConnection,DbTransaction,Guid,string,CancellationToken)</code><br>181–186 | ConfigureAwait @183; ResolveCoreAsync @183; Contains @184; Contains @185; Contains @185 | No extracted literal effects. |

</details>

## SqliteSessionUnlockValidator.cs {#src-a09def58afd6}

<code>Software/src/GetSeek.Infrastructure/Security/SqliteSessionUnlockValidator.cs</code> · 632 lines.

SHA-256: <code>6df07090aeb0efb42fadf8d34fe5d7904fe126deea48a3d826278ced6c281c13</code>.

Declarations: <code>SqliteSessionUnlockValidator : ISessionUnlockValidator</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (12)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-96a7e8b89347"></span><code>SqliteSessionUnlockValidator.SetActiveCashier(Guid?)</code><br>10–14 | — | No extracted literal effects. |
| <span id="m-6177daa50e3e"></span><code>SqliteSessionUnlockValidator.GetOpenConnection(bool)</code><br>26–50 | _connectionFactory @30; Open @33; Open @43 | InvalidOperationException @49 |
| <span id="m-d463b0b1c1c3"></span><code>SqliteSessionUnlockValidator.ValidateCredential(string)</code><br>52–52 | AuthenticateCredential @52 | No extracted literal effects. |
| <span id="m-1657189fbebd"></span><code>SqliteSessionUnlockValidator.GetUnlockCandidates()</code><br>54–174 | GetOpenConnection @60; GetLiveActiveShiftCashierId @63; CreateCommand @67; CreateParameter @75; ToString @77; Add @78; ExecuteReader @80; Read @81; Add @83; Parse @84; GetString @84; ToArray @158; Where @158; IsElevatedOperator @160; Empty(UnlockCandidateDto) @165; Dispose @171 | FROM user_roles @130; FROM user_roles @69; FROM user_roles @95; FROM users @130; FROM users @69; FROM users @95; JOIN role_permissions @130; JOIN role_permissions @95; JOIN user_roles @130; JOIN user_roles @95 |
| <span id="m-e80e0aa196db"></span><code>SqliteSessionUnlockValidator.GetLiveActiveShiftCashierId(DbConnection,DbTransaction?)</code><br>180–197 | CreateCommand @182; ExecuteScalar @190; TryParse @191 | FROM shifts @184 |
| <span id="m-434328717972"></span><code>SqliteSessionUnlockValidator.IsElevatedOperator(DbConnection,Guid,DbTransaction?)</code><br>199–223 | CreateCommand @201; CreateParameter @209; ToString @211; Add @212; ExecuteScalar @213; HasEffectivePermission @220 | FROM user_roles @203 |
| <span id="m-213f50c9f88c"></span><code>SqliteSessionUnlockValidator.HasEffectivePermission(DbConnection,Guid,string,DbTransaction?)</code><br>225–267 | CreateCommand @227; CreateParameter @231; ToString @233; Add @234; ToInt32 @235; ExecuteScalar @235; CreateParameter @247; Add @247; ExecuteScalar @249; CreateParameter @264; Add @264; ExecuteScalar @266 | FROM user_permission_overrides @244; FROM user_roles @258; FROM users @230; JOIN role_permissions @258 |
| <span id="m-123d592f4f3a"></span><code>SqliteSessionUnlockValidator.CheckLockout(DbConnection,DbTransaction,Guid,int,int,string?)</code><br>269–347 | CreateCommand @279; CreateParameter @286; Add @289; ExecuteReader @300; Read @301; GetString @303; GetInt32 @304; IsDBNull @310; TryParse @311; Max @333; Ceiling @333 | FROM sign_in_lockout_state @281 |
| <span id="m-e6ab9612320c"></span><code>SqliteSessionUnlockValidator.RecordFailure(DbConnection,DbTransaction,Guid,bool,int,int)</code><br>349–449 | ToString @357; CreateCommand @362; CreateParameter @366; Add @369; ExecuteScalar @370; ToInt32 @373; ToString @401; AddMinutes @401; ExecuteNonQuery @421 | FROM sign_in_lockout_state @365; FROM sign_in_lockout_state @383; INSERT INTO sign_in_lockout_state @408; INSERT INTO sign_in_lockout_state @428 · rethrow @447 |
| <span id="m-cdfbc82f1cb4"></span><code>SqliteSessionUnlockValidator.ResetFailure(DbConnection,DbTransaction,Guid)</code><br>451–473 | ToString @455; CreateCommand @459; CreateParameter @469; Add @469; ExecuteNonQuery @471 | INSERT INTO sign_in_lockout_state @461 |
| <span id="m-2efc5701a9bc"></span><code>SqliteSessionUnlockValidator.AuthenticateSelectedUser(Guid,string)</code><br>475–625 | GetOpenConnection @482; BeginTransaction @483; RecordFailure @487; Commit @488; Failed @489; CheckLockout @496; IsNullOrWhiteSpace @502; All @510; RecordAndFail @512; GetLiveActiveShiftCashierId @517; IsElevatedOperator @522; CreateCommand @537; CreateParameter @544; ToString @546; Add @547; ExecuteReader @549; Read @550; Close @552; GetString @556; IsDBNull @558; GetInt32 @559; IsNullOrEmpty @567; VerifyPin @572; ResetFailure @580; CreateParameter @589; Add @592; ExecuteReader @594; Read @595; Add @597; GetString @597; GetResult @603; GetAwaiter @603; ResolveEffectivePermissionsAsync @603; ToList @611; Dispose @622 | FROM user_roles @588; FROM users @539 |
| <span id="m-d2f8aca949eb"></span><code>SqliteSessionUnlockValidator.AuthenticateCredential(string)</code><br>627–631 | Failed @630 | No extracted literal effects. |

</details>

## AXAML, migrations and project inputs

### GetSeek.Infrastructure.csproj {#src-2a58abaee0e2}

<code>Software/src/GetSeek.Infrastructure/GetSeek.Infrastructure.csproj</code> · 38 lines · SHA-256 <code>57685fed92ac836f8eb4036510839d5cb22f56df1d4c117056f67ce9f47e388e</code>.

### 001_InitialCoreSchema.sql {#src-aac2c19aed38}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/001_InitialCoreSchema.sql</code> · 272 lines · SHA-256 <code>33bd875f4cfff77685e0ac30ba43cfb87062dddc8d334da4ca8a3b33fe9dcda2</code>.

### 002_AdvancedInventoryAndManufacturing.sql {#src-b2a1f541051d}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/002_AdvancedInventoryAndManufacturing.sql</code> · 91 lines · SHA-256 <code>010041272611c5adfc3b2b11b4f4fabc6150adeca828619705b0aa4803d28904</code>.

### 003_CoreLedgerAndStoreConfig.sql {#src-a1d1b1fdb6c7}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/003_CoreLedgerAndStoreConfig.sql</code> · 30 lines · SHA-256 <code>d2d11bab83bd990132f8893dc94cde775b973b5b901da821c81703a6567f7f52</code>.

### 004_TransactionSafetyAndBusinessProfile.sql {#src-efcab9501d9f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/004_TransactionSafetyAndBusinessProfile.sql</code> · 44 lines · SHA-256 <code>26549cd05a72d177a9033c4e89c633cec68f317f314a57e07d159ecea01cf8eb</code>.

### 005_DeviceProvisioning.sql {#src-5d71e8135306}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/005_DeviceProvisioning.sql</code> · 3 lines · SHA-256 <code>c3b0895018f2abd88d2483c01d28c39bd039fb56ffc300e55ea54af82c0beae6</code>.

### 006_RestaurantOrdersSchema.sql {#src-8f7ce6278155}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/006_RestaurantOrdersSchema.sql</code> · 40 lines · SHA-256 <code>79a0f4754f6ce9ca3032cb697f4cc8ae8bd1f362741fd9df163960f634a48c82</code>.

### 007_ManualPaymentDisplay.sql {#src-ab24922f17a8}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/007_ManualPaymentDisplay.sql</code> · 21 lines · SHA-256 <code>2b1aaf5fce4edaf0c4a82c59fc2baf60780bdbf27ee10d4c6f153638be4d825e</code>.

### 008_InventoryReorderAndTrackingPolicy.sql {#src-256049a15900}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/008_InventoryReorderAndTrackingPolicy.sql</code> · 20 lines · SHA-256 <code>2ed529ef9ba3ea9ab02e9250c59bc8c7b6dd8e9221b7206914bae584c52be86c</code>.

### 009_UomConversionsLocationsAndSuppliers.sql {#src-2525897ed56c}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/009_UomConversionsLocationsAndSuppliers.sql</code> · 159 lines · SHA-256 <code>b562e1eff2c0121f0048a7f9c8332cf1141b05fc5359211d87cf2fb2f8384267</code>.

### 010_RemoveDefaultSupplierSeed.sql {#src-bf4f54596291}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/010_RemoveDefaultSupplierSeed.sql</code> · 3 lines · SHA-256 <code>d8ed7e1b24164581770f048da7ffbcd39c109e46e895091a43254325830c12e5</code>.

### 011_CustomerMasterSchema.sql {#src-74b7fd4d48ec}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/011_CustomerMasterSchema.sql</code> · 16 lines · SHA-256 <code>3b371cfc391fad471bb287eab43d542018a9f63580640801653d344863f269f2</code>.

### 012_CustomerCodeCaseInsensitiveUniqueness.sql {#src-6db457101a81}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/012_CustomerCodeCaseInsensitiveUniqueness.sql</code> · 4 lines · SHA-256 <code>cd25b09de5d8cce3b433ecdf65382c1fd5d1638e34cec41f7bbc1dcf81dba721</code>.

### 013_ItemRelationshipsKitsAndManufacturing.sql {#src-28670c4b00ef}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/013_ItemRelationshipsKitsAndManufacturing.sql</code> · 79 lines · SHA-256 <code>0eb58302e11ba11ac17bf3b5af9f208235989ac3eb7c3ab4f2af70c6bd81deed</code>.

### 014_ShiftZReportSnapshots.sql {#src-4e7cd825ddae}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/014_ShiftZReportSnapshots.sql</code> · 45 lines · SHA-256 <code>a00b9c07a8f677bb4a4a5a765d9994a97c580d0a083c0261f76d3aaa328fabc7</code>.

### 015_OutputDevices.sql {#src-a005b7d653c5}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/015_OutputDevices.sql</code> · 21 lines · SHA-256 <code>6ac1963a5a8a9688c58817f61ae7e08e07e1beb12d920ba2f94166d1930ba31b</code>.

### 016_ProductCategoriesAndUomRegistry.sql {#src-bc761c0c533c}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/016_ProductCategoriesAndUomRegistry.sql</code> · 274 lines · SHA-256 <code>0496a6b8e2acf93bcb0ece08bbdf75603e8becd2f3b93db13ca429cdf014d63b</code>.

### 017_BusinessDateFulfillmentAndTaxRateDecimal.sql {#src-4008335ea88f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/017_BusinessDateFulfillmentAndTaxRateDecimal.sql</code> · 27 lines · SHA-256 <code>6146b921476b163f573fdae858cc72f8698a8708c94665a9ecc6607ff3978465</code>.

### 018_TraceabilityAllocations.sql {#src-2e3572978a8f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/018_TraceabilityAllocations.sql</code> · 27 lines · SHA-256 <code>d9596cd45f05b81e97dc82cd309b8e0c44d0b8512cf6560a11c87418e89d9480</code>.

### 019_CategoryTargetTypesAndPartyUserAssociations.sql {#src-8f6e2280a4a4}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/019_CategoryTargetTypesAndPartyUserAssociations.sql</code> · 31 lines · SHA-256 <code>7e39b1beb023f8a1505cfb31a4667cd9d0e5b312f4b810f5dc35742887c6549b</code>.

### 020_ManufacturingExecutionEnhancements.sql {#src-cdf07342be65}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/020_ManufacturingExecutionEnhancements.sql</code> · 107 lines · SHA-256 <code>046b3c58abcfd5579f2970d589703a4675eebcd9dd4197f7bb1a9a7aebc96fd5</code>.

### 021_CartPromoSnapshots.sql {#src-e090c5ae98e8}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/021_CartPromoSnapshots.sql</code> · 13 lines · SHA-256 <code>b784eb4df1eacccd58ddd98f2f2da528f9909534807be29e4553a71e717a0016</code>.

### 022_ThirdPartyImportHistoryAndExternalKeys.sql {#src-2d58a4c029e1}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/022_ThirdPartyImportHistoryAndExternalKeys.sql</code> · 34 lines · SHA-256 <code>dd534f896c8ee26b41487b17d614a917feb4be99dd8c5f3c3d282b36335fdac8</code>.

### 023_UomDimensionsPreferencesAndItemMeasurements.sql {#src-fba72ef849c1}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/023_UomDimensionsPreferencesAndItemMeasurements.sql</code> · 59 lines · SHA-256 <code>1c34bad52f89097f1d73ed068d0302f89c8e9af5ac4d2bb77ce4d1218b6592be</code>.

### 024_PricingBatchRuns.sql {#src-f16b23a06b4f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/024_PricingBatchRuns.sql</code> · 88 lines · SHA-256 <code>fb244c83f4978889f58bb77cf36220c302b87f62db1e1d9f5110c9058ac9e900</code>.

### 025_BatchSelectionPreviews.sql {#src-be491b91652e}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/025_BatchSelectionPreviews.sql</code> · 27 lines · SHA-256 <code>02c81712b68d597af8f1d4890fc0fcdf95e684c270759547608153079e1d3362</code>.

### 026_PricingIncrementRounding.sql {#src-c11235eaed69}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/026_PricingIncrementRounding.sql</code> · 126 lines · SHA-256 <code>64426fab43813c7dc58580ae0cc6bd165d625814b8de5bf2536f1c6590d24a77</code>.

### 027_InventoryProductMaster.sql {#src-b0caeb9e2b5a}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/027_InventoryProductMaster.sql</code> · 99 lines · SHA-256 <code>5780951e5aaf2840b051e0380825d8b3fdc3fc554c139d7402909ca6c9885f71</code>.

### 028_StaleSafeIntakePriceProposals.sql {#src-0bdadaaf1cc4}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/028_StaleSafeIntakePriceProposals.sql</code> · 56 lines · SHA-256 <code>1d6a1139492cde88b343f3c3cb4d80c843c8921269f90e42a60d2875caf5a6d6</code>.

### 029_PricingCostBasisSource.sql {#src-33e50b512959}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/029_PricingCostBasisSource.sql</code> · 11 lines · SHA-256 <code>ad47e18e41a76e6d1e2a0ce43ed642b26f6594580663273c3752e1bba9e05c9e</code>.

### 030_ProposalExactCostBasis.sql {#src-9ee876b22c8f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/030_ProposalExactCostBasis.sql</code> · 8 lines · SHA-256 <code>c0f3f8e0e92bac50cb96803e0fb6525fbdfb821401582f0dbf90df387ae12963</code>.

### 031_UserPermissionOverrides.sql {#src-1ee421bb0825}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/031_UserPermissionOverrides.sql</code> · 131 lines · SHA-256 <code>903897ec7dc0d22949772562d99cc3d84ad308a4d34709cf52e256bce655fe9b</code>.

### 032_ItemImagePath.sql {#src-787f31942a9e}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/032_ItemImagePath.sql</code> · 2 lines · SHA-256 <code>bc15319944e1f99febc17639d2b966e590ebe20561738a0d05f299d214841b1c</code>.

### 033_WorkspaceProvenance.sql {#src-e27b49f196b1}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/033_WorkspaceProvenance.sql</code> · 9 lines · SHA-256 <code>93318e8e8d86c1c4431a060827a01d8de6bf01ec4c9850833bfbfc70e5708347</code>.

### 034_TerminalLockoutState.sql {#src-b4ef228306bf}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/034_TerminalLockoutState.sql</code> · 7 lines · SHA-256 <code>4bfc77de47d36d2f6399efd9e09cee5219479cdcca39a90273b242028ed303b8</code>.

### 035_LockoutClockHighWater.sql {#src-4a2455af5b5c}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/035_LockoutClockHighWater.sql</code> · 3 lines · SHA-256 <code>8952fa0569bf3d53761fc491d57810f226edc46059a5efe9d20ccf396b117efa</code>.

### 036_LockoutClockHighWaterBackfill.sql {#src-d3bcd9d61eea}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/036_LockoutClockHighWaterBackfill.sql</code> · 9 lines · SHA-256 <code>2e63d3e840fcc8dfbc553ab000c95a81872a988d7c6a2649889892892808f430</code>.

### 037_CashFinancialSettings.sql {#src-8f6e3c3a7dd3}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/037_CashFinancialSettings.sql</code> · 35 lines · SHA-256 <code>6621ca67afe83b18653579aae7eb3ee1f41cf3ab4395992d3ba73246cd1fc845</code>.

### 038_ReceiptDesignAndPrinterCapabilities.sql {#src-2c562fd2b809}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/038_ReceiptDesignAndPrinterCapabilities.sql</code> · 67 lines · SHA-256 <code>0e8a7526ea1d6b9187bc993fe6aab54f28d1a28074800a2679b67c7c26c1fd87</code>.

### 039_CashReceiptRecoveryAndReporting.sql {#src-dc7c1164b0e5}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/039_CashReceiptRecoveryAndReporting.sql</code> · 30 lines · SHA-256 <code>40911184caa009adac53ab435875248e328e04708f924b557b41421c3d9fc794</code>.

### 040_NewWorkspaceRetailDefault.sql {#src-3294a6dfbcd4}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/040_NewWorkspaceRetailDefault.sql</code> · 16 lines · SHA-256 <code>87c59cd95b0d61202457b3d0adfa6d1b8bd8ca43261a5d102a8eb596fddbc4a4</code>.

### 041_ResetPermissionsAndDemoSeededUsers.sql {#src-db5606298ed1}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/041_ResetPermissionsAndDemoSeededUsers.sql</code> · 13 lines · SHA-256 <code>5dd4a07f01b1118f87e83d6ddcac494e52e1f175c309837a688184de8d0cc4dc</code>.

### 042_DemoDatasetState.sql {#src-fcea5b916f6f}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/042_DemoDatasetState.sql</code> · 18 lines · SHA-256 <code>5ddec21476cbcc61e266fe75f13be05ca11b394e291a0700c057278dffd1e5fc</code>.

### 043_PinOnlyUserCredentials.sql {#src-f9eb520b3978}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/043_PinOnlyUserCredentials.sql</code> · 3 lines · SHA-256 <code>1a751d41ef5a8f8641492a1bc647ee64b10a921a5b02244cd0ef7148244a98c7</code>.

### 044_PricingMassRuns.sql {#src-11dd82056ed9}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/044_PricingMassRuns.sql</code> · 37 lines · SHA-256 <code>07e779186f9462704703e0f2a97234875e37bdbb37e56945db3c9f59b6b06547</code>.

### 045_PriceOffers.sql {#src-3a4b6ffc4c59}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/045_PriceOffers.sql</code> · 29 lines · SHA-256 <code>1935bc5b0a782aaa10a3c12641a342663578690dadb617c7cd84eea6d4a082b0</code>.

### 046_PendingShelfLabelsAndKitAlerts.sql {#src-cdee70fd3302}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/046_PendingShelfLabelsAndKitAlerts.sql</code> · 26 lines · SHA-256 <code>40760ae0cae204400b10600dcc8989875ae6b7515cf4587feddb990e880dff17</code>.

### 047_PricingIntegrityAndOfferSemantics.sql {#src-e1cc110fd0df}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/047_PricingIntegrityAndOfferSemantics.sql</code> · 24 lines · SHA-256 <code>06cf386a18c2b576f582646c863f35ea6af8a09805aa959d078b249a8ce4ec40</code>.

### 048_ExclusiveTaxPolicy.sql {#src-dcbca61f9f78}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/048_ExclusiveTaxPolicy.sql</code> · 7 lines · SHA-256 <code>fd3a02cac0540b8e71c6c9e640a2ec8997166a72d5aa1b294be2d1b50220908e</code>.

### 049_RemoveItemUomConversions.sql {#src-711dfb876816}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/049_RemoveItemUomConversions.sql</code> · 3 lines · SHA-256 <code>695855420d5a0a368833ac740d21200dd66605e8bbd3615242d4696c3304841d</code>.

### 050_ProductPurchaseAndSaleDefaultUnits.sql {#src-f7d02920148c}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/050_ProductPurchaseAndSaleDefaultUnits.sql</code> · 14 lines · SHA-256 <code>b20a4f3a393a94e80c574102b9fa0016216fb76d68fa2ae9506792682faccf74</code>.

### 051_ThirdPartyBarcode.sql {#src-8291bfc26d38}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/051_ThirdPartyBarcode.sql</code> · 10 lines · SHA-256 <code>d931e1dfa5d53d7e2eede61880b26f6e7db7dfb1e524ea13c85ec78c126a54a5</code>.

### 052_OptionalItemCoordinates.sql {#src-a56760f6aa70}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/052_OptionalItemCoordinates.sql</code> · 26 lines · SHA-256 <code>7babd75f74681906ac3f1eb9cf65358ca9f3f72dad7fc79a86421f12162b5314</code>.

### 053_StockMovementHistoryIndex.sql {#src-dd9c2a757721}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/053_StockMovementHistoryIndex.sql</code> · 4 lines · SHA-256 <code>4b6db59fd59fa54d28f60019017430402fc95ebc8da38fd61ed8e08976588474</code>.

### 054_ItemPriceHistory.sql {#src-83a3d46284d5}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/054_ItemPriceHistory.sql</code> · 55 lines · SHA-256 <code>d518d6d733ff174ac6c6d51bb787f8b893722460c283c2b38f951afaddec325b</code>.

### 055_DurablePricingRunScopes.sql {#src-4c1d45fe8b51}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/055_DurablePricingRunScopes.sql</code> · 36 lines · SHA-256 <code>e0c24fb36a9a7fe8521d3b8a4bac62d207a1f889e49e2e647ea0de4f05c5ec77</code>.

### 056_PricingRunPreviews.sql {#src-ee611df9ce65}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/056_PricingRunPreviews.sql</code> · 22 lines · SHA-256 <code>e46c17e4f3a4be749a01070210eff8a968e9cdc342780888b275abd2c6453617</code>.

### 057_MultiTierPricingRuns.sql {#src-1bf88834c7ac}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/057_MultiTierPricingRuns.sql</code> · 10 lines · SHA-256 <code>6e0a47dee66cbf0620832df21643dfabc78cc93fdcafe271af3290a33156ceb1</code>.

### 058_OfferVersionsAndSnapshots.sql {#src-6fef2285ae58}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/058_OfferVersionsAndSnapshots.sql</code> · 11 lines · SHA-256 <code>acb66595f86e72bdbb6208a97ac800eba26acbd888ddc7b73594896c5fe21dfb</code>.

### 059_ShelfLabelLifecycle.sql {#src-007c4f329632}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/059_ShelfLabelLifecycle.sql</code> · 33 lines · SHA-256 <code>bf433169700be00576a54c4cb6422428c9e4fa6105fe6053cc9608e608ed2f08</code>.

### 060_CheckoutPriceOverrideAndShelfSnapshots.sql {#src-2325da8217c0}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/060_CheckoutPriceOverrideAndShelfSnapshots.sql</code> · 10 lines · SHA-256 <code>b4fb3ea698c57b5c4e7072cebf17b05da434ce0458a78894de48cf4360bd4f9f</code>.

### 061_KitPriceAlertLifecycle.sql {#src-33f2149be35b}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/061_KitPriceAlertLifecycle.sql</code> · 5 lines · SHA-256 <code>575251fe7be4b1c9aa8c7059410f734bbe0202b89005ec0385ff05ae9d1be64a</code>.

### 062_ShelfLabelOutputProfile.sql {#src-ae4e41a9a228}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/062_ShelfLabelOutputProfile.sql</code> · 9 lines · SHA-256 <code>a72bfa45abcfe7adbcc6f959949b97f5fa74b7d5d7daae2133339612dfdbac10</code>.

### 063_KitAlertProvenance.sql {#src-a403a293ed73}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/063_KitAlertProvenance.sql</code> · 4 lines · SHA-256 <code>ef950b647e88c8832c43273db4b9e818b147b15f089e6869a282557f79410f27</code>.

### 064_ScheduledOfferShelfLabelTransitions.sql {#src-96366501ea15}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/064_ScheduledOfferShelfLabelTransitions.sql</code> · 46 lines · SHA-256 <code>b92443aa6638db0c8655efa4e7c67b7d35caad92fd3eb835bb39074f5a4bc9b0</code>.

### 065_ReportsExportPermission.sql {#src-9eafb90338e6}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/065_ReportsExportPermission.sql</code> · 9 lines · SHA-256 <code>08904075a14880e64eb305405667dd215c53238f0185382f78bf4962c7a34a24</code>.

### 066_InvoiceCollectionsAndReturns.sql {#src-9021699c2da8}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/066_InvoiceCollectionsAndReturns.sql</code> · 120 lines · SHA-256 <code>2f8ec1bb49dff368c05f3d3459d2ae94a4314da324b61786c76b7246e7003b31</code>.

### 067_LossAndDiscountRegisters.sql {#src-25ab341f6525}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/067_LossAndDiscountRegisters.sql</code> · 70 lines · SHA-256 <code>75dfa6c97f17a2a44aea22e0dc1f1e9b0cd9a2af4b95cdf50660961b8b3466f9</code>.

### 068_FinancialFactSnapshots.sql {#src-15d9968cbc95}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/068_FinancialFactSnapshots.sql</code> · 43 lines · SHA-256 <code>e41e2ddf0852a6b2c90536639d384700bcfc04fa27ae8ba255e7f4cf34721577</code>.

### 069_ProductionDraftLotFormula.sql {#src-d85472333e45}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/069_ProductionDraftLotFormula.sql</code> · 2 lines · SHA-256 <code>95449328e95d2c01eee8ad29c2eef13c0dd8ce8f3a3671fd069a649b499063d3</code>.

### 070_InventoryTraceabilityIndexes.sql {#src-66a69940f00c}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/070_InventoryTraceabilityIndexes.sql</code> · 10 lines · SHA-256 <code>318fd386a818ecab9dfa8d20baab63debabddcbebb59cda654f5982717c60033</code>.

### 071_InvoiceFulfillmentAndAccounts.sql {#src-4694c281f058}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/071_InvoiceFulfillmentAndAccounts.sql</code> · 157 lines · SHA-256 <code>fe060c06e9309d33e9e27384c963304775e5064db7a1036fe6ade9cedc8e1a8f</code>.

### 072_CommercialDraftsAndReturnShipments.sql {#src-790ab6fd28b2}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/072_CommercialDraftsAndReturnShipments.sql</code> · 52 lines · SHA-256 <code>af20889d09e90d35b9aacf7556f8e0d9ad5ac36d23857417b127c284772eb4d9</code>.

### 073_SupplierReturnsAndRefunds.sql {#src-6409018ab703}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/073_SupplierReturnsAndRefunds.sql</code> · 6 lines · SHA-256 <code>8cbf19dd5ec2c3e401758fda7f0b43a2dfdd03be2e9aaf445ac0e1aabf26ff37</code>.

### 074_ProductionExactCostSnapshots.sql {#src-562eae5ca899}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/074_ProductionExactCostSnapshots.sql</code> · 2 lines · SHA-256 <code>956a70123e7c950dd321b62dba64b3553f41d05a779a09b03eb4308b5eacea77</code>.

### 075_CommercialWorkflowDetails.sql {#src-a5c45b3bd9f1}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/075_CommercialWorkflowDetails.sql</code> · 28 lines · SHA-256 <code>4d683fcfe85d82d322415bc7aca74ee9a7f8e861b73fa88b85a0c95849dd9c44</code>.

### 076_SearchUsage.sql {#src-4cf7f8ec7d0c}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/076_SearchUsage.sql</code> · 21 lines · SHA-256 <code>f7343cdfa36e0891e82f176b1c73bc5dea603068e563b527d4f79f5b5d6a4acb</code>.

### 077_ProductionCreatedAt.sql {#src-65ec10cf9244}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/077_ProductionCreatedAt.sql</code> · 3 lines · SHA-256 <code>396ed71a578c7b6f49032e022767a13b6be1280a13a4a0a2d62ca54c7398cf02</code>.

### 078_PeopleAndSalaryAgreements.sql {#src-df02b864ac11}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/078_PeopleAndSalaryAgreements.sql</code> · 45 lines · SHA-256 <code>65479cc953acfbc80cdc88e4902763ce8e096d51345f373ee51f62574878d5c6</code>.

### 079_SalaryPeriodsAndLedger.sql {#src-45eaf27680ca}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/079_SalaryPeriodsAndLedger.sql</code> · 79 lines · SHA-256 <code>ae5f520b1f31c04c18cb7658855f8b490c9c73f5603f893ec6808c9edd2b0f17</code>.

### 080_ExpensesAndAttachments.sql {#src-940f2ddfbf40}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/080_ExpensesAndAttachments.sql</code> · 90 lines · SHA-256 <code>4a64896efd20d3a5beaf836dfab206e1db31538e4c8e6b17498a8e704e307ff5</code>.

### 081_SalaryStatementSnapshots.sql {#src-87bd3ff74069}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/081_SalaryStatementSnapshots.sql</code> · 48 lines · SHA-256 <code>8456fddd22411faf9285a6575aca3e9b30f60ca8218831e1adea1f2043fb03f7</code>.

### 082_SalaryEligibilityAndExpensePresets.sql {#src-c16955506a4c}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/082_SalaryEligibilityAndExpensePresets.sql</code> · 16 lines · SHA-256 <code>d4510de15b1c329bb61e503f4da109e2fa51bb0790d801d3bb3b93ff80da01b9</code>.

### 083_ZReportSalaryExpensesAndWasteSettings.sql {#src-4282e327f848}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/083_ZReportSalaryExpensesAndWasteSettings.sql</code> · 20 lines · SHA-256 <code>ae99807f5c1865b115d692d802ebcb90ecd568d1c59eaaae2008f0ef358d96bf</code>.

### 084_CashRoundingTieRule.sql {#src-edd8b63847ba}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/084_CashRoundingTieRule.sql</code> · 4 lines · SHA-256 <code>97f8481ec4a44207cf7f1f9dfb2ba25fd0f4e8b3cc3004a48086a8b330284ae3</code>.

### 085_ServiceItemsAndCatalogIdentity.sql {#src-f9df461b9d64}

<code>Software/src/GetSeek.Infrastructure/Persistence/Migrations/085_ServiceItemsAndCatalogIdentity.sql</code> · 29 lines · SHA-256 <code>d298e0e122b856f5de63a64dd7ed7f7307c43603360a3770e780a970508a3454</code>.
