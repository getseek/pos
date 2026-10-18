---
id: PP-REVIEW-CODE-DESKTOP
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# GetSeek.Desktop source catalogue

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.Desktop.csproj:1](code-desktop.md#src-2f265207af15). Dependencies: <code>GetSeek.UI.Components</code>, <code>GetSeek.Contracts</code>, <code>GetSeek.Infrastructure</code>, <code>GetSeek.Application</code>, <code>GetSeek.Domain</code>.

## App.axaml.cs {#src-de5bb454765b}

<code>Software/src/GetSeek.Desktop/App.axaml.cs</code> · 101 lines.

SHA-256: <code>e515a65d3b838d80917aa145595f7510be197d1ca9d3ad2b8d7c078f65d79d2e</code>.

Declarations: <code>App : Avalonia.Application</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-17cc6a23f0c2"></span><code>App.Initialize()</code><br>19–23 | Load @21 | No extracted literal effects. |
| <span id="m-4e55005e33b1"></span><code>App.OnUiUnhandledException(object?,DispatcherUnhandledExceptionEventArgs)</code><br>25–36 | Report @29; Post @35; Record @35 | No extracted literal effects. |
| <span id="m-f7abd70f5f1c"></span><code>App.OnFrameworkInitializationCompleted()</code><br>38–70 | Empty(string) @42; Contains @43; Equals @46; GetEnvironmentVariable @46; CreateDemo @52; CreateInitializing @52; Cancel @57; Dispose @58; InitializeAppAsync @66; OnFrameworkInitializationCompleted @69 | No extracted literal effects. |
| <span id="m-5aca014abc71"></span><code>App.InitializeAppAsync(MainWindow,bool,bool)</code><br>72–100 | BootstrapDemoWorkspaceAsync @75; BootstrapAsync @76; ReferenceEquals @80; Dispose @82; GetDefaultDatabasePath @91; ToString @92; Run @93; ConfigureAwait @95; RunAsync @95; LogDiagnosticError @97 | No extracted literal effects. |

</details>

## ScrollGestureBehavior.cs {#src-b110df618545}

<code>Software/src/GetSeek.Desktop/Behaviors/ScrollGestureBehavior.cs</code> · 130 lines.

SHA-256: <code>da01d0d074ad0536fd9d1fe11c8ea6805ba5cbfd07f1ce2970f43397e6efa161</code>.

Declarations: <code>ScrollGestureBehavior</code> (line 15), <code>PanState</code> (line 20).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d16a68009af1"></span><code>ScrollGestureBehavior.GetIsEnabled(AvaloniaObject)</code><br>39–39 | GetValue @39 | No extracted literal effects. |
| <span id="m-9f7b4e83d308"></span><code>ScrollGestureBehavior.SetIsEnabled(AvaloniaObject,bool)</code><br>40–40 | SetValue @40 | No extracted literal effects. |
| <span id="m-0e3c8aeb3141"></span><code>ScrollGestureBehavior.Attach(ScrollViewer)</code><br>42–50 | TryGetValue @44; Add @45; AddHandler @46 | No extracted literal effects. |
| <span id="m-eaa3635bd8b6"></span><code>ScrollGestureBehavior.Detach(ScrollViewer)</code><br>52–61 | TryGetValue @54; Capture @55; Remove @56; RemoveHandler @57 | No extracted literal effects. |
| <span id="m-f45d25c1911a"></span><code>ScrollGestureBehavior.OnPressed(object?,PointerPressedEventArgs)</code><br>63–74 | TryGetValue @65; IsInteractiveSource @66; GetPosition @69 | No extracted literal effects. |
| <span id="m-b3c38331b5bb"></span><code>ScrollGestureBehavior.OnMoved(object?,PointerEventArgs)</code><br>76–98 | TryGetValue @78; GetPosition @81; Capture @89; Clamp @94; Max @94 | No extracted literal effects. |
| <span id="m-b7c17ad88f09"></span><code>ScrollGestureBehavior.OnReleased(object?,PointerReleasedEventArgs)</code><br>100–110 | TryGetValue @102; Capture @108 | No extracted literal effects. |
| <span id="m-c4fea86b519a"></span><code>ScrollGestureBehavior.OnCaptureLost(object?,PointerCaptureLostEventArgs)</code><br>112–118 | TryGetValue @114 | No extracted literal effects. |
| <span id="m-6e181ca03bb6"></span><code>ScrollGestureBehavior.IsInteractiveSource(object?,ScrollViewer)</code><br>120–129 | GetVisualParent @123 | No extracted literal effects. |

</details>

## PosBootstrapper.cs {#src-d26211d90637}

<code>Software/src/GetSeek.Desktop/Bootstrap/PosBootstrapper.cs</code> · 310 lines.

SHA-256: <code>d7f5535d3c1ae9ffda8fb551f7e670fe5d57ebe26683d872375030da64763159</code>.

Declarations: <code>PosBootstrapper</code> (line 19).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-2863e7bcbde1"></span><code>PosBootstrapper.GetDefaultDatabasePath()</code><br>21–27 | GetFolderPath @23; Combine @24; CreateDirectory @25 | No extracted literal effects. |
| <span id="m-d7f9cca148b1"></span><code>PosBootstrapper.GetDefaultDemoWorkspaceDirectory()</code><br>29–33 | GetFolderPath @31; Combine @32 | No extracted literal effects. |
| <span id="m-6180ac19f20c"></span><code>PosBootstrapper.GetDefaultDemoDatabasePath()</code><br>35–36 | Combine @36; GetDefaultDemoWorkspaceDirectory @36 | No extracted literal effects. |
| <span id="m-010a66dc5c97"></span><code>PosBootstrapper.ValidateSeparateDemoDatabasePath(string)</code><br>38–52 | GetFullPath @40; GetDefaultDatabasePath @40; Equals @42; GetDirectoryName @45; CreateDirectory @47; GetAttributes @48; Exists @50 | InvalidOperationException @43; InvalidOperationException @49; InvalidOperationException @51 |
| <span id="m-cab7bff553e8"></span><code>PosBootstrapper.GetDefaultLogPath()</code><br>54–58 | GetFolderPath @56; Combine @57 | No extracted literal effects. |
| <span id="m-ba1b92053190"></span><code>PosBootstrapper.GetDefaultDocumentsPath()</code><br>60–66 | GetFolderPath @62; Combine @63; CreateDirectory @64 | No extracted literal effects. |
| <span id="m-a679348838c0"></span><code>PosBootstrapper.LogDiagnosticError(string,Exception,string)</code><br>68–72 | Log @71 | No extracted literal effects. |
| <span id="m-597075fcd734"></span><code>PosBootstrapper.BootstrapAsync(string?,bool,CancellationToken)</code><br>74–78 | BootstrapAsyncCore @78 | No extracted literal effects. |
| <span id="m-9819d2ee6a13"></span><code>PosBootstrapper.BootstrapDemoWorkspaceAsync(CancellationToken)</code><br>80–81 | BootstrapAsyncCore @81 | No extracted literal effects. |
| <span id="m-3dc17a44b22a"></span><code>PosBootstrapper.BootstrapAsyncCore(string?,bool,bool,CancellationToken)</code><br>83–131 | CreateDemo @91; ToUpperInvariant @94; ToString @94; NewGuid @94; IsNullOrWhiteSpace @98; GetDefaultDemoDatabasePath @100; GetDefaultDatabasePath @100; ValidateSeparateDemoDatabasePath @103; GetDirectoryName @105; IsNullOrEmpty @106; CreateDirectory @108; ConfigureAwait @115; ApplyWritePolicyAsync @115; BootstrapWithConnectionAsyncCore @117; LogDiagnosticError @127; CreateStartupError @129 | No extracted literal effects. |
| <span id="m-58efbdaa54ec"></span><code>PosBootstrapper.BootstrapWithConnectionAsync(DbConnection,string?,Func&lt;DbConnection&gt;?,CancellationToken)</code><br>133–138 | BootstrapWithConnectionAsyncCore @138 | No extracted literal effects. |
| <span id="m-c46379c8160f"></span><code>PosBootstrapper.BootstrapWithConnectionAsyncCore(DbConnection,string?,Func&lt;DbConnection&gt;?,bool,CancellationToken)</code><br>140–282 | ToUpperInvariant @147; ToString @147; NewGuid @147; ConfigureAwait @155; InitializeDisposableDemoWorkspaceAsync @155; MigrateAsync @157; GetStoreProfileAsync @161; GetActiveItemsAsync @164; GetActiveShiftAsync @167; Initialize @170; Lock @171; connectionFactory @182; OpenAsync @200; ApplyWritePolicyAsync @202; CreateCommand @226; ExecuteScalarAsync @229; CreateProduction @232; ConfigureInvoiceReader @245; ConfigureSearchPorts @248; Contains @249; ConfigureSalaryPorts @250; ConfigureTeamsPorts @253; ConfigureExpensePorts @256; RestoreActiveCartAsync @267; LoadManualPaymentSettingsAsync @268; LoadActivityInvoicesAsync @269; LoadSuppliersAsync @270; LoadOutputDevicesAsync @271; AuditDocumentsFolder @272; UpdateDemoSeedingAvailabilityAsync @273; LogDiagnosticError @278; CreateStartupError @280 | FROM users @228 |
| <span id="m-8c0c809dac65"></span><code>PosBootstrapper.AuditDocumentsFolder(string,string)</code><br>284–308 | GetDefaultDocumentsPath @288; Exists @289; GetFiles @291; ToLowerInvariant @294; GetExtension @294; GetFileName @295; Contains @296; Log @298 | No extracted literal effects. |

</details>

## NotificationItem.cs {#src-a6098c7284a3}

<code>Software/src/GetSeek.Desktop/Models/NotificationItem.cs</code> · 8 lines.

SHA-256: <code>033ddca9107f891f44b87513d6469e4ce4af1eb941828e5efdb3738c26898536</code>.

Declarations: <code>NotificationItem</code> (line 5).

## UiModels.cs {#src-89bb8d72822c}

<code>Software/src/GetSeek.Desktop/Models/UiModels.cs</code> · 806 lines.

SHA-256: <code>466c4cedf456348e7d4652455b37eb6a7a8f736423418ab086ddcd68e60a4487</code>.

Declarations: <code>CurrencyFormatter</code> (line 6), <code>CategoryItem : ReactiveObject</code> (line 20), <code>ProductCategoryOption</code> (line 47), <code>ExpenseCategoryOption</code> (line 64), <code>ProductPurposeOption</code> (line 79), <code>UomOption</code> (line 84), <code>StoreUomPreferenceItem : ReactiveObject</code> (line 138), <code>ProductItem : ReactiveObject</code> (line 160), <code>OrderItem : ReactiveObject</code> (line 186), <code>StaleCartPriceReviewUiRow</code> (line 262), <code>LotCandidateItem</code> (line 270), <code>SerialCandidateItem : ReactiveObject</code> (line 285), <code>OrderStatusChip : ReactiveObject</code> (line 309), <code>OrderLogItem : ReactiveObject</code> (line 349), <code>InventoryItem : ReactiveObject</code> (line 380), <code>KitComponentDraftItem : ReactiveObject</code> (line 497), <code>PayrollMonthOption : IEquatable&lt;PayrollMonthOption&gt;</code> (line 529), <code>StaffMember : ReactiveObject</code> (line 553), <code>UserPermissionOverrideItem : ReactiveObject</code> (line 611), <code>ReportTenderItem : ReactiveObject</code> (line 669), <code>ShiftReportSummary : ReactiveObject</code> (line 678), <code>FacilityItem : ReactiveObject</code> (line 718), <code>BinLocationItem : ReactiveObject</code> (line 728), <code>ItemLocationEligibilityItem : ReactiveObject</code> (line 742), <code>ReceiveTrackingKind</code> (line 757), <code>ReceiveLineItem : ReactiveObject</code> (line 769).

<details markdown>
<summary>Methods, calls, table effects and failures (11)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7303823d0b7e"></span><code>CurrencyFormatter.Format(decimal,string,int)</code><br>8–17 | Clamp @10; Round @14; ToString @16 | No extracted literal effects. |
| <span id="m-1667c822cb94"></span><code>ProductCategoryOption.ToString()</code><br>61–61 | — | No extracted literal effects. |
| <span id="m-6c53d4e69e32"></span><code>ExpenseCategoryOption.ToString()</code><br>76–76 | — | No extracted literal effects. |
| <span id="m-3a2f50acce63"></span><code>ProductPurposeOption.ToString()</code><br>81–81 | — | No extracted literal effects. |
| <span id="m-b2cf49c707d1"></span><code>UomOption.ToString()</code><br>135–135 | — | No extracted literal effects. |
| <span id="m-3db5ee47b77b"></span><code>LotCandidateItem.ToString()</code><br>281–281 | — | No extracted literal effects. |
| <span id="m-36e975b06f00"></span><code>SerialCandidateItem.ToString()</code><br>306–306 | — | No extracted literal effects. |
| <span id="m-fdd97835bafe"></span><code>PayrollMonthOption.Equals(PayrollMonthOption?)</code><br>542–543 | — | No extracted literal effects. |
| <span id="m-90bd24b05e5e"></span><code>PayrollMonthOption.Equals(object?)</code><br>545–546 | Equals @546 | No extracted literal effects. |
| <span id="m-facea2a640e0"></span><code>PayrollMonthOption.GetHashCode()</code><br>548–548 | GetHashCode @548 | No extracted literal effects. |
| <span id="m-5306ed406183"></span><code>PayrollMonthOption.ToString()</code><br>550–550 | — | No extracted literal effects. |

</details>

## Program.cs {#src-b643fde582df}

<code>Software/src/GetSeek.Desktop/Program.cs</code> · 18 lines.

SHA-256: <code>f0e38492b4a3d3884b150828ff1049dfff4e48d1ce0cf02f4568bfa3e9f9ac35</code>.

Declarations: <code>Program</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d1261a71932d"></span><code>Program.Main(string[])</code><br>8–10 | StartWithClassicDesktopLifetime @9; BuildAvaloniaApp @9 | No extracted literal effects. |
| <span id="m-28a2dddf33b3"></span><code>Program.BuildAvaloniaApp()</code><br>12–17 | UseReactiveUI(App) @13; LogToTrace(App) @13; WithInterFont(App) @13; UsePlatformDetect(App) @13; Configure(App) @13 | No extracted literal effects. |

</details>

## SessionUnlockValidator.cs {#src-ea6741e49c98}

<code>Software/src/GetSeek.Desktop/Security/SessionUnlockValidator.cs</code> · 268 lines.

SHA-256: <code>ff542fac6de28184c40e6bab1c4ac60599f4c71a33803c7f563bdd5b7c709b55</code>.

Declarations: <code>DemoSessionUnlockValidator : ISessionUnlockValidator</code> (line 5), <code>DelegateSessionUnlockValidator : ISessionUnlockValidator</code> (line 237).

<details markdown>
<summary>Methods, calls, table effects and failures (16)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-29dd4f57a4db"></span><code>DemoSessionUnlockValidator.SetQuickPin(Guid,string)</code><br>22–26 | ResetFailure @25 | No extracted literal effects. |
| <span id="m-265819f1d48f"></span><code>DemoSessionUnlockValidator.SetActiveCashier(Guid?)</code><br>28–31 | — | No extracted literal effects. |
| <span id="m-b920f3d9a0e8"></span><code>DemoSessionUnlockValidator.GetUnlockCandidates()</code><br>33–41 | ToArray @37; Where @37 | No extracted literal effects. |
| <span id="m-5b10ef291d8e"></span><code>DemoSessionUnlockValidator.ValidateCredential(string)</code><br>43–43 | AuthenticateCredential @43 | No extracted literal effects. |
| <span id="m-a700445bba6d"></span><code>DemoSessionUnlockValidator.CheckLockout(Guid,int,int)</code><br>45–65 | Max @50; Ceiling @50; TryGetValue @55 | No extracted literal effects. |
| <span id="m-d1895fd8715d"></span><code>DemoSessionUnlockValidator.RecordFailure(Guid,bool,int,int)</code><br>67–100 | TryGetValue @70; AddMinutes @75; Max @91; Ceiling @91 | No extracted literal effects. |
| <span id="m-a181dee9a67d"></span><code>DemoSessionUnlockValidator.ResetFailure(Guid)</code><br>102–107 | Remove @104 | No extracted literal effects. |
| <span id="m-dd5c35292808"></span><code>DemoSessionUnlockValidator.AuthenticateSelectedUser(Guid,string)</code><br>109–171 | CheckLockout @115; Failed @117; IsNullOrWhiteSpace @120; Parse @126; RecordFailure @131; IsValidPin @145; TryGetValue @152; ResetFailure @165; GetDemoSuccessResult @166 | No extracted literal effects. |
| <span id="m-cb795857e74e"></span><code>DemoSessionUnlockValidator.IsValidPin(string)</code><br>173–173 | All @173 | No extracted literal effects. |
| <span id="m-49ed5878e068"></span><code>DemoSessionUnlockValidator.AuthenticateCredential(string)</code><br>175–179 | Failed @178 | No extracted literal effects. |
| <span id="m-9549a0a53dd2"></span><code>DemoSessionUnlockValidator.GetDemoSuccessResult(Guid)</code><br>181–234 | Parse @183; Failed @233 | No extracted literal effects. |
| <span id="m-858d57bd1b79"></span><code>DelegateSessionUnlockValidator.SetActiveCashier(Guid?)</code><br>254–257 | — | No extracted literal effects. |
| <span id="m-cc515f3a8650"></span><code>DelegateSessionUnlockValidator.ValidateCredential(string)</code><br>259–259 | AuthenticateCredential @259 | No extracted literal effects. |
| <span id="m-4f26a963e7d7"></span><code>DelegateSessionUnlockValidator.AuthenticateCredential(string)</code><br>260–260 | _authenticator @260 | No extracted literal effects. |
| <span id="m-943bfe71dc83"></span><code>DelegateSessionUnlockValidator.AuthenticateSelectedUser(Guid,string)</code><br>262–262 | _authenticator @262 | No extracted literal effects. |
| <span id="m-a4bd584f12ea"></span><code>DelegateSessionUnlockValidator.GetUnlockCandidates()</code><br>264–267 | NewGuid @266 | No extracted literal effects. |

</details>

## ErrorReporter.cs {#src-7bb1829faf9c}

<code>Software/src/GetSeek.Desktop/Services/ErrorReporter.cs</code> · 80 lines.

SHA-256: <code>c28ea46f651cf9c7f225ad44ab439180acbc646fd8de0248558b5cf7c222f525</code>.

Declarations: <code>ErrorLogEntry</code> (line 6), <code>ErrorReporter</code> (line 39).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4dd5ea2f8129"></span><code>ErrorReporter.Report(string,string?,string,Exception?,string?)</code><br>55–79 | IsNullOrWhiteSpace @62; ToString @63; NewGuid @63; Trim @64; LogDiagnostic @67 | No extracted literal effects. |

</details>

## ErrorSink.cs {#src-b32338ae37aa}

<code>Software/src/GetSeek.Desktop/Services/ErrorSink.cs</code> · 21 lines.

SHA-256: <code>ac28f85603a5fa1ac57890e19a8c707d9fe6bc8896a8e4c816ae7a077a630de9</code>.

Declarations: <code>ErrorSink</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-0b0d56b5b10f"></span><code>ErrorSink.Record(ErrorLogEntry)</code><br>12–20 | Invoke @19 | No extracted literal effects. |

</details>

## ModalCoordinator.cs {#src-a9e730e05c08}

<code>Software/src/GetSeek.Desktop/Services/ModalCoordinator.cs</code> · 68 lines.

SHA-256: <code>52380a582313db4a2e2f2082254e3e93a2c2691f6d495894d23ce3e672f7ea60</code>.

Declarations: <code>ModalCoordinator : IDisposable</code> (line 7), <code>Registration</code> (line 50), <code>RegistrationToken : IDisposable</code> (line 58).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-6814c155ab5a"></span><code>ModalCoordinator.Register(string,int,Func&lt;bool&gt;,Action,bool)</code><br>12–26 | ThrowIfNullOrWhiteSpace @19; ThrowIfNull @20; Add @24 | No extracted literal effects. |
| <span id="m-c81cd9a268b4"></span><code>ModalCoordinator.TryHandleEscape()</code><br>29–44 | FirstOrDefault @31; ThenByDescending @31; OrderByDescending @31; Where @31; IsOpen @32; RequestDismiss @41 | No extracted literal effects. |
| <span id="m-c132af526ec8"></span><code>ModalCoordinator.Dispose()</code><br>46–46 | Clear @46 | No extracted literal effects. |
| <span id="m-68fac85ee8a9"></span><code>ModalCoordinator.Unregister(Registration)</code><br>48–48 | Remove @48 | No extracted literal effects. |
| <span id="m-eb1d48192360"></span><code>RegistrationToken.Dispose()</code><br>62–66 | Unregister @64 | No extracted literal effects. |

</details>

## UiPreferencesService.cs {#src-3ede46aa073a}

<code>Software/src/GetSeek.Desktop/Services/UiPreferencesService.cs</code> · 4,787 lines.

SHA-256: <code>e02a9beb3047099c809cc181c18cb0017baa8ab2342c1b091da00006e3b77e1a</code>.

Declarations: <code>UiPreferences</code> (line 12), <code>IUiPreferencesService</code> (line 20), <code>UiPreferencesService : IUiPreferencesService</code> (line 30), <code>ILocalizationService</code> (line 86), <code>LocalizationService : ILocalizationService</code> (line 96), <code>ThemeManager</code> (line 4678).

<details markdown>
<summary>Methods, calls, table effects and failures (12)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-69a3b01d8029"></span><code>IUiPreferencesService.Load()</code><br>22–22 | — | No extracted literal effects. |
| <span id="m-592fdd3892e2"></span><code>IUiPreferencesService.Save(UiPreferences)</code><br>23–23 | — | No extracted literal effects. |
| <span id="m-c2b8dbfc95d6"></span><code>UiPreferencesService.Load()</code><br>47–64 | Exists @51; ReadAllText @53; Deserialize(UiPreferences) @54 | No extracted literal effects. |
| <span id="m-7261564d0166"></span><code>UiPreferencesService.Save(UiPreferences)</code><br>66–82 | GetDirectoryName @70; IsNullOrEmpty @71; CreateDirectory @73; WriteAllText @76; Serialize @76 | No extracted literal effects. |
| <span id="m-6065c0c3e12d"></span><code>ILocalizationService.Localize(string,object?[])</code><br>89–89 | — | No extracted literal effects. |
| <span id="m-3d6830d6f052"></span><code>LocalizationService.Localize(string,object?[])</code><br>4645–4675 | ToLowerInvariant @4647; Trim @4647; TryGetValue @4655; TryGetValue @4658; Format @4668 | No extracted literal effects. |
| <span id="m-9d057167a859"></span><code>ThemeManager.Resolve(string?)</code><br>4695–4696 | IsNullOrWhiteSpace @4696; ContainsKey @4696 | No extracted literal effects. |
| <span id="m-5c7db80627d3"></span><code>ThemeManager.DisplayName(string?)</code><br>4698–4698 | Resolve @4698 | No extracted literal effects. |
| <span id="m-d5bceda95365"></span><code>ThemeManager.NextTheme(string?)</code><br>4701–4714 | Equals @4706 | No extracted literal effects. |
| <span id="m-54cee5300285"></span><code>ThemeManager.Apply(string?)</code><br>4717–4751 | Equals @4720; Resolve @4722; SwapThemeSlot @4736; CheckAccess @4741; Post @4743; ApplyCore @4747 | No extracted literal effects. |
| <span id="m-4fd8e6f7551d"></span><code>ThemeManager.IsThemeInclude(object)</code><br>4754–4756 | Contains @4756 | No extracted literal effects. |
| <span id="m-bfb9fb163972"></span><code>ThemeManager.SwapThemeSlot(IList&lt;IResourceProvider&gt;,string)</code><br>4758–4781 | ToList(ResourceInclude) @4762; Where(ResourceInclude) @4762; OfType(ResourceInclude) @4762; Remove @4764; Equals @4769; Add @4780 | No extracted literal effects. |

</details>

## ItemPricingEditorState.cs {#src-e15de4a665a7}

<code>Software/src/GetSeek.Desktop/ViewModels/ItemPricingEditorState.cs</code> · 123 lines.

SHA-256: <code>b21590b35e78286b0ced964bda77b31a19e0b5497f93e7af68e45e00999f3b18</code>.

Declarations: <code>ProductPricePreviewRow</code> (line 10), <code>ItemPricingEditorState : ReactiveObject</code> (line 17).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a951500ecabc"></span><code>ItemPricingEditorState.OnTiersChanged(object?,NotifyCollectionChangedEventArgs)</code><br>67–74 | RaisePropertyChanged @73; nameof @73 | No extracted literal effects. |
| <span id="m-5b98875590ef"></span><code>ItemPricingEditorState.OnTierChanged(object?,PropertyChangedEventArgs)</code><br>76–76 | RaisePropertyChanged @76; nameof @76 | No extracted literal effects. |
| <span id="m-636d545ba8b9"></span><code>ItemPricingEditorState.Clone()</code><br>78–105 | Add @94 | No extracted literal effects. |
| <span id="m-48426e41c6f7"></span><code>ItemPricingEditorState.ToCommand(Guid,int)</code><br>107–122 | ToMinorUnits @114; ToList @115; Select @115 | No extracted literal effects. |

</details>

## MainViewModel.Commercial.cs {#src-e4058a856f7c}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Commercial.cs</code> · 592 lines.

SHA-256: <code>071da96d048c0d19e2e0882786bf3785c6c3f5af6d3eb1a40cd14d2d9a6eedb8</code>.

Declarations: <code>CommercialLineEditor : ReactiveObject</code> (line 17), <code>DispatchQuantityEditor : ReactiveObject</code> (line 39), <code>MainViewModel</code> (line 48).

<details markdown>
<summary>Methods, calls, table effects and failures (31)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-851347bbf251"></span><code>MainViewModel.ResetCommercialFilterPages()</code><br>91–91 | ResetToFirstPage @91; ResetToFirstPage @91; LoadCommercialAsync @91 | No extracted literal effects. |
| <span id="m-57c4d3c6b6ff"></span><code>MainViewModel.CommercialSourceText(string)</code><br>146–146 | Localize @146 | No extracted literal effects. |
| <span id="m-f66b4f83fc11"></span><code>MainViewModel.CText(string)</code><br>161–161 | Localize @161 | No extracted literal effects. |
| <span id="m-8d3e91622cc3"></span><code>MainViewModel.CMoney(long,string,int)</code><br>162–162 | ToString @162; ToDecimal @162 | No extracted literal effects. |
| <span id="m-95faab49defb"></span><code>MainViewModel.InitializeCommercialWorkspace()</code><br>175–211 | CreateFromTask @177; Create @178; Clear @181; Clear @181; Clear @181; nameof @182; RaisePropertyChanged @182; ResetCommercialFilterPages @183; OpenCommercial @185; AddCommercialLine @186; CreateFromTask(CommercialLineEditor) @186; Create(CommercialLineEditor) @186; Remove @186; SaveCommercialAsync @187; CreateFromTask(CommercialInvoiceRow) @191; OpenCommercialMoneyAsync @191; OpenCommercialReceiptAsync @195; OpenCommercialPurchaseCreditAsync @196; Create(MoneyEventRow) @201; Parse @201; Create(ShipmentSummary) @202; CreateFromTask(MoneyEventRow) @203; TryParse @203; LoadCommercialSourceInvoicesAsync @203; RecordSuccessfulSearchUseAsync @203; FromGuid @203; CreateFromTask(ShipmentSummary) @204; LoadCommercialHistoryAsync @204; Register @205; BindRefresh @206; LoadCommercialAsync @206; BindRefresh @206; BindRefresh @206; CommercialSnapshot @206; OpenCommercialInvoiceAsync @208; Create(DispatchQuantityEditor) @209; CText @209; BuildCommercialTables @210 | No extracted literal effects. |
| <span id="m-400c4addef31"></span><code>MainViewModel.BuildCommercialTables()</code><br>212–224 | CText @214; ToString @215; Col @216; CMoney @216; HasPermission @217; ToLocalTime @219; Parse @221; CommercialSourceText @221; LocalizeTable @223; Localize @223; Max @223; Ceiling @223 | No extracted literal effects. |
| <span id="m-31fd4d5a54e6"></span><code>MainViewModel.ResolveCommercialDateRangeUtcAsync()</code><br>225–260 | ConfigureAwait @237; GetStoreTimeZoneAsync @237; ConvertLocalToUtc @249; AddDays @255 | No extracted literal effects. |
| <span id="m-a6d690916ae0"></span><code>MainViewModel.LoadCommercialAsync()</code><br>262–304 | ConfigureAwait @268; ResolveCommercialDateRangeUtcAsync @268; DispatchToUi @271; ApplyPagedResult @275; ApplyPagedResult @276; GetInvoicesAsync @286; ToPageRequest @286; GetShipmentsAsync @292; ToPageRequest @292; ApplyPagedResult @293; GetAccountsAsync @298; GetMoneyAsync @299; ToPageRequest @299; TryParse @299; ToString @299; Clear @300; Add @300; RaisePropertyChanged @300; nameof @300; SafeError @303 | No extracted literal effects. |
| <span id="m-7df72f622a36"></span><code>MainViewModel.OpenCommercial(string,string)</code><br>305–312 | CheckSessionUnlocked @307; CText @307; HasPermission @307; ToString @308; NewGuid @308; Clear @308; Clear @308; Clear @308; Clear @308; Clear @309; Clear @309; Where @310; GetProperties @310; GetType @310; StartsWith @310; RaisePropertyChanged @310; CommercialSnapshot @311; RefreshCommercialLookupsAsync @311 | No extracted literal effects. |
| <span id="m-363b83279ce0"></span><code>MainViewModel.RefreshCommercialLookupsAsync()</code><br>313–324 | FindPartiesAsync @319; FindItemsAsync @319; DispatchToUi @319; Clear @319; Add @319; Clear @319; Add @319; GetAccountsAsync @321; Clear @321; Where @321; Add @321; SafeError @323 | No extracted literal effects. |
| <span id="m-88ab07812b3b"></span><code>MainViewModel.EnsurePaymentAccountsLoadedAsync(CancellationToken)</code><br>325–348 | HasPermission @327; ConfigureAwait @331; GetAccountsAsync @331; DispatchToUi @332; Clear @335; Where @336; Add @338; RaisePropertyChanged @340; nameof @340; SafeError @346 | No extracted literal effects. |
| <span id="m-599d120d8705"></span><code>MainViewModel.AssignCommercialParty(CommercialPartyChoice?,string?)</code><br>349–360 | ReferenceEquals @351; IsNullOrWhiteSpace @357; ToString @357; NewGuid @357; RecordSuccessfulSearchUseAsync @358; FromGuid @358 | No extracted literal effects. |
| <span id="m-057eeea1834d"></span><code>MainViewModel.AddCommercialLine(string?)</code><br>362–371 | Any @365; CText @365; Add @367; ToDecimal @367; IsNullOrWhiteSpace @369; ToString @369; NewGuid @369; RecordSuccessfulSearchUseAsync @370; FromGuid @370 | No extracted literal effects. |
| <span id="m-72c0fe771e4b"></span><code>MainViewModel.LoadCommercialKitAsync(CommercialLineEditor)</code><br>372–377 | GetKitLeavesAsync @375; Clear @375; Add @375; SafeError @376 | No extracted literal effects. |
| <span id="m-be5a21a20fce"></span><code>MainViewModel.OpenCommercialInvoiceAsync(CommercialInvoiceRow)</code><br>378–404 | OpenCommercial @383; GetDraftAsync @384; CText @384; ToDateTime @385; Add @386; ToDecimal @386; Where @387; First @388; LoadCommercialKitAsync @388; FirstOrDefault @388; CommercialSnapshot @389; GetPurchaseAsync @393; RecordSuccessfulSearchUseAsync @399; FromGuid @399; RaisePropertyChanged @401; nameof @401; LoadCommercialHistoryAsync @401; GetInvoiceAsync @403; OpenInvoiceAsync @403 | No extracted literal effects. |
| <span id="m-55142b386bdf"></span><code>MainViewModel.OpenCommercialDispatchAsync(CommercialInvoiceRow)</code><br>405–410 | OpenCommercial @407; GetReservationsAsync @408; Add @408; CommercialSnapshot @408; SafeError @409 | No extracted literal effects. |
| <span id="m-ba8578eb7455"></span><code>MainViewModel.OpenCommercialReceiptAsync(CommercialInvoiceRow,bool)</code><br>411–416 | OpenCommercial @413; GetPurchaseAsync @414; Where @414; Add @414; CommercialSnapshot @414; SafeError @415 | No extracted literal effects. |
| <span id="m-911dbd9dcc02"></span><code>MainViewModel.OpenCommercialPurchaseCreditAsync(CommercialInvoiceRow)</code><br>417–422 | OpenCommercial @419; GetPurchaseAsync @420; Where @421; Add @421; CommercialSnapshot @421 | No extracted literal effects. |
| <span id="m-d2ca35d6dd6f"></span><code>MainViewModel.OpenCommercialMoneyAsync(CommercialInvoiceRow,string,string)</code><br>423–424 | OpenCommercial @424; ToDecimal @424; Abs @424; GetUnshippedLinesAsync @424; Add @424; CommercialSnapshot @424; RefreshCommercialLookupsAsync @424 | No extracted literal effects. |
| <span id="m-398614bb75b1"></span><code>MainViewModel.CommercialSnapshot()</code><br>425–425 | Serialize @425; Select @425; Select @425; Select @425 | No extracted literal effects. |
| <span id="m-51dfd20ea93c"></span><code>MainViewModel.RequestCommercialClose()</code><br>426–426 | CommercialSnapshot @426 | No extracted literal effects. |
| <span id="m-82c10c708fe8"></span><code>MainViewModel.RequestCommercialReturnAsync()</code><br>427–440 | CheckSessionUnlocked @429; InvoiceEditorState @430; Localize @430; ExecuteAsync(RequestReturnShipmentCommand, Guid) @434; ReturnCommand @434; LoadCommercialAsync @436; SafeError @438 | No extracted literal effects. |
| <span id="m-34d3cf9d5a32"></span><code>MainViewModel.OpenCommercialReturnReceiptAsync(CommercialInvoiceRow)</code><br>441–456 | OpenCommercial @443; GetReturnRequestAsync @446; GetInvoiceAsync @446; First @449; ToList @449; Select @449; Where @449; Any @449; Add @449; Join @449; PreviewReturnAsync @451; RaisePropertyChanged @453; nameof @453; CommercialSnapshot @453; SafeError @455 | No extracted literal effects. |
| <span id="m-c093db27f863"></span><code>MainViewModel.SaveCommercialAsync(bool)</code><br>457–537 | CommercialSnapshot @462; ToString @462; NewGuid @462; FromDateTime @465; CText @468; ExecuteAsync(SaveOrderDraftCommand, Guid) @469; ToList @469; Select @469; FromDecimal @469; Select @469; Where @469; ExecuteAsync(PreviewOrderInvoiceCommand, OrderInvoicePreview) @473; FirstOrDefault @476; CMoney @476; RaisePropertyChanged @478; nameof @478; ExecuteAsync(IssueOrderInvoiceCommand, SalesInvoice) @480; Failure(Guid) @480; ExecuteAsync(SavePurchaseDraftCommand, Guid) @488; LoadCommercialAsync @489; Preview @495; ExecuteAsync(RecordSupplierInvoiceCommand, Guid) @501; ExecuteAsync(DispatchShipmentCommand, Guid) @505; Where @505; Where @507; IsNullOrWhiteSpace @507; SpecifyKind @507; AddTicks @507; AddDays @507; Split @507; ExecuteAsync(ReturnSupplierGoodsCommand, Guid) @507; ExecuteAsync(ReceivePurchaseGoodsCommand, Guid) @507; ExecuteAsync(ReplaceInvoiceReservationCommand, bool) @509; Success(Guid) @509; ExecuteAsync(UpdateShipmentTrackingCommand, bool) @511; ExecuteAsync(CancelSupplierInvoiceLinesCommand, Guid) @512; ExecuteAsync(CancelReturnShipmentRequestCommand, Guid) @513; ExecuteAsync(ConfirmSupplierReturnDeliveryCommand, bool) @515; ExecuteAsync(ConfirmShipmentDeliveryCommand, bool) @515; PreviewCommercialReturnReceiptAsync @518; ExecuteAsync(ReceiveReturnShipmentCommand, Guid) @521; BuildCommercialReturnReceipt @521; ExecuteAsync(ReverseMoneyTransferCommand, Guid) @523; ExecuteAsync(ReceiveSupplierRefundCommand, Guid) @524; ExecuteAsync(CancelInvoiceRemainderCommand, Guid) @525; ExecuteAsync(RecordAccountOpeningCommand, Guid) @526; ExecuteAsync(RefundCancelledInvoiceCommand, Guid) @527; ExecuteAsync(CreateMoneyAccountCommand, Guid) @528; ExecuteAsync(TransferMoneyCommand, Guid) @529; ExecuteAsync(PaySupplierInvoiceCommand, Guid) @530; ExecuteAsync(CollectBankInvoiceCommand, Guid) @531; LoadInventoryAsync @533; SafeError @535 | InvalidOperationException @468; InvalidOperationException @484; InvalidOperationException @532 |
| <span id="m-248eed0235bb"></span><code>MainViewModel.PreviewCommercialReturnReceiptAsync()</code><br>538–553 | CText @540; GetInvoiceAsync @541; BuildCommercialReturnReceipt @543; PreviewReturnAsync @546; Round @549; CMoney @552; RaisePropertyChanged @552; nameof @552 | InvalidOperationException @540; InvalidOperationException @548; InvalidOperationException @551 |
| <span id="m-36209a379643"></span><code>MainViewModel.BuildCommercialReturnReceipt()</code><br>554–570 | CText @556; ToList @557; Select @557; Where @557; First @559; ToHashSet @560; Split @560; First @561; Where @562; Select @562; FirstOrDefault @564; Contains @565 | InvalidOperationException @556 |
| <span id="m-84eb8f3448bc"></span><code>MainViewModel.LoadCommercialSourceInvoicesAsync(Guid,string)</code><br>571–575 | GetSourceInvoicesAsync @573; Clear @574; Add @574 | No extracted literal effects. |
| <span id="m-5fe420f5497b"></span><code>MainViewModel.LoadCommercialHistoryAsync(Guid,string)</code><br>576–580 | GetHistoryAsync @578; Clear @579; Add @579; ToString @579; ToLocalTime @579; CommercialSourceText @579 | No extracted literal effects. |
| <span id="m-a46d9b031aaa"></span><code>MainViewModel.PrintCommercialDocumentAsync()</code><br>581–588 | ExecuteAsync(QueueCommercialDocumentCommand, Guid) @586; CText @586; SafeError @587 | No extracted literal effects. |
| <span id="m-a771132a9575"></span><code>MainViewModel.RefreshCommercialLocalization()</code><br>590–590 | BuildCommercialTables @590; Where @590; GetProperties @590; GetType @590; StartsWith @590; RaisePropertyChanged @590 | No extracted literal effects. |
| <span id="m-2691cdd07002"></span><code>MainViewModel.ResetCommercialWorkspace()</code><br>591–591 | Clear @591; Clear @591; Clear @591; Clear @591; Clear @591; Clear @591; Clear @591 | No extracted literal effects. |

</details>

## MainViewModel.DiagnosticsLogs.cs {#src-b96b381ea091}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.DiagnosticsLogs.cs</code> · 89 lines.

SHA-256: <code>b9520cdd5940a865491704e16fbb9eb56059cd58492eca1220b58719fdd45c97</code>.

Declarations: <code>MainViewModel</code> (line 8).

## MainViewModel.Expenses.cs {#src-849697ea5909}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Expenses.cs</code> · 1,641 lines.

SHA-256: <code>09106f06a1a1bcb5e59cf167b56e68a22ab8a629e8a24563594fbdebb3c11077</code>.

Declarations: <code>MainViewModel</code> (line 16), <code>ExpenseFormBaseline</code> (line 683).

<details markdown>
<summary>Methods, calls, table effects and failures (39)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-744647748e4a"></span><code>MainViewModel.ResetExpensesWorkspaceState()</code><br>22–53 | Increment @24; Clear @32; Clear @33; Clear @34; Clear @35; Clear @36; Dispose @38; RaisePropertyChanged @40; nameof @40 | No extracted literal effects. |
| <span id="m-41efb98304c6"></span><code>MainViewModel.ConfigureExpensePorts(IExpenseReader,IExpenseAttachmentService)</code><br>55–60 | InitializeExpensesTables @59 | No extracted literal effects. |
| <span id="m-cb463dfaf631"></span><code>MainViewModel.RaiseExpenseLabels()</code><br>81–102 | RaisePropertyChanged @83; nameof @83 | No extracted literal effects. |
| <span id="m-61c3a434cf89"></span><code>MainViewModel.ExpenseNextPage()</code><br>213–216 | NextPage @215 | No extracted literal effects. |
| <span id="m-f8e98a293cfe"></span><code>MainViewModel.ExpensePreviousPage()</code><br>218–221 | PreviousPage @220 | No extracted literal effects. |
| <span id="m-2ff09a7da5be"></span><code>MainViewModel.InitializeExpensesTables()</code><br>228–232 | BindRefresh @230; LoadExpenseRowsAsync @230; BuildExpensesTable @231 | No extracted literal effects. |
| <span id="m-26f46318f352"></span><code>MainViewModel.BuildExpensesTable()</code><br>234–300 | CreateColumns @241; TextColumn @242; Localize @242; ToString @248; ToDisplayAmount @248; ToLocalTime @261; LocalizeTable @288; Max @296; Ceiling @296; RaisePropertyChanged @299; nameof @299 | No extracted literal effects. |
| <span id="m-3584e10ad1c4"></span><code>MainViewModel.LoadExpensesWorkspaceAsync(CancellationToken)</code><br>322–354 | EnsurePaymentAccountsLoadedAsync @324; ConfigureAwait @325; LoadExpenseCategoriesAsync @325; LoadExpenseRowsAsync @326; RaisePropertyChanged @331; nameof @331; DispatchToUi @337; RefreshExpenseFormCategories @339; FirstOrDefault @342 | No extracted literal effects. |
| <span id="m-837b51e741a4"></span><code>MainViewModel.LoadExpenseRowsAsync(CancellationToken)</code><br>356–396 | Read @359; ToPageRequest @364; ConfigureAwait @370; GetExpensesAsync @370; DispatchToUi @375; ApplyPagedResult @380; Clear @381; Add @384 | No extracted literal effects. |
| <span id="m-581366c7c4ce"></span><code>MainViewModel.RefreshExpenseFormCategories()</code><br>398–409 | Clear @400; Add @406 | No extracted literal effects. |
| <span id="m-79ab51f90bde"></span><code>MainViewModel.LoadExpenseCategoriesAsync(CancellationToken)</code><br>411–443 | Read @414; ConfigureAwait @418; GetCategoriesAsync @418; DispatchToUi @423; Clear @428; Add @431; RefreshExpenseFormCategories @433 | No extracted literal effects. |
| <span id="m-718cb3fa5047"></span><code>MainViewModel.LoadExpensePayeeChoicesAsync(CancellationToken)</code><br>445–473 | Read @448; ConfigureAwait @452; FindPayeesAsync @452; DispatchToUi @457; Clear @462; Add @465 | No extracted literal effects. |
| <span id="m-e69d79fe8518"></span><code>MainViewModel.SetExpenseFormAttachment(PreparedAttachment,string)</code><br>639–656 | Dispose @641; Max @645; RaisePropertyChanged @655; nameof @655 | No extracted literal effects. |
| <span id="m-5d70aeb61289"></span><code>MainViewModel.SetExpenseFormAttachmentAsync(Stream,string,string?)</code><br>658–670 | ConfigureAwait @661; PrepareAttachmentAsync @661; DispatchToUi @664; SetExpenseFormAttachment @664 | No extracted literal effects. |
| <span id="m-ce10db57bf3f"></span><code>MainViewModel.ClearExpenseFormAttachment()</code><br>672–679 | Dispose @674; RaisePropertyChanged @678; nameof @678 | No extracted literal effects. |
| <span id="m-6002630d6007"></span><code>MainViewModel.CaptureExpenseFormBaseline()</code><br>695–708 | RaisePropertyChanged @707; nameof @707 | No extracted literal effects. |
| <span id="m-5a83c9680eba"></span><code>MainViewModel.RequestCloseExpenseForm()</code><br>726–736 | CloseExpenseForm @735 | No extracted literal effects. |
| <span id="m-b1b82d704bf5"></span><code>MainViewModel.KeepEditingExpenseForm()</code><br>738–741 | — | No extracted literal effects. |
| <span id="m-c83e80d03c06"></span><code>MainViewModel.ConfirmDiscardExpenseForm()</code><br>743–747 | CloseExpenseForm @746 | No extracted literal effects. |
| <span id="m-539a66dcbd77"></span><code>MainViewModel.OpenAddExpenseModal()</code><br>749–785 | EnsurePaymentAccountsLoadedAsync @752; NewGuid @765; Clear @767; Where @768; Add @770; LoadExpensePayeeChoicesAsync @782; CaptureExpenseFormBaseline @783 | No extracted literal effects. |
| <span id="m-fc75a3b9f200"></span><code>MainViewModel.OpenEditExpenseModalAsync(Guid)</code><br>787–823 | ConfigureAwait @790; GetExpenseAsync @790; DispatchToUi @793; ToDisplayAmount @800; Clear @809; Add @814; LoadExpensePayeeChoicesAsync @819; CaptureExpenseFormBaseline @820 | No extracted literal effects. |
| <span id="m-f191bc8a6256"></span><code>MainViewModel.CloseExpenseForm()</code><br>825–831 | RaisePropertyChanged @830; nameof @830 | No extracted literal effects. |
| <span id="m-e23c8a9ab78a"></span><code>MainViewModel.SaveExpenseAsync()</code><br>840–952 | Trim @844; IsNullOrWhiteSpace @845; ToMinorUnits @857; Trim @866; NewGuid @870; ConfigureAwait(UpdateExpenseRecordCommand, bool) @889; ExecuteAsync(UpdateExpenseRecordCommand, bool) @889; DispatchToUi @892; RaisePropertyChanged @903; nameof @903; LoadExpenseRowsAsync @905; ConfigureAwait(CreateExpenseRecordCommand, Guid) @925; ExecuteAsync(CreateExpenseRecordCommand, Guid) @925 | No extracted literal effects. |
| <span id="m-43e536b1e1b0"></span><code>MainViewModel.SaveAndPayExpenseAsync()</code><br>954–1075 | Trim @958; IsNullOrWhiteSpace @959; FirstOrDefault @977; ToMinorUnits @987; Equals @994; Trim @1019; Trim @1021; NewGuid @1023; ConfigureAwait(SaveAndPayExpenseCommand, Guid) @1048; ExecuteAsync(SaveAndPayExpenseCommand, Guid) @1048; DispatchToUi @1051; RaisePropertyChanged @1062; nameof @1062; LoadExpenseRowsAsync @1064 | No extracted literal effects. |
| <span id="m-f6dec7a0806d"></span><code>MainViewModel.OpenManageExpenseCategories()</code><br>1085–1097 | RaisePropertyChanged @1094; nameof @1094; SelectMenu @1096 | No extracted literal effects. |
| <span id="m-dc4da14ab797"></span><code>MainViewModel.OpenManageExpenseCategoriesFromForm()</code><br>1099–1102 | OpenManageExpenseCategories @1101 | No extracted literal effects. |
| <span id="m-62c14c3a679e"></span><code>MainViewModel.ReturnToExpenseWorkspace()</code><br>1104–1110 | RaisePropertyChanged @1108; nameof @1108; SelectMenu @1109 | No extracted literal effects. |
| <span id="m-419ad2fb64d9"></span><code>MainViewModel.OpenCategoryManagerModal()</code><br>1132–1135 | OpenManageExpenseCategories @1134 | No extracted literal effects. |
| <span id="m-30ec092aa683"></span><code>MainViewModel.CloseExpenseCategoryModal()</code><br>1137–1140 | — | No extracted literal effects. |
| <span id="m-032b94effe04"></span><code>MainViewModel.CreateCategoryAsync()</code><br>1153–1192 | Trim @1157; IsNullOrWhiteSpace @1158; Trim @1169; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @1173; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @1173; DispatchToUi @1176; LoadExpenseCategoriesAsync @1185 | No extracted literal effects. |
| <span id="m-999baccf22fe"></span><code>MainViewModel.ToggleCategoryActiveAsync(Guid,int,string,string,bool)</code><br>1194–1226 | ConfigureAwait(UpdateExpenseCategoryCommand, bool) @1209; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @1209; DispatchToUi @1212; LoadExpenseCategoriesAsync @1219 | No extracted literal effects. |
| <span id="m-b2eeae0afd50"></span><code>MainViewModel.OpenPayExpenseModal(Guid,string,int,decimal)</code><br>1302–1308 | ToMinorUnits @1306; OpenPayExpenseModal @1307 | No extracted literal effects. |
| <span id="m-819967631e11"></span><code>MainViewModel.OpenPayExpenseModal(Guid,string,int,long,string,int)</code><br>1310–1328 | EnsurePaymentAccountsLoadedAsync @1313; Max @1320; ToDisplayAmount @1320; NewGuid @1325 | No extracted literal effects. |
| <span id="m-621dfce525ff"></span><code>MainViewModel.CloseExpensePaymentModal()</code><br>1330–1333 | — | No extracted literal effects. |
| <span id="m-1f55ae76c172"></span><code>MainViewModel.ConfirmExpensePaymentAsync()</code><br>1338–1439 | FirstOrDefault @1348; Equals @1355; IsNullOrWhiteSpace @1376; ToMinorUnits @1383; Trim @1396; Trim @1397; NewGuid @1399; ConfigureAwait(PayExpenseCommand, Guid) @1415; ExecuteAsync(PayExpenseCommand, Guid) @1415; DispatchToUi @1418; LoadExpenseRowsAsync @1428; OpenExpenseDetailModalAsync @1431 | No extracted literal effects. |
| <span id="m-4a2dea2896bc"></span><code>MainViewModel.OpenExpenseDetailModalAsync(Guid)</code><br>1490–1539 | ConfigureAwait @1495; GetExpenseAsync @1495; GetCurrentAttachmentAsync @1501; DispatchToUi @1504; Dispose @1509; Clear @1527; Add @1530 | No extracted literal effects. |
| <span id="m-93950ae8ecef"></span><code>MainViewModel.CloseExpenseDetailModal()</code><br>1541–1549 | Dispose @1544; Clear @1548 | No extracted literal effects. |
| <span id="m-85e53bebf72a"></span><code>MainViewModel.CancelExpenseAsync()</code><br>1572–1604 | ConfigureAwait(CancelExpenseRecordCommand, bool) @1586; ExecuteAsync(CancelExpenseRecordCommand, bool) @1586; DispatchToUi @1589; LoadExpenseRowsAsync @1596; OpenExpenseDetailModalAsync @1597 | No extracted literal effects. |
| <span id="m-991a0deed7b5"></span><code>MainViewModel.ReverseExpensePaymentAsync(Guid,int)</code><br>1606–1640 | ConfigureAwait(ReverseExpensePaymentCommand, Guid) @1622; ExecuteAsync(ReverseExpensePaymentCommand, Guid) @1622; DispatchToUi @1625; LoadExpenseRowsAsync @1632; OpenExpenseDetailModalAsync @1633 | No extracted literal effects. |

</details>

## MainViewModel.ImportReview.cs {#src-90113acc8bd5}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ImportReview.cs</code> · 113 lines.

SHA-256: <code>ab9c776a7cabe406f307b43ef08bb8960e663824f30b06f38cd1c5dfe5c2d967</code>.

Declarations: <code>MainViewModel</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f756c8667b34"></span><code>MainViewModel.ExportMasterDataAsync(string)</code><br>21–37 | CheckSessionUnlocked @23; ConfigureAwait @28; ExportAsync @28; DispatchToUi @29; ReferenceEquals @31; Invoke @32; SafeError @35 | No extracted literal effects. |
| <span id="m-a62e023b1fbe"></span><code>MainViewModel.MakeImportTable(string,PagedTableState&lt;ImportRowPreview&gt;,Func&lt;IReadOnlyList&lt;ImportRowPreview&gt;&gt;)</code><br>73–90 | ApplyPagedResult @75; ToArray @75; Take @75; Skip @75; rows @75; BindRefresh @76; Localize @82; ToString @83; LocalizeImportAction @85; LocalizeTable @87; Max @88; Ceiling @88 | No extracted literal effects. |
| <span id="m-85af36c6dc44"></span><code>MainViewModel.LocalizeImportAction(string)</code><br>91–97 | Localize @93; StartsWith @96 | No extracted literal effects. |
| <span id="m-d17d533504d3"></span><code>MainViewModel.RefreshImportLocalization()</code><br>98–105 | RaisePropertyChanged @100; nameof @100; ApplyPagedResult @104; ToArray @104 | No extracted literal effects. |
| <span id="m-58392d80041f"></span><code>MainViewModel.SetImportReviewRows(bool,IReadOnlyList&lt;ImportRowPreview&gt;)</code><br>106–112 | ApplyPagedResult @111; ToArray @111; Take @111 | No extracted literal effects. |

</details>

## MainViewModel.InventoryTraceability.cs {#src-f3c9eb6aacd1}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.InventoryTraceability.cs</code> · 237 lines.

SHA-256: <code>b09a0d533ed6bacda421abaef00bd2698292410eeac72c6e03811bc629c3d9fb</code>.

Declarations: <code>MainViewModel</code> (line 13).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-ae2e0c6852eb"></span><code>MainViewModel.TraceText(string)</code><br>79–79 | Localize @79 | No extracted literal effects. |
| <span id="m-a70f2a794771"></span><code>MainViewModel.InitializeProductTraceability()</code><br>81–87 | Register @83; BindRefresh @84; LoadProductTraceabilityAsync @84; BindRefresh @85; BuildProductTraceabilityTables @86 | No extracted literal effects. |
| <span id="m-c65b706851b5"></span><code>MainViewModel.BuildProductTraceabilityTables()</code><br>88–118 | ToString @93; TextColumn @95; TraceText @95; LocalizeTable @113; Localize @113; Max @116; Ceiling @116 | No extracted literal effects. |
| <span id="m-d5764a736229"></span><code>MainViewModel.ResetProductTraceability()</code><br>119–125 | Clear @122; Clear @122; ResetToFirstPage @122; ResetToFirstPage @122; ClearSelection @123; Clear @123; RaiseTraceabilityState @124 | No extracted literal effects. |
| <span id="m-305861034f13"></span><code>MainViewModel.RaiseTraceabilityState()</code><br>126–130 | nameof @128; RaisePropertyChanged @129 | No extracted literal effects. |
| <span id="m-c07294422d97"></span><code>MainViewModel.RefreshTraceabilityLocalization()</code><br>131–138 | BuildProductTraceabilityTables @133; RaisePropertyChanged @134; nameof @134; Where @136; GetProperties @136; GetType @136; StartsWith @136 | No extracted literal effects. |
| <span id="m-69ffe9e0fe93"></span><code>MainViewModel.LoadProductTraceabilityAsync()</code><br>139–163 | GetLotsAsync @148; ToPageRequest @148; DispatchToUi @149; ApplyPagedResult @149; GetSerialsAsync @153; ToPageRequest @153; ApplyPagedResult @157; SafeError @162 | No extracted literal effects. |
| <span id="m-aa95b2f13dc5"></span><code>MainViewModel.ParseTraceabilitySerials()</code><br>164–164 | Split @164 | No extracted literal effects. |
| <span id="m-902524558d4e"></span><code>MainViewModel.TraceabilityDraftSnapshot()</code><br>165–165 | Serialize @165 | No extracted literal effects. |
| <span id="m-5b09f84076fd"></span><code>MainViewModel.InvalidateTraceabilityPreview()</code><br>166–166 | RaisePropertyChanged @166; nameof @166 | No extracted literal effects. |
| <span id="m-ed77e846432f"></span><code>MainViewModel.OpenTraceabilityEditor(string,LotStockRow?)</code><br>167–182 | CheckSessionUnlocked @169; ToList @175; Select @175; Where @175; GetSelectedIdsForPreview @175; TraceText @177; ToString @178; NewGuid @178; TraceabilityDraftSnapshot @178; nameof @179; RaisePropertyChanged @180 | No extracted literal effects. |
| <span id="m-d8dc483b4954"></span><code>MainViewModel.RequestCloseTraceability()</code><br>183–188 | TraceabilityDraftSnapshot @186 | No extracted literal effects. |
| <span id="m-fd569d0970d8"></span><code>MainViewModel.ConfirmTraceabilityAsync()</code><br>189–236 | CheckSessionUnlocked @191; ParseTraceabilitySerials @193; IsNullOrWhiteSpace @194; Count @196; Distinct @196; TraceText @198; RaisePropertyChanged @200; nameof @200; SpecifyKind @206; AddTicks @206; AddDays @206; ExecuteAsync(SetLotStockQuantityCommand, LotStockRow) @209; Trim @209; ExecuteAsync(UpdateLotExpiryCommand, LotStockRow) @214; ExecuteAsync(RemoveInventorySerialsCommand, int) @219; Trim @224; ToArray @225; Select @225; Sum @226; ExecuteAsync(ReceiveStockCommand, StockMovement) @227; SafePipelineError @230; ClearSelection @231; Clear @231; LoadInventoryAsync @232; LoadItemHistoryAsync @232; LoadProductTraceabilityAsync @232; SafeError @234 | No extracted literal effects. |

</details>

## MainViewModel.Invoices.cs {#src-b3daabd12c31}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Invoices.cs</code> · 399 lines.

SHA-256: <code>f3f8479bc3da9cd91a5eb520040ca1d678a641d79619fff9f94b97c2f872498c</code>.

Declarations: <code>InvoiceChoice</code> (line 18), <code>ReturnStockEditor : ReactiveObject</code> (line 19), <code>ReturnLineEditor : ReactiveObject</code> (line 29), <code>CollectionEditor : ReactiveObject</code> (line 37), <code>MainViewModel</code> (line 47).

<details markdown>
<summary>Methods, calls, table effects and failures (23)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b388b3bd0aba"></span><code>InvoiceChoice.ToString()</code><br>18–18 | — | No extracted literal effects. |
| <span id="m-2ac9169eb3e5"></span><code>MainViewModel.FinancialIdentityMatches(Guid,long)</code><br>51–51 | — | No extracted literal effects. |
| <span id="m-692451a54b95"></span><code>MainViewModel.ResetFinancialWorkspace()</code><br>52–65 | ResetCommercialWorkspace @54; Clear @57; Clear @57; Clear @57; Clear @57; ClearSelection @58; ClearSelection @58; Clear @61; ClearFinancialReceiptImages @61; ResetTeamMemberFormState @62; ResetSalaryWorkspaceState @63; ResetExpensesWorkspaceState @64 | No extracted literal effects. |
| <span id="m-b74c39788ee3"></span><code>MainViewModel.ConfigureInvoiceReader(IInvoiceAndRegisterReader)</code><br>193–193 | — | No extracted literal effects. |
| <span id="m-c87342a2c508"></span><code>MainViewModel.InitializeInvoiceWorkspace()</code><br>194–216 | CreateFromTask @197; CreateFromTask(InvoiceBalance) @199; Create @201; Clear @201; Add @201; OpenInvoiceOperation @201; CheckSessionUnlocked @202; InvoiceEditorState @204; AllocateOldestFirst @208; Select @208; FirstOrDefault @208; SafeError @208; CreateFromTask(FinancialRegisterRow) @209; BindRefresh @212; LoadInvoicesAsync @212; BindRefresh @212; LoadFinancialRegisterAsync @212; Register @213; Execute @213; BuildInvoiceTables @215 | No extracted literal effects. |
| <span id="m-6b9aa13193cf"></span><code>MainViewModel.InvoiceMoney(long,string)</code><br>217–217 | ToString @217; ToDecimal @217 | No extracted literal effects. |
| <span id="m-fa33649e2003"></span><code>MainViewModel.InvoiceMoney(long,string,int?)</code><br>218–218 | ToString @218; ToDecimal @218; Localize @218 | No extracted literal effects. |
| <span id="m-775cd9af9dbb"></span><code>MainViewModel.InvoiceTime(DateTime,string)</code><br>219–224 | ToString @221; ConvertTimeFromUtc @221; SpecifyKind @221; FindSystemTimeZoneById @221; ToString @222 | No extracted literal effects. |
| <span id="m-c2e2dd270d15"></span><code>MainViewModel.Choices()</code><br>226–226 | ToArray(T) @226; Select(T) @226; GetValues(T) @226; Localize @226 | No extracted literal effects. |
| <span id="m-d3798771e182"></span><code>MainViewModel.BuildInvoiceTables()</code><br>227–238 | TextColumn @229; Localize @229; read @229; ToString @230; OpenCollectionAsync @230; HasPermission @230; Max @230; Ceiling @230; Column @231; InvoiceTime @231; InvoiceMoney @231; LocalizeTable @231; RemoveAll @233; RaisePropertyChanged @237; nameof @237 | No extracted literal effects. |
| <span id="m-9017d9bc4580"></span><code>MainViewModel.LoadInvoicesAsync()</code><br>239–246 | SetSelectionScope @243; GetInvoicesAsync @244; ToPageRequest @244; DispatchToUi @244; FinancialIdentityMatches @244; ApplyPagedResult @244; SafeError @245 | No extracted literal effects. |
| <span id="m-7f5cdf5e6557"></span><code>MainViewModel.LoadFinancialRegisterAsync()</code><br>247–262 | TryParseExact @253; ParseDate @256; Localize @257; GetRegisterAsync @258; ToPageRequest @258; DispatchToUi @259; FinancialIdentityMatches @259; ApplyPagedResult @259; Join @259; Select @259; InvoiceMoney @259; Select @259; SafeError @261 | No extracted literal effects. |
| <span id="m-b1a4d88b5e09"></span><code>MainViewModel.OpenInvoiceAsync(InvoiceBalance)</code><br>263–269 | GetInvoiceAsync @267; DispatchToUi @267; FinancialIdentityMatches @267; RaisePropertyChanged @267; nameof @267; OpenInvoiceOperation @267; RecordSuccessfulSearchUseAsync @267; FromGuid @267; SafeError @268 | No extracted literal effects. |
| <span id="m-7ba15509e22e"></span><code>MainViewModel.OpenCollectionAsync()</code><br>270–278 | GetSelectedIdsForPreview @273; GetSelectedInvoicesAsync @276; ToArray @276; Select @276; DispatchToUi @276; FinancialIdentityMatches @276; Clear @276; Where @276; Add @276; OpenInvoiceOperation @276; SafeError @277 | No extracted literal effects. |
| <span id="m-92c42bc006f8"></span><code>MainViewModel.OpenInvoiceOperation(string)</code><br>279–285 | ToString @282; NewGuid @282; nameof @283; RaisePropertyChanged @283; InvoiceEditorState @284 | No extracted literal effects. |
| <span id="m-b6d796cce4e1"></span><code>MainViewModel.InvoiceEditorState()</code><br>286–286 | Serialize @286; Select @286; Select @286; Select @286 | No extracted literal effects. |
| <span id="m-ebb02e1d92f4"></span><code>MainViewModel.ReturnCommand()</code><br>287–287 | ToArray @287; Select @287; Where @287; Where @287 | No extracted literal effects. |
| <span id="m-c89e1168c40c"></span><code>MainViewModel.InvoiceConfirmation(long,string)</code><br>288–288 | Trim @288 | No extracted literal effects. |
| <span id="m-aede3915d892"></span><code>MainViewModel.PreviewInvoiceReturnAsync()</code><br>289–313 | RaisePropertyChanged @295; nameof @295; Validate @301; ToArray @301; Select @301; Select @302; Where @302; InvoiceMoney @303; InvoiceEditorState @304; SafeError @306; ReturnCommand @310; PreviewReturnAsync @311; DispatchToUi @311; FinancialIdentityMatches @311; Localize @311; SafePipelineError @311 | No extracted literal effects. |
| <span id="m-12c424210b86"></span><code>MainViewModel.OpenRegisterRowAsync(FinancialRegisterRow)</code><br>314–329 | OpenInvoiceOperation @320; RecordSuccessfulSearchUseAsync @320; FromGuid @320; GetRegisterSourceAsync @322; FinancialIdentityMatches @323; GetInvoiceAsync @324; OpenInvoiceAsync @324; DispatchToUi @325; Join @325; Select @325; Localize @325; InvoiceMoney @325; SafeError @328 | No extracted literal effects. |
| <span id="m-ad1e65790bc0"></span><code>MainViewModel.SaveInvoiceDialogAsync()</code><br>330–380 | CheckSessionUnlocked @332; InvoiceEditorState @333; Localize @333; IsNullOrWhiteSpace @341; TryParseExact @341; InvoiceConfirmation @342; CreateInvoiceDepositTender @343; Empty(SalesTender) @343; ExecuteAsync(IssueDeferredInvoiceCommand, SalesInvoice) @344; FinancialIdentityMatches @345; DispatchToUi @345; Clear @345; RestoreActiveCartAsync @345; LoadInventoryAsync @345; SafeError @345; FirstOrDefault @347; ExecuteAsync(ReceiveInvoicePaymentCommand, InvoiceCollectionResult) @349; ToArray @349; Select @349; Where @349; ReturnCommand @353; ExecuteAsync(ProcessReturnCommand, SaleReturnResult) @356; ExecuteAsync(ResolveInspectionCommand, InspectionResolutionResult) @360; ExecuteAsync(RecordKnownCashLossCommand, CashLossResult) @364; ExecuteAsync(CorrectCashLossRecordCommand, CashLossResult) @368; SafePipelineError @370; ToString @370; NewGuid @370; LoadInvoicesAsync @371; LoadFinancialRegisterAsync @371; LoadReportDataAsync @374 | InvalidOperationException @341 |
| <span id="m-39faa7fce6e5"></span><code>MainViewModel.CreateInvoiceDepositTender(TenderType,long,string,ManualPaymentConfirmation?)</code><br>381–386 | Zero @383; Trim @384 | No extracted literal effects. |
| <span id="m-171f36b2d689"></span><code>MainViewModel.RaiseInvoiceLabels()</code><br>387–392 | nameof @390; RaisePropertyChanged @390; BuildInvoiceTables @391 | No extracted literal effects. |

</details>

## MainViewModel.ItemHistory.cs {#src-97d7fd82738a}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ItemHistory.cs</code> · 380 lines.

SHA-256: <code>1d5b134b53c7dfc5f0357caf736655df4056820d96284eeac2c8506cc54e8dfb</code>.

Declarations: <code>MainViewModel</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (18)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9692eb79775b"></span><code>MainViewModel.EditedStockItem()</code><br>37–38 | FirstOrDefault @38; Concat @38 | No extracted literal effects. |
| <span id="m-13f8d8245d85"></span><code>MainViewModel.ResetProductStockDraft()</code><br>41–48 | ResetProductTraceability @43 | No extracted literal effects. |
| <span id="m-fc9fb189c283"></span><code>MainViewModel.ApplyProductStockChangeAsync()</code><br>55–84 | CheckSessionUnlocked @57; ConfigureAwait @64; SaveProductConfigurationAsync @64; Trim @69; ToString @70; NewGuid @70; ConfigureAwait(AdjustStockCommand, StockMovement) @71; ExecuteAsync(AdjustStockCommand, StockMovement) @71; DispatchToUi @73; SafePipelineError @73; LoadInventoryAsync @79; LoadItemHistoryAsync @80; SafeError @82 | No extracted literal effects. |
| <span id="m-a506f704b2b9"></span><code>MainViewModel.InitializeItemHistoryTables()</code><br>155–196 | BindRefresh @157; LoadItemHistoryAsync @157; BindRefresh @158; LoadItemPriceHistoryAsync @158; ToString @162; Column @165; ToLocalTime @165; MovementName @166; Delta @168; EnteredQuantityText @171; Localize @172; RouteText @173; MoneyText @186; PriceNewText @187; PriceSourceText @189; RaisePropertyChanged @194; nameof @194 | No extracted literal effects. |
| <span id="m-b6edab369d7c"></span><code>MainViewModel.LoadItemHistoryAsync(bool)</code><br>198–236 | ResetToFirstPage @202; DispatchToUi @203; ConfigureAwait @206; GetItemStockHistoryAsync @206; ToPageRequest @206; RaisePropertyChanged @213; nameof @213; Localize @217; ApplyPagedResult @218; GetTraceabilitySummaryAsync @222; ApplyItemTraceabilitySummary @225; LoadProductTraceabilityAsync @226; SafeError @230 | No extracted literal effects. |
| <span id="m-94066839a947"></span><code>MainViewModel.LoadItemPriceHistoryAsync()</code><br>238–252 | ConfigureAwait @244; GetHistoryAsync @244; ToPageRequest @244; DispatchToUi @246; ApplyPagedResult @246; SafeError @250; Localize @250 | No extracted literal effects. |
| <span id="m-0676721a8812"></span><code>MainViewModel.ClearItemHistory()</code><br>254–273 | ApplyPagedResult @259; ApplyPagedResult @260; Clear @264; Clear @265; Clear @266; RaisePropertyChanged @267; nameof @267 | No extracted literal effects. |
| <span id="m-f734955060b1"></span><code>MainViewModel.ApplyItemTraceabilitySummary(ItemTraceabilitySummaryProjection)</code><br>275–310 | Clear @277; ToString @280; ToLocalTime @280; Localize @281; Add @282; Format @282; ToString @284; Clear @290; Add @292; Clear @296; Add @298; RaisePropertyChanged @304; nameof @304 | No extracted literal effects. |
| <span id="m-ff876b9af548"></span><code>MainViewModel.LoadExactProductCostSnapshotsAsync(Guid)</code><br>312–353 | CreateCommand @321; CreateParameter @326; ToString @328; Add @329; ConfigureAwait @330; ExecuteReaderAsync @330; ReadAsync @331; ReadDecimal @333; DispatchToUi @339; RaisePropertyChanged @345; nameof @345 | FROM items @322 |
| <span id="m-fb4dcbf1bef1"></span><code>MainViewModel.Column(string,Func&lt;object, string&gt;,double)</code><br>355–355 | Localize @355 | No extracted literal effects. |
| <span id="m-75b66ba0da94"></span><code>MainViewModel.MoneyText(long?)</code><br>356–356 | Format @356; ToDecimal @356 | No extracted literal effects. |
| <span id="m-d6822bdf4d5f"></span><code>MainViewModel.PriceNewText(ItemPriceHistoryRow)</code><br>357–357 | MoneyText @357 | No extracted literal effects. |
| <span id="m-ad723d075314"></span><code>MainViewModel.PriceSourceText(ItemPriceHistoryRow)</code><br>358–361 | — | No extracted literal effects. |
| <span id="m-91087fbaef88"></span><code>MainViewModel.Delta(decimal,bool)</code><br>362–362 | ToString @362; ToString @362 | No extracted literal effects. |
| <span id="m-ae2f4ec3176e"></span><code>MainViewModel.EnteredQuantityText(ItemStockHistoryRow)</code><br>363–368 | — | No extracted literal effects. |
| <span id="m-aea697dda7dd"></span><code>MainViewModel.RouteText(ItemStockHistoryRow)</code><br>369–369 | — | No extracted literal effects. |
| <span id="m-f5172edfaeae"></span><code>MainViewModel.ReadDecimal(System.Data.Common.DbDataReader,int)</code><br>370–373 | IsDBNull @371; TryParse @371; GetString @371 | No extracted literal effects. |
| <span id="m-77c7cfd2e288"></span><code>MainViewModel.MovementName(int)</code><br>374–379 | Localize @374 | No extracted literal effects. |

</details>

## MainViewModel.Keyboard.cs {#src-260122c13e33}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Keyboard.cs</code> · 32 lines.

SHA-256: <code>c09ee0b4afcb9f4c84df7a21c84f179e41d994c4522b203f6db604c0f5273002</code>.

Declarations: <code>MainViewModel</code> (line 5).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-72bd2d6532fa"></span><code>MainViewModel.TryHandleEscapeKey()</code><br>11–31 | TryHandleEscape @15; Execute @28 | No extracted literal effects. |

</details>

## MainViewModel.PricingWorkflows.cs {#src-391f51781612}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.PricingWorkflows.cs</code> · 456 lines.

SHA-256: <code>1880b3b80c289340c113ec90558bec07d47bc46fa9c2130d306d5dc9b9262bd3</code>.

Declarations: <code>PricingRunPolicyOption</code> (line 12), <code>PricingRunCategoryOption</code> (line 13), <code>PricingRunPreviewDisplayRow</code> (line 14), <code>PricingRunRecoveryOption</code> (line 16), <code>PricingRunWorkflowOption</code> (line 18), <code>PricingTierOperationOption</code> (line 19), <code>PricingTierOperationEditor : ReactiveObject</code> (line 21), <code>MainViewModel</code> (line 64).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-bbfd544f7653"></span><code>MainViewModel.OpenPricingRunAsync()</code><br>245–258 | Clear @248; FirstOrDefault @249; Equals @250; ResetPricingTierOperations @255; ConfigureAwait @257; LoadActivePricingRunsAsync @257 | No extracted literal effects. |
| <span id="m-e82983bc9bb4"></span><code>MainViewModel.SetPricingRunWorkflow(string)</code><br>266–277 | Localize @272 | No extracted literal effects. |
| <span id="m-d22abe02ac2b"></span><code>MainViewModel.ResetPricingTierOperations()</code><br>278–291 | Clear @281; OrderBy @282; Where @282; Add @288; InvalidatePricingRunPreview @290 | No extracted literal effects. |
| <span id="m-05a7b78882b2"></span><code>MainViewModel.OnPricingTierOperationChanged(object?,System.ComponentModel.PropertyChangedEventArgs)</code><br>292–295 | InvalidatePricingRunPreview @294 | No extracted literal effects. |
| <span id="m-76e437c48d84"></span><code>MainViewModel.InvalidatePricingRunPreview()</code><br>302–306 | Clear @305 | No extracted literal effects. |
| <span id="m-d2e973029ab5"></span><code>MainViewModel.BuildPricingRunConfiguration(string?)</code><br>308–317 | ToMinorUnits @310; EffectivePricingRunCategoryId @311; ToArray @313; Where @313; Select @313; GetSelectedIdsForPreview @313; TryParse @314; BuildTierOperations @317 | No extracted literal effects. |
| <span id="m-306485307b00"></span><code>MainViewModel.BuildTierOperations()</code><br>319–322 | ToArray @319; Select @319; ToMinorUnits @321 | No extracted literal effects. |
| <span id="m-382d93fdb141"></span><code>MainViewModel.EffectivePricingRunCategoryId()</code><br>324–324 | — | No extracted literal effects. |
| <span id="m-d019742030f3"></span><code>MainViewModel.CreatePricingRunPreviewAsync()</code><br>326–350 | CheckSessionUnlocked @328; GetSelectedIdsForPreview @329; Localize @330; InvalidatePricingRunPreview @333; ConfigureAwait(PreviewPricingMassRunCommand, PricingMassRunPreviewDto) @334; ExecuteAsync(PreviewPricingMassRunCommand, PricingMassRunPreviewDto) @334; BuildPricingRunConfiguration @335; DispatchToUi @336; SafePipelineError @338; Clear @339; Add @341; FormatPricingRunMinor @341; Join @343; Select @343; SafeError @348 | No extracted literal effects. |
| <span id="m-a838f1440c33"></span><code>MainViewModel.FormatPricingRunMinor(long)</code><br>352–353 | ToString @353; ToDisplayAmount @353 | No extracted literal effects. |
| <span id="m-8df13c631251"></span><code>MainViewModel.StartPricingRunAsync()</code><br>355–377 | CheckSessionUnlocked @357; BuildPricingRunConfiguration @361; ToString @361; NewGuid @361; ConfigureAwait(CreatePricingMassRunCommand, Guid) @362; ExecuteAsync(CreatePricingMassRunCommand, Guid) @362; DispatchToUi @364; SafePipelineError @366; RaisePropertyChanged @369; nameof @369; Localize @370; ConfigureAwait @373; LoadActivePricingRunsAsync @373; SafeError @375 | No extracted literal effects. |
| <span id="m-0a23b69eec4b"></span><code>MainViewModel.ControlPricingRunAsync(string)</code><br>379–420 | CheckSessionUnlocked @381; ConfigureAwait(ProcessPricingMassRunCycleCommand, PricingMassRunCycleResult) @388; ExecuteAsync(ProcessPricingMassRunCycleCommand, PricingMassRunCycleResult) @388; DispatchToUi @390; SafePipelineError @392; RaisePropertyChanged @396; nameof @396; Localize @397; ConfigureAwait @400; LoadActivePricingRunsAsync @400; LoadInventoryAsync @402; ConfigureAwait(SetPricingMassRunControlCommand, bool) @406; ExecuteAsync(SetPricingMassRunControlCommand, bool) @406; SafeError @418 | No extracted literal effects. |
| <span id="m-935dcb759c31"></span><code>MainViewModel.LoadActivePricingRunsAsync(Guid?)</code><br>422–453 | CreateCommand @428; ConfigureAwait @432; ExecuteReaderAsync @432; ReadAsync @433; Parse @435; GetString @435; GetInt32 @436; Add @437; DispatchToUi @439; Clear @441; Add @442; RaisePropertyChanged @443; nameof @443; FirstOrDefault @444; SafeError @452 | FROM pricing_mass_runs @429 |

</details>

## MainViewModel.ProductionWorkspace.cs {#src-0ca7e312d4b8}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ProductionWorkspace.cs</code> · 662 lines.

SHA-256: <code>3affdb93d62b64846e52993978138310020f03dcfda43775b46c1e91d54fbcef</code>.

Declarations: <code>ProductionIngredientLotDraft : ReactiveObject</code> (line 18), <code>MainViewModel</code> (line 36).

<details markdown>
<summary>Methods, calls, table effects and failures (16)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-cd3625b68ce8"></span><code>MainViewModel.InitializeManufacturingWorkspace()</code><br>190–238 | CreateFromTask @192; CreateFromTask(object) @193; OpenProductionRunByIdAsync @195; GetProductionRunDetailForActionAsync @209; CancelProductionDraftAsync @210; Create @219; Register @230; BindRefresh @231; RefreshManufacturingTablesAsync @231; BindRefresh @232; BuildManufacturingTableDefinitions @237 | No extracted literal effects. |
| <span id="m-da0f52ec4e69"></span><code>MainViewModel.GetProductionRunDetailForActionAsync(Guid)</code><br>240–248 | GetProductionRunDetailAsync @245; FirstOrDefault @247 | No extracted literal effects. |
| <span id="m-4998c32e64b6"></span><code>MainViewModel.BuildManufacturingTableDefinitions()</code><br>250–301 | ToString @257; CreateFromTask(RecipeRow) @258; OpenNewProductionByRecipeIdAsync @260; TextColumn @264; Localize @264; CreateFromTask(ProductionRunRow) @279; OpenProductionRunByIdAsync @281; ToLocalTime @285; LocalizeTable @294; Max @299; Ceiling @299 | No extracted literal effects. |
| <span id="m-90e7ad5f4118"></span><code>MainViewModel.RefreshManufacturingLocalization()</code><br>303–317 | nameof @306; RaisePropertyChanged @312; BuildManufacturingTableDefinitions @314 | No extracted literal effects. |
| <span id="m-1f0c2529e94e"></span><code>MainViewModel.RefreshManufacturingTablesAsync()</code><br>319–379 | WaitAsync @321; GetRecipesAsync @327; ToPageRequest @329; GetProductionRunsAsync @333; ToPageRequest @335; DispatchToUi @340; ApplyPagedResult @340; ApplyPagedResult @340; ToList @344; Select @344; Where @344; Join @346; Select @346; Where @349; IsNullOrWhiteSpace @351; Contains @354; Contains @355; Contains @356; Where @359; Where @363; Contains @368; Take @372; Skip @372; Skip @373; RaisePropertyChanged @375; nameof @375; SafeError @377; Release @378 | No extracted literal effects. |
| <span id="m-adc07086792b"></span><code>MainViewModel.SetProductionActionMode(string)</code><br>381–385 | RaiseProductionStateChanged @384 | No extracted literal effects. |
| <span id="m-38d336eaeb2d"></span><code>MainViewModel.ProductionModalSnapshot()</code><br>387–399 | Join @390; ToString @393; ToString @394; ToString @395; Trim @396; Select @398 | No extracted literal effects. |
| <span id="m-e8f8f44cde4d"></span><code>MainViewModel.TakeProductionSnapshot()</code><br>401–405 | ProductionModalSnapshot @403; RaiseProductionStateChanged @404 | No extracted literal effects. |
| <span id="m-527529237687"></span><code>MainViewModel.RaiseProductionStateChanged()</code><br>417–448 | nameof @421; RaisePropertyChanged @446 | No extracted literal effects. |
| <span id="m-ea930511912e"></span><code>MainViewModel.OpenProductionRunByIdAsync(Guid,string?)</code><br>450–487 | CheckSessionUnlocked @452; GetProductionRunDetailAsync @458; GetRecipeDetailAsync @460; FirstOrDefault @464; FirstOrDefault @466; Localize @471; RecordSuccessfulSearchUseAsync @476; FromGuid @476; OpenExistingProductionAsync @486 | No extracted literal effects. |
| <span id="m-13c559954127"></span><code>MainViewModel.OpenNewProductionByRecipeIdAsync(Guid)</code><br>489–510 | CheckSessionUnlocked @491; GetRecipeDetailAsync @496; FirstOrDefault @500; Localize @505; OpenProductionModal @509 | No extracted literal effects. |
| <span id="m-8b98c18c2a70"></span><code>MainViewModel.OpenExistingProductionAsync(ProductionRunDto,string,BomDto?)</code><br>512–547 | CheckSessionUnlocked @514; FirstOrDefault @518; GetRecipeDetailAsync @522; RaisePropertyChanged @527; nameof @527; SetProductionActionMode @528; Clear @540; TakeProductionSnapshot @541; LoadProductionIngredientLotsAsync @545 | No extracted literal effects. |
| <span id="m-3acb20ecea0c"></span><code>MainViewModel.LoadProductionIngredientLotsAsync()</code><br>549–576 | Clear @551; RaisePropertyChanged @554; nameof @554; DistinctBy @559; GetLotCandidatesAsync @561; Add @570; Add @571; SafeError @574 | No extracted literal effects. |
| <span id="m-9493dc9caf73"></span><code>MainViewModel.SaveProductionDraftAsync()</code><br>578–604 | CheckSessionUnlocked @580; Localize @583; ExecuteAsync(CreateProductionDraftCommand, ProductionRunDto) @591; SafePipelineError @593; RecordSuccessfulSearchUseAsync @597; FromGuid @597; LoadManufacturingDataAsync @599; SafeError @602 | No extracted literal effects. |
| <span id="m-2790bddb629c"></span><code>MainViewModel.ExecuteExistingProductionAsync()</code><br>606–642 | CheckSessionUnlocked @608; Localize @611; ExecuteAsync(StageProductionRunCommand, ProductionRunDto) @631; ToDictionary @632; Where @632; ExecuteAsync(CompleteProductionRunCommand, ProductionRunDto) @633; SafePipelineError @635; LoadManufacturingDataAsync @636; LoadInventoryAsync @637; SafeError @640 | No extracted literal effects. |
| <span id="m-0ae788bfdf35"></span><code>MainViewModel.CancelProductionDraftAsync(ProductionRunDto)</code><br>644–661 | CheckSessionUnlocked @646; Localize @649; ExecuteAsync(CancelProductionRunCommand, bool) @655; LoadManufacturingDataAsync @656; SafePipelineError @657; SafeError @659 | No extracted literal effects. |

</details>

## MainViewModel.ReceiptManagement.cs {#src-3872b07af065}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ReceiptManagement.cs</code> · 222 lines.

SHA-256: <code>6cdcd7582e12d5ece52f887ce1a09530076e4e365e07cb677e1c481d1aa7042a</code>.

Declarations: <code>FinancialReceiptPreviewPage</code> (line 14), <code>MainViewModel</code> (line 16).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-bbcea3187936"></span><code>MainViewModel.ClearFinancialReceiptImages()</code><br>60–64 | Dispose @62; Clear @63 | No extracted literal effects. |
| <span id="m-fef8b472f6b7"></span><code>MainViewModel.OpenManageReceiptsAsync()</code><br>104–112 | CheckSessionUnlocked @106; Clear @109; ConfigureAwait @111; LoadReceiptsAsync @111 | No extracted literal effects. |
| <span id="m-5da4f32ba660"></span><code>MainViewModel.LoadReceiptsAsync()</code><br>114–137 | ConfigureAwait @121; GetReceiptsAsync @121; DispatchToUi @122; FinancialIdentityMatches @124; Clear @125; Add @126; FirstOrDefault @129; SafeError @135 | No extracted literal effects. |
| <span id="m-82eda9f7158a"></span><code>MainViewModel.LoadSelectedReceiptLinesAsync(string?)</code><br>139–177 | IsNullOrWhiteSpace @143; DispatchToUi @145; Clear @145; Clear @145; ClearFinancialReceiptImages @145; RaisePropertyChanged @145; nameof @145; ConfigureAwait @151; GetReceiptLinesAsync @151; GetFinancialPreviewAsync @152; GetFinancialPreviewImagesAsync @153; FinancialIdentityMatches @156; Add @158; Add @159; Add @163; TryParse @166; RecordSuccessfulSearchUseAsync @169; FromGuid @169; SafeError @175 | No extracted literal effects. |
| <span id="m-e04e4bda9395"></span><code>MainViewModel.ReprintSelectedReceiptAsync()</code><br>179–219 | CheckSessionUnlocked @182; ConfigureAwait(QueueReceiptReprintCommand, string) @193; ExecuteAsync(QueueReceiptReprintCommand, string) @193; IsNullOrWhiteSpace @195; DispatchToUi @197; FinancialIdentityMatches @197; SafePipelineError @197; Min @205; ConfigureAwait @209; LoadReceiptsAsync @209; SafeError @213 | No extracted literal effects. |

</details>

## MainViewModel.Recipes.cs {#src-c1bc941cef14}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Recipes.cs</code> · 229 lines.

SHA-256: <code>a624de1baae659cb08a186c8497c2f8ad66e0a1ee7d11c8dbf6a71f8ad880e7d</code>.

Declarations: <code>RecipeIngredientDraft : ReactiveObject</code> (line 12), <code>MainViewModel</code> (line 24).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-48b502f331c1"></span><code>MainViewModel.RecipeSnapshot()</code><br>118–119 | Serialize @118; Select @119 | No extracted literal effects. |
| <span id="m-3af204c36c02"></span><code>MainViewModel.RequestCloseRecipe()</code><br>121–126 | RecipeSnapshot @124 | No extracted literal effects. |
| <span id="m-f79f6deaec4e"></span><code>MainViewModel.OpenRecipeEditorByIdAsync(Guid)</code><br>128–145 | CheckSessionUnlocked @130; GetRecipeDetailAsync @135; FirstOrDefault @139; OpenRecipeEditorAsync @143 | No extracted literal effects. |
| <span id="m-eabacf79a8c0"></span><code>MainViewModel.OpenRecipeEditorAsync(BomDto?)</code><br>147–171 | CheckSessionUnlocked @149; RaisePropertyChanged @151; nameof @151; FirstOrDefault @154; Clear @156; Add @159; Clear @162; RecipeSnapshot @164; LoadRecipeChoicesAsync @165; RecordSuccessfulSearchUseAsync @169; FromGuid @169 | No extracted literal effects. |
| <span id="m-f16c1b33119c"></span><code>MainViewModel.LoadRecipeChoicesAsync()</code><br>173–200 | ToList @180; Take @180; Where @180; Contains @180; GetPagedInventoryItemsAsync @183; Select @186; Where @186; DispatchToUi @189; Cast(InventoryItem) @192; Where @192; Append @192; Select @192; DistinctBy @193; Concat @193; Any @195; Add @195; Where @196; All @196; Remove @196; SafeError @199 | No extracted literal effects. |
| <span id="m-5b7e0157226b"></span><code>MainViewModel.SaveRecipeAsync()</code><br>202–228 | CheckSessionUnlocked @204; IsNullOrWhiteSpace @206; Any @207; Localize @208; Count @209; Distinct @209; Select @209; ToList @217; Trim @217; ExecuteAsync(CreateBomCommand, BomDto) @220; Trim @220; ExecuteAsync(UpdateBomCommand, BomDto) @221; DispatchToUi @222; SafePipelineError @222; LoadManufacturingDataAsync @223; SafeError @226 | No extracted literal effects. |

</details>

## MainViewModel.ReturnsAndWaste.cs {#src-71e9030a9a8d}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ReturnsAndWaste.cs</code> · 481 lines.

SHA-256: <code>7100dbb242728b22504a4c0c6dcbd811e86c38c93a24461c1ebc327cc3c3cfab</code>.

Declarations: <code>MainViewModel</code> (line 19).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-754ed1718afb"></span><code>MainViewModel.OpenExpensePaymentReturnModal(ExpensePaymentRow,int)</code><br>134–158 | CheckSessionUnlocked @136; Pow @151; ToString @152; Contains @153; Contains @153 | No extracted literal effects. |
| <span id="m-d195153a6347"></span><code>MainViewModel.OpenSalaryPaymentReturnModal(SalaryLedgerRow)</code><br>160–190 | CheckSessionUnlocked @162; Pow @183; ToString @184; Contains @185 | No extracted literal effects. |
| <span id="m-a969f9075aad"></span><code>MainViewModel.ClosePaymentReturnModal()</code><br>192–198 | — | No extracted literal effects. |
| <span id="m-8c5e4aab7dbe"></span><code>MainViewModel.ConfirmPaymentReturnAsync()</code><br>200–283 | Trim @203; IsNullOrWhiteSpace @204; Trim @210; ConfigureAwait(ReverseExpensePaymentCommand, Guid) @237; ExecuteAsync(ReverseExpensePaymentCommand, Guid) @237; DispatchToUi @240; SafePipelineError @240; LoadExpenseRowsAsync @248; OpenExpenseDetailModalAsync @249; ConfigureAwait(ReverseSalaryPaymentCommand, Guid) @264; ExecuteAsync(ReverseSalaryPaymentCommand, Guid) @264; OpenSalaryMonthDetailModalAsync @275; SafeError @281 | No extracted literal effects. |
| <span id="m-4f3679bacdbd"></span><code>MainViewModel.OpenWasteExpenseConfirmation(StockMovement,InventoryItem,decimal,string)</code><br>408–422 | FirstOrDefault @417; Parse @417 | No extracted literal effects. |
| <span id="m-1332499c7a64"></span><code>MainViewModel.CloseWasteExpenseConfirmation()</code><br>424–428 | — | No extracted literal effects. |
| <span id="m-9cc46b00ccc9"></span><code>MainViewModel.ConfirmWasteExpenseAsync()</code><br>430–480 | Trim @458; ConfigureAwait(RecordWasteExpenseCommand, Guid) @462; ExecuteAsync(RecordWasteExpenseCommand, Guid) @462; DispatchToUi @465; SafePipelineError @465; LoadExpenseRowsAsync @473; SafeError @478 | No extracted literal effects. |

</details>

## MainViewModel.Salary.cs {#src-2f2298be3577}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Salary.cs</code> · 1,734 lines.

SHA-256: <code>74dc331417b744b4a100c77e5859949fa86dbb9ce6b8f5a79333d20ce0e18d63</code>.

Declarations: <code>MainViewModel</code> (line 19).

<details markdown>
<summary>Methods, calls, table effects and failures (42)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-6a6b765a9b54"></span><code>MainViewModel.ResetSalaryWorkspaceState()</code><br>24–43 | Increment @26; Clear @36; Clear @37; Clear @38; Clear @39; Clear @40; Clear @41; Clear @42 | No extracted literal effects. |
| <span id="m-43f30d494aa7"></span><code>MainViewModel.ConfigureSalaryPorts(ISalaryReader)</code><br>45–49 | InitializeSalaryTables @48 | No extracted literal effects. |
| <span id="m-06731b054f7a"></span><code>MainViewModel.RaiseSalaryLabels()</code><br>72–95 | RaisePropertyChanged @74; nameof @74; RefreshPayrollMonthDisplayNames @94 | No extracted literal effects. |
| <span id="m-8b368e4d5286"></span><code>MainViewModel.SelectSalaryTab(string)</code><br>116–119 | — | No extracted literal effects. |
| <span id="m-5a8400260beb"></span><code>MainViewModel.NavigateToTeamsWorkspace()</code><br>175–178 | SelectMenu @177 | No extracted literal effects. |
| <span id="m-f3b06f93888c"></span><code>MainViewModel.EnsurePayrollMonthRangeInitializedAsync(CancellationToken)</code><br>180–186 | ConfigureAwait @184; RebuildPayrollMonthRangeAsync @184 | No extracted literal effects. |
| <span id="m-2042c16d1dc1"></span><code>MainViewModel.RebuildPayrollMonthRangeAsync(CancellationToken)</code><br>188–300 | ConfigureAwait @195; GetStoreTimeZoneAsync @195; ToStoreLocalTime @203; GetEarliestPayrollMonthAsync @212; IsNullOrWhiteSpace @222; TryParse @223; Clear @250; Add @253; Contains @256; RaisePropertyChanged @261; nameof @261; Clear @266; GetLocalizedMonthName @270; Add @271; Clamp @280; FirstOrDefault @281 | No extracted literal effects. |
| <span id="m-ce18f610ecf4"></span><code>MainViewModel.OnPayrollYearChanged(int)</code><br>302–347 | Clear @312; GetLocalizedMonthName @316; Add @317; Clamp @326; FirstOrDefault @327; RaisePropertyChanged @332; nameof @332; ResetToFirstPage @345; LoadSalaryMonthRowsAsync @346 | No extracted literal effects. |
| <span id="m-bb516f7b1a12"></span><code>MainViewModel.OnPayrollMonthOptionChanged(PayrollMonthOption?)</code><br>349–365 | RaisePropertyChanged @356; nameof @356; ResetToFirstPage @363; LoadSalaryMonthRowsAsync @364 | No extracted literal effects. |
| <span id="m-7ea0a7d9c98f"></span><code>MainViewModel.ApplySelectedMonthStringToDropdowns(string)</code><br>367–403 | TryParse @369; Contains @375; Add @377; ToList @378; OrderByDescending @378; Clear @379; RaisePropertyChanged @383; nameof @383; Clear @387; Min @389; Max @389; GetLocalizedMonthName @391; Add @392; FirstOrDefault @395 | No extracted literal effects. |
| <span id="m-7645d33b7392"></span><code>MainViewModel.RefreshPayrollMonthDisplayNames()</code><br>405–431 | ToList @412; Select @412; Clear @413; GetLocalizedMonthName @417; Add @418; FirstOrDefault @424; RaisePropertyChanged @425; nameof @425 | No extracted literal effects. |
| <span id="m-c9caa9b9beed"></span><code>MainViewModel.GetLocalizedMonthName(int)</code><br>433–448 | Localize @437; IsNullOrWhiteSpace @438; StartsWith @438; GetMonthName @442; GetMonthName @446 | No extracted literal effects. |
| <span id="m-0b4f0d7326df"></span><code>MainViewModel.SalaryNextPage()</code><br>532–536 | NextPage @534; NextPage @535 | No extracted literal effects. |
| <span id="m-4e7adf898fd0"></span><code>MainViewModel.SalaryPreviousPage()</code><br>538–542 | PreviousPage @540; PreviousPage @541 | No extracted literal effects. |
| <span id="m-986ad1f52504"></span><code>MainViewModel.LoadSalaryWorkspaceAsync(CancellationToken)</code><br>576–588 | EnsurePaymentAccountsLoadedAsync @578; ConfigureAwait @579; EnsurePayrollMonthRangeInitializedAsync @579; LoadSalaryMonthRowsAsync @582; LoadSalaryPeopleRowsAsync @586 | No extracted literal effects. |
| <span id="m-e14a90f5e605"></span><code>MainViewModel.InitializeSalaryTables()</code><br>590–596 | BindRefresh @592; LoadSalaryMonthRowsAsync @592; BindRefresh @593; LoadSalaryPeopleRowsAsync @593; BindRefresh @594; LoadSalaryHistoryAsync @594; BuildSalaryTables @595 | No extracted literal effects. |
| <span id="m-fc28bba222da"></span><code>MainViewModel.BuildSalaryTables()</code><br>598–773 | CreateColumns @605; TextColumn @606; Localize @606; ToString @610; ToDisplayAmount @610; LocalizeTable @665; Max @673; Ceiling @673; ToLocalTime @747; RaisePropertyChanged @770; nameof @770 | No extracted literal effects. |
| <span id="m-485c99ca8922"></span><code>MainViewModel.LoadSalaryMonthRowsAsync(CancellationToken)</code><br>825–873 | Read @828; ToPageRequest @838; ConfigureAwait @839; GetMonthlyPayrollAsync @839; GetMonthlyPayrollSummariesAsync @840; DispatchToUi @846; ApplyPagedResult @851; Clear @852; Add @855; Clear @857; Add @860 | No extracted literal effects. |
| <span id="m-62802e1f5345"></span><code>MainViewModel.LoadSalaryPeopleRowsAsync(CancellationToken)</code><br>875–915 | Read @878; ToPageRequest @888; ConfigureAwait @889; GetPeopleAsync @889; DispatchToUi @894; ApplyPagedResult @899; Clear @900; Add @903 | No extracted literal effects. |
| <span id="m-09362f7caa08"></span><code>MainViewModel.LoadSalaryHistoryAsync(Guid?,CancellationToken)</code><br>917–949 | Read @923; ToPageRequest @928; ConfigureAwait @929; GetLedgerAsync @929; DispatchToUi @934; ApplyPagedResult @939 | No extracted literal effects. |
| <span id="m-a90f40ab6e31"></span><code>MainViewModel.CapturePersonFormBaseline()</code><br>1062–1065 | CaptureTeamMemberBaseline @1064 | No extracted literal effects. |
| <span id="m-213e908847b1"></span><code>MainViewModel.RequestClosePersonForm()</code><br>1069–1072 | RequestCloseTeamMemberModal @1071 | No extracted literal effects. |
| <span id="m-234b6c0fb530"></span><code>MainViewModel.KeepEditingPersonForm()</code><br>1074–1077 | KeepEditingTeamMemberForm @1076 | No extracted literal effects. |
| <span id="m-3ce8b45e76d9"></span><code>MainViewModel.ConfirmDiscardPersonForm()</code><br>1079–1082 | ConfirmDiscardTeamMemberForm @1081 | No extracted literal effects. |
| <span id="m-e844fb86a006"></span><code>MainViewModel.OpenAddPersonModal()</code><br>1084–1092 | OpenAddTeamMemberModal @1087; Localize @1090; CaptureTeamMemberBaseline @1091 | No extracted literal effects. |
| <span id="m-e9a198a79672"></span><code>MainViewModel.OpenEditPersonModalAsync(Guid)</code><br>1094–1098 | ConfigureAwait @1097; OpenEditTeamMemberModalAsync @1097 | No extracted literal effects. |
| <span id="m-3918274b179c"></span><code>MainViewModel.ClosePersonForm()</code><br>1100–1103 | CloseTeamMemberModal @1102 | No extracted literal effects. |
| <span id="m-1a7a94b14aba"></span><code>MainViewModel.SavePersonFormAsync()</code><br>1111–1114 | ConfigureAwait @1113; SaveTeamMemberAsync @1113 | No extracted literal effects. |
| <span id="m-f6d0b5525654"></span><code>MainViewModel.OpenSalaryMonthDetailModalAsync(Guid)</code><br>1135–1160 | ConfigureAwait @1140; GetPersonPayrollDetailAsync @1140; DispatchToUi @1143; Clear @1146; Add @1149; ResetToFirstPage @1151; LoadSalaryHistoryAsync @1152 | No extracted literal effects. |
| <span id="m-89a4b8530b9c"></span><code>MainViewModel.CloseSalaryMonthDetailModal()</code><br>1162–1165 | — | No extracted literal effects. |
| <span id="m-b5180fae5d18"></span><code>MainViewModel.OpenPayAdvanceModal(Guid,string,int,string,int)</code><br>1302–1318 | EnsurePaymentAccountsLoadedAsync @1305; ToDisplayAmount @1312; ScalingFactor @1312; NewGuid @1316 | No extracted literal effects. |
| <span id="m-3675ad48e958"></span><code>MainViewModel.OpenPaySalaryModal(Guid,string,int,long,string,int)</code><br>1320–1337 | EnsurePaymentAccountsLoadedAsync @1323; Max @1331; ToDisplayAmount @1331; NewGuid @1335 | No extracted literal effects. |
| <span id="m-25d6b7d3710e"></span><code>MainViewModel.CloseSalaryPaymentModal()</code><br>1339–1342 | — | No extracted literal effects. |
| <span id="m-f16ebdbb485a"></span><code>MainViewModel.ConfirmSalaryPaymentAsync()</code><br>1347–1479 | FirstOrDefault @1357; Equals @1364; IsNullOrWhiteSpace @1385; ToMinorUnits @1392; Trim @1407; Trim @1408; NewGuid @1410; ConfigureAwait(PayAdvanceCommand, Guid) @1430; ExecuteAsync(PayAdvanceCommand, Guid) @1430; DispatchToUi @1433; ConfigureAwait(PaySalaryCommand, Guid) @1450; ExecuteAsync(PaySalaryCommand, Guid) @1450; LoadSalaryWorkspaceAsync @1464; OpenSalaryMonthDetailModalAsync @1467 | No extracted literal effects. |
| <span id="m-a6f4d2388741"></span><code>MainViewModel.OpenAddBonusModal(Guid,int,string,string,int)</code><br>1550–1562 | ToDisplayAmount @1559; ScalingFactor @1559 | No extracted literal effects. |
| <span id="m-e2fc44e4858f"></span><code>MainViewModel.OpenAddDeductionModal(Guid,int,string,string,int)</code><br>1564–1576 | ToDisplayAmount @1573; ScalingFactor @1573 | No extracted literal effects. |
| <span id="m-5ec9efcaa7ae"></span><code>MainViewModel.OpenRecordUnpaidDaysModal(Guid,int,string)</code><br>1578–1588 | — | No extracted literal effects. |
| <span id="m-0d09588fe48a"></span><code>MainViewModel.CloseSalaryAdjustmentModal()</code><br>1590–1593 | — | No extracted literal effects. |
| <span id="m-67f733067aea"></span><code>MainViewModel.ConfirmSalaryAdjustmentAsync()</code><br>1598–1661 | IsNullOrWhiteSpace @1613; Trim @1613; ConfigureAwait(RecordUnpaidDaysCommand, bool) @1616; ExecuteAsync(RecordUnpaidDaysCommand, bool) @1616; DispatchToUi @1619; ToLowerInvariant @1625; ToMinorUnits @1626; ConfigureAwait(RecordSalaryAdjustmentCommand, Guid) @1638; ExecuteAsync(RecordSalaryAdjustmentCommand, Guid) @1638; LoadSalaryWorkspaceAsync @1650; OpenSalaryMonthDetailModalAsync @1653 | No extracted literal effects. |
| <span id="m-df27c254cafa"></span><code>MainViewModel.OpenFinalizeMonthModal(Guid,int,string)</code><br>1680–1688 | — | No extracted literal effects. |
| <span id="m-4fe60bd114d8"></span><code>MainViewModel.CloseSalaryFinalizeModal()</code><br>1690–1693 | — | No extracted literal effects. |
| <span id="m-f2cc7d762064"></span><code>MainViewModel.ConfirmFinalizeMonthAsync()</code><br>1698–1733 | ConfigureAwait(FinalizeSalaryPeriodCommand, Guid) @1711; ExecuteAsync(FinalizeSalaryPeriodCommand, Guid) @1711; DispatchToUi @1714; LoadSalaryWorkspaceAsync @1722; OpenSalaryMonthDetailModalAsync @1725 | No extracted literal effects. |

</details>

## MainViewModel.Search.cs {#src-f42896a9593e}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Search.cs</code> · 869 lines.

SHA-256: <code>de7f2f3001ca643f05ee60d403587505eb5e4da78d642b8f6c75069380470f3c</code>.

Declarations: <code>MainViewModel</code> (line 15), <code>DelegatingSearchSuggestionReader : ISearchSuggestionReader</code> (line 844), <code>DelegatingSearchUsageWriter : ISearchUsageWriter</code> (line 857).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b0189613797b"></span><code>MainViewModel.ConfigureSearchPorts(ISearchSuggestionReader,ISearchUsageWriter?,IOperationalLogger?)</code><br>29–36 | nameof @31; Increment @34; InvalidateAllSearchScopes @35 | No extracted literal effects. |
| <span id="m-4baa396d90bb"></span><code>MainViewModel.GetRealWorkspaceIdentity()</code><br>734–739 | — | No extracted literal effects. |
| <span id="m-9d53b7263f48"></span><code>MainViewModel.CreateSearchState(SearchContext,Func&lt;object?&gt;?,Action&lt;SearchOption?&gt;?,Action&lt;string, SearchEntityKey?&gt;?,Func&lt;SearchContext&gt;?,AsyncSearchSelectionHandler?)</code><br>741–770 | Localize @760; GetRealWorkspaceIdentity @763; Add @768 | No extracted literal effects. |
| <span id="m-089acf32fd69"></span><code>MainViewModel.RecordSuccessfulSearchUseAsync(SearchContext,SearchEntityKey,string,CancellationToken)</code><br>772–813 | IsNullOrWhiteSpace @778; LogFailure @786; ConfigureAwait @799; RecordUseAsync @799 | No extracted literal effects. |
| <span id="m-13451db4e30f"></span><code>MainViewModel.InvalidateAllSearchScopes(bool)</code><br>815–825 | Invalidate @819; TriggerSearchAsync @822 | No extracted literal effects. |
| <span id="m-835f560972bb"></span><code>MainViewModel.ClearAllSearchStates()</code><br>827–833 | Clear @831 | No extracted literal effects. |
| <span id="m-46cb464d4c12"></span><code>MainViewModel.DisposeSearchStates()</code><br>835–842 | Dispose @839; Clear @841 | No extracted literal effects. |
| <span id="m-8f43b7fde6e9"></span><code>DelegatingSearchSuggestionReader.GetSuggestionsAsync(SearchRequest,CancellationToken)</code><br>846–854 | readerSupplier @848; GetSuggestionsAsync @853 | InvalidOperationException @851 |
| <span id="m-0805f7290c93"></span><code>DelegatingSearchUsageWriter.RecordUseAsync(SearchUseRequest,CancellationToken)</code><br>859–867 | writerSupplier @861; RecordUseAsync @866 | InvalidOperationException @864 |

</details>

## MainViewModel.Tables.cs {#src-3f4385d56088}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Tables.cs</code> · 1,186 lines.

SHA-256: <code>29097d7a7d5e164ca15aa2b181f0408ed53a5fd85abe99ae6a03c069dae324ef</code>.

Declarations: <code>MainViewModel</code> (line 21).

<details markdown>
<summary>Methods, calls, table effects and failures (42)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-da61c4610f66"></span><code>MainViewModel.InitializeSharedDataTables()</code><br>132–179 | RebuildSharedDataTableDefinitions @134; BindRefresh @135; LoadPriceProposalsAsync @135; nameof @138; RaisePropertyChanged @140; InvalidateSelectedBatchPreview @143; SetSelectionScope @173; WorkspaceScopePrefix @173; SetSelectionScope @174; InventorySelectionScope @174; SetSelectionScope @175; ThirdPartySelectionScope @175; BindRefresh @176; BindRefresh @177; BindRefresh @178 | No extracted literal effects. |
| <span id="m-bbc9d9442542"></span><code>MainViewModel.OpenSelectedBatchOperation(string,bool)</code><br>181–205 | CheckSessionUnlocked @183; DispatchToUi @186; Localize @186; Clear @195; FirstOrDefault @196; RaisePropertyChanged @198; nameof @198 | No extracted literal effects. |
| <span id="m-6458dbba57c6"></span><code>MainViewModel.OpenSelectedThirdPartyBatchOperation(string,bool)</code><br>207–231 | CheckSessionUnlocked @209; DispatchToUi @212; Localize @212; Clear @221; FirstOrDefault @223; RaisePropertyChanged @224; nameof @224 | No extracted literal effects. |
| <span id="m-8b2dae480a2a"></span><code>MainViewModel.OpenSelectedThirdPartyBatchPriceLevel()</code><br>233–233 | OpenSelectedThirdPartyBatchOperation @233 | No extracted literal effects. |
| <span id="m-838efb56a5c3"></span><code>MainViewModel.OpenSelectedRegistryBatchOperation(BatchPreviewTarget,string,bool)</code><br>235–266 | CheckSessionUnlocked @237; DispatchToUi @246; Localize @246; Clear @255; RaisePropertyChanged @257; nameof @257 | No extracted literal effects. |
| <span id="m-0cd10fabe230"></span><code>MainViewModel.CurrentSelectedBatchIds()</code><br>268–274 | GetSelectedIdsForPreview @270; GetSelectedIdsForPreview @271; GetSelectedIdsForPreview @272; GetSelectedIdsForPreview @273; GetSelectedIdsForPreview @273 | No extracted literal effects. |
| <span id="m-64a177007a52"></span><code>MainViewModel.InvalidateSelectedBatchPreview()</code><br>276–283 | Clear @281; RaisePropertyChanged @282; nameof @282 | No extracted literal effects. |
| <span id="m-46ab3fde6fd9"></span><code>MainViewModel.CloseSelectedBatchModal()</code><br>285–289 | InvalidateSelectedBatchPreview @288 | No extracted literal effects. |
| <span id="m-5776cdbb59df"></span><code>MainViewModel.CreateSelectedBatchPreviewAsync()</code><br>291–351 | CheckSessionUnlocked @293; CurrentSelectedBatchIds @294; DispatchToUi @297; Localize @297; ToString @323; ConfigureAwait(CreateBatchPreviewCommand, BatchPreviewResult) @327; ExecuteAsync(CreateBatchPreviewCommand, BatchPreviewResult) @327; SafePipelineError @331; Serialize @339; Clear @340; Empty(BatchPreviewChange) @341; Add @342; RaisePropertyChanged @343; nameof @343; SafeError @349 | No extracted literal effects. |
| <span id="m-9c98723d14d4"></span><code>MainViewModel.ConfirmSelectedBatchAsync()</code><br>353–502 | ConfigureAwait(BatchDeleteUnitDefinitionsCommand, BatchResult) @363; ExecuteAsync(BatchDeleteUnitDefinitionsCommand, BatchResult) @363; ToString @364; DispatchToUi @367; SafePipelineError @367; ConfigureAwait(BatchDeleteCategoryDefinitionsCommand, BatchResult) @374; ExecuteAsync(BatchDeleteCategoryDefinitionsCommand, BatchResult) @374; ConfigureAwait(BatchUpdateUnitStatusCommand, BatchResult) @385; ExecuteAsync(BatchUpdateUnitStatusCommand, BatchResult) @385; ConfigureAwait(BatchUpdateCategoryStatusCommand, BatchResult) @396; ExecuteAsync(BatchUpdateCategoryStatusCommand, BatchResult) @396; ConfigureAwait(BatchUpdateExpenseCategoryStatusCommand, BatchResult) @407; ExecuteAsync(BatchUpdateExpenseCategoryStatusCommand, BatchResult) @407; ConfigureAwait(BatchUpdateThirdPartyStatusCommand, BatchResult) @418; ExecuteAsync(BatchUpdateThirdPartyStatusCommand, BatchResult) @418; ConfigureAwait(BatchAssignThirdPartyPriceLevelCommand, BatchResult) @429; ExecuteAsync(BatchAssignThirdPartyPriceLevelCommand, BatchResult) @429; ToString @439; ConfigureAwait(BatchAssignItemCategoryCommand, BatchResult) @440; ExecuteAsync(BatchAssignItemCategoryCommand, BatchResult) @440; ConfigureAwait(BatchAssignItemPurposeCommand, BatchResult) @451; ExecuteAsync(BatchAssignItemPurposeCommand, BatchResult) @451; ConfigureAwait(BatchUpdateItemStatusCommand, BatchResult) @462; ExecuteAsync(BatchUpdateItemStatusCommand, BatchResult) @462; ClearSelection @474; ClearSelection @476; ClearSelection @478; ClearSelection @480; ClearSelection @482; CloseSelectedBatchModal @483; Localize @484; ConfigureAwait @488; LoadManagedCategoriesAsync @488; LoadExpenseCategoriesAsync @489; LoadCatalogRegistryAsync @492; LoadThirdPartiesAsync @494; LoadInventoryAsync @496; SafeError @500 | No extracted literal effects. |
| <span id="m-2ce7e046cb91"></span><code>MainViewModel.RebuildSharedDataTableDefinitions()</code><br>504–870 | CreateColumns @511; TextColumn @512; Localize @515; ToString @519; LocalizeTable @522; Max @533; Ceiling @533; CreateLifecycleStatusHeader @581; LifecycleStatusFilterToolTip @587; OpenSelectedBatchOperation @604; OpenSelectedThirdPartyBatchOperation @665; OpenSelectedRegistryBatchOperation @772; FormatCanonicalUnitFactor @830; RaisePropertyChanged @859; nameof @859; BuildSalaryTables @868; BuildExpensesTable @869 | No extracted literal effects. |
| <span id="m-ddeaf3d0fbdd"></span><code>MainViewModel.RefreshManagedCategoriesTable()</code><br>872–883 | ThenBy @877; OrderByDescending @877; OrderBy @877; ApplyLocalPage @882 | No extracted literal effects. |
| <span id="m-a243f6280174"></span><code>MainViewModel.RefreshManagedUnitsTable()</code><br>885–899 | OrderByDescending @890; OrderBy @890; ThenBy @891; ParseCanonicalFactor @894; ApplyLocalPage @898 | No extracted literal effects. |
| <span id="m-aa927a2102ab"></span><code>MainViewModel.ApplyLocalPage(IEnumerable&lt;T&gt;,PagedTableState&lt;T&gt;)</code><br>901–910 | ToArray @903; Max @904; Ceiling @904; ApplyPagedResult @907; ToArray @908; Take @908; Skip @908 | No extracted literal effects. |
| <span id="m-c5d23e802e77"></span><code>MainViewModel.ParseCanonicalFactor(string?)</code><br>912–913 | TryParse @913 | No extracted literal effects. |
| <span id="m-ba63c15ed2ae"></span><code>MainViewModel.FormatCanonicalUnitFactor(UomOption)</code><br>915–916 | IsNullOrWhiteSpace @916 | No extracted literal effects. |
| <span id="m-56be8ab0dc9d"></span><code>MainViewModel.RefreshManagedExpenseCategoriesTable()</code><br>918–929 | OrderByDescending @923; OrderBy @923; ThenBy @924; ApplyLocalPage @928 | No extracted literal effects. |
| <span id="m-114fc6c06615"></span><code>MainViewModel.CreateManagedCategoryStatusCell(object)</code><br>931–935 | CreateStatusToggle @934; ToggleManagedCategoryActiveAsync @934 | No extracted literal effects. |
| <span id="m-ef28619201c2"></span><code>MainViewModel.CreateManagedExpenseCategoryStatusCell(object)</code><br>937–941 | CreateStatusToggle @940; ToggleManagedExpenseCategoryActiveAsync @940 | No extracted literal effects. |
| <span id="m-57b122c98341"></span><code>MainViewModel.CreateManagedUnitStatusCell(object)</code><br>943–947 | CreateStatusToggle @946; ToggleManagedUnitActiveAsync @946 | No extracted literal effects. |
| <span id="m-8c565566fa37"></span><code>MainViewModel.CreateStatusToggle(bool,Func&lt;Task&gt;)</code><br>949–962 | toggle @960 | No extracted literal effects. |
| <span id="m-81dead16ae65"></span><code>MainViewModel.CreateColumns(IReadOnlyList&lt;DataTableColumnDescriptor&gt;)</code><br>964–964 | — | No extracted literal effects. |
| <span id="m-adcf3dd24e30"></span><code>MainViewModel.TextColumn(string,string,Func&lt;object, string?&gt;,string?,double,double,DataTableCellStyle)</code><br>966–976 | — | No extracted literal effects. |
| <span id="m-ae1add5fe111"></span><code>MainViewModel.LocalizeTable(string)</code><br>978–978 | Localize @978 | No extracted literal effects. |
| <span id="m-6634048dca99"></span><code>MainViewModel.SelectionHeaderToolTip(bool)</code><br>980–981 | Localize @980 | No extracted literal effects. |
| <span id="m-44b51c465363"></span><code>MainViewModel.LifecycleStatusFilterToolTip(LifecycleStatusScope)</code><br>983–988 | Localize @983 | No extracted literal effects. |
| <span id="m-ce0660e3a853"></span><code>MainViewModel.CreateLifecycleStatusHeader(LifecycleStatusScope)</code><br>990–1004 | Add @1000 | No extracted literal effects. |
| <span id="m-c6313033e3f8"></span><code>MainViewModel.CreateInventoryLifecycleStatusCell(object)</code><br>1006–1015 | — | No extracted literal effects. |
| <span id="m-f265f43ba22d"></span><code>MainViewModel.CreateInventoryProductCell(object)</code><br>1017–1038 | Add @1023 | No extracted literal effects. |
| <span id="m-9bfdd711ae4e"></span><code>MainViewModel.CreateInventoryStockCell(object)</code><br>1040–1047 | CreateInventoryTwoLineCell @1046 | No extracted literal effects. |
| <span id="m-0298b8df2bc6"></span><code>MainViewModel.CreateInventoryPricingCell(object)</code><br>1049–1053 | CreateInventoryTwoLineCell @1052 | No extracted literal effects. |
| <span id="m-36523a838e7e"></span><code>MainViewModel.CreateInventoryTwoLineCell(string,string,DataTableCellStyle,DataTableCellStyle)</code><br>1055–1073 | Add @1058; InventoryCellStyleClass @1063 | No extracted literal effects. |
| <span id="m-f3abc006e008"></span><code>MainViewModel.InventoryCellStyleClass(DataTableCellStyle)</code><br>1075–1085 | — | No extracted literal effects. |
| <span id="m-5259a152f612"></span><code>MainViewModel.CreateThirdPartyStatusCell(object)</code><br>1087–1111 | Contains @1104; HasPermission @1105; SetTip @1108; RequestThirdPartyStatusChange @1109 | No extracted literal effects. |
| <span id="m-f068886ed030"></span><code>MainViewModel.CreateThirdPartyPriceLevelCell(object)</code><br>1113–1134 | FirstOrDefault @1119; Equals @1119; HasPermission @1124; SaveThirdPartyPriceLevelAsync @1131 | No extracted literal effects. |
| <span id="m-57247aef96ca"></span><code>MainViewModel.LocalizeInventoryStatus(string)</code><br>1136–1144 | Localize @1138 | No extracted literal effects. |
| <span id="m-e5864495843e"></span><code>MainViewModel.WorkspaceScopePrefix()</code><br>1146–1146 | Join @1146 | No extracted literal effects. |
| <span id="m-6b2d30df0da9"></span><code>MainViewModel.NotifySelectionScopeChange(bool)</code><br>1148–1152 | Localize @1151 | No extracted literal effects. |
| <span id="m-ef72a7cef9f9"></span><code>MainViewModel.InventorySelectionScope()</code><br>1154–1155 | Join @1154; WorkspaceScopePrefix @1154; Trim @1154; ToString @1155 | No extracted literal effects. |
| <span id="m-be422d375475"></span><code>MainViewModel.ThirdPartySelectionScope()</code><br>1157–1158 | Join @1157; WorkspaceScopePrefix @1157; Trim @1157; ToString @1158 | No extracted literal effects. |
| <span id="m-8a8c289f0a47"></span><code>MainViewModel.CreateInventoryToolbarButton(string,System.Windows.Input.ICommand,bool,string?)</code><br>1160–1174 | IsNullOrEmpty @1170; Add @1171 | No extracted literal effects. |
| <span id="m-c097d2295489"></span><code>MainViewModel.RefreshSharedDataTableDefinitions()</code><br>1176–1182 | RebuildSharedDataTableDefinitions @1178; BuildSalaryTables @1179; BuildExpensesTable @1180; BuildTeamsTable @1181 | No extracted literal effects. |

</details>

## MainViewModel.Teams.cs {#src-45e93424b80f}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Teams.cs</code> · 1,474 lines.

SHA-256: <code>2165e0876b95527ee215d165c9ef018a57fa0ce332319ca3f0f724ce436877e0</code>.

Declarations: <code>MainViewModel</code> (line 20), <code>TeamMemberBaseline</code> (line 406).

<details markdown>
<summary>Methods, calls, table effects and failures (20)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-db72914eb3a5"></span><code>MainViewModel.ConfigureTeamsPorts(ITeamsReader,IPinHasher?)</code><br>26–30 | — | No extracted literal effects. |
| <span id="m-43976c34eb89"></span><code>MainViewModel.RaiseTeamsLabels()</code><br>325–348 | RaisePropertyChanged @327; nameof @327 | No extracted literal effects. |
| <span id="m-fea66447dffd"></span><code>MainViewModel.OnTeamMemberFieldChanged()</code><br>439–442 | CheckTeamMemberIsDirty @441 | No extracted literal effects. |
| <span id="m-c86df117372e"></span><code>MainViewModel.CaptureTeamMemberBaseline()</code><br>444–468 | ToList @446; Select @446 | No extracted literal effects. |
| <span id="m-ed43fff1ec6d"></span><code>MainViewModel.CheckTeamMemberIsDirty()</code><br>470–495 | ToList @473; Select @473; All @475; Zip @475; Equals @477 | No extracted literal effects. |
| <span id="m-6d33929675ee"></span><code>MainViewModel.CheckSalarySectionIsDirty()</code><br>497–507 | Equals @503 | No extracted literal effects. |
| <span id="m-ab20e62338ed"></span><code>MainViewModel.GetRegisteredPermissionDefinitions()</code><br>512–541 | — | No extracted literal effects. |
| <span id="m-5b5c35f7b076"></span><code>MainViewModel.LoadDefaultPermissionOverrides()</code><br>543–561 | Clear @545; GetRegisteredPermissionDefinitions @546; Add @550 | No extracted literal effects. |
| <span id="m-c8ed8d8f5f19"></span><code>MainViewModel.InitializeTeamsCommands()</code><br>611–655 | Create @613; CreateFromTask @614; CreateFromTask(string) @619; CreateFromTask(object?) @621; IsNullOrWhiteSpace @623; ConfigureAwait @625; OpenEditTeamMemberModalAsync @625; Create(object?) @629; OpenChangePinModal @633; Execute @641; Execute @649; BindRefresh @653; ApplyTeamsTablePage @653; BuildTeamsTable @654 | No extracted literal effects. |
| <span id="m-9b48ae66a434"></span><code>MainViewModel.BuildTeamsTable()</code><br>657–716 | CreateColumns @664; TextColumn @665; Localize @665; IsNullOrWhiteSpace @666; LocalizeTable @705; Max @713; Ceiling @713; RaisePropertyChanged @715; nameof @715 | No extracted literal effects. |
| <span id="m-615346e55c05"></span><code>MainViewModel.ApplyTeamsTablePage(IEnumerable&lt;StaffMember&gt;?)</code><br>718–752 | IsNullOrWhiteSpace @722; Trim @724; Where @725; Contains @726; Contains @727; Contains @728; ThenBy @742; OrderByDescending @742; OrderBy @742; ApplyLocalPage @751 | No extracted literal effects. |
| <span id="m-cc8100cbd028"></span><code>MainViewModel.LoadTeamsStaffAsync()</code><br>754–881 | ApplyTeamsTablePage @758; Clear @766; ApplyPagedResult @767; ConfigureAwait @788; GetTeamMembersAsync @788; DispatchToUi @790; IsNullOrEmpty @803; Contains @804; Pow @813; ToString @814; Add @860; Add @861; SafeError @879 | No extracted literal effects. |
| <span id="m-9aee1304efdc"></span><code>MainViewModel.ResetTeamMemberFormState()</code><br>883–922 | Increment @885; Clear @921 | No extracted literal effects. |
| <span id="m-86f46db58f73"></span><code>MainViewModel.OpenAddTeamMemberModal()</code><br>924–982 | GetResult @943; GetAwaiter @943; GetStoreTimeZoneAsync @943; GetStoreLocalMonth @951; ToDateTime @956; GetStoreLocalDate @956; Localize @972; IsNullOrWhiteSpace @973; LoadDefaultPermissionOverrides @978; CaptureTeamMemberBaseline @979 | No extracted literal effects. |
| <span id="m-a424b10c9f53"></span><code>MainViewModel.OpenEditTeamMemberModalAsync(string)</code><br>984–1173 | Read @986; ConfigureAwait @998; GetTeamMemberDetailAsync @998; GetTeamMemberDetailAsync @1003; StartsWith @1020; TryParse @1023; AsSpan @1023; GetPersonAsync @1025; DispatchToUi @1032; ToDateTime @1048; ToDateTime @1049; Pow @1059; ToString @1064; ToString @1065; AddMonths @1065; Localize @1078; IsNullOrWhiteSpace @1079; LoadDefaultPermissionOverrides @1081; CaptureTeamMemberBaseline @1082; ToDateTime @1109; Clear @1146; GetRegisteredPermissionDefinitions @1147; ToDictionary @1148; TryGetValue @1153; Add @1158 | No extracted literal effects. |
| <span id="m-07e28d68419b"></span><code>MainViewModel.SaveTeamMemberAsync()</code><br>1175–1437 | IsNullOrWhiteSpace @1184; Trim @1195; All @1205; IsNullOrEmpty @1215; IsMatch @1250; Trim @1250; Trim @1257; Pow @1264; Round @1265; ToList @1274; Select @1274; Where @1274; Trim @1283; ToLowerInvariant @1284; Trim @1284; FromDateTime @1285; Trim @1288; Trim @1300; Trim @1301; Trim @1309; CheckSalarySectionIsDirty @1322; Trim @1337; ToString @1351; ConfigureAwait(CreateTeamMemberCommand, CreateTeamMemberResult) @1371; ExecuteAsync(CreateTeamMemberCommand, CreateTeamMemberResult) @1371; DispatchToUi @1374; ConfigureAwait(UpdateTeamMemberCommand, UpdateTeamMemberResult) @1395; ExecuteAsync(UpdateTeamMemberCommand, UpdateTeamMemberResult) @1395; LoadTeamsStaffAsync @1420; LoadSalaryWorkspaceAsync @1421 | No extracted literal effects. |
| <span id="m-1c116004f701"></span><code>MainViewModel.RequestCloseTeamMemberModal()</code><br>1439–1449 | CloseTeamMemberModal @1448 | No extracted literal effects. |
| <span id="m-620098d282c1"></span><code>MainViewModel.CloseTeamMemberModal()</code><br>1451–1462 | — | No extracted literal effects. |
| <span id="m-7e21a7f191da"></span><code>MainViewModel.ConfirmDiscardTeamMemberForm()</code><br>1464–1468 | CloseTeamMemberModal @1467 | No extracted literal effects. |
| <span id="m-30f48a89f091"></span><code>MainViewModel.KeepEditingTeamMemberForm()</code><br>1470–1473 | — | No extracted literal effects. |

</details>

## MainViewModel.ThirdParties.cs {#src-974d69a1850f}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdParties.cs</code> · 4,410 lines.

SHA-256: <code>3c53552e5e52a963205ba747a1f2ec7dbd048ba490f4b486f74a997588a1c03b</code>.

Declarations: <code>MainViewModel</code> (line 32), <code>ThirdPartyFormSnapshot</code> (line 160), <code>ItemTierPricingRow : ReactiveObject</code> (line 4288), <code>PricingRoundingOption</code> (line 4337), <code>PricingIncrementOption</code> (line 4338), <code>PricingMethodOption</code> (line 4339), <code>PricingCostBasisOption</code> (line 4340), <code>CategoryPricingPreviewProduct</code> (line 4341), <code>TierWeightModeOption</code> (line 4345), <code>PriceOfferRow</code> (line 4347), <code>PendingShelfLabelRow : ReactiveObject</code> (line 4368), <code>KitPriceAlertRow</code> (line 4390).

<details markdown>
<summary>Methods, calls, table effects and failures (74)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f6748aa6eaea"></span><code>MainViewModel.SetThirdPartyFormValue(T,T,string?)</code><br>188–195 | Equals(T) @190; RaiseAndSetIfChanged @193; RaisePropertyChanged @194; nameof @194 | No extracted literal effects. |
| <span id="m-194379d2b2b1"></span><code>MainViewModel.CaptureThirdPartyFormSnapshot()</code><br>197–201 | — | No extracted literal effects. |
| <span id="m-cf0a11cec1ac"></span><code>MainViewModel.CaptureThirdPartyFormBaseline()</code><br>203–207 | CaptureThirdPartyFormSnapshot @205; RaisePropertyChanged @206; nameof @206 | No extracted literal effects. |
| <span id="m-a718c0780d1b"></span><code>MainViewModel.KindMatches(string?,string)</code><br>365–374 | ToLowerInvariant @367; Trim @367 | No extracted literal effects. |
| <span id="m-8730d5b4f808"></span><code>MainViewModel.CycleThirdPartyLifecycleStatusScope()</code><br>450–455 | — | No extracted literal effects. |
| <span id="m-01a1aac61fb1"></span><code>MainViewModel.FormatBatchPrice(long)</code><br>900–905 | Clamp @902; ScalingFactor @903; ToString @904 | No extracted literal effects. |
| <span id="m-83f7581193ec"></span><code>MainViewModel.LocalizeBatchPricingOutcome(string)</code><br>907–914 | StartsWith @909; Localize @913 | No extracted literal effects. |
| <span id="m-c0e05a205337"></span><code>MainViewModel.InvalidateBatchPricingPreview()</code><br>916–928 | CancelBatchPricingPreviewExpiry @918; RaisePropertyChanged @923; nameof @923 | No extracted literal effects. |
| <span id="m-9fa51132e6a5"></span><code>MainViewModel.CurrentBatchPricingOptions()</code><br>930–933 | ToMinorUnits @932; Clamp @932 | No extracted literal effects. |
| <span id="m-c368929f4af7"></span><code>MainViewModel.CurrentBatchPricingOptionsJson()</code><br>934–935 | OperationParametersJson @934; CurrentBatchPricingOptions @935 | No extracted literal effects. |
| <span id="m-3a7cc56114b4"></span><code>MainViewModel.CurrentSelectedBatchIdsJson()</code><br>937–937 | Serialize @937; GetSelectedIdsForPreview @937 | No extracted literal effects. |
| <span id="m-3724a3713a44"></span><code>MainViewModel.StartBatchPricingPreviewExpiry(Guid,DateTime)</code><br>939–944 | CancelBatchPricingPreviewExpiry @941; NotifyBatchPricingPreviewExpiryAsync @943 | No extracted literal effects. |
| <span id="m-e5d1dbf3c104"></span><code>MainViewModel.CancelBatchPricingPreviewExpiry()</code><br>946–951 | Cancel @948; Dispose @949 | No extracted literal effects. |
| <span id="m-56351a5b9bbb"></span><code>MainViewModel.NotifyBatchPricingPreviewExpiryAsync(Guid,DateTime,CancellationToken)</code><br>953–966 | ConfigureAwait @958; Delay @958; DispatchToUi @959; RaisePropertyChanged @962; nameof @962 | No extracted literal effects. |
| <span id="m-c213f7b139f6"></span><code>MainViewModel.KeepEditingThirdPartyForm()</code><br>1049–1049 | — | No extracted literal effects. |
| <span id="m-a4a0b03e3806"></span><code>MainViewModel.OpenBatchPricingForSelectedItems()</code><br>1108–1119 | CheckSessionUnlocked @1110; DispatchToUi @1113; Localize @1113; InvalidateBatchPricingPreview @1117 | No extracted literal effects. |
| <span id="m-ff3df36a7d2d"></span><code>MainViewModel.OpenAddThirdParty()</code><br>1149–1168 | CheckSessionUnlocked @1151; RequestCloseThirdPartyForm @1154; ClearThirdPartyForm @1157; FirstOrDefault @1160; CaptureThirdPartyFormBaseline @1167 | No extracted literal effects. |
| <span id="m-4f3298280ee2"></span><code>MainViewModel.OpenEditThirdParty(ThirdPartyDto?)</code><br>1170–1202 | CheckSessionUnlocked @1172; IsNullOrWhiteSpace @1178; FirstOrDefault @1191; FirstOrDefault @1193; CaptureThirdPartyFormBaseline @1201 | No extracted literal effects. |
| <span id="m-ba548bc4351c"></span><code>MainViewModel.RequestThirdPartyStatusChange(ThirdPartyDto?)</code><br>1204–1217 | Contains @1207; CheckSessionUnlocked @1208; HasPermission @1209; RaisePropertyChanged @1213; nameof @1213 | No extracted literal effects. |
| <span id="m-46261b2ff0e3"></span><code>MainViewModel.ConfirmThirdPartyStatusChangeAsync()</code><br>1219–1243 | Add @1222; CancelThirdPartyStatusChange @1224; RefreshSharedDataTableDefinitions @1225; RaisePropertyChanged @1226; nameof @1226; ConfigureAwait @1230; ReactivateThirdPartyAsync @1230; DeactivateThirdPartyAsync @1232; Remove @1236; DispatchToUi @1237 | No extracted literal effects. |
| <span id="m-766a7d987a90"></span><code>MainViewModel.CancelThirdPartyStatusChange()</code><br>1245–1252 | RaisePropertyChanged @1249; nameof @1249 | No extracted literal effects. |
| <span id="m-9ce5d2fcdd0c"></span><code>MainViewModel.SaveThirdPartyPriceLevelAsync(ThirdPartyDto,string,ComboBox?)</code><br>1254–1290 | IsNullOrWhiteSpace @1257; Equals @1258; Add @1259; CheckSessionUnlocked @1261; Remove @1263; FirstOrDefault @1264; ConfigureAwait(SetThirdPartyPriceLevelCommand, bool) @1272; ExecuteAsync(SetThirdPartyPriceLevelCommand, bool) @1272; DispatchToUi @1275; SafePipelineError @1275; Localize @1277; SafeError @1281; ConfigureAwait @1286; LoadThirdPartiesAsync @1286; HasPermission @1288 | No extracted literal effects. |
| <span id="m-328b18472b41"></span><code>MainViewModel.RequestCloseThirdPartyForm()</code><br>1292–1307 | CloseThirdPartyForm @1306 | No extracted literal effects. |
| <span id="m-9be9d97667e9"></span><code>MainViewModel.ConfirmDiscardThirdPartyForm()</code><br>1309–1313 | CloseThirdPartyForm @1312 | No extracted literal effects. |
| <span id="m-1c9e00fe0336"></span><code>MainViewModel.CloseThirdPartyForm()</code><br>1315–1324 | ClearThirdPartyForm @1322; RaisePropertyChanged @1323; nameof @1323 | No extracted literal effects. |
| <span id="m-3d3bbaf6a038"></span><code>MainViewModel.OpenThirdPartiesWorkspace(string?)</code><br>1330–1345 | CheckSessionUnlocked @1332; SelectMenu @1336; IsNullOrWhiteSpace @1339; ResetToFirstPage @1342; LoadThirdPartiesAsync @1343 | No extracted literal effects. |
| <span id="m-781627a39246"></span><code>MainViewModel.OpenEditPartyFromChooserAsync(CustomerDto?)</code><br>1353–1375 | CloseCustomerChooser @1357; SelectMenu @1361; ConfigureAwait @1364; LoadThirdPartiesAsync @1364; FirstOrDefault @1366; DispatchToUi @1374; OpenEditThirdParty @1374 | No extracted literal effects. |
| <span id="m-3f670f496afd"></span><code>MainViewModel.ClearThirdPartyForm()</code><br>1377–1398 | — | No extracted literal effects. |
| <span id="m-9672164a89dd"></span><code>MainViewModel.ConfirmSaveThirdPartyAsync()</code><br>1400–1474 | IsNullOrWhiteSpace @1402; NormalizeDbValue @1417; Trim @1423; NullIfBlank @1424; FirstOrDefault @1429; ConfigureAwait(UpdateThirdPartyCommand, ThirdPartyDto) @1434; ExecuteAsync(UpdateThirdPartyCommand, ThirdPartyDto) @1434; DispatchToUi @1437; SafePipelineError @1437; ConfigureAwait(CreateThirdPartyCommand, ThirdPartyDto) @1454; ExecuteAsync(CreateThirdPartyCommand, ThirdPartyDto) @1454; ConfigureAwait @1462; LoadThirdPartiesAsync @1462; LoadThirdPartiesLegacyListsAsync @1463; CloseThirdPartyForm @1466; SafeError @1472 | No extracted literal effects. |
| <span id="m-be2b39e40de6"></span><code>MainViewModel.DeactivateThirdPartyAsync(Guid)</code><br>1476–1508 | CheckSessionUnlocked @1478; ConfigureAwait(DeactivateThirdPartyCommand, bool) @1489; ExecuteAsync(DeactivateThirdPartyCommand, bool) @1489; DispatchToUi @1492; SafePipelineError @1492; ConfigureAwait @1496; LoadThirdPartiesAsync @1496; LoadThirdPartiesLegacyListsAsync @1497; SafeError @1506 | No extracted literal effects. |
| <span id="m-542ff9890b87"></span><code>MainViewModel.LoadThirdPartiesAsync()</code><br>1513–1542 | Increment @1516; ConfigureAwait @1519; GetPagedThirdPartiesAsync @1519; ToPageRequest @1521; DispatchToUi @1529; Read @1531; Clear @1532; AddRange @1533; ApplyPagedResult @1534; RefreshThirdPartyList @1535; SafeError @1540 | No extracted literal effects. |
| <span id="m-263e6124e1f2"></span><code>MainViewModel.LoadThirdPartiesLegacyListsAsync()</code><br>1545–1549 | ConfigureAwait @1547; LoadCustomersAsync @1547; LoadSuppliersAsync @1548 | No extracted literal effects. |
| <span id="m-0fb65ab8f6d6"></span><code>MainViewModel.LoadPriceLevelSettingsAsync()</code><br>1551–1620 | CreateCommand @1558; ConfigureAwait @1561; ExecuteScalarAsync @1561; ToInt32 @1564; ExecuteReaderAsync @1571; ReadAsync @1572; ParseStoredPercentage @1574; IsDBNull @1574; GetString @1574; GetInt32 @1574; ToString @1575; Add @1576; DispatchToUi @1586; Clear @1590; Clear @1591; Clear @1592; Add @1595; Add @1598; Add @1599; Any @1603; FirstOrDefault @1608; BuildItemTierRows @1613; SafeError @1618 | FROM price_level_settings @1570; FROM store_config @1560 |
| <span id="m-025d1cd1cb9d"></span><code>MainViewModel.LoadPriceProposalsAsync()</code><br>1622–1718 | Increment @1625; ConfigureAwait @1626; WaitAsync @1626; CreateCommand @1630; ToInt32 @1633; ExecuteScalarAsync @1633; Max @1637; Ceiling @1637; Min @1638; ToLowerInvariant @1640; IsNullOrWhiteSpace @1649; AddSqlParam @1664; ExecuteReaderAsync @1666; ReadAsync @1667; IsDBNull @1669; GetString @1669; TryParse @1676; Localize @1678; Format @1679; ScalingFactor @1680; Add @1683; ParseGuidSafe @1684; GetInt64 @1686; ParseDate @1690; Read @1696; DispatchToUi @1698; ApplyPagedResult @1701; Clear @1702; Add @1705; SafeError @1712; Release @1716 | FROM price_change_proposals @1632 · DYNAMIC SQL: inspect manually |
| <span id="m-a98f9f0900da"></span><code>MainViewModel.SavePriceTierSettingsAsync()</code><br>1720–1761 | TryParse @1733; DispatchToUi @1736; Localize @1736; Add @1739; ToString @1742; ConfigureAwait(UpdatePriceTierSettingsCommand, bool) @1747; ExecuteAsync(UpdatePriceTierSettingsCommand, bool) @1747; SafePipelineError @1750; ConfigureAwait @1754; LoadPriceLevelSettingsAsync @1754; SafeError @1759 | No extracted literal effects. |
| <span id="m-f17d05a287f6"></span><code>MainViewModel.ResolveProposalAsync(string?,bool)</code><br>1763–1795 | TryParse @1765; ConfigureAwait(ResolvePriceChangeProposalCommand, bool) @1774; ExecuteAsync(ResolvePriceChangeProposalCommand, bool) @1774; DispatchToUi @1777; SafePipelineError @1777; ConfigureAwait @1783; LoadPriceProposalsAsync @1783; Localize @1784; SafeError @1793 | No extracted literal effects. |
| <span id="m-d1e7bb54acb6"></span><code>MainViewModel.LoadItemPricingAsync(InventoryItem?)</code><br>1800–1902 | DispatchToUi @1804; RaisePropertyChanged @1807; nameof @1807; ToString @1813; CreateCommand @1816; CreateParameter @1823; Add @1823; ConfigureAwait @1824; ExecuteReaderAsync @1824; ReadAsync @1825; IsDBNull @1827; GetString @1827; GetInt32 @1828; ParseStoredPricingPercentForDisplay @1829; GetInt64 @1833; ToDisplayAmount @1846; IsIncrementRoundingRule @1848; CalculateAsync @1858; TryGetValue @1883; SafeError @1900 | FROM item_price_levels @1865; FROM item_pricing @1818 |
| <span id="m-e8f6bda4704f"></span><code>MainViewModel.BuildItemTierRows(IEnumerable&lt;PriceLevelSettingDto&gt;)</code><br>1904–1921 | Count @1906; Clear @1911; OrderBy @1912; Where @1912; Add @1914 | No extracted literal effects. |
| <span id="m-34eb8535cca9"></span><code>MainViewModel.SaveItemPricingAsync()</code><br>1923–1975 | Add @1948; ToCommand @1958; ConfigureAwait(SaveItemPricingCommand, bool) @1961; ExecuteAsync(SaveItemPricingCommand, bool) @1961; DispatchToUi @1965; SafePipelineError @1965; SafeError @1973 | No extracted literal effects. |
| <span id="m-3fc3169378c6"></span><code>MainViewModel.CreateBatchPricingPreviewAsync()</code><br>1977–2035 | Localize @1988; DispatchToUi @1994; InvalidateBatchPricingPreview @1994; GetSelectedIdsForPreview @1995; CurrentBatchPricingOptions @2005; ConfigureAwait(CreateBatchPreviewCommand, BatchPreviewResult) @2006; ExecuteAsync(CreateBatchPreviewCommand, BatchPreviewResult) @2006; CurrentBatchPricingOptionsJson @2013; Serialize @2015; StartBatchPricingPreviewExpiry @2017; RaisePropertyChanged @2018; nameof @2018; SafePipelineError @2024; SafeError @2029 | No extracted literal effects. |
| <span id="m-6e92b32c825f"></span><code>MainViewModel.LoadCategoryPricingRuleAsync(ProductCategoryOption?)</code><br>2037–2124 | Equals @2039; DispatchToUi @2041; Clear @2044; CreateCommand @2054; AddSqlParam @2060; ToString @2060; ConfigureAwait @2061; ExecuteReaderAsync @2061; ReadAsync @2062; ParseGuidSafe @2065; GetString @2065; GetInt32 @2065; GetInt64 @2066; IsDBNull @2067; ParseDate @2068; Add @2084; Add @2094; TryParse @2108; ToDisplayAmount @2110; FirstOrDefault @2115; SafeError @2122 | FROM item_kits @2075; FROM items @2075; FROM product_category_pricing_rules @2056 |
| <span id="m-56bff75e903d"></span><code>MainViewModel.PreviewCategoryPricingRuleAsync()</code><br>2126–2218 | Localize @2130; ParseRoundingRule @2138; IsRoundingRuleCompatible @2139; TryConvertRoundingIncrement @2141; ConfigureAwait @2151; CalculateAsync @2151; CreateCommand @2163; AddSqlParam @2168; ToString @2168; ExecuteReaderAsync @2169; ReadAsync @2170; GetInt64 @2176; IsDBNull @2179; DisposeAsync @2194; SetCategoryPricingPreviewAsync @2201; ToInt64 @2210; ExecuteScalarAsync @2210; DispatchToUi @2216; SafeError @2216 | FROM items @2164; FROM items @2208; JOIN item_pricing @2164; JOIN item_pricing @2208 |
| <span id="m-4189c5f89502"></span><code>MainViewModel.SetCategoryPricingPreviewAsync(decimal,long,string,RoundingRule,long,int)</code><br>2220–2252 | ParsePricingMethod @2224; ToMinorUnits @2226; CalculateUnroundedBasePriceMinor @2228; ResolveEffectiveBasePrice @2229; ScalingFactor @2231; FormatPricingCandidate @2232; Format @2234; ToDisplayAmount @2234; Abs @2238; FirstOrDefault @2239; Localize @2242; DispatchToUi @2248; ToString @2250 | No extracted literal effects. |
| <span id="m-86e79355e8a6"></span><code>MainViewModel.FormatPricingCandidate(decimal,int)</code><br>2254–2260 | ScalingFactor @2256; Min @2257; ToString @2258; ToString @2259 | No extracted literal effects. |
| <span id="m-0ce8848ae0c7"></span><code>MainViewModel.SaveCategoryPricingRuleAsync()</code><br>2262–2300 | Localize @2266; ToMinorUnits @2280; ConfigureAwait(SaveCategoryPricingRuleCommand, CategoryPricingRuleSaveResult) @2283; ExecuteAsync(SaveCategoryPricingRuleCommand, CategoryPricingRuleSaveResult) @2283; DispatchToUi @2287; SafePipelineError @2287; ConfigureAwait @2291; LoadCategoryPricingRuleAsync @2291; LoadPriceProposalsAsync @2292; SafeError @2298 | No extracted literal effects. |
| <span id="m-e10ffd086703"></span><code>MainViewModel.DeactivateCategoryPricingRuleAsync()</code><br>2302–2323 | ConfigureAwait(DeactivateCategoryPricingRuleCommand, bool) @2307; ExecuteAsync(DeactivateCategoryPricingRuleCommand, bool) @2307; DispatchToUi @2312; SafePipelineError @2312; ConfigureAwait @2315; LoadCategoryPricingRuleAsync @2315; LoadPriceProposalsAsync @2316; Localize @2317; SafeError @2321 | No extracted literal effects. |
| <span id="m-fd288e34e844"></span><code>MainViewModel.LoadKitComponentCostPreviewAsync(InventoryItem,string)</code><br>2325–2352 | ConfigureAwait @2334; CalculateAsync @2334; DispatchToUi @2336; Equals @2339; RaisePropertyChanged @2345; nameof @2345; SafeError @2350 | No extracted literal effects. |
| <span id="m-b32e7d97179e"></span><code>MainViewModel.FormatKitComponentCostPreview(KitComponentCostResult)</code><br>2354–2370 | Localize @2356; ScalingFactor @2361; Format @2362; Select @2363; ToString @2364; FormatMinor @2364; Join @2368 | No extracted literal effects. |
| <span id="m-c40d6b580f62"></span><code>MainViewModel.ReactivateThirdPartyAsync(Guid)</code><br>2372–2398 | CheckSessionUnlocked @2374; ConfigureAwait(ReactivateThirdPartyCommand, bool) @2379; ExecuteAsync(ReactivateThirdPartyCommand, bool) @2379; DispatchToUi @2383; SafePipelineError @2383; ConfigureAwait @2386; LoadThirdPartiesAsync @2386; LoadThirdPartiesLegacyListsAsync @2387; SafeError @2396 | No extracted literal effects. |
| <span id="m-2e97c1625d99"></span><code>MainViewModel.ConfirmBatchPricingAsync()</code><br>2404–2443 | DispatchToUi @2408; Localize @2408; CurrentBatchPricingOptions @2414; ConfigureAwait(ApplyBatchPricingCommand, BatchPricingResult) @2419; ExecuteAsync(ApplyBatchPricingCommand, BatchPricingResult) @2419; ToString @2420; InvalidateBatchPricingPreview @2423; ConfigureAwait @2424; LoadInventoryAsync @2424; LoadPriceProposalsAsync @2425; SafePipelineError @2432; SafeError @2437 | No extracted literal effects. |
| <span id="m-7ebc2fb7f47d"></span><code>MainViewModel.RequestElevationForCheckout(string?)</code><br>2448–2463 | Clear @2450; DistinctBy @2451; Where @2451; GetUnlockCandidates @2451; Equals @2452; Add @2456; Localize @2460 | No extracted literal effects. |
| <span id="m-49577f23c947"></span><code>MainViewModel.CancelElevation()</code><br>2465–2472 | — | No extracted literal effects. |
| <span id="m-698aa63ecca3"></span><code>MainViewModel.ConfirmElevationAsync()</code><br>2474–2518 | Localize @2479; IsNullOrWhiteSpace @2483; AuthenticateSelectedUser @2491; Trim @2491; Any @2492; Equals @2492; Contains @2495; HasPermission @2498; ConfigureAwait @2512; PlaceOrderAsync @2512; SafeError @2516 | No extracted literal effects. |
| <span id="m-4929f94973c1"></span><code>MainViewModel.FormatCartSummaryNumber(decimal)</code><br>2703–2710 | Clamp @2708; ToString @2709 | No extracted literal effects. |
| <span id="m-c002ee2a92a5"></span><code>MainViewModel.Localize(string,object?[])</code><br>3166–3166 | Localize @3166 | No extracted literal effects. |
| <span id="m-80fcf93fb5c4"></span><code>MainViewModel.RaiseLocalizedLabels()</code><br>3172–3915 | RaisePropertyChanged @3174; nameof @3174; RefreshManufacturingLocalization @3666; RefreshTraceabilityLocalization @3667; RefreshCommercialLocalization @3668; RefreshImportLocalization @3669 | No extracted literal effects. |
| <span id="m-5972c8c91a56"></span><code>MainViewModel.RefreshThirdPartyList()</code><br>3920–3927 | Clear @3922; Add @3925 | No extracted literal effects. |
| <span id="m-2097a3059af5"></span><code>MainViewModel.NullIfBlank(string?)</code><br>3929–3929 | IsNullOrWhiteSpace @3929; Trim @3929 | No extracted literal effects. |
| <span id="m-ae6a71852e65"></span><code>MainViewModel.ParsePercent(string?)</code><br>3931–3932 | TryParse @3932 | No extracted literal effects. |
| <span id="m-64845607dcd0"></span><code>MainViewModel.ParseStoredPricingPercentForDisplay(string?,int)</code><br>3934–3935 | ParseStoredPercentage @3935 | No extracted literal effects. |
| <span id="m-7afdfee37b74"></span><code>MainViewModel.IsIncrementRoundingRule(string?)</code><br>3937–3939 | Equals @3938 | No extracted literal effects. |
| <span id="m-bbfe8b815558"></span><code>MainViewModel.ParseDate(string?)</code><br>3941–3942 | TryParse @3942 | No extracted literal effects. |
| <span id="m-198731cc3c7c"></span><code>MainViewModel.OpenNewPriceOffer()</code><br>4040–4050 | ToString @4044; ToString @4045; AddDays @4045; FirstOrDefault @4047 | No extracted literal effects. |
| <span id="m-7a7d4da11f83"></span><code>MainViewModel.OpenEditPriceOfferAsync(PriceOfferRow)</code><br>4052–4075 | CreateCommand @4055; CreateParameter @4058; ToString @4058; Add @4058; ConfigureAwait @4059; ExecuteReaderAsync @4059; ReadAsync @4059; Parse @4060; GetString @4060; GetInt32 @4060; IsDBNull @4062; TryParse @4062; ToString @4062; ToUniversalTime @4062; ToString @4062; ToUniversalTime @4063; AddDays @4063; FirstOrDefault @4065; TryParse @4067; FirstOrDefault @4068; Pow @4071; GetInt64 @4072 | FROM price_offers @4055; JOIN items @4055 |
| <span id="m-7faa1cdf5201"></span><code>MainViewModel.SavePriceOfferAsync()</code><br>4077–4094 | CheckSessionUnlocked @4079; TryParse @4080; ToString @4080; Round @4080; Pow @4080; IsNullOrWhiteSpace @4081; ConfigureAwait(SavePriceOfferCommand, Guid) @4090; ExecuteAsync(SavePriceOfferCommand, Guid) @4090; ReportError @4091; DispatchToUi @4092; ConfigureAwait @4093; LoadPriceOffersAsync @4093 | No extracted literal effects. |
| <span id="m-854c830006e5"></span><code>MainViewModel.TogglePriceOfferAsync(PriceOfferRow)</code><br>4096–4104 | CheckSessionUnlocked @4098; ConfigureAwait(SetPriceOfferStatusCommand, bool) @4100; ExecuteAsync(SetPriceOfferStatusCommand, bool) @4100; ReportError @4102; ConfigureAwait @4103; LoadPriceOffersAsync @4103 | No extracted literal effects. |
| <span id="m-9053d93ac7d4"></span><code>MainViewModel.LoadPriceOffersAsync()</code><br>4106–4145 | CreateCommand @4111; ConfigureAwait @4121; ExecuteReaderAsync @4121; ReadAsync @4122; Add @4124; Parse @4125; GetString @4125; GetDouble @4129; GetInt64 @4132; IsDBNull @4133; GetInt32 @4135; DispatchToUi @4138; Clear @4140; Add @4141 | FROM price_offers @4112; JOIN items @4112; JOIN product_categories @4112 |
| <span id="m-6cfe858c8b78"></span><code>MainViewModel.LoadPendingShelfLabelsAsync()</code><br>4147–4186 | CreateCommand @4152; ConfigureAwait @4161; ExecuteReaderAsync @4161; ReadAsync @4162; Add @4164; Parse @4165; GetString @4165; GetInt64 @4169; GetInt32 @4174; Add @4175; Remove @4175; RaisePropertyChanged @4175; nameof @4175; Localize @4176; DispatchToUi @4179; Clear @4181; Add @4182 | FROM pending_shelf_labels @4153; JOIN items @4153 |
| <span id="m-4efe1a1bc0be"></span><code>MainViewModel.LoadKitPriceReviewAlertsAsync()</code><br>4188–4227 | CreateCommand @4193; ConfigureAwait @4205; ExecuteReaderAsync @4205; ReadAsync @4206; Add @4208; Parse @4209; GetString @4209; GetInt64 @4213; GetInt32 @4217; DispatchToUi @4220; Clear @4222; Add @4223 | FROM kit_price_review_alerts @4194; JOIN items @4194 |
| <span id="m-6a39b18d2b0c"></span><code>MainViewModel.SetKitPriceAlertStatusAsync(KitPriceAlertRow,string,string)</code><br>4229–4237 | CheckSessionUnlocked @4231; ConfigureAwait(ResolveKitPriceAlertCommand, bool) @4232; ExecuteAsync(ResolveKitPriceAlertCommand, bool) @4232; ReportError @4234; ConfigureAwait @4236; LoadKitPriceReviewAlertsAsync @4236 | No extracted literal effects. |
| <span id="m-3e11bf60f8d1"></span><code>MainViewModel.MarkShelfLabelsPrintedAsync()</code><br>4239–4242 | ConfigureAwait @4241; SetSelectedShelfLabelStatusAsync @4241 | No extracted literal effects. |
| <span id="m-5cece5486fd3"></span><code>MainViewModel.QueueSelectedShelfLabelsAsync()</code><br>4244–4256 | CheckSessionUnlocked @4246; ToArray @4247; Select @4247; Where @4247; Contains @4247; ConfigureAwait(QueueShelfLabelPrintCommand, string) @4250; ExecuteAsync(QueueShelfLabelPrintCommand, string) @4250; ReportError @4252; Clear @4253; RaisePropertyChanged @4253; nameof @4253; ConfigureAwait @4255; LoadPendingShelfLabelsAsync @4255 | No extracted literal effects. |
| <span id="m-b67cea2d4a74"></span><code>MainViewModel.SetSelectedShelfLabelStatusAsync(string)</code><br>4258–4272 | CheckSessionUnlocked @4260; ToArray @4261; Select @4261; Where @4261; Contains @4261; ConfigureAwait(SetShelfLabelStatusCommand, int) @4264; ExecuteAsync(SetShelfLabelStatusCommand, int) @4264; Trim @4265; ReportError @4267; Clear @4268; RaisePropertyChanged @4269; nameof @4269; ConfigureAwait @4271; LoadPendingShelfLabelsAsync @4271 | No extracted literal effects. |
| <span id="m-84070a2a4cd2"></span><code>MainViewModel.AddSqlParam(DbCommand,string,object)</code><br>4278–4284 | CreateParameter @4280; Add @4283 | No extracted literal effects. |

</details>

## MainViewModel.ThirdPartyImport.cs {#src-63148b75a5e2}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdPartyImport.cs</code> · 262 lines.

SHA-256: <code>4e3306a908d0e3fe8bbb2c78f62468fd601cbc5ab1a8896e66e90239e0a262b7</code>.

Declarations: <code>MainViewModel</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-1f14c7360e7b"></span><code>MainViewModel.OpenThirdPartyImport()</code><br>116–130 | CheckSessionUnlocked @118; Increment @125; ResetThirdPartyImport @127; Invoke @129 | No extracted literal effects. |
| <span id="m-9fb52a37592b"></span><code>MainViewModel.PreviewThirdPartyImportFileAsync(string)</code><br>132–188 | Increment @135; ResetThirdPartyImport @139; IsNullOrWhiteSpace @142; Exists @142; ConfigureAwait @155; ReadAllBytesAsync @155; ToHexStringLower @156; HashData @156; ReadThirdPartiesAsync @157; ValidateThirdPartiesAsync @164; TemplateContextAsync @165; CompletedWorkbook @166; DispatchToUi @167; ReferenceEquals @169; SetImportReviewRows @170; ToArray @170; Select @170; Clear @174; Add @175; Clear @176; Add @177; RaisePropertyChanged @178; nameof @178; Localize @179; SafeError @185 | No extracted literal effects. |
| <span id="m-4e3fd7b60eb2"></span><code>MainViewModel.ConfirmThirdPartyImportAsync()</code><br>190–239 | ConfigureAwait(ImportThirdPartiesCommand, ImportThirdPartiesResult) @209; ExecuteAsync(ImportThirdPartiesCommand, ImportThirdPartiesResult) @209; ReportError @216; DispatchToUi @217; Localize @222; Invoke @228; ConfigureAwait @230; LoadThirdPartiesAsync @230; LoadThirdPartiesLegacyListsAsync @231; ReportException @235 | No extracted literal effects. |
| <span id="m-1affd789406b"></span><code>MainViewModel.CancelThirdPartyImport()</code><br>241–247 | ResetThirdPartyImport @246 | No extracted literal effects. |
| <span id="m-bf31d1955c25"></span><code>MainViewModel.ResetThirdPartyImport()</code><br>249–259 | Clear @256; Clear @257; RaisePropertyChanged @258; nameof @258 | No extracted literal effects. |

</details>

## MainViewModel.cs {#src-16497b924a99}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 12,737 lines.

SHA-256: <code>aa07125e84d7ad377e50d9ef5796e8e6c8b93ffe93b4b61142908213afa35625</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 8381).

