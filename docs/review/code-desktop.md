---
id: PP-REVIEW-CODE-DESKTOP
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: []
---

# GetSeek.Desktop source catalogue

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.Desktop.csproj:1](code-desktop.md#src-2f265207af15). Dependencies: <code>GetSeek.UI.Components</code>, <code>GetSeek.Contracts</code>, <code>GetSeek.Infrastructure</code>, <code>GetSeek.Application</code>, <code>GetSeek.Domain</code>.

## App.axaml.cs {#src-de5bb454765b}

<code>Software/src/GetSeek.Desktop/App.axaml.cs</code> · 113 lines.

SHA-256: <code>22f2fa3069004b41b87a26662c9e666c2a08a95d773bd3570f11b8147e9ae83f</code>.

Declarations: <code>App : Avalonia.Application</code> (line 14).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-17cc6a23f0c2"></span><code>App.Initialize()</code><br>19–23 | Load @21 | No extracted literal effects. |
| <span id="m-4e55005e33b1"></span><code>App.OnUiUnhandledException(object?,DispatcherUnhandledExceptionEventArgs)</code><br>25–36 | Report @29; Post @35; Record @35 | No extracted literal effects. |
| <span id="m-f7abd70f5f1c"></span><code>App.OnFrameworkInitializationCompleted()</code><br>38–80 | Select @42; Cancel @50; Dispose @51; ToUpperInvariant @56; ToString @56; NewGuid @56; Report @57; Record @62; CreateStartupError @64; OnFrameworkInitializationCompleted @65; CreateDemo @71; CreateInitializing @71; InitializeAppAsync @76 | No extracted literal effects. |
| <span id="m-c227f29215ad"></span><code>App.InitializeAppAsync(MainWindow,bool,bool)</code><br>82–112 | BootstrapDemoWorkspaceAsync @85; BootstrapAsync @86; ReferenceEquals @90; Dispose @92; GetDefaultDatabasePath @101; ToString @103; LogDiagnosticError @104; Run @105; ConfigureAwait @107; RunAsync @107 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Bootstrap/PosBootstrapper.cs</code> · 345 lines.

SHA-256: <code>6958275f0438d90aae65c748a21f5248c8680f17d61b2d20388e2df694c62595</code>.

Declarations: <code>PosBootstrapper</code> (line 19).

<details markdown>
<summary>Methods, calls, table effects and failures (14)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-2863e7bcbde1"></span><code>PosBootstrapper.GetDefaultDatabasePath()</code><br>21–27 | GetFolderPath @23; Combine @24; CreateDirectory @25 | No extracted literal effects. |
| <span id="m-d7f9cca148b1"></span><code>PosBootstrapper.GetDefaultDemoWorkspaceDirectory()</code><br>29–33 | GetFolderPath @31; Combine @32 | No extracted literal effects. |
| <span id="m-6180ac19f20c"></span><code>PosBootstrapper.GetDefaultDemoDatabasePath()</code><br>35–36 | Combine @36; GetDefaultDemoWorkspaceDirectory @36 | No extracted literal effects. |
| <span id="m-010a66dc5c97"></span><code>PosBootstrapper.ValidateSeparateDemoDatabasePath(string)</code><br>38–52 | GetFullPath @40; GetDefaultDatabasePath @40; Equals @42; GetDirectoryName @45; CreateDirectory @47; GetAttributes @48; Exists @50 | InvalidOperationException @43; InvalidOperationException @49; InvalidOperationException @51 |
| <span id="m-cab7bff553e8"></span><code>PosBootstrapper.GetDefaultLogPath()</code><br>54–58 | GetFolderPath @56; Combine @57 | No extracted literal effects. |
| <span id="m-ba1b92053190"></span><code>PosBootstrapper.GetDefaultDocumentsPath()</code><br>60–66 | GetFolderPath @62; Combine @63; CreateDirectory @64 | No extracted literal effects. |
| <span id="m-a679348838c0"></span><code>PosBootstrapper.LogDiagnosticError(string,Exception,string)</code><br>68–72 | Log @71 | No extracted literal effects. |
| <span id="m-bd0f8ab44763"></span><code>PosBootstrapper.ResolveDiagnosticsWorkspace(string?,bool)</code><br>74–106 | IsNullOrWhiteSpace @81; Contains @90; Equals @91; ToString @91; GetFullPath @96; GetDefaultDatabasePath @97 | No extracted literal effects. |
| <span id="m-27d118a142ab"></span><code>PosBootstrapper.BootstrapAsync(string?,bool,CancellationToken)</code><br>108–112 | BootstrapAsyncCore @112 | No extracted literal effects. |
| <span id="m-d4b8bfc5ebb6"></span><code>PosBootstrapper.BootstrapDemoWorkspaceAsync(CancellationToken)</code><br>114–115 | BootstrapAsyncCore @115 | No extracted literal effects. |
| <span id="m-80415cd29d28"></span><code>PosBootstrapper.BootstrapAsyncCore(string?,bool,bool,CancellationToken)</code><br>117–165 | CreateDemo @125; ToUpperInvariant @128; ToString @128; NewGuid @128; IsNullOrWhiteSpace @132; GetDefaultDemoDatabasePath @134; GetDefaultDatabasePath @134; ValidateSeparateDemoDatabasePath @137; GetDirectoryName @139; IsNullOrEmpty @140; CreateDirectory @142; ConfigureAwait @149; ApplyWritePolicyAsync @149; BootstrapWithConnectionAsyncCore @151; LogDiagnosticError @161; ResolveDiagnosticsWorkspace @161; CreateStartupError @163 | No extracted literal effects. |
| <span id="m-454d11bc79c7"></span><code>PosBootstrapper.BootstrapWithConnectionAsync(DbConnection,string?,Func&lt;DbConnection&gt;?,CancellationToken)</code><br>167–172 | BootstrapWithConnectionAsyncCore @172 | No extracted literal effects. |
| <span id="m-0d19bb964a55"></span><code>PosBootstrapper.BootstrapWithConnectionAsyncCore(DbConnection,string?,Func&lt;DbConnection&gt;?,bool,CancellationToken)</code><br>174–317 | ToUpperInvariant @181; ToString @181; NewGuid @181; ConfigureAwait @189; InitializeDisposableDemoWorkspaceAsync @189; MigrateAsync @191; GetStoreProfileAsync @195; GetActiveItemsAsync @198; GetActiveShiftAsync @201; Initialize @204; Lock @205; connectionFactory @216; OpenAsync @234; ApplyWritePolicyAsync @236; ResolveDiagnosticsWorkspace @246; CreateCommand @261; ExecuteScalarAsync @264; CreateProduction @267; ConfigureInvoiceReader @280; ConfigureSearchPorts @283; Contains @284; ConfigureSalaryPorts @285; ConfigureTeamsPorts @288; ConfigureExpensePorts @291; RestoreActiveCartAsync @302; LoadManualPaymentSettingsAsync @303; LoadActivityInvoicesAsync @304; LoadSuppliersAsync @305; LoadOutputDevicesAsync @306; AuditDocumentsFolder @307; UpdateDemoSeedingAvailabilityAsync @308; LogDiagnosticError @313; CreateStartupError @315 | FROM users @263 |
| <span id="m-13d20e2c95c4"></span><code>PosBootstrapper.AuditDocumentsFolder(string,string)</code><br>319–343 | GetDefaultDocumentsPath @323; Exists @324; GetFiles @326; ToLowerInvariant @329; GetExtension @329; GetFileName @330; Contains @331; Log @333 | No extracted literal effects. |

</details>

## WorkspaceLaunchSelector.cs {#src-7282538860ec}

<code>Software/src/GetSeek.Desktop/Bootstrap/WorkspaceLaunchSelector.cs</code> · 79 lines.

SHA-256: <code>786a3db324f060464603a476d775b235ccb6427d39fe51544818f0e83f2c6a64</code>.

Declarations: <code>WorkspaceLaunchMode</code> (line 3), <code>WorkspaceLaunchSelection</code> (line 11), <code>WorkspaceLaunchSelector</code> (line 22).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f1cd6440bec3"></span><code>WorkspaceLaunchSelector.Select(string[]?,string?)</code><br>24–78 | Empty(string) @26; Contains @27; Equals @59; GetEnvironmentVariable @60 | No extracted literal effects. |

</details>

## NotificationItem.cs {#src-a6098c7284a3}

<code>Software/src/GetSeek.Desktop/Models/NotificationItem.cs</code> · 8 lines.

SHA-256: <code>033ddca9107f891f44b87513d6469e4ce4af1eb941828e5efdb3738c26898536</code>.

Declarations: <code>NotificationItem</code> (line 5).

## UiModels.cs {#src-89bb8d72822c}

<code>Software/src/GetSeek.Desktop/Models/UiModels.cs</code> · 919 lines.

SHA-256: <code>587faa2c028fb4f30097cb8000a5f4c540a97271dbbe58a1bfc6ae4d29ca4fc9</code>.

Declarations: <code>CurrencyFormatter</code> (line 6), <code>CategoryItem : ReactiveObject</code> (line 20), <code>ProductCategoryOption</code> (line 48), <code>ExpenseCategoryOption</code> (line 65), <code>ProductPurposeOption</code> (line 80), <code>UomOption</code> (line 85), <code>StoreUomPreferenceItem : ReactiveObject</code> (line 139), <code>ProductItem : ReactiveObject</code> (line 161), <code>OrderItem : ReactiveObject</code> (line 200), <code>ParkedCart</code> (line 311), <code>StaleCartPriceReviewUiRow</code> (line 325), <code>LotCandidateItem</code> (line 333), <code>SerialCandidateItem : ReactiveObject</code> (line 348), <code>OrderStatusChip : ReactiveObject</code> (line 372), <code>OrderLogItem : ReactiveObject</code> (line 412), <code>InventoryItem : ReactiveObject</code> (line 443), <code>KitComponentDraftItem : ReactiveObject</code> (line 597), <code>PayrollMonthOption : IEquatable&lt;PayrollMonthOption&gt;</code> (line 629), <code>StaffMember : ReactiveObject</code> (line 653), <code>TeamMemberShiftItem : ReactiveObject</code> (line 713), <code>UserPermissionOverrideItem : ReactiveObject</code> (line 724), <code>ReportTenderItem : ReactiveObject</code> (line 782), <code>ShiftReportSummary : ReactiveObject</code> (line 791), <code>FacilityItem : ReactiveObject</code> (line 831), <code>BinLocationItem : ReactiveObject</code> (line 841), <code>ItemLocationEligibilityItem : ReactiveObject</code> (line 855), <code>ReceiveTrackingKind</code> (line 870), <code>ReceiveLineItem : ReactiveObject</code> (line 882).

<details markdown>
<summary>Methods, calls, table effects and failures (11)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7303823d0b7e"></span><code>CurrencyFormatter.Format(decimal,string,int)</code><br>8–17 | Clamp @10; Round @14; ToString @16 | No extracted literal effects. |
| <span id="m-bfe1e76935c9"></span><code>ProductCategoryOption.ToString()</code><br>62–62 | — | No extracted literal effects. |
| <span id="m-bb0cf46280a9"></span><code>ExpenseCategoryOption.ToString()</code><br>77–77 | — | No extracted literal effects. |
| <span id="m-c4b775694cc8"></span><code>ProductPurposeOption.ToString()</code><br>82–82 | — | No extracted literal effects. |
| <span id="m-7c1bacac4559"></span><code>UomOption.ToString()</code><br>136–136 | — | No extracted literal effects. |
| <span id="m-0ae9be36a799"></span><code>LotCandidateItem.ToString()</code><br>344–344 | — | No extracted literal effects. |
| <span id="m-d950e65633bf"></span><code>SerialCandidateItem.ToString()</code><br>369–369 | — | No extracted literal effects. |
| <span id="m-090b3276f6a9"></span><code>PayrollMonthOption.Equals(PayrollMonthOption?)</code><br>642–643 | — | No extracted literal effects. |
| <span id="m-cbda2790555e"></span><code>PayrollMonthOption.Equals(object?)</code><br>645–646 | Equals @646 | No extracted literal effects. |
| <span id="m-732f35abc037"></span><code>PayrollMonthOption.GetHashCode()</code><br>648–648 | GetHashCode @648 | No extracted literal effects. |
| <span id="m-ec86049b38e3"></span><code>PayrollMonthOption.ToString()</code><br>650–650 | — | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Services/UiPreferencesService.cs</code> · 4,907 lines.

SHA-256: <code>b34d8c1f462e0df79ed9e11ea9f7389555a71aef1705f1a2aca9aadbec9d5f5c</code>.

Declarations: <code>UiPreferences</code> (line 12), <code>IUiPreferencesService</code> (line 20), <code>UiPreferencesService : IUiPreferencesService</code> (line 30), <code>ILocalizationService</code> (line 86), <code>LocalizationService : ILocalizationService</code> (line 96), <code>ThemeManager</code> (line 4798).

<details markdown>
<summary>Methods, calls, table effects and failures (12)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-69a3b01d8029"></span><code>IUiPreferencesService.Load()</code><br>22–22 | — | No extracted literal effects. |
| <span id="m-592fdd3892e2"></span><code>IUiPreferencesService.Save(UiPreferences)</code><br>23–23 | — | No extracted literal effects. |
| <span id="m-c2b8dbfc95d6"></span><code>UiPreferencesService.Load()</code><br>47–64 | Exists @51; ReadAllText @53; Deserialize(UiPreferences) @54 | No extracted literal effects. |
| <span id="m-7261564d0166"></span><code>UiPreferencesService.Save(UiPreferences)</code><br>66–82 | GetDirectoryName @70; IsNullOrEmpty @71; CreateDirectory @73; WriteAllText @76; Serialize @76 | No extracted literal effects. |
| <span id="m-6065c0c3e12d"></span><code>ILocalizationService.Localize(string,object?[])</code><br>89–89 | — | No extracted literal effects. |
| <span id="m-cf7b825764b6"></span><code>LocalizationService.Localize(string,object?[])</code><br>4765–4795 | ToLowerInvariant @4767; Trim @4767; TryGetValue @4775; TryGetValue @4778; Format @4788 | No extracted literal effects. |
| <span id="m-313765708204"></span><code>ThemeManager.Resolve(string?)</code><br>4815–4816 | IsNullOrWhiteSpace @4816; ContainsKey @4816 | No extracted literal effects. |
| <span id="m-28d1d43ea341"></span><code>ThemeManager.DisplayName(string?)</code><br>4818–4818 | Resolve @4818 | No extracted literal effects. |
| <span id="m-c3273d3795a4"></span><code>ThemeManager.NextTheme(string?)</code><br>4821–4834 | Equals @4826 | No extracted literal effects. |
| <span id="m-dff66277d86f"></span><code>ThemeManager.Apply(string?)</code><br>4837–4871 | Equals @4840; Resolve @4842; SwapThemeSlot @4856; CheckAccess @4861; Post @4863; ApplyCore @4867 | No extracted literal effects. |
| <span id="m-3e0e4e14dc9f"></span><code>ThemeManager.IsThemeInclude(object)</code><br>4874–4876 | Contains @4876 | No extracted literal effects. |
| <span id="m-18574bca22ab"></span><code>ThemeManager.SwapThemeSlot(IList&lt;IResourceProvider&gt;,string)</code><br>4878–4901 | ToList(ResourceInclude) @4882; Where(ResourceInclude) @4882; OfType(ResourceInclude) @4882; Remove @4884; Equals @4889; Add @4900 | No extracted literal effects. |

</details>

## CatalogOrderPageHelper.cs {#src-88c3ed51d197}

<code>Software/src/GetSeek.Desktop/ViewModels/CatalogOrderPageHelper.cs</code> · 440 lines.

SHA-256: <code>8827abfd7c476f7411fc4c00e71eab258782bbffe08d92e28f06bebe9fcbf5e2</code>.

Declarations: <code>CatalogFamily</code> (line 9), <code>AllItemCycleState</code> (line 15), <code>NocodeCycleState</code> (line 23), <code>CatalogCycleStateMachine</code> (line 30), <code>CatalogFilterRequest</code> (line 156), <code>CatalogFilterResult</code> (line 170), <code>CatalogOrderPageHelper</code> (line 178).

<details markdown>
<summary>Methods, calls, table effects and failures (22)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a314a645da82"></span><code>CatalogCycleStateMachine.GetNextAllItemState(AllItemCycleState)</code><br>37–44 | — | No extracted literal effects. |
| <span id="m-12544ee078c7"></span><code>CatalogCycleStateMachine.GetNextNocodeState(NocodeCycleState)</code><br>46–52 | — | No extracted literal effects. |
| <span id="m-6c3f99aae86b"></span><code>CatalogCycleStateMachine.GetAllItemCaption(AllItemCycleState)</code><br>54–61 | — | No extracted literal effects. |
| <span id="m-ae24f595d6b1"></span><code>CatalogCycleStateMachine.GetAllItemCaption(AllItemCycleState,ILocalizationService?)</code><br>63–74 | GetAllItemCaption @65; Localize @68 | No extracted literal effects. |
| <span id="m-9fd2d17ec023"></span><code>CatalogCycleStateMachine.GetNocodeCaption(NocodeCycleState)</code><br>76–82 | — | No extracted literal effects. |
| <span id="m-6b3c331e48bf"></span><code>CatalogCycleStateMachine.GetNocodeCaption(NocodeCycleState,ILocalizationService?)</code><br>84–94 | GetNocodeCaption @86; Localize @89 | No extracted literal effects. |
| <span id="m-3796b6e7078b"></span><code>CatalogCycleStateMachine.SelectOrCycleAllItem()</code><br>103–113 | GetNextAllItemState @111 | No extracted literal effects. |
| <span id="m-10f608ace3dc"></span><code>CatalogCycleStateMachine.SelectOrCycleNocode()</code><br>115–130 | GetNextNocodeState @128 | No extracted literal effects. |
| <span id="m-6140d8ec07cb"></span><code>CatalogCycleStateMachine.CycleActive()</code><br>132–142 | GetNextAllItemState @136; GetNextNocodeState @140 | No extracted literal effects. |
| <span id="m-10b698c1096b"></span><code>CatalogCycleStateMachine.SelectFamily(CatalogFamily)</code><br>144–153 | — | No extracted literal effects. |
| <span id="m-9c38bef92992"></span><code>CatalogOrderPageHelper.CompareAtoZ(ProductItem,ProductItem)</code><br>184–193 | Compare @186; CompareTo @192 | No extracted literal effects. |
| <span id="m-2adcf1451f95"></span><code>CatalogOrderPageHelper.CompareZtoA(ProductItem,ProductItem)</code><br>195–205 | Compare @198; CompareTo @204 | No extracted literal effects. |
| <span id="m-e62d1744fc19"></span><code>CatalogOrderPageHelper.CompareMostSold(ProductItem,ProductItem)</code><br>207–213 | CompareTo @209; CompareAtoZ @212 | No extracted literal effects. |
| <span id="m-02e609ca986c"></span><code>CatalogOrderPageHelper.CompareNonBarcodeFirst(ProductItem,ProductItem)</code><br>215–222 | CompareAtoZ @221 | No extracted literal effects. |
| <span id="m-22658beba4d9"></span><code>CatalogOrderPageHelper.CompareBarcodeFirst(ProductItem,ProductItem)</code><br>224–231 | CompareAtoZ @230 | No extracted literal effects. |
| <span id="m-7002cf50a62f"></span><code>CatalogOrderPageHelper.CompareMostSoldNonBarcode(ProductItem,ProductItem)</code><br>233–244 | CompareMostSold @241; CompareAtoZ @243 | No extracted literal effects. |
| <span id="m-b86be992f565"></span><code>CatalogOrderPageHelper.CompareMostSoldAll(ProductItem,ProductItem)</code><br>246–249 | CompareMostSold @248 | No extracted literal effects. |
| <span id="m-02dc43f87a76"></span><code>CatalogOrderPageHelper.HasMatchingBarcode(ProductItem,Func&lt;string, bool&gt;)</code><br>251–263 | IsNullOrEmpty @257; predicate @257 | No extracted literal effects. |
| <span id="m-895b2c1dbc4d"></span><code>CatalogOrderPageHelper.MatchesSearch(ProductItem,string)</code><br>265–279 | IsNullOrWhiteSpace @267; IsNullOrEmpty @269; Contains @269; Contains @272; HasMatchingBarcode @275; Contains @275 | No extracted literal effects. |
| <span id="m-91d3edceeb78"></span><code>CatalogOrderPageHelper.GetSearchRelevanceTier(ProductItem,string)</code><br>281–311 | IsNullOrEmpty @284; Equals @284; HasMatchingBarcode @285; StartsWith @297; StartsWith @298; StartsWith @304 | No extracted literal effects. |
| <span id="m-3dacbdf77d5e"></span><code>CatalogOrderPageHelper.CompareSearchRelevance(ProductItem,ProductItem,string)</code><br>313–322 | GetSearchRelevanceTier @315; CompareTo @319; CompareAtoZ @321 | No extracted literal effects. |
| <span id="m-164cfb5ebb48"></span><code>CatalogOrderPageHelper.FilterAndPage(CatalogFilterRequest)</code><br>324–439 | ThrowIfNull @326; IsNullOrWhiteSpace @328; Trim @328; Equals @336; MatchesSearch @374; Add @379; Sort @385; CompareSearchRelevance @385; Contains @414; Empty(ProductItem) @423; Clamp @428; ToList @430; Take @430; Skip @430 | No extracted literal effects. |

</details>

## ItemPricingEditorState.cs {#src-e15de4a665a7}

<code>Software/src/GetSeek.Desktop/ViewModels/ItemPricingEditorState.cs</code> · 125 lines.

SHA-256: <code>a1bf5c8d63d19b6e78721614e18c95182f643d31b91a1cc55cbe193198addef4</code>.

Declarations: <code>ProductPricePreviewRow</code> (line 10), <code>ItemPricingEditorState : ReactiveObject</code> (line 17).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-c133b52f37b9"></span><code>ItemPricingEditorState.OnTiersChanged(object?,NotifyCollectionChangedEventArgs)</code><br>69–76 | RaisePropertyChanged @75; nameof @75 | No extracted literal effects. |
| <span id="m-9e39e1b43b91"></span><code>ItemPricingEditorState.OnTierChanged(object?,PropertyChangedEventArgs)</code><br>78–78 | RaisePropertyChanged @78; nameof @78 | No extracted literal effects. |
| <span id="m-0cbbb24d961d"></span><code>ItemPricingEditorState.Clone()</code><br>80–107 | Add @96 | No extracted literal effects. |
| <span id="m-ea651f1dc797"></span><code>ItemPricingEditorState.ToCommand(Guid,int)</code><br>109–124 | ToMinorUnits @116; ToList @117; Select @117 | No extracted literal effects. |

</details>

## MainViewModel.Catalog.cs {#src-13c27bf9bf1a}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Catalog.cs</code> · 462 lines.

SHA-256: <code>99699baa508acd0672d181e22b13210a279b228834446cf2e6329ef923750689</code>.

Declarations: <code>MainViewModel</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (16)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-427b4ac50790"></span><code>MainViewModel.SetProductServiceGate(bool)</code><br>29–43 | RaisePropertyChanged @33; nameof @33; Equals @35; SelectCatalogKind @37; ApplyFilter @41 | No extracted literal effects. |
| <span id="m-ae2b98473303"></span><code>MainViewModel.IsProductEligibleForCurrentScope(ProductItem?)</code><br>98–125 | Equals @102; IsNullOrWhiteSpace @115 | No extracted literal effects. |
| <span id="m-36d8a913f355"></span><code>MainViewModel.RaiseCatalogLabels()</code><br>127–140 | RaisePropertyChanged @129; nameof @129 | No extracted literal effects. |
| <span id="m-4570d4410f4c"></span><code>MainViewModel.InitializeCatalogCommands()</code><br>157–171 | Create @159; Create(object) @162; SetCatalogPageSize @164; TryParse @165; SelectCatalogKind @169 | No extracted literal effects. |
| <span id="m-028c6478ea5a"></span><code>MainViewModel.SelectOrCycleAllItem()</code><br>173–185 | SelectOrCycleAllItem @175; RaisePropertyChanged @176; nameof @176; ApplyFilter @184 | No extracted literal effects. |
| <span id="m-60a3206d3c89"></span><code>MainViewModel.SelectOrCycleNocode()</code><br>187–199 | SelectOrCycleNocode @189; RaisePropertyChanged @190; nameof @190; ApplyFilter @198 | No extracted literal effects. |
| <span id="m-969ff87dfaa4"></span><code>MainViewModel.CycleActiveCatalogOrdering()</code><br>201–214 | CycleActive @203; RaisePropertyChanged @204; nameof @204; ApplyFilter @213 | No extracted literal effects. |
| <span id="m-aad5cef5ae8d"></span><code>MainViewModel.SetCatalogPageSize(int)</code><br>216–239 | Contains @223; RaisePropertyChanged @230; nameof @230; ApplyFilter @238 | No extracted literal effects. |
| <span id="m-deb3134f61ae"></span><code>MainViewModel.NextCatalogPage()</code><br>241–249 | RaisePropertyChanged @246; nameof @246; ApplyFilter @247 | No extracted literal effects. |
| <span id="m-c84f435fd159"></span><code>MainViewModel.PreviousCatalogPage()</code><br>251–259 | RaisePropertyChanged @256; nameof @256; ApplyFilter @257 | No extracted literal effects. |
| <span id="m-f2c821593a75"></span><code>MainViewModel.GoToCatalogPage(int)</code><br>261–266 | RaisePropertyChanged @264; nameof @264; ApplyFilter @265 | No extracted literal effects. |
| <span id="m-0fb364bb1815"></span><code>MainViewModel.SelectCatalogKind(string)</code><br>268–331 | Equals @270; RaisePropertyChanged @279; nameof @279; Clear @302; Any @307; IsNullOrEmpty @311; LoadCategoriesForKind @324; ApplyFilter @330 | No extracted literal effects. |
| <span id="m-28cba691b7bf"></span><code>MainViewModel.LoadCategoriesForKind(string)</code><br>333–359 | ToList @335; Where @335; Equals @335; Clear @336; GroupBy @337; IsNullOrEmpty @341; Add @349; Count @353; RaisePropertyChanged @358; nameof @358 | No extracted literal effects. |
| <span id="m-0f14967e987a"></span><code>MainViewModel.OnSearchQueryChanged(string?,string?)</code><br>361–395 | IsNullOrWhiteSpace @363; RaisePropertyChanged @370; nameof @370; ApplyFilter @394 | No extracted literal effects. |
| <span id="m-6cf4e6910bce"></span><code>MainViewModel.SelectCategoryById(Guid?)</code><br>397–423 | SelectCategory @401; FirstOrDefault @405; FirstOrDefault @415; RaisePropertyChanged @418; nameof @418; ApplyFilter @421 | No extracted literal effects. |
| <span id="m-4380dfda7e82"></span><code>MainViewModel.ApplyFilter()</code><br>425–461 | FilterAndPage @441; RaisePropertyChanged @447; nameof @447; Clear @456; Add @459 | No extracted literal effects. |

</details>

## MainViewModel.Commercial.cs {#src-e4058a856f7c}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Commercial.cs</code> · 599 lines.

SHA-256: <code>9069c4162d2dd0d35437b69566f8150339976c8c2fb2ab2a666e7d9cdc1d965d</code>.

Declarations: <code>CommercialLineEditor : ReactiveObject</code> (line 17), <code>DispatchQuantityEditor : ReactiveObject</code> (line 39), <code>MainViewModel</code> (line 48).

<details markdown>
<summary>Methods, calls, table effects and failures (33)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-586832c3eecb"></span><code>MainViewModel.CanOpenSeparateConnection(System.Data.Common.DbConnection?)</code><br>50–50 | IsNullOrWhiteSpace @50; Contains @50 | No extracted literal effects. |
| <span id="m-6e35d4ec1292"></span><code>MainViewModel.CanQueryCommercialPermissionAsync(string,CancellationToken)</code><br>51–56 | CanOpenSeparateConnection @53; HasPermission @53; ConfigureAwait @54; OpenAsync @54; HasPermissionAsync @54 | No extracted literal effects. |
| <span id="m-858494434d02"></span><code>MainViewModel.ResetCommercialFilterPages()</code><br>98–98 | ResetToFirstPage @98; ResetToFirstPage @98; LoadCommercialAsync @98 | No extracted literal effects. |
| <span id="m-0b2be05ba0f5"></span><code>MainViewModel.CommercialSourceText(string)</code><br>153–153 | Localize @153 | No extracted literal effects. |
| <span id="m-11fa5fadee55"></span><code>MainViewModel.CText(string)</code><br>168–168 | Localize @168 | No extracted literal effects. |
| <span id="m-e356c819dbdb"></span><code>MainViewModel.CMoney(long,string,int)</code><br>169–169 | ToString @169; ToDecimal @169 | No extracted literal effects. |
| <span id="m-3d68327c61aa"></span><code>MainViewModel.InitializeCommercialWorkspace()</code><br>182–218 | CreateFromTask @184; Create @185; Clear @188; Clear @188; Clear @188; nameof @189; RaisePropertyChanged @189; ResetCommercialFilterPages @190; OpenCommercial @192; AddCommercialLine @193; CreateFromTask(CommercialLineEditor) @193; Create(CommercialLineEditor) @193; Remove @193; SaveCommercialAsync @194; CreateFromTask(CommercialInvoiceRow) @198; OpenCommercialMoneyAsync @198; OpenCommercialReceiptAsync @202; OpenCommercialPurchaseCreditAsync @203; Create(MoneyEventRow) @208; Parse @208; Create(ShipmentSummary) @209; CreateFromTask(MoneyEventRow) @210; TryParse @210; LoadCommercialSourceInvoicesAsync @210; RecordSuccessfulSearchUseAsync @210; FromGuid @210; CreateFromTask(ShipmentSummary) @211; LoadCommercialHistoryAsync @211; Register @212; BindRefresh @213; LoadCommercialAsync @213; BindRefresh @213; BindRefresh @213; CommercialSnapshot @213; OpenCommercialInvoiceAsync @215; Create(DispatchQuantityEditor) @216; CText @216; BuildCommercialTables @217 | No extracted literal effects. |
| <span id="m-f539d9800afd"></span><code>MainViewModel.BuildCommercialTables()</code><br>219–231 | CText @221; ToString @222; Col @223; CMoney @223; HasPermission @224; ToLocalTime @226; Parse @228; CommercialSourceText @228; LocalizeTable @230; Localize @230; Max @230; Ceiling @230 | No extracted literal effects. |
| <span id="m-5be832fb8f68"></span><code>MainViewModel.ResolveCommercialDateRangeUtcAsync()</code><br>232–267 | ConfigureAwait @244; GetStoreTimeZoneAsync @244; ConvertLocalToUtc @256; AddDays @262 | No extracted literal effects. |
| <span id="m-d092196ddc32"></span><code>MainViewModel.LoadCommercialAsync()</code><br>269–311 | CanOpenSeparateConnection @271; ConfigureAwait @275; ResolveCommercialDateRangeUtcAsync @275; DispatchToUi @278; ApplyPagedResult @282; ApplyPagedResult @283; CanQueryCommercialPermissionAsync @289; GetInvoicesAsync @293; ToPageRequest @293; GetShipmentsAsync @299; ToPageRequest @299; ApplyPagedResult @300; GetAccountsAsync @305; GetMoneyAsync @306; ToPageRequest @306; TryParse @306; ToString @306; Clear @307; Add @307; RaisePropertyChanged @307; nameof @307; SafeError @310 | No extracted literal effects. |
| <span id="m-9ad8253ebdf4"></span><code>MainViewModel.OpenCommercial(string,string)</code><br>312–319 | CheckSessionUnlocked @314; CText @314; HasPermission @314; ToString @315; NewGuid @315; Clear @315; Clear @315; Clear @315; Clear @315; Clear @316; Clear @316; Where @317; GetProperties @317; GetType @317; StartsWith @317; RaisePropertyChanged @317; CommercialSnapshot @318; RefreshCommercialLookupsAsync @318 | No extracted literal effects. |
| <span id="m-7b9c6d1a09b6"></span><code>MainViewModel.RefreshCommercialLookupsAsync()</code><br>320–331 | CanOpenSeparateConnection @322; ConfigureAwait @325; CanQueryCommercialPermissionAsync @325; FindPartiesAsync @326; FindItemsAsync @326; DispatchToUi @326; Clear @326; Add @326; Clear @326; Add @326; GetAccountsAsync @328; Clear @328; Where @328; Add @328; SafeError @330 | No extracted literal effects. |
| <span id="m-48cd9b5932b9"></span><code>MainViewModel.EnsurePaymentAccountsLoadedAsync(CancellationToken)</code><br>332–355 | ConfigureAwait @334; CanQueryCommercialPermissionAsync @334; GetAccountsAsync @338; DispatchToUi @339; Clear @342; Where @343; Add @345; RaisePropertyChanged @347; nameof @347; SafeError @353 | No extracted literal effects. |
| <span id="m-e66f96c79da6"></span><code>MainViewModel.AssignCommercialParty(CommercialPartyChoice?,string?)</code><br>356–367 | ReferenceEquals @358; IsNullOrWhiteSpace @364; ToString @364; NewGuid @364; RecordSuccessfulSearchUseAsync @365; FromGuid @365 | No extracted literal effects. |
| <span id="m-148e9eb28017"></span><code>MainViewModel.AddCommercialLine(string?)</code><br>369–378 | Any @372; CText @372; Add @374; ToDecimal @374; IsNullOrWhiteSpace @376; ToString @376; NewGuid @376; RecordSuccessfulSearchUseAsync @377; FromGuid @377 | No extracted literal effects. |
| <span id="m-2897b6af971e"></span><code>MainViewModel.LoadCommercialKitAsync(CommercialLineEditor)</code><br>379–384 | GetKitLeavesAsync @382; Clear @382; Add @382; SafeError @383 | No extracted literal effects. |
| <span id="m-de15da1f80fe"></span><code>MainViewModel.OpenCommercialInvoiceAsync(CommercialInvoiceRow)</code><br>385–411 | OpenCommercial @390; GetDraftAsync @391; CText @391; ToDateTime @392; Add @393; ToDecimal @393; Where @394; First @395; LoadCommercialKitAsync @395; FirstOrDefault @395; CommercialSnapshot @396; GetPurchaseAsync @400; RecordSuccessfulSearchUseAsync @406; FromGuid @406; RaisePropertyChanged @408; nameof @408; LoadCommercialHistoryAsync @408; GetInvoiceAsync @410; OpenInvoiceAsync @410 | No extracted literal effects. |
| <span id="m-795fe1fcb3fe"></span><code>MainViewModel.OpenCommercialDispatchAsync(CommercialInvoiceRow)</code><br>412–417 | OpenCommercial @414; GetReservationsAsync @415; Add @415; CommercialSnapshot @415; SafeError @416 | No extracted literal effects. |
| <span id="m-093127202339"></span><code>MainViewModel.OpenCommercialReceiptAsync(CommercialInvoiceRow,bool)</code><br>418–423 | OpenCommercial @420; GetPurchaseAsync @421; Where @421; Add @421; CommercialSnapshot @421; SafeError @422 | No extracted literal effects. |
| <span id="m-66f24cce46e7"></span><code>MainViewModel.OpenCommercialPurchaseCreditAsync(CommercialInvoiceRow)</code><br>424–429 | OpenCommercial @426; GetPurchaseAsync @427; Where @428; Add @428; CommercialSnapshot @428 | No extracted literal effects. |
| <span id="m-f131e0291027"></span><code>MainViewModel.OpenCommercialMoneyAsync(CommercialInvoiceRow,string,string)</code><br>430–431 | OpenCommercial @431; ToDecimal @431; Abs @431; GetUnshippedLinesAsync @431; Add @431; CommercialSnapshot @431; RefreshCommercialLookupsAsync @431 | No extracted literal effects. |
| <span id="m-8190e61cd357"></span><code>MainViewModel.CommercialSnapshot()</code><br>432–432 | Serialize @432; Select @432; Select @432; Select @432 | No extracted literal effects. |
| <span id="m-619f1c8b74d6"></span><code>MainViewModel.RequestCommercialClose()</code><br>433–433 | CommercialSnapshot @433 | No extracted literal effects. |
| <span id="m-bbe14e5207ae"></span><code>MainViewModel.RequestCommercialReturnAsync()</code><br>434–447 | CheckSessionUnlocked @436; InvoiceEditorState @437; Localize @437; ExecuteAsync(RequestReturnShipmentCommand, Guid) @441; ReturnCommand @441; LoadCommercialAsync @443; SafeError @445 | No extracted literal effects. |
| <span id="m-6e2e529fb0d5"></span><code>MainViewModel.OpenCommercialReturnReceiptAsync(CommercialInvoiceRow)</code><br>448–463 | OpenCommercial @450; GetReturnRequestAsync @453; GetInvoiceAsync @453; First @456; ToList @456; Select @456; Where @456; Any @456; Add @456; Join @456; PreviewReturnAsync @458; RaisePropertyChanged @460; nameof @460; CommercialSnapshot @460; SafeError @462 | No extracted literal effects. |
| <span id="m-f5d7324d7f0f"></span><code>MainViewModel.SaveCommercialAsync(bool)</code><br>464–544 | CommercialSnapshot @469; ToString @469; NewGuid @469; FromDateTime @472; CText @475; ExecuteAsync(SaveOrderDraftCommand, Guid) @476; ToList @476; Select @476; FromDecimal @476; Select @476; Where @476; ExecuteAsync(PreviewOrderInvoiceCommand, OrderInvoicePreview) @480; FirstOrDefault @483; CMoney @483; RaisePropertyChanged @485; nameof @485; ExecuteAsync(IssueOrderInvoiceCommand, SalesInvoice) @487; Failure(Guid) @487; ExecuteAsync(SavePurchaseDraftCommand, Guid) @495; LoadCommercialAsync @496; Preview @502; ExecuteAsync(RecordSupplierInvoiceCommand, Guid) @508; ExecuteAsync(DispatchShipmentCommand, Guid) @512; Where @512; Where @514; IsNullOrWhiteSpace @514; SpecifyKind @514; AddTicks @514; AddDays @514; Split @514; ExecuteAsync(ReturnSupplierGoodsCommand, Guid) @514; ExecuteAsync(ReceivePurchaseGoodsCommand, Guid) @514; ExecuteAsync(ReplaceInvoiceReservationCommand, bool) @516; Success(Guid) @516; ExecuteAsync(UpdateShipmentTrackingCommand, bool) @518; ExecuteAsync(CancelSupplierInvoiceLinesCommand, Guid) @519; ExecuteAsync(CancelReturnShipmentRequestCommand, Guid) @520; ExecuteAsync(ConfirmSupplierReturnDeliveryCommand, bool) @522; ExecuteAsync(ConfirmShipmentDeliveryCommand, bool) @522; PreviewCommercialReturnReceiptAsync @525; ExecuteAsync(ReceiveReturnShipmentCommand, Guid) @528; BuildCommercialReturnReceipt @528; ExecuteAsync(ReverseMoneyTransferCommand, Guid) @530; ExecuteAsync(ReceiveSupplierRefundCommand, Guid) @531; ExecuteAsync(CancelInvoiceRemainderCommand, Guid) @532; ExecuteAsync(RecordAccountOpeningCommand, Guid) @533; ExecuteAsync(RefundCancelledInvoiceCommand, Guid) @534; ExecuteAsync(CreateMoneyAccountCommand, Guid) @535; ExecuteAsync(TransferMoneyCommand, Guid) @536; ExecuteAsync(PaySupplierInvoiceCommand, Guid) @537; ExecuteAsync(CollectBankInvoiceCommand, Guid) @538; LoadInventoryAsync @540; SafeError @542 | InvalidOperationException @475; InvalidOperationException @491; InvalidOperationException @539 |
| <span id="m-63e79015eeb4"></span><code>MainViewModel.PreviewCommercialReturnReceiptAsync()</code><br>545–560 | CText @547; GetInvoiceAsync @548; BuildCommercialReturnReceipt @550; PreviewReturnAsync @553; Round @556; CMoney @559; RaisePropertyChanged @559; nameof @559 | InvalidOperationException @547; InvalidOperationException @555; InvalidOperationException @558 |
| <span id="m-22e0627de261"></span><code>MainViewModel.BuildCommercialReturnReceipt()</code><br>561–577 | CText @563; ToList @564; Select @564; Where @564; First @566; ToHashSet @567; Split @567; First @568; Where @569; Select @569; FirstOrDefault @571; Contains @572 | InvalidOperationException @563 |
| <span id="m-d42fe1949f29"></span><code>MainViewModel.LoadCommercialSourceInvoicesAsync(Guid,string)</code><br>578–582 | GetSourceInvoicesAsync @580; Clear @581; Add @581 | No extracted literal effects. |
| <span id="m-0ac7a99516e1"></span><code>MainViewModel.LoadCommercialHistoryAsync(Guid,string)</code><br>583–587 | GetHistoryAsync @585; Clear @586; Add @586; ToString @586; ToLocalTime @586; CommercialSourceText @586 | No extracted literal effects. |
| <span id="m-7da92e02f004"></span><code>MainViewModel.PrintCommercialDocumentAsync()</code><br>588–595 | ExecuteAsync(QueueCommercialDocumentCommand, Guid) @593; CText @593; SafeError @594 | No extracted literal effects. |
| <span id="m-0fef1b6fc226"></span><code>MainViewModel.RefreshCommercialLocalization()</code><br>597–597 | BuildCommercialTables @597; Where @597; GetProperties @597; GetType @597; StartsWith @597; RaisePropertyChanged @597 | No extracted literal effects. |
| <span id="m-474925d7b12c"></span><code>MainViewModel.ResetCommercialWorkspace()</code><br>598–598 | Clear @598; Clear @598; Clear @598; Clear @598; Clear @598; Clear @598; Clear @598 | No extracted literal effects. |

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

## MainViewModel.ImportResults.cs {#src-969918d8254d}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ImportResults.cs</code> · 114 lines.

SHA-256: <code>6a4abb535229d4afe94f0ea89c0d81e3ff6c13f70d4bb0ed47d2ca664aa562fa</code>.

Declarations: <code>MainViewModel</code> (line 13), <code>ImportAttempt</code> (line 15), <code>ImportDownload</code> (line 16).

<details markdown>
<summary>Methods, calls, table effects and failures (10)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3c2b304e26fe"></span><code>MainViewModel.CanDownloadImportResult(ImportDownload?)</code><br>27–28 | ReferenceEquals @28 | No extracted literal effects. |
| <span id="m-2cedebe210ac"></span><code>MainViewModel.IsCurrentImportAttempt(ImportAttempt)</code><br>29–31 | ReferenceEquals @30 | No extracted literal effects. |
| <span id="m-5bbacd62125a"></span><code>MainViewModel.NotifyImportResults()</code><br>32–36 | RaisePropertyChanged @34; nameof @34 | No extracted literal effects. |
| <span id="m-b75eda067930"></span><code>MainViewModel.ClearImportResults()</code><br>37–44 | Increment @39; NotifyImportResults @43 | No extracted literal effects. |
| <span id="m-d307265a3b8c"></span><code>MainViewModel.DownloadImportResult(bool)</code><br>45–50 | CanDownloadImportResult @48; NotifyImportResults @48; Invoke @49 | No extracted literal effects. |
| <span id="m-5a0b28739c54"></span><code>MainViewModel.ReportImportResultSave(byte[],string)</code><br>51–56 | FirstOrDefault @53; ReferenceEquals @53; CanDownloadImportResult @54; Localize @55 | No extracted literal effects. |
| <span id="m-2d5a0b8916f8"></span><code>MainViewModel.FinishImportAttempt(ImportAttempt,byte[],string,string)</code><br>57–84 | IsCurrentImportAttempt @59; ResetThirdPartyImport @67; ResetInventoryImport @74; NotifyImportResults @76; Invoke @78; ReportException @81; ReportImportResultSave @82 | No extracted literal effects. |
| <span id="m-2dfa4595a241"></span><code>MainViewModel.FinishFailedImport(ImportAttempt,IReadOnlyList&lt;ImportIssue&gt;,string)</code><br>85–93 | ToArray @89; Append @89; FailedWorkbook @90; DispatchToUi @91; FinishImportAttempt @91; Localize @92 | No extracted literal effects. |
| <span id="m-1aa855610ca4"></span><code>MainViewModel.ImportCommandIssue(string?)</code><br>94–96 | — | No extracted literal effects. |
| <span id="m-f76c6c495fa5"></span><code>MainViewModel.RecoverImportOutcomeAsync(CommandResult&lt;T&gt;,object,string,IUnitOfWork)</code><br>99–113 | Failure(T) @104; ToHexStringLower @105; HashData @105; GetBytes @105; Serialize @105; GetType @105; ConfigureAwait @106; CheckAsync @106; Deserialize(T) @107; Success(T) @108 | IMPORT_OUTCOME_UNKNOWN @104; IMPORT_OUTCOME_UNKNOWN @109; IMPORT_OUTCOME_UNKNOWN @112 |

</details>

## MainViewModel.ImportReview.cs {#src-90113acc8bd5}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ImportReview.cs</code> · 139 lines.

SHA-256: <code>b03d4db44b6a6bff0b75b7d69b2e30d78963238f60511345e24d5684490481f0</code>.

Declarations: <code>MainViewModel</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f756c8667b34"></span><code>MainViewModel.ExportMasterDataAsync(string)</code><br>21–37 | CheckSessionUnlocked @23; ConfigureAwait @28; ExportAsync @28; DispatchToUi @29; ReferenceEquals @31; Invoke @32; SafeError @35 | No extracted literal effects. |
| <span id="m-a62e023b1fbe"></span><code>MainViewModel.MakeImportTable(string,PagedTableState&lt;ImportRowPreview&gt;,Func&lt;IReadOnlyList&lt;ImportRowPreview&gt;&gt;)</code><br>73–90 | ApplyPagedResult @75; ToArray @75; Take @75; Skip @75; rows @75; BindRefresh @76; Localize @82; ToString @83; LocalizeImportAction @85; LocalizeTable @87; Max @88; Ceiling @88 | No extracted literal effects. |
| <span id="m-85af36c6dc44"></span><code>MainViewModel.LocalizeImportAction(string)</code><br>91–97 | Localize @93; StartsWith @96 | No extracted literal effects. |
| <span id="m-d17d533504d3"></span><code>MainViewModel.RefreshImportLocalization()</code><br>98–106 | RaisePropertyChanged @100; nameof @100; ApplyPagedResult @105; ToArray @105 | No extracted literal effects. |
| <span id="m-67e05b2cdc53"></span><code>MainViewModel.SetImportReviewRows(bool,IReadOnlyList&lt;ImportRowPreview&gt;)</code><br>107–113 | ApplyPagedResult @112; ToArray @112; Take @112 | No extracted literal effects. |
| <span id="m-a6961312df05"></span><code>MainViewModel.ResetImportReviewRows(bool)</code><br>115–123 | SetImportReviewRows @118; Empty(ImportRowPreview) @118; ClearSelection @120 | No extracted literal effects. |
| <span id="m-a939bf9a6617"></span><code>MainViewModel.ResetInventoryImport()</code><br>125–138 | Clear @133; RaisePropertyChanged @136; nameof @136; ResetImportReviewRows @137 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Keyboard.cs</code> · 34 lines.

SHA-256: <code>3f8c1fb6c8e4e43dcca708d597f9ccc73afd779b4f3fd7aa376cdb08df2f1870</code>.

Declarations: <code>MainViewModel</code> (line 5).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-72bd2d6532fa"></span><code>MainViewModel.TryHandleEscapeKey()</code><br>11–33 | TryHandleEscape @15; ResetCashReview @27; Execute @30 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ProductionWorkspace.cs</code> · 666 lines.

SHA-256: <code>694ee069ad4ec0fa4ff96fb15cd42c7fe2fea297a34b0cece2b52eadea3330e6</code>.

Declarations: <code>ProductionIngredientLotDraft : ReactiveObject</code> (line 18), <code>MainViewModel</code> (line 36).

<details markdown>
<summary>Methods, calls, table effects and failures (16)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-cd3625b68ce8"></span><code>MainViewModel.InitializeManufacturingWorkspace()</code><br>190–238 | CreateFromTask @192; CreateFromTask(object) @193; OpenProductionRunByIdAsync @195; GetProductionRunDetailForActionAsync @209; CancelProductionDraftAsync @210; Create @219; Register @230; BindRefresh @231; RefreshManufacturingTablesAsync @231; BindRefresh @232; BuildManufacturingTableDefinitions @237 | No extracted literal effects. |
| <span id="m-da0f52ec4e69"></span><code>MainViewModel.GetProductionRunDetailForActionAsync(Guid)</code><br>240–248 | GetProductionRunDetailAsync @245; FirstOrDefault @247 | No extracted literal effects. |
| <span id="m-4998c32e64b6"></span><code>MainViewModel.BuildManufacturingTableDefinitions()</code><br>250–301 | ToString @257; CreateFromTask(RecipeRow) @258; OpenNewProductionByRecipeIdAsync @260; TextColumn @264; Localize @264; CreateFromTask(ProductionRunRow) @279; OpenProductionRunByIdAsync @281; ToLocalTime @285; LocalizeTable @294; Max @299; Ceiling @299 | No extracted literal effects. |
| <span id="m-90e7ad5f4118"></span><code>MainViewModel.RefreshManufacturingLocalization()</code><br>303–317 | nameof @306; RaisePropertyChanged @312; BuildManufacturingTableDefinitions @314 | No extracted literal effects. |
| <span id="m-1f0c2529e94e"></span><code>MainViewModel.RefreshManufacturingTablesAsync()</code><br>319–383 | WaitAsync @321; HasPermission @326; GetRecipesAsync @331; ToPageRequest @333; GetProductionRunsAsync @337; ToPageRequest @339; DispatchToUi @344; ApplyPagedResult @344; ApplyPagedResult @344; ToList @348; Select @348; Where @348; Join @350; Select @350; Where @353; IsNullOrWhiteSpace @355; Contains @358; Contains @359; Contains @360; Where @363; Where @367; Contains @372; Take @376; Skip @376; Skip @377; RaisePropertyChanged @379; nameof @379; SafeError @381; Release @382 | No extracted literal effects. |
| <span id="m-b5e56b205179"></span><code>MainViewModel.SetProductionActionMode(string)</code><br>385–389 | RaiseProductionStateChanged @388 | No extracted literal effects. |
| <span id="m-2c2e04a13e18"></span><code>MainViewModel.ProductionModalSnapshot()</code><br>391–403 | Join @394; ToString @397; ToString @398; ToString @399; Trim @400; Select @402 | No extracted literal effects. |
| <span id="m-ddce3957ddf0"></span><code>MainViewModel.TakeProductionSnapshot()</code><br>405–409 | ProductionModalSnapshot @407; RaiseProductionStateChanged @408 | No extracted literal effects. |
| <span id="m-d24c6ca5333e"></span><code>MainViewModel.RaiseProductionStateChanged()</code><br>421–452 | nameof @425; RaisePropertyChanged @450 | No extracted literal effects. |
| <span id="m-6822b1693082"></span><code>MainViewModel.OpenProductionRunByIdAsync(Guid,string?)</code><br>454–491 | CheckSessionUnlocked @456; GetProductionRunDetailAsync @462; GetRecipeDetailAsync @464; FirstOrDefault @468; FirstOrDefault @470; Localize @475; RecordSuccessfulSearchUseAsync @480; FromGuid @480; OpenExistingProductionAsync @490 | No extracted literal effects. |
| <span id="m-7a561a8230ca"></span><code>MainViewModel.OpenNewProductionByRecipeIdAsync(Guid)</code><br>493–514 | CheckSessionUnlocked @495; GetRecipeDetailAsync @500; FirstOrDefault @504; Localize @509; OpenProductionModal @513 | No extracted literal effects. |
| <span id="m-4c7141c6bd1b"></span><code>MainViewModel.OpenExistingProductionAsync(ProductionRunDto,string,BomDto?)</code><br>516–551 | CheckSessionUnlocked @518; FirstOrDefault @522; GetRecipeDetailAsync @526; RaisePropertyChanged @531; nameof @531; SetProductionActionMode @532; Clear @544; TakeProductionSnapshot @545; LoadProductionIngredientLotsAsync @549 | No extracted literal effects. |
| <span id="m-bf8f9621cdcf"></span><code>MainViewModel.LoadProductionIngredientLotsAsync()</code><br>553–580 | Clear @555; RaisePropertyChanged @558; nameof @558; DistinctBy @563; GetLotCandidatesAsync @565; Add @574; Add @575; SafeError @578 | No extracted literal effects. |
| <span id="m-e34bfbb97a58"></span><code>MainViewModel.SaveProductionDraftAsync()</code><br>582–608 | CheckSessionUnlocked @584; Localize @587; ExecuteAsync(CreateProductionDraftCommand, ProductionRunDto) @595; SafePipelineError @597; RecordSuccessfulSearchUseAsync @601; FromGuid @601; LoadManufacturingDataAsync @603; SafeError @606 | No extracted literal effects. |
| <span id="m-b4d12164adcf"></span><code>MainViewModel.ExecuteExistingProductionAsync()</code><br>610–646 | CheckSessionUnlocked @612; Localize @615; ExecuteAsync(StageProductionRunCommand, ProductionRunDto) @635; ToDictionary @636; Where @636; ExecuteAsync(CompleteProductionRunCommand, ProductionRunDto) @637; SafePipelineError @639; LoadManufacturingDataAsync @640; LoadInventoryAsync @641; SafeError @644 | No extracted literal effects. |
| <span id="m-a1170780e713"></span><code>MainViewModel.CancelProductionDraftAsync(ProductionRunDto)</code><br>648–665 | CheckSessionUnlocked @650; Localize @653; ExecuteAsync(CancelProductionRunCommand, bool) @659; LoadManufacturingDataAsync @660; SafePipelineError @661; SafeError @663 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Recipes.cs</code> · 230 lines.

SHA-256: <code>a745ba8f2017ad19ff76c6267bd5b1818b57b39f97b82c9cd2492c26fefa0497</code>.

Declarations: <code>RecipeIngredientDraft : ReactiveObject</code> (line 12), <code>MainViewModel</code> (line 24).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-48b502f331c1"></span><code>MainViewModel.RecipeSnapshot()</code><br>118–119 | Serialize @118; Select @119 | No extracted literal effects. |
| <span id="m-3af204c36c02"></span><code>MainViewModel.RequestCloseRecipe()</code><br>121–126 | RecipeSnapshot @124 | No extracted literal effects. |
| <span id="m-f79f6deaec4e"></span><code>MainViewModel.OpenRecipeEditorByIdAsync(Guid)</code><br>128–145 | CheckSessionUnlocked @130; GetRecipeDetailAsync @135; FirstOrDefault @139; OpenRecipeEditorAsync @143 | No extracted literal effects. |
| <span id="m-eabacf79a8c0"></span><code>MainViewModel.OpenRecipeEditorAsync(BomDto?)</code><br>147–171 | CheckSessionUnlocked @149; RaisePropertyChanged @151; nameof @151; FirstOrDefault @154; Clear @156; Add @159; Clear @162; RecipeSnapshot @164; LoadRecipeChoicesAsync @165; RecordSuccessfulSearchUseAsync @169; FromGuid @169 | No extracted literal effects. |
| <span id="m-f16c1b33119c"></span><code>MainViewModel.LoadRecipeChoicesAsync()</code><br>173–201 | ToList @180; Take @180; Where @180; Contains @180; GetPagedInventoryItemsAsync @184; Select @187; Where @187; DispatchToUi @190; Cast(InventoryItem) @193; Where @193; Append @193; Select @193; DistinctBy @194; Concat @194; Any @196; Add @196; Where @197; All @197; Remove @197; SafeError @200 | No extracted literal effects. |
| <span id="m-9804cabcbe4c"></span><code>MainViewModel.SaveRecipeAsync()</code><br>203–229 | CheckSessionUnlocked @205; IsNullOrWhiteSpace @207; Any @208; Localize @209; Count @210; Distinct @210; Select @210; ToList @218; Trim @218; ExecuteAsync(CreateBomCommand, BomDto) @221; Trim @221; ExecuteAsync(UpdateBomCommand, BomDto) @222; DispatchToUi @223; SafePipelineError @223; LoadManufacturingDataAsync @224; SafeError @227 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Search.cs</code> · 886 lines.

SHA-256: <code>3e331685ac63f8952bb6034a88195c70b197cad1f70c6791abbac4723930380f</code>.

Declarations: <code>MainViewModel</code> (line 15), <code>DelegatingSearchSuggestionReader : ISearchSuggestionReader</code> (line 861), <code>DelegatingSearchUsageWriter : ISearchUsageWriter</code> (line 874).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b0189613797b"></span><code>MainViewModel.ConfigureSearchPorts(ISearchSuggestionReader,ISearchUsageWriter?,IOperationalLogger?)</code><br>29–36 | nameof @31; Increment @34; InvalidateAllSearchScopes @35 | No extracted literal effects. |
| <span id="m-06111fca8b14"></span><code>MainViewModel.GetRealWorkspaceIdentity()</code><br>746–751 | — | No extracted literal effects. |
| <span id="m-514c8ac3fc88"></span><code>MainViewModel.CreateSearchState(SearchContext,Func&lt;object?&gt;?,Action&lt;SearchOption?&gt;?,Action&lt;string, SearchEntityKey?&gt;?,Func&lt;SearchContext&gt;?,AsyncSearchSelectionHandler?)</code><br>753–782 | Localize @772; GetRealWorkspaceIdentity @775; Add @780 | No extracted literal effects. |
| <span id="m-7c69bec7d814"></span><code>MainViewModel.RecordSuccessfulSearchUseAsync(SearchContext,SearchEntityKey,string,CancellationToken)</code><br>784–830 | IsNullOrWhiteSpace @790; CanOpenSeparateConnection @795; LogFailure @803; ConfigureAwait @816; RecordUseAsync @816 | No extracted literal effects. |
| <span id="m-7163337cd1d8"></span><code>MainViewModel.InvalidateAllSearchScopes(bool)</code><br>832–842 | Invalidate @836; TriggerSearchAsync @839 | No extracted literal effects. |
| <span id="m-eaa6e93bfcf5"></span><code>MainViewModel.ClearAllSearchStates()</code><br>844–850 | Clear @848 | No extracted literal effects. |
| <span id="m-e53de22f8ee4"></span><code>MainViewModel.DisposeSearchStates()</code><br>852–859 | Dispose @856; Clear @858 | No extracted literal effects. |
| <span id="m-4fc6f4445281"></span><code>DelegatingSearchSuggestionReader.GetSuggestionsAsync(SearchRequest,CancellationToken)</code><br>863–871 | readerSupplier @865; GetSuggestionsAsync @870 | InvalidOperationException @868 |
| <span id="m-34390c1f279b"></span><code>DelegatingSearchUsageWriter.RecordUseAsync(SearchUseRequest,CancellationToken)</code><br>876–884 | writerSupplier @878; RecordUseAsync @883 | InvalidOperationException @881 |

</details>

## MainViewModel.Tables.cs {#src-3f4385d56088}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Tables.cs</code> · 1,340 lines.

SHA-256: <code>547c4af9c2602f62c3d79802c448791e466ac07154ca3f4eb0f797daa96c2250</code>.

Declarations: <code>MainViewModel</code> (line 21).

<details markdown>
<summary>Methods, calls, table effects and failures (44)</summary>

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
| <span id="m-2ce7e046cb91"></span><code>MainViewModel.RebuildSharedDataTableDefinitions()</code><br>504–902 | CreateColumns @511; TextColumn @512; Localize @515; ToString @519; LocalizeTable @522; Max @533; Ceiling @533; CreateLifecycleStatusHeader @591; LifecycleStatusFilterToolTip @597; OpenSelectedBatchOperation @614; OpenSelectedThirdPartyBatchOperation @675; OpenSelectedRegistryBatchOperation @804; FormatCanonicalUnitFactor @862; RaisePropertyChanged @891; nameof @891; BuildSalaryTables @900; BuildExpensesTable @901 | No extracted literal effects. |
| <span id="m-c3923881f5a7"></span><code>MainViewModel.RefreshManagedCategoriesTable()</code><br>904–915 | ThenBy @909; OrderByDescending @909; OrderBy @909; ApplyLocalPage @914 | No extracted literal effects. |
| <span id="m-891a982c8a86"></span><code>MainViewModel.RefreshManagedUnitsTable()</code><br>917–931 | OrderByDescending @922; OrderBy @922; ThenBy @923; ParseCanonicalFactor @926; ApplyLocalPage @930 | No extracted literal effects. |
| <span id="m-4712608ac2aa"></span><code>MainViewModel.ApplyLocalPage(IEnumerable&lt;T&gt;,PagedTableState&lt;T&gt;)</code><br>933–942 | ToArray @935; Max @936; Ceiling @936; ApplyPagedResult @939; ToArray @940; Take @940; Skip @940 | No extracted literal effects. |
| <span id="m-722fbe4668cf"></span><code>MainViewModel.ParseCanonicalFactor(string?)</code><br>944–945 | TryParse @945 | No extracted literal effects. |
| <span id="m-6a659dae0ddc"></span><code>MainViewModel.FormatCanonicalUnitFactor(UomOption)</code><br>947–948 | IsNullOrWhiteSpace @948 | No extracted literal effects. |
| <span id="m-6167799b5be0"></span><code>MainViewModel.RefreshManagedExpenseCategoriesTable()</code><br>950–961 | OrderByDescending @955; OrderBy @955; ThenBy @956; ApplyLocalPage @960 | No extracted literal effects. |
| <span id="m-e9d98d10973a"></span><code>MainViewModel.CreateManagedCategoryStatusCell(object)</code><br>963–967 | CreateStatusToggle @966; ToggleManagedCategoryActiveAsync @966 | No extracted literal effects. |
| <span id="m-41676a393c4c"></span><code>MainViewModel.CreateManagedExpenseCategoryStatusCell(object)</code><br>969–973 | CreateStatusToggle @972; ToggleManagedExpenseCategoryActiveAsync @972 | No extracted literal effects. |
| <span id="m-ccf4a652f49b"></span><code>MainViewModel.CreateManagedUnitStatusCell(object)</code><br>975–979 | CreateStatusToggle @978; ToggleManagedUnitActiveAsync @978 | No extracted literal effects. |
| <span id="m-4acbf583857b"></span><code>MainViewModel.CreateStatusToggle(bool,Func&lt;Task&gt;)</code><br>981–994 | toggle @992 | No extracted literal effects. |
| <span id="m-b335e11afd58"></span><code>MainViewModel.CreateColumns(IReadOnlyList&lt;DataTableColumnDescriptor&gt;)</code><br>996–996 | — | No extracted literal effects. |
| <span id="m-c43507c10abe"></span><code>MainViewModel.TextColumn(string,string,Func&lt;object, string?&gt;,string?,double,double,DataTableCellStyle)</code><br>998–1008 | — | No extracted literal effects. |
| <span id="m-f01956da275f"></span><code>MainViewModel.LocalizeTable(string)</code><br>1010–1010 | Localize @1010 | No extracted literal effects. |
| <span id="m-e57a051d58ec"></span><code>MainViewModel.SelectionHeaderToolTip(bool)</code><br>1012–1013 | Localize @1012 | No extracted literal effects. |
| <span id="m-101f5996f61a"></span><code>MainViewModel.LifecycleStatusFilterToolTip(LifecycleStatusScope)</code><br>1015–1020 | Localize @1015 | No extracted literal effects. |
| <span id="m-a1ffcd8d4e6a"></span><code>MainViewModel.CreateLifecycleStatusHeader(LifecycleStatusScope)</code><br>1022–1036 | Add @1032 | No extracted literal effects. |
| <span id="m-2dcf38cae0d9"></span><code>MainViewModel.CreateInventoryLifecycleStatusCell(object)</code><br>1038–1047 | — | No extracted literal effects. |
| <span id="m-bf619cdef7c5"></span><code>MainViewModel.CreateInventoryProductCell(object)</code><br>1049–1070 | Add @1055 | No extracted literal effects. |
| <span id="m-d4939f80b6be"></span><code>MainViewModel.CreateInventoryStockCell(object)</code><br>1072–1083 | CreateInventoryTwoLineCell @1077 | No extracted literal effects. |
| <span id="m-b9de083d6160"></span><code>MainViewModel.CreateInventoryPricingCell(object)</code><br>1085–1092 | CreateInventoryTwoLineCell @1091 | No extracted literal effects. |
| <span id="m-4d94ad1cd611"></span><code>MainViewModel.CreateInventoryTwoLineCell(string,string,DataTableCellStyle,DataTableCellStyle)</code><br>1094–1112 | Add @1097; InventoryCellStyleClass @1102 | No extracted literal effects. |
| <span id="m-e6e7915735f7"></span><code>MainViewModel.InventoryCellStyleClass(DataTableCellStyle)</code><br>1114–1124 | — | No extracted literal effects. |
| <span id="m-ceec4fa19261"></span><code>MainViewModel.CreateThirdPartyStatusCell(object)</code><br>1126–1150 | Contains @1143; HasPermission @1144; SetTip @1147; RequestThirdPartyStatusChange @1148 | No extracted literal effects. |
| <span id="m-59b64b1d5b51"></span><code>MainViewModel.CreatePricingItemPriceCell(object)</code><br>1152–1229 | HasPermission @1166; nameof @1172; Cancel @1191; SaveQuickItemPriceAsync @1194; ContinueWith @1205; Delay @1205; DispatchToUi @1209; CommitChange @1209 | No extracted literal effects. |
| <span id="m-5e144bb3c185"></span><code>MainViewModel.CreatePricingItemMethodCell(object)</code><br>1231–1265 | FirstOrDefault @1237; Equals @1237; HasPermission @1244; nameof @1250; SaveQuickItemPricingMethodAsync @1261 | No extracted literal effects. |
| <span id="m-26faaceeb258"></span><code>MainViewModel.CreateThirdPartyPriceLevelCell(object)</code><br>1267–1288 | FirstOrDefault @1273; Equals @1273; HasPermission @1278; SaveThirdPartyPriceLevelAsync @1285 | No extracted literal effects. |
| <span id="m-612fd997903a"></span><code>MainViewModel.LocalizeInventoryStatus(string)</code><br>1290–1298 | Localize @1292 | No extracted literal effects. |
| <span id="m-c7966470ce03"></span><code>MainViewModel.WorkspaceScopePrefix()</code><br>1300–1300 | Join @1300 | No extracted literal effects. |
| <span id="m-0144d1004bad"></span><code>MainViewModel.NotifySelectionScopeChange(bool)</code><br>1302–1306 | Localize @1305 | No extracted literal effects. |
| <span id="m-29a347ec366c"></span><code>MainViewModel.InventorySelectionScope()</code><br>1308–1309 | Join @1308; WorkspaceScopePrefix @1308; Trim @1308; ToString @1309 | No extracted literal effects. |
| <span id="m-42024291aa0f"></span><code>MainViewModel.ThirdPartySelectionScope()</code><br>1311–1312 | Join @1311; WorkspaceScopePrefix @1311; Trim @1311; ToString @1312 | No extracted literal effects. |
| <span id="m-634eb0a6ba65"></span><code>MainViewModel.CreateInventoryToolbarButton(string,System.Windows.Input.ICommand,bool,string?)</code><br>1314–1328 | IsNullOrEmpty @1324; Add @1325 | No extracted literal effects. |
| <span id="m-2717c224a502"></span><code>MainViewModel.RefreshSharedDataTableDefinitions()</code><br>1330–1336 | RebuildSharedDataTableDefinitions @1332; BuildSalaryTables @1333; BuildExpensesTable @1334; BuildTeamsTable @1335 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdParties.cs</code> · 4,959 lines.

SHA-256: <code>f066acb1ce160fd35bdf4028cf407f455760c660ea42eaf8528bfb1e09883edc</code>.

Declarations: <code>MainViewModel</code> (line 32), <code>ThirdPartyFormSnapshot</code> (line 160), <code>ItemTierPricingRow : ReactiveObject</code> (line 4734), <code>PricingRoundingOption</code> (line 4886), <code>PricingIncrementOption</code> (line 4887), <code>PricingMethodOption</code> (line 4888), <code>PricingCostBasisOption</code> (line 4889), <code>CategoryPricingPreviewProduct</code> (line 4890), <code>TierWeightModeOption</code> (line 4894), <code>PriceOfferRow</code> (line 4896), <code>PendingShelfLabelRow : ReactiveObject</code> (line 4917), <code>KitPriceAlertRow</code> (line 4939).

<details markdown>
<summary>Methods, calls, table effects and failures (80)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f6748aa6eaea"></span><code>MainViewModel.SetThirdPartyFormValue(T,T,string?)</code><br>188–195 | Equals(T) @190; RaiseAndSetIfChanged @193; RaisePropertyChanged @194; nameof @194 | No extracted literal effects. |
| <span id="m-194379d2b2b1"></span><code>MainViewModel.CaptureThirdPartyFormSnapshot()</code><br>197–201 | — | No extracted literal effects. |
| <span id="m-cf0a11cec1ac"></span><code>MainViewModel.CaptureThirdPartyFormBaseline()</code><br>203–207 | CaptureThirdPartyFormSnapshot @205; RaisePropertyChanged @206; nameof @206 | No extracted literal effects. |
| <span id="m-a718c0780d1b"></span><code>MainViewModel.KindMatches(string?,string)</code><br>365–374 | ToLowerInvariant @367; Trim @367 | No extracted literal effects. |
| <span id="m-8730d5b4f808"></span><code>MainViewModel.CycleThirdPartyLifecycleStatusScope()</code><br>450–455 | — | No extracted literal effects. |
| <span id="m-054107065154"></span><code>MainViewModel.UpdateItemPricingCostFloorWarning()</code><br>687–715 | RaisePropertyChanged @692; nameof @692; ToMinorUnits @698; ToDisplayAmount @700; Format @705 | No extracted literal effects. |
| <span id="m-7b04423ed73f"></span><code>MainViewModel.FormatBatchPrice(long)</code><br>1031–1036 | Clamp @1033; ScalingFactor @1034; ToString @1035 | No extracted literal effects. |
| <span id="m-736f56c79b27"></span><code>MainViewModel.LocalizeBatchPricingOutcome(string)</code><br>1038–1045 | StartsWith @1040; Localize @1044 | No extracted literal effects. |
| <span id="m-cf93524f782c"></span><code>MainViewModel.InvalidateBatchPricingPreview()</code><br>1047–1059 | CancelBatchPricingPreviewExpiry @1049; RaisePropertyChanged @1054; nameof @1054 | No extracted literal effects. |
| <span id="m-19bf0c55ffe2"></span><code>MainViewModel.CurrentBatchPricingOptions()</code><br>1061–1064 | ToMinorUnits @1063; Clamp @1063 | No extracted literal effects. |
| <span id="m-acd4ba43f7d6"></span><code>MainViewModel.CurrentBatchPricingOptionsJson()</code><br>1065–1066 | OperationParametersJson @1065; CurrentBatchPricingOptions @1066 | No extracted literal effects. |
| <span id="m-14e527644ba8"></span><code>MainViewModel.CurrentSelectedBatchIdsJson()</code><br>1068–1068 | Serialize @1068; GetSelectedIdsForPreview @1068 | No extracted literal effects. |
| <span id="m-82a43e5141eb"></span><code>MainViewModel.StartBatchPricingPreviewExpiry(Guid,DateTime)</code><br>1070–1075 | CancelBatchPricingPreviewExpiry @1072; NotifyBatchPricingPreviewExpiryAsync @1074 | No extracted literal effects. |
| <span id="m-5a3a4b8db14f"></span><code>MainViewModel.CancelBatchPricingPreviewExpiry()</code><br>1077–1082 | Cancel @1079; Dispose @1080 | No extracted literal effects. |
| <span id="m-3600a45e04dd"></span><code>MainViewModel.NotifyBatchPricingPreviewExpiryAsync(Guid,DateTime,CancellationToken)</code><br>1084–1097 | ConfigureAwait @1089; Delay @1089; DispatchToUi @1090; RaisePropertyChanged @1093; nameof @1093 | No extracted literal effects. |
| <span id="m-f47143a6bbc6"></span><code>MainViewModel.KeepEditingThirdPartyForm()</code><br>1180–1180 | — | No extracted literal effects. |
| <span id="m-de1827d43384"></span><code>MainViewModel.OpenBatchPricingForSelectedItems()</code><br>1239–1250 | CheckSessionUnlocked @1241; DispatchToUi @1244; Localize @1244; InvalidateBatchPricingPreview @1248 | No extracted literal effects. |
| <span id="m-631cd59b6fcc"></span><code>MainViewModel.OpenAddThirdParty()</code><br>1280–1299 | CheckSessionUnlocked @1282; RequestCloseThirdPartyForm @1285; ClearThirdPartyForm @1288; FirstOrDefault @1291; CaptureThirdPartyFormBaseline @1298 | No extracted literal effects. |
| <span id="m-466f40d5dfe5"></span><code>MainViewModel.OpenEditThirdParty(ThirdPartyDto?)</code><br>1301–1333 | CheckSessionUnlocked @1303; IsNullOrWhiteSpace @1309; FirstOrDefault @1322; FirstOrDefault @1324; CaptureThirdPartyFormBaseline @1332 | No extracted literal effects. |
| <span id="m-8e4cfa8a9ada"></span><code>MainViewModel.RequestThirdPartyStatusChange(ThirdPartyDto?)</code><br>1335–1348 | Contains @1338; CheckSessionUnlocked @1339; HasPermission @1340; RaisePropertyChanged @1344; nameof @1344 | No extracted literal effects. |
| <span id="m-d8be7b266f5d"></span><code>MainViewModel.ConfirmThirdPartyStatusChangeAsync()</code><br>1350–1374 | Add @1353; CancelThirdPartyStatusChange @1355; RefreshSharedDataTableDefinitions @1356; RaisePropertyChanged @1357; nameof @1357; ConfigureAwait @1361; ReactivateThirdPartyAsync @1361; DeactivateThirdPartyAsync @1363; Remove @1367; DispatchToUi @1368 | No extracted literal effects. |
| <span id="m-50723d9d4dfa"></span><code>MainViewModel.CancelThirdPartyStatusChange()</code><br>1376–1383 | RaisePropertyChanged @1380; nameof @1380 | No extracted literal effects. |
| <span id="m-be3d2380f3b7"></span><code>MainViewModel.SaveThirdPartyPriceLevelAsync(ThirdPartyDto,string,ComboBox?)</code><br>1385–1421 | IsNullOrWhiteSpace @1388; Equals @1389; Add @1390; CheckSessionUnlocked @1392; Remove @1394; FirstOrDefault @1395; ConfigureAwait(SetThirdPartyPriceLevelCommand, bool) @1403; ExecuteAsync(SetThirdPartyPriceLevelCommand, bool) @1403; DispatchToUi @1406; SafePipelineError @1406; Localize @1408; SafeError @1412; ConfigureAwait @1417; LoadThirdPartiesAsync @1417; HasPermission @1419 | No extracted literal effects. |
| <span id="m-9329f194d614"></span><code>MainViewModel.SaveQuickItemPriceAsync(InventoryItem,decimal,NumericUpDown?)</code><br>1425–1509 | Add @1427; CheckSessionUnlocked @1430; Remove @1432; ToMinorUnits @1439; CreateCommand @1444; AddSqlParam @1446; ToString @1446; ConfigureAwait @1447; ExecuteReaderAsync @1447; ReadAsync @1448; GetString @1450; IsDBNull @1451; GetDecimal @1452; GetInt64 @1453; Add @1454; ConfigureAwait(SaveItemPricingCommand, bool) @1472; ExecuteAsync(SaveItemPricingCommand, bool) @1472; DispatchToUi @1475; UpdateTierRowsBasePrice @1483; SafePipelineError @1493; SafeError @1502 | FROM item_price_levels @1445 |
| <span id="m-3f312eac6ca0"></span><code>MainViewModel.SaveQuickItemPricingMethodAsync(InventoryItem,string,ComboBox?)</code><br>1511–1637 | IsNullOrWhiteSpace @1513; Add @1513; CheckSessionUnlocked @1516; Remove @1518; FirstOrDefault @1520; Equals @1520; ToMinorUnits @1526; CreateCommand @1534; AddSqlParam @1536; ToString @1536; ConfigureAwait @1537; ExecuteReaderAsync @1537; ReadAsync @1538; IsDBNull @1540; TryParse @1540; GetString @1540; GetInt64 @1543; ExecuteReaderAsync @1558; ReadAsync @1559; GetString @1561; IsDBNull @1562; GetDecimal @1563; GetInt64 @1564; Add @1565; ConfigureAwait(SaveItemPricingCommand, bool) @1585; ExecuteAsync(SaveItemPricingCommand, bool) @1585; ExecuteScalarAsync @1594; ToInt64 @1596; ToDisplayAmount @1600; DispatchToUi @1601; UpdateTierRowsBasePrice @1609; SafePipelineError @1620; SafeError @1630 | FROM item_price_levels @1556; FROM item_pricing @1535; FROM items @1592 |
| <span id="m-99001fbfccc3"></span><code>MainViewModel.RequestCloseThirdPartyForm()</code><br>1639–1654 | CloseThirdPartyForm @1653 | No extracted literal effects. |
| <span id="m-a2ab58dba836"></span><code>MainViewModel.ConfirmDiscardThirdPartyForm()</code><br>1656–1660 | CloseThirdPartyForm @1659 | No extracted literal effects. |
| <span id="m-0c42b31b8b22"></span><code>MainViewModel.CloseThirdPartyForm()</code><br>1662–1671 | ClearThirdPartyForm @1669; RaisePropertyChanged @1670; nameof @1670 | No extracted literal effects. |
| <span id="m-240444abb07c"></span><code>MainViewModel.OpenThirdPartiesWorkspace(string?)</code><br>1677–1692 | CheckSessionUnlocked @1679; SelectMenu @1683; IsNullOrWhiteSpace @1686; ResetToFirstPage @1689; LoadThirdPartiesAsync @1690 | No extracted literal effects. |
| <span id="m-b4d691e44db1"></span><code>MainViewModel.OpenEditPartyFromChooserAsync(CustomerDto?)</code><br>1700–1722 | CloseCustomerChooser @1704; SelectMenu @1708; ConfigureAwait @1711; LoadThirdPartiesAsync @1711; FirstOrDefault @1713; DispatchToUi @1721; OpenEditThirdParty @1721 | No extracted literal effects. |
| <span id="m-fc68d5f3f52b"></span><code>MainViewModel.ClearThirdPartyForm()</code><br>1724–1745 | — | No extracted literal effects. |
| <span id="m-719a84f2a818"></span><code>MainViewModel.ConfirmSaveThirdPartyAsync()</code><br>1747–1821 | IsNullOrWhiteSpace @1749; NormalizeDbValue @1764; Trim @1770; NullIfBlank @1771; FirstOrDefault @1776; ConfigureAwait(UpdateThirdPartyCommand, ThirdPartyDto) @1781; ExecuteAsync(UpdateThirdPartyCommand, ThirdPartyDto) @1781; DispatchToUi @1784; SafePipelineError @1784; ConfigureAwait(CreateThirdPartyCommand, ThirdPartyDto) @1801; ExecuteAsync(CreateThirdPartyCommand, ThirdPartyDto) @1801; ConfigureAwait @1809; LoadThirdPartiesAsync @1809; LoadThirdPartiesLegacyListsAsync @1810; CloseThirdPartyForm @1813; SafeError @1819 | No extracted literal effects. |
| <span id="m-c9f07dc9b8b9"></span><code>MainViewModel.DeactivateThirdPartyAsync(Guid)</code><br>1823–1855 | CheckSessionUnlocked @1825; ConfigureAwait(DeactivateThirdPartyCommand, bool) @1836; ExecuteAsync(DeactivateThirdPartyCommand, bool) @1836; DispatchToUi @1839; SafePipelineError @1839; ConfigureAwait @1843; LoadThirdPartiesAsync @1843; LoadThirdPartiesLegacyListsAsync @1844; SafeError @1853 | No extracted literal effects. |
| <span id="m-80f4cdb808d6"></span><code>MainViewModel.LoadThirdPartiesAsync()</code><br>1860–1890 | HasPermission @1863; Increment @1864; ConfigureAwait @1867; GetPagedThirdPartiesAsync @1867; ToPageRequest @1869; DispatchToUi @1877; Read @1879; Clear @1880; AddRange @1881; ApplyPagedResult @1882; RefreshThirdPartyList @1883; SafeError @1888 | No extracted literal effects. |
| <span id="m-8b7528160aed"></span><code>MainViewModel.LoadThirdPartiesLegacyListsAsync()</code><br>1893–1897 | ConfigureAwait @1895; LoadCustomersAsync @1895; LoadSuppliersAsync @1896 | No extracted literal effects. |
| <span id="m-03cb155d34a9"></span><code>MainViewModel.LoadPriceLevelSettingsAsync()</code><br>1899–1968 | CreateCommand @1906; ConfigureAwait @1909; ExecuteScalarAsync @1909; ToInt32 @1912; ExecuteReaderAsync @1919; ReadAsync @1920; ParseStoredPercentage @1922; IsDBNull @1922; GetString @1922; GetInt32 @1922; ToString @1923; Add @1924; DispatchToUi @1934; Clear @1938; Clear @1939; Clear @1940; Add @1943; Add @1946; Add @1947; Any @1951; FirstOrDefault @1956; BuildItemTierRows @1961; SafeError @1966 | FROM price_level_settings @1918; FROM store_config @1908 |
| <span id="m-d5e504254913"></span><code>MainViewModel.LoadPriceProposalsAsync()</code><br>1970–2066 | Increment @1973; ConfigureAwait @1974; WaitAsync @1974; CreateCommand @1978; ToInt32 @1981; ExecuteScalarAsync @1981; Max @1985; Ceiling @1985; Min @1986; ToLowerInvariant @1988; IsNullOrWhiteSpace @1997; AddSqlParam @2012; ExecuteReaderAsync @2014; ReadAsync @2015; IsDBNull @2017; GetString @2017; TryParse @2024; Localize @2026; Format @2027; ScalingFactor @2028; Add @2031; ParseGuidSafe @2032; GetInt64 @2034; ParseDate @2038; Read @2044; DispatchToUi @2046; ApplyPagedResult @2049; Clear @2050; Add @2053; SafeError @2060; Release @2064 | FROM price_change_proposals @1980 · DYNAMIC SQL: inspect manually |
| <span id="m-d14f9cd224ae"></span><code>MainViewModel.SavePriceTierSettingsAsync()</code><br>2068–2110 | TryParse @2081; DispatchToUi @2084; Localize @2084; Add @2087; ToString @2090; ConfigureAwait(UpdatePriceTierSettingsCommand, bool) @2095; ExecuteAsync(UpdatePriceTierSettingsCommand, bool) @2095; SafePipelineError @2098; ConfigureAwait @2102; LoadPriceLevelSettingsAsync @2102; SafeError @2108 | No extracted literal effects. |
| <span id="m-afe8c24f2058"></span><code>MainViewModel.ResolveProposalAsync(string?,bool)</code><br>2112–2144 | TryParse @2114; ConfigureAwait(ResolvePriceChangeProposalCommand, bool) @2123; ExecuteAsync(ResolvePriceChangeProposalCommand, bool) @2123; DispatchToUi @2126; SafePipelineError @2126; ConfigureAwait @2132; LoadPriceProposalsAsync @2132; Localize @2133; SafeError @2142 | No extracted literal effects. |
| <span id="m-4f502c704d1c"></span><code>MainViewModel.LoadItemPricingAsync(InventoryItem?)</code><br>2150–2264 | Increment @2152; DispatchToUi @2155; RaisePropertyChanged @2158; nameof @2158; ToString @2164; CreateCommand @2167; CreateParameter @2174; Add @2174; ConfigureAwait @2175; ExecuteReaderAsync @2175; ReadAsync @2176; IsDBNull @2178; GetString @2178; GetInt32 @2179; ParseStoredPricingPercentForDisplay @2180; GetInt64 @2184; ToDisplayAmount @2197; IsIncrementRoundingRule @2199; CalculateAsync @2209; BuildItemTierRows @2235; GetEffectiveTier1BasePrice @2237; TryGetValue @2242; RecalculateEffectivePrice @2254; SafeError @2262 | FROM item_price_levels @2216; FROM item_pricing @2169 |
| <span id="m-f4780ed8843c"></span><code>MainViewModel.GetEffectiveTier1BasePrice()</code><br>2268–2293 | ToDisplayAmount @2276; Round @2282 | No extracted literal effects. |
| <span id="m-c0e8b8daea0b"></span><code>MainViewModel.UpdateTierRowsBasePrice()</code><br>2297–2308 | GetEffectiveTier1BasePrice @2299; RecalculateEffectivePrice @2304; RaisePropertyChanged @2306; nameof @2306 | No extracted literal effects. |
| <span id="m-e381c5be42ad"></span><code>MainViewModel.BuildItemTierRows(IEnumerable&lt;PriceLevelSettingDto&gt;)</code><br>2310–2337 | ToList @2312; OrderBy @2312; Where @2312; SequenceEqual @2314; Select @2314; Select @2314; UpdateTierRowsBasePrice @2316; Clear @2320; GetEffectiveTier1BasePrice @2321; RecalculateEffectivePrice @2332; Add @2333; RaisePropertyChanged @2335; nameof @2335 | No extracted literal effects. |
| <span id="m-d6b1fa6eb118"></span><code>MainViewModel.SaveItemPricingAsync()</code><br>2339–2392 | Add @2364; ToCommand @2374; ConfigureAwait(SaveItemPricingCommand, bool) @2377; ExecuteAsync(SaveItemPricingCommand, bool) @2377; DispatchToUi @2381; SafePipelineError @2381; SafeError @2390 | No extracted literal effects. |
| <span id="m-b131ec36d554"></span><code>MainViewModel.CreateBatchPricingPreviewAsync()</code><br>2394–2452 | Localize @2405; DispatchToUi @2411; InvalidateBatchPricingPreview @2411; GetSelectedIdsForPreview @2412; CurrentBatchPricingOptions @2422; ConfigureAwait(CreateBatchPreviewCommand, BatchPreviewResult) @2423; ExecuteAsync(CreateBatchPreviewCommand, BatchPreviewResult) @2423; CurrentBatchPricingOptionsJson @2430; Serialize @2432; StartBatchPricingPreviewExpiry @2434; RaisePropertyChanged @2435; nameof @2435; SafePipelineError @2441; SafeError @2446 | No extracted literal effects. |
| <span id="m-b2eec7c059a6"></span><code>MainViewModel.LoadCategoryPricingRuleAsync(ProductCategoryOption?)</code><br>2454–2541 | Equals @2456; DispatchToUi @2458; Clear @2461; CreateCommand @2471; AddSqlParam @2477; ToString @2477; ConfigureAwait @2478; ExecuteReaderAsync @2478; ReadAsync @2479; ParseGuidSafe @2482; GetString @2482; GetInt32 @2482; GetInt64 @2483; IsDBNull @2484; ParseDate @2485; Add @2501; Add @2511; TryParse @2525; ToDisplayAmount @2527; FirstOrDefault @2532; SafeError @2539 | FROM item_kits @2492; FROM items @2492; FROM product_category_pricing_rules @2473 |
| <span id="m-36c4e0c5136a"></span><code>MainViewModel.PreviewCategoryPricingRuleAsync()</code><br>2543–2635 | Localize @2547; ParseRoundingRule @2555; IsRoundingRuleCompatible @2556; TryConvertRoundingIncrement @2558; ConfigureAwait @2568; CalculateAsync @2568; CreateCommand @2580; AddSqlParam @2585; ToString @2585; ExecuteReaderAsync @2586; ReadAsync @2587; GetInt64 @2593; IsDBNull @2596; DisposeAsync @2611; SetCategoryPricingPreviewAsync @2618; ToInt64 @2627; ExecuteScalarAsync @2627; DispatchToUi @2633; SafeError @2633 | FROM items @2581; FROM items @2625; JOIN item_pricing @2581; JOIN item_pricing @2625 |
| <span id="m-2b18a4cbc5c7"></span><code>MainViewModel.SetCategoryPricingPreviewAsync(decimal,long,string,RoundingRule,long,int)</code><br>2637–2669 | ParsePricingMethod @2641; ToMinorUnits @2643; CalculateUnroundedBasePriceMinor @2645; ResolveEffectiveBasePrice @2646; ScalingFactor @2648; FormatPricingCandidate @2649; Format @2651; ToDisplayAmount @2651; Abs @2655; FirstOrDefault @2656; Localize @2659; DispatchToUi @2665; ToString @2667 | No extracted literal effects. |
| <span id="m-6fed7b77c1bd"></span><code>MainViewModel.FormatPricingCandidate(decimal,int)</code><br>2671–2677 | ScalingFactor @2673; Min @2674; ToString @2675; ToString @2676 | No extracted literal effects. |
| <span id="m-309b9a163cf6"></span><code>MainViewModel.SaveCategoryPricingRuleAsync()</code><br>2679–2717 | Localize @2683; ToMinorUnits @2697; ConfigureAwait(SaveCategoryPricingRuleCommand, CategoryPricingRuleSaveResult) @2700; ExecuteAsync(SaveCategoryPricingRuleCommand, CategoryPricingRuleSaveResult) @2700; DispatchToUi @2704; SafePipelineError @2704; ConfigureAwait @2708; LoadCategoryPricingRuleAsync @2708; LoadPriceProposalsAsync @2709; SafeError @2715 | No extracted literal effects. |
| <span id="m-d54b26877078"></span><code>MainViewModel.DeactivateCategoryPricingRuleAsync()</code><br>2719–2740 | ConfigureAwait(DeactivateCategoryPricingRuleCommand, bool) @2724; ExecuteAsync(DeactivateCategoryPricingRuleCommand, bool) @2724; DispatchToUi @2729; SafePipelineError @2729; ConfigureAwait @2732; LoadCategoryPricingRuleAsync @2732; LoadPriceProposalsAsync @2733; Localize @2734; SafeError @2738 | No extracted literal effects. |
| <span id="m-36257c906fdb"></span><code>MainViewModel.LoadKitComponentCostPreviewAsync(InventoryItem,string)</code><br>2742–2769 | ConfigureAwait @2751; CalculateAsync @2751; DispatchToUi @2753; Equals @2756; RaisePropertyChanged @2762; nameof @2762; SafeError @2767 | No extracted literal effects. |
| <span id="m-78c18bd48f54"></span><code>MainViewModel.FormatKitComponentCostPreview(KitComponentCostResult)</code><br>2771–2787 | Localize @2773; ScalingFactor @2778; Format @2779; Select @2780; ToString @2781; FormatMinor @2781; Join @2785 | No extracted literal effects. |
| <span id="m-4e4def32de4f"></span><code>MainViewModel.ReactivateThirdPartyAsync(Guid)</code><br>2789–2815 | CheckSessionUnlocked @2791; ConfigureAwait(ReactivateThirdPartyCommand, bool) @2796; ExecuteAsync(ReactivateThirdPartyCommand, bool) @2796; DispatchToUi @2800; SafePipelineError @2800; ConfigureAwait @2803; LoadThirdPartiesAsync @2803; LoadThirdPartiesLegacyListsAsync @2804; SafeError @2813 | No extracted literal effects. |
| <span id="m-747823c918ae"></span><code>MainViewModel.ConfirmBatchPricingAsync()</code><br>2821–2860 | DispatchToUi @2825; Localize @2825; CurrentBatchPricingOptions @2831; ConfigureAwait(ApplyBatchPricingCommand, BatchPricingResult) @2836; ExecuteAsync(ApplyBatchPricingCommand, BatchPricingResult) @2836; ToString @2837; InvalidateBatchPricingPreview @2840; ConfigureAwait @2841; LoadInventoryAsync @2841; LoadPriceProposalsAsync @2842; SafePipelineError @2849; SafeError @2854 | No extracted literal effects. |
| <span id="m-eaeebd5e5e50"></span><code>MainViewModel.RequestElevationForCheckout(string?)</code><br>2865–2880 | Clear @2867; DistinctBy @2868; Where @2868; GetUnlockCandidates @2868; Equals @2869; Add @2873; Localize @2877 | No extracted literal effects. |
| <span id="m-9f34fb1d4efa"></span><code>MainViewModel.CancelElevation()</code><br>2882–2889 | — | No extracted literal effects. |
| <span id="m-f76360a1c493"></span><code>MainViewModel.ConfirmElevationAsync()</code><br>2891–2935 | Localize @2896; IsNullOrWhiteSpace @2900; AuthenticateSelectedUser @2908; Trim @2908; Any @2909; Equals @2909; Contains @2912; HasPermission @2915; ConfigureAwait @2929; PlaceOrderAsync @2929; SafeError @2933 | No extracted literal effects. |
| <span id="m-ad41b4bd6089"></span><code>MainViewModel.FormatCartSummaryNumber(decimal)</code><br>3120–3127 | Clamp @3125; ToString @3126 | No extracted literal effects. |
| <span id="m-1b36a9384f66"></span><code>MainViewModel.Localize(string,object?[])</code><br>3598–3598 | Localize @3598 | No extracted literal effects. |
| <span id="m-9612e46fd956"></span><code>MainViewModel.RaiseLocalizedLabels()</code><br>3604–4361 | RaiseCatalogLabels @3606; RaisePropertyChanged @3607; nameof @3607; RefreshManufacturingLocalization @4112; RefreshTraceabilityLocalization @4113; RefreshCommercialLocalization @4114; RefreshImportLocalization @4115 | No extracted literal effects. |
| <span id="m-571a399bec24"></span><code>MainViewModel.RefreshThirdPartyList()</code><br>4366–4373 | Clear @4368; Add @4371 | No extracted literal effects. |
| <span id="m-55b4708b0923"></span><code>MainViewModel.NullIfBlank(string?)</code><br>4375–4375 | IsNullOrWhiteSpace @4375; Trim @4375 | No extracted literal effects. |
| <span id="m-ec8a3349b146"></span><code>MainViewModel.ParsePercent(string?)</code><br>4377–4378 | TryParse @4378 | No extracted literal effects. |
| <span id="m-c1944734c44f"></span><code>MainViewModel.ParseStoredPricingPercentForDisplay(string?,int)</code><br>4380–4381 | ParseStoredPercentage @4381 | No extracted literal effects. |
| <span id="m-fc5ecfb89324"></span><code>MainViewModel.IsIncrementRoundingRule(string?)</code><br>4383–4385 | Equals @4384 | No extracted literal effects. |
| <span id="m-b174308323e8"></span><code>MainViewModel.ParseDate(string?)</code><br>4387–4388 | TryParse @4388 | No extracted literal effects. |
| <span id="m-c471b14500aa"></span><code>MainViewModel.OpenNewPriceOffer()</code><br>4486–4496 | ToString @4490; ToString @4491; AddDays @4491; FirstOrDefault @4493 | No extracted literal effects. |
| <span id="m-fb8bc44b6639"></span><code>MainViewModel.OpenEditPriceOfferAsync(PriceOfferRow)</code><br>4498–4521 | CreateCommand @4501; CreateParameter @4504; ToString @4504; Add @4504; ConfigureAwait @4505; ExecuteReaderAsync @4505; ReadAsync @4505; Parse @4506; GetString @4506; GetInt32 @4506; IsDBNull @4508; TryParse @4508; ToString @4508; ToUniversalTime @4508; ToString @4508; ToUniversalTime @4509; AddDays @4509; FirstOrDefault @4511; TryParse @4513; FirstOrDefault @4514; Pow @4517; GetInt64 @4518 | FROM price_offers @4501; JOIN items @4501 |
| <span id="m-66783bc9e623"></span><code>MainViewModel.SavePriceOfferAsync()</code><br>4523–4540 | CheckSessionUnlocked @4525; TryParse @4526; ToString @4526; Round @4526; Pow @4526; IsNullOrWhiteSpace @4527; ConfigureAwait(SavePriceOfferCommand, Guid) @4536; ExecuteAsync(SavePriceOfferCommand, Guid) @4536; ReportError @4537; DispatchToUi @4538; ConfigureAwait @4539; LoadPriceOffersAsync @4539 | No extracted literal effects. |
| <span id="m-c8384bbd9843"></span><code>MainViewModel.TogglePriceOfferAsync(PriceOfferRow)</code><br>4542–4550 | CheckSessionUnlocked @4544; ConfigureAwait(SetPriceOfferStatusCommand, bool) @4546; ExecuteAsync(SetPriceOfferStatusCommand, bool) @4546; ReportError @4548; ConfigureAwait @4549; LoadPriceOffersAsync @4549 | No extracted literal effects. |
| <span id="m-54516bbdd9dc"></span><code>MainViewModel.LoadPriceOffersAsync()</code><br>4552–4591 | CreateCommand @4557; ConfigureAwait @4567; ExecuteReaderAsync @4567; ReadAsync @4568; Add @4570; Parse @4571; GetString @4571; GetDouble @4575; GetInt64 @4578; IsDBNull @4579; GetInt32 @4581; DispatchToUi @4584; Clear @4586; Add @4587 | FROM price_offers @4558; JOIN items @4558; JOIN product_categories @4558 |
| <span id="m-de4fe36b0e7c"></span><code>MainViewModel.LoadPendingShelfLabelsAsync()</code><br>4593–4632 | CreateCommand @4598; ConfigureAwait @4607; ExecuteReaderAsync @4607; ReadAsync @4608; Add @4610; Parse @4611; GetString @4611; GetInt64 @4615; GetInt32 @4620; Add @4621; Remove @4621; RaisePropertyChanged @4621; nameof @4621; Localize @4622; DispatchToUi @4625; Clear @4627; Add @4628 | FROM pending_shelf_labels @4599; JOIN items @4599 |
| <span id="m-47630b4bec1a"></span><code>MainViewModel.LoadKitPriceReviewAlertsAsync()</code><br>4634–4673 | CreateCommand @4639; ConfigureAwait @4651; ExecuteReaderAsync @4651; ReadAsync @4652; Add @4654; Parse @4655; GetString @4655; GetInt64 @4659; GetInt32 @4663; DispatchToUi @4666; Clear @4668; Add @4669 | FROM kit_price_review_alerts @4640; JOIN items @4640 |
| <span id="m-423505c018dd"></span><code>MainViewModel.SetKitPriceAlertStatusAsync(KitPriceAlertRow,string,string)</code><br>4675–4683 | CheckSessionUnlocked @4677; ConfigureAwait(ResolveKitPriceAlertCommand, bool) @4678; ExecuteAsync(ResolveKitPriceAlertCommand, bool) @4678; ReportError @4680; ConfigureAwait @4682; LoadKitPriceReviewAlertsAsync @4682 | No extracted literal effects. |
| <span id="m-c0427163079b"></span><code>MainViewModel.MarkShelfLabelsPrintedAsync()</code><br>4685–4688 | ConfigureAwait @4687; SetSelectedShelfLabelStatusAsync @4687 | No extracted literal effects. |
| <span id="m-85100b56be6a"></span><code>MainViewModel.QueueSelectedShelfLabelsAsync()</code><br>4690–4702 | CheckSessionUnlocked @4692; ToArray @4693; Select @4693; Where @4693; Contains @4693; ConfigureAwait(QueueShelfLabelPrintCommand, string) @4696; ExecuteAsync(QueueShelfLabelPrintCommand, string) @4696; ReportError @4698; Clear @4699; RaisePropertyChanged @4699; nameof @4699; ConfigureAwait @4701; LoadPendingShelfLabelsAsync @4701 | No extracted literal effects. |
| <span id="m-aa4af2ec8d1a"></span><code>MainViewModel.SetSelectedShelfLabelStatusAsync(string)</code><br>4704–4718 | CheckSessionUnlocked @4706; ToArray @4707; Select @4707; Where @4707; Contains @4707; ConfigureAwait(SetShelfLabelStatusCommand, int) @4710; ExecuteAsync(SetShelfLabelStatusCommand, int) @4710; Trim @4711; ReportError @4713; Clear @4714; RaisePropertyChanged @4715; nameof @4715; ConfigureAwait @4717; LoadPendingShelfLabelsAsync @4717 | No extracted literal effects. |
| <span id="m-80339b0f0013"></span><code>MainViewModel.AddSqlParam(DbCommand,string,object)</code><br>4724–4730 | CreateParameter @4726; Add @4729 | No extracted literal effects. |
| <span id="m-c5b6f39b7eb8"></span><code>ItemTierPricingRow.RecalculateEffectivePrice()</code><br>4862–4883 | Max @4867; TryParse @4876 | No extracted literal effects. |

</details>

## MainViewModel.ThirdPartyImport.cs {#src-63148b75a5e2}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdPartyImport.cs</code> · 276 lines.

SHA-256: <code>36b3834cae4664089ae8d554018568e7bd3c871b43310cee711aed1806b2351e</code>.

Declarations: <code>MainViewModel</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-1f14c7360e7b"></span><code>MainViewModel.OpenThirdPartyImport()</code><br>116–130 | CheckSessionUnlocked @118; Increment @125; ResetThirdPartyImport @127; Invoke @129 | No extracted literal effects. |
| <span id="m-9fb52a37592b"></span><code>MainViewModel.PreviewThirdPartyImportFileAsync(string)</code><br>132–197 | Increment @135; ResetThirdPartyImport @139; IsNullOrWhiteSpace @143; Exists @143; FinishFailedImport @145; ConfigureAwait @156; ReadAllBytesAsync @156; ToHexStringLower @157; HashData @157; ReadThirdPartiesAsync @158; ValidateThirdPartiesAsync @165; TemplateContextAsync @166; CompletedWorkbook @167; DispatchToUi @174; ReferenceEquals @176; SetImportReviewRows @177; ToArray @177; Select @177; Clear @182; Add @183; Clear @184; Add @185; RaisePropertyChanged @186; nameof @186; Localize @187; ReportException @193 | No extracted literal effects. |
| <span id="m-3ac09fe71005"></span><code>MainViewModel.ConfirmThirdPartyImportAsync()</code><br>199–250 | IsCurrentImportAttempt @214; ConfigureAwait(ImportThirdPartiesCommand, ImportThirdPartiesResult) @220; ExecuteAsync(ImportThirdPartiesCommand, ImportThirdPartiesResult) @220; ConfigureAwait @225; RecoverImportOutcomeAsync @225; ReportError @228; FinishFailedImport @229; ImportCommandIssue @229; Localize @234; DispatchToUi @236; FinishImportAttempt @236; LoadThirdPartiesAsync @239; LoadThirdPartiesLegacyListsAsync @240; ReportException @242 | No extracted literal effects. |
| <span id="m-03522eb30c1c"></span><code>MainViewModel.CancelThirdPartyImport()</code><br>252–258 | ResetThirdPartyImport @257 | No extracted literal effects. |
| <span id="m-5bb1f624d4d5"></span><code>MainViewModel.ResetThirdPartyImport()</code><br>260–273 | Clear @269; Clear @270; ResetImportReviewRows @271; RaisePropertyChanged @272; nameof @272 | No extracted literal effects. |

</details>

## MainViewModel.cs {#src-16497b924a99}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 13,638 lines.

SHA-256: <code>55ce18f6f90d7d62619d0a809487e8bf4e062cced5df83ba355a481d2550d628</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 8936).

