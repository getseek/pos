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

<code>Software/src/GetSeek.Desktop/Models/UiModels.cs</code> · 819 lines.

SHA-256: <code>aa424c9f4a87af8711d4ab50075945fd57072a5fa113ff88e5e3221d225f1ed1</code>.

Declarations: <code>CurrencyFormatter</code> (line 6), <code>CategoryItem : ReactiveObject</code> (line 20), <code>ProductCategoryOption</code> (line 47), <code>ExpenseCategoryOption</code> (line 64), <code>ProductPurposeOption</code> (line 79), <code>UomOption</code> (line 84), <code>StoreUomPreferenceItem : ReactiveObject</code> (line 138), <code>ProductItem : ReactiveObject</code> (line 160), <code>OrderItem : ReactiveObject</code> (line 186), <code>StaleCartPriceReviewUiRow</code> (line 262), <code>LotCandidateItem</code> (line 270), <code>SerialCandidateItem : ReactiveObject</code> (line 285), <code>OrderStatusChip : ReactiveObject</code> (line 309), <code>OrderLogItem : ReactiveObject</code> (line 349), <code>InventoryItem : ReactiveObject</code> (line 380), <code>KitComponentDraftItem : ReactiveObject</code> (line 497), <code>PayrollMonthOption : IEquatable&lt;PayrollMonthOption&gt;</code> (line 529), <code>StaffMember : ReactiveObject</code> (line 553), <code>TeamMemberShiftItem : ReactiveObject</code> (line 613), <code>UserPermissionOverrideItem : ReactiveObject</code> (line 624), <code>ReportTenderItem : ReactiveObject</code> (line 682), <code>ShiftReportSummary : ReactiveObject</code> (line 691), <code>FacilityItem : ReactiveObject</code> (line 731), <code>BinLocationItem : ReactiveObject</code> (line 741), <code>ItemLocationEligibilityItem : ReactiveObject</code> (line 755), <code>ReceiveTrackingKind</code> (line 770), <code>ReceiveLineItem : ReactiveObject</code> (line 782).

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

<code>Software/src/GetSeek.Desktop/Services/UiPreferencesService.cs</code> · 4,796 lines.

SHA-256: <code>f6fdf6bb1caab8fdda7c32902551907904dd68e4ad877d2744d770dbcb02efa7</code>.

Declarations: <code>UiPreferences</code> (line 12), <code>IUiPreferencesService</code> (line 20), <code>UiPreferencesService : IUiPreferencesService</code> (line 30), <code>ILocalizationService</code> (line 86), <code>LocalizationService : ILocalizationService</code> (line 96), <code>ThemeManager</code> (line 4687).

<details markdown>
<summary>Methods, calls, table effects and failures (12)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-69a3b01d8029"></span><code>IUiPreferencesService.Load()</code><br>22–22 | — | No extracted literal effects. |
| <span id="m-592fdd3892e2"></span><code>IUiPreferencesService.Save(UiPreferences)</code><br>23–23 | — | No extracted literal effects. |
| <span id="m-c2b8dbfc95d6"></span><code>UiPreferencesService.Load()</code><br>47–64 | Exists @51; ReadAllText @53; Deserialize(UiPreferences) @54 | No extracted literal effects. |
| <span id="m-7261564d0166"></span><code>UiPreferencesService.Save(UiPreferences)</code><br>66–82 | GetDirectoryName @70; IsNullOrEmpty @71; CreateDirectory @73; WriteAllText @76; Serialize @76 | No extracted literal effects. |
| <span id="m-6065c0c3e12d"></span><code>ILocalizationService.Localize(string,object?[])</code><br>89–89 | — | No extracted literal effects. |
| <span id="m-9613ad2534cb"></span><code>LocalizationService.Localize(string,object?[])</code><br>4654–4684 | ToLowerInvariant @4656; Trim @4656; TryGetValue @4664; TryGetValue @4667; Format @4677 | No extracted literal effects. |
| <span id="m-ad2564d444f7"></span><code>ThemeManager.Resolve(string?)</code><br>4704–4705 | IsNullOrWhiteSpace @4705; ContainsKey @4705 | No extracted literal effects. |
| <span id="m-2f54069bce5a"></span><code>ThemeManager.DisplayName(string?)</code><br>4707–4707 | Resolve @4707 | No extracted literal effects. |
| <span id="m-be5ea9b047a7"></span><code>ThemeManager.NextTheme(string?)</code><br>4710–4723 | Equals @4715 | No extracted literal effects. |
| <span id="m-b7d6ad204c3e"></span><code>ThemeManager.Apply(string?)</code><br>4726–4760 | Equals @4729; Resolve @4731; SwapThemeSlot @4745; CheckAccess @4750; Post @4752; ApplyCore @4756 | No extracted literal effects. |
| <span id="m-298ef8b009b4"></span><code>ThemeManager.IsThemeInclude(object)</code><br>4763–4765 | Contains @4765 | No extracted literal effects. |
| <span id="m-402551991a5e"></span><code>ThemeManager.SwapThemeSlot(IList&lt;IResourceProvider&gt;,string)</code><br>4767–4790 | ToList(ResourceInclude) @4771; Where(ResourceInclude) @4771; OfType(ResourceInclude) @4771; Remove @4773; Equals @4778; Add @4789 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Teams.cs</code> · 1,904 lines.

SHA-256: <code>57ea9efffd1c45429bb49f166ea5661c24a90919c17abb2f08dbce8b89d1541b</code>.

Declarations: <code>MainViewModel</code> (line 24), <code>TeamMemberBaseline</code> (line 540).

<details markdown>
<summary>Methods, calls, table effects and failures (23)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-01e8fdfeb22f"></span><code>MainViewModel.ConfigureTeamsPorts(ITeamsReader,IPinHasher?)</code><br>30–34 | — | No extracted literal effects. |
| <span id="m-631c93f0ef8d"></span><code>MainViewModel.RaiseTeamsLabels()</code><br>331–354 | RaisePropertyChanged @333; nameof @333 | No extracted literal effects. |
| <span id="m-b2b9b819a6f2"></span><code>MainViewModel.OnTeamMemberFieldChanged()</code><br>573–576 | CheckTeamMemberIsDirty @575 | No extracted literal effects. |
| <span id="m-48c5e63b17f1"></span><code>MainViewModel.CaptureTeamMemberBaseline()</code><br>578–602 | ToList @580; Select @580 | No extracted literal effects. |
| <span id="m-57970e613d3b"></span><code>MainViewModel.CheckTeamMemberIsDirty()</code><br>604–629 | ToList @607; Select @607; All @609; Zip @609; Equals @611 | No extracted literal effects. |
| <span id="m-e15dfc254834"></span><code>MainViewModel.CheckSalarySectionIsDirty()</code><br>631–641 | Equals @637 | No extracted literal effects. |
| <span id="m-88afe1ac9666"></span><code>MainViewModel.GetRegisteredPermissionDefinitions()</code><br>646–675 | — | No extracted literal effects. |
| <span id="m-61bb4b8cbb49"></span><code>MainViewModel.LoadDefaultPermissionOverrides()</code><br>677–695 | Clear @679; GetRegisteredPermissionDefinitions @680; Add @684 | No extracted literal effects. |
| <span id="m-32b1f47a6683"></span><code>MainViewModel.InitializeTeamsCommands()</code><br>745–874 | Create @747; CreateFromTask @748; CreateFromTask(string) @753; CreateFromTask(object?) @755; IsNullOrWhiteSpace @757; ConfigureAwait @759; OpenEditTeamMemberModalAsync @759; Create(object?) @763; OpenChangePinModal @767; Execute @775; Execute @783; Create(string) @787; IsNullOrEmpty @797; OnTeamMemberFieldChanged @800; OpenShiftForStaffAsync @835; LoadTeamMemberShiftHistoryAsync @842; LoadTeamsStaffAsync @843; OpenCloseShiftModal @849; SaveTeamMemberAsync @869; BindRefresh @872; ApplyTeamsTablePage @872; BuildTeamsTable @873 | No extracted literal effects. |
| <span id="m-976e3464bd76"></span><code>MainViewModel.BuildTeamsTable()</code><br>876–915 | CreateColumns @883; TextColumn @884; Localize @884; IsNullOrWhiteSpace @885; LocalizeTable @904; Max @912; Ceiling @912; RaisePropertyChanged @914; nameof @914 | No extracted literal effects. |
| <span id="m-61c3315b7e1a"></span><code>MainViewModel.CreateTeamMemberStatusCell(object)</code><br>917–941 | SetTip @938; ConfigureAwait @939; ToggleTeamMemberStatusAsync @939 | No extracted literal effects. |
| <span id="m-5b20bce73201"></span><code>MainViewModel.ToggleTeamMemberStatusAsync(StaffMember)</code><br>943–1019 | IsNullOrWhiteSpace @955; ToLowerInvariant @955; Trim @955; ConfigureAwait(UpdateTeamMemberCommand, UpdateTeamMemberResult) @994; ExecuteAsync(UpdateTeamMemberCommand, UpdateTeamMemberResult) @994; DispatchToUi @997; LoadTeamsStaffAsync @1009 | No extracted literal effects. |
| <span id="m-bb33db91a4c7"></span><code>MainViewModel.LoadTeamMemberShiftHistoryAsync(Guid)</code><br>1021–1095 | CreateCommand @1027; CreateParameter @1035; ToString @1037; Add @1038; ConfigureAwait @1046; ExecuteReaderAsync @1046; ReadAsync @1047; GetString @1049; GetInt64 @1050; IsDBNull @1051; GetInt32 @1052; Add @1069; DispatchToUi @1081; Clear @1083; Add @1084 | FROM shifts @1029 |
| <span id="m-8a0e646163b9"></span><code>MainViewModel.ApplyTeamsTablePage(IEnumerable&lt;StaffMember&gt;?)</code><br>1097–1131 | IsNullOrWhiteSpace @1101; Trim @1103; Where @1104; Contains @1105; Contains @1106; Contains @1107; ThenBy @1121; OrderByDescending @1121; OrderBy @1121; ApplyLocalPage @1130 | No extracted literal effects. |
| <span id="m-949bef7567a3"></span><code>MainViewModel.LoadTeamsStaffAsync()</code><br>1133–1261 | ApplyTeamsTablePage @1137; Clear @1145; ApplyPagedResult @1146; ConfigureAwait @1167; GetTeamMembersAsync @1167; DispatchToUi @1169; IsNullOrEmpty @1182; Contains @1183; Pow @1192; ToString @1193; Add @1240; Add @1241; SafeError @1259 | No extracted literal effects. |
| <span id="m-c29549ed8878"></span><code>MainViewModel.ResetTeamMemberFormState()</code><br>1263–1302 | Increment @1265; Clear @1301 | No extracted literal effects. |
| <span id="m-312fe951aaa1"></span><code>MainViewModel.OpenAddTeamMemberModal()</code><br>1304–1373 | GetResult @1323; GetAwaiter @1323; GetStoreTimeZoneAsync @1323; GetStoreLocalMonth @1331; ToDateTime @1336; GetStoreLocalDate @1336; Localize @1352; IsNullOrWhiteSpace @1353; Clear @1366; LoadDefaultPermissionOverrides @1369; CaptureTeamMemberBaseline @1370 | No extracted literal effects. |
| <span id="m-227def267d61"></span><code>MainViewModel.OpenEditTeamMemberModalAsync(string)</code><br>1375–1603 | Read @1377; ConfigureAwait @1389; GetTeamMemberDetailAsync @1389; GetTeamMemberDetailAsync @1394; StartsWith @1411; TryParse @1414; AsSpan @1414; GetPersonAsync @1416; DispatchToUi @1423; ToDateTime @1439; ToDateTime @1440; Pow @1450; ToString @1455; ToString @1456; AddMonths @1456; Localize @1469; IsNullOrWhiteSpace @1470; Clear @1477; LoadTeamMemberShiftHistoryAsync @1482; LoadDefaultPermissionOverrides @1492; CaptureTeamMemberBaseline @1493; ToDateTime @1520; Clear @1557; GetRegisteredPermissionDefinitions @1558; ToDictionary @1559; TryGetValue @1564; Add @1569 | No extracted literal effects. |
| <span id="m-f24517e5571b"></span><code>MainViewModel.SaveTeamMemberAsync()</code><br>1605–1867 | IsNullOrWhiteSpace @1614; Trim @1625; All @1635; IsNullOrEmpty @1645; IsMatch @1680; Trim @1680; Trim @1687; Pow @1694; Round @1695; ToList @1704; Select @1704; Where @1704; Trim @1713; ToLowerInvariant @1714; Trim @1714; FromDateTime @1715; Trim @1718; Trim @1730; Trim @1731; Trim @1739; CheckSalarySectionIsDirty @1752; Trim @1767; ToString @1781; ConfigureAwait(CreateTeamMemberCommand, CreateTeamMemberResult) @1801; ExecuteAsync(CreateTeamMemberCommand, CreateTeamMemberResult) @1801; DispatchToUi @1804; ConfigureAwait(UpdateTeamMemberCommand, UpdateTeamMemberResult) @1825; ExecuteAsync(UpdateTeamMemberCommand, UpdateTeamMemberResult) @1825; LoadTeamsStaffAsync @1850; LoadSalaryWorkspaceAsync @1851 | No extracted literal effects. |
| <span id="m-64ab6de7568d"></span><code>MainViewModel.RequestCloseTeamMemberModal()</code><br>1869–1879 | CloseTeamMemberModal @1878 | No extracted literal effects. |
| <span id="m-8c8e5154edd1"></span><code>MainViewModel.CloseTeamMemberModal()</code><br>1881–1892 | — | No extracted literal effects. |
| <span id="m-6cc30735de8f"></span><code>MainViewModel.ConfirmDiscardTeamMemberForm()</code><br>1894–1898 | CloseTeamMemberModal @1897 | No extracted literal effects. |
| <span id="m-540c154845a9"></span><code>MainViewModel.KeepEditingTeamMemberForm()</code><br>1900–1903 | — | No extracted literal effects. |

</details>

## MainViewModel.ThirdParties.cs {#src-974d69a1850f}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdParties.cs</code> · 4,425 lines.

SHA-256: <code>280e894bfeb96677c94fae731cc7ada4020491220ca92a472a4e0b2cb5876887</code>.

Declarations: <code>MainViewModel</code> (line 32), <code>ThirdPartyFormSnapshot</code> (line 160), <code>ItemTierPricingRow : ReactiveObject</code> (line 4303), <code>PricingRoundingOption</code> (line 4352), <code>PricingIncrementOption</code> (line 4353), <code>PricingMethodOption</code> (line 4354), <code>PricingCostBasisOption</code> (line 4355), <code>CategoryPricingPreviewProduct</code> (line 4356), <code>TierWeightModeOption</code> (line 4360), <code>PriceOfferRow</code> (line 4362), <code>PendingShelfLabelRow : ReactiveObject</code> (line 4383), <code>KitPriceAlertRow</code> (line 4405).