<details markdown>
<summary>Methods, calls, table effects and failures (253)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4d3c549b9d46"></span><code>MainViewModel.RefreshCurrentTime()</code><br>121–121 | RaisePropertyChanged @121; nameof @121 | No extracted literal effects. |
| <span id="m-47378cde4176"></span><code>MainViewModel.SetStatusNotificationOnUi(string)</code><br>391–404 | RaiseAndSetIfChanged @393; IsNullOrWhiteSpace @394; Insert @396; RemoveAt @397; RaisePropertyChanged @398; nameof @398; Stop @401; Start @403 | No extracted literal effects. |
| <span id="m-fa69ff5d121c"></span><code>MainViewModel.ClearNotifications()</code><br>426–433 | Stop @428; Clear @430; RaisePropertyChanged @431; nameof @431; RaiseAndSetIfChanged @432 | No extracted literal effects. |
| <span id="m-1aafdc317eca"></span><code>MainViewModel.CycleInventoryLifecycleStatusScope()</code><br>677–682 | — | No extracted literal effects. |
| <span id="m-0f212c412d70"></span><code>MainViewModel.IsLockScreenLockedOut(int)</code><br>1182–1198 | Ceiling @1189 | No extracted literal effects. |
| <span id="m-12ac067d00d0"></span><code>MainViewModel.RefreshUnlockCandidates()</code><br>1240–1265 | GetUnlockCandidates @1243; Clear @1246; Add @1249; Any @1251; CheckAccess @1257; action @1259; Post @1263 | No extracted literal effects. |
| <span id="m-b92965f7a2ce"></span><code>MainViewModel.UpdateReceiveKitBreakdownAsync()</code><br>1623–1643 | GetValueOrDefault @1631; ConfigureAwait @1636; BuildBreakdownSummaryAsync @1636 | No extracted literal effects. |
| <span id="m-7b354fe59de3"></span><code>MainViewModel.UpdateCartKitBreakdownAsync(OrderItem)</code><br>1645–1657 | ConfigureAwait @1650; BuildBreakdownSummaryAsync @1650 | No extracted literal effects. |
| <span id="m-0af9554a083f"></span><code>MainViewModel.OnProductPricingDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>2082–2101 | RaisePropertyChanged @2084; nameof @2084; RecomputeProductPricingPreview @2100 | No extracted literal effects. |
| <span id="m-be2cd1f33f20"></span><code>MainViewModel.RecomputeProductPricingPreview()</code><br>2110–2160 | Clear @2112; RaisePropertyChanged @2113; nameof @2113; ToMinorUnits @2122; Parse @2127; TryParse @2131; Equals @2145; Increment @2148; Localize @2149; ToArray @2151; RecomputeKitPricingPreviewAsync @2152; ResolveSelectedProductSaleUnitFactor @2157; Round @2158; RebuildProductPricingPreview @2159 | No extracted literal effects. |
| <span id="m-ff2e9cd489e5"></span><code>MainViewModel.RecomputeKitPricingPreviewAsync(long,string,string,decimal,string,long,decimal,IReadOnlyList&lt;KitComponentDraftItem&gt;)</code><br>2162–2232 | ConfigureAwait @2166; WaitAsync @2166; Read @2169; DispatchToUi @2173; SetProductPricingPreviewNotice @2173; CalculateItemOrKitAsync @2187; ResolveSelectedProductSaleUnitFactor @2211; Round @2212; RebuildProductPricingPreview @2216; Release @2230 | No extracted literal effects. |
| <span id="m-7c7ae546e576"></span><code>MainViewModel.SetProductPricingPreviewNotice(string)</code><br>2234–2238 | Localize @2236; RaisePropertyChanged @2237; nameof @2237 | No extracted literal effects. |
| <span id="m-c21c8b6c7457"></span><code>MainViewModel.RebuildProductPricingPreview(long,string,decimal,string,long,decimal)</code><br>2240–2304 | Clear @2243; RaisePropertyChanged @2245; nameof @2245; Equals @2246; SetProductPricingPreviewNotice @2248; ParsePricingMethod @2252; ParseRoundingRule @2253; IsRoundingRuleCompatible @2254; TryConvertRoundingIncrement @2261; ToMinorUnits @2268; ResolveEffectiveBasePrice @2269; ToList @2273; OrderBy @2273; Where @2273; FirstOrDefault @2280; TryParse @2291; ToString @2292; ResolveTierPrice @2295; Add @2297; Format @2299; ToDisplayAmount @2299; FirstOrDefault @2300 | No extracted literal effects. |
| <span id="m-1cd827d295b1"></span><code>MainViewModel.ResolveSelectedProductSaleUnitFactor()</code><br>2358–2373 | FirstOrDefault @2361; Equals @2361; TryParse @2365 | No extracted literal effects. |
| <span id="m-05f7970ff4a8"></span><code>MainViewModel.ExactMinorToCurrency(decimal)</code><br>2381–2382 | ScalingFactor @2382; Clamp @2382 | No extracted literal effects. |
| <span id="m-6dc1ced58792"></span><code>MainViewModel.BuildCostSourcesTooltip(long,long,long,long?,string,DateTime?)</code><br>2439–2459 | Format @2447; ToDecimal @2448; Localize @2451; Format @2451; ToLocalTime @2453; Join @2458 | No extracted literal effects. |
| <span id="m-5ad09108deec"></span><code>MainViewModel.AddKitComponent()</code><br>2619–2656 | IsNullOrWhiteSpace @2634; FirstOrDefault @2636; Equals @2637; Add @2644; RaisePropertyChanged @2655; nameof @2655 | No extracted literal effects. |
| <span id="m-630728ee8eac"></span><code>MainViewModel.RemoveKitComponent(KitComponentDraftItem?)</code><br>2658–2665 | Remove @2662; RaisePropertyChanged @2663; nameof @2663 | No extracted literal effects. |
| <span id="m-0c57d150cd50"></span><code>MainViewModel.RefreshVirtualKitAvailability()</code><br>2676–2689 | Increment @2678; ToArray @2685; Select @2685; LoadVirtualKitAvailabilityAsync @2688 | No extracted literal effects. |
| <span id="m-516d1c97b8a7"></span><code>MainViewModel.LoadVirtualKitAvailabilityAsync(long,IReadOnlyList&lt;KitComponentInput&gt;)</code><br>2691–2731 | ConfigureAwait @2695; GetKitAvailabilityAsync @2695; DispatchToUi @2697; Read @2699; Localize @2702; Max @2711; ResolveSelectedProductSaleUnitFactor @2711; GetValueOrDefault @2712; Clamp @2713; Pow @2714; Floor @2715; Format @2717; ToString @2719 | No extracted literal effects. |
| <span id="m-6c6ee75d833b"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3511–3519 | IsNullOrWhiteSpace @3513 | No extracted literal effects. |
| <span id="m-80e79547bc72"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3521–3532 | Load @3523; IsNullOrWhiteSpace @3527; Resolve @3529; Apply @3531 | No extracted literal effects. |
| <span id="m-faae49055ff5"></span><code>MainViewModel.OpenImport()</code><br>3561–3575 | CheckSessionUnlocked @3563; Increment @3566; Clear @3570; Invoke @3574 | No extracted literal effects. |
| <span id="m-01a2e540e687"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3577–3634 | Increment @3580; Clear @3588; IsNullOrWhiteSpace @3594; Exists @3594; ConfigureAwait @3608; ReadAllBytesAsync @3608; ToHexString @3609; HashData @3609; TemplateContextAsync @3613; Run @3614; Read @3614; ValidateInventoryAsync @3615; CompletedWorkbook @3616; DispatchToUi @3617; ReferenceEquals @3619; Add @3620; Localize @3621; SetImportReviewRows @3624; RaisePropertyChanged @3625; nameof @3625; SafeError @3631 | No extracted literal effects. |
| <span id="m-13fca803335f"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3636–3692 | ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3663; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3663; Localize @3669; DispatchToUi @3670; Invoke @3676; ConfigureAwait @3678; LoadInventoryAsync @3678; ReportError @3682; ReportException @3688 | No extracted literal effects. |
| <span id="m-0cd6482b12e7"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3704–3714 | Report @3706; DispatchToUi @3707; Insert @3709 | No extracted literal effects. |
| <span id="m-c02025c30e47"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3716–3720 | RaisePropertyChanged @3719; nameof @3719 | No extracted literal effects. |
| <span id="m-8ea2fbc0e65e"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3722–3725 | ReportError @3724 | No extracted literal effects. |
| <span id="m-1c2267d9e419"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3731–3736 | ReportError @3734 | No extracted literal effects. |
| <span id="m-3a77f92bdcb5"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3745–3751 | IsNullOrWhiteSpace @3747; Trim @3747; ReportError @3749 | No extracted literal effects. |
| <span id="m-fb45f0c623e9"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3753–3756 | DispatchToUi @3755; Insert @3755 | No extracted literal effects. |
| <span id="m-d38288e801fc"></span><code>MainViewModel.DispatchToUi(Action)</code><br>3762–3776 | CheckAccess @3764; action @3766; GetResult @3774; GetAwaiter @3774; InvokeAsync @3774 | No extracted literal effects. |
| <span id="m-89336099d270"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4291–4354 | Register @4293; Execute @4293; Execute @4294; Execute @4299; Execute @4300; Execute @4301; Execute @4302; Execute @4303; Execute @4304; Execute @4305; Execute @4306; Execute @4307; Execute @4308; Execute @4309; Execute @4310; Execute @4311; Execute @4312; Execute @4313; Execute @4314; Execute @4315; Execute @4316; Execute @4317; Execute @4318; Execute @4319; Execute @4320; Execute @4321; Execute @4322; Execute @4323; Execute @4324; Execute @4325; Execute @4326; Execute @4327; Execute @4328; Execute @4329; Execute @4330; Execute @4332; Execute @4333; RequestClosePersonForm @4334; KeepEditingPersonForm @4335; CloseSalaryMonthDetailModal @4336; CloseSalaryPaymentModal @4337; CloseSalaryAdjustmentModal @4338; CloseSalaryFinalizeModal @4339; RequestCloseExpenseForm @4340; KeepEditingExpenseForm @4341; CloseExpenseCategoryModal @4342; CloseExpensePaymentModal @4343; CloseExpenseDetailModal @4344; ClosePaymentReturnModal @4345; CloseWasteExpenseConfirmation @4346; InitializeSalaryTables @4351; InitializeExpensesTables @4352; InitializeTeamsCommands @4353 | No extracted literal effects. |
| <span id="m-4086ec034c15"></span><code>MainViewModel.CreateDemo()</code><br>4356–4363 | SetActiveCashier @4359; Parse @4359; RefreshUnlockCandidates @4361 | No extracted literal effects. |
| <span id="m-449a80f95251"></span><code>MainViewModel.CreateInitializing()</code><br>4365–4373 | — | No extracted literal effects. |
| <span id="m-ad59836a87f0"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4375–4385 | — | No extracted literal effects. |
| <span id="m-4f55aedeaa88"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4387–4405 | ConfigureDiagnosticsWorkspace @4401; ApplyPersistedState @4402; RefreshUnlockCandidates @4403 | No extracted literal effects. |
| <span id="m-ad29341abdb9"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4407–4435 | CheckSessionUnlocked @4409; HasPermission @4410; Equals @4421; GetFileNameWithoutExtension @4421; GetEntryAssembly @4423; Add @4425; Start @4428; ReportException @4433 | No extracted literal effects. |
| <span id="m-a3a6175b1cc4"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4437–4460 | CheckSessionUnlocked @4439; HasPermission @4440; Equals @4450; GetFileNameWithoutExtension @4450; Add @4451; GetEntryAssembly @4451; Start @4453; ReportException @4458 | No extracted literal effects. |
| <span id="m-fe9d10950f9b"></span><code>MainViewModel.Dispose()</code><br>4462–4481 | Increment @4464; ResetFinancialWorkspace @4466; Dispose @4467; Stop @4468; CancelBatchPricingPreviewExpiry @4471; Dispose @4472; Dispose @4473; DisposeSearchStates @4479; SuppressFinalize @4480 | No extracted literal effects. |
| <span id="m-34c887c8963d"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4483–4487 | Stop @4485 | No extracted literal effects. |
| <span id="m-d345d6d0872a"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4489–4527 | Clear @4499; Clear @4500; Clear @4501; Clear @4502; Clear @4503; Clear @4504; Clear @4505; Clear @4506; Clear @4507; Clear @4508 | No extracted literal effects. |
| <span id="m-4f75ef3115aa"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4529–4632 | RaisePropertyChanged @4543; nameof @4543; Clear @4545; Clear @4546; Clear @4547; CreateCommand @4554; ExecuteReader @4556; Read @4557; TryParse @4559; GetString @4559; Add @4560; Add @4568; GroupBy @4569; Count @4571; Contains @4576; Add @4593; Add @4594; SetActiveCashier @4602; ToString @4606; ToString @4609; ToLocalTime @4609; NotifyTotalsChanged @4631 | FROM item_kits @4555 |
| <span id="m-e8353a9df544"></span><code>MainViewModel.InitializeDemoData()</code><br>4634–4714 | Add @4640; Add @4659; Add @4672; Add @4676; Add @4681; Add @4687; ApplyActivityFilter @4693; Add @4696; ApplyInventoryFilter @4705; Add @4708; Parse @4708; NotifyTotalsChanged @4713 | No extracted literal effects. |
| <span id="m-74bf5680eb6a"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>4716–4729 | — | No extracted literal effects. |
| <span id="m-028bbff05708"></span><code>MainViewModel.SelectMenu(string)</code><br>4731–4802 | CheckSessionUnlocked @4733; NormalizeMenuKey @4737; LoadInvoicesAsync @4743; LoadCommercialAsync @4744; LoadActivityInvoicesAsync @4751; LoadTeamsStaffAsync @4754; LoadCatalogRegistryAsync @4755; UpdateDemoSeedingAvailabilityAsync @4758; UpdateReceiptDesignPreview @4761; RefreshDiagnosticsAsync @4762; LoadPriceLevelSettingsAsync @4763; LoadInventoryAsync @4766; LoadPriceProposalsAsync @4768; LoadReportDataAsync @4771; LoadFinancialRegisterAsync @4772; LoadCustomersAsync @4775; LoadSuppliersAsync @4776; LoadThirdPartiesAsync @4777; LoadManufacturingDataAsync @4782; LoadManagedUnitsAsync @4790; LoadManagedCategoriesAsync @4793; LoadSalaryWorkspaceAsync @4796; LoadExpensesWorkspaceAsync @4799 | No extracted literal effects. |
| <span id="m-5696de4d0be3"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>4804–4823 | — | No extracted literal effects. |
| <span id="m-fa00f275dd4a"></span><code>MainViewModel.LogOut()</code><br>4825–4841 | ClearNotifications @4827; ResetCashReview @4831; RaisePropertyChanged @4833; nameof @4833; Lock @4834; RefreshUnlockCandidates @4839; UpdateDemoSeedingAvailabilityAsync @4840 | No extracted literal effects. |
| <span id="m-3b9e75e6f524"></span><code>MainViewModel.UnlockSession()</code><br>4843–4846 | UnlockSession @4845 | No extracted literal effects. |
| <span id="m-a68c4147a377"></span><code>MainViewModel.UnlockSession(string?)</code><br>4848–4947 | IsLockScreenLockedOut @4856; IsNullOrWhiteSpace @4872; AuthenticateSelectedUser @4881; Lock @4886; AddSeconds @4892; AddMinutes @4909; Initialize @4928; Unlock @4929; Any @4933; Equals @4933; RaisePropertyChanged @4934; nameof @4934; LoadActivityInvoicesAsync @4938; LoadTrackOrdersAsync @4939; UpdateDemoSeedingAvailabilityAsync @4940; StartAutomaticDemoDatasetLoadAsync @4941 | No extracted literal effects. |
| <span id="m-c6ba417a071b"></span><code>MainViewModel.PowerAction()</code><br>4949–4955 | CheckSessionUnlocked @4951 | No extracted literal effects. |
| <span id="m-88ad292984ef"></span><code>MainViewModel.CycleTable()</code><br>4957–4963 | CheckSessionUnlocked @4959 | No extracted literal effects. |
| <span id="m-bf5f27fbb4d7"></span><code>MainViewModel.CycleDiningType()</code><br>4965–4971 | CheckSessionUnlocked @4967 | No extracted literal effects. |
| <span id="m-4f414b87a28f"></span><code>MainViewModel.CycleCustomer()</code><br>4973–4976 | OpenCustomerChooser @4975 | No extracted literal effects. |
| <span id="m-d5e3a7fd3e8f"></span><code>MainViewModel.OpenPromoDialog()</code><br>4978–4993 | CheckSessionUnlocked @4980; IsNullOrWhiteSpace @4987; RaisePropertyChanged @4991; nameof @4991 | No extracted literal effects. |
| <span id="m-4d8578916832"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>4995–5064 | CheckSessionUnlocked @4997; ToLowerInvariant @5010; Trim @5010; IsNullOrWhiteSpace @5017; Trim @5017; ToList @5025; Select @5025; ToMinorUnits @5029; Equals @5045; Calculate @5049; NotifyTotalsChanged @5061; ConfigureAwait @5063; SaveDurableCartAsync @5063 | No extracted literal effects. |
| <span id="m-d52acd92b7d3"></span><code>MainViewModel.TogglePromo()</code><br>5066–5083 | CheckSessionUnlocked @5068; RemovePromo @5077; OpenPromoDialog @5081 | No extracted literal effects. |
| <span id="m-ee4f707848f3"></span><code>MainViewModel.RemovePromo()</code><br>5085–5095 | NotifyTotalsChanged @5092; SaveDurableCartAsync @5094 | No extracted literal effects. |
| <span id="m-a16b7aee3338"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5097–5108 | CheckSessionUnlocked @5099; NotifyTotalsChanged @5105; ConfigureAwait @5107; SaveDurableCartAsync @5107 | No extracted literal effects. |
| <span id="m-62e0fbfbfd1a"></span><code>MainViewModel.CancelPromoDialog()</code><br>5110–5114 | — | No extracted literal effects. |
| <span id="m-92270bfb2b37"></span><code>MainViewModel.RecalculateCart()</code><br>5116–5170 | ToMinorUnits @5132; Add @5133; Equals @5154; Calculate @5158; ToDictionary @5161; TryGetValue @5164 | No extracted literal effects. |
| <span id="m-a6728c8bc6d6"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5172–5179 | CheckSessionUnlocked @5174; ResetCashReview @5175 | No extracted literal effects. |
| <span id="m-24d80d2bb6a6"></span><code>MainViewModel.SelectCategory(CategoryItem)</code><br>5181–5189 | CheckSessionUnlocked @5183; ApplyFilter @5187 | No extracted literal effects. |
| <span id="m-c1ad58638c55"></span><code>MainViewModel.ApplyFilter()</code><br>5191–5213 | FirstOrDefault @5193; Clear @5196; AsEnumerable @5197; Where @5201; Equals @5201; IsNullOrWhiteSpace @5204; Contains @5206; Add @5211 | No extracted literal effects. |
| <span id="m-47aafd71d70f"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5215–5215 | AddToCart @5215 | No extracted literal effects. |
| <span id="m-eee5c61045e4"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5217–5255 | CheckSessionUnlocked @5219; ResetCashReview @5220; ResolveProductSaleUnitFactor @5223; Round @5230; FirstOrDefault @5231; UpdateCartKitBreakdownAsync @5235; Add @5246; NotifyTotalsChanged @5249; SaveDurableCartAsync @5251; IsNullOrWhiteSpace @5253; ToString @5253; NewGuid @5253; RecordSuccessfulSearchUseAsync @5254; FromGuid @5254 | No extracted literal effects. |
| <span id="m-e63392e3264e"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5257–5265 | CheckSessionUnlocked @5259; ResetCashReview @5260; UpdateCartKitBreakdownAsync @5262; NotifyTotalsChanged @5263; SaveDurableCartAsync @5264 | No extracted literal effects. |
| <span id="m-6ec891a7af44"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5267–5282 | CheckSessionUnlocked @5269; ResetCashReview @5270; UpdateCartKitBreakdownAsync @5274; Remove @5278; NotifyTotalsChanged @5280; SaveDurableCartAsync @5281 | No extracted literal effects. |
| <span id="m-db094b836abb"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5284–5290 | ConfigureAwait @5287; LoadAsync @5287; RefreshSavedPaymentImages @5288; CancelManualPaymentSettings @5289 | No extracted literal effects. |
| <span id="m-02adda10a49e"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5292–5321 | ValidImage @5299; CreatePaymentBitmap @5304; Dispose @5307; RaisePropertyChanged @5319; nameof @5319 | No extracted literal effects. |
| <span id="m-1571bfa89a2f"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5323–5339 | Dispose @5333; CreatePaymentBitmap @5335; RaisePropertyChanged @5337; nameof @5337 | No extracted literal effects. |
| <span id="m-ba50cfe0204b"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5341–5345 | — | No extracted literal effects. |
| <span id="m-3fd522fe125f"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5347–5355 | Dispose @5349; CreatePaymentBitmap @5351; RaisePropertyChanged @5353; nameof @5353 | No extracted literal effects. |
| <span id="m-939e8e0b15b5"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5357–5376 | ConfigureAwait @5366; ExecuteAsync @5366; DispatchToUi @5369; SafePipelineError @5369; LoadAsync @5372; RefreshSavedPaymentImages @5373; CancelManualPaymentSettings @5374 | No extracted literal effects. |
| <span id="m-82fb35c0edf9"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5378–5397 | IsNullOrWhiteSpace @5382; Trim @5383; ToMinorUnits @5389; ConfigureAwait @5395; PlaceOrderAsync @5395 | No extracted literal effects. |
| <span id="m-061003ac43cd"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5399–5599 | Localize @5403; ExecuteDemoPlaceOrder @5409; ConfigureAwait @5435; SaveDurableCartAsync @5435; ToMinorUnits @5443; Trim @5445; Equals @5456; Equals @5463; ResetCashReview @5465; Max @5523; Add @5528; ConfigureAwait(TakePaymentCommand, SalesInvoice) @5546; ExecuteAsync(TakePaymentCommand, SalesInvoice) @5546; Format @5558; ToDecimal @5558; DispatchToUi @5560; Clear @5563; NewGuid @5572; NotifyTotalsChanged @5573; LoadActivityInvoicesAsync @5580; OpenStaleCartPriceReviewAsync @5585; RequestElevationForCheckout @5587; SafePipelineError @5591; SafeError @5597 | No extracted literal effects. |
| <span id="m-8578a0367914"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>5601–5633 | DispatchToUi @5605; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5608; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5608; SafePipelineError @5613; ToArray @5617; Select @5617; Where @5617; FormatCartReviewMoney @5621; Clear @5628; Add @5629 | No extracted literal effects. |
| <span id="m-0fed945e42ec"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>5635–5640 | ScalingFactor @5637; Format @5639; Equals @5639 | No extracted literal effects. |
| <span id="m-eb01bdcd96e8"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>5642–5673 | CheckSessionUnlocked @5644; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5646; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5646; DispatchToUi @5651; SafePipelineError @5651; ConfigureAwait @5652; OpenStaleCartPriceReviewAsync @5652; FirstOrDefault @5659; ScalingFactor @5662; ResetCashReview @5666; Clear @5669; NotifyTotalsChanged @5670 | No extracted literal effects. |
| <span id="m-cfc7204a1848"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>5675–5682 | Clear @5679; ResetCashReview @5680 | No extracted literal effects. |
| <span id="m-f07797d39662"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>5684–5710 | CheckSessionUnlocked @5686; ResetCashReview @5693; ToMinorUnits @5704; ConfigureAwait @5709; PlaceOrderAsync @5709 | No extracted literal effects. |
| <span id="m-f37488a54182"></span><code>MainViewModel.CancelCashReview()</code><br>5712–5716 | ResetCashReview @5714 | No extracted literal effects. |
| <span id="m-3822c9148afa"></span><code>MainViewModel.ResetCashReview()</code><br>5718–5727 | — | No extracted literal effects. |
| <span id="m-89cf6dac6c5b"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>5729–5748 | RaisePropertyChanged @5740; nameof @5740; Clear @5743; ResetCashReview @5744; NotifyTotalsChanged @5745 | No extracted literal effects. |
| <span id="m-ded1de68f6b3"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>5750–5815 | ConfigureAwait @5754; WaitAsync @5754; ClearActiveCartAsync @5759; ToMinorUnits @5769; Add @5770; ToUpperInvariant @5773; ToString @5773; IsNullOrWhiteSpace @5776; SaveActiveCartAsync @5789; DispatchToUi @5808; SafeError @5808; Release @5813 | No extracted literal effects. |
| <span id="m-39abb8a708ea"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>5817–5872 | ConfigureAwait @5823; GetActiveCartAsync @5823; Clear @5835; FirstOrDefault @5838; ToDecimal @5842; Add @5848; NotifyTotalsChanged @5865 | No extracted literal effects. |
| <span id="m-109cda40d546"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>5874–5951 | ApplyPagedResult @5878; ToList @5879; ApplyActivityFilter @5883; HasPermission @5888; ConfigureAwait @5895; GetPagedActivityInvoicesAsync @5895; ToPageRequest @5898; ToDecimal @5904; Add @5905; ToString @5910; ToLocalTime @5910; DispatchToUi @5929; Clear @5931; Add @5934; SafeError @5948 | No extracted literal effects. |
| <span id="m-fc5602230929"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>5953–6030 | HasPermission @5958; ConfigureAwait @5965; GetActiveOrdersAsync @5965; Clear @5966; ToDecimal @5970; Join @6004; Select @6004; Add @6006; ToString @6021; ToLocalTime @6021 | No extracted literal effects. |
| <span id="m-97aa05e3729d"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6032–6059 | CheckSessionUnlocked @6034; Clear @6037; ConfigureAwait @6043; GetOrderByIdAsync @6043; Add @6048; DispatchToUi @6054; SafeError @6054 | No extracted literal effects. |
| <span id="m-dc2afb594e8d"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6061–6066 | Clear @6065 | No extracted literal effects. |
| <span id="m-ccf2b8f7f7ce"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6068–6101 | CheckSessionUnlocked @6070; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6086; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6086; ConfigureAwait @6095; LoadTrackOrdersAsync @6095; DispatchToUi @6099; SafePipelineError @6099 | No extracted literal effects. |
| <span id="m-47ac78b22984"></span><code>MainViewModel.MarkReadyAsync()</code><br>6103–6136 | CheckSessionUnlocked @6105; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6121; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6121; ConfigureAwait @6130; LoadTrackOrdersAsync @6130; DispatchToUi @6134; SafePipelineError @6134 | No extracted literal effects. |
| <span id="m-515fc3512d96"></span><code>MainViewModel.MarkServedAsync()</code><br>6138–6171 | CheckSessionUnlocked @6140; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6156; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6156; ConfigureAwait @6165; LoadTrackOrdersAsync @6165; DispatchToUi @6169; SafePipelineError @6169 | No extracted literal effects. |
| <span id="m-0a8b4d09afdf"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6173–6201 | CheckSessionUnlocked @6175; Remove @6179; CloseOrderDetailsModal @6180; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6189; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6189; ConfigureAwait @6195; LoadTrackOrdersAsync @6195; DispatchToUi @6199; SafePipelineError @6199 | No extracted literal effects. |
| <span id="m-a436246c2b73"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6203–6299 | CheckSessionUnlocked @6205; CloseOrderDetailsModal @6211; ConfigureAwait @6218; GetOrderByIdAsync @6218; Zero @6240; NewGuid @6246; ToList @6249; Select @6249; ToUpperInvariant @6252; ToString @6252; SaveActiveCartAsync @6261; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6277; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6277; DispatchToUi @6280; SafePipelineError @6280; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6286; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6286; LoadTrackOrdersAsync @6292; LoadActivityInvoicesAsync @6293 | No extracted literal effects. |
| <span id="m-787b09526cbe"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6301–6308 | CheckSessionUnlocked @6303 | No extracted literal effects. |
| <span id="m-930e62eef3d1"></span><code>MainViewModel.FilterActivity(string)</code><br>6327–6333 | CheckSessionUnlocked @6329; ApplyActivityFilter @6331 | No extracted literal effects. |
| <span id="m-2f940098ce83"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6335–6374 | Clear @6337; AsEnumerable @6338; Where @6343; IsNullOrWhiteSpace @6346; Trim @6348; Contains @6350; Contains @6351; Contains @6352; IsNullOrEmpty @6356; Equals @6358; ToList @6362; Add @6364; ApplyPagedResult @6368 | No extracted literal effects. |
| <span id="m-9d1c6acdd001"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6376–6412 | CheckSessionUnlocked @6378; ConfigureAwait(QueueReceiptReprintCommand, string) @6398; ExecuteAsync(QueueReceiptReprintCommand, string) @6398; IsNullOrWhiteSpace @6399; ReportError @6401; RefreshOutputStatusAsync @6406; DispatchToUi @6410; SafeError @6410 | No extracted literal effects. |
| <span id="m-d7537cff1a6d"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6414–6457 | RefreshOutputPrinterQueues @6419; ReadAsync @6420; Equals @6427; IsNullOrWhiteSpace @6427; TryReadGeometry @6429; ComputeCapabilityFingerprint @6433; ConfigureAwait @6437; InvalidateThermalVerificationAsync @6437; LoadCashFinancialSettingsAsync @6449; LoadReceiptDesignAsync @6450; RefreshOutputStatusAsync @6451; DispatchToUi @6455; SafeError @6455 | No extracted literal effects. |
| <span id="m-f4563930548a"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6459–6485 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6472; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6472; ReportError @6475; LoadOutputDevicesAsync @6478; DispatchToUi @6483; SafeError @6483 | No extracted literal effects. |
| <span id="m-eee30274714a"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6487–6560 | Equals @6501; IsNullOrWhiteSpace @6506; IsWindows @6511; TryReadGeometry @6516; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6533; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6533; ReportError @6536; Render @6539; ToString @6540; ConfigureAwait @6541; Run @6541; Send @6541; ComputeCapabilityFingerprint @6542; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @6543; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @6543; RefreshOutputStatusAsync @6554; DispatchToUi @6558; SafeError @6558 | No extracted literal effects. |
| <span id="m-02e61bf2a151"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>6562–6599 | IsWindows @6576; IsNullOrWhiteSpace @6576; TryReadGeometry @6578; ComputeCapabilityFingerprint @6582; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @6583; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @6583; ReportError @6587; ConfigureAwait @6593; RefreshOutputStatusAsync @6593; DispatchToUi @6597; SafeError @6597 | InvalidOperationException @6577; InvalidOperationException @6581 |
| <span id="m-522df70af2a0"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>6601–6636 | CreateCommand @6606; ConfigureAwait @6615; ExecuteReaderAsync @6615; ReadAsync @6616; GetInt32 @6619; GetString @6619; GetInt64 @6619; Parse @6620; RaisePropertyChanged @6622; nameof @6622; NotifyTotalsChanged @6629; DispatchToUi @6634; SafeError @6634 | FROM store_config @6607 |
| <span id="m-3b60c6741fed"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>6638–6666 | ConfigureAwait @6651; ExecuteAsync @6651; ReportError @6654; NotifyTotalsChanged @6659; DispatchToUi @6664; SafeError @6664 | No extracted literal effects. |
| <span id="m-7c66dca9be42"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>6668–6712 | DispatchToUi @6672; CreateCommand @6677; ConfigureAwait @6683; ExecuteReaderAsync @6683; ReadAsync @6684; Deserialize(ReceiptDesignDocument) @6686; GetString @6686; SafeError @6705 | FROM receipt_designs @6678; JOIN receipt_design_versions @6678 |
| <span id="m-2cdcf5af5629"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>6714–6741 | ConfigureAwait @6727; ExecuteAsync @6727; ReportError @6732; DispatchToUi @6739; SafeError @6739 | No extracted literal effects. |
| <span id="m-2634ba8af789"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>6743–6755 | IsWindows @6745; Select @6746; Enumerate @6746; Empty(string) @6747; ToArray @6748; OrderBy @6748; Distinct @6748; Where @6748; Append @6748; IsNullOrWhiteSpace @6749; Clear @6753; Add @6754 | No extracted literal effects. |
| <span id="m-7f129bcec88f"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>6757–6815 | CheckAccess @6759; DispatchToUi @6761; CreateSampleData @6767; Equals @6773; IsWindows @6780; TryReadGeometry @6781; BuildPaperDocument @6790; RenderPreviewPngPages @6793; SetReceiptDesignPreviewPages @6795; Localize @6797; BuildThermalLines @6802; RenderPreviewPng @6804; Empty(byte[]) @6811; ReportException @6813 | No extracted literal effects. |
| <span id="m-bedde28761d8"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>6817–6822 | ShowReceiptDesignPreviewPage @6821 | No extracted literal effects. |
| <span id="m-9c9d39a846e8"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>6824–6830 | ShowReceiptDesignPreviewPage @6829 | No extracted literal effects. |
| <span id="m-da27ad6f963f"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>6832–6846 | RaisePropertyChanged @6843; nameof @6843 | No extracted literal effects. |
| <span id="m-e20d0743664f"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>6848–6877 | ReadAsync @6851; Localize @6854; CreateCommand @6856; ConfigureAwait @6858; ExecuteScalarAsync @6858; ToString @6858; IsNullOrWhiteSpace @6859; ExecuteReaderAsync @6873; ReadAsync @6874; Trim @6875; GetString @6875 | FROM hardware_jobs @6857; FROM hardware_jobs @6872 |
| <span id="m-719021945d68"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>6879–6895 | Clear @6881; AsEnumerable @6882; Where @6885; IsNullOrWhiteSpace @6887; Contains @6889; Contains @6890; Contains @6891; Add @6894 | No extracted literal effects. |
| <span id="m-b06bdacc3372"></span><code>MainViewModel.GenerateXReport()</code><br>6897–6916 | CheckSessionUnlocked @6899; ToString @6903; GenerateXReportInternalAsync @6915 | No extracted literal effects. |
| <span id="m-cd8258fbef14"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>6918–6933 | ConfigureAwait @6922; LoadReportDataAsync @6922; DispatchToUi @6931; SafeError @6931 | No extracted literal effects. |
| <span id="m-58f06d92c4fa"></span><code>MainViewModel.CloseShiftZReport()</code><br>6935–6938 | OpenCloseShiftModal @6937 | No extracted literal effects. |
| <span id="m-124cde0d6aae"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>6940–6949 | CheckSessionUnlocked @6947 | No extracted literal effects. |
| <span id="m-0d2f6af568a7"></span><code>MainViewModel.SaveSettings()</code><br>6951–6955 | CheckSessionUnlocked @6953 | No extracted literal effects. |
| <span id="m-7d85a444771b"></span><code>MainViewModel.ApplySettingsAsync()</code><br>6957–7044 | CheckSessionUnlocked @6966; NotifyTotalsChanged @6985; ExecuteAsync @7013; DispatchToUi @7037; SafePipelineError @7037; SafeError @7042 | No extracted literal effects. |
| <span id="m-7d506866dc78"></span><code>MainViewModel.CancelSettings()</code><br>7046–7067 | CheckSessionUnlocked @7048; NotifyTotalsChanged @7060 | No extracted literal effects. |
| <span id="m-d3fac4a8fdb0"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7070–7100 | ProbeDatabaseAsync @7083; ProbeLicense @7089; RefreshOutputStatusAsync @7092; ProbeHardwareStubs @7093; DispatchToUi @7098; SafeError @7098 | No extracted literal effects. |
| <span id="m-11db44f201f1"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7161–7199 | RaisePropertyChanged @7163; nameof @7163; FormatRealResetPreviewSummary @7198 | No extracted literal effects. |
| <span id="m-eb8a390b02de"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7201–7214 | Localize @7202; ToString @7204; GetValueOrDefault @7204; ToString @7209; ToString @7210; ToString @7211 | No extracted literal effects. |
| <span id="m-cba8c997e11d"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7323–7415 | Post @7327; ConfigureAwait @7334; GetWorkspaceEnvironmentAsync @7334; Equals @7335; GetDatasetStateAsync @7337; CreateCommand @7343; CreateParameter @7350; ToString @7352; Add @7353; ExecuteScalarAsync @7354; HasPermission @7359; ToInt64 @7364; ExecuteScalarAsync @7364; ExecuteScalarAsync @7368; ExecuteScalarAsync @7375; ExecuteScalarAsync @7381; Localize @7400 | FROM items @7363; FROM sales_invoices @7367; FROM third_parties @7380; FROM users @7344; JOIN user_roles @7344 · DYNAMIC SQL: inspect manually |
| <span id="m-45bd419eac67"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>7417–7427 | CheckSessionUnlocked @7419; HasPermission @7420 | No extracted literal effects. |
| <span id="m-fb4b4015ac2e"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>7429–7434 | ConfigureAwait @7433; ResetDatabaseAsync @7433 | No extracted literal effects. |
| <span id="m-2959ae3afa22"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>7436–7437 | ConfigureAwait @7437; EnsureDefaultDemoDatasetAsync @7437 | No extracted literal effects. |
| <span id="m-d8b7cab724a3"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>7439–7445 | EnsureDefaultDemoDatasetAsync @7443 | No extracted literal effects. |
| <span id="m-9448199e0abc"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>7447–7551 | Localize @7452; ConfigureAwait @7459; WaitAsync @7459; GetWorkspaceEnvironmentAsync @7462; Equals @7463; HasPermission @7470; Post @7484; LocalizeDemoSeedProgress @7486; EnsureInitialDatasetAsync @7492; Join @7516; Select @7516; ReloadCatalogAsync @7526; LoadInventoryAsync @7527; LoadThirdPartiesAsync @7528; LoadManufacturingDataAsync @7529; LoadSuppliersAsync @7530; UpdateDemoSeedingAvailabilityAsync @7531; ToUpperInvariant @7536; ToString @7536; NewGuid @7536; LogDiagnosticError @7537; ReportError @7542; Release @7549 | No extracted literal effects. |
| <span id="m-35c4d9fb5034"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>7553–7567 | Localize @7555 | No extracted literal effects. |
| <span id="m-0c05853c9f76"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>7569–7664 | Localize @7573; ConfigureAwait @7577; WaitAsync @7577; HasPermission @7581; GetWorkspaceEnvironmentAsync @7588; Equals @7589; ResetDatabaseAsync @7597; GetStoreProfileAsync @7600; Post @7601; Clear @7604; Clear @7605; Clear @7606; NewGuid @7607; RaisePropertyChanged @7610; nameof @7610; Lock @7611; Defaults @7624; RefreshUnlockCandidates @7635; LoadCashFinancialSettingsAsync @7636; LoadOutputDevicesAsync @7637; LoadManualPaymentSettingsAsync @7638; LoadReceiptDesignAsync @7639; ReloadCatalogAsync @7640; LoadInventoryAsync @7641; LoadThirdPartiesAsync @7642; LoadManufacturingDataAsync @7643; LoadActivityInvoicesAsync @7644; UpdateDemoSeedingAvailabilityAsync @7645; ToUpperInvariant @7650; ToString @7650; LogDiagnosticError @7651; ReportError @7657; Release @7662 | No extracted literal effects. |
| <span id="m-5482af545edc"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>7666–7708 | CheckSessionUnlocked @7668; HasPermission @7670; ConfigureAwait @7678; GetWorkspaceEnvironmentAsync @7678; Equals @7679; PreviewAsync @7682; FormatRealResetPreviewSummary @7683; Post @7684; RaisePropertyChanged @7701; nameof @7701; SafeError @7706 | UnauthorizedAccessException @7680 |
| <span id="m-118d83be30d6"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>7710–7796 | HasPermission @7713; ConfigureAwait @7731; ExecuteAsync @7731; GetStoreProfileAsync @7740; Post @7743; Clear @7747; Clear @7748; Clear @7749; Clear @7750; NewGuid @7751; Lock @7754; RaisePropertyChanged @7768; nameof @7768; LoadCashFinancialSettingsAsync @7769; LoadOutputDevicesAsync @7770; LoadManualPaymentSettingsAsync @7771; LoadReceiptDesignAsync @7772; RefreshUnlockCandidates @7780; LoadInventoryAsync @7781; LoadActivityInvoicesAsync @7782; UpdateDemoSeedingAvailabilityAsync @7783; ToUpperInvariant @7788; ToString @7788; LogDiagnosticError @7789 | No extracted literal effects. |
| <span id="m-5b7c1b77331c"></span><code>MainViewModel.CancelRealShopReset()</code><br>7798–7805 | RaisePropertyChanged @7804; nameof @7804 | No extracted literal effects. |
| <span id="m-20eed4716e63"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>7809–7826 | ConfigureAwait @7811; ExportDocumentAsync @7811; Post @7815; GetFileName @7819 | No extracted literal effects. |
| <span id="m-8ccfb917a006"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>7828–7850 | Exists @7833; CreateDirectory @7835; Start @7837; ToUpperInvariant @7846; ToString @7846; NewGuid @7846; LogDiagnosticError @7847 | No extracted literal effects. |
| <span id="m-2de2e15a5035"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>7852–7862 | CheckSessionUnlocked @7854; RaisePropertyChanged @7856; nameof @7856; Localize @7858; ToString @7859 | No extracted literal effects. |
| <span id="m-9018ead51c2b"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>7869–7885 | CheckSessionUnlocked @7871; HasPermission @7872; RaisePropertyChanged @7878; nameof @7878; Localize @7881; ToString @7882 | No extracted literal effects. |
| <span id="m-77b0e9c2907a"></span><code>MainViewModel.CommitNumpad()</code><br>7887–7934 | CheckSessionUnlocked @7889; TryParse @7895; IsNullOrWhiteSpace @7897; Trim @7903; NotifyTotalsChanged @7913; SaveDurableCartAsync @7914; TryParse @7916; UpdateCartKitBreakdownAsync @7919; Remove @7925; RaisePropertyChanged @7933; nameof @7933 | No extracted literal effects. |
| <span id="m-e3290c71e947"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>7940–7958 | CheckSessionUnlocked @7948 | No extracted literal effects. |
| <span id="m-ebbf339beed2"></span><code>MainViewModel.StageBusinessProfile()</code><br>7965–7995 | CheckSessionUnlocked @7967; HasPermission @7971 | No extracted literal effects. |
| <span id="m-68732dba83de"></span><code>MainViewModel.ToggleServiceStyle()</code><br>7997–8006 | — | No extracted literal effects. |
| <span id="m-478a10f96457"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8008–8031 | RecalculateCart @8010; RaisePropertyChanged @8012; nameof @8012 | No extracted literal effects. |
| <span id="m-e1b6113b56e3"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8033–8120 | IsNullOrWhiteSpace @8036; Trim @8036; All @8046; Trim @8063; Trim @8064; NewGuid @8068; ToString @8073; ConfigureAwait @8077; BeginTransactionAsync @8077; HandleAsync @8078; AppendAsync @8083; ToString @8084; Serialize @8089; CommitAsync @8092; Initialize @8098; Unlock @8099; RaisePropertyChanged @8104; nameof @8104; LoadTeamsStaffAsync @8107; StartAutomaticDemoDatasetLoadAsync @8108; RollbackAsync @8112; DispatchToUi @8113; SafePipelineError @8113; SafeError @8118 | No extracted literal effects. |
| <span id="m-e72bfc1a7204"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8122–8129 | IsNullOrWhiteSpace @8124; ConfigureAwait @8128; SaveTeamMemberAsync @8128 | No extracted literal effects. |
| <span id="m-cc28d51f51a5"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8131–8149 | CheckSessionUnlocked @8134; HasPermission @8136 | No extracted literal effects. |
| <span id="m-b77d77d8023d"></span><code>MainViewModel.CancelChangePin()</code><br>8151–8158 | — | No extracted literal effects. |
| <span id="m-59c5cff5470e"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8160–8236 | Trim @8168; IsNullOrWhiteSpace @8171; All @8177; Equals @8190; Equals @8191; SetQuickPin @8203; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8216; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8216; ConfigureAwait @8224; LoadTeamsStaffAsync @8224; DispatchToUi @8229; SafePipelineError @8229; SafeError @8234 | No extracted literal effects. |
| <span id="m-330fcad1667d"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8238–8312 | HasPermission @8244; ConfigureAwait @8253; ResolveEffectivePermissionsAsync @8253; Contains @8286; Contains @8287; Add @8289; Contains @8295; DispatchToUi @8301; Clear @8303; Add @8304; SafeError @8310 | No extracted literal effects. |
| <span id="m-0875564f8c3e"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8314–8356 | OnTeamMemberFieldChanged @8320; ConfigureAwait @8337; ExecuteAsync @8337; DispatchToUi @8341; SafePipelineError @8349; SafeError @8354 | No extracted literal effects. |
| <span id="m-e33d36c3b3ce"></span><code>MainViewModel.ClosePermissionEditor()</code><br>8358–8363 | — | No extracted literal effects. |
| <span id="m-bd8f2a6f096b"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>8365–8379 | — | No extracted literal effects. |
| <span id="m-deb7501289b8"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>8383–8383 | — | No extracted literal effects. |
| <span id="m-c986d8e2b87c"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>8384–8384 | — | No extracted literal effects. |
| <span id="m-2dd6c829ec67"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>8385–8385 | FromResult @8385 | No extracted literal effects. |
| <span id="m-ca552231f75b"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>8388–8473 | HasPermission @8397; FromDecimal @8412; ConfigureAwait(OpenShiftCommand, Shift) @8416; ExecuteAsync(OpenShiftCommand, Shift) @8416; SetActiveCashier @8431; RefreshUnlockCandidates @8432; ToUpperInvariant @8449; ToString @8449; ToString @8451; ConfigureAwait @8461; LoadTeamsStaffAsync @8461; LoadTrackOrdersAsync @8462; DispatchToUi @8466; SafePipelineError @8466; SafeError @8471 | No extracted literal effects. |
| <span id="m-628b46d7ae61"></span><code>MainViewModel.LoadInventoryAsync()</code><br>8475–8612 | ApplyPagedResult @8479; ToList @8480; ApplyInventoryFilter @8484; Clear @8492; Empty(InventoryItem) @8494; ConfigureAwait @8499; GetPagedInventoryItemsAsync @8499; ToPageRequest @8504; CreateCommand @8517; ExecuteReaderAsync @8519; ReadAsync @8520; Add @8522; Parse @8522; GetString @8522; Add @8530; Contains @8539; ToDecimal @8542; Localize @8550; ToLocalTime @8556; BuildCostSourcesTooltip @8558; DispatchToUi @8585; Add @8588; SafeError @8610 | FROM item_kits @8518 |
| <span id="m-7510544fa469"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>8614–8670 | CheckSessionUnlocked @8616; FirstOrDefault @8617; Clear @8628; Add @8630; CreateCommand @8635; CreateParameter @8646; Add @8649; ExecuteReader @8650; Read @8651; GetString @8653; Contains @8654; FirstOrDefault @8666; ResetReceiveLines @8667; UpdateReceiveKitBreakdownAsync @8668 | FROM uoms @8636; JOIN uoms @8636 |
| <span id="m-76b9f7846764"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>8672–8773 | IsNullOrWhiteSpace @8685; Localize @8702; HasPermission @8706; BuildReceiptLines @8712; Sum @8729; Trim @8739; ToMinorUnits @8744; ConfigureAwait(ReceiveStockCommand, StockMovement) @8749; ExecuteAsync(ReceiveStockCommand, StockMovement) @8749; Clear @8759; ConfigureAwait @8761; LoadInventoryAsync @8761; LoadItemHistoryAsync @8762; DispatchToUi @8766; SafePipelineError @8766; SafeError @8771 | No extracted literal effects. |
| <span id="m-8d0a4f54e0b5"></span><code>MainViewModel.ResetReceiveLines()</code><br>8779–8796 | Clear @8781; Add @8785; RaisePropertyChanged @8791; nameof @8791; Invoke @8794 | No extracted literal effects. |
| <span id="m-74ab2fbff5a9"></span><code>MainViewModel.AddReceiveLine()</code><br>8799–8822 | IsNullOrWhiteSpace @8806; Add @8812; RaisePropertyChanged @8817; nameof @8817; Invoke @8820 | No extracted literal effects. |
| <span id="m-6da1e43cf185"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>8825–8842 | Remove @8832; Add @8835; RaisePropertyChanged @8841; nameof @8841 | No extracted literal effects. |
| <span id="m-fa11c8513a58"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>8848–8869 | IsNullOrWhiteSpace @8850; LastOrDefault @8855; Add @8859; Trim @8862; ReferenceEquals @8863; RaisePropertyChanged @8867; nameof @8867; Invoke @8868 | No extracted literal effects. |
| <span id="m-c652a72950fd"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>8872–8949 | Add @8884; IsNullOrWhiteSpace @8892; Trim @8896; FirstOrDefault @8905; GroupBy @8905; Count @8907; Trim @8934 | No extracted literal effects. |
| <span id="m-0d610f4bcd24"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>8951–8987 | CreateCommand @8956; ConfigureAwait @8963; ExecuteReaderAsync @8963; Clear @8964; ReadAsync @8965; Add @8967; ParseGuidSafe @8968; GetString @8968; IsDBNull @8972; GetInt32 @8976; Parse @8978; DispatchToUi @8985; SafeError @8985 | FROM third_parties @8957 |
| <span id="m-ffb8fb024ae0"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>8989–9007 | CheckSessionUnlocked @8991; FirstOrDefault @8997 | No extracted literal effects. |
| <span id="m-dfa3fb1929fb"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9009–9100 | IsNullOrWhiteSpace @9032; HasPermission @9043; Trim @9061; Trim @9063; ConfigureAwait(AdjustStockCommand, StockMovement) @9067; ExecuteAsync(AdjustStockCommand, StockMovement) @9067; ConfigureAwait @9083; LoadInventoryAsync @9083; LoadItemHistoryAsync @9084; OpenWasteExpenseConfirmation @9088; DispatchToUi @9093; SafePipelineError @9093; SafeError @9098 | No extracted literal effects. |
| <span id="m-114e84412b59"></span><code>MainViewModel.OpenAddProduct()</code><br>9102–9170 | ResetProductStockDraft @9104; CheckSessionUnlocked @9105; HasPermission @9106; RaisePropertyChanged @9114; nameof @9114; ClearItemHistory @9116; LoadCatalogRegistryAsync @9123; InitializeProductPricingDraft @9126; Clear @9141; Clear @9142; Where @9143; Add @9145; FirstOrDefault @9147; Clear @9158; CaptureProductModalBaselineAsync @9169 | No extracted literal effects. |
| <span id="m-29b700cb6efe"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9172–9172 | OpenEditProduct @9172 | No extracted literal effects. |
| <span id="m-a167bbecf74f"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9174–9254 | ResetProductStockDraft @9176; CheckSessionUnlocked @9178; HasPermission @9179; RaisePropertyChanged @9187; nameof @9187; ClearItemHistory @9189; LoadCatalogRegistryAsync @9197; InitializeProductPricingDraft @9203; ToMinorUnits @9204; LoadExactProductCostSnapshotsAsync @9210; ToDecimal @9214; Clear @9221; Clear @9222; Where @9223; Add @9225; FirstOrDefault @9227; LoadItemLocationEligibilitiesAsync @9246; LoadProductKitAsync @9247; LoadPrimaryBarcodeAsync @9248; LoadProductPricingDraftAsync @9249; LoadItemHistoryAsync @9250; LoadItemPriceHistoryAsync @9251; CaptureProductModalBaselineAsync @9253 | No extracted literal effects. |
| <span id="m-04c0024aab5a"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>9256–9269 | OrderBy @9259; Where @9259; Add @9261 | No extracted literal effects. |
| <span id="m-7c0ea226560f"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>9271–9344 | CreateCommand @9278; CreateParameter @9285; ToString @9287; Add @9288; ConfigureAwait @9289; ExecuteReaderAsync @9289; ReadAsync @9290; GetInt32 @9292; IsDBNull @9293; GetString @9293; ParseStoredPricingPercentForDisplay @9294; ToDisplayAmount @9298; GetInt64 @9298; OrderBy @9318; Where @9318; TryGetValue @9321; Add @9327; InvokeAsync @9329; RaisePropertyChanged @9334; nameof @9334; CaptureProductPricingSnapshot @9337; DispatchToUi @9342; SafeError @9342 | FROM item_price_levels @9309; FROM item_pricing @9280 |
| <span id="m-cb6c7664099e"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>9346–9381 | CreateCommand @9353; CreateParameter @9359; ToString @9361; Add @9362; ConfigureAwait @9363; ExecuteReaderAsync @9363; ReadAsync @9364; Parse @9367; GetString @9367; GetInt32 @9367; GetInt64 @9368; IsDBNull @9368; Parse @9369; InvokeAsync @9371; DispatchToUi @9379; SafeError @9379 | FROM product_category_pricing_rules @9354 |
| <span id="m-f6ff50ad3cdb"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>9383–9412 | ConfigureAwait @9387; WhenAll @9387; InvokeAsync @9388; CaptureProductModalSnapshot @9392; CaptureProductPricingSnapshot @9393; RaisePropertyChanged @9394; nameof @9394 | No extracted literal effects. |
| <span id="m-55d7400a0862"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>9414–9462 | Serialize @9414; ToArray @9437; Select @9437; Select @9454; OrderBy @9454; OrderBy @9458 | No extracted literal effects. |
| <span id="m-3638d885b44e"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>9464–9476 | Serialize @9464; ToArray @9475; Select @9475 | No extracted literal effects. |
| <span id="m-6468e85aa9f8"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9478–9510 | nameof @9480; RaisePropertyChanged @9481; RaiseTraceabilityState @9486; StartsWith @9490; RecomputeProductPricingPreview @9501; RefreshVirtualKitAvailability @9503 | No extracted literal effects. |
| <span id="m-cd1acaf4981a"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>9512–9526 | RaisePropertyChanged @9520; nameof @9520; RecomputeProductPricingPreview @9523; RefreshVirtualKitAvailability @9524 | No extracted literal effects. |
| <span id="m-bf4337c66d41"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9528–9536 | RaisePropertyChanged @9530; nameof @9530; RecomputeProductPricingPreview @9533; RefreshVirtualKitAvailability @9534 | No extracted literal effects. |
| <span id="m-37115c70a64d"></span><code>MainViewModel.RequestCloseProductModal()</code><br>9538–9551 | DiscardProductModal @9550 | No extracted literal effects. |
| <span id="m-f0d1a184eb5e"></span><code>MainViewModel.DiscardProductModal()</code><br>9553–9562 | RaisePropertyChanged @9558; nameof @9558; ClearItemHistory @9560 | No extracted literal effects. |
| <span id="m-68e61676aa0d"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>9564–9582 | CreateCommand @9569; CreateParameter @9571; ToString @9573; Add @9574; ConfigureAwait @9575; ExecuteScalarAsync @9575; DispatchToUi @9578; ToString @9578 | FROM barcodes @9570 |
| <span id="m-a05aeb2957cb"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>9584–9635 | CreateCommand @9589; CreateParameter @9596; ToString @9598; Add @9599; ConfigureAwait @9603; ExecuteReaderAsync @9603; ReadAsync @9604; IsDBNull @9607; GetString @9607; GetDouble @9608; ResolveQuantity @9609; Add @9610; Parse @9612; DispatchToUi @9620; Clear @9623; Add @9624; RaisePropertyChanged @9627; nameof @9627; RecomputeProductPricingPreview @9630; RefreshVirtualKitAvailability @9631 | FROM item_kits @9590; JOIN item_kit_components @9590; JOIN items @9590 |
| <span id="m-fefbba64cd11"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>9637–9637 | SaveProductConfigurationAsync @9637 | No extracted literal effects. |
| <span id="m-51fe9af2e85e"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>9639–9844 | ConfigureAwait @9644; LoadCatalogRegistryAsync @9644; HasPermission @9646; IsNullOrWhiteSpace @9651; Localize @9673; Equals @9683; ToMinorUnits @9728; GetValueOrDefault @9740; Trim @9741; Trim @9742; Trim @9743; Trim @9750; Trim @9752; ToList @9797; Select @9797; CaptureProductPricingSnapshot @9801; ToCommand @9803; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @9811; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @9811; DispatchToUi @9814; RaiseTraceabilityState @9820; CaptureProductModalSnapshot @9822; RaisePropertyChanged @9824; nameof @9824; ReloadCatalogAsync @9831; LoadInventoryAsync @9832; LoadItemHistoryAsync @9833; SafePipelineError @9837; SafeError @9842 | No extracted literal effects. |
| <span id="m-aeda898cab23"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>9846–9882 | CheckSessionUnlocked @9848; HasPermission @9849; ConfigureAwait(DeactivateProductCommand, bool) @9865; ExecuteAsync(DeactivateProductCommand, bool) @9865; ConfigureAwait @9870; ReloadCatalogAsync @9870; LoadInventoryAsync @9871; DispatchToUi @9875; SafePipelineError @9875; SafeError @9880 | No extracted literal effects. |
| <span id="m-0d222e766735"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>9884–9943 | ConfigureAwait @9890; GetActiveItemsAsync @9890; Clear @9892; Clear @9893; Clear @9894; CreateCommand @9899; ExecuteReaderAsync @9901; ReadAsync @9902; TryParse @9904; GetString @9904; Add @9905; Add @9912; GroupBy @9913; Count @9915; Contains @9920; Add @9933; Add @9934; ApplyFilter @9937 | FROM item_kits @9900 |
| <span id="m-7836adcb98b0"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>9945–9951 | IsNullOrWhiteSpace @9947; TryParse @9948; HashData @9949; GetBytes @9949; AsSpan @9950 | No extracted literal effects. |
| <span id="m-cc1fb293dff3"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>9953–10019 | CreateCommand @9959; ConfigureAwait @9962; ExecuteReaderAsync @9962; ReadAsync @9964; Add @9966; GetString @9968; GetInt32 @9972; Clear @9978; Add @9979; ExecuteReaderAsync @9991; ReadAsync @9993; Add @9995; GetString @9997; IsDBNull @10001; GetInt32 @10005; Clear @10011; Add @10012; DispatchToUi @10017; SafeError @10017 | FROM bins @9984; FROM facilities @9961; JOIN facilities @9984 |
| <span id="m-d91fd31bee51"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>10234–10338 | CreateCommand @10244; ConfigureAwait @10251; ExecuteReaderAsync @10251; ReadAsync @10252; Add @10254; ParseGuidSafe @10256; GetString @10256; IsDBNull @10259; GetInt32 @10260; Add @10280; DispatchToUi @10295; Clear @10297; Clear @10298; Clear @10299; Equals @10303; Add @10304; Add @10306; Add @10308; Clear @10310; Add @10311; FirstOrDefault @10314; Equals @10314; FirstOrDefault @10319; FirstOrDefault @10326; ApplySaleUnitDefaultsToCatalog @10331; SafeError @10336 | FROM product_categories @10246; FROM uoms @10272 |
| <span id="m-d57f9d01b35f"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>10340–10354 | ResolveProductSaleUnitFactor @10344; Round @10350; ApplyFilter @10353 | No extracted literal effects. |
| <span id="m-487baddb8a6b"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>10356–10374 | FirstOrDefault @10358; Equals @10359; TryParse @10366 | No extracted literal effects. |
| <span id="m-ff2d37ae3be2"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>10376–10398 | CheckSessionUnlocked @10378; HasPermission @10379; ConfigureAwait @10394; LoadManagedCategoriesAsync @10394; CaptureCategoryFormSnapshot @10396; RaisePropertyChanged @10397; nameof @10397 | No extracted literal effects. |
| <span id="m-ddb4768b4ed2"></span><code>MainViewModel.CloseCategoryManager()</code><br>10400–10409 | — | No extracted literal effects. |
| <span id="m-0b5d4c2c89fc"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>10411–10433 | CheckSessionUnlocked @10413; HasPermission @10414; ConfigureAwait @10429; LoadManagedUnitsAsync @10429; CaptureUnitFormSnapshot @10431; RaisePropertyChanged @10432; nameof @10432 | No extracted literal effects. |
| <span id="m-e235c9a15cc0"></span><code>MainViewModel.CloseUnitManager()</code><br>10435–10444 | — | No extracted literal effects. |
| <span id="m-baf2ec2833fc"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>10446–10509 | Clear @10449; Clear @10450; Clear @10451; CreateCommand @10452; ConfigureAwait @10458; ExecuteReaderAsync @10458; ReadAsync @10459; Add @10461; ParseGuidSafe @10463; GetString @10463; IsDBNull @10466; GetInt32 @10467; Where @10475; Equals @10475; Add @10476; TryParse @10489; Add @10490; RefreshTargetedCategoryCollections @10503; DispatchToUi @10504; RefreshManagedCategoriesTable @10506; RefreshManagedExpenseCategoriesTable @10507 | FROM expense_categories @10480; FROM product_categories @10454; JOIN expense_records @10480 |
| <span id="m-c805237afa5a"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>10511–10518 | OpenCategoryManagerAsync @10513; FirstOrDefault @10514; EditManagedCategory @10517 | No extracted literal effects. |
| <span id="m-f475cad70e9e"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>10520–10528 | OpenCategoryManagerAsync @10523; FirstOrDefault @10524; EditManagedExpenseCategory @10527 | No extracted literal effects. |
| <span id="m-2d51052508b5"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>10530–10549 | DispatchToUi @10532; Clear @10534; Clear @10535; Clear @10536; Where @10538; Equals @10541; Add @10542; Add @10544; Add @10546 | No extracted literal effects. |
| <span id="m-2ace2063f443"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>10551–10563 | CaptureCategoryFormSnapshot @10561; RaisePropertyChanged @10562; nameof @10562 | No extracted literal effects. |
| <span id="m-c2e88111a608"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>10565–10578 | CaptureCategoryFormSnapshot @10576; RaisePropertyChanged @10577; nameof @10577 | No extracted literal effects. |
| <span id="m-c699b5ba9bae"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>10580–10590 | Serialize @10580 | No extracted literal effects. |
| <span id="m-d18d9cc48f85"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>10592–10602 | Serialize @10592 | No extracted literal effects. |
| <span id="m-5f0a6aa85ba0"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>10604–10604 | — | No extracted literal effects. |
| <span id="m-306f034e72e9"></span><code>MainViewModel.DiscardRegistryForm()</code><br>10606–10622 | Equals @10609; RaisePropertyChanged @10613; nameof @10613 | No extracted literal effects. |
| <span id="m-8b0de9afa872"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>10624–10751 | Equals @10635; HasPermission @10637; FirstOrDefault @10646; Trim @10651; Trim @10652; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @10654; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @10654; DispatchToUi @10657; SafePipelineError @10657; IsNullOrWhiteSpace @10665; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @10667; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @10667; ConfigureAwait @10676; LoadManagedCategoriesAsync @10676; LoadExpenseCategoriesAsync @10677; CaptureCategoryFormSnapshot @10687; RaisePropertyChanged @10688; nameof @10688; Trim @10706; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @10708; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @10708; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @10724; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @10724; LoadCatalogRegistryAsync @10733; ReloadCatalogAsync @10734; SafeError @10749 | No extracted literal effects. |
| <span id="m-2ff2efa5f585"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>10753–10798 | HasPermission @10763; ConfigureAwait(DeactivateCategoryCommand, bool) @10776; ExecuteAsync(DeactivateCategoryCommand, bool) @10776; ConfigureAwait(ReactivateCategoryCommand, bool) @10781; ExecuteAsync(ReactivateCategoryCommand, bool) @10781; DispatchToUi @10786; SafePipelineError @10786; ConfigureAwait @10790; LoadManagedCategoriesAsync @10790; LoadCatalogRegistryAsync @10791; ReloadCatalogAsync @10792; SafeError @10796 | No extracted literal effects. |
| <span id="m-18339abef3f9"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>10800–10840 | HasPermission @10810; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @10826; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @10826; DispatchToUi @10829; SafePipelineError @10829; ConfigureAwait @10833; LoadManagedCategoriesAsync @10833; LoadExpenseCategoriesAsync @10834; SafeError @10838 | No extracted literal effects. |
| <span id="m-ad2fad0aea0a"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>10842–10942 | Clear @10845; CreateCommand @10848; ConfigureAwait @10854; ExecuteReaderAsync @10854; ReadAsync @10855; Add @10857; GetString @10859; IsDBNull @10861; GetInt32 @10865; IsNullOrWhiteSpace @10876; Equals @10880; Add @10887; Clear @10891; ExecuteReaderAsync @10896; ReadAsync @10897; GetString @10899; Where @10921; Add @10923; TryGetValue @10926; FirstOrDefault @10933; Add @10937; DispatchToUi @10940; UpdateConversionPreview @10941 | FROM store_uom_preferences @10895; FROM uoms @10850 |
| <span id="m-c25642356073"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>10944–10951 | OpenUnitManagerAsync @10946; FirstOrDefault @10947; Equals @10947; EditManagedUnit @10950 | No extracted literal effects. |
| <span id="m-52d28fa94f8e"></span><code>MainViewModel.UpdateConversionPreview()</code><br>10953–10989 | IsNullOrWhiteSpace @10955; FirstOrDefault @10961; Equals @10961; TryParse @10976 | No extracted literal effects. |
| <span id="m-b27bdbb302cb"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>10991–11012 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @10998; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @10998; DispatchToUi @11001; SafePipelineError @11005; SafeError @11010 | No extracted literal effects. |
| <span id="m-b27185ad5fc5"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11014–11027 | IsNullOrWhiteSpace @11020; TryParse @11023; CaptureUnitFormSnapshot @11025; RaisePropertyChanged @11026; nameof @11026 | No extracted literal effects. |
| <span id="m-46546dca2b4e"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>11029–11091 | IsNullOrWhiteSpace @11041; Trim @11045; Trim @11046; Trim @11049; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @11050; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @11050; DispatchToUi @11053; SafePipelineError @11053; Trim @11060; Equals @11063; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @11068; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @11068; ConfigureAwait @11076; LoadManagedUnitsAsync @11076; LoadCatalogRegistryAsync @11077; CaptureUnitFormSnapshot @11084; RaisePropertyChanged @11085; nameof @11085; SafeError @11089 | No extracted literal effects. |
| <span id="m-70fe63a244fb"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>11093–11131 | ConfigureAwait(DeactivateUomCommand, bool) @11110; ExecuteAsync(DeactivateUomCommand, bool) @11110; ConfigureAwait(ReactivateUomCommand, bool) @11115; ExecuteAsync(ReactivateUomCommand, bool) @11115; DispatchToUi @11120; SafePipelineError @11120; ConfigureAwait @11124; LoadManagedUnitsAsync @11124; LoadCatalogRegistryAsync @11125; SafeError @11129 | No extracted literal effects. |
| <span id="m-4d2a0f96275d"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>11133–11171 | CreateCommand @11138; CreateParameter @11145; ToString @11147; Add @11148; ConfigureAwait @11150; ExecuteReaderAsync @11150; Clear @11151; ReadAsync @11152; Add @11154; ParseGuidSafe @11156; GetString @11156; GetInt32 @11159; IsDBNull @11161; ToDecimal @11161; GetDouble @11161; DispatchToUi @11169; SafeError @11169 | FROM item_locations @11139 |
| <span id="m-9c2d877e87ab"></span><code>MainViewModel.OpenLocationsModal()</code><br>11174–11200 | CheckSessionUnlocked @11176; HasPermission @11177; LoadFacilitiesAndBinsAsync @11198 | No extracted literal effects. |
| <span id="m-26d50ff90357"></span><code>MainViewModel.OpenAddFacility()</code><br>11202–11210 | — | No extracted literal effects. |
| <span id="m-3966515671be"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>11212–11221 | — | No extracted literal effects. |
| <span id="m-8c36a76e0de1"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>11223–11282 | HasPermission @11226; IsNullOrWhiteSpace @11231; IsNullOrEmpty @11247; Trim @11249; Trim @11249; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @11250; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @11250; OpenAddFacility @11254; ConfigureAwait @11255; LoadFacilitiesAndBinsAsync @11255; DispatchToUi @11259; SafePipelineError @11259; ConfigureAwait(CreateFacilityCommand, FacilityDto) @11265; ExecuteAsync(CreateFacilityCommand, FacilityDto) @11265; SafeError @11280 | No extracted literal effects. |
| <span id="m-ad9e12fc02c0"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>11284–11315 | HasPermission @11287; ConfigureAwait(DeactivateFacilityCommand, bool) @11299; ExecuteAsync(DeactivateFacilityCommand, bool) @11299; OpenAddFacility @11303; ConfigureAwait @11304; LoadFacilitiesAndBinsAsync @11304; DispatchToUi @11308; SafePipelineError @11308; SafeError @11313 | No extracted literal effects. |
| <span id="m-75845a11348d"></span><code>MainViewModel.OpenAddBin()</code><br>11317–11328 | FirstOrDefault @11327 | No extracted literal effects. |
| <span id="m-45548c2e9e62"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>11330–11342 | FirstOrDefault @11340 | No extracted literal effects. |
| <span id="m-0340148219fd"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>11344–11419 | HasPermission @11347; IsNullOrWhiteSpace @11357; IsNullOrEmpty @11368; Trim @11373; Trim @11374; Trim @11375; Trim @11376; Trim @11377; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @11380; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @11380; OpenAddBin @11384; ConfigureAwait @11385; LoadFacilitiesAndBinsAsync @11385; DispatchToUi @11389; SafePipelineError @11389; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @11402; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @11402; SafeError @11417 | No extracted literal effects. |
| <span id="m-f2fa27930112"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>11421–11452 | HasPermission @11424; ConfigureAwait(DeactivateLocationBinCommand, bool) @11436; ExecuteAsync(DeactivateLocationBinCommand, bool) @11436; OpenAddBin @11440; ConfigureAwait @11441; LoadFacilitiesAndBinsAsync @11441; DispatchToUi @11445; SafePipelineError @11445; SafeError @11450 | No extracted literal effects. |
| <span id="m-583457744fb0"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>11454–11507 | HasPermission @11462; IsNullOrWhiteSpace @11467; Trim @11479; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @11487; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @11487; ConfigureAwait @11495; LoadItemLocationEligibilitiesAsync @11495; DispatchToUi @11500; SafePipelineError @11500; SafeError @11505 | No extracted literal effects. |
| <span id="m-d033c2534f86"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>11509–11539 | HasPermission @11512; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @11524; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @11524; ConfigureAwait @11527; LoadItemLocationEligibilitiesAsync @11527; DispatchToUi @11532; SafePipelineError @11532; SafeError @11537 | No extracted literal effects. |
| <span id="m-036f1b216284"></span><code>MainViewModel.LoadCustomersAsync()</code><br>11542–11575 | NewGuid @11550; Clear @11556; Add @11557; FilterCustomers @11559; ConfigureAwait @11566; GetCustomersAsync @11566; DispatchToUi @11573; SafeError @11573 | No extracted literal effects. |
| <span id="m-fe61876c2b3f"></span><code>MainViewModel.FilterCustomers()</code><br>11577–11590 | Clear @11579; Trim @11580; IsNullOrWhiteSpace @11581; Where @11583; Contains @11583; Contains @11584; Contains @11585; Add @11588 | No extracted literal effects. |
| <span id="m-462525d44eb9"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>11592–11628 | CheckSessionUnlocked @11594; CreateCommand @11603; CreateParameter @11606; ToString @11608; Add @11609; ConfigureAwait @11610; ExecuteScalarAsync @11610; ToString @11611; Equals @11614; LoadPickerCandidatesAsync @11626; DispatchToUi @11627 | FROM items @11605 |
| <span id="m-6544d7cbab54"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>11630–11691 | ConfigureAwait @11637; GetLotCandidatesAsync @11637; DispatchToUi @11640; Clear @11642; Add @11645; ToString @11654; GetSerialCandidatesAsync @11662; Clear @11667; Add @11670; ToString @11679 | No extracted literal effects. |
| <span id="m-67d9993e9370"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>11693–11699 | Clear @11696; Clear @11697 | No extracted literal effects. |
| <span id="m-50b8393049a5"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>11701–11760 | FirstOrDefault @11714; ConfigureAwait(SelectLotForCartLineCommand, bool) @11722; ExecuteAsync(SelectLotForCartLineCommand, bool) @11722; DispatchToUi @11725; SafePipelineError @11725; ToList @11731; Where @11731; ConfigureAwait(SelectSerialForCartLineCommand, bool) @11741; ExecuteAsync(SelectSerialForCartLineCommand, bool) @11741; SafeError @11758 | No extracted literal effects. |
| <span id="m-6b5bb7cbaeb0"></span><code>MainViewModel.OpenCustomerChooser()</code><br>11762–11770 | CheckSessionUnlocked @11764; Clear @11767; LoadCustomersAsync @11768 | No extracted literal effects. |
| <span id="m-040ea3b18fc9"></span><code>MainViewModel.CloseCustomerChooser()</code><br>11772–11775 | — | No extracted literal effects. |
| <span id="m-3f3c4b94cd00"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>11777–11794 | SaveDurableCartAsync @11787; IsNullOrWhiteSpace @11791; ToString @11791; NewGuid @11791; RecordSuccessfulSearchUseAsync @11792; FromGuid @11792 | No extracted literal effects. |
| <span id="m-ec79edaf8093"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>11796–11805 | SaveDurableCartAsync @11804 | No extracted literal effects. |
| <span id="m-65e6b407ee5f"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>11807–11852 | CheckSessionUnlocked @11809; IndexOf @11813; SelectWalkInCustomer @11819; FilterCustomers @11821; ConfigureAwait(DeactivateCustomerCommand, bool) @11833; ExecuteAsync(DeactivateCustomerCommand, bool) @11833; ConfigureAwait @11840; LoadCustomersAsync @11840; DispatchToUi @11845; SafePipelineError @11845; SafeError @11850 | No extracted literal effects. |
| <span id="m-1571577f00d5"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>11981–12020 | Add @11987; NewGuid @11988; RefreshManufacturingTablesAsync @12002; ConfigureAwait @12010; GetKitsAsync @12010; Clear @12011; Add @12012; DispatchToUi @12018; SafeError @12018 | No extracted literal effects. |
| <span id="m-a1769eb9a06e"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12024–12040 | CheckSessionUnlocked @12026; SetProductionActionMode @12028; FirstOrDefault @12033; LoadProductionIngredientLotsAsync @12038; TakeProductionSnapshot @12039 | No extracted literal effects. |
| <span id="m-a2cd1072d695"></span><code>MainViewModel.CloseProductionModal()</code><br>12042–12056 | — | No extracted literal effects. |
| <span id="m-33f6650f78e6"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>12058–12157 | ExecuteExistingProductionAsync @12061; Resolve @12083; NewGuid @12086; ToUpperInvariant @12088; ToString @12088; Insert @12106; IsNullOrWhiteSpace @12128; Trim @12128; ToDictionary @12130; Where @12130; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @12134; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @12134; DispatchToUi @12137; SafePipelineError @12137; RecordSuccessfulSearchUseAsync @12144; FromGuid @12144; ConfigureAwait @12147; LoadManufacturingDataAsync @12147; LoadInventoryAsync @12148; SafeError @12154 | No extracted literal effects. |
| <span id="m-de0ac34eebcd"></span><code>MainViewModel.CloseXReportModal()</code><br>12256–12259 | — | No extracted literal effects. |
| <span id="m-8714d5c69aa6"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>12261–12291 | CheckSessionUnlocked @12263; Clear @12281; Where @12282; GetUnlockCandidates @12282; Equals @12283; Add @12287 | No extracted literal effects. |
| <span id="m-627a14d172c5"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>12293–12297 | — | No extracted literal effects. |
| <span id="m-571af010216d"></span><code>MainViewModel.CloseZReportModal()</code><br>12299–12302 | — | No extracted literal effects. |
| <span id="m-7e84ce787d0e"></span><code>MainViewModel.LoadReportDataAsync()</code><br>12304–12421 | ToString @12324; DispatchToUi @12340; ConfigureAwait @12368; ExecuteAsync @12368; Join @12370; Select(string, Money) @12370; InvoiceMoney @12370; ToDecimal @12373; ToDecimal @12374; ToDecimal @12375; ToDecimal @12376; ToDecimal @12378; ToDecimal @12380; ToDecimal @12381; ToDecimal @12382; ToDecimal @12383; ToDecimal @12384; ToUpperInvariant @12386; ToString @12386; ToString @12388; ToString @12389; Sum @12395; ToDecimal @12395; ToDecimal @12398; Add @12400; Format @12405; SafeError @12413 | No extracted literal effects. |
| <span id="m-11ff4c2cb8d9"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>12423–12512 | CheckSessionUnlocked @12426; IsNullOrWhiteSpace @12443; AuthenticateSelectedUser @12451; Trim @12453; Round @12462; Trim @12466; ConfigureAwait(CloseShiftCommand, Shift) @12470; ExecuteAsync(CloseShiftCommand, Shift) @12470; DispatchToUi @12488; SafePipelineError @12488; ConfigureAwait @12495; ExecuteAsync @12495; SetActiveCashier @12499; RefreshUnlockCandidates @12500; RaisePropertyChanged @12501; nameof @12501; LoadReportDataAsync @12505; LoadTeamsStaffAsync @12506; SafeError @12510 | No extracted literal effects. |
| <span id="m-b5e707bcf134"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>12514–12578 | FirstOrDefault @12516; CreateCommand @12523; CreateParameter @12535; ToString @12537; Add @12538; ExecuteReader @12540; Read @12541; Parse @12543; GetString @12543; GetInt64 @12546; Pow @12548; IsDBNull @12550; Add @12571 | FROM items @12524; JOIN barcodes @12524; JOIN product_categories @12524 |
| <span id="m-d96cce58bcc2"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>12580–12684 | IsNullOrWhiteSpace @12582; Trim @12585; ToList @12588; Where @12588; IsNullOrEmpty @12589; Equals @12589; ToString @12591; AddToCart @12597; CreateCommand @12613; CreateParameter @12628; Add @12631; ExecuteReader @12633; Read @12635; Parse @12637; GetString @12637; ContainsKey @12638; GetInt64 @12642; Pow @12644; IsDBNull @12646; First @12673; Add @12674 | FROM items @12614; JOIN barcodes @12614; JOIN product_categories @12614 |
| <span id="m-613b14af7f98"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>12686–12729 | IsNullOrWhiteSpace @12688; Trim @12691; AppendReceiveSerialScan @12697; TryAddUniqueExactMatchToCart @12703; Clear @12705; ToList @12710; Where @12710; Equals @12710; AddToCart @12713 | No extracted literal effects. |