<details markdown>
<summary>Methods, calls, table effects and failures (259)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4d3c549b9d46"></span><code>MainViewModel.RefreshCurrentTime()</code><br>121–121 | RaisePropertyChanged @121; nameof @121 | No extracted literal effects. |
| <span id="m-7788c0d90846"></span><code>MainViewModel.SetStatusNotificationOnUi(string)</code><br>393–406 | RaiseAndSetIfChanged @395; IsNullOrWhiteSpace @396; Insert @398; RemoveAt @399; RaisePropertyChanged @400; nameof @400; Stop @403; Start @405 | No extracted literal effects. |
| <span id="m-62986d2b2ad3"></span><code>MainViewModel.ClearNotifications()</code><br>428–435 | Stop @430; Clear @432; RaisePropertyChanged @433; nameof @433; RaiseAndSetIfChanged @434 | No extracted literal effects. |
| <span id="m-4bff130f3985"></span><code>MainViewModel.CycleInventoryLifecycleStatusScope()</code><br>693–698 | — | No extracted literal effects. |
| <span id="m-d9c459b4bdf6"></span><code>MainViewModel.IsLockScreenLockedOut(int)</code><br>1212–1228 | Ceiling @1219 | No extracted literal effects. |
| <span id="m-ae6ca81d08b6"></span><code>MainViewModel.RefreshUnlockCandidates()</code><br>1270–1295 | GetUnlockCandidates @1273; Clear @1276; Add @1279; Any @1281; CheckAccess @1287; action @1289; Post @1293 | No extracted literal effects. |
| <span id="m-1e3f0fa04d83"></span><code>MainViewModel.UpdateReceiveKitBreakdownAsync()</code><br>1653–1673 | GetValueOrDefault @1661; ConfigureAwait @1666; BuildBreakdownSummaryAsync @1666 | No extracted literal effects. |
| <span id="m-855da3fdf66d"></span><code>MainViewModel.UpdateCartKitBreakdownAsync(OrderItem)</code><br>1675–1687 | ConfigureAwait @1680; BuildBreakdownSummaryAsync @1680 | No extracted literal effects. |
| <span id="m-b3d121c33d77"></span><code>MainViewModel.OnProductPricingDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>2157–2176 | RaisePropertyChanged @2159; nameof @2159; RecomputeProductPricingPreview @2175 | No extracted literal effects. |
| <span id="m-394fe8f30a41"></span><code>MainViewModel.RecomputeProductPricingPreview()</code><br>2185–2235 | Clear @2187; RaisePropertyChanged @2188; nameof @2188; ToMinorUnits @2197; Parse @2202; TryParse @2206; Equals @2220; Increment @2223; Localize @2224; ToArray @2226; RecomputeKitPricingPreviewAsync @2227; ResolveSelectedProductSaleUnitFactor @2232; Round @2233; RebuildProductPricingPreview @2234 | No extracted literal effects. |
| <span id="m-55751151d3f2"></span><code>MainViewModel.RecomputeKitPricingPreviewAsync(long,string,string,decimal,string,long,decimal,IReadOnlyList&lt;KitComponentDraftItem&gt;)</code><br>2237–2307 | ConfigureAwait @2241; WaitAsync @2241; Read @2244; DispatchToUi @2248; SetProductPricingPreviewNotice @2248; CalculateItemOrKitAsync @2262; ResolveSelectedProductSaleUnitFactor @2286; Round @2287; RebuildProductPricingPreview @2291; Release @2305 | No extracted literal effects. |
| <span id="m-d11dc8722d03"></span><code>MainViewModel.SetProductPricingPreviewNotice(string)</code><br>2309–2313 | Localize @2311; RaisePropertyChanged @2312; nameof @2312 | No extracted literal effects. |
| <span id="m-a8b32d68cf53"></span><code>MainViewModel.RebuildProductPricingPreview(long,string,decimal,string,long,decimal)</code><br>2315–2379 | Clear @2318; RaisePropertyChanged @2320; nameof @2320; Equals @2321; SetProductPricingPreviewNotice @2323; ParsePricingMethod @2327; ParseRoundingRule @2328; IsRoundingRuleCompatible @2329; TryConvertRoundingIncrement @2336; ToMinorUnits @2343; ResolveEffectiveBasePrice @2344; ToList @2348; OrderBy @2348; Where @2348; FirstOrDefault @2355; TryParse @2366; ToString @2367; ResolveTierPrice @2370; Add @2372; Format @2374; ToDisplayAmount @2374; FirstOrDefault @2375 | No extracted literal effects. |
| <span id="m-5626fa604f40"></span><code>MainViewModel.ResolveSelectedProductSaleUnitFactor()</code><br>2433–2448 | FirstOrDefault @2436; Equals @2436; TryParse @2440 | No extracted literal effects. |
| <span id="m-48e87a4499bd"></span><code>MainViewModel.ExactMinorToCurrency(decimal)</code><br>2456–2457 | ScalingFactor @2457; Clamp @2457 | No extracted literal effects. |
| <span id="m-60a1375347b3"></span><code>MainViewModel.BuildCostSourcesTooltip(long,long,long,long?,string,DateTime?)</code><br>2514–2534 | Format @2522; ToDecimal @2523; Localize @2526; Format @2526; ToLocalTime @2528; Join @2533 | No extracted literal effects. |
| <span id="m-937783aba33c"></span><code>MainViewModel.AddKitComponent()</code><br>2694–2731 | IsNullOrWhiteSpace @2709; FirstOrDefault @2711; Equals @2712; Add @2719; RaisePropertyChanged @2730; nameof @2730 | No extracted literal effects. |
| <span id="m-b2fe9a77a577"></span><code>MainViewModel.RemoveKitComponent(KitComponentDraftItem?)</code><br>2733–2740 | Remove @2737; RaisePropertyChanged @2738; nameof @2738 | No extracted literal effects. |
| <span id="m-dc9d44304e1d"></span><code>MainViewModel.RefreshVirtualKitAvailability()</code><br>2751–2764 | Increment @2753; ToArray @2760; Select @2760; LoadVirtualKitAvailabilityAsync @2763 | No extracted literal effects. |
| <span id="m-cc6ea26c75a0"></span><code>MainViewModel.LoadVirtualKitAvailabilityAsync(long,IReadOnlyList&lt;KitComponentInput&gt;)</code><br>2766–2806 | ConfigureAwait @2770; GetKitAvailabilityAsync @2770; DispatchToUi @2772; Read @2774; Localize @2777; Max @2786; ResolveSelectedProductSaleUnitFactor @2786; GetValueOrDefault @2787; Clamp @2788; Pow @2789; Floor @2790; Format @2792; ToString @2794 | No extracted literal effects. |
| <span id="m-a24911c700b1"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3655–3663 | IsNullOrWhiteSpace @3657 | No extracted literal effects. |
| <span id="m-c8c5d8acf3f5"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3665–3676 | Load @3667; IsNullOrWhiteSpace @3671; Resolve @3673; Apply @3675 | No extracted literal effects. |
| <span id="m-2f5021b954b4"></span><code>MainViewModel.OpenImport()</code><br>3705–3713 | CheckSessionUnlocked @3707; Increment @3709; ResetInventoryImport @3710; Invoke @3712 | No extracted literal effects. |
| <span id="m-f5f07e5b94c8"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3715–3776 | Increment @3718; ResetInventoryImport @3723; IsNullOrWhiteSpace @3728; Exists @3728; FinishFailedImport @3730; ConfigureAwait @3742; ReadAllBytesAsync @3742; ToHexString @3743; HashData @3743; TemplateContextAsync @3747; Run @3748; Read @3748; ValidateInventoryAsync @3749; CompletedWorkbook @3750; DispatchToUi @3757; ReferenceEquals @3759; Add @3760; Localize @3761; SetImportReviewRows @3765; RaisePropertyChanged @3766; nameof @3766; ReportException @3772 | No extracted literal effects. |
| <span id="m-dee9b3cb77b4"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3778–3832 | IsCurrentImportAttempt @3794; ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3808; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3808; ConfigureAwait @3812; RecoverImportOutcomeAsync @3812; Localize @3815; DispatchToUi @3816; FinishImportAttempt @3816; LoadInventoryAsync @3817; ReportException @3818; ReportError @3822; FinishFailedImport @3823; ImportCommandIssue @3823 | No extracted literal effects. |
| <span id="m-351b426850b1"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3844–3854 | Report @3846; DispatchToUi @3847; Insert @3849 | No extracted literal effects. |
| <span id="m-fa6cb09ff6d0"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3856–3860 | RaisePropertyChanged @3859; nameof @3859 | No extracted literal effects. |
| <span id="m-e76d34897cd5"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3862–3865 | ReportError @3864 | No extracted literal effects. |
| <span id="m-338c1239dcac"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3871–3876 | ReportError @3874 | No extracted literal effects. |
| <span id="m-e5afd1022484"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3885–3891 | IsNullOrWhiteSpace @3887; Trim @3887; ReportError @3889 | No extracted literal effects. |
| <span id="m-40305e88b29d"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3893–3896 | DispatchToUi @3895; Insert @3895 | No extracted literal effects. |
| <span id="m-61e78ee8f169"></span><code>MainViewModel.DispatchToUi(Action)</code><br>3902–3916 | CheckAccess @3904; action @3906; GetResult @3914; GetAwaiter @3914; InvokeAsync @3914 | No extracted literal effects. |
| <span id="m-f819a85e2b3f"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4583–4648 | Register @4585; Execute @4585; Execute @4586; Execute @4587; Execute @4588; Execute @4593; Execute @4594; Execute @4595; Execute @4596; Execute @4597; Execute @4598; Execute @4599; Execute @4600; Execute @4601; Execute @4602; Execute @4603; Execute @4604; Execute @4605; Execute @4606; Execute @4607; Execute @4608; Execute @4609; Execute @4610; Execute @4611; Execute @4612; Execute @4613; Execute @4614; Execute @4615; Execute @4616; Execute @4617; Execute @4618; Execute @4619; Execute @4620; Execute @4621; Execute @4622; Execute @4623; Execute @4624; Execute @4626; Execute @4627; RequestClosePersonForm @4628; KeepEditingPersonForm @4629; CloseSalaryMonthDetailModal @4630; CloseSalaryPaymentModal @4631; CloseSalaryAdjustmentModal @4632; CloseSalaryFinalizeModal @4633; RequestCloseExpenseForm @4634; KeepEditingExpenseForm @4635; CloseExpenseCategoryModal @4636; CloseExpensePaymentModal @4637; CloseExpenseDetailModal @4638; ClosePaymentReturnModal @4639; CloseWasteExpenseConfirmation @4640; InitializeSalaryTables @4645; InitializeExpensesTables @4646; InitializeTeamsCommands @4647 | No extracted literal effects. |
| <span id="m-819b40acdce2"></span><code>MainViewModel.CreateDemo()</code><br>4650–4657 | SetActiveCashier @4653; Parse @4653; RefreshUnlockCandidates @4655 | No extracted literal effects. |
| <span id="m-f1c5f17b7b96"></span><code>MainViewModel.CreateInitializing()</code><br>4659–4667 | — | No extracted literal effects. |
| <span id="m-ec8cfbbce192"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4669–4679 | — | No extracted literal effects. |
| <span id="m-b4f34adebd8a"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4681–4699 | ConfigureDiagnosticsWorkspace @4695; ResolveDiagnosticsWorkspace @4695; ApplyPersistedState @4696; RefreshUnlockCandidates @4697 | No extracted literal effects. |
| <span id="m-08d2ef7632a8"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4701–4729 | CheckSessionUnlocked @4703; HasPermission @4704; Equals @4715; GetFileNameWithoutExtension @4715; GetEntryAssembly @4717; Add @4719; Start @4722; ReportException @4727 | No extracted literal effects. |
| <span id="m-a9940a137605"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4731–4754 | CheckSessionUnlocked @4733; HasPermission @4734; Equals @4744; GetFileNameWithoutExtension @4744; Add @4745; GetEntryAssembly @4745; Start @4747; ReportException @4752 | No extracted literal effects. |
| <span id="m-04df57f701f3"></span><code>MainViewModel.Dispose()</code><br>4756–4777 | ClearImportResults @4759; Increment @4760; ResetFinancialWorkspace @4762; Dispose @4763; Stop @4764; CancelBatchPricingPreviewExpiry @4767; Dispose @4768; Dispose @4769; DisposeSearchStates @4775; SuppressFinalize @4776 | No extracted literal effects. |
| <span id="m-d99aafce2709"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4779–4783 | Stop @4781 | No extracted literal effects. |
| <span id="m-68a208920710"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4785–4823 | Clear @4795; Clear @4796; Clear @4797; Clear @4798; Clear @4799; Clear @4800; Clear @4801; Clear @4802; Clear @4803; Clear @4804 | No extracted literal effects. |
| <span id="m-11b50f3e4d8f"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4825–4942 | RaisePropertyChanged @4839; nameof @4839; Clear @4841; Clear @4842; Clear @4843; CreateCommand @4850; ExecuteReader @4852; Read @4853; TryParse @4855; GetString @4855; Add @4856; GroupBy @4865; Add @4867; Count @4867; Contains @4872; Equals @4895; Add @4897; ApplyFilter @4899; All @4901; SafeError @4904; SetActiveCashier @4912; ToString @4916; ToString @4919; ToLocalTime @4919; NotifyTotalsChanged @4941 | FROM item_kits @4851 |
| <span id="m-c04c8f7dd224"></span><code>MainViewModel.InitializeDemoData()</code><br>4944–5022 | Add @4951; Add @4970; ApplyFilter @4981; Add @4984; Add @4989; Add @4995; ApplyActivityFilter @5001; Add @5004; ApplyInventoryFilter @5013; Add @5016; Parse @5016; NotifyTotalsChanged @5021 | No extracted literal effects. |
| <span id="m-9116002b81e0"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>5024–5037 | — | No extracted literal effects. |
| <span id="m-09ed6501d46c"></span><code>MainViewModel.SelectMenu(string)</code><br>5039–5112 | CheckSessionUnlocked @5041; NormalizeMenuKey @5045; LoadInvoicesAsync @5051; LoadCommercialAsync @5052; LoadActivityInvoicesAsync @5059; LoadTeamsStaffAsync @5062; LoadCatalogRegistryAsync @5063; UpdateDemoSeedingAvailabilityAsync @5066; UpdateReceiptDesignPreview @5069; RefreshDiagnosticsAsync @5070; LoadPriceLevelSettingsAsync @5071; RefreshWorkspaceCategories @5075; LoadInventoryAsync @5076; LoadPriceProposalsAsync @5078; LoadReportDataAsync @5081; LoadFinancialRegisterAsync @5082; LoadCustomersAsync @5085; LoadSuppliersAsync @5086; LoadThirdPartiesAsync @5087; LoadManufacturingDataAsync @5092; LoadManagedUnitsAsync @5100; LoadManagedCategoriesAsync @5103; LoadSalaryWorkspaceAsync @5106; LoadExpensesWorkspaceAsync @5109 | No extracted literal effects. |
| <span id="m-6bb4b5dbc807"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>5114–5133 | — | No extracted literal effects. |
| <span id="m-769c413e2221"></span><code>MainViewModel.LogOut()</code><br>5135–5156 | Clear @5137; RaisePropertyChanged @5140; nameof @5140; ClearNotifications @5142; ResetCashReview @5146; Lock @5149; RefreshUnlockCandidates @5154; UpdateDemoSeedingAvailabilityAsync @5155 | No extracted literal effects. |
| <span id="m-e26799a31788"></span><code>MainViewModel.UnlockSession()</code><br>5158–5161 | UnlockSession @5160 | No extracted literal effects. |
| <span id="m-032284e35c29"></span><code>MainViewModel.UnlockSession(string?)</code><br>5163–5262 | IsLockScreenLockedOut @5171; IsNullOrWhiteSpace @5187; AuthenticateSelectedUser @5196; Lock @5201; AddSeconds @5207; AddMinutes @5224; Initialize @5243; Unlock @5244; Any @5248; Equals @5248; RaisePropertyChanged @5249; nameof @5249; LoadActivityInvoicesAsync @5253; LoadTrackOrdersAsync @5254; UpdateDemoSeedingAvailabilityAsync @5255; StartAutomaticDemoDatasetLoadAsync @5256 | No extracted literal effects. |
| <span id="m-ccc808363692"></span><code>MainViewModel.PowerAction()</code><br>5264–5270 | CheckSessionUnlocked @5266 | No extracted literal effects. |
| <span id="m-04690adf2e3e"></span><code>MainViewModel.CycleTable()</code><br>5272–5278 | CheckSessionUnlocked @5274 | No extracted literal effects. |
| <span id="m-87b5837984ff"></span><code>MainViewModel.CycleDiningType()</code><br>5280–5286 | CheckSessionUnlocked @5282 | No extracted literal effects. |
| <span id="m-61205aabf59f"></span><code>MainViewModel.CycleCustomer()</code><br>5288–5291 | OpenCustomerChooser @5290 | No extracted literal effects. |
| <span id="m-ab444657afe2"></span><code>MainViewModel.OpenPromoDialog()</code><br>5293–5308 | CheckSessionUnlocked @5295; IsNullOrWhiteSpace @5302; RaisePropertyChanged @5306; nameof @5306 | No extracted literal effects. |
| <span id="m-90397765f2d0"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5310–5379 | CheckSessionUnlocked @5312; ToLowerInvariant @5325; Trim @5325; IsNullOrWhiteSpace @5332; Trim @5332; ToList @5340; Select @5340; ToMinorUnits @5344; Equals @5360; Calculate @5364; NotifyTotalsChanged @5376; ConfigureAwait @5378; SaveDurableCartAsync @5378 | No extracted literal effects. |
| <span id="m-7a8d3df9fb3e"></span><code>MainViewModel.TogglePromo()</code><br>5381–5398 | CheckSessionUnlocked @5383; RemovePromo @5392; OpenPromoDialog @5396 | No extracted literal effects. |
| <span id="m-47392d386277"></span><code>MainViewModel.RemovePromo()</code><br>5400–5410 | NotifyTotalsChanged @5407; SaveDurableCartAsync @5409 | No extracted literal effects. |
| <span id="m-640c9898cef3"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5412–5423 | CheckSessionUnlocked @5414; NotifyTotalsChanged @5420; ConfigureAwait @5422; SaveDurableCartAsync @5422 | No extracted literal effects. |
| <span id="m-8e489f3c41d0"></span><code>MainViewModel.CancelPromoDialog()</code><br>5425–5429 | — | No extracted literal effects. |
| <span id="m-c5797c85b667"></span><code>MainViewModel.RecalculateCart()</code><br>5431–5485 | ToMinorUnits @5447; Add @5448; Equals @5469; Calculate @5473; ToDictionary @5476; TryGetValue @5479 | No extracted literal effects. |
| <span id="m-5f0ac270d7c4"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5487–5494 | CheckSessionUnlocked @5489; ResetCashReview @5490 | No extracted literal effects. |
| <span id="m-da37f0e2db5f"></span><code>MainViewModel.SelectCategory(CategoryItem?)</code><br>5496–5542 | CheckSessionUnlocked @5498; RaisePropertyChanged @5506; nameof @5506; ApplyFilter @5507; Localize @5510 | No extracted literal effects. |
| <span id="m-9e2dbe7fb0c9"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5544–5544 | AddToCart @5544 | No extracted literal effects. |
| <span id="m-dfc965606d3e"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5546–5590 | CheckSessionUnlocked @5548; ResetCashReview @5549; ResolveProductSaleUnitFactor @5552; Round @5559; FirstOrDefault @5560; UpdateCartKitBreakdownAsync @5569; Add @5581; NotifyTotalsChanged @5584; SaveDurableCartAsync @5586; IsNullOrWhiteSpace @5588; ToString @5588; NewGuid @5588; RecordSuccessfulSearchUseAsync @5589; FromGuid @5589 | No extracted literal effects. |
| <span id="m-331a9bbf2c33"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5592–5605 | CheckSessionUnlocked @5594; ResetCashReview @5595; UpdateCartKitBreakdownAsync @5602; NotifyTotalsChanged @5603; SaveDurableCartAsync @5604 | No extracted literal effects. |
| <span id="m-37ac7167af16"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5607–5622 | CheckSessionUnlocked @5609; ResetCashReview @5610; UpdateCartKitBreakdownAsync @5614; Remove @5618; NotifyTotalsChanged @5620; SaveDurableCartAsync @5621 | No extracted literal effects. |
| <span id="m-e553825656d0"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5624–5630 | ConfigureAwait @5627; LoadAsync @5627; RefreshSavedPaymentImages @5628; CancelManualPaymentSettings @5629 | No extracted literal effects. |
| <span id="m-0752b75d0ace"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5632–5661 | ValidImage @5639; CreatePaymentBitmap @5644; Dispose @5647; RaisePropertyChanged @5659; nameof @5659 | No extracted literal effects. |
| <span id="m-c2e38c5ad91a"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5663–5679 | Dispose @5673; CreatePaymentBitmap @5675; RaisePropertyChanged @5677; nameof @5677 | No extracted literal effects. |
| <span id="m-ab9ecc873196"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5681–5685 | — | No extracted literal effects. |
| <span id="m-5657a5779afb"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5687–5695 | Dispose @5689; CreatePaymentBitmap @5691; RaisePropertyChanged @5693; nameof @5693 | No extracted literal effects. |
| <span id="m-327d1c4390d2"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5697–5716 | ConfigureAwait @5706; ExecuteAsync @5706; DispatchToUi @5709; SafePipelineError @5709; LoadAsync @5712; RefreshSavedPaymentImages @5713; CancelManualPaymentSettings @5714 | No extracted literal effects. |
| <span id="m-41ce4dc5427d"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5718–5737 | IsNullOrWhiteSpace @5722; Trim @5723; ToMinorUnits @5729; ConfigureAwait @5735; PlaceOrderAsync @5735 | No extracted literal effects. |
| <span id="m-26e6f30b03e8"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5739–5751 | PlaceOrderInternalAsync @5745 | No extracted literal effects. |
| <span id="m-66d98260a71f"></span><code>MainViewModel.PlaceOrderInternalAsync()</code><br>5753–5954 | Localize @5757; ExecuteDemoPlaceOrder @5763; ConfigureAwait @5789; SaveDurableCartAsync @5789; ToMinorUnits @5797; Trim @5799; Equals @5810; Equals @5817; ResetCashReview @5819; Max @5877; Add @5882; ConfigureAwait(TakePaymentCommand, SalesInvoice) @5900; ExecuteAsync(TakePaymentCommand, SalesInvoice) @5900; Format @5912; ToDecimal @5912; DispatchToUi @5914; Clear @5918; NewGuid @5927; NotifyTotalsChanged @5928; LoadActivityInvoicesAsync @5935; OpenStaleCartPriceReviewAsync @5940; RequestElevationForCheckout @5942; SafePipelineError @5946; SafeError @5952 | No extracted literal effects. |
| <span id="m-baecad427d72"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>5956–5988 | DispatchToUi @5960; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5963; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5963; SafePipelineError @5968; ToArray @5972; Select @5972; Where @5972; FormatCartReviewMoney @5976; Clear @5983; Add @5984 | No extracted literal effects. |
| <span id="m-a4d2760b6d6c"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>5990–5995 | ScalingFactor @5992; Format @5994; Equals @5994 | No extracted literal effects. |
| <span id="m-7a31a8598a88"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>5997–6028 | CheckSessionUnlocked @5999; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @6001; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @6001; DispatchToUi @6006; SafePipelineError @6006; ConfigureAwait @6007; OpenStaleCartPriceReviewAsync @6007; FirstOrDefault @6014; ScalingFactor @6017; ResetCashReview @6021; Clear @6024; NotifyTotalsChanged @6025 | No extracted literal effects. |
| <span id="m-9b93412005cc"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>6030–6037 | Clear @6034; ResetCashReview @6035 | No extracted literal effects. |
| <span id="m-ff1f3aacff1a"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>6039–6065 | CheckSessionUnlocked @6041; ResetCashReview @6048; ToMinorUnits @6059; ConfigureAwait @6064; PlaceOrderAsync @6064 | No extracted literal effects. |
| <span id="m-74c7181eb88d"></span><code>MainViewModel.CancelCashReview()</code><br>6067–6071 | ResetCashReview @6069 | No extracted literal effects. |
| <span id="m-459c4f35f01a"></span><code>MainViewModel.ResetCashReview()</code><br>6073–6082 | — | No extracted literal effects. |
| <span id="m-418ff96540f4"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>6084–6103 | RaisePropertyChanged @6095; nameof @6095; Clear @6098; ResetCashReview @6099; NotifyTotalsChanged @6100 | No extracted literal effects. |
| <span id="m-a74153ae4c71"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>6105–6170 | ConfigureAwait @6109; WaitAsync @6109; ClearActiveCartAsync @6114; ToMinorUnits @6124; Add @6125; ToUpperInvariant @6128; ToString @6128; IsNullOrWhiteSpace @6131; SaveActiveCartAsync @6144; DispatchToUi @6163; SafeError @6163; Release @6168 | No extracted literal effects. |
| <span id="m-4e900d40c039"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>6172–6231 | ConfigureAwait @6178; GetActiveCartAsync @6178; Clear @6190; FirstOrDefault @6193; ToDecimal @6197; Add @6207; NotifyTotalsChanged @6224 | No extracted literal effects. |
| <span id="m-818046d4faf3"></span><code>MainViewModel.SanitizeOrderHistorySummary(string?,bool)</code><br>6233–6246 | IsNullOrWhiteSpace @6235; Replace @6240; Trim @6245; Trim @6245 | No extracted literal effects. |
| <span id="m-b2858cf165fc"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>6248–6325 | ApplyPagedResult @6252; ToList @6253; ApplyActivityFilter @6257; HasPermission @6262; ConfigureAwait @6269; GetPagedActivityInvoicesAsync @6269; ToPageRequest @6272; ToDecimal @6278; Add @6279; ToString @6284; ToLocalTime @6284; SanitizeOrderHistorySummary @6285; DispatchToUi @6303; Clear @6305; Add @6308; SafeError @6322 | No extracted literal effects. |
| <span id="m-f968ddf00871"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>6327–6404 | HasPermission @6332; ConfigureAwait @6339; GetActiveOrdersAsync @6339; Clear @6340; ToDecimal @6344; Join @6378; Select @6378; Add @6380; ToString @6395; ToLocalTime @6395; SanitizeOrderHistorySummary @6396 | No extracted literal effects. |
| <span id="m-0ee7cdfa8c8c"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6406–6433 | CheckSessionUnlocked @6408; Clear @6411; ConfigureAwait @6417; GetOrderByIdAsync @6417; Add @6422; DispatchToUi @6428; SafeError @6428 | No extracted literal effects. |
| <span id="m-35d75555ceb6"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6435–6440 | Clear @6439 | No extracted literal effects. |
| <span id="m-daa0416bd961"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6442–6475 | CheckSessionUnlocked @6444; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6460; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6460; ConfigureAwait @6469; LoadTrackOrdersAsync @6469; DispatchToUi @6473; SafePipelineError @6473 | No extracted literal effects. |
| <span id="m-95eaf4c9d71b"></span><code>MainViewModel.MarkReadyAsync()</code><br>6477–6510 | CheckSessionUnlocked @6479; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6495; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6495; ConfigureAwait @6504; LoadTrackOrdersAsync @6504; DispatchToUi @6508; SafePipelineError @6508 | No extracted literal effects. |
| <span id="m-796da209d5f1"></span><code>MainViewModel.MarkServedAsync()</code><br>6512–6545 | CheckSessionUnlocked @6514; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6530; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6530; ConfigureAwait @6539; LoadTrackOrdersAsync @6539; DispatchToUi @6543; SafePipelineError @6543 | No extracted literal effects. |
| <span id="m-36a2a47c4e06"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6547–6575 | CheckSessionUnlocked @6549; Remove @6553; CloseOrderDetailsModal @6554; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6563; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6563; ConfigureAwait @6569; LoadTrackOrdersAsync @6569; DispatchToUi @6573; SafePipelineError @6573 | No extracted literal effects. |
| <span id="m-1a33d453b848"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6577–6673 | CheckSessionUnlocked @6579; CloseOrderDetailsModal @6585; ConfigureAwait @6592; GetOrderByIdAsync @6592; Zero @6614; NewGuid @6620; ToList @6623; Select @6623; ToUpperInvariant @6626; ToString @6626; SaveActiveCartAsync @6635; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6651; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6651; DispatchToUi @6654; SafePipelineError @6654; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6660; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6660; LoadTrackOrdersAsync @6666; LoadActivityInvoicesAsync @6667 | No extracted literal effects. |
| <span id="m-fe6ad157516a"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6675–6682 | CheckSessionUnlocked @6677 | No extracted literal effects. |
| <span id="m-61e58db4e605"></span><code>MainViewModel.FilterActivity(string)</code><br>6701–6707 | CheckSessionUnlocked @6703; ApplyActivityFilter @6705 | No extracted literal effects. |
| <span id="m-977c93365ea1"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6709–6748 | Clear @6711; AsEnumerable @6712; Where @6717; IsNullOrWhiteSpace @6720; Trim @6722; Contains @6724; Contains @6725; Contains @6726; IsNullOrEmpty @6730; Equals @6732; ToList @6736; Add @6738; ApplyPagedResult @6742 | No extracted literal effects. |
| <span id="m-46f454861961"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6750–6786 | CheckSessionUnlocked @6752; ConfigureAwait(QueueReceiptReprintCommand, string) @6772; ExecuteAsync(QueueReceiptReprintCommand, string) @6772; IsNullOrWhiteSpace @6773; ReportError @6775; RefreshOutputStatusAsync @6780; DispatchToUi @6784; SafeError @6784 | No extracted literal effects. |
| <span id="m-f95d585c6be4"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6788–6831 | RefreshOutputPrinterQueues @6793; ReadAsync @6794; Equals @6801; IsNullOrWhiteSpace @6801; TryReadGeometry @6803; ComputeCapabilityFingerprint @6807; ConfigureAwait @6811; InvalidateThermalVerificationAsync @6811; LoadCashFinancialSettingsAsync @6823; LoadReceiptDesignAsync @6824; RefreshOutputStatusAsync @6825; DispatchToUi @6829; SafeError @6829 | No extracted literal effects. |
| <span id="m-e86adda15f3c"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6833–6859 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6846; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6846; ReportError @6849; LoadOutputDevicesAsync @6852; DispatchToUi @6857; SafeError @6857 | No extracted literal effects. |
| <span id="m-804269a79975"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6861–6934 | Equals @6875; IsNullOrWhiteSpace @6880; IsWindows @6885; TryReadGeometry @6890; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6907; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6907; ReportError @6910; Render @6913; ToString @6914; ConfigureAwait @6915; Run @6915; Send @6915; ComputeCapabilityFingerprint @6916; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @6917; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @6917; RefreshOutputStatusAsync @6928; DispatchToUi @6932; SafeError @6932 | No extracted literal effects. |
| <span id="m-f3f69e119d57"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>6936–6973 | IsWindows @6950; IsNullOrWhiteSpace @6950; TryReadGeometry @6952; ComputeCapabilityFingerprint @6956; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @6957; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @6957; ReportError @6961; ConfigureAwait @6967; RefreshOutputStatusAsync @6967; DispatchToUi @6971; SafeError @6971 | InvalidOperationException @6951; InvalidOperationException @6955 |
| <span id="m-47dd9f48b31c"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>6975–7012 | CreateCommand @6980; ConfigureAwait @6989; ExecuteReaderAsync @6989; ReadAsync @6990; GetInt32 @6993; GetString @6993; GetInt64 @6993; Parse @6994; RaisePropertyChanged @6996; nameof @6996; NotifyTotalsChanged @7005; DispatchToUi @7010; SafeError @7010 | FROM store_config @6981 |
| <span id="m-ef226afad27d"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>7014–7042 | ConfigureAwait @7027; ExecuteAsync @7027; ReportError @7030; NotifyTotalsChanged @7035; DispatchToUi @7040; SafeError @7040 | No extracted literal effects. |
| <span id="m-0c098ab139b3"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>7044–7088 | DispatchToUi @7048; CreateCommand @7053; ConfigureAwait @7059; ExecuteReaderAsync @7059; ReadAsync @7060; Deserialize(ReceiptDesignDocument) @7062; GetString @7062; SafeError @7081 | FROM receipt_designs @7054; JOIN receipt_design_versions @7054 |
| <span id="m-5199fd11cf6f"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>7090–7117 | ConfigureAwait @7103; ExecuteAsync @7103; ReportError @7108; DispatchToUi @7115; SafeError @7115 | No extracted literal effects. |
| <span id="m-9df7458838b6"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>7119–7131 | IsWindows @7121; Select @7122; Enumerate @7122; Empty(string) @7123; ToArray @7124; OrderBy @7124; Distinct @7124; Where @7124; Append @7124; IsNullOrWhiteSpace @7125; Clear @7129; Add @7130 | No extracted literal effects. |
| <span id="m-8318741e6a93"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>7133–7191 | CheckAccess @7135; DispatchToUi @7137; CreateSampleData @7143; Equals @7149; IsWindows @7156; TryReadGeometry @7157; BuildPaperDocument @7166; RenderPreviewPngPages @7169; SetReceiptDesignPreviewPages @7171; Localize @7173; BuildThermalLines @7178; RenderPreviewPng @7180; Empty(byte[]) @7187; ReportException @7189 | No extracted literal effects. |
| <span id="m-7b8aa2858a41"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>7193–7198 | ShowReceiptDesignPreviewPage @7197 | No extracted literal effects. |
| <span id="m-0af6df1ef703"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>7200–7206 | ShowReceiptDesignPreviewPage @7205 | No extracted literal effects. |
| <span id="m-a5d5e4a90f20"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>7208–7222 | RaisePropertyChanged @7219; nameof @7219 | No extracted literal effects. |
| <span id="m-687ae5fcfa1b"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>7224–7253 | ReadAsync @7227; Localize @7230; CreateCommand @7232; ConfigureAwait @7234; ExecuteScalarAsync @7234; ToString @7234; IsNullOrWhiteSpace @7235; ExecuteReaderAsync @7249; ReadAsync @7250; Trim @7251; GetString @7251 | FROM hardware_jobs @7233; FROM hardware_jobs @7248 |
| <span id="m-a998e4144615"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>7255–7275 | Clear @7257; AsEnumerable @7258; Where @7261; Equals @7261; IsNullOrWhiteSpace @7267; Contains @7269; Contains @7270; Contains @7271; Add @7274 | No extracted literal effects. |
| <span id="m-1aad4a9b1776"></span><code>MainViewModel.SelectInventoryKind(string)</code><br>7277–7321 | NormalizeItemKind @7279; SelectCatalogKind @7282; Clear @7286; ClearSelection @7291; InvalidateSelectedBatchPreview @7292; IsNullOrEmpty @7295; RaisePropertyChanged @7303; nameof @7303; ResetToFirstPage @7306; NotifySelectionScopeChange @7307; SetSelectionScope @7307; InventorySelectionScope @7307; RefreshWorkspaceCategories @7310; LoadInventoryAsync @7313 | No extracted literal effects. |
| <span id="m-97d78c949880"></span><code>MainViewModel.RefreshWorkspaceCategories()</code><br>7323–7382 | Clear @7325; Equals @7326; IsNullOrEmpty @7330; Add @7335; Localize @7338; Add @7349; RaisePropertyChanged @7381; nameof @7381 | No extracted literal effects. |
| <span id="m-7b5f5ba9e514"></span><code>MainViewModel.SelectWorkspaceCategory(CategoryItem?)</code><br>7384–7417 | Equals @7387; Localize @7389; RaisePropertyChanged @7401; nameof @7401; ClearSelection @7412; InvalidateSelectedBatchPreview @7413; ResetToFirstPage @7414; NotifySelectionScopeChange @7415; SetSelectionScope @7415; InventorySelectionScope @7415; LoadInventoryAsync @7416 | No extracted literal effects. |
| <span id="m-2d70806a34d6"></span><code>MainViewModel.GenerateXReport()</code><br>7419–7438 | CheckSessionUnlocked @7421; ToString @7425; GenerateXReportInternalAsync @7437 | No extracted literal effects. |
| <span id="m-8a219417698f"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>7440–7455 | ConfigureAwait @7444; LoadReportDataAsync @7444; DispatchToUi @7453; SafeError @7453 | No extracted literal effects. |
| <span id="m-8439ca49bafe"></span><code>MainViewModel.CloseShiftZReport()</code><br>7457–7460 | OpenCloseShiftModal @7459 | No extracted literal effects. |
| <span id="m-2d5bca1aaa52"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>7462–7471 | CheckSessionUnlocked @7469 | No extracted literal effects. |
| <span id="m-53c5a1ab0421"></span><code>MainViewModel.SaveSettings()</code><br>7473–7477 | CheckSessionUnlocked @7475 | No extracted literal effects. |
| <span id="m-de0a842d6d2a"></span><code>MainViewModel.ApplySettingsAsync()</code><br>7479–7566 | CheckSessionUnlocked @7488; NotifyTotalsChanged @7507; ExecuteAsync @7535; DispatchToUi @7559; SafePipelineError @7559; SafeError @7564 | No extracted literal effects. |
| <span id="m-1e76baf65235"></span><code>MainViewModel.CancelSettings()</code><br>7568–7589 | CheckSessionUnlocked @7570; NotifyTotalsChanged @7582 | No extracted literal effects. |
| <span id="m-6c82c3ee0bed"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7592–7622 | ProbeDatabaseAsync @7605; ProbeLicense @7611; RefreshOutputStatusAsync @7614; ProbeHardwareStubs @7615; DispatchToUi @7620; SafeError @7620 | No extracted literal effects. |
| <span id="m-a37d5b49bb8d"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7683–7721 | RaisePropertyChanged @7685; nameof @7685; FormatRealResetPreviewSummary @7720 | No extracted literal effects. |
| <span id="m-88c6283b1e20"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7723–7736 | Localize @7724; ToString @7726; GetValueOrDefault @7726; ToString @7731; ToString @7732; ToString @7733 | No extracted literal effects. |
| <span id="m-f617ae9853c6"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7845–7937 | Post @7849; ConfigureAwait @7856; GetWorkspaceEnvironmentAsync @7856; Equals @7857; GetDatasetStateAsync @7859; CreateCommand @7865; CreateParameter @7872; ToString @7874; Add @7875; ExecuteScalarAsync @7876; HasPermission @7881; ToInt64 @7886; ExecuteScalarAsync @7886; ExecuteScalarAsync @7890; ExecuteScalarAsync @7897; ExecuteScalarAsync @7903; Localize @7922 | FROM items @7885; FROM sales_invoices @7889; FROM third_parties @7902; FROM users @7866; JOIN user_roles @7866 · DYNAMIC SQL: inspect manually |
| <span id="m-46873492a631"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>7939–7949 | CheckSessionUnlocked @7941; HasPermission @7942 | No extracted literal effects. |
| <span id="m-13fd055afe4c"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>7951–7956 | ConfigureAwait @7955; ResetDatabaseAsync @7955 | No extracted literal effects. |
| <span id="m-033f93b9f45b"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>7958–7959 | ConfigureAwait @7959; EnsureDefaultDemoDatasetAsync @7959 | No extracted literal effects. |
| <span id="m-80beb0ec0a83"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>7961–7967 | EnsureDefaultDemoDatasetAsync @7965 | No extracted literal effects. |
| <span id="m-678d1cd2fc3c"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>7969–8073 | Localize @7974; ConfigureAwait @7981; WaitAsync @7981; GetWorkspaceEnvironmentAsync @7984; Equals @7985; HasPermission @7992; Post @8006; LocalizeDemoSeedProgress @8008; EnsureInitialDatasetAsync @8014; Join @8038; Select @8038; ReloadCatalogAsync @8048; LoadInventoryAsync @8049; LoadThirdPartiesAsync @8050; LoadManufacturingDataAsync @8051; LoadSuppliersAsync @8052; UpdateDemoSeedingAvailabilityAsync @8053; ToUpperInvariant @8058; ToString @8058; NewGuid @8058; LogDiagnosticError @8059; ReportError @8064; Release @8071 | No extracted literal effects. |
| <span id="m-8e9411521711"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>8075–8089 | Localize @8077 | No extracted literal effects. |
| <span id="m-3b8b3b47f94d"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>8091–8188 | Localize @8095; ConfigureAwait @8099; WaitAsync @8099; HasPermission @8103; GetWorkspaceEnvironmentAsync @8110; Equals @8111; ResetDatabaseAsync @8119; GetStoreProfileAsync @8122; Post @8123; Clear @8126; Clear @8127; Clear @8128; NewGuid @8129; RaisePropertyChanged @8132; nameof @8132; Lock @8133; Defaults @8146; RefreshUnlockCandidates @8159; LoadCashFinancialSettingsAsync @8160; LoadOutputDevicesAsync @8161; LoadManualPaymentSettingsAsync @8162; LoadReceiptDesignAsync @8163; ReloadCatalogAsync @8164; LoadInventoryAsync @8165; LoadThirdPartiesAsync @8166; LoadManufacturingDataAsync @8167; LoadActivityInvoicesAsync @8168; UpdateDemoSeedingAvailabilityAsync @8169; ToUpperInvariant @8174; ToString @8174; LogDiagnosticError @8175; ReportError @8181; Release @8186 | No extracted literal effects. |
| <span id="m-e07d6fde411b"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>8190–8232 | CheckSessionUnlocked @8192; HasPermission @8194; ConfigureAwait @8202; GetWorkspaceEnvironmentAsync @8202; Equals @8203; PreviewAsync @8206; FormatRealResetPreviewSummary @8207; Post @8208; RaisePropertyChanged @8225; nameof @8225; SafeError @8230 | UnauthorizedAccessException @8204 |
| <span id="m-133a88846806"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>8234–8320 | HasPermission @8237; ConfigureAwait @8255; ExecuteAsync @8255; GetStoreProfileAsync @8264; Post @8267; Clear @8271; Clear @8272; Clear @8273; Clear @8274; NewGuid @8275; Lock @8278; RaisePropertyChanged @8292; nameof @8292; LoadCashFinancialSettingsAsync @8293; LoadOutputDevicesAsync @8294; LoadManualPaymentSettingsAsync @8295; LoadReceiptDesignAsync @8296; RefreshUnlockCandidates @8304; LoadInventoryAsync @8305; LoadActivityInvoicesAsync @8306; UpdateDemoSeedingAvailabilityAsync @8307; ToUpperInvariant @8312; ToString @8312; LogDiagnosticError @8313 | No extracted literal effects. |
| <span id="m-73d49c0b280b"></span><code>MainViewModel.CancelRealShopReset()</code><br>8322–8329 | RaisePropertyChanged @8328; nameof @8328 | No extracted literal effects. |
| <span id="m-f9ac9e6e4bab"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>8333–8350 | ConfigureAwait @8335; ExportDocumentAsync @8335; Post @8339; GetFileName @8343 | No extracted literal effects. |
| <span id="m-bced8e653ac0"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>8352–8374 | Exists @8357; CreateDirectory @8359; Start @8361; ToUpperInvariant @8370; ToString @8370; NewGuid @8370; LogDiagnosticError @8371 | No extracted literal effects. |
| <span id="m-4b97b8840ccd"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>8376–8386 | CheckSessionUnlocked @8378; RaisePropertyChanged @8380; nameof @8380; Localize @8382; ToString @8383 | No extracted literal effects. |
| <span id="m-17234cf05b06"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>8393–8409 | CheckSessionUnlocked @8395; HasPermission @8396; RaisePropertyChanged @8402; nameof @8402; Localize @8405; ToString @8406 | No extracted literal effects. |
| <span id="m-7b5ae0771a3e"></span><code>MainViewModel.CommitNumpad()</code><br>8411–8488 | CheckSessionUnlocked @8413; ResetCashReview @8414; TryParse @8420; IsNullOrWhiteSpace @8422; Trim @8428; NotifyTotalsChanged @8438; SaveDurableCartAsync @8439; Min @8445; ToMinorUnits @8447; Round @8448; TryParse @8463; UpdateCartKitBreakdownAsync @8471; Remove @8477; RaisePropertyChanged @8486; nameof @8486 | No extracted literal effects. |
| <span id="m-d2cfeddb934c"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>8494–8512 | CheckSessionUnlocked @8502 | No extracted literal effects. |
| <span id="m-3263d64963d7"></span><code>MainViewModel.StageBusinessProfile()</code><br>8519–8549 | CheckSessionUnlocked @8521; HasPermission @8525 | No extracted literal effects. |
| <span id="m-9e8c725075e2"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8551–8560 | — | No extracted literal effects. |
| <span id="m-12c60a5b75ec"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8562–8585 | RecalculateCart @8564; RaisePropertyChanged @8566; nameof @8566 | No extracted literal effects. |
| <span id="m-22f17d082d3e"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8587–8674 | IsNullOrWhiteSpace @8590; Trim @8590; All @8600; Trim @8617; Trim @8618; NewGuid @8622; ToString @8627; ConfigureAwait @8631; BeginTransactionAsync @8631; HandleAsync @8632; AppendAsync @8637; ToString @8638; Serialize @8643; CommitAsync @8646; Initialize @8652; Unlock @8653; RaisePropertyChanged @8658; nameof @8658; LoadTeamsStaffAsync @8661; StartAutomaticDemoDatasetLoadAsync @8662; RollbackAsync @8666; DispatchToUi @8667; SafePipelineError @8667; SafeError @8672 | No extracted literal effects. |
| <span id="m-fd49a48362a1"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8676–8683 | IsNullOrWhiteSpace @8678; ConfigureAwait @8682; SaveTeamMemberAsync @8682 | No extracted literal effects. |
| <span id="m-9f12a627945c"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8685–8703 | CheckSessionUnlocked @8688; HasPermission @8690 | No extracted literal effects. |
| <span id="m-f6da9b2c9aca"></span><code>MainViewModel.CancelChangePin()</code><br>8705–8712 | — | No extracted literal effects. |
| <span id="m-d280146c29ec"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8714–8790 | Trim @8722; IsNullOrWhiteSpace @8725; All @8731; Equals @8744; Equals @8745; SetQuickPin @8757; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8770; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8770; ConfigureAwait @8778; LoadTeamsStaffAsync @8778; DispatchToUi @8783; SafePipelineError @8783; SafeError @8788 | No extracted literal effects. |
| <span id="m-ff52f7c15c27"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8792–8866 | HasPermission @8798; ConfigureAwait @8807; ResolveEffectivePermissionsAsync @8807; Contains @8840; Contains @8841; Add @8843; Contains @8849; DispatchToUi @8855; Clear @8857; Add @8858; SafeError @8864 | No extracted literal effects. |
| <span id="m-cc83f6b4c883"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8868–8910 | OnTeamMemberFieldChanged @8874; ConfigureAwait @8891; ExecuteAsync @8891; DispatchToUi @8895; SafePipelineError @8903; SafeError @8908 | No extracted literal effects. |
| <span id="m-e5d103d93b17"></span><code>MainViewModel.ClosePermissionEditor()</code><br>8912–8917 | — | No extracted literal effects. |
| <span id="m-83cb3a44a459"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>8919–8934 | ClearImportResults @8921 | No extracted literal effects. |
| <span id="m-ebbca56b039e"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>8938–8938 | — | No extracted literal effects. |
| <span id="m-3eb95ac31c5b"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>8939–8939 | — | No extracted literal effects. |
| <span id="m-5ea00bae4a9a"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>8940–8940 | FromResult @8940 | No extracted literal effects. |
| <span id="m-ba6617890aaf"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>8943–9028 | HasPermission @8952; FromDecimal @8967; ConfigureAwait(OpenShiftCommand, Shift) @8971; ExecuteAsync(OpenShiftCommand, Shift) @8971; SetActiveCashier @8986; RefreshUnlockCandidates @8987; ToUpperInvariant @9004; ToString @9004; ToString @9006; ConfigureAwait @9016; LoadTeamsStaffAsync @9016; LoadTrackOrdersAsync @9017; DispatchToUi @9021; SafePipelineError @9021; SafeError @9026 | No extracted literal effects. |
| <span id="m-42a56ad283bc"></span><code>MainViewModel.LoadInventoryAsync()</code><br>9030–9189 | ApplyPagedResult @9034; ToList @9035; Where @9035; Equals @9035; Count @9036; ApplyInventoryFilter @9039; Clear @9048; Empty(InventoryItem) @9050; ConfigureAwait @9055; GetPagedInventoryItemsAsync @9055; ToPageRequest @9060; CreateCommand @9075; ExecuteReaderAsync @9077; ReadAsync @9078; Add @9080; Parse @9080; GetString @9080; ExecuteReaderAsync @9090; ReadAsync @9091; TryParse @9093; GetString @9093; IsDBNull @9093; Add @9104; TryGetValue @9107; Contains @9115; ToDecimal @9118; Localize @9126; ToLocalTime @9132; BuildCostSourcesTooltip @9134; DispatchToUi @9161; Add @9165; SafeError @9187 | FROM item_kits @9076; FROM item_pricing @9089 |
| <span id="m-ae0301aa2b1e"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>9191–9247 | CheckSessionUnlocked @9193; FirstOrDefault @9194; Clear @9205; Add @9207; CreateCommand @9212; CreateParameter @9223; Add @9226; ExecuteReader @9227; Read @9228; GetString @9230; Contains @9231; FirstOrDefault @9243; ResetReceiveLines @9244; UpdateReceiveKitBreakdownAsync @9245 | FROM uoms @9213; JOIN uoms @9213 |
| <span id="m-87621bd073d6"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>9249–9350 | IsNullOrWhiteSpace @9262; Localize @9279; HasPermission @9283; BuildReceiptLines @9289; Sum @9306; Trim @9316; ToMinorUnits @9321; ConfigureAwait(ReceiveStockCommand, StockMovement) @9326; ExecuteAsync(ReceiveStockCommand, StockMovement) @9326; Clear @9336; ConfigureAwait @9338; LoadInventoryAsync @9338; LoadItemHistoryAsync @9339; DispatchToUi @9343; SafePipelineError @9343; SafeError @9348 | No extracted literal effects. |
| <span id="m-d7d86f6e324a"></span><code>MainViewModel.ResetReceiveLines()</code><br>9356–9373 | Clear @9358; Add @9362; RaisePropertyChanged @9368; nameof @9368; Invoke @9371 | No extracted literal effects. |
| <span id="m-7ada75d4259a"></span><code>MainViewModel.AddReceiveLine()</code><br>9376–9399 | IsNullOrWhiteSpace @9383; Add @9389; RaisePropertyChanged @9394; nameof @9394; Invoke @9397 | No extracted literal effects. |
| <span id="m-60b77f5cd75c"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>9402–9419 | Remove @9409; Add @9412; RaisePropertyChanged @9418; nameof @9418 | No extracted literal effects. |
| <span id="m-7909fc1924d1"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>9425–9446 | IsNullOrWhiteSpace @9427; LastOrDefault @9432; Add @9436; Trim @9439; ReferenceEquals @9440; RaisePropertyChanged @9444; nameof @9444; Invoke @9445 | No extracted literal effects. |
| <span id="m-32a331fafab0"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>9449–9526 | Add @9461; IsNullOrWhiteSpace @9469; Trim @9473; FirstOrDefault @9482; GroupBy @9482; Count @9484; Trim @9511 | No extracted literal effects. |
| <span id="m-5ce82783a0d8"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>9528–9564 | CreateCommand @9533; ConfigureAwait @9540; ExecuteReaderAsync @9540; Clear @9541; ReadAsync @9542; Add @9544; ParseGuidSafe @9545; GetString @9545; IsDBNull @9549; GetInt32 @9553; Parse @9555; DispatchToUi @9562; SafeError @9562 | FROM third_parties @9534 |
| <span id="m-1768dd296dca"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9566–9584 | CheckSessionUnlocked @9568; FirstOrDefault @9574 | No extracted literal effects. |
| <span id="m-7201cc22f70e"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9586–9677 | IsNullOrWhiteSpace @9609; HasPermission @9620; Trim @9638; Trim @9640; ConfigureAwait(AdjustStockCommand, StockMovement) @9644; ExecuteAsync(AdjustStockCommand, StockMovement) @9644; ConfigureAwait @9660; LoadInventoryAsync @9660; LoadItemHistoryAsync @9661; OpenWasteExpenseConfirmation @9665; DispatchToUi @9670; SafePipelineError @9670; SafeError @9675 | No extracted literal effects. |
| <span id="m-31dc0585552f"></span><code>MainViewModel.OpenAddService()</code><br>9679–9741 | ResetProductStockDraft @9681; CheckSessionUnlocked @9682; HasPermission @9683; RaisePropertyChanged @9692; nameof @9692; ClearItemHistory @9701; LoadCatalogRegistryAsync @9708; InitializeProductPricingDraft @9711; Clear @9726; Clear @9727; Clear @9736; CaptureProductModalBaselineAsync @9740 | No extracted literal effects. |
| <span id="m-b88420b5494e"></span><code>MainViewModel.OpenAddProduct()</code><br>9743–9819 | ResetProductStockDraft @9745; CheckSessionUnlocked @9746; RaisePropertyChanged @9748; nameof @9748; HasPermission @9755; ClearItemHistory @9765; LoadCatalogRegistryAsync @9772; InitializeProductPricingDraft @9775; Clear @9790; Clear @9791; Where @9792; Add @9794; FirstOrDefault @9796; Clear @9807; CaptureProductModalBaselineAsync @9818 | No extracted literal effects. |
| <span id="m-4a718e0ef279"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9821–9821 | OpenEditProduct @9821 | No extracted literal effects. |
| <span id="m-c25d81f81270"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9823–9912 | ResetProductStockDraft @9825; CheckSessionUnlocked @9827; RaisePropertyChanged @9830; nameof @9830; HasPermission @9837; ClearItemHistory @9847; LoadCatalogRegistryAsync @9855; InitializeProductPricingDraft @9861; ToMinorUnits @9862; LoadExactProductCostSnapshotsAsync @9868; ToDecimal @9872; Clear @9879; Clear @9880; Where @9881; Add @9883; FirstOrDefault @9885; LoadItemLocationEligibilitiesAsync @9904; LoadProductKitAsync @9905; LoadPrimaryBarcodeAsync @9906; LoadProductPricingDraftAsync @9907; LoadItemHistoryAsync @9908; LoadItemPriceHistoryAsync @9909; CaptureProductModalBaselineAsync @9911 | No extracted literal effects. |
| <span id="m-5acd2f00b000"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>9914–9927 | OrderBy @9917; Where @9917; Add @9919 | No extracted literal effects. |
| <span id="m-7e1bfd63bec0"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>9929–10002 | CreateCommand @9936; CreateParameter @9943; ToString @9945; Add @9946; ConfigureAwait @9947; ExecuteReaderAsync @9947; ReadAsync @9948; GetInt32 @9950; IsDBNull @9951; GetString @9951; ParseStoredPricingPercentForDisplay @9952; ToDisplayAmount @9956; GetInt64 @9956; OrderBy @9976; Where @9976; TryGetValue @9979; Add @9985; InvokeAsync @9987; RaisePropertyChanged @9992; nameof @9992; CaptureProductPricingSnapshot @9995; DispatchToUi @10000; SafeError @10000 | FROM item_price_levels @9967; FROM item_pricing @9938 |
| <span id="m-72feefa0885e"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>10004–10039 | CreateCommand @10011; CreateParameter @10017; ToString @10019; Add @10020; ConfigureAwait @10021; ExecuteReaderAsync @10021; ReadAsync @10022; Parse @10025; GetString @10025; GetInt32 @10025; GetInt64 @10026; IsDBNull @10026; Parse @10027; InvokeAsync @10029; DispatchToUi @10037; SafeError @10037 | FROM product_category_pricing_rules @10012 |
| <span id="m-3400a9ebf084"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>10041–10070 | ConfigureAwait @10045; WhenAll @10045; InvokeAsync @10046; CaptureProductModalSnapshot @10050; CaptureProductPricingSnapshot @10051; RaisePropertyChanged @10052; nameof @10052 | No extracted literal effects. |
| <span id="m-28bf5dc68462"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>10072–10120 | Serialize @10072; ToArray @10095; Select @10095; Select @10112; OrderBy @10112; OrderBy @10116 | No extracted literal effects. |
| <span id="m-67cf7bf8aa94"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>10122–10134 | Serialize @10122; ToArray @10133; Select @10133 | No extracted literal effects. |
| <span id="m-c57605f508fd"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>10136–10168 | nameof @10138; RaisePropertyChanged @10139; RaiseTraceabilityState @10144; StartsWith @10148; RecomputeProductPricingPreview @10159; RefreshVirtualKitAvailability @10161 | No extracted literal effects. |
| <span id="m-0b1b21454e4d"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>10170–10184 | RaisePropertyChanged @10178; nameof @10178; RecomputeProductPricingPreview @10181; RefreshVirtualKitAvailability @10182 | No extracted literal effects. |
| <span id="m-9de7f7996ee9"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>10186–10194 | RaisePropertyChanged @10188; nameof @10188; RecomputeProductPricingPreview @10191; RefreshVirtualKitAvailability @10192 | No extracted literal effects. |
| <span id="m-3856722bdc74"></span><code>MainViewModel.RequestCloseProductModal()</code><br>10196–10209 | DiscardProductModal @10208 | No extracted literal effects. |
| <span id="m-3b1adcb2bc68"></span><code>MainViewModel.DiscardProductModal()</code><br>10211–10220 | RaisePropertyChanged @10216; nameof @10216; ClearItemHistory @10218 | No extracted literal effects. |
| <span id="m-19994e387ff7"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>10222–10240 | CreateCommand @10227; CreateParameter @10229; ToString @10231; Add @10232; ConfigureAwait @10233; ExecuteScalarAsync @10233; DispatchToUi @10236; ToString @10236 | FROM barcodes @10228 |
| <span id="m-471b51f6499e"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>10242–10293 | CreateCommand @10247; CreateParameter @10254; ToString @10256; Add @10257; ConfigureAwait @10261; ExecuteReaderAsync @10261; ReadAsync @10262; IsDBNull @10265; GetString @10265; GetDouble @10266; ResolveQuantity @10267; Add @10268; Parse @10270; DispatchToUi @10278; Clear @10281; Add @10282; RaisePropertyChanged @10285; nameof @10285; RecomputeProductPricingPreview @10288; RefreshVirtualKitAvailability @10289 | FROM item_kits @10248; JOIN item_kit_components @10248; JOIN items @10248 |
| <span id="m-5261f3d14d13"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>10295–10295 | SaveProductConfigurationAsync @10295 | No extracted literal effects. |
| <span id="m-c0a700fc1402"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>10297–10646 | ConfigureAwait @10302; LoadCatalogRegistryAsync @10302; HasPermission @10304; IsNullOrWhiteSpace @10309; Equals @10334; ValidateUnitEligibility @10347; ToMinorUnits @10367; GetValueOrDefault @10374; Trim @10375; Trim @10376; Trim @10378; Empty(KitComponentInput) @10411; CaptureProductPricingSnapshot @10414; ToCommand @10416; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @10427; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @10427; DispatchToUi @10430; RaiseTraceabilityState @10437; CaptureProductModalSnapshot @10440; RaisePropertyChanged @10442; nameof @10442; SelectInventoryKind @10448; ReloadCatalogAsync @10450; LoadInventoryAsync @10451; LoadItemHistoryAsync @10452; SafePipelineError @10456; SafeError @10462; Localize @10474; GetValueOrDefault @10541; Trim @10544; Trim @10551; ToList @10598; Select @10598 | No extracted literal effects. |
| <span id="m-98fabf4b6742"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>10648–10684 | CheckSessionUnlocked @10650; HasPermission @10651; ConfigureAwait(DeactivateProductCommand, bool) @10667; ExecuteAsync(DeactivateProductCommand, bool) @10667; ConfigureAwait @10672; ReloadCatalogAsync @10672; LoadInventoryAsync @10673; DispatchToUi @10677; SafePipelineError @10677; SafeError @10682 | No extracted literal effects. |
| <span id="m-d6fac978dd2a"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>10686–10762 | ConfigureAwait @10692; GetActiveItemsAsync @10692; Clear @10694; Clear @10695; Clear @10696; CreateCommand @10701; ExecuteReaderAsync @10703; ReadAsync @10704; TryParse @10706; GetString @10706; Add @10707; GroupBy @10715; Add @10717; Count @10717; Contains @10722; Equals @10745; Add @10747; All @10750; SafeError @10753; ApplyFilter @10756 | FROM item_kits @10702 |
| <span id="m-785904681c42"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>10764–10770 | IsNullOrWhiteSpace @10766; TryParse @10767; HashData @10768; GetBytes @10768; AsSpan @10769 | No extracted literal effects. |
| <span id="m-e5e23ed7d447"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>10772–10838 | CreateCommand @10778; ConfigureAwait @10781; ExecuteReaderAsync @10781; ReadAsync @10783; Add @10785; GetString @10787; GetInt32 @10791; Clear @10797; Add @10798; ExecuteReaderAsync @10810; ReadAsync @10812; Add @10814; GetString @10816; IsDBNull @10820; GetInt32 @10824; Clear @10830; Add @10831; DispatchToUi @10836; SafeError @10836 | FROM bins @10803; FROM facilities @10780; JOIN facilities @10803 |
| <span id="m-ae541e357c02"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>11064–11186 | CreateCommand @11074; ConfigureAwait @11081; ExecuteReaderAsync @11081; ReadAsync @11082; Add @11084; ParseGuidSafe @11086; GetString @11086; IsDBNull @11089; GetInt32 @11090; Add @11110; DispatchToUi @11125; Clear @11127; Clear @11128; Clear @11129; Clear @11130; Equals @11134; Add @11135; Add @11137; Add @11139; Add @11141; Clear @11143; Add @11144; FirstOrDefault @11149; Equals @11149; FirstOrDefault @11155; ToList @11161; FirstOrDefault @11162; FirstOrDefault @11166; FirstOrDefault @11171; ApplySaleUnitDefaultsToCatalog @11176; RaisePropertyChanged @11177; nameof @11177; RefreshWorkspaceCategories @11179; SafeError @11184 | FROM product_categories @11076; FROM uoms @11102 |
| <span id="m-08bf423ec2c2"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>11188–11202 | ResolveProductSaleUnitFactor @11192; Round @11198; ApplyFilter @11201 | No extracted literal effects. |
| <span id="m-eeadcd963a94"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>11204–11222 | FirstOrDefault @11206; Equals @11207; TryParse @11214 | No extracted literal effects. |
| <span id="m-a2cb6611b81a"></span><code>MainViewModel.OpenAddCategoryForCurrentKindAsync()</code><br>11224–11239 | CheckSessionUnlocked @11226; HasPermission @11227; OpenCategoryManagerAsync @11233; CaptureCategoryFormSnapshot @11236; RaisePropertyChanged @11237; nameof @11237 | No extracted literal effects. |
| <span id="m-b8cbc6520f20"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>11241–11263 | CheckSessionUnlocked @11243; HasPermission @11244; ConfigureAwait @11259; LoadManagedCategoriesAsync @11259; CaptureCategoryFormSnapshot @11261; RaisePropertyChanged @11262; nameof @11262 | No extracted literal effects. |
| <span id="m-4fe0ee7b3627"></span><code>MainViewModel.CloseCategoryManager()</code><br>11265–11274 | — | No extracted literal effects. |
| <span id="m-3890f5e5ade0"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>11276–11298 | CheckSessionUnlocked @11278; HasPermission @11279; ConfigureAwait @11294; LoadManagedUnitsAsync @11294; CaptureUnitFormSnapshot @11296; RaisePropertyChanged @11297; nameof @11297 | No extracted literal effects. |
| <span id="m-ccee68f49707"></span><code>MainViewModel.CloseUnitManager()</code><br>11300–11309 | — | No extracted literal effects. |
| <span id="m-a8a9d8ac178d"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>11311–11374 | Clear @11314; Clear @11315; Clear @11316; CreateCommand @11317; ConfigureAwait @11323; ExecuteReaderAsync @11323; ReadAsync @11324; Add @11326; ParseGuidSafe @11328; GetString @11328; IsDBNull @11331; GetInt32 @11332; Where @11340; Equals @11340; Add @11341; TryParse @11354; Add @11355; RefreshTargetedCategoryCollections @11368; DispatchToUi @11369; RefreshManagedCategoriesTable @11371; RefreshManagedExpenseCategoriesTable @11372 | FROM expense_categories @11345; FROM product_categories @11319; JOIN expense_records @11345 |
| <span id="m-7eb9fb5128df"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>11376–11383 | OpenCategoryManagerAsync @11378; FirstOrDefault @11379; EditManagedCategory @11382 | No extracted literal effects. |
| <span id="m-e27b00ed188d"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>11385–11393 | OpenCategoryManagerAsync @11388; FirstOrDefault @11389; EditManagedExpenseCategory @11392 | No extracted literal effects. |
| <span id="m-ee434942aa78"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>11395–11417 | DispatchToUi @11397; Clear @11399; Clear @11400; Clear @11401; Clear @11402; Where @11404; Equals @11407; Add @11408; Add @11410; Add @11412; Add @11414 | No extracted literal effects. |
| <span id="m-cd9e753ac9f6"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>11419–11431 | CaptureCategoryFormSnapshot @11429; RaisePropertyChanged @11430; nameof @11430 | No extracted literal effects. |
| <span id="m-61be485293a4"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>11433–11446 | CaptureCategoryFormSnapshot @11444; RaisePropertyChanged @11445; nameof @11445 | No extracted literal effects. |
| <span id="m-5b47803ec8ad"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>11448–11458 | Serialize @11448 | No extracted literal effects. |
| <span id="m-c71cc9e72dd1"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>11460–11470 | Serialize @11460 | No extracted literal effects. |
| <span id="m-64140b4ddc9b"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>11472–11472 | — | No extracted literal effects. |
| <span id="m-b11e5bf554a0"></span><code>MainViewModel.DiscardRegistryForm()</code><br>11474–11490 | Equals @11477; RaisePropertyChanged @11481; nameof @11481 | No extracted literal effects. |
| <span id="m-e914b5654d1b"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>11492–11619 | Equals @11503; HasPermission @11505; FirstOrDefault @11514; Trim @11519; Trim @11520; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11522; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11522; DispatchToUi @11525; SafePipelineError @11525; IsNullOrWhiteSpace @11533; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @11535; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @11535; ConfigureAwait @11544; LoadManagedCategoriesAsync @11544; LoadExpenseCategoriesAsync @11545; CaptureCategoryFormSnapshot @11555; RaisePropertyChanged @11556; nameof @11556; Trim @11574; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @11576; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @11576; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @11592; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @11592; LoadCatalogRegistryAsync @11601; ReloadCatalogAsync @11602; SafeError @11617 | No extracted literal effects. |
| <span id="m-ad61a04862ca"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>11621–11666 | HasPermission @11631; ConfigureAwait(DeactivateCategoryCommand, bool) @11644; ExecuteAsync(DeactivateCategoryCommand, bool) @11644; ConfigureAwait(ReactivateCategoryCommand, bool) @11649; ExecuteAsync(ReactivateCategoryCommand, bool) @11649; DispatchToUi @11654; SafePipelineError @11654; ConfigureAwait @11658; LoadManagedCategoriesAsync @11658; LoadCatalogRegistryAsync @11659; ReloadCatalogAsync @11660; SafeError @11664 | No extracted literal effects. |
| <span id="m-cb72657c3c5b"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>11668–11708 | HasPermission @11678; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11694; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11694; DispatchToUi @11697; SafePipelineError @11697; ConfigureAwait @11701; LoadManagedCategoriesAsync @11701; LoadExpenseCategoriesAsync @11702; SafeError @11706 | No extracted literal effects. |
| <span id="m-7860edc133be"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>11710–11810 | Clear @11713; CreateCommand @11716; ConfigureAwait @11722; ExecuteReaderAsync @11722; ReadAsync @11723; Add @11725; GetString @11727; IsDBNull @11729; GetInt32 @11733; IsNullOrWhiteSpace @11744; Equals @11748; Add @11755; Clear @11759; ExecuteReaderAsync @11764; ReadAsync @11765; GetString @11767; Where @11789; Add @11791; TryGetValue @11794; FirstOrDefault @11801; Add @11805; DispatchToUi @11808; UpdateConversionPreview @11809 | FROM store_uom_preferences @11763; FROM uoms @11718 |
| <span id="m-d6227afad011"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>11812–11819 | OpenUnitManagerAsync @11814; FirstOrDefault @11815; Equals @11815; EditManagedUnit @11818 | No extracted literal effects. |
| <span id="m-20b05870f2af"></span><code>MainViewModel.UpdateConversionPreview()</code><br>11821–11857 | IsNullOrWhiteSpace @11823; FirstOrDefault @11829; Equals @11829; TryParse @11844 | No extracted literal effects. |
| <span id="m-b93644f87b7a"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11859–11880 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11866; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11866; DispatchToUi @11869; SafePipelineError @11873; SafeError @11878 | No extracted literal effects. |
| <span id="m-98d6d7edf52c"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11882–11895 | IsNullOrWhiteSpace @11888; TryParse @11891; CaptureUnitFormSnapshot @11893; RaisePropertyChanged @11894; nameof @11894 | No extracted literal effects. |
| <span id="m-efab9000f10f"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>11897–11959 | IsNullOrWhiteSpace @11909; Trim @11913; Trim @11914; Trim @11917; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @11918; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @11918; DispatchToUi @11921; SafePipelineError @11921; Trim @11928; Equals @11931; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @11936; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @11936; ConfigureAwait @11944; LoadManagedUnitsAsync @11944; LoadCatalogRegistryAsync @11945; CaptureUnitFormSnapshot @11952; RaisePropertyChanged @11953; nameof @11953; SafeError @11957 | No extracted literal effects. |
| <span id="m-1f909c3730a1"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>11961–11999 | ConfigureAwait(DeactivateUomCommand, bool) @11978; ExecuteAsync(DeactivateUomCommand, bool) @11978; ConfigureAwait(ReactivateUomCommand, bool) @11983; ExecuteAsync(ReactivateUomCommand, bool) @11983; DispatchToUi @11988; SafePipelineError @11988; ConfigureAwait @11992; LoadManagedUnitsAsync @11992; LoadCatalogRegistryAsync @11993; SafeError @11997 | No extracted literal effects. |
| <span id="m-c611a5326a6f"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>12001–12039 | CreateCommand @12006; CreateParameter @12013; ToString @12015; Add @12016; ConfigureAwait @12018; ExecuteReaderAsync @12018; Clear @12019; ReadAsync @12020; Add @12022; ParseGuidSafe @12024; GetString @12024; GetInt32 @12027; IsDBNull @12029; ToDecimal @12029; GetDouble @12029; DispatchToUi @12037; SafeError @12037 | FROM item_locations @12007 |
| <span id="m-236e3612de55"></span><code>MainViewModel.OpenLocationsModal()</code><br>12042–12068 | CheckSessionUnlocked @12044; HasPermission @12045; LoadFacilitiesAndBinsAsync @12066 | No extracted literal effects. |
| <span id="m-2e941f936e22"></span><code>MainViewModel.OpenAddFacility()</code><br>12070–12078 | — | No extracted literal effects. |
| <span id="m-3028cc451fb8"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>12080–12089 | — | No extracted literal effects. |
| <span id="m-b4df3597914d"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>12091–12150 | HasPermission @12094; IsNullOrWhiteSpace @12099; IsNullOrEmpty @12115; Trim @12117; Trim @12117; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @12118; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @12118; OpenAddFacility @12122; ConfigureAwait @12123; LoadFacilitiesAndBinsAsync @12123; DispatchToUi @12127; SafePipelineError @12127; ConfigureAwait(CreateFacilityCommand, FacilityDto) @12133; ExecuteAsync(CreateFacilityCommand, FacilityDto) @12133; SafeError @12148 | No extracted literal effects. |
| <span id="m-512b8d0e12e3"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>12152–12183 | HasPermission @12155; ConfigureAwait(DeactivateFacilityCommand, bool) @12167; ExecuteAsync(DeactivateFacilityCommand, bool) @12167; OpenAddFacility @12171; ConfigureAwait @12172; LoadFacilitiesAndBinsAsync @12172; DispatchToUi @12176; SafePipelineError @12176; SafeError @12181 | No extracted literal effects. |
| <span id="m-a35b134ce47d"></span><code>MainViewModel.OpenAddBin()</code><br>12185–12196 | FirstOrDefault @12195 | No extracted literal effects. |
| <span id="m-63ad638c8abc"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>12198–12210 | FirstOrDefault @12208 | No extracted literal effects. |
| <span id="m-a9f708778d72"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>12212–12287 | HasPermission @12215; IsNullOrWhiteSpace @12225; IsNullOrEmpty @12236; Trim @12241; Trim @12242; Trim @12243; Trim @12244; Trim @12245; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @12248; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @12248; OpenAddBin @12252; ConfigureAwait @12253; LoadFacilitiesAndBinsAsync @12253; DispatchToUi @12257; SafePipelineError @12257; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @12270; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @12270; SafeError @12285 | No extracted literal effects. |
| <span id="m-72d1d9dbbc0d"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>12289–12320 | HasPermission @12292; ConfigureAwait(DeactivateLocationBinCommand, bool) @12304; ExecuteAsync(DeactivateLocationBinCommand, bool) @12304; OpenAddBin @12308; ConfigureAwait @12309; LoadFacilitiesAndBinsAsync @12309; DispatchToUi @12313; SafePipelineError @12313; SafeError @12318 | No extracted literal effects. |
| <span id="m-b967591e573e"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>12322–12375 | HasPermission @12330; IsNullOrWhiteSpace @12335; Trim @12347; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @12355; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @12355; ConfigureAwait @12363; LoadItemLocationEligibilitiesAsync @12363; DispatchToUi @12368; SafePipelineError @12368; SafeError @12373 | No extracted literal effects. |
| <span id="m-32a5b7b1ac94"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>12377–12407 | HasPermission @12380; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @12392; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @12392; ConfigureAwait @12395; LoadItemLocationEligibilitiesAsync @12395; DispatchToUi @12400; SafePipelineError @12400; SafeError @12405 | No extracted literal effects. |
| <span id="m-2e0ec606ba87"></span><code>MainViewModel.LoadCustomersAsync()</code><br>12410–12443 | NewGuid @12418; Clear @12424; Add @12425; FilterCustomers @12427; ConfigureAwait @12434; GetCustomersAsync @12434; DispatchToUi @12441; SafeError @12441 | No extracted literal effects. |
| <span id="m-5fc6a2eb4a51"></span><code>MainViewModel.FilterCustomers()</code><br>12445–12458 | Clear @12447; Trim @12448; IsNullOrWhiteSpace @12449; Where @12451; Contains @12451; Contains @12452; Contains @12453; Add @12456 | No extracted literal effects. |
| <span id="m-9616ca007d01"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>12460–12496 | CheckSessionUnlocked @12462; CreateCommand @12471; CreateParameter @12474; ToString @12476; Add @12477; ConfigureAwait @12478; ExecuteScalarAsync @12478; ToString @12479; Equals @12482; LoadPickerCandidatesAsync @12494; DispatchToUi @12495 | FROM items @12473 |
| <span id="m-24d2f6136f9f"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>12498–12559 | ConfigureAwait @12505; GetLotCandidatesAsync @12505; DispatchToUi @12508; Clear @12510; Add @12513; ToString @12522; GetSerialCandidatesAsync @12530; Clear @12535; Add @12538; ToString @12547 | No extracted literal effects. |
| <span id="m-79e828cb2c17"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>12561–12567 | Clear @12564; Clear @12565 | No extracted literal effects. |
| <span id="m-0af125a823d6"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>12569–12628 | FirstOrDefault @12582; ConfigureAwait(SelectLotForCartLineCommand, bool) @12590; ExecuteAsync(SelectLotForCartLineCommand, bool) @12590; DispatchToUi @12593; SafePipelineError @12593; ToList @12599; Where @12599; ConfigureAwait(SelectSerialForCartLineCommand, bool) @12609; ExecuteAsync(SelectSerialForCartLineCommand, bool) @12609; SafeError @12626 | No extracted literal effects. |
| <span id="m-aaa28050f744"></span><code>MainViewModel.OpenCustomerChooser()</code><br>12630–12638 | CheckSessionUnlocked @12632; Clear @12635; LoadCustomersAsync @12636 | No extracted literal effects. |
| <span id="m-533b1f27b205"></span><code>MainViewModel.CloseCustomerChooser()</code><br>12640–12643 | — | No extracted literal effects. |
| <span id="m-85fe81ab0d4e"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>12645–12662 | SaveDurableCartAsync @12655; IsNullOrWhiteSpace @12659; ToString @12659; NewGuid @12659; RecordSuccessfulSearchUseAsync @12660; FromGuid @12660 | No extracted literal effects. |
| <span id="m-5e5b6be11eb1"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>12664–12673 | SaveDurableCartAsync @12672 | No extracted literal effects. |
| <span id="m-cdc792df29c2"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>12675–12720 | CheckSessionUnlocked @12677; IndexOf @12681; SelectWalkInCustomer @12687; FilterCustomers @12689; ConfigureAwait(DeactivateCustomerCommand, bool) @12701; ExecuteAsync(DeactivateCustomerCommand, bool) @12701; ConfigureAwait @12708; LoadCustomersAsync @12708; DispatchToUi @12713; SafePipelineError @12713; SafeError @12718 | No extracted literal effects. |
| <span id="m-91f492f51af6"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>12849–12888 | Add @12855; NewGuid @12856; RefreshManufacturingTablesAsync @12870; ConfigureAwait @12878; GetKitsAsync @12878; Clear @12879; Add @12880; DispatchToUi @12886; SafeError @12886 | No extracted literal effects. |
| <span id="m-dcf3cc637bda"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12892–12908 | CheckSessionUnlocked @12894; SetProductionActionMode @12896; FirstOrDefault @12901; LoadProductionIngredientLotsAsync @12906; TakeProductionSnapshot @12907 | No extracted literal effects. |
| <span id="m-88674692712c"></span><code>MainViewModel.CloseProductionModal()</code><br>12910–12924 | — | No extracted literal effects. |
| <span id="m-728c20167e2c"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>12926–13025 | ExecuteExistingProductionAsync @12929; Resolve @12951; NewGuid @12954; ToUpperInvariant @12956; ToString @12956; Insert @12974; IsNullOrWhiteSpace @12996; Trim @12996; ToDictionary @12998; Where @12998; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @13002; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @13002; DispatchToUi @13005; SafePipelineError @13005; RecordSuccessfulSearchUseAsync @13012; FromGuid @13012; ConfigureAwait @13015; LoadManufacturingDataAsync @13015; LoadInventoryAsync @13016; SafeError @13022 | No extracted literal effects. |
| <span id="m-e4aec64f0529"></span><code>MainViewModel.CloseXReportModal()</code><br>13124–13127 | — | No extracted literal effects. |
| <span id="m-cce249671c2f"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>13129–13159 | CheckSessionUnlocked @13131; Clear @13149; Where @13150; GetUnlockCandidates @13150; Equals @13151; Add @13155 | No extracted literal effects. |
| <span id="m-7d650238e79a"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>13161–13165 | — | No extracted literal effects. |
| <span id="m-a4b883af51a7"></span><code>MainViewModel.CloseZReportModal()</code><br>13167–13170 | — | No extracted literal effects. |
| <span id="m-32edd75b142d"></span><code>MainViewModel.LoadReportDataAsync()</code><br>13172–13289 | ToString @13192; DispatchToUi @13208; ConfigureAwait @13236; ExecuteAsync @13236; Join @13238; Select(string, Money) @13238; InvoiceMoney @13238; ToDecimal @13241; ToDecimal @13242; ToDecimal @13243; ToDecimal @13244; ToDecimal @13246; ToDecimal @13248; ToDecimal @13249; ToDecimal @13250; ToDecimal @13251; ToDecimal @13252; ToUpperInvariant @13254; ToString @13254; ToString @13256; ToString @13257; Sum @13263; ToDecimal @13263; ToDecimal @13266; Add @13268; Format @13273; SafeError @13281 | No extracted literal effects. |
| <span id="m-eb8c6a455df5"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>13291–13380 | CheckSessionUnlocked @13294; IsNullOrWhiteSpace @13311; AuthenticateSelectedUser @13319; Trim @13321; Round @13330; Trim @13334; ConfigureAwait(CloseShiftCommand, Shift) @13338; ExecuteAsync(CloseShiftCommand, Shift) @13338; DispatchToUi @13356; SafePipelineError @13356; ConfigureAwait @13363; ExecuteAsync @13363; SetActiveCashier @13367; RefreshUnlockCandidates @13368; RaisePropertyChanged @13369; nameof @13369; LoadReportDataAsync @13373; LoadTeamsStaffAsync @13374; SafeError @13378 | No extracted literal effects. |
| <span id="m-49d088a2d00e"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>13382–13458 | FirstOrDefault @13384; CreateCommand @13391; CreateParameter @13406; ToString @13408; Add @13409; ExecuteReader @13411; Read @13412; Parse @13414; GetString @13414; GetInt64 @13417; Pow @13419; IsDBNull @13421; TryParse @13427; GetInt32 @13428; Add @13451 | FROM barcodes @13392; FROM items @13392; JOIN barcodes @13392; JOIN product_categories @13392 |
| <span id="m-7ee8eb87acd2"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>13460–13585 | IsNullOrWhiteSpace @13462; Trim @13465; ToList @13468; Where @13468; IsNullOrEmpty @13469; Equals @13469; Any @13470; ToString @13472; AddToCart @13482; CreateCommand @13498; CreateParameter @13516; Add @13519; ExecuteReader @13521; Read @13523; Parse @13525; GetString @13525; ContainsKey @13526; GetInt64 @13530; Pow @13532; IsDBNull @13534; TryParse @13540; GetInt32 @13541; First @13570; Add @13575 | FROM barcodes @13499; FROM items @13499; JOIN barcodes @13499; JOIN product_categories @13499 |
| <span id="m-628526eb9bc4"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>13587–13630 | IsNullOrWhiteSpace @13589; Trim @13592; AppendReceiveSerialScan @13598; TryAddUniqueExactMatchToCart @13604; Clear @13606; ToList @13611; Where @13611; Equals @13611; Equals @13611; AddToCart @13614 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/SearchState.cs</code> · 514 lines.