<details markdown>
<summary>Methods, calls, table effects and failures (74)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f6748aa6eaea"></span><code>MainViewModel.SetThirdPartyFormValue(T,T,string?)</code><br>188–195 | Equals(T) @190; RaiseAndSetIfChanged @193; RaisePropertyChanged @194; nameof @194 | No extracted literal effects. |
| <span id="m-194379d2b2b1"></span><code>MainViewModel.CaptureThirdPartyFormSnapshot()</code><br>197–201 | — | No extracted literal effects. |
| <span id="m-cf0a11cec1ac"></span><code>MainViewModel.CaptureThirdPartyFormBaseline()</code><br>203–207 | CaptureThirdPartyFormSnapshot @205; RaisePropertyChanged @206; nameof @206 | No extracted literal effects. |
| <span id="m-a718c0780d1b"></span><code>MainViewModel.KindMatches(string?,string)</code><br>365–374 | ToLowerInvariant @367; Trim @367 | No extracted literal effects. |
| <span id="m-8730d5b4f808"></span><code>MainViewModel.CycleThirdPartyLifecycleStatusScope()</code><br>450–455 | — | No extracted literal effects. |
| <span id="m-3ae81eb2856d"></span><code>MainViewModel.FormatBatchPrice(long)</code><br>907–912 | Clamp @909; ScalingFactor @910; ToString @911 | No extracted literal effects. |
| <span id="m-7d6a80f55185"></span><code>MainViewModel.LocalizeBatchPricingOutcome(string)</code><br>914–921 | StartsWith @916; Localize @920 | No extracted literal effects. |
| <span id="m-a2e8946c9075"></span><code>MainViewModel.InvalidateBatchPricingPreview()</code><br>923–935 | CancelBatchPricingPreviewExpiry @925; RaisePropertyChanged @930; nameof @930 | No extracted literal effects. |
| <span id="m-942d46fd3c21"></span><code>MainViewModel.CurrentBatchPricingOptions()</code><br>937–940 | ToMinorUnits @939; Clamp @939 | No extracted literal effects. |
| <span id="m-31c42e9e345e"></span><code>MainViewModel.CurrentBatchPricingOptionsJson()</code><br>941–942 | OperationParametersJson @941; CurrentBatchPricingOptions @942 | No extracted literal effects. |
| <span id="m-aed5fb42aeac"></span><code>MainViewModel.CurrentSelectedBatchIdsJson()</code><br>944–944 | Serialize @944; GetSelectedIdsForPreview @944 | No extracted literal effects. |
| <span id="m-c09e1756f8c3"></span><code>MainViewModel.StartBatchPricingPreviewExpiry(Guid,DateTime)</code><br>946–951 | CancelBatchPricingPreviewExpiry @948; NotifyBatchPricingPreviewExpiryAsync @950 | No extracted literal effects. |
| <span id="m-9085482b9f1c"></span><code>MainViewModel.CancelBatchPricingPreviewExpiry()</code><br>953–958 | Cancel @955; Dispose @956 | No extracted literal effects. |
| <span id="m-358db6342656"></span><code>MainViewModel.NotifyBatchPricingPreviewExpiryAsync(Guid,DateTime,CancellationToken)</code><br>960–973 | ConfigureAwait @965; Delay @965; DispatchToUi @966; RaisePropertyChanged @969; nameof @969 | No extracted literal effects. |
| <span id="m-b4ca3dd779a5"></span><code>MainViewModel.KeepEditingThirdPartyForm()</code><br>1056–1056 | — | No extracted literal effects. |
| <span id="m-810dd7bf6019"></span><code>MainViewModel.OpenBatchPricingForSelectedItems()</code><br>1115–1126 | CheckSessionUnlocked @1117; DispatchToUi @1120; Localize @1120; InvalidateBatchPricingPreview @1124 | No extracted literal effects. |
| <span id="m-ead1e1f67300"></span><code>MainViewModel.OpenAddThirdParty()</code><br>1156–1175 | CheckSessionUnlocked @1158; RequestCloseThirdPartyForm @1161; ClearThirdPartyForm @1164; FirstOrDefault @1167; CaptureThirdPartyFormBaseline @1174 | No extracted literal effects. |
| <span id="m-0929ef772964"></span><code>MainViewModel.OpenEditThirdParty(ThirdPartyDto?)</code><br>1177–1209 | CheckSessionUnlocked @1179; IsNullOrWhiteSpace @1185; FirstOrDefault @1198; FirstOrDefault @1200; CaptureThirdPartyFormBaseline @1208 | No extracted literal effects. |
| <span id="m-f5ce7ecc6567"></span><code>MainViewModel.RequestThirdPartyStatusChange(ThirdPartyDto?)</code><br>1211–1224 | Contains @1214; CheckSessionUnlocked @1215; HasPermission @1216; RaisePropertyChanged @1220; nameof @1220 | No extracted literal effects. |
| <span id="m-a74002ab49c6"></span><code>MainViewModel.ConfirmThirdPartyStatusChangeAsync()</code><br>1226–1250 | Add @1229; CancelThirdPartyStatusChange @1231; RefreshSharedDataTableDefinitions @1232; RaisePropertyChanged @1233; nameof @1233; ConfigureAwait @1237; ReactivateThirdPartyAsync @1237; DeactivateThirdPartyAsync @1239; Remove @1243; DispatchToUi @1244 | No extracted literal effects. |
| <span id="m-70cd07b68f8a"></span><code>MainViewModel.CancelThirdPartyStatusChange()</code><br>1252–1259 | RaisePropertyChanged @1256; nameof @1256 | No extracted literal effects. |
| <span id="m-164298518901"></span><code>MainViewModel.SaveThirdPartyPriceLevelAsync(ThirdPartyDto,string,ComboBox?)</code><br>1261–1297 | IsNullOrWhiteSpace @1264; Equals @1265; Add @1266; CheckSessionUnlocked @1268; Remove @1270; FirstOrDefault @1271; ConfigureAwait(SetThirdPartyPriceLevelCommand, bool) @1279; ExecuteAsync(SetThirdPartyPriceLevelCommand, bool) @1279; DispatchToUi @1282; SafePipelineError @1282; Localize @1284; SafeError @1288; ConfigureAwait @1293; LoadThirdPartiesAsync @1293; HasPermission @1295 | No extracted literal effects. |
| <span id="m-2a705395afc4"></span><code>MainViewModel.RequestCloseThirdPartyForm()</code><br>1299–1314 | CloseThirdPartyForm @1313 | No extracted literal effects. |
| <span id="m-45d51f7dda0e"></span><code>MainViewModel.ConfirmDiscardThirdPartyForm()</code><br>1316–1320 | CloseThirdPartyForm @1319 | No extracted literal effects. |
| <span id="m-51fa7785268c"></span><code>MainViewModel.CloseThirdPartyForm()</code><br>1322–1331 | ClearThirdPartyForm @1329; RaisePropertyChanged @1330; nameof @1330 | No extracted literal effects. |
| <span id="m-6c99b5e29678"></span><code>MainViewModel.OpenThirdPartiesWorkspace(string?)</code><br>1337–1352 | CheckSessionUnlocked @1339; SelectMenu @1343; IsNullOrWhiteSpace @1346; ResetToFirstPage @1349; LoadThirdPartiesAsync @1350 | No extracted literal effects. |
| <span id="m-23dfbd325d9a"></span><code>MainViewModel.OpenEditPartyFromChooserAsync(CustomerDto?)</code><br>1360–1382 | CloseCustomerChooser @1364; SelectMenu @1368; ConfigureAwait @1371; LoadThirdPartiesAsync @1371; FirstOrDefault @1373; DispatchToUi @1381; OpenEditThirdParty @1381 | No extracted literal effects. |
| <span id="m-4e1615b88c9e"></span><code>MainViewModel.ClearThirdPartyForm()</code><br>1384–1405 | — | No extracted literal effects. |
| <span id="m-3141c0b54589"></span><code>MainViewModel.ConfirmSaveThirdPartyAsync()</code><br>1407–1481 | IsNullOrWhiteSpace @1409; NormalizeDbValue @1424; Trim @1430; NullIfBlank @1431; FirstOrDefault @1436; ConfigureAwait(UpdateThirdPartyCommand, ThirdPartyDto) @1441; ExecuteAsync(UpdateThirdPartyCommand, ThirdPartyDto) @1441; DispatchToUi @1444; SafePipelineError @1444; ConfigureAwait(CreateThirdPartyCommand, ThirdPartyDto) @1461; ExecuteAsync(CreateThirdPartyCommand, ThirdPartyDto) @1461; ConfigureAwait @1469; LoadThirdPartiesAsync @1469; LoadThirdPartiesLegacyListsAsync @1470; CloseThirdPartyForm @1473; SafeError @1479 | No extracted literal effects. |
| <span id="m-0b4709774874"></span><code>MainViewModel.DeactivateThirdPartyAsync(Guid)</code><br>1483–1515 | CheckSessionUnlocked @1485; ConfigureAwait(DeactivateThirdPartyCommand, bool) @1496; ExecuteAsync(DeactivateThirdPartyCommand, bool) @1496; DispatchToUi @1499; SafePipelineError @1499; ConfigureAwait @1503; LoadThirdPartiesAsync @1503; LoadThirdPartiesLegacyListsAsync @1504; SafeError @1513 | No extracted literal effects. |
| <span id="m-b10d340cd055"></span><code>MainViewModel.LoadThirdPartiesAsync()</code><br>1520–1549 | Increment @1523; ConfigureAwait @1526; GetPagedThirdPartiesAsync @1526; ToPageRequest @1528; DispatchToUi @1536; Read @1538; Clear @1539; AddRange @1540; ApplyPagedResult @1541; RefreshThirdPartyList @1542; SafeError @1547 | No extracted literal effects. |
| <span id="m-4303771d79dc"></span><code>MainViewModel.LoadThirdPartiesLegacyListsAsync()</code><br>1552–1556 | ConfigureAwait @1554; LoadCustomersAsync @1554; LoadSuppliersAsync @1555 | No extracted literal effects. |
| <span id="m-bec8d29b30c7"></span><code>MainViewModel.LoadPriceLevelSettingsAsync()</code><br>1558–1627 | CreateCommand @1565; ConfigureAwait @1568; ExecuteScalarAsync @1568; ToInt32 @1571; ExecuteReaderAsync @1578; ReadAsync @1579; ParseStoredPercentage @1581; IsDBNull @1581; GetString @1581; GetInt32 @1581; ToString @1582; Add @1583; DispatchToUi @1593; Clear @1597; Clear @1598; Clear @1599; Add @1602; Add @1605; Add @1606; Any @1610; FirstOrDefault @1615; BuildItemTierRows @1620; SafeError @1625 | FROM price_level_settings @1577; FROM store_config @1567 |
| <span id="m-0897a95aa39d"></span><code>MainViewModel.LoadPriceProposalsAsync()</code><br>1629–1725 | Increment @1632; ConfigureAwait @1633; WaitAsync @1633; CreateCommand @1637; ToInt32 @1640; ExecuteScalarAsync @1640; Max @1644; Ceiling @1644; Min @1645; ToLowerInvariant @1647; IsNullOrWhiteSpace @1656; AddSqlParam @1671; ExecuteReaderAsync @1673; ReadAsync @1674; IsDBNull @1676; GetString @1676; TryParse @1683; Localize @1685; Format @1686; ScalingFactor @1687; Add @1690; ParseGuidSafe @1691; GetInt64 @1693; ParseDate @1697; Read @1703; DispatchToUi @1705; ApplyPagedResult @1708; Clear @1709; Add @1712; SafeError @1719; Release @1723 | FROM price_change_proposals @1639 · DYNAMIC SQL: inspect manually |
| <span id="m-b794d2a0b7cb"></span><code>MainViewModel.SavePriceTierSettingsAsync()</code><br>1727–1768 | TryParse @1740; DispatchToUi @1743; Localize @1743; Add @1746; ToString @1749; ConfigureAwait(UpdatePriceTierSettingsCommand, bool) @1754; ExecuteAsync(UpdatePriceTierSettingsCommand, bool) @1754; SafePipelineError @1757; ConfigureAwait @1761; LoadPriceLevelSettingsAsync @1761; SafeError @1766 | No extracted literal effects. |
| <span id="m-83559744e4d4"></span><code>MainViewModel.ResolveProposalAsync(string?,bool)</code><br>1770–1802 | TryParse @1772; ConfigureAwait(ResolvePriceChangeProposalCommand, bool) @1781; ExecuteAsync(ResolvePriceChangeProposalCommand, bool) @1781; DispatchToUi @1784; SafePipelineError @1784; ConfigureAwait @1790; LoadPriceProposalsAsync @1790; Localize @1791; SafeError @1800 | No extracted literal effects. |
| <span id="m-56d2f1ca4c73"></span><code>MainViewModel.LoadItemPricingAsync(InventoryItem?)</code><br>1807–1909 | DispatchToUi @1811; RaisePropertyChanged @1814; nameof @1814; ToString @1820; CreateCommand @1823; CreateParameter @1830; Add @1830; ConfigureAwait @1831; ExecuteReaderAsync @1831; ReadAsync @1832; IsDBNull @1834; GetString @1834; GetInt32 @1835; ParseStoredPricingPercentForDisplay @1836; GetInt64 @1840; ToDisplayAmount @1853; IsIncrementRoundingRule @1855; CalculateAsync @1865; TryGetValue @1890; SafeError @1907 | FROM item_price_levels @1872; FROM item_pricing @1825 |
| <span id="m-94abdd2d0568"></span><code>MainViewModel.BuildItemTierRows(IEnumerable&lt;PriceLevelSettingDto&gt;)</code><br>1911–1928 | Count @1913; Clear @1918; OrderBy @1919; Where @1919; Add @1921 | No extracted literal effects. |
| <span id="m-70e9e46d8643"></span><code>MainViewModel.SaveItemPricingAsync()</code><br>1930–1982 | Add @1955; ToCommand @1965; ConfigureAwait(SaveItemPricingCommand, bool) @1968; ExecuteAsync(SaveItemPricingCommand, bool) @1968; DispatchToUi @1972; SafePipelineError @1972; SafeError @1980 | No extracted literal effects. |
| <span id="m-4c413ad4839c"></span><code>MainViewModel.CreateBatchPricingPreviewAsync()</code><br>1984–2042 | Localize @1995; DispatchToUi @2001; InvalidateBatchPricingPreview @2001; GetSelectedIdsForPreview @2002; CurrentBatchPricingOptions @2012; ConfigureAwait(CreateBatchPreviewCommand, BatchPreviewResult) @2013; ExecuteAsync(CreateBatchPreviewCommand, BatchPreviewResult) @2013; CurrentBatchPricingOptionsJson @2020; Serialize @2022; StartBatchPricingPreviewExpiry @2024; RaisePropertyChanged @2025; nameof @2025; SafePipelineError @2031; SafeError @2036 | No extracted literal effects. |
| <span id="m-864cb28a1ded"></span><code>MainViewModel.LoadCategoryPricingRuleAsync(ProductCategoryOption?)</code><br>2044–2131 | Equals @2046; DispatchToUi @2048; Clear @2051; CreateCommand @2061; AddSqlParam @2067; ToString @2067; ConfigureAwait @2068; ExecuteReaderAsync @2068; ReadAsync @2069; ParseGuidSafe @2072; GetString @2072; GetInt32 @2072; GetInt64 @2073; IsDBNull @2074; ParseDate @2075; Add @2091; Add @2101; TryParse @2115; ToDisplayAmount @2117; FirstOrDefault @2122; SafeError @2129 | FROM item_kits @2082; FROM items @2082; FROM product_category_pricing_rules @2063 |
| <span id="m-e4d7f70fd9ed"></span><code>MainViewModel.PreviewCategoryPricingRuleAsync()</code><br>2133–2225 | Localize @2137; ParseRoundingRule @2145; IsRoundingRuleCompatible @2146; TryConvertRoundingIncrement @2148; ConfigureAwait @2158; CalculateAsync @2158; CreateCommand @2170; AddSqlParam @2175; ToString @2175; ExecuteReaderAsync @2176; ReadAsync @2177; GetInt64 @2183; IsDBNull @2186; DisposeAsync @2201; SetCategoryPricingPreviewAsync @2208; ToInt64 @2217; ExecuteScalarAsync @2217; DispatchToUi @2223; SafeError @2223 | FROM items @2171; FROM items @2215; JOIN item_pricing @2171; JOIN item_pricing @2215 |
| <span id="m-f3416912b1f7"></span><code>MainViewModel.SetCategoryPricingPreviewAsync(decimal,long,string,RoundingRule,long,int)</code><br>2227–2259 | ParsePricingMethod @2231; ToMinorUnits @2233; CalculateUnroundedBasePriceMinor @2235; ResolveEffectiveBasePrice @2236; ScalingFactor @2238; FormatPricingCandidate @2239; Format @2241; ToDisplayAmount @2241; Abs @2245; FirstOrDefault @2246; Localize @2249; DispatchToUi @2255; ToString @2257 | No extracted literal effects. |
| <span id="m-898df343b4e3"></span><code>MainViewModel.FormatPricingCandidate(decimal,int)</code><br>2261–2267 | ScalingFactor @2263; Min @2264; ToString @2265; ToString @2266 | No extracted literal effects. |
| <span id="m-21c88402b457"></span><code>MainViewModel.SaveCategoryPricingRuleAsync()</code><br>2269–2307 | Localize @2273; ToMinorUnits @2287; ConfigureAwait(SaveCategoryPricingRuleCommand, CategoryPricingRuleSaveResult) @2290; ExecuteAsync(SaveCategoryPricingRuleCommand, CategoryPricingRuleSaveResult) @2290; DispatchToUi @2294; SafePipelineError @2294; ConfigureAwait @2298; LoadCategoryPricingRuleAsync @2298; LoadPriceProposalsAsync @2299; SafeError @2305 | No extracted literal effects. |
| <span id="m-dd366b199e60"></span><code>MainViewModel.DeactivateCategoryPricingRuleAsync()</code><br>2309–2330 | ConfigureAwait(DeactivateCategoryPricingRuleCommand, bool) @2314; ExecuteAsync(DeactivateCategoryPricingRuleCommand, bool) @2314; DispatchToUi @2319; SafePipelineError @2319; ConfigureAwait @2322; LoadCategoryPricingRuleAsync @2322; LoadPriceProposalsAsync @2323; Localize @2324; SafeError @2328 | No extracted literal effects. |
| <span id="m-c33d7786e3c9"></span><code>MainViewModel.LoadKitComponentCostPreviewAsync(InventoryItem,string)</code><br>2332–2359 | ConfigureAwait @2341; CalculateAsync @2341; DispatchToUi @2343; Equals @2346; RaisePropertyChanged @2352; nameof @2352; SafeError @2357 | No extracted literal effects. |
| <span id="m-a5b88bab197c"></span><code>MainViewModel.FormatKitComponentCostPreview(KitComponentCostResult)</code><br>2361–2377 | Localize @2363; ScalingFactor @2368; Format @2369; Select @2370; ToString @2371; FormatMinor @2371; Join @2375 | No extracted literal effects. |
| <span id="m-8547d39be80d"></span><code>MainViewModel.ReactivateThirdPartyAsync(Guid)</code><br>2379–2405 | CheckSessionUnlocked @2381; ConfigureAwait(ReactivateThirdPartyCommand, bool) @2386; ExecuteAsync(ReactivateThirdPartyCommand, bool) @2386; DispatchToUi @2390; SafePipelineError @2390; ConfigureAwait @2393; LoadThirdPartiesAsync @2393; LoadThirdPartiesLegacyListsAsync @2394; SafeError @2403 | No extracted literal effects. |
| <span id="m-8242530d0d7f"></span><code>MainViewModel.ConfirmBatchPricingAsync()</code><br>2411–2450 | DispatchToUi @2415; Localize @2415; CurrentBatchPricingOptions @2421; ConfigureAwait(ApplyBatchPricingCommand, BatchPricingResult) @2426; ExecuteAsync(ApplyBatchPricingCommand, BatchPricingResult) @2426; ToString @2427; InvalidateBatchPricingPreview @2430; ConfigureAwait @2431; LoadInventoryAsync @2431; LoadPriceProposalsAsync @2432; SafePipelineError @2439; SafeError @2444 | No extracted literal effects. |
| <span id="m-954ef899c3dc"></span><code>MainViewModel.RequestElevationForCheckout(string?)</code><br>2455–2470 | Clear @2457; DistinctBy @2458; Where @2458; GetUnlockCandidates @2458; Equals @2459; Add @2463; Localize @2467 | No extracted literal effects. |
| <span id="m-36d4fd9b0282"></span><code>MainViewModel.CancelElevation()</code><br>2472–2479 | — | No extracted literal effects. |
| <span id="m-f5d10bce79d8"></span><code>MainViewModel.ConfirmElevationAsync()</code><br>2481–2525 | Localize @2486; IsNullOrWhiteSpace @2490; AuthenticateSelectedUser @2498; Trim @2498; Any @2499; Equals @2499; Contains @2502; HasPermission @2505; ConfigureAwait @2519; PlaceOrderAsync @2519; SafeError @2523 | No extracted literal effects. |
| <span id="m-ca0f7e171aab"></span><code>MainViewModel.FormatCartSummaryNumber(decimal)</code><br>2710–2717 | Clamp @2715; ToString @2716 | No extracted literal effects. |
| <span id="m-5f0035f264d4"></span><code>MainViewModel.Localize(string,object?[])</code><br>3175–3175 | Localize @3175 | No extracted literal effects. |
| <span id="m-76eb89727af7"></span><code>MainViewModel.RaiseLocalizedLabels()</code><br>3181–3930 | RaisePropertyChanged @3183; nameof @3183; RefreshManufacturingLocalization @3681; RefreshTraceabilityLocalization @3682; RefreshCommercialLocalization @3683; RefreshImportLocalization @3684 | No extracted literal effects. |
| <span id="m-b3ce7cd05e31"></span><code>MainViewModel.RefreshThirdPartyList()</code><br>3935–3942 | Clear @3937; Add @3940 | No extracted literal effects. |
| <span id="m-81871dcea20c"></span><code>MainViewModel.NullIfBlank(string?)</code><br>3944–3944 | IsNullOrWhiteSpace @3944; Trim @3944 | No extracted literal effects. |
| <span id="m-0319efc772a4"></span><code>MainViewModel.ParsePercent(string?)</code><br>3946–3947 | TryParse @3947 | No extracted literal effects. |
| <span id="m-48e17fe39d5a"></span><code>MainViewModel.ParseStoredPricingPercentForDisplay(string?,int)</code><br>3949–3950 | ParseStoredPercentage @3950 | No extracted literal effects. |
| <span id="m-318ba06c0978"></span><code>MainViewModel.IsIncrementRoundingRule(string?)</code><br>3952–3954 | Equals @3953 | No extracted literal effects. |
| <span id="m-af82dfbe9f96"></span><code>MainViewModel.ParseDate(string?)</code><br>3956–3957 | TryParse @3957 | No extracted literal effects. |
| <span id="m-6593502e046b"></span><code>MainViewModel.OpenNewPriceOffer()</code><br>4055–4065 | ToString @4059; ToString @4060; AddDays @4060; FirstOrDefault @4062 | No extracted literal effects. |
| <span id="m-c5d60b83c5fb"></span><code>MainViewModel.OpenEditPriceOfferAsync(PriceOfferRow)</code><br>4067–4090 | CreateCommand @4070; CreateParameter @4073; ToString @4073; Add @4073; ConfigureAwait @4074; ExecuteReaderAsync @4074; ReadAsync @4074; Parse @4075; GetString @4075; GetInt32 @4075; IsDBNull @4077; TryParse @4077; ToString @4077; ToUniversalTime @4077; ToString @4077; ToUniversalTime @4078; AddDays @4078; FirstOrDefault @4080; TryParse @4082; FirstOrDefault @4083; Pow @4086; GetInt64 @4087 | FROM price_offers @4070; JOIN items @4070 |
| <span id="m-03775da63068"></span><code>MainViewModel.SavePriceOfferAsync()</code><br>4092–4109 | CheckSessionUnlocked @4094; TryParse @4095; ToString @4095; Round @4095; Pow @4095; IsNullOrWhiteSpace @4096; ConfigureAwait(SavePriceOfferCommand, Guid) @4105; ExecuteAsync(SavePriceOfferCommand, Guid) @4105; ReportError @4106; DispatchToUi @4107; ConfigureAwait @4108; LoadPriceOffersAsync @4108 | No extracted literal effects. |
| <span id="m-67c18350076c"></span><code>MainViewModel.TogglePriceOfferAsync(PriceOfferRow)</code><br>4111–4119 | CheckSessionUnlocked @4113; ConfigureAwait(SetPriceOfferStatusCommand, bool) @4115; ExecuteAsync(SetPriceOfferStatusCommand, bool) @4115; ReportError @4117; ConfigureAwait @4118; LoadPriceOffersAsync @4118 | No extracted literal effects. |
| <span id="m-2e8ada01bb08"></span><code>MainViewModel.LoadPriceOffersAsync()</code><br>4121–4160 | CreateCommand @4126; ConfigureAwait @4136; ExecuteReaderAsync @4136; ReadAsync @4137; Add @4139; Parse @4140; GetString @4140; GetDouble @4144; GetInt64 @4147; IsDBNull @4148; GetInt32 @4150; DispatchToUi @4153; Clear @4155; Add @4156 | FROM price_offers @4127; JOIN items @4127; JOIN product_categories @4127 |
| <span id="m-c1dd92421598"></span><code>MainViewModel.LoadPendingShelfLabelsAsync()</code><br>4162–4201 | CreateCommand @4167; ConfigureAwait @4176; ExecuteReaderAsync @4176; ReadAsync @4177; Add @4179; Parse @4180; GetString @4180; GetInt64 @4184; GetInt32 @4189; Add @4190; Remove @4190; RaisePropertyChanged @4190; nameof @4190; Localize @4191; DispatchToUi @4194; Clear @4196; Add @4197 | FROM pending_shelf_labels @4168; JOIN items @4168 |
| <span id="m-6ae160e2c5f3"></span><code>MainViewModel.LoadKitPriceReviewAlertsAsync()</code><br>4203–4242 | CreateCommand @4208; ConfigureAwait @4220; ExecuteReaderAsync @4220; ReadAsync @4221; Add @4223; Parse @4224; GetString @4224; GetInt64 @4228; GetInt32 @4232; DispatchToUi @4235; Clear @4237; Add @4238 | FROM kit_price_review_alerts @4209; JOIN items @4209 |
| <span id="m-457ffec7c305"></span><code>MainViewModel.SetKitPriceAlertStatusAsync(KitPriceAlertRow,string,string)</code><br>4244–4252 | CheckSessionUnlocked @4246; ConfigureAwait(ResolveKitPriceAlertCommand, bool) @4247; ExecuteAsync(ResolveKitPriceAlertCommand, bool) @4247; ReportError @4249; ConfigureAwait @4251; LoadKitPriceReviewAlertsAsync @4251 | No extracted literal effects. |
| <span id="m-c8b9f1957d0c"></span><code>MainViewModel.MarkShelfLabelsPrintedAsync()</code><br>4254–4257 | ConfigureAwait @4256; SetSelectedShelfLabelStatusAsync @4256 | No extracted literal effects. |
| <span id="m-83ef94eb9900"></span><code>MainViewModel.QueueSelectedShelfLabelsAsync()</code><br>4259–4271 | CheckSessionUnlocked @4261; ToArray @4262; Select @4262; Where @4262; Contains @4262; ConfigureAwait(QueueShelfLabelPrintCommand, string) @4265; ExecuteAsync(QueueShelfLabelPrintCommand, string) @4265; ReportError @4267; Clear @4268; RaisePropertyChanged @4268; nameof @4268; ConfigureAwait @4270; LoadPendingShelfLabelsAsync @4270 | No extracted literal effects. |
| <span id="m-ce1c906cd404"></span><code>MainViewModel.SetSelectedShelfLabelStatusAsync(string)</code><br>4273–4287 | CheckSessionUnlocked @4275; ToArray @4276; Select @4276; Where @4276; Contains @4276; ConfigureAwait(SetShelfLabelStatusCommand, int) @4279; ExecuteAsync(SetShelfLabelStatusCommand, int) @4279; Trim @4280; ReportError @4282; Clear @4283; RaisePropertyChanged @4284; nameof @4284; ConfigureAwait @4286; LoadPendingShelfLabelsAsync @4286 | No extracted literal effects. |
| <span id="m-1df13dfc4bfd"></span><code>MainViewModel.AddSqlParam(DbCommand,string,object)</code><br>4293–4299 | CreateParameter @4295; Add @4298 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 12,754 lines.