</details>

## PagedTableState.cs {#src-d7eeb702829b}

<code>Software/src/GetSeek.Desktop/ViewModels/PagedTableState.cs</code> · 235 lines.

SHA-256: <code>7d37be4286eb4fc0b6937e7bb077b6930e1db59eefb972b5e597ca453ed7f83c</code>.

Declarations: <code>PagedTableState : ReactiveObject, IDataTableState</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (14)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-073a031cf641"></span><code>PagedTableState.BindRefresh(Action)</code><br>103–106 | — | No extracted literal effects. |
| <span id="m-05b032c46dd0"></span><code>PagedTableState.ToPageRequest()</code><br>108–111 | — | No extracted literal effects. |
| <span id="m-fe73e199eaf7"></span><code>PagedTableState.ApplyPagedResult(PagedResult&lt;T&gt;)</code><br>113–132 | Clear @115; Add @118; RaisePropertyChanged @125; nameof @125 | No extracted literal effects. |
| <span id="m-7cae3ba80d50"></span><code>PagedTableState.ToggleSort(string)</code><br>134–156 | Equals @136; ResetToFirstPage @154; Invoke @155 | No extracted literal effects. |
| <span id="m-b99e7b5634dc"></span><code>PagedTableState.ResetToFirstPage()</code><br>159–167 | RaisePropertyChanged @163; nameof @163 | No extracted literal effects. |
| <span id="m-042c49128386"></span><code>PagedTableState.NextPage()</code><br>169–175 | — | No extracted literal effects. |
| <span id="m-39417656c43b"></span><code>PagedTableState.PreviousPage()</code><br>177–183 | — | No extracted literal effects. |
| <span id="m-8fdd4503b39e"></span><code>PagedTableState.SelectRow(string,bool)</code><br>185–194 | IsNullOrWhiteSpace @187; Add @189; Remove @191; RaisePropertyChanged @193; nameof @193 | No extracted literal effects. |
| <span id="m-07da6b94ffc8"></span><code>PagedTableState.SelectPage(IEnumerable&lt;string&gt;)</code><br>196–197 | SetPageSelection @197 | No extracted literal effects. |
| <span id="m-9e348f66087f"></span><code>PagedTableState.SetPageSelection(IEnumerable&lt;string&gt;,bool)</code><br>199–209 | Where @201; IsNullOrWhiteSpace @201; Add @204; Remove @206; RaisePropertyChanged @208; nameof @208 | No extracted literal effects. |
| <span id="m-31dd353eaedd"></span><code>PagedTableState.IsRowSelected(string)</code><br>211–211 | Contains @211 | No extracted literal effects. |
| <span id="m-aba30cfa583f"></span><code>PagedTableState.ClearSelection()</code><br>213–217 | Clear @215; RaisePropertyChanged @216; nameof @216 | No extracted literal effects. |
| <span id="m-308e350723f2"></span><code>PagedTableState.SetSelectionScope(string)</code><br>223–232 | Equals @226; ClearSelection @229; RaisePropertyChanged @230; nameof @230 | No extracted literal effects. |
| <span id="m-58305c2a3d47"></span><code>PagedTableState.GetSelectedIdsForPreview()</code><br>234–234 | ToArray @234; OrderBy @234 | No extracted literal effects. |