SHA-256: <code>bef8f88e99d06df6e21a705b38a6ee70324c9df1d149bddee000c311bf49ec28</code>.

Declarations: <code>SearchSelectionStatus</code> (line 12), <code>SearchSelectionResult</code> (line 20), <code>SearchState : ReactiveObject, IDisposable</code> (line 41), <code>SearchRequestSnapshot</code> (line 54).

<details markdown>
<summary>Methods, calls, table effects and failures (17)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-1efe4e215fdb"></span><code>SearchSelectionResult.Accepted()</code><br>33–33 | — | No extracted literal effects. |
| <span id="m-1eb37beb5c22"></span><code>SearchSelectionResult.Rejected(string?)</code><br>34–34 | — | No extracted literal effects. |
| <span id="m-fdba8268e1fb"></span><code>SearchSelectionResult.Ignored(string?)</code><br>35–35 | — | No extracted literal effects. |
| <span id="m-63437e5db781"></span><code>SearchSelectionResult.Failed(string?)</code><br>36–36 | — | No extracted literal effects. |
| <span id="m-e9d02d15bca8"></span><code>SearchState.Invalidate()</code><br>84–100 | Increment @88; Cancel @90; Dispose @91 | No extracted literal effects. |
| <span id="m-9e7acc1ddacf"></span><code>SearchState.SelectOptionAsync(SearchOption?,CancellationToken)</code><br>124–174 | Ignored @126; Invalidate @128; RaisePropertyChanged @134; nameof @134; Invoke @136; ConfigureAwait @141; _onSelectedAsync @141; ParseEntityKey @149; Failed @169; Accepted @173 | No extracted literal effects. |
| <span id="m-ac20987126c0"></span><code>SearchState.GetCurrentContext()</code><br>267–279 | _contextWithConfigSupplier @271; _operatorWorkspaceSupplier @275 | No extracted literal effects. |
| <span id="m-2213626155a0"></span><code>SearchState.IsContextValid(SearchRequestSnapshot)</code><br>281–292 | GetCurrentContext @283 | No extracted literal effects. |
| <span id="m-6427730ea7dd"></span><code>SearchState.RestartDebounce()</code><br>294–322 | Cancel @298; Dispose @299; Run @307; ConfigureAwait @311; Delay @311; TriggerSearchAsync @314 | No extracted literal effects. |
| <span id="m-6b5eb17786ae"></span><code>SearchState.FlushAsync()</code><br>324–333 | Cancel @328; Dispose @329; ConfigureAwait @332; TriggerSearchAsync @332 | No extracted literal effects. |
| <span id="m-3cd832f741d3"></span><code>SearchState.RefreshScopeAsync(bool)</code><br>335–346 | Invalidate @337; ConfigureAwait @340; TriggerSearchAsync @340; RestartDebounce @344 | No extracted literal effects. |
| <span id="m-34101df4126a"></span><code>SearchState.TriggerSearchAsync()</code><br>348–435 | Increment @357; Cancel @358; Dispose @359; GetCurrentContext @364; Invoke @371; ConfigureAwait @377; RunOnUIThreadAsync @377; GetSuggestionsAsync @388; IsContextValid @393; Clear @401; Add @404; ToString @404 | No extracted literal effects. |
| <span id="m-e03284169a0c"></span><code>SearchState.Clear()</code><br>438–465 | Invalidate @444; RaisePropertyChanged @446; nameof @446; Clear @451; _onSelectedAsync @457; Invoke @459 | No extracted literal effects. |
| <span id="m-db7aba94337d"></span><code>SearchState.RecordUsageAsync(string,SearchEntityKey,CancellationToken)</code><br>467–483 | IsNullOrWhiteSpace @469; ConfigureAwait @473; RecordUseAsync @473 | No extracted literal effects. |
| <span id="m-98c363b95c5e"></span><code>SearchState.ParseEntityKey(string)</code><br>485–493 | IndexOf @487 | No extracted literal effects. |
| <span id="m-c28432112b8d"></span><code>SearchState.RunOnUIThreadAsync(Action)</code><br>495–505 | CheckAccess @497; action @499; InvokeAsync @503 | No extracted literal effects. |
| <span id="m-5fbe2dd89e98"></span><code>SearchState.Dispose()</code><br>507–513 | Invalidate @511; Clear @512 | No extracted literal effects. |