SHA-256: <code>86706870e08eb5924044a4e9920a1d54bb90a1165aebe540d51e896955c5c403</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 8398).

<details markdown>
<summary>Methods, calls, table effects and failures (253)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4d3c549b9d46"></span><code>MainViewModel.RefreshCurrentTime()</code><br>121–121 | RaisePropertyChanged @121; nameof @121 | No extracted literal effects. |
| <span id="m-47378cde4176"></span><code>MainViewModel.SetStatusNotificationOnUi(string)</code><br>391–404 | RaiseAndSetIfChanged @393; IsNullOrWhiteSpace @394; Insert @396; RemoveAt @397; RaisePropertyChanged @398; nameof @398; Stop @401; Start @403 | No extracted literal effects. |
| <span id="m-fa69ff5d121c"></span><code>MainViewModel.ClearNotifications()</code><br>426–433 | Stop @428; Clear @430; RaisePropertyChanged @431; nameof @431; RaiseAndSetIfChanged @432 | No extracted literal effects. |
| <span id="m-1aafdc317eca"></span><code>MainViewModel.CycleInventoryLifecycleStatusScope()</code><br>677–682 | — | No extracted literal effects. |
| <span id="m-fa7a7c7368c8"></span><code>MainViewModel.IsLockScreenLockedOut(int)</code><br>1195–1211 | Ceiling @1202 | No extracted literal effects. |
| <span id="m-0296ed547990"></span><code>MainViewModel.RefreshUnlockCandidates()</code><br>1253–1278 | GetUnlockCandidates @1256; Clear @1259; Add @1262; Any @1264; CheckAccess @1270; action @1272; Post @1276 | No extracted literal effects. |
| <span id="m-20644e5979ce"></span><code>MainViewModel.UpdateReceiveKitBreakdownAsync()</code><br>1636–1656 | GetValueOrDefault @1644; ConfigureAwait @1649; BuildBreakdownSummaryAsync @1649 | No extracted literal effects. |
| <span id="m-b8b5218c5298"></span><code>MainViewModel.UpdateCartKitBreakdownAsync(OrderItem)</code><br>1658–1670 | ConfigureAwait @1663; BuildBreakdownSummaryAsync @1663 | No extracted literal effects. |
| <span id="m-72beca74d937"></span><code>MainViewModel.OnProductPricingDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>2095–2114 | RaisePropertyChanged @2097; nameof @2097; RecomputeProductPricingPreview @2113 | No extracted literal effects. |
| <span id="m-0da38dca946b"></span><code>MainViewModel.RecomputeProductPricingPreview()</code><br>2123–2173 | Clear @2125; RaisePropertyChanged @2126; nameof @2126; ToMinorUnits @2135; Parse @2140; TryParse @2144; Equals @2158; Increment @2161; Localize @2162; ToArray @2164; RecomputeKitPricingPreviewAsync @2165; ResolveSelectedProductSaleUnitFactor @2170; Round @2171; RebuildProductPricingPreview @2172 | No extracted literal effects. |
| <span id="m-04391db598a1"></span><code>MainViewModel.RecomputeKitPricingPreviewAsync(long,string,string,decimal,string,long,decimal,IReadOnlyList&lt;KitComponentDraftItem&gt;)</code><br>2175–2245 | ConfigureAwait @2179; WaitAsync @2179; Read @2182; DispatchToUi @2186; SetProductPricingPreviewNotice @2186; CalculateItemOrKitAsync @2200; ResolveSelectedProductSaleUnitFactor @2224; Round @2225; RebuildProductPricingPreview @2229; Release @2243 | No extracted literal effects. |
| <span id="m-6dc02eedb494"></span><code>MainViewModel.SetProductPricingPreviewNotice(string)</code><br>2247–2251 | Localize @2249; RaisePropertyChanged @2250; nameof @2250 | No extracted literal effects. |
| <span id="m-2d522c49b5a8"></span><code>MainViewModel.RebuildProductPricingPreview(long,string,decimal,string,long,decimal)</code><br>2253–2317 | Clear @2256; RaisePropertyChanged @2258; nameof @2258; Equals @2259; SetProductPricingPreviewNotice @2261; ParsePricingMethod @2265; ParseRoundingRule @2266; IsRoundingRuleCompatible @2267; TryConvertRoundingIncrement @2274; ToMinorUnits @2281; ResolveEffectiveBasePrice @2282; ToList @2286; OrderBy @2286; Where @2286; FirstOrDefault @2293; TryParse @2304; ToString @2305; ResolveTierPrice @2308; Add @2310; Format @2312; ToDisplayAmount @2312; FirstOrDefault @2313 | No extracted literal effects. |
| <span id="m-222f0bd71a93"></span><code>MainViewModel.ResolveSelectedProductSaleUnitFactor()</code><br>2371–2386 | FirstOrDefault @2374; Equals @2374; TryParse @2378 | No extracted literal effects. |
| <span id="m-f8852b3130cd"></span><code>MainViewModel.ExactMinorToCurrency(decimal)</code><br>2394–2395 | ScalingFactor @2395; Clamp @2395 | No extracted literal effects. |
| <span id="m-1a5f58b98e5f"></span><code>MainViewModel.BuildCostSourcesTooltip(long,long,long,long?,string,DateTime?)</code><br>2452–2472 | Format @2460; ToDecimal @2461; Localize @2464; Format @2464; ToLocalTime @2466; Join @2471 | No extracted literal effects. |
| <span id="m-b40003c87e3d"></span><code>MainViewModel.AddKitComponent()</code><br>2632–2669 | IsNullOrWhiteSpace @2647; FirstOrDefault @2649; Equals @2650; Add @2657; RaisePropertyChanged @2668; nameof @2668 | No extracted literal effects. |
| <span id="m-4b3441ec4aa7"></span><code>MainViewModel.RemoveKitComponent(KitComponentDraftItem?)</code><br>2671–2678 | Remove @2675; RaisePropertyChanged @2676; nameof @2676 | No extracted literal effects. |
| <span id="m-e07213cf0109"></span><code>MainViewModel.RefreshVirtualKitAvailability()</code><br>2689–2702 | Increment @2691; ToArray @2698; Select @2698; LoadVirtualKitAvailabilityAsync @2701 | No extracted literal effects. |
| <span id="m-a05a10688a37"></span><code>MainViewModel.LoadVirtualKitAvailabilityAsync(long,IReadOnlyList&lt;KitComponentInput&gt;)</code><br>2704–2744 | ConfigureAwait @2708; GetKitAvailabilityAsync @2708; DispatchToUi @2710; Read @2712; Localize @2715; Max @2724; ResolveSelectedProductSaleUnitFactor @2724; GetValueOrDefault @2725; Clamp @2726; Pow @2727; Floor @2728; Format @2730; ToString @2732 | No extracted literal effects. |
| <span id="m-ef607f9a261f"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3524–3532 | IsNullOrWhiteSpace @3526 | No extracted literal effects. |
| <span id="m-1c89b3cc5821"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3534–3545 | Load @3536; IsNullOrWhiteSpace @3540; Resolve @3542; Apply @3544 | No extracted literal effects. |
| <span id="m-467d413fee4d"></span><code>MainViewModel.OpenImport()</code><br>3574–3588 | CheckSessionUnlocked @3576; Increment @3579; Clear @3583; Invoke @3587 | No extracted literal effects. |
| <span id="m-8217ef4f16c0"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3590–3647 | Increment @3593; Clear @3601; IsNullOrWhiteSpace @3607; Exists @3607; ConfigureAwait @3621; ReadAllBytesAsync @3621; ToHexString @3622; HashData @3622; TemplateContextAsync @3626; Run @3627; Read @3627; ValidateInventoryAsync @3628; CompletedWorkbook @3629; DispatchToUi @3630; ReferenceEquals @3632; Add @3633; Localize @3634; SetImportReviewRows @3637; RaisePropertyChanged @3638; nameof @3638; SafeError @3644 | No extracted literal effects. |
| <span id="m-3be3aaad4cca"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3649–3705 | ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3676; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3676; Localize @3682; DispatchToUi @3683; Invoke @3689; ConfigureAwait @3691; LoadInventoryAsync @3691; ReportError @3695; ReportException @3701 | No extracted literal effects. |
| <span id="m-796e7dae516f"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3717–3727 | Report @3719; DispatchToUi @3720; Insert @3722 | No extracted literal effects. |
| <span id="m-44112bc106ad"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3729–3733 | RaisePropertyChanged @3732; nameof @3732 | No extracted literal effects. |
| <span id="m-5e3d83c68de9"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3735–3738 | ReportError @3737 | No extracted literal effects. |
| <span id="m-b3354c7d05be"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3744–3749 | ReportError @3747 | No extracted literal effects. |
| <span id="m-417c0c5dbb18"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3758–3764 | IsNullOrWhiteSpace @3760; Trim @3760; ReportError @3762 | No extracted literal effects. |
| <span id="m-6e5e3c73eae9"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3766–3769 | DispatchToUi @3768; Insert @3768 | No extracted literal effects. |
| <span id="m-5eb83ea2abf1"></span><code>MainViewModel.DispatchToUi(Action)</code><br>3775–3789 | CheckAccess @3777; action @3779; GetResult @3787; GetAwaiter @3787; InvokeAsync @3787 | No extracted literal effects. |
| <span id="m-bcd910348f89"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4304–4367 | Register @4306; Execute @4306; Execute @4307; Execute @4312; Execute @4313; Execute @4314; Execute @4315; Execute @4316; Execute @4317; Execute @4318; Execute @4319; Execute @4320; Execute @4321; Execute @4322; Execute @4323; Execute @4324; Execute @4325; Execute @4326; Execute @4327; Execute @4328; Execute @4329; Execute @4330; Execute @4331; Execute @4332; Execute @4333; Execute @4334; Execute @4335; Execute @4336; Execute @4337; Execute @4338; Execute @4339; Execute @4340; Execute @4341; Execute @4342; Execute @4343; Execute @4345; Execute @4346; RequestClosePersonForm @4347; KeepEditingPersonForm @4348; CloseSalaryMonthDetailModal @4349; CloseSalaryPaymentModal @4350; CloseSalaryAdjustmentModal @4351; CloseSalaryFinalizeModal @4352; RequestCloseExpenseForm @4353; KeepEditingExpenseForm @4354; CloseExpenseCategoryModal @4355; CloseExpensePaymentModal @4356; CloseExpenseDetailModal @4357; ClosePaymentReturnModal @4358; CloseWasteExpenseConfirmation @4359; InitializeSalaryTables @4364; InitializeExpensesTables @4365; InitializeTeamsCommands @4366 | No extracted literal effects. |
| <span id="m-a9dbde566ccf"></span><code>MainViewModel.CreateDemo()</code><br>4369–4376 | SetActiveCashier @4372; Parse @4372; RefreshUnlockCandidates @4374 | No extracted literal effects. |
| <span id="m-7b8ba32ffeff"></span><code>MainViewModel.CreateInitializing()</code><br>4378–4386 | — | No extracted literal effects. |
| <span id="m-d882c56cd3c6"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4388–4398 | — | No extracted literal effects. |
| <span id="m-756a20f9a4a5"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4400–4418 | ConfigureDiagnosticsWorkspace @4414; ApplyPersistedState @4415; RefreshUnlockCandidates @4416 | No extracted literal effects. |
| <span id="m-0b55f0d33e2e"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4420–4448 | CheckSessionUnlocked @4422; HasPermission @4423; Equals @4434; GetFileNameWithoutExtension @4434; GetEntryAssembly @4436; Add @4438; Start @4441; ReportException @4446 | No extracted literal effects. |
| <span id="m-0f89b2491284"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4450–4473 | CheckSessionUnlocked @4452; HasPermission @4453; Equals @4463; GetFileNameWithoutExtension @4463; Add @4464; GetEntryAssembly @4464; Start @4466; ReportException @4471 | No extracted literal effects. |
| <span id="m-b471422148f9"></span><code>MainViewModel.Dispose()</code><br>4475–4494 | Increment @4477; ResetFinancialWorkspace @4479; Dispose @4480; Stop @4481; CancelBatchPricingPreviewExpiry @4484; Dispose @4485; Dispose @4486; DisposeSearchStates @4492; SuppressFinalize @4493 | No extracted literal effects. |
| <span id="m-94f130a86740"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4496–4500 | Stop @4498 | No extracted literal effects. |
| <span id="m-79f933550ba9"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4502–4540 | Clear @4512; Clear @4513; Clear @4514; Clear @4515; Clear @4516; Clear @4517; Clear @4518; Clear @4519; Clear @4520; Clear @4521 | No extracted literal effects. |
| <span id="m-2bf26efae448"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4542–4645 | RaisePropertyChanged @4556; nameof @4556; Clear @4558; Clear @4559; Clear @4560; CreateCommand @4567; ExecuteReader @4569; Read @4570; TryParse @4572; GetString @4572; Add @4573; Add @4581; GroupBy @4582; Count @4584; Contains @4589; Add @4606; Add @4607; SetActiveCashier @4615; ToString @4619; ToString @4622; ToLocalTime @4622; NotifyTotalsChanged @4644 | FROM item_kits @4568 |
| <span id="m-db79e434a3b8"></span><code>MainViewModel.InitializeDemoData()</code><br>4647–4727 | Add @4653; Add @4672; Add @4685; Add @4689; Add @4694; Add @4700; ApplyActivityFilter @4706; Add @4709; ApplyInventoryFilter @4718; Add @4721; Parse @4721; NotifyTotalsChanged @4726 | No extracted literal effects. |
| <span id="m-f8f53230c7b9"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>4729–4742 | — | No extracted literal effects. |
| <span id="m-46fbd141b63a"></span><code>MainViewModel.SelectMenu(string)</code><br>4744–4815 | CheckSessionUnlocked @4746; NormalizeMenuKey @4750; LoadInvoicesAsync @4756; LoadCommercialAsync @4757; LoadActivityInvoicesAsync @4764; LoadTeamsStaffAsync @4767; LoadCatalogRegistryAsync @4768; UpdateDemoSeedingAvailabilityAsync @4771; UpdateReceiptDesignPreview @4774; RefreshDiagnosticsAsync @4775; LoadPriceLevelSettingsAsync @4776; LoadInventoryAsync @4779; LoadPriceProposalsAsync @4781; LoadReportDataAsync @4784; LoadFinancialRegisterAsync @4785; LoadCustomersAsync @4788; LoadSuppliersAsync @4789; LoadThirdPartiesAsync @4790; LoadManufacturingDataAsync @4795; LoadManagedUnitsAsync @4803; LoadManagedCategoriesAsync @4806; LoadSalaryWorkspaceAsync @4809; LoadExpensesWorkspaceAsync @4812 | No extracted literal effects. |
| <span id="m-38fc0b1dc363"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>4817–4836 | — | No extracted literal effects. |
| <span id="m-a4c85f7d1e9f"></span><code>MainViewModel.LogOut()</code><br>4838–4854 | ClearNotifications @4840; ResetCashReview @4844; RaisePropertyChanged @4846; nameof @4846; Lock @4847; RefreshUnlockCandidates @4852; UpdateDemoSeedingAvailabilityAsync @4853 | No extracted literal effects. |
| <span id="m-28322bdb7e1b"></span><code>MainViewModel.UnlockSession()</code><br>4856–4859 | UnlockSession @4858 | No extracted literal effects. |
| <span id="m-e9b7f157dd5d"></span><code>MainViewModel.UnlockSession(string?)</code><br>4861–4960 | IsLockScreenLockedOut @4869; IsNullOrWhiteSpace @4885; AuthenticateSelectedUser @4894; Lock @4899; AddSeconds @4905; AddMinutes @4922; Initialize @4941; Unlock @4942; Any @4946; Equals @4946; RaisePropertyChanged @4947; nameof @4947; LoadActivityInvoicesAsync @4951; LoadTrackOrdersAsync @4952; UpdateDemoSeedingAvailabilityAsync @4953; StartAutomaticDemoDatasetLoadAsync @4954 | No extracted literal effects. |
| <span id="m-0ca717b01ce6"></span><code>MainViewModel.PowerAction()</code><br>4962–4968 | CheckSessionUnlocked @4964 | No extracted literal effects. |
| <span id="m-df7e8c6beab1"></span><code>MainViewModel.CycleTable()</code><br>4970–4976 | CheckSessionUnlocked @4972 | No extracted literal effects. |
| <span id="m-5b60adce8ee8"></span><code>MainViewModel.CycleDiningType()</code><br>4978–4984 | CheckSessionUnlocked @4980 | No extracted literal effects. |
| <span id="m-73fc2af36ecb"></span><code>MainViewModel.CycleCustomer()</code><br>4986–4989 | OpenCustomerChooser @4988 | No extracted literal effects. |
| <span id="m-b34d4e1347d3"></span><code>MainViewModel.OpenPromoDialog()</code><br>4991–5006 | CheckSessionUnlocked @4993; IsNullOrWhiteSpace @5000; RaisePropertyChanged @5004; nameof @5004 | No extracted literal effects. |
| <span id="m-46b783af38cb"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5008–5077 | CheckSessionUnlocked @5010; ToLowerInvariant @5023; Trim @5023; IsNullOrWhiteSpace @5030; Trim @5030; ToList @5038; Select @5038; ToMinorUnits @5042; Equals @5058; Calculate @5062; NotifyTotalsChanged @5074; ConfigureAwait @5076; SaveDurableCartAsync @5076 | No extracted literal effects. |
| <span id="m-b40aad45fd16"></span><code>MainViewModel.TogglePromo()</code><br>5079–5096 | CheckSessionUnlocked @5081; RemovePromo @5090; OpenPromoDialog @5094 | No extracted literal effects. |
| <span id="m-c38819164f61"></span><code>MainViewModel.RemovePromo()</code><br>5098–5108 | NotifyTotalsChanged @5105; SaveDurableCartAsync @5107 | No extracted literal effects. |
| <span id="m-92764f5da31e"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5110–5121 | CheckSessionUnlocked @5112; NotifyTotalsChanged @5118; ConfigureAwait @5120; SaveDurableCartAsync @5120 | No extracted literal effects. |
| <span id="m-f76068f20af0"></span><code>MainViewModel.CancelPromoDialog()</code><br>5123–5127 | — | No extracted literal effects. |
| <span id="m-3c7159b235eb"></span><code>MainViewModel.RecalculateCart()</code><br>5129–5183 | ToMinorUnits @5145; Add @5146; Equals @5167; Calculate @5171; ToDictionary @5174; TryGetValue @5177 | No extracted literal effects. |
| <span id="m-9bfd8b7229a4"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5185–5192 | CheckSessionUnlocked @5187; ResetCashReview @5188 | No extracted literal effects. |
| <span id="m-fd6a1ee06215"></span><code>MainViewModel.SelectCategory(CategoryItem)</code><br>5194–5202 | CheckSessionUnlocked @5196; ApplyFilter @5200 | No extracted literal effects. |
| <span id="m-a350977da8c2"></span><code>MainViewModel.ApplyFilter()</code><br>5204–5226 | FirstOrDefault @5206; Clear @5209; AsEnumerable @5210; Where @5214; Equals @5214; IsNullOrWhiteSpace @5217; Contains @5219; Add @5224 | No extracted literal effects. |
| <span id="m-d43a5512c71d"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5228–5228 | AddToCart @5228 | No extracted literal effects. |
| <span id="m-2ed55554259d"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5230–5268 | CheckSessionUnlocked @5232; ResetCashReview @5233; ResolveProductSaleUnitFactor @5236; Round @5243; FirstOrDefault @5244; UpdateCartKitBreakdownAsync @5248; Add @5259; NotifyTotalsChanged @5262; SaveDurableCartAsync @5264; IsNullOrWhiteSpace @5266; ToString @5266; NewGuid @5266; RecordSuccessfulSearchUseAsync @5267; FromGuid @5267 | No extracted literal effects. |
| <span id="m-2efd35f0fb33"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5270–5278 | CheckSessionUnlocked @5272; ResetCashReview @5273; UpdateCartKitBreakdownAsync @5275; NotifyTotalsChanged @5276; SaveDurableCartAsync @5277 | No extracted literal effects. |
| <span id="m-7dae02b7a6ca"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5280–5295 | CheckSessionUnlocked @5282; ResetCashReview @5283; UpdateCartKitBreakdownAsync @5287; Remove @5291; NotifyTotalsChanged @5293; SaveDurableCartAsync @5294 | No extracted literal effects. |
| <span id="m-b4d3b0526f64"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5297–5303 | ConfigureAwait @5300; LoadAsync @5300; RefreshSavedPaymentImages @5301; CancelManualPaymentSettings @5302 | No extracted literal effects. |
| <span id="m-214375a2380f"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5305–5334 | ValidImage @5312; CreatePaymentBitmap @5317; Dispose @5320; RaisePropertyChanged @5332; nameof @5332 | No extracted literal effects. |
| <span id="m-db537d1f7876"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5336–5352 | Dispose @5346; CreatePaymentBitmap @5348; RaisePropertyChanged @5350; nameof @5350 | No extracted literal effects. |
| <span id="m-2d176046406a"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5354–5358 | — | No extracted literal effects. |
| <span id="m-9761697f453f"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5360–5368 | Dispose @5362; CreatePaymentBitmap @5364; RaisePropertyChanged @5366; nameof @5366 | No extracted literal effects. |
| <span id="m-4dbf71d5ab06"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5370–5389 | ConfigureAwait @5379; ExecuteAsync @5379; DispatchToUi @5382; SafePipelineError @5382; LoadAsync @5385; RefreshSavedPaymentImages @5386; CancelManualPaymentSettings @5387 | No extracted literal effects. |
| <span id="m-2c5abb7f2e44"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5391–5410 | IsNullOrWhiteSpace @5395; Trim @5396; ToMinorUnits @5402; ConfigureAwait @5408; PlaceOrderAsync @5408 | No extracted literal effects. |
| <span id="m-5b4b93177026"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5412–5612 | Localize @5416; ExecuteDemoPlaceOrder @5422; ConfigureAwait @5448; SaveDurableCartAsync @5448; ToMinorUnits @5456; Trim @5458; Equals @5469; Equals @5476; ResetCashReview @5478; Max @5536; Add @5541; ConfigureAwait(TakePaymentCommand, SalesInvoice) @5559; ExecuteAsync(TakePaymentCommand, SalesInvoice) @5559; Format @5571; ToDecimal @5571; DispatchToUi @5573; Clear @5576; NewGuid @5585; NotifyTotalsChanged @5586; LoadActivityInvoicesAsync @5593; OpenStaleCartPriceReviewAsync @5598; RequestElevationForCheckout @5600; SafePipelineError @5604; SafeError @5610 | No extracted literal effects. |
| <span id="m-4a88546f6a48"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>5614–5646 | DispatchToUi @5618; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5621; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5621; SafePipelineError @5626; ToArray @5630; Select @5630; Where @5630; FormatCartReviewMoney @5634; Clear @5641; Add @5642 | No extracted literal effects. |
| <span id="m-6684d2dfd7a8"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>5648–5653 | ScalingFactor @5650; Format @5652; Equals @5652 | No extracted literal effects. |
| <span id="m-dec65e8bde4e"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>5655–5686 | CheckSessionUnlocked @5657; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5659; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5659; DispatchToUi @5664; SafePipelineError @5664; ConfigureAwait @5665; OpenStaleCartPriceReviewAsync @5665; FirstOrDefault @5672; ScalingFactor @5675; ResetCashReview @5679; Clear @5682; NotifyTotalsChanged @5683 | No extracted literal effects. |
| <span id="m-9929995ddf98"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>5688–5695 | Clear @5692; ResetCashReview @5693 | No extracted literal effects. |
| <span id="m-b17b7b67b912"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>5697–5723 | CheckSessionUnlocked @5699; ResetCashReview @5706; ToMinorUnits @5717; ConfigureAwait @5722; PlaceOrderAsync @5722 | No extracted literal effects. |
| <span id="m-255cb2f77608"></span><code>MainViewModel.CancelCashReview()</code><br>5725–5729 | ResetCashReview @5727 | No extracted literal effects. |
| <span id="m-e0fcc04c24e7"></span><code>MainViewModel.ResetCashReview()</code><br>5731–5740 | — | No extracted literal effects. |
| <span id="m-7fa487a2cbce"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>5742–5761 | RaisePropertyChanged @5753; nameof @5753; Clear @5756; ResetCashReview @5757; NotifyTotalsChanged @5758 | No extracted literal effects. |
| <span id="m-0145efde6610"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>5763–5828 | ConfigureAwait @5767; WaitAsync @5767; ClearActiveCartAsync @5772; ToMinorUnits @5782; Add @5783; ToUpperInvariant @5786; ToString @5786; IsNullOrWhiteSpace @5789; SaveActiveCartAsync @5802; DispatchToUi @5821; SafeError @5821; Release @5826 | No extracted literal effects. |
| <span id="m-d49ba285ee7f"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>5830–5885 | ConfigureAwait @5836; GetActiveCartAsync @5836; Clear @5848; FirstOrDefault @5851; ToDecimal @5855; Add @5861; NotifyTotalsChanged @5878 | No extracted literal effects. |
| <span id="m-c3b08f4f5df4"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>5887–5964 | ApplyPagedResult @5891; ToList @5892; ApplyActivityFilter @5896; HasPermission @5901; ConfigureAwait @5908; GetPagedActivityInvoicesAsync @5908; ToPageRequest @5911; ToDecimal @5917; Add @5918; ToString @5923; ToLocalTime @5923; DispatchToUi @5942; Clear @5944; Add @5947; SafeError @5961 | No extracted literal effects. |
| <span id="m-599019b632a1"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>5966–6043 | HasPermission @5971; ConfigureAwait @5978; GetActiveOrdersAsync @5978; Clear @5979; ToDecimal @5983; Join @6017; Select @6017; Add @6019; ToString @6034; ToLocalTime @6034 | No extracted literal effects. |
| <span id="m-289ace692a85"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6045–6072 | CheckSessionUnlocked @6047; Clear @6050; ConfigureAwait @6056; GetOrderByIdAsync @6056; Add @6061; DispatchToUi @6067; SafeError @6067 | No extracted literal effects. |
| <span id="m-f6e0cea63ef8"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6074–6079 | Clear @6078 | No extracted literal effects. |
| <span id="m-9e4b000c7d28"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6081–6114 | CheckSessionUnlocked @6083; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6099; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6099; ConfigureAwait @6108; LoadTrackOrdersAsync @6108; DispatchToUi @6112; SafePipelineError @6112 | No extracted literal effects. |
| <span id="m-aea4424e1e6f"></span><code>MainViewModel.MarkReadyAsync()</code><br>6116–6149 | CheckSessionUnlocked @6118; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6134; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6134; ConfigureAwait @6143; LoadTrackOrdersAsync @6143; DispatchToUi @6147; SafePipelineError @6147 | No extracted literal effects. |
| <span id="m-b3bdd6c5bc47"></span><code>MainViewModel.MarkServedAsync()</code><br>6151–6184 | CheckSessionUnlocked @6153; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6169; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6169; ConfigureAwait @6178; LoadTrackOrdersAsync @6178; DispatchToUi @6182; SafePipelineError @6182 | No extracted literal effects. |
| <span id="m-138ebe9cbd0a"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6186–6214 | CheckSessionUnlocked @6188; Remove @6192; CloseOrderDetailsModal @6193; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6202; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6202; ConfigureAwait @6208; LoadTrackOrdersAsync @6208; DispatchToUi @6212; SafePipelineError @6212 | No extracted literal effects. |
| <span id="m-6780ec69b5c2"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6216–6312 | CheckSessionUnlocked @6218; CloseOrderDetailsModal @6224; ConfigureAwait @6231; GetOrderByIdAsync @6231; Zero @6253; NewGuid @6259; ToList @6262; Select @6262; ToUpperInvariant @6265; ToString @6265; SaveActiveCartAsync @6274; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6290; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6290; DispatchToUi @6293; SafePipelineError @6293; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6299; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6299; LoadTrackOrdersAsync @6305; LoadActivityInvoicesAsync @6306 | No extracted literal effects. |
| <span id="m-1c86438d6eff"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6314–6321 | CheckSessionUnlocked @6316 | No extracted literal effects. |
| <span id="m-0513957117e6"></span><code>MainViewModel.FilterActivity(string)</code><br>6340–6346 | CheckSessionUnlocked @6342; ApplyActivityFilter @6344 | No extracted literal effects. |
| <span id="m-c34958c0de43"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6348–6387 | Clear @6350; AsEnumerable @6351; Where @6356; IsNullOrWhiteSpace @6359; Trim @6361; Contains @6363; Contains @6364; Contains @6365; IsNullOrEmpty @6369; Equals @6371; ToList @6375; Add @6377; ApplyPagedResult @6381 | No extracted literal effects. |
| <span id="m-2ca637ed0510"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6389–6425 | CheckSessionUnlocked @6391; ConfigureAwait(QueueReceiptReprintCommand, string) @6411; ExecuteAsync(QueueReceiptReprintCommand, string) @6411; IsNullOrWhiteSpace @6412; ReportError @6414; RefreshOutputStatusAsync @6419; DispatchToUi @6423; SafeError @6423 | No extracted literal effects. |
| <span id="m-37a1815b4197"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6427–6470 | RefreshOutputPrinterQueues @6432; ReadAsync @6433; Equals @6440; IsNullOrWhiteSpace @6440; TryReadGeometry @6442; ComputeCapabilityFingerprint @6446; ConfigureAwait @6450; InvalidateThermalVerificationAsync @6450; LoadCashFinancialSettingsAsync @6462; LoadReceiptDesignAsync @6463; RefreshOutputStatusAsync @6464; DispatchToUi @6468; SafeError @6468 | No extracted literal effects. |
| <span id="m-d0f7d7102f57"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6472–6498 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6485; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6485; ReportError @6488; LoadOutputDevicesAsync @6491; DispatchToUi @6496; SafeError @6496 | No extracted literal effects. |
| <span id="m-ee55a6c1ed51"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6500–6573 | Equals @6514; IsNullOrWhiteSpace @6519; IsWindows @6524; TryReadGeometry @6529; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6546; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6546; ReportError @6549; Render @6552; ToString @6553; ConfigureAwait @6554; Run @6554; Send @6554; ComputeCapabilityFingerprint @6555; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @6556; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @6556; RefreshOutputStatusAsync @6567; DispatchToUi @6571; SafeError @6571 | No extracted literal effects. |
| <span id="m-129fec63dbc3"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>6575–6612 | IsWindows @6589; IsNullOrWhiteSpace @6589; TryReadGeometry @6591; ComputeCapabilityFingerprint @6595; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @6596; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @6596; ReportError @6600; ConfigureAwait @6606; RefreshOutputStatusAsync @6606; DispatchToUi @6610; SafeError @6610 | InvalidOperationException @6590; InvalidOperationException @6594 |
| <span id="m-5fd9bdc8fac1"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>6614–6651 | CreateCommand @6619; ConfigureAwait @6628; ExecuteReaderAsync @6628; ReadAsync @6629; GetInt32 @6632; GetString @6632; GetInt64 @6632; Parse @6633; RaisePropertyChanged @6635; nameof @6635; NotifyTotalsChanged @6644; DispatchToUi @6649; SafeError @6649 | FROM store_config @6620 |
| <span id="m-3485e6732802"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>6653–6681 | ConfigureAwait @6666; ExecuteAsync @6666; ReportError @6669; NotifyTotalsChanged @6674; DispatchToUi @6679; SafeError @6679 | No extracted literal effects. |
| <span id="m-d9b2c7e52a80"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>6683–6727 | DispatchToUi @6687; CreateCommand @6692; ConfigureAwait @6698; ExecuteReaderAsync @6698; ReadAsync @6699; Deserialize(ReceiptDesignDocument) @6701; GetString @6701; SafeError @6720 | FROM receipt_designs @6693; JOIN receipt_design_versions @6693 |
| <span id="m-cd4af98f4b32"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>6729–6756 | ConfigureAwait @6742; ExecuteAsync @6742; ReportError @6747; DispatchToUi @6754; SafeError @6754 | No extracted literal effects. |
| <span id="m-4add17d04fc9"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>6758–6770 | IsWindows @6760; Select @6761; Enumerate @6761; Empty(string) @6762; ToArray @6763; OrderBy @6763; Distinct @6763; Where @6763; Append @6763; IsNullOrWhiteSpace @6764; Clear @6768; Add @6769 | No extracted literal effects. |
| <span id="m-f01bcb1d7c2c"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>6772–6830 | CheckAccess @6774; DispatchToUi @6776; CreateSampleData @6782; Equals @6788; IsWindows @6795; TryReadGeometry @6796; BuildPaperDocument @6805; RenderPreviewPngPages @6808; SetReceiptDesignPreviewPages @6810; Localize @6812; BuildThermalLines @6817; RenderPreviewPng @6819; Empty(byte[]) @6826; ReportException @6828 | No extracted literal effects. |
| <span id="m-f314f77eca54"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>6832–6837 | ShowReceiptDesignPreviewPage @6836 | No extracted literal effects. |
| <span id="m-3f276f41dd2d"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>6839–6845 | ShowReceiptDesignPreviewPage @6844 | No extracted literal effects. |
| <span id="m-473362e43219"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>6847–6861 | RaisePropertyChanged @6858; nameof @6858 | No extracted literal effects. |
| <span id="m-ea5893e9abaa"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>6863–6892 | ReadAsync @6866; Localize @6869; CreateCommand @6871; ConfigureAwait @6873; ExecuteScalarAsync @6873; ToString @6873; IsNullOrWhiteSpace @6874; ExecuteReaderAsync @6888; ReadAsync @6889; Trim @6890; GetString @6890 | FROM hardware_jobs @6872; FROM hardware_jobs @6887 |
| <span id="m-b36ba3ada832"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>6894–6910 | Clear @6896; AsEnumerable @6897; Where @6900; IsNullOrWhiteSpace @6902; Contains @6904; Contains @6905; Contains @6906; Add @6909 | No extracted literal effects. |
| <span id="m-c8a65029f4af"></span><code>MainViewModel.GenerateXReport()</code><br>6912–6931 | CheckSessionUnlocked @6914; ToString @6918; GenerateXReportInternalAsync @6930 | No extracted literal effects. |
| <span id="m-d82ecb93c333"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>6933–6948 | ConfigureAwait @6937; LoadReportDataAsync @6937; DispatchToUi @6946; SafeError @6946 | No extracted literal effects. |
| <span id="m-19a0a433415d"></span><code>MainViewModel.CloseShiftZReport()</code><br>6950–6953 | OpenCloseShiftModal @6952 | No extracted literal effects. |
| <span id="m-fbcb7894ec4b"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>6955–6964 | CheckSessionUnlocked @6962 | No extracted literal effects. |
| <span id="m-e74e6a77c353"></span><code>MainViewModel.SaveSettings()</code><br>6966–6970 | CheckSessionUnlocked @6968 | No extracted literal effects. |
| <span id="m-baad21048b84"></span><code>MainViewModel.ApplySettingsAsync()</code><br>6972–7059 | CheckSessionUnlocked @6981; NotifyTotalsChanged @7000; ExecuteAsync @7028; DispatchToUi @7052; SafePipelineError @7052; SafeError @7057 | No extracted literal effects. |
| <span id="m-e7cf18a49c98"></span><code>MainViewModel.CancelSettings()</code><br>7061–7082 | CheckSessionUnlocked @7063; NotifyTotalsChanged @7075 | No extracted literal effects. |
| <span id="m-fd6a79e55b47"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7085–7115 | ProbeDatabaseAsync @7098; ProbeLicense @7104; RefreshOutputStatusAsync @7107; ProbeHardwareStubs @7108; DispatchToUi @7113; SafeError @7113 | No extracted literal effects. |
| <span id="m-3fac3c856f84"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7176–7214 | RaisePropertyChanged @7178; nameof @7178; FormatRealResetPreviewSummary @7213 | No extracted literal effects. |
| <span id="m-1cebd00f1210"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7216–7229 | Localize @7217; ToString @7219; GetValueOrDefault @7219; ToString @7224; ToString @7225; ToString @7226 | No extracted literal effects. |
| <span id="m-d7459a2295ee"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7338–7430 | Post @7342; ConfigureAwait @7349; GetWorkspaceEnvironmentAsync @7349; Equals @7350; GetDatasetStateAsync @7352; CreateCommand @7358; CreateParameter @7365; ToString @7367; Add @7368; ExecuteScalarAsync @7369; HasPermission @7374; ToInt64 @7379; ExecuteScalarAsync @7379; ExecuteScalarAsync @7383; ExecuteScalarAsync @7390; ExecuteScalarAsync @7396; Localize @7415 | FROM items @7378; FROM sales_invoices @7382; FROM third_parties @7395; FROM users @7359; JOIN user_roles @7359 · DYNAMIC SQL: inspect manually |
| <span id="m-73ab0d06deee"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>7432–7442 | CheckSessionUnlocked @7434; HasPermission @7435 | No extracted literal effects. |
| <span id="m-934ba03757a7"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>7444–7449 | ConfigureAwait @7448; ResetDatabaseAsync @7448 | No extracted literal effects. |
| <span id="m-116af35c389c"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>7451–7452 | ConfigureAwait @7452; EnsureDefaultDemoDatasetAsync @7452 | No extracted literal effects. |
| <span id="m-7148fd0d21c9"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>7454–7460 | EnsureDefaultDemoDatasetAsync @7458 | No extracted literal effects. |
| <span id="m-0614610de766"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>7462–7566 | Localize @7467; ConfigureAwait @7474; WaitAsync @7474; GetWorkspaceEnvironmentAsync @7477; Equals @7478; HasPermission @7485; Post @7499; LocalizeDemoSeedProgress @7501; EnsureInitialDatasetAsync @7507; Join @7531; Select @7531; ReloadCatalogAsync @7541; LoadInventoryAsync @7542; LoadThirdPartiesAsync @7543; LoadManufacturingDataAsync @7544; LoadSuppliersAsync @7545; UpdateDemoSeedingAvailabilityAsync @7546; ToUpperInvariant @7551; ToString @7551; NewGuid @7551; LogDiagnosticError @7552; ReportError @7557; Release @7564 | No extracted literal effects. |
| <span id="m-bff96a752d0f"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>7568–7582 | Localize @7570 | No extracted literal effects. |
| <span id="m-8ffbc5d7188c"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>7584–7681 | Localize @7588; ConfigureAwait @7592; WaitAsync @7592; HasPermission @7596; GetWorkspaceEnvironmentAsync @7603; Equals @7604; ResetDatabaseAsync @7612; GetStoreProfileAsync @7615; Post @7616; Clear @7619; Clear @7620; Clear @7621; NewGuid @7622; RaisePropertyChanged @7625; nameof @7625; Lock @7626; Defaults @7639; RefreshUnlockCandidates @7652; LoadCashFinancialSettingsAsync @7653; LoadOutputDevicesAsync @7654; LoadManualPaymentSettingsAsync @7655; LoadReceiptDesignAsync @7656; ReloadCatalogAsync @7657; LoadInventoryAsync @7658; LoadThirdPartiesAsync @7659; LoadManufacturingDataAsync @7660; LoadActivityInvoicesAsync @7661; UpdateDemoSeedingAvailabilityAsync @7662; ToUpperInvariant @7667; ToString @7667; LogDiagnosticError @7668; ReportError @7674; Release @7679 | No extracted literal effects. |
| <span id="m-379f07cf2cb3"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>7683–7725 | CheckSessionUnlocked @7685; HasPermission @7687; ConfigureAwait @7695; GetWorkspaceEnvironmentAsync @7695; Equals @7696; PreviewAsync @7699; FormatRealResetPreviewSummary @7700; Post @7701; RaisePropertyChanged @7718; nameof @7718; SafeError @7723 | UnauthorizedAccessException @7697 |
| <span id="m-8295f7e367f2"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>7727–7813 | HasPermission @7730; ConfigureAwait @7748; ExecuteAsync @7748; GetStoreProfileAsync @7757; Post @7760; Clear @7764; Clear @7765; Clear @7766; Clear @7767; NewGuid @7768; Lock @7771; RaisePropertyChanged @7785; nameof @7785; LoadCashFinancialSettingsAsync @7786; LoadOutputDevicesAsync @7787; LoadManualPaymentSettingsAsync @7788; LoadReceiptDesignAsync @7789; RefreshUnlockCandidates @7797; LoadInventoryAsync @7798; LoadActivityInvoicesAsync @7799; UpdateDemoSeedingAvailabilityAsync @7800; ToUpperInvariant @7805; ToString @7805; LogDiagnosticError @7806 | No extracted literal effects. |
| <span id="m-5df58f3e26b0"></span><code>MainViewModel.CancelRealShopReset()</code><br>7815–7822 | RaisePropertyChanged @7821; nameof @7821 | No extracted literal effects. |
| <span id="m-bb710488e1c0"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>7826–7843 | ConfigureAwait @7828; ExportDocumentAsync @7828; Post @7832; GetFileName @7836 | No extracted literal effects. |
| <span id="m-367c86755084"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>7845–7867 | Exists @7850; CreateDirectory @7852; Start @7854; ToUpperInvariant @7863; ToString @7863; NewGuid @7863; LogDiagnosticError @7864 | No extracted literal effects. |
| <span id="m-16427818279d"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>7869–7879 | CheckSessionUnlocked @7871; RaisePropertyChanged @7873; nameof @7873; Localize @7875; ToString @7876 | No extracted literal effects. |
| <span id="m-bf752bc0f8d5"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>7886–7902 | CheckSessionUnlocked @7888; HasPermission @7889; RaisePropertyChanged @7895; nameof @7895; Localize @7898; ToString @7899 | No extracted literal effects. |
| <span id="m-111ddc464e42"></span><code>MainViewModel.CommitNumpad()</code><br>7904–7951 | CheckSessionUnlocked @7906; TryParse @7912; IsNullOrWhiteSpace @7914; Trim @7920; NotifyTotalsChanged @7930; SaveDurableCartAsync @7931; TryParse @7933; UpdateCartKitBreakdownAsync @7936; Remove @7942; RaisePropertyChanged @7950; nameof @7950 | No extracted literal effects. |
| <span id="m-07949fa33f6b"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>7957–7975 | CheckSessionUnlocked @7965 | No extracted literal effects. |
| <span id="m-6606d0d71c23"></span><code>MainViewModel.StageBusinessProfile()</code><br>7982–8012 | CheckSessionUnlocked @7984; HasPermission @7988 | No extracted literal effects. |
| <span id="m-7ff66beb3f34"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8014–8023 | — | No extracted literal effects. |
| <span id="m-73bcb29b5a77"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8025–8048 | RecalculateCart @8027; RaisePropertyChanged @8029; nameof @8029 | No extracted literal effects. |
| <span id="m-e0c87f41a5cc"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8050–8137 | IsNullOrWhiteSpace @8053; Trim @8053; All @8063; Trim @8080; Trim @8081; NewGuid @8085; ToString @8090; ConfigureAwait @8094; BeginTransactionAsync @8094; HandleAsync @8095; AppendAsync @8100; ToString @8101; Serialize @8106; CommitAsync @8109; Initialize @8115; Unlock @8116; RaisePropertyChanged @8121; nameof @8121; LoadTeamsStaffAsync @8124; StartAutomaticDemoDatasetLoadAsync @8125; RollbackAsync @8129; DispatchToUi @8130; SafePipelineError @8130; SafeError @8135 | No extracted literal effects. |
| <span id="m-dac70d95c7e8"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8139–8146 | IsNullOrWhiteSpace @8141; ConfigureAwait @8145; SaveTeamMemberAsync @8145 | No extracted literal effects. |
| <span id="m-9060e872064c"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8148–8166 | CheckSessionUnlocked @8151; HasPermission @8153 | No extracted literal effects. |
| <span id="m-7123898b2db6"></span><code>MainViewModel.CancelChangePin()</code><br>8168–8175 | — | No extracted literal effects. |
| <span id="m-5557829035aa"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8177–8253 | Trim @8185; IsNullOrWhiteSpace @8188; All @8194; Equals @8207; Equals @8208; SetQuickPin @8220; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8233; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8233; ConfigureAwait @8241; LoadTeamsStaffAsync @8241; DispatchToUi @8246; SafePipelineError @8246; SafeError @8251 | No extracted literal effects. |
| <span id="m-dc2bac19dc54"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8255–8329 | HasPermission @8261; ConfigureAwait @8270; ResolveEffectivePermissionsAsync @8270; Contains @8303; Contains @8304; Add @8306; Contains @8312; DispatchToUi @8318; Clear @8320; Add @8321; SafeError @8327 | No extracted literal effects. |
| <span id="m-79e132ccb50b"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8331–8373 | OnTeamMemberFieldChanged @8337; ConfigureAwait @8354; ExecuteAsync @8354; DispatchToUi @8358; SafePipelineError @8366; SafeError @8371 | No extracted literal effects. |
| <span id="m-1d9d34eab511"></span><code>MainViewModel.ClosePermissionEditor()</code><br>8375–8380 | — | No extracted literal effects. |
| <span id="m-e44e33b729bd"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>8382–8396 | — | No extracted literal effects. |
| <span id="m-465853b2e494"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>8400–8400 | — | No extracted literal effects. |
| <span id="m-4cac2dacac81"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>8401–8401 | — | No extracted literal effects. |
| <span id="m-1fb870b0b8c0"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>8402–8402 | FromResult @8402 | No extracted literal effects. |
| <span id="m-a45621e6cd91"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>8405–8490 | HasPermission @8414; FromDecimal @8429; ConfigureAwait(OpenShiftCommand, Shift) @8433; ExecuteAsync(OpenShiftCommand, Shift) @8433; SetActiveCashier @8448; RefreshUnlockCandidates @8449; ToUpperInvariant @8466; ToString @8466; ToString @8468; ConfigureAwait @8478; LoadTeamsStaffAsync @8478; LoadTrackOrdersAsync @8479; DispatchToUi @8483; SafePipelineError @8483; SafeError @8488 | No extracted literal effects. |
| <span id="m-dedfa3deb0ed"></span><code>MainViewModel.LoadInventoryAsync()</code><br>8492–8629 | ApplyPagedResult @8496; ToList @8497; ApplyInventoryFilter @8501; Clear @8509; Empty(InventoryItem) @8511; ConfigureAwait @8516; GetPagedInventoryItemsAsync @8516; ToPageRequest @8521; CreateCommand @8534; ExecuteReaderAsync @8536; ReadAsync @8537; Add @8539; Parse @8539; GetString @8539; Add @8547; Contains @8556; ToDecimal @8559; Localize @8567; ToLocalTime @8573; BuildCostSourcesTooltip @8575; DispatchToUi @8602; Add @8605; SafeError @8627 | FROM item_kits @8535 |
| <span id="m-56dbf857823c"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>8631–8687 | CheckSessionUnlocked @8633; FirstOrDefault @8634; Clear @8645; Add @8647; CreateCommand @8652; CreateParameter @8663; Add @8666; ExecuteReader @8667; Read @8668; GetString @8670; Contains @8671; FirstOrDefault @8683; ResetReceiveLines @8684; UpdateReceiveKitBreakdownAsync @8685 | FROM uoms @8653; JOIN uoms @8653 |
| <span id="m-95e29c5ad938"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>8689–8790 | IsNullOrWhiteSpace @8702; Localize @8719; HasPermission @8723; BuildReceiptLines @8729; Sum @8746; Trim @8756; ToMinorUnits @8761; ConfigureAwait(ReceiveStockCommand, StockMovement) @8766; ExecuteAsync(ReceiveStockCommand, StockMovement) @8766; Clear @8776; ConfigureAwait @8778; LoadInventoryAsync @8778; LoadItemHistoryAsync @8779; DispatchToUi @8783; SafePipelineError @8783; SafeError @8788 | No extracted literal effects. |
| <span id="m-a641f33e6f0c"></span><code>MainViewModel.ResetReceiveLines()</code><br>8796–8813 | Clear @8798; Add @8802; RaisePropertyChanged @8808; nameof @8808; Invoke @8811 | No extracted literal effects. |
| <span id="m-119a8e8862bd"></span><code>MainViewModel.AddReceiveLine()</code><br>8816–8839 | IsNullOrWhiteSpace @8823; Add @8829; RaisePropertyChanged @8834; nameof @8834; Invoke @8837 | No extracted literal effects. |
| <span id="m-d31fe345ae99"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>8842–8859 | Remove @8849; Add @8852; RaisePropertyChanged @8858; nameof @8858 | No extracted literal effects. |
| <span id="m-b2da91d13362"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>8865–8886 | IsNullOrWhiteSpace @8867; LastOrDefault @8872; Add @8876; Trim @8879; ReferenceEquals @8880; RaisePropertyChanged @8884; nameof @8884; Invoke @8885 | No extracted literal effects. |
| <span id="m-7a45b1c8f3a0"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>8889–8966 | Add @8901; IsNullOrWhiteSpace @8909; Trim @8913; FirstOrDefault @8922; GroupBy @8922; Count @8924; Trim @8951 | No extracted literal effects. |
| <span id="m-a6eb403c21dd"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>8968–9004 | CreateCommand @8973; ConfigureAwait @8980; ExecuteReaderAsync @8980; Clear @8981; ReadAsync @8982; Add @8984; ParseGuidSafe @8985; GetString @8985; IsDBNull @8989; GetInt32 @8993; Parse @8995; DispatchToUi @9002; SafeError @9002 | FROM third_parties @8974 |
| <span id="m-8604a9299321"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9006–9024 | CheckSessionUnlocked @9008; FirstOrDefault @9014 | No extracted literal effects. |
| <span id="m-9837c3554776"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9026–9117 | IsNullOrWhiteSpace @9049; HasPermission @9060; Trim @9078; Trim @9080; ConfigureAwait(AdjustStockCommand, StockMovement) @9084; ExecuteAsync(AdjustStockCommand, StockMovement) @9084; ConfigureAwait @9100; LoadInventoryAsync @9100; LoadItemHistoryAsync @9101; OpenWasteExpenseConfirmation @9105; DispatchToUi @9110; SafePipelineError @9110; SafeError @9115 | No extracted literal effects. |
| <span id="m-5879649b49ed"></span><code>MainViewModel.OpenAddProduct()</code><br>9119–9187 | ResetProductStockDraft @9121; CheckSessionUnlocked @9122; HasPermission @9123; RaisePropertyChanged @9131; nameof @9131; ClearItemHistory @9133; LoadCatalogRegistryAsync @9140; InitializeProductPricingDraft @9143; Clear @9158; Clear @9159; Where @9160; Add @9162; FirstOrDefault @9164; Clear @9175; CaptureProductModalBaselineAsync @9186 | No extracted literal effects. |
| <span id="m-c9d411716aab"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9189–9189 | OpenEditProduct @9189 | No extracted literal effects. |
| <span id="m-672c370ac1ec"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9191–9271 | ResetProductStockDraft @9193; CheckSessionUnlocked @9195; HasPermission @9196; RaisePropertyChanged @9204; nameof @9204; ClearItemHistory @9206; LoadCatalogRegistryAsync @9214; InitializeProductPricingDraft @9220; ToMinorUnits @9221; LoadExactProductCostSnapshotsAsync @9227; ToDecimal @9231; Clear @9238; Clear @9239; Where @9240; Add @9242; FirstOrDefault @9244; LoadItemLocationEligibilitiesAsync @9263; LoadProductKitAsync @9264; LoadPrimaryBarcodeAsync @9265; LoadProductPricingDraftAsync @9266; LoadItemHistoryAsync @9267; LoadItemPriceHistoryAsync @9268; CaptureProductModalBaselineAsync @9270 | No extracted literal effects. |
| <span id="m-55d1627e1cc1"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>9273–9286 | OrderBy @9276; Where @9276; Add @9278 | No extracted literal effects. |
| <span id="m-1d8bc96d1b00"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>9288–9361 | CreateCommand @9295; CreateParameter @9302; ToString @9304; Add @9305; ConfigureAwait @9306; ExecuteReaderAsync @9306; ReadAsync @9307; GetInt32 @9309; IsDBNull @9310; GetString @9310; ParseStoredPricingPercentForDisplay @9311; ToDisplayAmount @9315; GetInt64 @9315; OrderBy @9335; Where @9335; TryGetValue @9338; Add @9344; InvokeAsync @9346; RaisePropertyChanged @9351; nameof @9351; CaptureProductPricingSnapshot @9354; DispatchToUi @9359; SafeError @9359 | FROM item_price_levels @9326; FROM item_pricing @9297 |
| <span id="m-f7ed9cc7b639"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>9363–9398 | CreateCommand @9370; CreateParameter @9376; ToString @9378; Add @9379; ConfigureAwait @9380; ExecuteReaderAsync @9380; ReadAsync @9381; Parse @9384; GetString @9384; GetInt32 @9384; GetInt64 @9385; IsDBNull @9385; Parse @9386; InvokeAsync @9388; DispatchToUi @9396; SafeError @9396 | FROM product_category_pricing_rules @9371 |
| <span id="m-a66c6904bae0"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>9400–9429 | ConfigureAwait @9404; WhenAll @9404; InvokeAsync @9405; CaptureProductModalSnapshot @9409; CaptureProductPricingSnapshot @9410; RaisePropertyChanged @9411; nameof @9411 | No extracted literal effects. |
| <span id="m-0f5ac3d04375"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>9431–9479 | Serialize @9431; ToArray @9454; Select @9454; Select @9471; OrderBy @9471; OrderBy @9475 | No extracted literal effects. |
| <span id="m-f22ffbf97273"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>9481–9493 | Serialize @9481; ToArray @9492; Select @9492 | No extracted literal effects. |
| <span id="m-92dbe013ddcd"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9495–9527 | nameof @9497; RaisePropertyChanged @9498; RaiseTraceabilityState @9503; StartsWith @9507; RecomputeProductPricingPreview @9518; RefreshVirtualKitAvailability @9520 | No extracted literal effects. |
| <span id="m-5bfbf12bab96"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>9529–9543 | RaisePropertyChanged @9537; nameof @9537; RecomputeProductPricingPreview @9540; RefreshVirtualKitAvailability @9541 | No extracted literal effects. |
| <span id="m-212936e4c4ad"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9545–9553 | RaisePropertyChanged @9547; nameof @9547; RecomputeProductPricingPreview @9550; RefreshVirtualKitAvailability @9551 | No extracted literal effects. |
| <span id="m-2eddf69698c3"></span><code>MainViewModel.RequestCloseProductModal()</code><br>9555–9568 | DiscardProductModal @9567 | No extracted literal effects. |
| <span id="m-701c4fa733a9"></span><code>MainViewModel.DiscardProductModal()</code><br>9570–9579 | RaisePropertyChanged @9575; nameof @9575; ClearItemHistory @9577 | No extracted literal effects. |
| <span id="m-d9f14b96a54a"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>9581–9599 | CreateCommand @9586; CreateParameter @9588; ToString @9590; Add @9591; ConfigureAwait @9592; ExecuteScalarAsync @9592; DispatchToUi @9595; ToString @9595 | FROM barcodes @9587 |
| <span id="m-ed4519173c82"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>9601–9652 | CreateCommand @9606; CreateParameter @9613; ToString @9615; Add @9616; ConfigureAwait @9620; ExecuteReaderAsync @9620; ReadAsync @9621; IsDBNull @9624; GetString @9624; GetDouble @9625; ResolveQuantity @9626; Add @9627; Parse @9629; DispatchToUi @9637; Clear @9640; Add @9641; RaisePropertyChanged @9644; nameof @9644; RecomputeProductPricingPreview @9647; RefreshVirtualKitAvailability @9648 | FROM item_kits @9607; JOIN item_kit_components @9607; JOIN items @9607 |
| <span id="m-ee46968690cd"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>9654–9654 | SaveProductConfigurationAsync @9654 | No extracted literal effects. |
| <span id="m-0c3c90f0bc79"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>9656–9861 | ConfigureAwait @9661; LoadCatalogRegistryAsync @9661; HasPermission @9663; IsNullOrWhiteSpace @9668; Localize @9690; Equals @9700; ToMinorUnits @9745; GetValueOrDefault @9757; Trim @9758; Trim @9759; Trim @9760; Trim @9767; Trim @9769; ToList @9814; Select @9814; CaptureProductPricingSnapshot @9818; ToCommand @9820; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @9828; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @9828; DispatchToUi @9831; RaiseTraceabilityState @9837; CaptureProductModalSnapshot @9839; RaisePropertyChanged @9841; nameof @9841; ReloadCatalogAsync @9848; LoadInventoryAsync @9849; LoadItemHistoryAsync @9850; SafePipelineError @9854; SafeError @9859 | No extracted literal effects. |
| <span id="m-191d462dfb1f"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>9863–9899 | CheckSessionUnlocked @9865; HasPermission @9866; ConfigureAwait(DeactivateProductCommand, bool) @9882; ExecuteAsync(DeactivateProductCommand, bool) @9882; ConfigureAwait @9887; ReloadCatalogAsync @9887; LoadInventoryAsync @9888; DispatchToUi @9892; SafePipelineError @9892; SafeError @9897 | No extracted literal effects. |
| <span id="m-a3437b4e1267"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>9901–9960 | ConfigureAwait @9907; GetActiveItemsAsync @9907; Clear @9909; Clear @9910; Clear @9911; CreateCommand @9916; ExecuteReaderAsync @9918; ReadAsync @9919; TryParse @9921; GetString @9921; Add @9922; Add @9929; GroupBy @9930; Count @9932; Contains @9937; Add @9950; Add @9951; ApplyFilter @9954 | FROM item_kits @9917 |
| <span id="m-1bef813e8400"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>9962–9968 | IsNullOrWhiteSpace @9964; TryParse @9965; HashData @9966; GetBytes @9966; AsSpan @9967 | No extracted literal effects. |
| <span id="m-00876f853e47"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>9970–10036 | CreateCommand @9976; ConfigureAwait @9979; ExecuteReaderAsync @9979; ReadAsync @9981; Add @9983; GetString @9985; GetInt32 @9989; Clear @9995; Add @9996; ExecuteReaderAsync @10008; ReadAsync @10010; Add @10012; GetString @10014; IsDBNull @10018; GetInt32 @10022; Clear @10028; Add @10029; DispatchToUi @10034; SafeError @10034 | FROM bins @10001; FROM facilities @9978; JOIN facilities @10001 |
| <span id="m-f0bb93f41e55"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>10251–10355 | CreateCommand @10261; ConfigureAwait @10268; ExecuteReaderAsync @10268; ReadAsync @10269; Add @10271; ParseGuidSafe @10273; GetString @10273; IsDBNull @10276; GetInt32 @10277; Add @10297; DispatchToUi @10312; Clear @10314; Clear @10315; Clear @10316; Equals @10320; Add @10321; Add @10323; Add @10325; Clear @10327; Add @10328; FirstOrDefault @10331; Equals @10331; FirstOrDefault @10336; FirstOrDefault @10343; ApplySaleUnitDefaultsToCatalog @10348; SafeError @10353 | FROM product_categories @10263; FROM uoms @10289 |
| <span id="m-c608fa665d8c"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>10357–10371 | ResolveProductSaleUnitFactor @10361; Round @10367; ApplyFilter @10370 | No extracted literal effects. |
| <span id="m-74e224fa1bc3"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>10373–10391 | FirstOrDefault @10375; Equals @10376; TryParse @10383 | No extracted literal effects. |
| <span id="m-fb49340faec9"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>10393–10415 | CheckSessionUnlocked @10395; HasPermission @10396; ConfigureAwait @10411; LoadManagedCategoriesAsync @10411; CaptureCategoryFormSnapshot @10413; RaisePropertyChanged @10414; nameof @10414 | No extracted literal effects. |
| <span id="m-6c99c18737ce"></span><code>MainViewModel.CloseCategoryManager()</code><br>10417–10426 | — | No extracted literal effects. |
| <span id="m-0291ebaaa403"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>10428–10450 | CheckSessionUnlocked @10430; HasPermission @10431; ConfigureAwait @10446; LoadManagedUnitsAsync @10446; CaptureUnitFormSnapshot @10448; RaisePropertyChanged @10449; nameof @10449 | No extracted literal effects. |
| <span id="m-17a4e721d552"></span><code>MainViewModel.CloseUnitManager()</code><br>10452–10461 | — | No extracted literal effects. |
| <span id="m-d507a414102e"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>10463–10526 | Clear @10466; Clear @10467; Clear @10468; CreateCommand @10469; ConfigureAwait @10475; ExecuteReaderAsync @10475; ReadAsync @10476; Add @10478; ParseGuidSafe @10480; GetString @10480; IsDBNull @10483; GetInt32 @10484; Where @10492; Equals @10492; Add @10493; TryParse @10506; Add @10507; RefreshTargetedCategoryCollections @10520; DispatchToUi @10521; RefreshManagedCategoriesTable @10523; RefreshManagedExpenseCategoriesTable @10524 | FROM expense_categories @10497; FROM product_categories @10471; JOIN expense_records @10497 |
| <span id="m-f61cea6e6e9d"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>10528–10535 | OpenCategoryManagerAsync @10530; FirstOrDefault @10531; EditManagedCategory @10534 | No extracted literal effects. |
| <span id="m-d918fe852315"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>10537–10545 | OpenCategoryManagerAsync @10540; FirstOrDefault @10541; EditManagedExpenseCategory @10544 | No extracted literal effects. |
| <span id="m-e53d9cc71d8d"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>10547–10566 | DispatchToUi @10549; Clear @10551; Clear @10552; Clear @10553; Where @10555; Equals @10558; Add @10559; Add @10561; Add @10563 | No extracted literal effects. |
| <span id="m-8422456eb708"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>10568–10580 | CaptureCategoryFormSnapshot @10578; RaisePropertyChanged @10579; nameof @10579 | No extracted literal effects. |
| <span id="m-04250dd4f285"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>10582–10595 | CaptureCategoryFormSnapshot @10593; RaisePropertyChanged @10594; nameof @10594 | No extracted literal effects. |
| <span id="m-d26c88b5606f"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>10597–10607 | Serialize @10597 | No extracted literal effects. |
| <span id="m-a9b47ccd8092"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>10609–10619 | Serialize @10609 | No extracted literal effects. |
| <span id="m-6e168ab54fc8"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>10621–10621 | — | No extracted literal effects. |
| <span id="m-97b1a950399d"></span><code>MainViewModel.DiscardRegistryForm()</code><br>10623–10639 | Equals @10626; RaisePropertyChanged @10630; nameof @10630 | No extracted literal effects. |
| <span id="m-6c1ac431b294"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>10641–10768 | Equals @10652; HasPermission @10654; FirstOrDefault @10663; Trim @10668; Trim @10669; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @10671; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @10671; DispatchToUi @10674; SafePipelineError @10674; IsNullOrWhiteSpace @10682; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @10684; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @10684; ConfigureAwait @10693; LoadManagedCategoriesAsync @10693; LoadExpenseCategoriesAsync @10694; CaptureCategoryFormSnapshot @10704; RaisePropertyChanged @10705; nameof @10705; Trim @10723; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @10725; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @10725; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @10741; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @10741; LoadCatalogRegistryAsync @10750; ReloadCatalogAsync @10751; SafeError @10766 | No extracted literal effects. |
| <span id="m-f9c04fe2098f"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>10770–10815 | HasPermission @10780; ConfigureAwait(DeactivateCategoryCommand, bool) @10793; ExecuteAsync(DeactivateCategoryCommand, bool) @10793; ConfigureAwait(ReactivateCategoryCommand, bool) @10798; ExecuteAsync(ReactivateCategoryCommand, bool) @10798; DispatchToUi @10803; SafePipelineError @10803; ConfigureAwait @10807; LoadManagedCategoriesAsync @10807; LoadCatalogRegistryAsync @10808; ReloadCatalogAsync @10809; SafeError @10813 | No extracted literal effects. |
| <span id="m-dffd50671013"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>10817–10857 | HasPermission @10827; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @10843; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @10843; DispatchToUi @10846; SafePipelineError @10846; ConfigureAwait @10850; LoadManagedCategoriesAsync @10850; LoadExpenseCategoriesAsync @10851; SafeError @10855 | No extracted literal effects. |
| <span id="m-63fd6df84bf1"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>10859–10959 | Clear @10862; CreateCommand @10865; ConfigureAwait @10871; ExecuteReaderAsync @10871; ReadAsync @10872; Add @10874; GetString @10876; IsDBNull @10878; GetInt32 @10882; IsNullOrWhiteSpace @10893; Equals @10897; Add @10904; Clear @10908; ExecuteReaderAsync @10913; ReadAsync @10914; GetString @10916; Where @10938; Add @10940; TryGetValue @10943; FirstOrDefault @10950; Add @10954; DispatchToUi @10957; UpdateConversionPreview @10958 | FROM store_uom_preferences @10912; FROM uoms @10867 |
| <span id="m-2525e24a5047"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>10961–10968 | OpenUnitManagerAsync @10963; FirstOrDefault @10964; Equals @10964; EditManagedUnit @10967 | No extracted literal effects. |
| <span id="m-9d058c7a1850"></span><code>MainViewModel.UpdateConversionPreview()</code><br>10970–11006 | IsNullOrWhiteSpace @10972; FirstOrDefault @10978; Equals @10978; TryParse @10993 | No extracted literal effects. |
| <span id="m-5e4fba0b9221"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11008–11029 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11015; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11015; DispatchToUi @11018; SafePipelineError @11022; SafeError @11027 | No extracted literal effects. |
| <span id="m-b79fb6d55f96"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11031–11044 | IsNullOrWhiteSpace @11037; TryParse @11040; CaptureUnitFormSnapshot @11042; RaisePropertyChanged @11043; nameof @11043 | No extracted literal effects. |
| <span id="m-880a5aebdff1"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>11046–11108 | IsNullOrWhiteSpace @11058; Trim @11062; Trim @11063; Trim @11066; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @11067; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @11067; DispatchToUi @11070; SafePipelineError @11070; Trim @11077; Equals @11080; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @11085; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @11085; ConfigureAwait @11093; LoadManagedUnitsAsync @11093; LoadCatalogRegistryAsync @11094; CaptureUnitFormSnapshot @11101; RaisePropertyChanged @11102; nameof @11102; SafeError @11106 | No extracted literal effects. |
| <span id="m-f1eb4952531e"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>11110–11148 | ConfigureAwait(DeactivateUomCommand, bool) @11127; ExecuteAsync(DeactivateUomCommand, bool) @11127; ConfigureAwait(ReactivateUomCommand, bool) @11132; ExecuteAsync(ReactivateUomCommand, bool) @11132; DispatchToUi @11137; SafePipelineError @11137; ConfigureAwait @11141; LoadManagedUnitsAsync @11141; LoadCatalogRegistryAsync @11142; SafeError @11146 | No extracted literal effects. |
| <span id="m-5558644dac20"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>11150–11188 | CreateCommand @11155; CreateParameter @11162; ToString @11164; Add @11165; ConfigureAwait @11167; ExecuteReaderAsync @11167; Clear @11168; ReadAsync @11169; Add @11171; ParseGuidSafe @11173; GetString @11173; GetInt32 @11176; IsDBNull @11178; ToDecimal @11178; GetDouble @11178; DispatchToUi @11186; SafeError @11186 | FROM item_locations @11156 |
| <span id="m-0fde4214c8d1"></span><code>MainViewModel.OpenLocationsModal()</code><br>11191–11217 | CheckSessionUnlocked @11193; HasPermission @11194; LoadFacilitiesAndBinsAsync @11215 | No extracted literal effects. |
| <span id="m-e978c4f5910d"></span><code>MainViewModel.OpenAddFacility()</code><br>11219–11227 | — | No extracted literal effects. |
| <span id="m-d2a15029000d"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>11229–11238 | — | No extracted literal effects. |
| <span id="m-f535b154ee27"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>11240–11299 | HasPermission @11243; IsNullOrWhiteSpace @11248; IsNullOrEmpty @11264; Trim @11266; Trim @11266; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @11267; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @11267; OpenAddFacility @11271; ConfigureAwait @11272; LoadFacilitiesAndBinsAsync @11272; DispatchToUi @11276; SafePipelineError @11276; ConfigureAwait(CreateFacilityCommand, FacilityDto) @11282; ExecuteAsync(CreateFacilityCommand, FacilityDto) @11282; SafeError @11297 | No extracted literal effects. |
| <span id="m-979466f3c07e"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>11301–11332 | HasPermission @11304; ConfigureAwait(DeactivateFacilityCommand, bool) @11316; ExecuteAsync(DeactivateFacilityCommand, bool) @11316; OpenAddFacility @11320; ConfigureAwait @11321; LoadFacilitiesAndBinsAsync @11321; DispatchToUi @11325; SafePipelineError @11325; SafeError @11330 | No extracted literal effects. |
| <span id="m-5e1a28c6aa14"></span><code>MainViewModel.OpenAddBin()</code><br>11334–11345 | FirstOrDefault @11344 | No extracted literal effects. |
| <span id="m-f77dfead6d06"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>11347–11359 | FirstOrDefault @11357 | No extracted literal effects. |
| <span id="m-8ba20b790f04"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>11361–11436 | HasPermission @11364; IsNullOrWhiteSpace @11374; IsNullOrEmpty @11385; Trim @11390; Trim @11391; Trim @11392; Trim @11393; Trim @11394; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @11397; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @11397; OpenAddBin @11401; ConfigureAwait @11402; LoadFacilitiesAndBinsAsync @11402; DispatchToUi @11406; SafePipelineError @11406; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @11419; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @11419; SafeError @11434 | No extracted literal effects. |
| <span id="m-ccf3c5435d5b"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>11438–11469 | HasPermission @11441; ConfigureAwait(DeactivateLocationBinCommand, bool) @11453; ExecuteAsync(DeactivateLocationBinCommand, bool) @11453; OpenAddBin @11457; ConfigureAwait @11458; LoadFacilitiesAndBinsAsync @11458; DispatchToUi @11462; SafePipelineError @11462; SafeError @11467 | No extracted literal effects. |
| <span id="m-dd81257aeee5"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>11471–11524 | HasPermission @11479; IsNullOrWhiteSpace @11484; Trim @11496; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @11504; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @11504; ConfigureAwait @11512; LoadItemLocationEligibilitiesAsync @11512; DispatchToUi @11517; SafePipelineError @11517; SafeError @11522 | No extracted literal effects. |
| <span id="m-ab2fba0f27f8"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>11526–11556 | HasPermission @11529; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @11541; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @11541; ConfigureAwait @11544; LoadItemLocationEligibilitiesAsync @11544; DispatchToUi @11549; SafePipelineError @11549; SafeError @11554 | No extracted literal effects. |
| <span id="m-28c461dd65ca"></span><code>MainViewModel.LoadCustomersAsync()</code><br>11559–11592 | NewGuid @11567; Clear @11573; Add @11574; FilterCustomers @11576; ConfigureAwait @11583; GetCustomersAsync @11583; DispatchToUi @11590; SafeError @11590 | No extracted literal effects. |
| <span id="m-31af7e3ba611"></span><code>MainViewModel.FilterCustomers()</code><br>11594–11607 | Clear @11596; Trim @11597; IsNullOrWhiteSpace @11598; Where @11600; Contains @11600; Contains @11601; Contains @11602; Add @11605 | No extracted literal effects. |
| <span id="m-11a35fdac3df"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>11609–11645 | CheckSessionUnlocked @11611; CreateCommand @11620; CreateParameter @11623; ToString @11625; Add @11626; ConfigureAwait @11627; ExecuteScalarAsync @11627; ToString @11628; Equals @11631; LoadPickerCandidatesAsync @11643; DispatchToUi @11644 | FROM items @11622 |
| <span id="m-303860ca4581"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>11647–11708 | ConfigureAwait @11654; GetLotCandidatesAsync @11654; DispatchToUi @11657; Clear @11659; Add @11662; ToString @11671; GetSerialCandidatesAsync @11679; Clear @11684; Add @11687; ToString @11696 | No extracted literal effects. |
| <span id="m-0904cc540adb"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>11710–11716 | Clear @11713; Clear @11714 | No extracted literal effects. |
| <span id="m-26f68d7b9cb3"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>11718–11777 | FirstOrDefault @11731; ConfigureAwait(SelectLotForCartLineCommand, bool) @11739; ExecuteAsync(SelectLotForCartLineCommand, bool) @11739; DispatchToUi @11742; SafePipelineError @11742; ToList @11748; Where @11748; ConfigureAwait(SelectSerialForCartLineCommand, bool) @11758; ExecuteAsync(SelectSerialForCartLineCommand, bool) @11758; SafeError @11775 | No extracted literal effects. |
| <span id="m-e74636e54bda"></span><code>MainViewModel.OpenCustomerChooser()</code><br>11779–11787 | CheckSessionUnlocked @11781; Clear @11784; LoadCustomersAsync @11785 | No extracted literal effects. |
| <span id="m-5d6956100d59"></span><code>MainViewModel.CloseCustomerChooser()</code><br>11789–11792 | — | No extracted literal effects. |
| <span id="m-49806a60247c"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>11794–11811 | SaveDurableCartAsync @11804; IsNullOrWhiteSpace @11808; ToString @11808; NewGuid @11808; RecordSuccessfulSearchUseAsync @11809; FromGuid @11809 | No extracted literal effects. |
| <span id="m-1dc4bcf48822"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>11813–11822 | SaveDurableCartAsync @11821 | No extracted literal effects. |
| <span id="m-a9e557391af8"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>11824–11869 | CheckSessionUnlocked @11826; IndexOf @11830; SelectWalkInCustomer @11836; FilterCustomers @11838; ConfigureAwait(DeactivateCustomerCommand, bool) @11850; ExecuteAsync(DeactivateCustomerCommand, bool) @11850; ConfigureAwait @11857; LoadCustomersAsync @11857; DispatchToUi @11862; SafePipelineError @11862; SafeError @11867 | No extracted literal effects. |
| <span id="m-4d8ede295160"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>11998–12037 | Add @12004; NewGuid @12005; RefreshManufacturingTablesAsync @12019; ConfigureAwait @12027; GetKitsAsync @12027; Clear @12028; Add @12029; DispatchToUi @12035; SafeError @12035 | No extracted literal effects. |
| <span id="m-1702221f41fa"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12041–12057 | CheckSessionUnlocked @12043; SetProductionActionMode @12045; FirstOrDefault @12050; LoadProductionIngredientLotsAsync @12055; TakeProductionSnapshot @12056 | No extracted literal effects. |
| <span id="m-11752a46bf79"></span><code>MainViewModel.CloseProductionModal()</code><br>12059–12073 | — | No extracted literal effects. |
| <span id="m-dacb8e875df2"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>12075–12174 | ExecuteExistingProductionAsync @12078; Resolve @12100; NewGuid @12103; ToUpperInvariant @12105; ToString @12105; Insert @12123; IsNullOrWhiteSpace @12145; Trim @12145; ToDictionary @12147; Where @12147; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @12151; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @12151; DispatchToUi @12154; SafePipelineError @12154; RecordSuccessfulSearchUseAsync @12161; FromGuid @12161; ConfigureAwait @12164; LoadManufacturingDataAsync @12164; LoadInventoryAsync @12165; SafeError @12171 | No extracted literal effects. |
| <span id="m-d8621e508568"></span><code>MainViewModel.CloseXReportModal()</code><br>12273–12276 | — | No extracted literal effects. |
| <span id="m-b191cc28cec9"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>12278–12308 | CheckSessionUnlocked @12280; Clear @12298; Where @12299; GetUnlockCandidates @12299; Equals @12300; Add @12304 | No extracted literal effects. |
| <span id="m-3038c007c0f1"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>12310–12314 | — | No extracted literal effects. |
| <span id="m-735d37846b18"></span><code>MainViewModel.CloseZReportModal()</code><br>12316–12319 | — | No extracted literal effects. |
| <span id="m-b5954f2fdda3"></span><code>MainViewModel.LoadReportDataAsync()</code><br>12321–12438 | ToString @12341; DispatchToUi @12357; ConfigureAwait @12385; ExecuteAsync @12385; Join @12387; Select(string, Money) @12387; InvoiceMoney @12387; ToDecimal @12390; ToDecimal @12391; ToDecimal @12392; ToDecimal @12393; ToDecimal @12395; ToDecimal @12397; ToDecimal @12398; ToDecimal @12399; ToDecimal @12400; ToDecimal @12401; ToUpperInvariant @12403; ToString @12403; ToString @12405; ToString @12406; Sum @12412; ToDecimal @12412; ToDecimal @12415; Add @12417; Format @12422; SafeError @12430 | No extracted literal effects. |
| <span id="m-ed6b5678f82c"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>12440–12529 | CheckSessionUnlocked @12443; IsNullOrWhiteSpace @12460; AuthenticateSelectedUser @12468; Trim @12470; Round @12479; Trim @12483; ConfigureAwait(CloseShiftCommand, Shift) @12487; ExecuteAsync(CloseShiftCommand, Shift) @12487; DispatchToUi @12505; SafePipelineError @12505; ConfigureAwait @12512; ExecuteAsync @12512; SetActiveCashier @12516; RefreshUnlockCandidates @12517; RaisePropertyChanged @12518; nameof @12518; LoadReportDataAsync @12522; LoadTeamsStaffAsync @12523; SafeError @12527 | No extracted literal effects. |
| <span id="m-6df9a954fb85"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>12531–12595 | FirstOrDefault @12533; CreateCommand @12540; CreateParameter @12552; ToString @12554; Add @12555; ExecuteReader @12557; Read @12558; Parse @12560; GetString @12560; GetInt64 @12563; Pow @12565; IsDBNull @12567; Add @12588 | FROM items @12541; JOIN barcodes @12541; JOIN product_categories @12541 |
| <span id="m-891858e614ff"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>12597–12701 | IsNullOrWhiteSpace @12599; Trim @12602; ToList @12605; Where @12605; IsNullOrEmpty @12606; Equals @12606; ToString @12608; AddToCart @12614; CreateCommand @12630; CreateParameter @12645; Add @12648; ExecuteReader @12650; Read @12652; Parse @12654; GetString @12654; ContainsKey @12655; GetInt64 @12659; Pow @12661; IsDBNull @12663; First @12690; Add @12691 | FROM items @12631; JOIN barcodes @12631; JOIN product_categories @12631 |
| <span id="m-45197ffe2d65"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>12703–12746 | IsNullOrWhiteSpace @12705; Trim @12708; AppendReceiveSerialScan @12714; TryAddUniqueExactMatchToCart @12720; Clear @12722; ToList @12727; Where @12727; Equals @12727; AddToCart @12730 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml</code> · 5907 lines · SHA-256 <code>53e26d3cb4370b7628020ff63ee7c98f638a50d706b64a0ae1c02eefd7c3be91</code>.