</details>

## SearchState.cs {#src-cfeb26f7fa10}

<code>Software/src/GetSeek.Desktop/ViewModels/SearchState.cs</code> · 513 lines.

SHA-256: <code>0e846b72f7515a16ed09ef8287efc0b9607e5d5ed62edfee03800a3be6cc6056</code>.

Declarations: <code>SearchSelectionStatus</code> (line 12), <code>SearchSelectionResult</code> (line 20), <code>SearchState : ReactiveObject, IDisposable</code> (line 41), <code>SearchRequestSnapshot</code> (line 54).

<details markdown>
<summary>Methods, calls, table effects and failures (17)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-1efe4e215fdb"></span><code>SearchSelectionResult.Accepted()</code><br>33–33 | — | No extracted literal effects. |
| <span id="m-1eb37beb5c22"></span><code>SearchSelectionResult.Rejected(string?)</code><br>34–34 | — | No extracted literal effects. |
| <span id="m-fdba8268e1fb"></span><code>SearchSelectionResult.Ignored(string?)</code><br>35–35 | — | No extracted literal effects. |
| <span id="m-63437e5db781"></span><code>SearchSelectionResult.Failed(string?)</code><br>36–36 | — | No extracted literal effects. |
| <span id="m-cbf5b2c0e500"></span><code>SearchState.Invalidate()</code><br>83–99 | Increment @87; Cancel @89; Dispose @90 | No extracted literal effects. |
| <span id="m-a201cc1f09d5"></span><code>SearchState.SelectOptionAsync(SearchOption?,CancellationToken)</code><br>123–173 | Ignored @125; Invalidate @127; RaisePropertyChanged @133; nameof @133; Invoke @135; ConfigureAwait @140; _onSelectedAsync @140; ParseEntityKey @148; Failed @168; Accepted @172 | No extracted literal effects. |
| <span id="m-7715f0fe9288"></span><code>SearchState.GetCurrentContext()</code><br>266–278 | _contextWithConfigSupplier @270; _operatorWorkspaceSupplier @274 | No extracted literal effects. |
| <span id="m-0bb0c0111d04"></span><code>SearchState.IsContextValid(SearchRequestSnapshot)</code><br>280–291 | GetCurrentContext @282 | No extracted literal effects. |
| <span id="m-1c77071db8a2"></span><code>SearchState.RestartDebounce()</code><br>293–321 | Cancel @297; Dispose @298; Run @306; ConfigureAwait @310; Delay @310; TriggerSearchAsync @313 | No extracted literal effects. |
| <span id="m-e1144479b00b"></span><code>SearchState.FlushAsync()</code><br>323–332 | Cancel @327; Dispose @328; ConfigureAwait @331; TriggerSearchAsync @331 | No extracted literal effects. |
| <span id="m-2da6d7ad403e"></span><code>SearchState.RefreshScopeAsync(bool)</code><br>334–345 | Invalidate @336; ConfigureAwait @339; TriggerSearchAsync @339; RestartDebounce @343 | No extracted literal effects. |
| <span id="m-47f141edace4"></span><code>SearchState.TriggerSearchAsync()</code><br>347–434 | Increment @356; Cancel @357; Dispose @358; GetCurrentContext @363; Invoke @370; ConfigureAwait @376; RunOnUIThreadAsync @376; GetSuggestionsAsync @387; IsContextValid @392; Clear @400; Add @403; ToString @403 | No extracted literal effects. |
| <span id="m-d2c45d35bd49"></span><code>SearchState.Clear()</code><br>437–464 | Invalidate @443; RaisePropertyChanged @445; nameof @445; Clear @450; _onSelectedAsync @456; Invoke @458 | No extracted literal effects. |
| <span id="m-5f4d751dcdec"></span><code>SearchState.RecordUsageAsync(string,SearchEntityKey,CancellationToken)</code><br>466–482 | IsNullOrWhiteSpace @468; ConfigureAwait @472; RecordUseAsync @472 | No extracted literal effects. |
| <span id="m-4e771faea773"></span><code>SearchState.ParseEntityKey(string)</code><br>484–492 | IndexOf @486 | No extracted literal effects. |
| <span id="m-7af3d7fed40f"></span><code>SearchState.RunOnUIThreadAsync(Action)</code><br>494–504 | CheckAccess @496; action @498; InvokeAsync @502 | No extracted literal effects. |
| <span id="m-dcbf022a0bb2"></span><code>SearchState.Dispose()</code><br>506–512 | Invalidate @510; Clear @511 | No extracted literal effects. |