</details>

## MainWindow.axaml.cs {#src-49e81864bc35}

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml.cs</code> · 2,090 lines.

SHA-256: <code>8624a420c9eb250a8b70ac04e4aebb62015ec414e0349ab562d1fd05c510cee1</code>.

Declarations: <code>MainWindow : Window</code> (line 41).

<details markdown>
<summary>Methods, calls, table effects and failures (37)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3c1c4758ed38"></span><code>MainWindow.ReportCodeBehindError(string,string,Exception)</code><br>139–159 | Localize @143; Report @147; Post @157; Record @157 | No extracted literal effects. |
| <span id="m-07ba14955706"></span><code>MainWindow.OnDataContextChanged(object?,EventArgs)</code><br>163–169 | ObserveViewModel @167 | No extracted literal effects. |
| <span id="m-59e16fc16a3b"></span><code>MainWindow.ObserveViewModel(MainViewModel?)</code><br>173–225 | ReferenceEquals @177 | No extracted literal effects. |
| <span id="m-9b07a37b57a4"></span><code>MainWindow.OnFocusSearchRequested()</code><br>229–247 | FindControl(TextBox) @233; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @233; FindControl(TextBox) @233; Focus @239; SelectAll @241 | No extracted literal effects. |
| <span id="m-b62df2403895"></span><code>MainWindow.OnFocusReceiveSerialRequested()</code><br>251–281 | Post @259; FindControl(ItemsControl) @263; LastOrDefault(TextBox) @265; OfType(TextBox) @265; GetVisualDescendants @265; Focus @271; SelectAll @273 | No extracted literal effects. |
| <span id="m-e6986d0e3f4d"></span><code>MainWindow.OnImportFilePickerRequested()</code><br>285–337 | OpenFilePickerAsync @303; Localize @307; PreviewImportFileAsync @323; ReportCodeBehindError @333 | No extracted literal effects. |
| <span id="m-cfcb4f51fb7a"></span><code>MainWindow.OnThirdPartyImportFilePickerRequested()</code><br>341–387 | OpenFilePickerAsync @351; PreviewThirdPartyImportFileAsync @369; FocusThirdPartyImportCloseButton @375; ReportCodeBehindError @383 | No extracted literal effects. |
| <span id="m-c265f561a504"></span><code>MainWindow.OnThirdPartyTemplateSaveRequested(byte[])</code><br>391–391 | SaveImportTemplateAsync @391 | No extracted literal effects. |
| <span id="m-68d58eaf2566"></span><code>MainWindow.OnCompletedImportSaveRequested(byte[],string)</code><br>395–421 | SaveImportTemplateAsync @413; ReferenceEquals @413; ReportImportResultSave @415 | No extracted literal effects. |
| <span id="m-5f89948c5d12"></span><code>MainWindow.OnInventoryTemplateSaveRequested(byte[])</code><br>423–423 | SaveImportTemplateAsync @423 | No extracted literal effects. |
| <span id="m-03849ec2e765"></span><code>MainWindow.SaveImportTemplateAsync(byte[],string,Func&lt;bool&gt;?)</code><br>425–483 | Invoke @433; GetDownloadsFolderPath @435; IsNullOrWhiteSpace @437; Exists @437; TryGetFolderFromPathAsync @439; SaveFilePickerAsync @443; OpenWriteAsync @461; SetLength @465; WriteAsync @467; ReportCodeBehindError @477 | No extracted literal effects. |
| <span id="m-cbceb2258998"></span><code>MainWindow.GetDownloadsFolderPath()</code><br>487–517 | IsWindows @491; SHGetKnownFolderPath @497; PtrToStringUni @505; FreeCoTaskMem @513 | No extracted literal effects. |
| <span id="m-afca8eb7c3fb"></span><code>MainWindow.SHGetKnownFolderPath(Guid,uint,IntPtr,IntPtr)</code><br>521–523 | — | No extracted literal effects. |
| <span id="m-bd6ca2b33631"></span><code>MainWindow.OnCopyToClipboardRequested(string)</code><br>527–553 | SetTextAsync @539; ReportCodeBehindError @549 | No extracted literal effects. |
| <span id="m-baf6281fcce3"></span><code>MainWindow.OnElementGotFocus(object?,GotFocusEventArgs)</code><br>557–569 | — | No extracted literal effects. |
| <span id="m-8e762fb2d37f"></span><code>MainWindow.OnPriceInputGotFocus(object?,GotFocusEventArgs)</code><br>573–581 | Post @579 | No extracted literal effects. |
| <span id="m-392f904e9cc3"></span><code>MainWindow.OnPriceInputPointerReleased(object?,PointerReleasedEventArgs)</code><br>585–603 | FindAncestorOfType(TextBox) @599; SelectAll @601 | No extracted literal effects. |
| <span id="m-4383265d30bf"></span><code>MainWindow.GetActiveEditableTextBox()</code><br>607–651 | IsAttachedToVisualTree @613; FindControl(TextBox) @635; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @635; FindControl(TextBox) @635 | No extracted literal effects. |
| <span id="m-516a2acc8384"></span><code>MainWindow.InsertTextIntoTextBox(TextBox,string)</code><br>655–711 | Min @665; Max @667; Insert @677; Remove @677; Clamp @695; Insert @697 | No extracted literal effects. |
| <span id="m-0bc43cc57f10"></span><code>MainWindow.HandleBackspaceOnTextBox(TextBox)</code><br>715–773 | Min @725; Max @727; Remove @737; Clamp @753; DeleteGraphemeAt @759 | No extracted literal effects. |
| <span id="m-2f649f5429eb"></span><code>MainWindow.HandleClearOnTextBox(TextBox)</code><br>777–789 | — | No extracted literal effects. |
| <span id="m-c6353ab371c2"></span><code>MainWindow.HandleNumericDigitOnTextBox(TextBox,string)</code><br>793–853 | Min @803; Max @805; Remove @817; Contains @823; IsNullOrEmpty @839; InsertTextIntoTextBox @851 | No extracted literal effects. |
| <span id="m-fb28f62c5ca0"></span><code>MainWindow.WireTouchControls()</code><br>857–1161 | AddHandler @861; FindControl(GetSeek.UI.Components.Controls.TouchKeyboardControl) @865; FindControl(Border) @867; WireDraggableFloatingSurface @877; GetActiveEditableTextBox @887; HandleNumericDigitOnTextBox @893; Execute @901; InsertTextIntoTextBox @919; HandleBackspaceOnTextBox @945; HandleClearOnTextBox @971; FindControl(GetSeek.UI.Components.Controls.TouchNumpadControl) @1009; Execute @1035; Execute @1071; Execute @1107; Execute @1145 | No extracted literal effects. |
| <span id="m-3def33e65cd5"></span><code>MainWindow.WireDraggableFloatingSurface(Control,Control)</code><br>1165–1279 | AddHandler @1193; GetCurrentPoint @1197; FindAncestorOfType(Button) @1201; FindAncestorOfType(TextBox) @1203; FindAncestorOfType(Avalonia.Controls.Primitives.ScrollBar) @1205; GetPosition @1217; Capture @1223; ReferenceEquals @1261; EndDrag @1275 | No extracted literal effects. |
| <span id="m-dcad6d63d15c"></span><code>MainWindow.OnChooseQrImage(object?,RoutedEventArgs)</code><br>1283–1283 | ChoosePaymentImageAsync @1283 | No extracted literal effects. |
| <span id="m-c297b97ef70a"></span><code>MainWindow.OnChooseBankImage(object?,RoutedEventArgs)</code><br>1285–1285 | ChoosePaymentImageAsync @1285 | No extracted literal effects. |
| <span id="m-e9af39e9d8a2"></span><code>MainWindow.ChoosePaymentImageAsync(bool)</code><br>1289–1385 | OpenFilePickerAsync @1299; Localize @1305; OpenReadAsync @1331; Localize @1337; ReadAsync @1349; WriteAsync @1363; AsMemory @1363; ToArray @1367; SetManualPaymentImage @1371; ReportCodeBehindError @1379 | No extracted literal effects. |
| <span id="m-58c056cd652f"></span><code>MainWindow.OnChooseExpenseReceiptImage(object?,RoutedEventArgs)</code><br>1389–1441 | OpenFilePickerAsync @1399; OpenReadAsync @1427; SetExpenseFormAttachmentAsync @1429; ReportCodeBehindError @1437 | No extracted literal effects. |
| <span id="m-cd061d04c041"></span><code>MainWindow.OnKeyDown(KeyEventArgs)</code><br>1445–1599 | OnKeyDown @1481; CanCaptureUnfocusedBarcodeWedge @1497; Clear @1501; ToString @1523; HandleBarcodeScanned @1535; GetPrintableCharacterFromKey @1553; IsNullOrEmpty @1555; Append @1565 | No extracted literal effects. |
| <span id="m-69443289bd49"></span><code>MainWindow.CanCaptureUnfocusedBarcodeWedge()</code><br>1603–1639 | GetTopLevel @1621; GetFocusedElement @1621; FindAncestorOfType(GetSeek.UI.Components.Controls.CompactDateField) @1625; GetType @1627 | No extracted literal effects. |
| <span id="m-9f9ba3747fb2"></span><code>MainWindow.OnPreviewKeyboardAction(object?,KeyEventArgs)</code><br>1643–1835 | FirstOrDefault(GetSeek.UI.Components.Controls.CompactDateField) @1651; OfType(GetSeek.UI.Components.Controls.CompactDateField) @1651; GetVisualDescendants @1651; FirstOrDefault(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1671; OfType(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1671; TryHandleEscapeKey @1691; HandlePhysicalBackspace @1713; GetTopLevel @1729; GetFocusedElement @1729; IsWithinThirdPartyImportOverlay @1731; TryActivateFocusedButton @1735; FindControl(GetSeek.UI.Components.Controls.ModalShell) @1747; FindControl(Button) @1747; Focus @1747; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1779; ReferenceEquals @1781; IsVisualAncestorOf @1781; SelectOption @1791; Trim @1801; IsNullOrEmpty @1803; TryAddUniqueExactMatchToCart @1807; Clear @1811 | No extracted literal effects. |
| <span id="m-f131f43e8d8f"></span><code>MainWindow.TryActivateFocusedButton()</code><br>1839–1893 | GetTopLevel @1847; GetFocusedElement @1849; CanExecute @1865; Execute @1879; RaiseEvent @1887 | No extracted literal effects. |
| <span id="m-2604658bfb50"></span><code>MainWindow.IsWithinThirdPartyImportOverlay(Visual)</code><br>1897–1915 | FindControl(GetSeek.UI.Components.Controls.ModalShell) @1901; GetVisualParent @1903 | No extracted literal effects. |
| <span id="m-2a658bb28418"></span><code>MainWindow.FocusThirdPartyImportCloseButton()</code><br>1919–1925 | Post @1923; FindControl(GetSeek.UI.Components.Controls.ModalShell) @1923; FindControl(Button) @1923; Focus @1923 | No extracted literal effects. |
| <span id="m-ff4e183aea6e"></span><code>MainWindow.HandlePhysicalBackspace()</code><br>1929–1993 | HandleBackspaceOnTextBox @1947; Execute @1959; Execute @1971; Execute @1983 | No extracted literal effects. |
| <span id="m-2dd3c8db0d65"></span><code>MainWindow.GetPrintableCharacterFromKey(Key,KeyModifiers)</code><br>1997–2033 | ToString @2009; ToUpperInvariant @2009; ToString @2009 | No extracted literal effects. |
| <span id="m-c2ae7bc5f70f"></span><code>MainWindow.OnKeyUp(KeyEventArgs)</code><br>2037–2087 | OnKeyUp @2085 | No extracted literal effects. |

</details>

## AXAML, migrations and project inputs

### App.axaml {#src-1e635b06c6de}

<code>Software/src/GetSeek.Desktop/App.axaml</code> · 37 lines · SHA-256 <code>fbcb9d4c8bbedcd7ab20df886f595435317e99118d45946f85f9cb14b023ed01</code>.

### GetSeek.Desktop.csproj {#src-2f265207af15}

<code>Software/src/GetSeek.Desktop/GetSeek.Desktop.csproj</code> · 27 lines · SHA-256 <code>57c435b4d7b778cfe77cd7da0397f3607a8ad46a8db4dfcd71d522dd51ee3bdb</code>.

### MainWindow.axaml {#src-67243af94cf2}

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml</code> · 6362 lines · SHA-256 <code>5910bd1ac8ca2eb028707dbc36ed9837910ccbdcdcb02a1f097f2a68a202dee0</code>.