</details>

## MainWindow.axaml.cs {#src-49e81864bc35}

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml.cs</code> · 945 lines.

SHA-256: <code>b86a88b9bc5928d11392b80d4234f57a9743c378142fd6f0de97f4f6446c3844</code>.

Declarations: <code>MainWindow : Window</code> (line 21).

<details markdown>
<summary>Methods, calls, table effects and failures (36)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-39dbde34cad7"></span><code>MainWindow.ReportCodeBehindError(string,string,Exception)</code><br>70–80 | Localize @72; Report @74; Post @79; Record @79 | No extracted literal effects. |
| <span id="m-7f000908676c"></span><code>MainWindow.OnDataContextChanged(object?,EventArgs)</code><br>82–85 | ObserveViewModel @84 | No extracted literal effects. |
| <span id="m-ff1ee6260e11"></span><code>MainWindow.ObserveViewModel(MainViewModel?)</code><br>87–113 | ReferenceEquals @89 | No extracted literal effects. |
| <span id="m-dd948ce8e944"></span><code>MainWindow.OnFocusSearchRequested()</code><br>115–124 | FindControl(TextBox) @117; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @117; FindControl(TextBox) @117; Focus @120; SelectAll @121 | No extracted literal effects. |
| <span id="m-698d0eb1184d"></span><code>MainWindow.OnFocusReceiveSerialRequested()</code><br>126–141 | Post @130; FindControl(ItemsControl) @132; LastOrDefault(TextBox) @133; OfType(TextBox) @133; GetVisualDescendants @133; Focus @136; SelectAll @137 | No extracted literal effects. |
| <span id="m-e8a5eac38a47"></span><code>MainWindow.OnImportFilePickerRequested()</code><br>143–169 | OpenFilePickerAsync @152; Localize @154; PreviewImportFileAsync @162; ReportCodeBehindError @167 | No extracted literal effects. |
| <span id="m-a576ee001b6e"></span><code>MainWindow.OnThirdPartyImportFilePickerRequested()</code><br>171–194 | OpenFilePickerAsync @176; PreviewThirdPartyImportFileAsync @185; FocusThirdPartyImportCloseButton @188; ReportCodeBehindError @192 | No extracted literal effects. |
| <span id="m-c4178746df3e"></span><code>MainWindow.OnThirdPartyTemplateSaveRequested(byte[])</code><br>196–196 | SaveImportTemplateAsync @196 | No extracted literal effects. |
| <span id="m-aed1f7b11c84"></span><code>MainWindow.OnCompletedImportSaveRequested(byte[],string)</code><br>197–197 | SaveImportTemplateAsync @197 | No extracted literal effects. |
| <span id="m-d1baee962eed"></span><code>MainWindow.OnInventoryTemplateSaveRequested(byte[])</code><br>198–198 | SaveImportTemplateAsync @198 | No extracted literal effects. |
| <span id="m-a15de4613bd6"></span><code>MainWindow.SaveImportTemplateAsync(byte[],string)</code><br>199–224 | GetDownloadsFolderPath @203; IsNullOrWhiteSpace @204; Exists @204; TryGetFolderFromPathAsync @205; SaveFilePickerAsync @207; OpenWriteAsync @216; SetLength @217; WriteAsync @218; ReportCodeBehindError @222 | No extracted literal effects. |
| <span id="m-cfaef8f85a2f"></span><code>MainWindow.GetDownloadsFolderPath()</code><br>226–241 | IsWindows @228; SHGetKnownFolderPath @231; PtrToStringUni @235; FreeCoTaskMem @239 | No extracted literal effects. |
| <span id="m-bce1852ddc9b"></span><code>MainWindow.SHGetKnownFolderPath(Guid,uint,IntPtr,IntPtr)</code><br>243–244 | — | No extracted literal effects. |
| <span id="m-e3c08ceca225"></span><code>MainWindow.OnCopyToClipboardRequested(string)</code><br>246–259 | SetTextAsync @252; ReportCodeBehindError @257 | No extracted literal effects. |
| <span id="m-12fba920eedb"></span><code>MainWindow.OnElementGotFocus(object?,GotFocusEventArgs)</code><br>261–267 | — | No extracted literal effects. |
| <span id="m-27cf71d64e79"></span><code>MainWindow.OnPriceInputGotFocus(object?,GotFocusEventArgs)</code><br>269–273 | Post @272 | No extracted literal effects. |
| <span id="m-b9ce911c1662"></span><code>MainWindow.OnPriceInputPointerReleased(object?,PointerReleasedEventArgs)</code><br>275–284 | FindAncestorOfType(TextBox) @282; SelectAll @283 | No extracted literal effects. |
| <span id="m-a73531413be5"></span><code>MainWindow.GetActiveEditableTextBox()</code><br>286–308 | IsAttachedToVisualTree @289; FindControl(TextBox) @300; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @300; FindControl(TextBox) @300 | No extracted literal effects. |
| <span id="m-3dfb97a473d7"></span><code>MainWindow.InsertTextIntoTextBox(TextBox,string)</code><br>310–338 | Min @315; Max @316; Insert @321; Remove @321; Clamp @330; Insert @331 | No extracted literal effects. |
| <span id="m-87093e134ab6"></span><code>MainWindow.HandleBackspaceOnTextBox(TextBox)</code><br>340–369 | Min @345; Max @346; Remove @351; Clamp @359; DeleteGraphemeAt @362 | No extracted literal effects. |
| <span id="m-71e91cb3e414"></span><code>MainWindow.HandleClearOnTextBox(TextBox)</code><br>371–377 | — | No extracted literal effects. |
| <span id="m-779fdb216cf3"></span><code>MainWindow.HandleNumericDigitOnTextBox(TextBox,string)</code><br>379–409 | Min @384; Max @385; Remove @391; Contains @394; IsNullOrEmpty @402; InsertTextIntoTextBox @408 | No extracted literal effects. |
| <span id="m-1eedf9e5f67b"></span><code>MainWindow.WireTouchControls()</code><br>411–540 | AddHandler @413; FindControl(GetSeek.UI.Components.Controls.TouchKeyboardControl) @415; GetActiveEditableTextBox @421; InsertTextIntoTextBox @424; Execute @428; HandleBackspaceOnTextBox @437; HandleClearOnTextBox @450; FindControl(GetSeek.UI.Components.Controls.TouchNumpadControl) @469; Execute @477; HandleNumericDigitOnTextBox @483; Execute @495; Execute @513; Execute @532 | No extracted literal effects. |
| <span id="m-4f32b2dbe3ec"></span><code>MainWindow.OnChooseQrImage(object?,RoutedEventArgs)</code><br>542–542 | ChoosePaymentImageAsync @542 | No extracted literal effects. |
| <span id="m-696ab836ff85"></span><code>MainWindow.OnChooseBankImage(object?,RoutedEventArgs)</code><br>543–543 | ChoosePaymentImageAsync @543 | No extracted literal effects. |
| <span id="m-47b9a7b046f6"></span><code>MainWindow.ChoosePaymentImageAsync(bool)</code><br>545–593 | OpenFilePickerAsync @550; Localize @553; OpenReadAsync @566; Localize @569; ReadAsync @575; WriteAsync @582; AsMemory @582; ToArray @584; SetManualPaymentImage @586; ReportCodeBehindError @590 | No extracted literal effects. |
| <span id="m-e4c02eb0bd32"></span><code>MainWindow.OnChooseExpenseReceiptImage(object?,RoutedEventArgs)</code><br>595–621 | OpenFilePickerAsync @600; OpenReadAsync @614; SetExpenseFormAttachmentAsync @615; ReportCodeBehindError @619 | No extracted literal effects. |
| <span id="m-529a3855abd6"></span><code>MainWindow.OnKeyDown(KeyEventArgs)</code><br>623–700 | OnKeyDown @641; CanCaptureUnfocusedBarcodeWedge @649; Clear @651; ToString @662; HandleBarcodeScanned @668; GetPrintableCharacterFromKey @677; IsNullOrEmpty @678; Append @683 | No extracted literal effects. |
| <span id="m-dbec54c97ea3"></span><code>MainWindow.CanCaptureUnfocusedBarcodeWedge()</code><br>702–720 | GetTopLevel @711; GetFocusedElement @711; FindAncestorOfType(GetSeek.UI.Components.Controls.CompactDateField) @713; GetType @714 | No extracted literal effects. |
| <span id="m-0ce8881db262"></span><code>MainWindow.OnPreviewKeyboardAction(object?,KeyEventArgs)</code><br>722–818 | FirstOrDefault(GetSeek.UI.Components.Controls.CompactDateField) @726; OfType(GetSeek.UI.Components.Controls.CompactDateField) @726; GetVisualDescendants @726; FirstOrDefault(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @736; OfType(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @736; TryHandleEscapeKey @746; HandlePhysicalBackspace @757; GetTopLevel @765; GetFocusedElement @765; IsWithinThirdPartyImportOverlay @766; TryActivateFocusedButton @768; FindControl(GetSeek.UI.Components.Controls.ModalShell) @774; FindControl(Button) @774; Focus @774; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @790; ReferenceEquals @791; IsVisualAncestorOf @791; SelectOption @796; Trim @801; IsNullOrEmpty @802; TryAddUniqueExactMatchToCart @804; Clear @806 | No extracted literal effects. |
| <span id="m-fae01d786fbd"></span><code>MainWindow.TryActivateFocusedButton()</code><br>820–847 | GetTopLevel @824; GetFocusedElement @825; CanExecute @833; Execute @840; RaiseEvent @844 | No extracted literal effects. |
| <span id="m-a2db6c2e2f63"></span><code>MainWindow.IsWithinThirdPartyImportOverlay(Visual)</code><br>849–858 | FindControl(GetSeek.UI.Components.Controls.ModalShell) @851; GetVisualParent @852 | No extracted literal effects. |
| <span id="m-3b0467de6996"></span><code>MainWindow.FocusThirdPartyImportCloseButton()</code><br>860–863 | Post @862; FindControl(GetSeek.UI.Components.Controls.ModalShell) @862; FindControl(Button) @862; Focus @862 | No extracted literal effects. |
| <span id="m-8d5e766a9074"></span><code>MainWindow.HandlePhysicalBackspace()</code><br>865–897 | HandleBackspaceOnTextBox @874; Execute @880; Execute @886; Execute @892 | No extracted literal effects. |
| <span id="m-fd7c647252aa"></span><code>MainWindow.GetPrintableCharacterFromKey(Key,KeyModifiers)</code><br>899–917 | ToString @905; ToUpperInvariant @905; ToString @905 | No extracted literal effects. |
| <span id="m-223e02183a95"></span><code>MainWindow.OnKeyUp(KeyEventArgs)</code><br>919–944 | OnKeyUp @943 | No extracted literal effects. |

</details>

## AXAML, migrations and project inputs

### App.axaml {#src-1e635b06c6de}

<code>Software/src/GetSeek.Desktop/App.axaml</code> · 37 lines · SHA-256 <code>fbcb9d4c8bbedcd7ab20df886f595435317e99118d45946f85f9cb14b023ed01</code>.

### GetSeek.Desktop.csproj {#src-2f265207af15}

<code>Software/src/GetSeek.Desktop/GetSeek.Desktop.csproj</code> · 27 lines · SHA-256 <code>57c435b4d7b778cfe77cd7da0397f3607a8ad46a8db4dfcd71d522dd51ee3bdb</code>.

### MainWindow.axaml {#src-67243af94cf2}

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml</code> · 5673 lines · SHA-256 <code>7fa4cd4aa1614ed740829cf02c452b50603dc9086330a9b413370dd911e16aac</code>.
