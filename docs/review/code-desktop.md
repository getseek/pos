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

SHA-256: <code>94796e1bb6b4ef910b68c628447480bf1e4f77aa458704753bc7317e9b4486f0</code>.

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

<code>Software/src/GetSeek.Desktop/Services/UiPreferencesService.cs</code> · 4,945 lines.

SHA-256: <code>4a767e6186915687d433b7514d7217c8aea99f16a706f6a0629a0755c3f0be23</code>.

Declarations: <code>UiPreferences</code> (line 12), <code>IUiPreferencesService</code> (line 48), <code>UiPreferencesService : IUiPreferencesService</code> (line 58), <code>ILocalizationService</code> (line 118), <code>LocalizationService : ILocalizationService</code> (line 128), <code>ThemeManager</code> (line 4836).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b1fcacbd5058"></span><code>UiPreferences.NormalizeCatalogueMode(string?)</code><br>24–33 | IsNullOrWhiteSpace @26; Equals @29 | No extracted literal effects. |
| <span id="m-c7cc62243ce4"></span><code>IUiPreferencesService.Load()</code><br>50–50 | — | No extracted literal effects. |
| <span id="m-ea32130cd52e"></span><code>IUiPreferencesService.Save(UiPreferences)</code><br>51–51 | — | No extracted literal effects. |
| <span id="m-b6d9b7254e93"></span><code>UiPreferencesService.Load()</code><br>75–93 | Exists @79; ReadAllText @81; Deserialize(UiPreferences) @82; NormalizeCatalogueMode @83 | No extracted literal effects. |
| <span id="m-53bebcf56e5b"></span><code>UiPreferencesService.Save(UiPreferences)</code><br>95–114 | NormalizeCatalogueMode @100; GetDirectoryName @102; IsNullOrEmpty @103; CreateDirectory @105; WriteAllText @108; Serialize @108 | No extracted literal effects. |
| <span id="m-41d7bc73da6a"></span><code>ILocalizationService.Localize(string,object?[])</code><br>121–121 | — | No extracted literal effects. |
| <span id="m-e282c58393cb"></span><code>LocalizationService.Localize(string,object?[])</code><br>4803–4833 | ToLowerInvariant @4805; Trim @4805; TryGetValue @4813; TryGetValue @4816; Format @4826 | No extracted literal effects. |
| <span id="m-ddbe6978226e"></span><code>ThemeManager.Resolve(string?)</code><br>4853–4854 | IsNullOrWhiteSpace @4854; ContainsKey @4854 | No extracted literal effects. |
| <span id="m-3a829f3c57ea"></span><code>ThemeManager.DisplayName(string?)</code><br>4856–4856 | Resolve @4856 | No extracted literal effects. |
| <span id="m-778f27358cfc"></span><code>ThemeManager.NextTheme(string?)</code><br>4859–4872 | Equals @4864 | No extracted literal effects. |
| <span id="m-0e0ab399d459"></span><code>ThemeManager.Apply(string?)</code><br>4875–4909 | Equals @4878; Resolve @4880; SwapThemeSlot @4894; CheckAccess @4899; Post @4901; ApplyCore @4905 | No extracted literal effects. |
| <span id="m-3933eb753f12"></span><code>ThemeManager.IsThemeInclude(object)</code><br>4912–4914 | Contains @4914 | No extracted literal effects. |
| <span id="m-75ddc7941eba"></span><code>ThemeManager.SwapThemeSlot(IList&lt;IResourceProvider&gt;,string)</code><br>4916–4939 | ToList(ResourceInclude) @4920; Where(ResourceInclude) @4920; OfType(ResourceInclude) @4920; Remove @4922; Equals @4927; Add @4938 | No extracted literal effects. |

</details>

## CatalogOrderPageHelper.cs {#src-88c3ed51d197}

<code>Software/src/GetSeek.Desktop/ViewModels/CatalogOrderPageHelper.cs</code> · 490 lines.

SHA-256: <code>46345de9d72c3f2093a1865bc03d5b6ee393740c11e62ee7cfef875ec34bfd04</code>.

Declarations: <code>CatalogFamily</code> (line 9), <code>AllItemCycleState</code> (line 15), <code>NocodeCycleState</code> (line 23), <code>CatalogModeOption</code> (line 30), <code>CatalogCycleStateMachine</code> (line 44), <code>CatalogFilterRequest</code> (line 203), <code>CatalogFilterResult</code> (line 217), <code>CatalogOrderPageHelper</code> (line 225).

<details markdown>
<summary>Methods, calls, table effects and failures (28)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-03493a08e45c"></span><code>CatalogModeOption.ToString()</code><br>41–41 | — | No extracted literal effects. |
| <span id="m-1bbafdb6dffa"></span><code>CatalogCycleStateMachine.ResetToDefault(AllItemCycleState)</code><br>56–62 | — | No extracted literal effects. |
| <span id="m-b566bbd936c5"></span><code>CatalogCycleStateMachine.ParseAllItemState(string?)</code><br>64–74 | IsNullOrWhiteSpace @66; Equals @67; nameof @67 | No extracted literal effects. |
| <span id="m-9ce0934092da"></span><code>CatalogCycleStateMachine.FormatAllItemState(AllItemCycleState)</code><br>76–82 | nameof @78 | No extracted literal effects. |
| <span id="m-7eb303dc5ade"></span><code>CatalogCycleStateMachine.GetNextAllItemState(AllItemCycleState)</code><br>84–91 | — | No extracted literal effects. |
| <span id="m-1a68ab91219b"></span><code>CatalogCycleStateMachine.GetNextNocodeState(NocodeCycleState)</code><br>93–99 | — | No extracted literal effects. |
| <span id="m-28ee969474be"></span><code>CatalogCycleStateMachine.GetAllItemCaption(AllItemCycleState)</code><br>101–108 | — | No extracted literal effects. |
| <span id="m-f08ee6623dba"></span><code>CatalogCycleStateMachine.GetAllItemCaption(AllItemCycleState,ILocalizationService?)</code><br>110–121 | GetAllItemCaption @112; Localize @115 | No extracted literal effects. |
| <span id="m-f7d1d2ae5fb2"></span><code>CatalogCycleStateMachine.GetNocodeCaption(NocodeCycleState)</code><br>123–129 | — | No extracted literal effects. |
| <span id="m-a2d50bdc9659"></span><code>CatalogCycleStateMachine.GetNocodeCaption(NocodeCycleState,ILocalizationService?)</code><br>131–141 | GetNocodeCaption @133; Localize @136 | No extracted literal effects. |
| <span id="m-61733def978e"></span><code>CatalogCycleStateMachine.SelectOrCycleAllItem()</code><br>150–160 | GetNextAllItemState @158 | No extracted literal effects. |
| <span id="m-9e47d0fd0314"></span><code>CatalogCycleStateMachine.SelectOrCycleNocode()</code><br>162–177 | GetNextNocodeState @175 | No extracted literal effects. |
| <span id="m-c23a4eedc975"></span><code>CatalogCycleStateMachine.CycleActive()</code><br>179–189 | GetNextAllItemState @183; GetNextNocodeState @187 | No extracted literal effects. |
| <span id="m-b721e07b4aa9"></span><code>CatalogCycleStateMachine.SelectFamily(CatalogFamily)</code><br>191–200 | — | No extracted literal effects. |
| <span id="m-0a570b2af156"></span><code>CatalogOrderPageHelper.ParseAllItemState(string?)</code><br>227–227 | ParseAllItemState @227 | No extracted literal effects. |
| <span id="m-20f9b8c569a6"></span><code>CatalogOrderPageHelper.FormatAllItemState(AllItemCycleState)</code><br>228–228 | FormatAllItemState @228 | No extracted literal effects. |
| <span id="m-ff3f06ba71f2"></span><code>CatalogOrderPageHelper.CompareAtoZ(ProductItem,ProductItem)</code><br>234–243 | Compare @236; CompareTo @242 | No extracted literal effects. |
| <span id="m-9b0c8772e63c"></span><code>CatalogOrderPageHelper.CompareZtoA(ProductItem,ProductItem)</code><br>245–255 | Compare @248; CompareTo @254 | No extracted literal effects. |
| <span id="m-d986d3421500"></span><code>CatalogOrderPageHelper.CompareMostSold(ProductItem,ProductItem)</code><br>257–263 | CompareTo @259; CompareAtoZ @262 | No extracted literal effects. |
| <span id="m-8ab400180a2d"></span><code>CatalogOrderPageHelper.CompareNonBarcodeFirst(ProductItem,ProductItem)</code><br>265–272 | CompareAtoZ @271 | No extracted literal effects. |
| <span id="m-6f469dca377b"></span><code>CatalogOrderPageHelper.CompareBarcodeFirst(ProductItem,ProductItem)</code><br>274–281 | CompareAtoZ @280 | No extracted literal effects. |
| <span id="m-406917e706b6"></span><code>CatalogOrderPageHelper.CompareMostSoldNonBarcode(ProductItem,ProductItem)</code><br>283–294 | CompareMostSold @291; CompareAtoZ @293 | No extracted literal effects. |
| <span id="m-e85cf26be0bc"></span><code>CatalogOrderPageHelper.CompareMostSoldAll(ProductItem,ProductItem)</code><br>296–299 | CompareMostSold @298 | No extracted literal effects. |
| <span id="m-6362edc32057"></span><code>CatalogOrderPageHelper.HasMatchingBarcode(ProductItem,Func&lt;string, bool&gt;)</code><br>301–313 | IsNullOrEmpty @307; predicate @307 | No extracted literal effects. |
| <span id="m-137bc14ea9d7"></span><code>CatalogOrderPageHelper.MatchesSearch(ProductItem,string)</code><br>315–329 | IsNullOrWhiteSpace @317; IsNullOrEmpty @319; Contains @319; Contains @322; HasMatchingBarcode @325; Contains @325 | No extracted literal effects. |
| <span id="m-63c8c291fb71"></span><code>CatalogOrderPageHelper.GetSearchRelevanceTier(ProductItem,string)</code><br>331–361 | IsNullOrEmpty @334; Equals @334; HasMatchingBarcode @335; StartsWith @347; StartsWith @348; StartsWith @354 | No extracted literal effects. |
| <span id="m-f842a314a092"></span><code>CatalogOrderPageHelper.CompareSearchRelevance(ProductItem,ProductItem,string)</code><br>363–372 | GetSearchRelevanceTier @365; CompareTo @369; CompareAtoZ @371 | No extracted literal effects. |
| <span id="m-e79c8f742c1b"></span><code>CatalogOrderPageHelper.FilterAndPage(CatalogFilterRequest)</code><br>374–489 | ThrowIfNull @376; IsNullOrWhiteSpace @378; Trim @378; Equals @386; MatchesSearch @424; Add @429; Sort @435; CompareSearchRelevance @435; Contains @464; Empty(ProductItem) @473; Clamp @478; ToList @480; Take @480; Skip @480 | No extracted literal effects. |

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

SHA-256: <code>967ecf04eb88e77a1cdaf66f42853c5cdceb68dd78cceb82f00ca9c34cefc4e5</code>.

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

SHA-256: <code>11bedebbd6bb5ed46152c8a73a7c60fc67928411a99893a10d58b8057d4f6dde</code>.

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

SHA-256: <code>123ac02f9618a296c04f3f85391fc11d551b8a68e95166cc005656bff45a5c91</code>.

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

SHA-256: <code>278683cb8a18dec18394861ee7ecf00c3e338287da5abc60fc1693d4455f755e</code>.

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdParties.cs</code> · 4,963 lines.

SHA-256: <code>13c21acd849d9f44e138be5d460315530ec15359979e6d94f2ebe3b0e714b084</code>.

Declarations: <code>MainViewModel</code> (line 32), <code>ThirdPartyFormSnapshot</code> (line 160), <code>ItemTierPricingRow : ReactiveObject</code> (line 4738), <code>PricingRoundingOption</code> (line 4890), <code>PricingIncrementOption</code> (line 4891), <code>PricingMethodOption</code> (line 4892), <code>PricingCostBasisOption</code> (line 4893), <code>CategoryPricingPreviewProduct</code> (line 4894), <code>TierWeightModeOption</code> (line 4898), <code>PriceOfferRow</code> (line 4900), <code>PendingShelfLabelRow : ReactiveObject</code> (line 4921), <code>KitPriceAlertRow</code> (line 4943).

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
| <span id="m-9612e46fd956"></span><code>MainViewModel.RaiseLocalizedLabels()</code><br>3604–4365 | RaiseCatalogLabels @3606; RaisePropertyChanged @3607; nameof @3607; RefreshDefaultItemCatalogueOptions @3610; RefreshManufacturingLocalization @4116; RefreshTraceabilityLocalization @4117; RefreshCommercialLocalization @4118; RefreshImportLocalization @4119 | No extracted literal effects. |
| <span id="m-275653cbc562"></span><code>MainViewModel.RefreshThirdPartyList()</code><br>4370–4377 | Clear @4372; Add @4375 | No extracted literal effects. |
| <span id="m-f3c6957422b5"></span><code>MainViewModel.NullIfBlank(string?)</code><br>4379–4379 | IsNullOrWhiteSpace @4379; Trim @4379 | No extracted literal effects. |
| <span id="m-bdafeb438bcf"></span><code>MainViewModel.ParsePercent(string?)</code><br>4381–4382 | TryParse @4382 | No extracted literal effects. |
| <span id="m-75da6d4f37f4"></span><code>MainViewModel.ParseStoredPricingPercentForDisplay(string?,int)</code><br>4384–4385 | ParseStoredPercentage @4385 | No extracted literal effects. |
| <span id="m-b5227481e72d"></span><code>MainViewModel.IsIncrementRoundingRule(string?)</code><br>4387–4389 | Equals @4388 | No extracted literal effects. |
| <span id="m-25036d5d635d"></span><code>MainViewModel.ParseDate(string?)</code><br>4391–4392 | TryParse @4392 | No extracted literal effects. |
| <span id="m-61611e748619"></span><code>MainViewModel.OpenNewPriceOffer()</code><br>4490–4500 | ToString @4494; ToString @4495; AddDays @4495; FirstOrDefault @4497 | No extracted literal effects. |
| <span id="m-d43b1dd15cfa"></span><code>MainViewModel.OpenEditPriceOfferAsync(PriceOfferRow)</code><br>4502–4525 | CreateCommand @4505; CreateParameter @4508; ToString @4508; Add @4508; ConfigureAwait @4509; ExecuteReaderAsync @4509; ReadAsync @4509; Parse @4510; GetString @4510; GetInt32 @4510; IsDBNull @4512; TryParse @4512; ToString @4512; ToUniversalTime @4512; ToString @4512; ToUniversalTime @4513; AddDays @4513; FirstOrDefault @4515; TryParse @4517; FirstOrDefault @4518; Pow @4521; GetInt64 @4522 | FROM price_offers @4505; JOIN items @4505 |
| <span id="m-881cea663568"></span><code>MainViewModel.SavePriceOfferAsync()</code><br>4527–4544 | CheckSessionUnlocked @4529; TryParse @4530; ToString @4530; Round @4530; Pow @4530; IsNullOrWhiteSpace @4531; ConfigureAwait(SavePriceOfferCommand, Guid) @4540; ExecuteAsync(SavePriceOfferCommand, Guid) @4540; ReportError @4541; DispatchToUi @4542; ConfigureAwait @4543; LoadPriceOffersAsync @4543 | No extracted literal effects. |
| <span id="m-f62818f6bd45"></span><code>MainViewModel.TogglePriceOfferAsync(PriceOfferRow)</code><br>4546–4554 | CheckSessionUnlocked @4548; ConfigureAwait(SetPriceOfferStatusCommand, bool) @4550; ExecuteAsync(SetPriceOfferStatusCommand, bool) @4550; ReportError @4552; ConfigureAwait @4553; LoadPriceOffersAsync @4553 | No extracted literal effects. |
| <span id="m-82c53874276b"></span><code>MainViewModel.LoadPriceOffersAsync()</code><br>4556–4595 | CreateCommand @4561; ConfigureAwait @4571; ExecuteReaderAsync @4571; ReadAsync @4572; Add @4574; Parse @4575; GetString @4575; GetDouble @4579; GetInt64 @4582; IsDBNull @4583; GetInt32 @4585; DispatchToUi @4588; Clear @4590; Add @4591 | FROM price_offers @4562; JOIN items @4562; JOIN product_categories @4562 |
| <span id="m-51bae0bc35a5"></span><code>MainViewModel.LoadPendingShelfLabelsAsync()</code><br>4597–4636 | CreateCommand @4602; ConfigureAwait @4611; ExecuteReaderAsync @4611; ReadAsync @4612; Add @4614; Parse @4615; GetString @4615; GetInt64 @4619; GetInt32 @4624; Add @4625; Remove @4625; RaisePropertyChanged @4625; nameof @4625; Localize @4626; DispatchToUi @4629; Clear @4631; Add @4632 | FROM pending_shelf_labels @4603; JOIN items @4603 |
| <span id="m-6f34c41f8247"></span><code>MainViewModel.LoadKitPriceReviewAlertsAsync()</code><br>4638–4677 | CreateCommand @4643; ConfigureAwait @4655; ExecuteReaderAsync @4655; ReadAsync @4656; Add @4658; Parse @4659; GetString @4659; GetInt64 @4663; GetInt32 @4667; DispatchToUi @4670; Clear @4672; Add @4673 | FROM kit_price_review_alerts @4644; JOIN items @4644 |
| <span id="m-cfb62771f58c"></span><code>MainViewModel.SetKitPriceAlertStatusAsync(KitPriceAlertRow,string,string)</code><br>4679–4687 | CheckSessionUnlocked @4681; ConfigureAwait(ResolveKitPriceAlertCommand, bool) @4682; ExecuteAsync(ResolveKitPriceAlertCommand, bool) @4682; ReportError @4684; ConfigureAwait @4686; LoadKitPriceReviewAlertsAsync @4686 | No extracted literal effects. |
| <span id="m-0f948208ceda"></span><code>MainViewModel.MarkShelfLabelsPrintedAsync()</code><br>4689–4692 | ConfigureAwait @4691; SetSelectedShelfLabelStatusAsync @4691 | No extracted literal effects. |
| <span id="m-327078f6c95a"></span><code>MainViewModel.QueueSelectedShelfLabelsAsync()</code><br>4694–4706 | CheckSessionUnlocked @4696; ToArray @4697; Select @4697; Where @4697; Contains @4697; ConfigureAwait(QueueShelfLabelPrintCommand, string) @4700; ExecuteAsync(QueueShelfLabelPrintCommand, string) @4700; ReportError @4702; Clear @4703; RaisePropertyChanged @4703; nameof @4703; ConfigureAwait @4705; LoadPendingShelfLabelsAsync @4705 | No extracted literal effects. |
| <span id="m-b9dd474f53ac"></span><code>MainViewModel.SetSelectedShelfLabelStatusAsync(string)</code><br>4708–4722 | CheckSessionUnlocked @4710; ToArray @4711; Select @4711; Where @4711; Contains @4711; ConfigureAwait(SetShelfLabelStatusCommand, int) @4714; ExecuteAsync(SetShelfLabelStatusCommand, int) @4714; Trim @4715; ReportError @4717; Clear @4718; RaisePropertyChanged @4719; nameof @4719; ConfigureAwait @4721; LoadPendingShelfLabelsAsync @4721 | No extracted literal effects. |
| <span id="m-d9e0964a5bc8"></span><code>MainViewModel.AddSqlParam(DbCommand,string,object)</code><br>4728–4734 | CreateParameter @4730; Add @4733 | No extracted literal effects. |
| <span id="m-95f322908355"></span><code>ItemTierPricingRow.RecalculateEffectivePrice()</code><br>4866–4887 | Max @4871; TryParse @4880 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 13,769 lines.

SHA-256: <code>0133a2118a05d5e0203675aad2f1345356d59baa51ecc70f7a6ba1b8d28b0d95</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 9067).

<details markdown>
<summary>Methods, calls, table effects and failures (265)</summary>

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
| <span id="m-96bc48179195"></span><code>MainViewModel.UpdatePosWindowContentWidth(double)</code><br>3329–3334 | Abs @3331; RaisePropertyChanged @3333; nameof @3333 | No extracted literal effects. |
| <span id="m-d94df199d42a"></span><code>MainViewModel.UpdateCatalogViewport(double)</code><br>3343–3350 | Max @3346; Floor @3346; RaisePropertyChanged @3349; nameof @3349 | No extracted literal effects. |
| <span id="m-c4f58a26535a"></span><code>MainViewModel.ApplyDefaultCatalogueMode(string)</code><br>3715–3718 | — | No extracted literal effects. |
| <span id="m-08d5307bbbce"></span><code>MainViewModel.ResetCatalogueToDefault()</code><br>3720–3728 | ParseAllItemState @3722; RaisePropertyChanged @3724; nameof @3724; ApplyFilter @3727 | No extracted literal effects. |
| <span id="m-aa6a123237f8"></span><code>MainViewModel.RefreshDefaultItemCatalogueOptions()</code><br>3730–3745 | nameof @3734; Localize @3734; FirstOrDefault @3740; Equals @3740; RaisePropertyChanged @3741 | No extracted literal effects. |
| <span id="m-e68325185882"></span><code>MainViewModel.UpdateSelectedDefaultItemCatalogueOption()</code><br>3747–3751 | FirstOrDefault @3749; Equals @3749; RaisePropertyChanged @3750; nameof @3750 | No extracted literal effects. |
| <span id="m-f96d459fb6e9"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3780–3788 | IsNullOrWhiteSpace @3782 | No extracted literal effects. |
| <span id="m-557725d7db81"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3790–3804 | Load @3792; IsNullOrWhiteSpace @3796; Resolve @3798; NormalizeCatalogueMode @3800; ParseAllItemState @3801; RefreshDefaultItemCatalogueOptions @3802; Apply @3803 | No extracted literal effects. |
| <span id="m-afad5543d1fb"></span><code>MainViewModel.OpenImport()</code><br>3833–3841 | CheckSessionUnlocked @3835; Increment @3837; ResetInventoryImport @3838; Invoke @3840 | No extracted literal effects. |
| <span id="m-020157f2cbf8"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3843–3904 | Increment @3846; ResetInventoryImport @3851; IsNullOrWhiteSpace @3856; Exists @3856; FinishFailedImport @3858; ConfigureAwait @3870; ReadAllBytesAsync @3870; ToHexString @3871; HashData @3871; TemplateContextAsync @3875; Run @3876; Read @3876; ValidateInventoryAsync @3877; CompletedWorkbook @3878; DispatchToUi @3885; ReferenceEquals @3887; Add @3888; Localize @3889; SetImportReviewRows @3893; RaisePropertyChanged @3894; nameof @3894; ReportException @3900 | No extracted literal effects. |
| <span id="m-865310fbbf20"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3906–3960 | IsCurrentImportAttempt @3922; ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3936; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3936; ConfigureAwait @3940; RecoverImportOutcomeAsync @3940; Localize @3943; DispatchToUi @3944; FinishImportAttempt @3944; LoadInventoryAsync @3945; ReportException @3946; ReportError @3950; FinishFailedImport @3951; ImportCommandIssue @3951 | No extracted literal effects. |
| <span id="m-0dbb65c8ed69"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3972–3982 | Report @3974; DispatchToUi @3975; Insert @3977 | No extracted literal effects. |
| <span id="m-7769b6a5dc0d"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3984–3988 | RaisePropertyChanged @3987; nameof @3987 | No extracted literal effects. |
| <span id="m-963e2043d568"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3990–3993 | ReportError @3992 | No extracted literal effects. |
| <span id="m-cf278e961b98"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3999–4004 | ReportError @4002 | No extracted literal effects. |
| <span id="m-e03d59247625"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>4013–4019 | IsNullOrWhiteSpace @4015; Trim @4015; ReportError @4017 | No extracted literal effects. |
| <span id="m-f1b7010421ba"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>4021–4024 | DispatchToUi @4023; Insert @4023 | No extracted literal effects. |
| <span id="m-4037df0e1a61"></span><code>MainViewModel.DispatchToUi(Action)</code><br>4030–4044 | CheckAccess @4032; action @4034; GetResult @4042; GetAwaiter @4042; InvokeAsync @4042 | No extracted literal effects. |
| <span id="m-28fa75007a59"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4714–4779 | Register @4716; Execute @4716; Execute @4717; Execute @4718; Execute @4719; Execute @4724; Execute @4725; Execute @4726; Execute @4727; Execute @4728; Execute @4729; Execute @4730; Execute @4731; Execute @4732; Execute @4733; Execute @4734; Execute @4735; Execute @4736; Execute @4737; Execute @4738; Execute @4739; Execute @4740; Execute @4741; Execute @4742; Execute @4743; Execute @4744; Execute @4745; Execute @4746; Execute @4747; Execute @4748; Execute @4749; Execute @4750; Execute @4751; Execute @4752; Execute @4753; Execute @4754; Execute @4755; Execute @4757; Execute @4758; RequestClosePersonForm @4759; KeepEditingPersonForm @4760; CloseSalaryMonthDetailModal @4761; CloseSalaryPaymentModal @4762; CloseSalaryAdjustmentModal @4763; CloseSalaryFinalizeModal @4764; RequestCloseExpenseForm @4765; KeepEditingExpenseForm @4766; CloseExpenseCategoryModal @4767; CloseExpensePaymentModal @4768; CloseExpenseDetailModal @4769; ClosePaymentReturnModal @4770; CloseWasteExpenseConfirmation @4771; InitializeSalaryTables @4776; InitializeExpensesTables @4777; InitializeTeamsCommands @4778 | No extracted literal effects. |
| <span id="m-29f91c2d3a00"></span><code>MainViewModel.CreateDemo()</code><br>4781–4788 | SetActiveCashier @4784; Parse @4784; RefreshUnlockCandidates @4786 | No extracted literal effects. |
| <span id="m-ac5f9ab52b88"></span><code>MainViewModel.CreateInitializing()</code><br>4790–4798 | — | No extracted literal effects. |
| <span id="m-44f75cd05269"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4800–4810 | — | No extracted literal effects. |
| <span id="m-720ea71d539f"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4812–4830 | ConfigureDiagnosticsWorkspace @4826; ResolveDiagnosticsWorkspace @4826; ApplyPersistedState @4827; RefreshUnlockCandidates @4828 | No extracted literal effects. |
| <span id="m-6f74e52028d8"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4832–4860 | CheckSessionUnlocked @4834; HasPermission @4835; Equals @4846; GetFileNameWithoutExtension @4846; GetEntryAssembly @4848; Add @4850; Start @4853; ReportException @4858 | No extracted literal effects. |
| <span id="m-ee79f23dfa09"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4862–4885 | CheckSessionUnlocked @4864; HasPermission @4865; Equals @4875; GetFileNameWithoutExtension @4875; Add @4876; GetEntryAssembly @4876; Start @4878; ReportException @4883 | No extracted literal effects. |
| <span id="m-6b86601cbe88"></span><code>MainViewModel.Dispose()</code><br>4887–4908 | ClearImportResults @4890; Increment @4891; ResetFinancialWorkspace @4893; Dispose @4894; Stop @4895; CancelBatchPricingPreviewExpiry @4898; Dispose @4899; Dispose @4900; DisposeSearchStates @4906; SuppressFinalize @4907 | No extracted literal effects. |
| <span id="m-d0e9f82a4f71"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4910–4914 | Stop @4912 | No extracted literal effects. |
| <span id="m-6b2533844fc2"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4916–4954 | Clear @4926; Clear @4927; Clear @4928; Clear @4929; Clear @4930; Clear @4931; Clear @4932; Clear @4933; Clear @4934; Clear @4935 | No extracted literal effects. |
| <span id="m-3c7267c47e97"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4956–5073 | RaisePropertyChanged @4970; nameof @4970; Clear @4972; Clear @4973; Clear @4974; CreateCommand @4981; ExecuteReader @4983; Read @4984; TryParse @4986; GetString @4986; Add @4987; GroupBy @4996; Add @4998; Count @4998; Contains @5003; Equals @5026; Add @5028; ApplyFilter @5030; All @5032; SafeError @5035; SetActiveCashier @5043; ToString @5047; ToString @5050; ToLocalTime @5050; NotifyTotalsChanged @5072 | FROM item_kits @4982 |
| <span id="m-febc3fc0f968"></span><code>MainViewModel.InitializeDemoData()</code><br>5075–5153 | Add @5082; Add @5101; ApplyFilter @5112; Add @5115; Add @5120; Add @5126; ApplyActivityFilter @5132; Add @5135; ApplyInventoryFilter @5144; Add @5147; Parse @5147; NotifyTotalsChanged @5152 | No extracted literal effects. |
| <span id="m-44aabbfd5b3f"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>5155–5168 | — | No extracted literal effects. |
| <span id="m-c4c9e1fa52ef"></span><code>MainViewModel.SelectMenu(string)</code><br>5170–5243 | CheckSessionUnlocked @5172; NormalizeMenuKey @5176; LoadInvoicesAsync @5182; LoadCommercialAsync @5183; LoadActivityInvoicesAsync @5190; LoadTeamsStaffAsync @5193; LoadCatalogRegistryAsync @5194; UpdateDemoSeedingAvailabilityAsync @5197; UpdateReceiptDesignPreview @5200; RefreshDiagnosticsAsync @5201; LoadPriceLevelSettingsAsync @5202; RefreshWorkspaceCategories @5206; LoadInventoryAsync @5207; LoadPriceProposalsAsync @5209; LoadReportDataAsync @5212; LoadFinancialRegisterAsync @5213; LoadCustomersAsync @5216; LoadSuppliersAsync @5217; LoadThirdPartiesAsync @5218; LoadManufacturingDataAsync @5223; LoadManagedUnitsAsync @5231; LoadManagedCategoriesAsync @5234; LoadSalaryWorkspaceAsync @5237; LoadExpensesWorkspaceAsync @5240 | No extracted literal effects. |
| <span id="m-1e96b4f9eb06"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>5245–5264 | — | No extracted literal effects. |
| <span id="m-e812e8f744b0"></span><code>MainViewModel.LogOut()</code><br>5266–5287 | Clear @5268; RaisePropertyChanged @5271; nameof @5271; ClearNotifications @5273; ResetCashReview @5277; Lock @5280; RefreshUnlockCandidates @5285; UpdateDemoSeedingAvailabilityAsync @5286 | No extracted literal effects. |
| <span id="m-b87b053ceeef"></span><code>MainViewModel.UnlockSession()</code><br>5289–5292 | UnlockSession @5291 | No extracted literal effects. |
| <span id="m-bb5dd6f1bd4b"></span><code>MainViewModel.UnlockSession(string?)</code><br>5294–5393 | IsLockScreenLockedOut @5302; IsNullOrWhiteSpace @5318; AuthenticateSelectedUser @5327; Lock @5332; AddSeconds @5338; AddMinutes @5355; Initialize @5374; Unlock @5375; Any @5379; Equals @5379; RaisePropertyChanged @5380; nameof @5380; LoadActivityInvoicesAsync @5384; LoadTrackOrdersAsync @5385; UpdateDemoSeedingAvailabilityAsync @5386; StartAutomaticDemoDatasetLoadAsync @5387 | No extracted literal effects. |
| <span id="m-fb57ab098bda"></span><code>MainViewModel.PowerAction()</code><br>5395–5401 | CheckSessionUnlocked @5397 | No extracted literal effects. |
| <span id="m-95afeaf4e96f"></span><code>MainViewModel.CycleTable()</code><br>5403–5409 | CheckSessionUnlocked @5405 | No extracted literal effects. |
| <span id="m-085e77cc6b2e"></span><code>MainViewModel.CycleDiningType()</code><br>5411–5417 | CheckSessionUnlocked @5413 | No extracted literal effects. |
| <span id="m-1c5e4573c7be"></span><code>MainViewModel.CycleCustomer()</code><br>5419–5422 | OpenCustomerChooser @5421 | No extracted literal effects. |
| <span id="m-77677b8c621d"></span><code>MainViewModel.OpenPromoDialog()</code><br>5424–5439 | CheckSessionUnlocked @5426; IsNullOrWhiteSpace @5433; RaisePropertyChanged @5437; nameof @5437 | No extracted literal effects. |
| <span id="m-9b1f044cbce9"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5441–5510 | CheckSessionUnlocked @5443; ToLowerInvariant @5456; Trim @5456; IsNullOrWhiteSpace @5463; Trim @5463; ToList @5471; Select @5471; ToMinorUnits @5475; Equals @5491; Calculate @5495; NotifyTotalsChanged @5507; ConfigureAwait @5509; SaveDurableCartAsync @5509 | No extracted literal effects. |
| <span id="m-e5a3e38b6141"></span><code>MainViewModel.TogglePromo()</code><br>5512–5529 | CheckSessionUnlocked @5514; RemovePromo @5523; OpenPromoDialog @5527 | No extracted literal effects. |
| <span id="m-b65a8d59625c"></span><code>MainViewModel.RemovePromo()</code><br>5531–5541 | NotifyTotalsChanged @5538; SaveDurableCartAsync @5540 | No extracted literal effects. |
| <span id="m-058ddfaa2577"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5543–5554 | CheckSessionUnlocked @5545; NotifyTotalsChanged @5551; ConfigureAwait @5553; SaveDurableCartAsync @5553 | No extracted literal effects. |
| <span id="m-6c2aaaa159f4"></span><code>MainViewModel.CancelPromoDialog()</code><br>5556–5560 | — | No extracted literal effects. |
| <span id="m-43c7928617a0"></span><code>MainViewModel.RecalculateCart()</code><br>5562–5616 | ToMinorUnits @5578; Add @5579; Equals @5600; Calculate @5604; ToDictionary @5607; TryGetValue @5610 | No extracted literal effects. |
| <span id="m-538f41e3da31"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5618–5625 | CheckSessionUnlocked @5620; ResetCashReview @5621 | No extracted literal effects. |
| <span id="m-babd22a9409d"></span><code>MainViewModel.SelectCategory(CategoryItem?)</code><br>5627–5673 | CheckSessionUnlocked @5629; RaisePropertyChanged @5637; nameof @5637; ApplyFilter @5638; Localize @5641 | No extracted literal effects. |
| <span id="m-6d1e7719c27b"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5675–5675 | AddToCart @5675 | No extracted literal effects. |
| <span id="m-e44735377950"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5677–5721 | CheckSessionUnlocked @5679; ResetCashReview @5680; ResolveProductSaleUnitFactor @5683; Round @5690; FirstOrDefault @5691; UpdateCartKitBreakdownAsync @5700; Add @5712; NotifyTotalsChanged @5715; SaveDurableCartAsync @5717; IsNullOrWhiteSpace @5719; ToString @5719; NewGuid @5719; RecordSuccessfulSearchUseAsync @5720; FromGuid @5720 | No extracted literal effects. |
| <span id="m-ee548d2d1345"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5723–5736 | CheckSessionUnlocked @5725; ResetCashReview @5726; UpdateCartKitBreakdownAsync @5733; NotifyTotalsChanged @5734; SaveDurableCartAsync @5735 | No extracted literal effects. |
| <span id="m-b0fb550997b7"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5738–5753 | CheckSessionUnlocked @5740; ResetCashReview @5741; UpdateCartKitBreakdownAsync @5745; Remove @5749; NotifyTotalsChanged @5751; SaveDurableCartAsync @5752 | No extracted literal effects. |
| <span id="m-52bab256ec17"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5755–5761 | ConfigureAwait @5758; LoadAsync @5758; RefreshSavedPaymentImages @5759; CancelManualPaymentSettings @5760 | No extracted literal effects. |
| <span id="m-24a0ac69a960"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5763–5792 | ValidImage @5770; CreatePaymentBitmap @5775; Dispose @5778; RaisePropertyChanged @5790; nameof @5790 | No extracted literal effects. |
| <span id="m-4dc81f7f8736"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5794–5810 | Dispose @5804; CreatePaymentBitmap @5806; RaisePropertyChanged @5808; nameof @5808 | No extracted literal effects. |
| <span id="m-25c03ab86c9e"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5812–5816 | — | No extracted literal effects. |
| <span id="m-a39b9b301d2d"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5818–5826 | Dispose @5820; CreatePaymentBitmap @5822; RaisePropertyChanged @5824; nameof @5824 | No extracted literal effects. |
| <span id="m-c2acd49a8cb6"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5828–5847 | ConfigureAwait @5837; ExecuteAsync @5837; DispatchToUi @5840; SafePipelineError @5840; LoadAsync @5843; RefreshSavedPaymentImages @5844; CancelManualPaymentSettings @5845 | No extracted literal effects. |
| <span id="m-62f0f111a862"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5849–5868 | IsNullOrWhiteSpace @5853; Trim @5854; ToMinorUnits @5860; ConfigureAwait @5866; PlaceOrderAsync @5866 | No extracted literal effects. |
| <span id="m-46c95b3cf0fc"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5870–5882 | PlaceOrderInternalAsync @5876 | No extracted literal effects. |
| <span id="m-99131a1852ea"></span><code>MainViewModel.PlaceOrderInternalAsync()</code><br>5884–6085 | Localize @5888; ExecuteDemoPlaceOrder @5894; ConfigureAwait @5920; SaveDurableCartAsync @5920; ToMinorUnits @5928; Trim @5930; Equals @5941; Equals @5948; ResetCashReview @5950; Max @6008; Add @6013; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6031; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6031; Format @6043; ToDecimal @6043; DispatchToUi @6045; Clear @6049; NewGuid @6058; NotifyTotalsChanged @6059; LoadActivityInvoicesAsync @6066; OpenStaleCartPriceReviewAsync @6071; RequestElevationForCheckout @6073; SafePipelineError @6077; SafeError @6083 | No extracted literal effects. |
| <span id="m-11f492b407fe"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>6087–6119 | DispatchToUi @6091; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @6094; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @6094; SafePipelineError @6099; ToArray @6103; Select @6103; Where @6103; FormatCartReviewMoney @6107; Clear @6114; Add @6115 | No extracted literal effects. |
| <span id="m-eb84b4ba500f"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>6121–6126 | ScalingFactor @6123; Format @6125; Equals @6125 | No extracted literal effects. |
| <span id="m-0e2b4fa8e7df"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>6128–6159 | CheckSessionUnlocked @6130; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @6132; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @6132; DispatchToUi @6137; SafePipelineError @6137; ConfigureAwait @6138; OpenStaleCartPriceReviewAsync @6138; FirstOrDefault @6145; ScalingFactor @6148; ResetCashReview @6152; Clear @6155; NotifyTotalsChanged @6156 | No extracted literal effects. |
| <span id="m-62922cab69b0"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>6161–6168 | Clear @6165; ResetCashReview @6166 | No extracted literal effects. |
| <span id="m-a15488ea7061"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>6170–6196 | CheckSessionUnlocked @6172; ResetCashReview @6179; ToMinorUnits @6190; ConfigureAwait @6195; PlaceOrderAsync @6195 | No extracted literal effects. |
| <span id="m-1b71affd51dd"></span><code>MainViewModel.CancelCashReview()</code><br>6198–6202 | ResetCashReview @6200 | No extracted literal effects. |
| <span id="m-a3e86097cac4"></span><code>MainViewModel.ResetCashReview()</code><br>6204–6213 | — | No extracted literal effects. |
| <span id="m-a44b103e76b7"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>6215–6234 | RaisePropertyChanged @6226; nameof @6226; Clear @6229; ResetCashReview @6230; NotifyTotalsChanged @6231 | No extracted literal effects. |
| <span id="m-8a53026c4aaa"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>6236–6301 | ConfigureAwait @6240; WaitAsync @6240; ClearActiveCartAsync @6245; ToMinorUnits @6255; Add @6256; ToUpperInvariant @6259; ToString @6259; IsNullOrWhiteSpace @6262; SaveActiveCartAsync @6275; DispatchToUi @6294; SafeError @6294; Release @6299 | No extracted literal effects. |
| <span id="m-4de5702425e1"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>6303–6362 | ConfigureAwait @6309; GetActiveCartAsync @6309; Clear @6321; FirstOrDefault @6324; ToDecimal @6328; Add @6338; NotifyTotalsChanged @6355 | No extracted literal effects. |
| <span id="m-3be8ed6efc05"></span><code>MainViewModel.SanitizeOrderHistorySummary(string?,bool)</code><br>6364–6377 | IsNullOrWhiteSpace @6366; Replace @6371; Trim @6376; Trim @6376 | No extracted literal effects. |
| <span id="m-b32408cee5e5"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>6379–6456 | ApplyPagedResult @6383; ToList @6384; ApplyActivityFilter @6388; HasPermission @6393; ConfigureAwait @6400; GetPagedActivityInvoicesAsync @6400; ToPageRequest @6403; ToDecimal @6409; Add @6410; ToString @6415; ToLocalTime @6415; SanitizeOrderHistorySummary @6416; DispatchToUi @6434; Clear @6436; Add @6439; SafeError @6453 | No extracted literal effects. |
| <span id="m-795c0219bb67"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>6458–6535 | HasPermission @6463; ConfigureAwait @6470; GetActiveOrdersAsync @6470; Clear @6471; ToDecimal @6475; Join @6509; Select @6509; Add @6511; ToString @6526; ToLocalTime @6526; SanitizeOrderHistorySummary @6527 | No extracted literal effects. |
| <span id="m-fd4ae3ff23aa"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6537–6564 | CheckSessionUnlocked @6539; Clear @6542; ConfigureAwait @6548; GetOrderByIdAsync @6548; Add @6553; DispatchToUi @6559; SafeError @6559 | No extracted literal effects. |
| <span id="m-a8b186987544"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6566–6571 | Clear @6570 | No extracted literal effects. |
| <span id="m-6e34202b1ef0"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6573–6606 | CheckSessionUnlocked @6575; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6591; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6591; ConfigureAwait @6600; LoadTrackOrdersAsync @6600; DispatchToUi @6604; SafePipelineError @6604 | No extracted literal effects. |
| <span id="m-61da8bf921df"></span><code>MainViewModel.MarkReadyAsync()</code><br>6608–6641 | CheckSessionUnlocked @6610; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6626; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6626; ConfigureAwait @6635; LoadTrackOrdersAsync @6635; DispatchToUi @6639; SafePipelineError @6639 | No extracted literal effects. |
| <span id="m-0762c7024625"></span><code>MainViewModel.MarkServedAsync()</code><br>6643–6676 | CheckSessionUnlocked @6645; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6661; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6661; ConfigureAwait @6670; LoadTrackOrdersAsync @6670; DispatchToUi @6674; SafePipelineError @6674 | No extracted literal effects. |
| <span id="m-3d33e4b6f7e6"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6678–6706 | CheckSessionUnlocked @6680; Remove @6684; CloseOrderDetailsModal @6685; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6694; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6694; ConfigureAwait @6700; LoadTrackOrdersAsync @6700; DispatchToUi @6704; SafePipelineError @6704 | No extracted literal effects. |
| <span id="m-23dc42b16520"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6708–6804 | CheckSessionUnlocked @6710; CloseOrderDetailsModal @6716; ConfigureAwait @6723; GetOrderByIdAsync @6723; Zero @6745; NewGuid @6751; ToList @6754; Select @6754; ToUpperInvariant @6757; ToString @6757; SaveActiveCartAsync @6766; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6782; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6782; DispatchToUi @6785; SafePipelineError @6785; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6791; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6791; LoadTrackOrdersAsync @6797; LoadActivityInvoicesAsync @6798 | No extracted literal effects. |
| <span id="m-0f01ab97978d"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6806–6813 | CheckSessionUnlocked @6808 | No extracted literal effects. |
| <span id="m-7afb20c0834b"></span><code>MainViewModel.FilterActivity(string)</code><br>6832–6838 | CheckSessionUnlocked @6834; ApplyActivityFilter @6836 | No extracted literal effects. |
| <span id="m-ceae01d2dbf3"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6840–6879 | Clear @6842; AsEnumerable @6843; Where @6848; IsNullOrWhiteSpace @6851; Trim @6853; Contains @6855; Contains @6856; Contains @6857; IsNullOrEmpty @6861; Equals @6863; ToList @6867; Add @6869; ApplyPagedResult @6873 | No extracted literal effects. |
| <span id="m-f64eb0ad4762"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6881–6917 | CheckSessionUnlocked @6883; ConfigureAwait(QueueReceiptReprintCommand, string) @6903; ExecuteAsync(QueueReceiptReprintCommand, string) @6903; IsNullOrWhiteSpace @6904; ReportError @6906; RefreshOutputStatusAsync @6911; DispatchToUi @6915; SafeError @6915 | No extracted literal effects. |
| <span id="m-3dde2a4a5959"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6919–6962 | RefreshOutputPrinterQueues @6924; ReadAsync @6925; Equals @6932; IsNullOrWhiteSpace @6932; TryReadGeometry @6934; ComputeCapabilityFingerprint @6938; ConfigureAwait @6942; InvalidateThermalVerificationAsync @6942; LoadCashFinancialSettingsAsync @6954; LoadReceiptDesignAsync @6955; RefreshOutputStatusAsync @6956; DispatchToUi @6960; SafeError @6960 | No extracted literal effects. |
| <span id="m-d52ddcd61802"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6964–6990 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6977; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6977; ReportError @6980; LoadOutputDevicesAsync @6983; DispatchToUi @6988; SafeError @6988 | No extracted literal effects. |
| <span id="m-bba98c6467b3"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6992–7065 | Equals @7006; IsNullOrWhiteSpace @7011; IsWindows @7016; TryReadGeometry @7021; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @7038; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @7038; ReportError @7041; Render @7044; ToString @7045; ConfigureAwait @7046; Run @7046; Send @7046; ComputeCapabilityFingerprint @7047; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @7048; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @7048; RefreshOutputStatusAsync @7059; DispatchToUi @7063; SafeError @7063 | No extracted literal effects. |
| <span id="m-d3872af9dc6f"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>7067–7104 | IsWindows @7081; IsNullOrWhiteSpace @7081; TryReadGeometry @7083; ComputeCapabilityFingerprint @7087; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @7088; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @7088; ReportError @7092; ConfigureAwait @7098; RefreshOutputStatusAsync @7098; DispatchToUi @7102; SafeError @7102 | InvalidOperationException @7082; InvalidOperationException @7086 |
| <span id="m-4e2230686f46"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>7106–7143 | CreateCommand @7111; ConfigureAwait @7120; ExecuteReaderAsync @7120; ReadAsync @7121; GetInt32 @7124; GetString @7124; GetInt64 @7124; Parse @7125; RaisePropertyChanged @7127; nameof @7127; NotifyTotalsChanged @7136; DispatchToUi @7141; SafeError @7141 | FROM store_config @7112 |
| <span id="m-90266e1a8b8d"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>7145–7173 | ConfigureAwait @7158; ExecuteAsync @7158; ReportError @7161; NotifyTotalsChanged @7166; DispatchToUi @7171; SafeError @7171 | No extracted literal effects. |
| <span id="m-2c46c64c7ff7"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>7175–7219 | DispatchToUi @7179; CreateCommand @7184; ConfigureAwait @7190; ExecuteReaderAsync @7190; ReadAsync @7191; Deserialize(ReceiptDesignDocument) @7193; GetString @7193; SafeError @7212 | FROM receipt_designs @7185; JOIN receipt_design_versions @7185 |
| <span id="m-84f88d5bc943"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>7221–7248 | ConfigureAwait @7234; ExecuteAsync @7234; ReportError @7239; DispatchToUi @7246; SafeError @7246 | No extracted literal effects. |
| <span id="m-db9bf3fdc995"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>7250–7262 | IsWindows @7252; Select @7253; Enumerate @7253; Empty(string) @7254; ToArray @7255; OrderBy @7255; Distinct @7255; Where @7255; Append @7255; IsNullOrWhiteSpace @7256; Clear @7260; Add @7261 | No extracted literal effects. |
| <span id="m-10c464288697"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>7264–7322 | CheckAccess @7266; DispatchToUi @7268; CreateSampleData @7274; Equals @7280; IsWindows @7287; TryReadGeometry @7288; BuildPaperDocument @7297; RenderPreviewPngPages @7300; SetReceiptDesignPreviewPages @7302; Localize @7304; BuildThermalLines @7309; RenderPreviewPng @7311; Empty(byte[]) @7318; ReportException @7320 | No extracted literal effects. |
| <span id="m-53fdf869b145"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>7324–7329 | ShowReceiptDesignPreviewPage @7328 | No extracted literal effects. |
| <span id="m-6692dff7ec16"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>7331–7337 | ShowReceiptDesignPreviewPage @7336 | No extracted literal effects. |
| <span id="m-f9c3544afdd5"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>7339–7353 | RaisePropertyChanged @7350; nameof @7350 | No extracted literal effects. |
| <span id="m-bc4ef263b1b4"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>7355–7384 | ReadAsync @7358; Localize @7361; CreateCommand @7363; ConfigureAwait @7365; ExecuteScalarAsync @7365; ToString @7365; IsNullOrWhiteSpace @7366; ExecuteReaderAsync @7380; ReadAsync @7381; Trim @7382; GetString @7382 | FROM hardware_jobs @7364; FROM hardware_jobs @7379 |
| <span id="m-f2c4f31d0eef"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>7386–7406 | Clear @7388; AsEnumerable @7389; Where @7392; Equals @7392; IsNullOrWhiteSpace @7398; Contains @7400; Contains @7401; Contains @7402; Add @7405 | No extracted literal effects. |
| <span id="m-38c040eb5bc6"></span><code>MainViewModel.SelectInventoryKind(string)</code><br>7408–7452 | NormalizeItemKind @7410; SelectCatalogKind @7413; Clear @7417; ClearSelection @7422; InvalidateSelectedBatchPreview @7423; IsNullOrEmpty @7426; RaisePropertyChanged @7434; nameof @7434; ResetToFirstPage @7437; NotifySelectionScopeChange @7438; SetSelectionScope @7438; InventorySelectionScope @7438; RefreshWorkspaceCategories @7441; LoadInventoryAsync @7444 | No extracted literal effects. |
| <span id="m-00f291ecc7c7"></span><code>MainViewModel.RefreshWorkspaceCategories()</code><br>7454–7513 | Clear @7456; Equals @7457; IsNullOrEmpty @7461; Add @7466; Localize @7469; Add @7480; RaisePropertyChanged @7512; nameof @7512 | No extracted literal effects. |
| <span id="m-9756eb326a5b"></span><code>MainViewModel.SelectWorkspaceCategory(CategoryItem?)</code><br>7515–7548 | Equals @7518; Localize @7520; RaisePropertyChanged @7532; nameof @7532; ClearSelection @7543; InvalidateSelectedBatchPreview @7544; ResetToFirstPage @7545; NotifySelectionScopeChange @7546; SetSelectionScope @7546; InventorySelectionScope @7546; LoadInventoryAsync @7547 | No extracted literal effects. |
| <span id="m-761cbe5d2c8c"></span><code>MainViewModel.GenerateXReport()</code><br>7550–7569 | CheckSessionUnlocked @7552; ToString @7556; GenerateXReportInternalAsync @7568 | No extracted literal effects. |
| <span id="m-1dd906165da2"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>7571–7586 | ConfigureAwait @7575; LoadReportDataAsync @7575; DispatchToUi @7584; SafeError @7584 | No extracted literal effects. |
| <span id="m-ca4f982b3e59"></span><code>MainViewModel.CloseShiftZReport()</code><br>7588–7591 | OpenCloseShiftModal @7590 | No extracted literal effects. |
| <span id="m-563b27904d8a"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>7593–7602 | CheckSessionUnlocked @7600 | No extracted literal effects. |
| <span id="m-497710241961"></span><code>MainViewModel.SaveSettings()</code><br>7604–7608 | CheckSessionUnlocked @7606 | No extracted literal effects. |
| <span id="m-63883c43e2b3"></span><code>MainViewModel.ApplySettingsAsync()</code><br>7610–7697 | CheckSessionUnlocked @7619; NotifyTotalsChanged @7638; ExecuteAsync @7666; DispatchToUi @7690; SafePipelineError @7690; SafeError @7695 | No extracted literal effects. |
| <span id="m-d4d17a19d63d"></span><code>MainViewModel.CancelSettings()</code><br>7699–7720 | CheckSessionUnlocked @7701; NotifyTotalsChanged @7713 | No extracted literal effects. |
| <span id="m-2288a814b5c1"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7723–7753 | ProbeDatabaseAsync @7736; ProbeLicense @7742; RefreshOutputStatusAsync @7745; ProbeHardwareStubs @7746; DispatchToUi @7751; SafeError @7751 | No extracted literal effects. |
| <span id="m-af475b433982"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7814–7852 | RaisePropertyChanged @7816; nameof @7816; FormatRealResetPreviewSummary @7851 | No extracted literal effects. |
| <span id="m-ecf960e78de0"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7854–7867 | Localize @7855; ToString @7857; GetValueOrDefault @7857; ToString @7862; ToString @7863; ToString @7864 | No extracted literal effects. |
| <span id="m-4658b2b23eb7"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7976–8068 | Post @7980; ConfigureAwait @7987; GetWorkspaceEnvironmentAsync @7987; Equals @7988; GetDatasetStateAsync @7990; CreateCommand @7996; CreateParameter @8003; ToString @8005; Add @8006; ExecuteScalarAsync @8007; HasPermission @8012; ToInt64 @8017; ExecuteScalarAsync @8017; ExecuteScalarAsync @8021; ExecuteScalarAsync @8028; ExecuteScalarAsync @8034; Localize @8053 | FROM items @8016; FROM sales_invoices @8020; FROM third_parties @8033; FROM users @7997; JOIN user_roles @7997 · DYNAMIC SQL: inspect manually |
| <span id="m-0db930d38ce7"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>8070–8080 | CheckSessionUnlocked @8072; HasPermission @8073 | No extracted literal effects. |
| <span id="m-499ae44a6300"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>8082–8087 | ConfigureAwait @8086; ResetDatabaseAsync @8086 | No extracted literal effects. |
| <span id="m-c6d89c2471cb"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>8089–8090 | ConfigureAwait @8090; EnsureDefaultDemoDatasetAsync @8090 | No extracted literal effects. |
| <span id="m-742543f7118f"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>8092–8098 | EnsureDefaultDemoDatasetAsync @8096 | No extracted literal effects. |
| <span id="m-60d898273c57"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>8100–8204 | Localize @8105; ConfigureAwait @8112; WaitAsync @8112; GetWorkspaceEnvironmentAsync @8115; Equals @8116; HasPermission @8123; Post @8137; LocalizeDemoSeedProgress @8139; EnsureInitialDatasetAsync @8145; Join @8169; Select @8169; ReloadCatalogAsync @8179; LoadInventoryAsync @8180; LoadThirdPartiesAsync @8181; LoadManufacturingDataAsync @8182; LoadSuppliersAsync @8183; UpdateDemoSeedingAvailabilityAsync @8184; ToUpperInvariant @8189; ToString @8189; NewGuid @8189; LogDiagnosticError @8190; ReportError @8195; Release @8202 | No extracted literal effects. |
| <span id="m-6770b37630ac"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>8206–8220 | Localize @8208 | No extracted literal effects. |
| <span id="m-31fbbf40bc25"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>8222–8319 | Localize @8226; ConfigureAwait @8230; WaitAsync @8230; HasPermission @8234; GetWorkspaceEnvironmentAsync @8241; Equals @8242; ResetDatabaseAsync @8250; GetStoreProfileAsync @8253; Post @8254; Clear @8257; Clear @8258; Clear @8259; NewGuid @8260; RaisePropertyChanged @8263; nameof @8263; Lock @8264; Defaults @8277; RefreshUnlockCandidates @8290; LoadCashFinancialSettingsAsync @8291; LoadOutputDevicesAsync @8292; LoadManualPaymentSettingsAsync @8293; LoadReceiptDesignAsync @8294; ReloadCatalogAsync @8295; LoadInventoryAsync @8296; LoadThirdPartiesAsync @8297; LoadManufacturingDataAsync @8298; LoadActivityInvoicesAsync @8299; UpdateDemoSeedingAvailabilityAsync @8300; ToUpperInvariant @8305; ToString @8305; LogDiagnosticError @8306; ReportError @8312; Release @8317 | No extracted literal effects. |
| <span id="m-943479927c81"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>8321–8363 | CheckSessionUnlocked @8323; HasPermission @8325; ConfigureAwait @8333; GetWorkspaceEnvironmentAsync @8333; Equals @8334; PreviewAsync @8337; FormatRealResetPreviewSummary @8338; Post @8339; RaisePropertyChanged @8356; nameof @8356; SafeError @8361 | UnauthorizedAccessException @8335 |
| <span id="m-147eb5a6290d"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>8365–8451 | HasPermission @8368; ConfigureAwait @8386; ExecuteAsync @8386; GetStoreProfileAsync @8395; Post @8398; Clear @8402; Clear @8403; Clear @8404; Clear @8405; NewGuid @8406; Lock @8409; RaisePropertyChanged @8423; nameof @8423; LoadCashFinancialSettingsAsync @8424; LoadOutputDevicesAsync @8425; LoadManualPaymentSettingsAsync @8426; LoadReceiptDesignAsync @8427; RefreshUnlockCandidates @8435; LoadInventoryAsync @8436; LoadActivityInvoicesAsync @8437; UpdateDemoSeedingAvailabilityAsync @8438; ToUpperInvariant @8443; ToString @8443; LogDiagnosticError @8444 | No extracted literal effects. |
| <span id="m-5fcf5b354463"></span><code>MainViewModel.CancelRealShopReset()</code><br>8453–8460 | RaisePropertyChanged @8459; nameof @8459 | No extracted literal effects. |
| <span id="m-16e8fec2a5e5"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>8464–8481 | ConfigureAwait @8466; ExportDocumentAsync @8466; Post @8470; GetFileName @8474 | No extracted literal effects. |
| <span id="m-57da1c8610ae"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>8483–8505 | Exists @8488; CreateDirectory @8490; Start @8492; ToUpperInvariant @8501; ToString @8501; NewGuid @8501; LogDiagnosticError @8502 | No extracted literal effects. |
| <span id="m-0e2be61379ff"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>8507–8517 | CheckSessionUnlocked @8509; RaisePropertyChanged @8511; nameof @8511; Localize @8513; ToString @8514 | No extracted literal effects. |
| <span id="m-e6705de52043"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>8524–8540 | CheckSessionUnlocked @8526; HasPermission @8527; RaisePropertyChanged @8533; nameof @8533; Localize @8536; ToString @8537 | No extracted literal effects. |
| <span id="m-d25c14a68c6a"></span><code>MainViewModel.CommitNumpad()</code><br>8542–8619 | CheckSessionUnlocked @8544; ResetCashReview @8545; TryParse @8551; IsNullOrWhiteSpace @8553; Trim @8559; NotifyTotalsChanged @8569; SaveDurableCartAsync @8570; Min @8576; ToMinorUnits @8578; Round @8579; TryParse @8594; UpdateCartKitBreakdownAsync @8602; Remove @8608; RaisePropertyChanged @8617; nameof @8617 | No extracted literal effects. |
| <span id="m-bbcb68dae706"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>8625–8643 | CheckSessionUnlocked @8633 | No extracted literal effects. |
| <span id="m-fe00da315d12"></span><code>MainViewModel.StageBusinessProfile()</code><br>8650–8680 | CheckSessionUnlocked @8652; HasPermission @8656 | No extracted literal effects. |
| <span id="m-95fdce6a37f3"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8682–8691 | — | No extracted literal effects. |
| <span id="m-99d5c80c2992"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8693–8716 | RecalculateCart @8695; RaisePropertyChanged @8697; nameof @8697 | No extracted literal effects. |
| <span id="m-44f069cf5020"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8718–8805 | IsNullOrWhiteSpace @8721; Trim @8721; All @8731; Trim @8748; Trim @8749; NewGuid @8753; ToString @8758; ConfigureAwait @8762; BeginTransactionAsync @8762; HandleAsync @8763; AppendAsync @8768; ToString @8769; Serialize @8774; CommitAsync @8777; Initialize @8783; Unlock @8784; RaisePropertyChanged @8789; nameof @8789; LoadTeamsStaffAsync @8792; StartAutomaticDemoDatasetLoadAsync @8793; RollbackAsync @8797; DispatchToUi @8798; SafePipelineError @8798; SafeError @8803 | No extracted literal effects. |
| <span id="m-1cdaaa35b2b4"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8807–8814 | IsNullOrWhiteSpace @8809; ConfigureAwait @8813; SaveTeamMemberAsync @8813 | No extracted literal effects. |
| <span id="m-5f0bd51b76aa"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8816–8834 | CheckSessionUnlocked @8819; HasPermission @8821 | No extracted literal effects. |
| <span id="m-44232741f2e4"></span><code>MainViewModel.CancelChangePin()</code><br>8836–8843 | — | No extracted literal effects. |
| <span id="m-e656d7b51340"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8845–8921 | Trim @8853; IsNullOrWhiteSpace @8856; All @8862; Equals @8875; Equals @8876; SetQuickPin @8888; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8901; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8901; ConfigureAwait @8909; LoadTeamsStaffAsync @8909; DispatchToUi @8914; SafePipelineError @8914; SafeError @8919 | No extracted literal effects. |
| <span id="m-a2246d4bb903"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8923–8997 | HasPermission @8929; ConfigureAwait @8938; ResolveEffectivePermissionsAsync @8938; Contains @8971; Contains @8972; Add @8974; Contains @8980; DispatchToUi @8986; Clear @8988; Add @8989; SafeError @8995 | No extracted literal effects. |
| <span id="m-603e09e4f6ac"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8999–9041 | OnTeamMemberFieldChanged @9005; ConfigureAwait @9022; ExecuteAsync @9022; DispatchToUi @9026; SafePipelineError @9034; SafeError @9039 | No extracted literal effects. |
| <span id="m-03e2ca623ce0"></span><code>MainViewModel.ClosePermissionEditor()</code><br>9043–9048 | — | No extracted literal effects. |
| <span id="m-5d68a7b3c45e"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>9050–9065 | ClearImportResults @9052 | No extracted literal effects. |
| <span id="m-1fd513913e50"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>9069–9069 | — | No extracted literal effects. |
| <span id="m-6c386d3c793f"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>9070–9070 | — | No extracted literal effects. |
| <span id="m-2d6740005df5"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>9071–9071 | FromResult @9071 | No extracted literal effects. |
| <span id="m-34a3ea0bb3d0"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>9074–9159 | HasPermission @9083; FromDecimal @9098; ConfigureAwait(OpenShiftCommand, Shift) @9102; ExecuteAsync(OpenShiftCommand, Shift) @9102; SetActiveCashier @9117; RefreshUnlockCandidates @9118; ToUpperInvariant @9135; ToString @9135; ToString @9137; ConfigureAwait @9147; LoadTeamsStaffAsync @9147; LoadTrackOrdersAsync @9148; DispatchToUi @9152; SafePipelineError @9152; SafeError @9157 | No extracted literal effects. |
| <span id="m-4f1325764c85"></span><code>MainViewModel.LoadInventoryAsync()</code><br>9161–9320 | ApplyPagedResult @9165; ToList @9166; Where @9166; Equals @9166; Count @9167; ApplyInventoryFilter @9170; Clear @9179; Empty(InventoryItem) @9181; ConfigureAwait @9186; GetPagedInventoryItemsAsync @9186; ToPageRequest @9191; CreateCommand @9206; ExecuteReaderAsync @9208; ReadAsync @9209; Add @9211; Parse @9211; GetString @9211; ExecuteReaderAsync @9221; ReadAsync @9222; TryParse @9224; GetString @9224; IsDBNull @9224; Add @9235; TryGetValue @9238; Contains @9246; ToDecimal @9249; Localize @9257; ToLocalTime @9263; BuildCostSourcesTooltip @9265; DispatchToUi @9292; Add @9296; SafeError @9318 | FROM item_kits @9207; FROM item_pricing @9220 |
| <span id="m-c3bbff3512da"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>9322–9378 | CheckSessionUnlocked @9324; FirstOrDefault @9325; Clear @9336; Add @9338; CreateCommand @9343; CreateParameter @9354; Add @9357; ExecuteReader @9358; Read @9359; GetString @9361; Contains @9362; FirstOrDefault @9374; ResetReceiveLines @9375; UpdateReceiveKitBreakdownAsync @9376 | FROM uoms @9344; JOIN uoms @9344 |
| <span id="m-06aabf3ff1b7"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>9380–9481 | IsNullOrWhiteSpace @9393; Localize @9410; HasPermission @9414; BuildReceiptLines @9420; Sum @9437; Trim @9447; ToMinorUnits @9452; ConfigureAwait(ReceiveStockCommand, StockMovement) @9457; ExecuteAsync(ReceiveStockCommand, StockMovement) @9457; Clear @9467; ConfigureAwait @9469; LoadInventoryAsync @9469; LoadItemHistoryAsync @9470; DispatchToUi @9474; SafePipelineError @9474; SafeError @9479 | No extracted literal effects. |
| <span id="m-a293461671c7"></span><code>MainViewModel.ResetReceiveLines()</code><br>9487–9504 | Clear @9489; Add @9493; RaisePropertyChanged @9499; nameof @9499; Invoke @9502 | No extracted literal effects. |
| <span id="m-fe74ebc0d717"></span><code>MainViewModel.AddReceiveLine()</code><br>9507–9530 | IsNullOrWhiteSpace @9514; Add @9520; RaisePropertyChanged @9525; nameof @9525; Invoke @9528 | No extracted literal effects. |
| <span id="m-8fffe54f2d1b"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>9533–9550 | Remove @9540; Add @9543; RaisePropertyChanged @9549; nameof @9549 | No extracted literal effects. |
| <span id="m-72d6d44adbef"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>9556–9577 | IsNullOrWhiteSpace @9558; LastOrDefault @9563; Add @9567; Trim @9570; ReferenceEquals @9571; RaisePropertyChanged @9575; nameof @9575; Invoke @9576 | No extracted literal effects. |
| <span id="m-a722692c1dba"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>9580–9657 | Add @9592; IsNullOrWhiteSpace @9600; Trim @9604; FirstOrDefault @9613; GroupBy @9613; Count @9615; Trim @9642 | No extracted literal effects. |
| <span id="m-45b44e0eaa44"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>9659–9695 | CreateCommand @9664; ConfigureAwait @9671; ExecuteReaderAsync @9671; Clear @9672; ReadAsync @9673; Add @9675; ParseGuidSafe @9676; GetString @9676; IsDBNull @9680; GetInt32 @9684; Parse @9686; DispatchToUi @9693; SafeError @9693 | FROM third_parties @9665 |
| <span id="m-b234d1f3fe38"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9697–9715 | CheckSessionUnlocked @9699; FirstOrDefault @9705 | No extracted literal effects. |
| <span id="m-31a7d788dc8a"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9717–9808 | IsNullOrWhiteSpace @9740; HasPermission @9751; Trim @9769; Trim @9771; ConfigureAwait(AdjustStockCommand, StockMovement) @9775; ExecuteAsync(AdjustStockCommand, StockMovement) @9775; ConfigureAwait @9791; LoadInventoryAsync @9791; LoadItemHistoryAsync @9792; OpenWasteExpenseConfirmation @9796; DispatchToUi @9801; SafePipelineError @9801; SafeError @9806 | No extracted literal effects. |
| <span id="m-0013b415eb28"></span><code>MainViewModel.OpenAddService()</code><br>9810–9872 | ResetProductStockDraft @9812; CheckSessionUnlocked @9813; HasPermission @9814; RaisePropertyChanged @9823; nameof @9823; ClearItemHistory @9832; LoadCatalogRegistryAsync @9839; InitializeProductPricingDraft @9842; Clear @9857; Clear @9858; Clear @9867; CaptureProductModalBaselineAsync @9871 | No extracted literal effects. |
| <span id="m-9446ff9c4ab3"></span><code>MainViewModel.OpenAddProduct()</code><br>9874–9950 | ResetProductStockDraft @9876; CheckSessionUnlocked @9877; RaisePropertyChanged @9879; nameof @9879; HasPermission @9886; ClearItemHistory @9896; LoadCatalogRegistryAsync @9903; InitializeProductPricingDraft @9906; Clear @9921; Clear @9922; Where @9923; Add @9925; FirstOrDefault @9927; Clear @9938; CaptureProductModalBaselineAsync @9949 | No extracted literal effects. |
| <span id="m-3bcdac70beba"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9952–9952 | OpenEditProduct @9952 | No extracted literal effects. |
| <span id="m-038cf99d71a2"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9954–10043 | ResetProductStockDraft @9956; CheckSessionUnlocked @9958; RaisePropertyChanged @9961; nameof @9961; HasPermission @9968; ClearItemHistory @9978; LoadCatalogRegistryAsync @9986; InitializeProductPricingDraft @9992; ToMinorUnits @9993; LoadExactProductCostSnapshotsAsync @9999; ToDecimal @10003; Clear @10010; Clear @10011; Where @10012; Add @10014; FirstOrDefault @10016; LoadItemLocationEligibilitiesAsync @10035; LoadProductKitAsync @10036; LoadPrimaryBarcodeAsync @10037; LoadProductPricingDraftAsync @10038; LoadItemHistoryAsync @10039; LoadItemPriceHistoryAsync @10040; CaptureProductModalBaselineAsync @10042 | No extracted literal effects. |
| <span id="m-616f46588d7b"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>10045–10058 | OrderBy @10048; Where @10048; Add @10050 | No extracted literal effects. |
| <span id="m-97358db02945"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>10060–10133 | CreateCommand @10067; CreateParameter @10074; ToString @10076; Add @10077; ConfigureAwait @10078; ExecuteReaderAsync @10078; ReadAsync @10079; GetInt32 @10081; IsDBNull @10082; GetString @10082; ParseStoredPricingPercentForDisplay @10083; ToDisplayAmount @10087; GetInt64 @10087; OrderBy @10107; Where @10107; TryGetValue @10110; Add @10116; InvokeAsync @10118; RaisePropertyChanged @10123; nameof @10123; CaptureProductPricingSnapshot @10126; DispatchToUi @10131; SafeError @10131 | FROM item_price_levels @10098; FROM item_pricing @10069 |
| <span id="m-edf0236783c5"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>10135–10170 | CreateCommand @10142; CreateParameter @10148; ToString @10150; Add @10151; ConfigureAwait @10152; ExecuteReaderAsync @10152; ReadAsync @10153; Parse @10156; GetString @10156; GetInt32 @10156; GetInt64 @10157; IsDBNull @10157; Parse @10158; InvokeAsync @10160; DispatchToUi @10168; SafeError @10168 | FROM product_category_pricing_rules @10143 |
| <span id="m-7144dc5b2b7c"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>10172–10201 | ConfigureAwait @10176; WhenAll @10176; InvokeAsync @10177; CaptureProductModalSnapshot @10181; CaptureProductPricingSnapshot @10182; RaisePropertyChanged @10183; nameof @10183 | No extracted literal effects. |
| <span id="m-ec35353ee253"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>10203–10251 | Serialize @10203; ToArray @10226; Select @10226; Select @10243; OrderBy @10243; OrderBy @10247 | No extracted literal effects. |
| <span id="m-c6cffca08ca8"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>10253–10265 | Serialize @10253; ToArray @10264; Select @10264 | No extracted literal effects. |
| <span id="m-affa9e346bce"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>10267–10299 | nameof @10269; RaisePropertyChanged @10270; RaiseTraceabilityState @10275; StartsWith @10279; RecomputeProductPricingPreview @10290; RefreshVirtualKitAvailability @10292 | No extracted literal effects. |
| <span id="m-c5b36184413b"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>10301–10315 | RaisePropertyChanged @10309; nameof @10309; RecomputeProductPricingPreview @10312; RefreshVirtualKitAvailability @10313 | No extracted literal effects. |
| <span id="m-b9b66ca75129"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>10317–10325 | RaisePropertyChanged @10319; nameof @10319; RecomputeProductPricingPreview @10322; RefreshVirtualKitAvailability @10323 | No extracted literal effects. |
| <span id="m-1f4f5281ce6c"></span><code>MainViewModel.RequestCloseProductModal()</code><br>10327–10340 | DiscardProductModal @10339 | No extracted literal effects. |
| <span id="m-0179cd15c65b"></span><code>MainViewModel.DiscardProductModal()</code><br>10342–10351 | RaisePropertyChanged @10347; nameof @10347; ClearItemHistory @10349 | No extracted literal effects. |
| <span id="m-eea70275adbd"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>10353–10371 | CreateCommand @10358; CreateParameter @10360; ToString @10362; Add @10363; ConfigureAwait @10364; ExecuteScalarAsync @10364; DispatchToUi @10367; ToString @10367 | FROM barcodes @10359 |
| <span id="m-c533ca8ddc79"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>10373–10424 | CreateCommand @10378; CreateParameter @10385; ToString @10387; Add @10388; ConfigureAwait @10392; ExecuteReaderAsync @10392; ReadAsync @10393; IsDBNull @10396; GetString @10396; GetDouble @10397; ResolveQuantity @10398; Add @10399; Parse @10401; DispatchToUi @10409; Clear @10412; Add @10413; RaisePropertyChanged @10416; nameof @10416; RecomputeProductPricingPreview @10419; RefreshVirtualKitAvailability @10420 | FROM item_kits @10379; JOIN item_kit_components @10379; JOIN items @10379 |
| <span id="m-be80b75c79fd"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>10426–10426 | SaveProductConfigurationAsync @10426 | No extracted literal effects. |
| <span id="m-1ca2992f5e5f"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>10428–10777 | ConfigureAwait @10433; LoadCatalogRegistryAsync @10433; HasPermission @10435; IsNullOrWhiteSpace @10440; Equals @10465; ValidateUnitEligibility @10478; ToMinorUnits @10498; GetValueOrDefault @10505; Trim @10506; Trim @10507; Trim @10509; Empty(KitComponentInput) @10542; CaptureProductPricingSnapshot @10545; ToCommand @10547; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @10558; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @10558; DispatchToUi @10561; RaiseTraceabilityState @10568; CaptureProductModalSnapshot @10571; RaisePropertyChanged @10573; nameof @10573; SelectInventoryKind @10579; ReloadCatalogAsync @10581; LoadInventoryAsync @10582; LoadItemHistoryAsync @10583; SafePipelineError @10587; SafeError @10593; Localize @10605; GetValueOrDefault @10672; Trim @10675; Trim @10682; ToList @10729; Select @10729 | No extracted literal effects. |
| <span id="m-f3132893ba2a"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>10779–10815 | CheckSessionUnlocked @10781; HasPermission @10782; ConfigureAwait(DeactivateProductCommand, bool) @10798; ExecuteAsync(DeactivateProductCommand, bool) @10798; ConfigureAwait @10803; ReloadCatalogAsync @10803; LoadInventoryAsync @10804; DispatchToUi @10808; SafePipelineError @10808; SafeError @10813 | No extracted literal effects. |
| <span id="m-ec01a0a18772"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>10817–10893 | ConfigureAwait @10823; GetActiveItemsAsync @10823; Clear @10825; Clear @10826; Clear @10827; CreateCommand @10832; ExecuteReaderAsync @10834; ReadAsync @10835; TryParse @10837; GetString @10837; Add @10838; GroupBy @10846; Add @10848; Count @10848; Contains @10853; Equals @10876; Add @10878; All @10881; SafeError @10884; ApplyFilter @10887 | FROM item_kits @10833 |
| <span id="m-c02e0e320c6b"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>10895–10901 | IsNullOrWhiteSpace @10897; TryParse @10898; HashData @10899; GetBytes @10899; AsSpan @10900 | No extracted literal effects. |
| <span id="m-76d2c67033d8"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>10903–10969 | CreateCommand @10909; ConfigureAwait @10912; ExecuteReaderAsync @10912; ReadAsync @10914; Add @10916; GetString @10918; GetInt32 @10922; Clear @10928; Add @10929; ExecuteReaderAsync @10941; ReadAsync @10943; Add @10945; GetString @10947; IsDBNull @10951; GetInt32 @10955; Clear @10961; Add @10962; DispatchToUi @10967; SafeError @10967 | FROM bins @10934; FROM facilities @10911; JOIN facilities @10934 |
| <span id="m-c5bead0696e9"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>11195–11317 | CreateCommand @11205; ConfigureAwait @11212; ExecuteReaderAsync @11212; ReadAsync @11213; Add @11215; ParseGuidSafe @11217; GetString @11217; IsDBNull @11220; GetInt32 @11221; Add @11241; DispatchToUi @11256; Clear @11258; Clear @11259; Clear @11260; Clear @11261; Equals @11265; Add @11266; Add @11268; Add @11270; Add @11272; Clear @11274; Add @11275; FirstOrDefault @11280; Equals @11280; FirstOrDefault @11286; ToList @11292; FirstOrDefault @11293; FirstOrDefault @11297; FirstOrDefault @11302; ApplySaleUnitDefaultsToCatalog @11307; RaisePropertyChanged @11308; nameof @11308; RefreshWorkspaceCategories @11310; SafeError @11315 | FROM product_categories @11207; FROM uoms @11233 |
| <span id="m-b00bcc4d1357"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>11319–11333 | ResolveProductSaleUnitFactor @11323; Round @11329; ApplyFilter @11332 | No extracted literal effects. |
| <span id="m-59f3f4d9a880"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>11335–11353 | FirstOrDefault @11337; Equals @11338; TryParse @11345 | No extracted literal effects. |
| <span id="m-510e1de11d99"></span><code>MainViewModel.OpenAddCategoryForCurrentKindAsync()</code><br>11355–11370 | CheckSessionUnlocked @11357; HasPermission @11358; OpenCategoryManagerAsync @11364; CaptureCategoryFormSnapshot @11367; RaisePropertyChanged @11368; nameof @11368 | No extracted literal effects. |
| <span id="m-bf135b228e1a"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>11372–11394 | CheckSessionUnlocked @11374; HasPermission @11375; ConfigureAwait @11390; LoadManagedCategoriesAsync @11390; CaptureCategoryFormSnapshot @11392; RaisePropertyChanged @11393; nameof @11393 | No extracted literal effects. |
| <span id="m-3cd0fe400c1b"></span><code>MainViewModel.CloseCategoryManager()</code><br>11396–11405 | — | No extracted literal effects. |
| <span id="m-f6aa43d79a81"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>11407–11429 | CheckSessionUnlocked @11409; HasPermission @11410; ConfigureAwait @11425; LoadManagedUnitsAsync @11425; CaptureUnitFormSnapshot @11427; RaisePropertyChanged @11428; nameof @11428 | No extracted literal effects. |
| <span id="m-44d8f89941ab"></span><code>MainViewModel.CloseUnitManager()</code><br>11431–11440 | — | No extracted literal effects. |
| <span id="m-8bd9c89fa1ac"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>11442–11505 | Clear @11445; Clear @11446; Clear @11447; CreateCommand @11448; ConfigureAwait @11454; ExecuteReaderAsync @11454; ReadAsync @11455; Add @11457; ParseGuidSafe @11459; GetString @11459; IsDBNull @11462; GetInt32 @11463; Where @11471; Equals @11471; Add @11472; TryParse @11485; Add @11486; RefreshTargetedCategoryCollections @11499; DispatchToUi @11500; RefreshManagedCategoriesTable @11502; RefreshManagedExpenseCategoriesTable @11503 | FROM expense_categories @11476; FROM product_categories @11450; JOIN expense_records @11476 |
| <span id="m-adddcba2bdeb"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>11507–11514 | OpenCategoryManagerAsync @11509; FirstOrDefault @11510; EditManagedCategory @11513 | No extracted literal effects. |
| <span id="m-121dc955ae90"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>11516–11524 | OpenCategoryManagerAsync @11519; FirstOrDefault @11520; EditManagedExpenseCategory @11523 | No extracted literal effects. |
| <span id="m-1d7aad866f24"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>11526–11548 | DispatchToUi @11528; Clear @11530; Clear @11531; Clear @11532; Clear @11533; Where @11535; Equals @11538; Add @11539; Add @11541; Add @11543; Add @11545 | No extracted literal effects. |
| <span id="m-dc82e37375da"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>11550–11562 | CaptureCategoryFormSnapshot @11560; RaisePropertyChanged @11561; nameof @11561 | No extracted literal effects. |
| <span id="m-12dc5e1c2975"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>11564–11577 | CaptureCategoryFormSnapshot @11575; RaisePropertyChanged @11576; nameof @11576 | No extracted literal effects. |
| <span id="m-0a9a95ea05c4"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>11579–11589 | Serialize @11579 | No extracted literal effects. |
| <span id="m-ad52b7b8858c"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>11591–11601 | Serialize @11591 | No extracted literal effects. |
| <span id="m-7c58c6793f3e"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>11603–11603 | — | No extracted literal effects. |
| <span id="m-f8448d67c238"></span><code>MainViewModel.DiscardRegistryForm()</code><br>11605–11621 | Equals @11608; RaisePropertyChanged @11612; nameof @11612 | No extracted literal effects. |
| <span id="m-ac2d02268d75"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>11623–11750 | Equals @11634; HasPermission @11636; FirstOrDefault @11645; Trim @11650; Trim @11651; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11653; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11653; DispatchToUi @11656; SafePipelineError @11656; IsNullOrWhiteSpace @11664; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @11666; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @11666; ConfigureAwait @11675; LoadManagedCategoriesAsync @11675; LoadExpenseCategoriesAsync @11676; CaptureCategoryFormSnapshot @11686; RaisePropertyChanged @11687; nameof @11687; Trim @11705; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @11707; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @11707; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @11723; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @11723; LoadCatalogRegistryAsync @11732; ReloadCatalogAsync @11733; SafeError @11748 | No extracted literal effects. |
| <span id="m-0599fe649d2e"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>11752–11797 | HasPermission @11762; ConfigureAwait(DeactivateCategoryCommand, bool) @11775; ExecuteAsync(DeactivateCategoryCommand, bool) @11775; ConfigureAwait(ReactivateCategoryCommand, bool) @11780; ExecuteAsync(ReactivateCategoryCommand, bool) @11780; DispatchToUi @11785; SafePipelineError @11785; ConfigureAwait @11789; LoadManagedCategoriesAsync @11789; LoadCatalogRegistryAsync @11790; ReloadCatalogAsync @11791; SafeError @11795 | No extracted literal effects. |
| <span id="m-66f4d706b348"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>11799–11839 | HasPermission @11809; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11825; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11825; DispatchToUi @11828; SafePipelineError @11828; ConfigureAwait @11832; LoadManagedCategoriesAsync @11832; LoadExpenseCategoriesAsync @11833; SafeError @11837 | No extracted literal effects. |
| <span id="m-9e9c1cd1b55a"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>11841–11941 | Clear @11844; CreateCommand @11847; ConfigureAwait @11853; ExecuteReaderAsync @11853; ReadAsync @11854; Add @11856; GetString @11858; IsDBNull @11860; GetInt32 @11864; IsNullOrWhiteSpace @11875; Equals @11879; Add @11886; Clear @11890; ExecuteReaderAsync @11895; ReadAsync @11896; GetString @11898; Where @11920; Add @11922; TryGetValue @11925; FirstOrDefault @11932; Add @11936; DispatchToUi @11939; UpdateConversionPreview @11940 | FROM store_uom_preferences @11894; FROM uoms @11849 |
| <span id="m-5d0d273f398d"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>11943–11950 | OpenUnitManagerAsync @11945; FirstOrDefault @11946; Equals @11946; EditManagedUnit @11949 | No extracted literal effects. |
| <span id="m-7b4a126b4771"></span><code>MainViewModel.UpdateConversionPreview()</code><br>11952–11988 | IsNullOrWhiteSpace @11954; FirstOrDefault @11960; Equals @11960; TryParse @11975 | No extracted literal effects. |
| <span id="m-96ab8f470dbb"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11990–12011 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11997; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11997; DispatchToUi @12000; SafePipelineError @12004; SafeError @12009 | No extracted literal effects. |
| <span id="m-ec8dd304f69b"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>12013–12026 | IsNullOrWhiteSpace @12019; TryParse @12022; CaptureUnitFormSnapshot @12024; RaisePropertyChanged @12025; nameof @12025 | No extracted literal effects. |
| <span id="m-94cf0f96230a"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>12028–12090 | IsNullOrWhiteSpace @12040; Trim @12044; Trim @12045; Trim @12048; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @12049; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @12049; DispatchToUi @12052; SafePipelineError @12052; Trim @12059; Equals @12062; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @12067; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @12067; ConfigureAwait @12075; LoadManagedUnitsAsync @12075; LoadCatalogRegistryAsync @12076; CaptureUnitFormSnapshot @12083; RaisePropertyChanged @12084; nameof @12084; SafeError @12088 | No extracted literal effects. |
| <span id="m-1cd58d2bd082"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>12092–12130 | ConfigureAwait(DeactivateUomCommand, bool) @12109; ExecuteAsync(DeactivateUomCommand, bool) @12109; ConfigureAwait(ReactivateUomCommand, bool) @12114; ExecuteAsync(ReactivateUomCommand, bool) @12114; DispatchToUi @12119; SafePipelineError @12119; ConfigureAwait @12123; LoadManagedUnitsAsync @12123; LoadCatalogRegistryAsync @12124; SafeError @12128 | No extracted literal effects. |
| <span id="m-72ab4e937fd3"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>12132–12170 | CreateCommand @12137; CreateParameter @12144; ToString @12146; Add @12147; ConfigureAwait @12149; ExecuteReaderAsync @12149; Clear @12150; ReadAsync @12151; Add @12153; ParseGuidSafe @12155; GetString @12155; GetInt32 @12158; IsDBNull @12160; ToDecimal @12160; GetDouble @12160; DispatchToUi @12168; SafeError @12168 | FROM item_locations @12138 |
| <span id="m-6a0176cbf665"></span><code>MainViewModel.OpenLocationsModal()</code><br>12173–12199 | CheckSessionUnlocked @12175; HasPermission @12176; LoadFacilitiesAndBinsAsync @12197 | No extracted literal effects. |
| <span id="m-7c5bd9fe6ebf"></span><code>MainViewModel.OpenAddFacility()</code><br>12201–12209 | — | No extracted literal effects. |
| <span id="m-bd6debaeef9a"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>12211–12220 | — | No extracted literal effects. |
| <span id="m-a163c6d8a207"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>12222–12281 | HasPermission @12225; IsNullOrWhiteSpace @12230; IsNullOrEmpty @12246; Trim @12248; Trim @12248; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @12249; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @12249; OpenAddFacility @12253; ConfigureAwait @12254; LoadFacilitiesAndBinsAsync @12254; DispatchToUi @12258; SafePipelineError @12258; ConfigureAwait(CreateFacilityCommand, FacilityDto) @12264; ExecuteAsync(CreateFacilityCommand, FacilityDto) @12264; SafeError @12279 | No extracted literal effects. |
| <span id="m-ba2ee68efabb"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>12283–12314 | HasPermission @12286; ConfigureAwait(DeactivateFacilityCommand, bool) @12298; ExecuteAsync(DeactivateFacilityCommand, bool) @12298; OpenAddFacility @12302; ConfigureAwait @12303; LoadFacilitiesAndBinsAsync @12303; DispatchToUi @12307; SafePipelineError @12307; SafeError @12312 | No extracted literal effects. |
| <span id="m-e60185b3512c"></span><code>MainViewModel.OpenAddBin()</code><br>12316–12327 | FirstOrDefault @12326 | No extracted literal effects. |
| <span id="m-b7b55b2599ec"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>12329–12341 | FirstOrDefault @12339 | No extracted literal effects. |
| <span id="m-b9572aa6948e"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>12343–12418 | HasPermission @12346; IsNullOrWhiteSpace @12356; IsNullOrEmpty @12367; Trim @12372; Trim @12373; Trim @12374; Trim @12375; Trim @12376; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @12379; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @12379; OpenAddBin @12383; ConfigureAwait @12384; LoadFacilitiesAndBinsAsync @12384; DispatchToUi @12388; SafePipelineError @12388; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @12401; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @12401; SafeError @12416 | No extracted literal effects. |
| <span id="m-2722226b2648"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>12420–12451 | HasPermission @12423; ConfigureAwait(DeactivateLocationBinCommand, bool) @12435; ExecuteAsync(DeactivateLocationBinCommand, bool) @12435; OpenAddBin @12439; ConfigureAwait @12440; LoadFacilitiesAndBinsAsync @12440; DispatchToUi @12444; SafePipelineError @12444; SafeError @12449 | No extracted literal effects. |
| <span id="m-0bf634a6c6da"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>12453–12506 | HasPermission @12461; IsNullOrWhiteSpace @12466; Trim @12478; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @12486; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @12486; ConfigureAwait @12494; LoadItemLocationEligibilitiesAsync @12494; DispatchToUi @12499; SafePipelineError @12499; SafeError @12504 | No extracted literal effects. |
| <span id="m-77a6000c5413"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>12508–12538 | HasPermission @12511; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @12523; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @12523; ConfigureAwait @12526; LoadItemLocationEligibilitiesAsync @12526; DispatchToUi @12531; SafePipelineError @12531; SafeError @12536 | No extracted literal effects. |
| <span id="m-6958d7de781e"></span><code>MainViewModel.LoadCustomersAsync()</code><br>12541–12574 | NewGuid @12549; Clear @12555; Add @12556; FilterCustomers @12558; ConfigureAwait @12565; GetCustomersAsync @12565; DispatchToUi @12572; SafeError @12572 | No extracted literal effects. |
| <span id="m-a67bf291db35"></span><code>MainViewModel.FilterCustomers()</code><br>12576–12589 | Clear @12578; Trim @12579; IsNullOrWhiteSpace @12580; Where @12582; Contains @12582; Contains @12583; Contains @12584; Add @12587 | No extracted literal effects. |
| <span id="m-468e9663111b"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>12591–12627 | CheckSessionUnlocked @12593; CreateCommand @12602; CreateParameter @12605; ToString @12607; Add @12608; ConfigureAwait @12609; ExecuteScalarAsync @12609; ToString @12610; Equals @12613; LoadPickerCandidatesAsync @12625; DispatchToUi @12626 | FROM items @12604 |
| <span id="m-0c11fe48c511"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>12629–12690 | ConfigureAwait @12636; GetLotCandidatesAsync @12636; DispatchToUi @12639; Clear @12641; Add @12644; ToString @12653; GetSerialCandidatesAsync @12661; Clear @12666; Add @12669; ToString @12678 | No extracted literal effects. |
| <span id="m-cc651606a2da"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>12692–12698 | Clear @12695; Clear @12696 | No extracted literal effects. |
| <span id="m-1f14bc9e0b3f"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>12700–12759 | FirstOrDefault @12713; ConfigureAwait(SelectLotForCartLineCommand, bool) @12721; ExecuteAsync(SelectLotForCartLineCommand, bool) @12721; DispatchToUi @12724; SafePipelineError @12724; ToList @12730; Where @12730; ConfigureAwait(SelectSerialForCartLineCommand, bool) @12740; ExecuteAsync(SelectSerialForCartLineCommand, bool) @12740; SafeError @12757 | No extracted literal effects. |
| <span id="m-254d963e25db"></span><code>MainViewModel.OpenCustomerChooser()</code><br>12761–12769 | CheckSessionUnlocked @12763; Clear @12766; LoadCustomersAsync @12767 | No extracted literal effects. |
| <span id="m-911306793725"></span><code>MainViewModel.CloseCustomerChooser()</code><br>12771–12774 | — | No extracted literal effects. |
| <span id="m-f699a9a863ba"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>12776–12793 | SaveDurableCartAsync @12786; IsNullOrWhiteSpace @12790; ToString @12790; NewGuid @12790; RecordSuccessfulSearchUseAsync @12791; FromGuid @12791 | No extracted literal effects. |
| <span id="m-3f9eb182fc8e"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>12795–12804 | SaveDurableCartAsync @12803 | No extracted literal effects. |
| <span id="m-d0f3ebc811c1"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>12806–12851 | CheckSessionUnlocked @12808; IndexOf @12812; SelectWalkInCustomer @12818; FilterCustomers @12820; ConfigureAwait(DeactivateCustomerCommand, bool) @12832; ExecuteAsync(DeactivateCustomerCommand, bool) @12832; ConfigureAwait @12839; LoadCustomersAsync @12839; DispatchToUi @12844; SafePipelineError @12844; SafeError @12849 | No extracted literal effects. |
| <span id="m-b0178489ba0f"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>12980–13019 | Add @12986; NewGuid @12987; RefreshManufacturingTablesAsync @13001; ConfigureAwait @13009; GetKitsAsync @13009; Clear @13010; Add @13011; DispatchToUi @13017; SafeError @13017 | No extracted literal effects. |
| <span id="m-1cf165a335fe"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>13023–13039 | CheckSessionUnlocked @13025; SetProductionActionMode @13027; FirstOrDefault @13032; LoadProductionIngredientLotsAsync @13037; TakeProductionSnapshot @13038 | No extracted literal effects. |
| <span id="m-f5fd196f72c3"></span><code>MainViewModel.CloseProductionModal()</code><br>13041–13055 | — | No extracted literal effects. |
| <span id="m-8fac95989add"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>13057–13156 | ExecuteExistingProductionAsync @13060; Resolve @13082; NewGuid @13085; ToUpperInvariant @13087; ToString @13087; Insert @13105; IsNullOrWhiteSpace @13127; Trim @13127; ToDictionary @13129; Where @13129; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @13133; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @13133; DispatchToUi @13136; SafePipelineError @13136; RecordSuccessfulSearchUseAsync @13143; FromGuid @13143; ConfigureAwait @13146; LoadManufacturingDataAsync @13146; LoadInventoryAsync @13147; SafeError @13153 | No extracted literal effects. |
| <span id="m-16983e12bbf5"></span><code>MainViewModel.CloseXReportModal()</code><br>13255–13258 | — | No extracted literal effects. |
| <span id="m-c9d6b698ca77"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>13260–13290 | CheckSessionUnlocked @13262; Clear @13280; Where @13281; GetUnlockCandidates @13281; Equals @13282; Add @13286 | No extracted literal effects. |
| <span id="m-0d8901c671ea"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>13292–13296 | — | No extracted literal effects. |
| <span id="m-d010a918eb8a"></span><code>MainViewModel.CloseZReportModal()</code><br>13298–13301 | — | No extracted literal effects. |
| <span id="m-5b3cb5b4ef4a"></span><code>MainViewModel.LoadReportDataAsync()</code><br>13303–13420 | ToString @13323; DispatchToUi @13339; ConfigureAwait @13367; ExecuteAsync @13367; Join @13369; Select(string, Money) @13369; InvoiceMoney @13369; ToDecimal @13372; ToDecimal @13373; ToDecimal @13374; ToDecimal @13375; ToDecimal @13377; ToDecimal @13379; ToDecimal @13380; ToDecimal @13381; ToDecimal @13382; ToDecimal @13383; ToUpperInvariant @13385; ToString @13385; ToString @13387; ToString @13388; Sum @13394; ToDecimal @13394; ToDecimal @13397; Add @13399; Format @13404; SafeError @13412 | No extracted literal effects. |
| <span id="m-c45ef4f01c97"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>13422–13511 | CheckSessionUnlocked @13425; IsNullOrWhiteSpace @13442; AuthenticateSelectedUser @13450; Trim @13452; Round @13461; Trim @13465; ConfigureAwait(CloseShiftCommand, Shift) @13469; ExecuteAsync(CloseShiftCommand, Shift) @13469; DispatchToUi @13487; SafePipelineError @13487; ConfigureAwait @13494; ExecuteAsync @13494; SetActiveCashier @13498; RefreshUnlockCandidates @13499; RaisePropertyChanged @13500; nameof @13500; LoadReportDataAsync @13504; LoadTeamsStaffAsync @13505; SafeError @13509 | No extracted literal effects. |
| <span id="m-388ce5a35577"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>13513–13589 | FirstOrDefault @13515; CreateCommand @13522; CreateParameter @13537; ToString @13539; Add @13540; ExecuteReader @13542; Read @13543; Parse @13545; GetString @13545; GetInt64 @13548; Pow @13550; IsDBNull @13552; TryParse @13558; GetInt32 @13559; Add @13582 | FROM barcodes @13523; FROM items @13523; JOIN barcodes @13523; JOIN product_categories @13523 |
| <span id="m-e22136948154"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>13591–13716 | IsNullOrWhiteSpace @13593; Trim @13596; ToList @13599; Where @13599; IsNullOrEmpty @13600; Equals @13600; Any @13601; ToString @13603; AddToCart @13613; CreateCommand @13629; CreateParameter @13647; Add @13650; ExecuteReader @13652; Read @13654; Parse @13656; GetString @13656; ContainsKey @13657; GetInt64 @13661; Pow @13663; IsDBNull @13665; TryParse @13671; GetInt32 @13672; First @13701; Add @13706 | FROM barcodes @13630; FROM items @13630; JOIN barcodes @13630; JOIN product_categories @13630 |
| <span id="m-af06a515f48f"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>13718–13761 | IsNullOrWhiteSpace @13720; Trim @13723; AppendReceiveSerialScan @13729; TryAddUniqueExactMatchToCart @13735; Clear @13737; ToList @13742; Where @13742; Equals @13742; Equals @13742; AddToCart @13745 | No extracted literal effects. |

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

SHA-256: <code>5dc068baa2f1d81bd9cdb8a893dbdde8dc5bb183d4b314566c9321b76b1f5d6c</code>.

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

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml.cs</code> · 2,126 lines.

SHA-256: <code>1f1b2959fedd7dc43cd26592336b152154ea4e1621f96812d27abb7b9d51488e</code>.

Declarations: <code>MainWindow : Window</code> (line 41).

<details markdown>
<summary>Methods, calls, table effects and failures (40)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-3c1c4758ed38"></span><code>MainWindow.ReportCodeBehindError(string,string,Exception)</code><br>139–159 | Localize @143; Report @147; Post @157; Record @157 | No extracted literal effects. |
| <span id="m-07ba14955706"></span><code>MainWindow.OnDataContextChanged(object?,EventArgs)</code><br>163–169 | ObserveViewModel @167 | No extracted literal effects. |
| <span id="m-5ba3fed45f7f"></span><code>MainWindow.OnApplicationLayoutRootSizeChanged(object?,SizeChangedEventArgs)</code><br>179–181 | PushLayoutWidthsToViewModel @181 | No extracted literal effects. |
| <span id="m-743e4122132b"></span><code>MainWindow.OnPosCatalogScrollSizeChanged(object?,SizeChangedEventArgs)</code><br>185–187 | PushLayoutWidthsToViewModel @187 | No extracted literal effects. |
| <span id="m-a0fdb02102e9"></span><code>MainWindow.PushLayoutWidthsToViewModel()</code><br>191–205 | UpdatePosWindowContentWidth @199; FindControl(ScrollViewer) @201; UpdateCatalogViewport @203 | No extracted literal effects. |
| <span id="m-8113d59e6c07"></span><code>MainWindow.ObserveViewModel(MainViewModel?)</code><br>209–261 | ReferenceEquals @213 | No extracted literal effects. |
| <span id="m-fc7128489b89"></span><code>MainWindow.OnFocusSearchRequested()</code><br>265–283 | FindControl(TextBox) @269; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @269; FindControl(TextBox) @269; Focus @275; SelectAll @277 | No extracted literal effects. |
| <span id="m-e11ceecf2242"></span><code>MainWindow.OnFocusReceiveSerialRequested()</code><br>287–317 | Post @295; FindControl(ItemsControl) @299; LastOrDefault(TextBox) @301; OfType(TextBox) @301; GetVisualDescendants @301; Focus @307; SelectAll @309 | No extracted literal effects. |
| <span id="m-3a2e5aae88ec"></span><code>MainWindow.OnImportFilePickerRequested()</code><br>321–373 | OpenFilePickerAsync @339; Localize @343; PreviewImportFileAsync @359; ReportCodeBehindError @369 | No extracted literal effects. |
| <span id="m-0634651b54cc"></span><code>MainWindow.OnThirdPartyImportFilePickerRequested()</code><br>377–423 | OpenFilePickerAsync @387; PreviewThirdPartyImportFileAsync @405; FocusThirdPartyImportCloseButton @411; ReportCodeBehindError @419 | No extracted literal effects. |
| <span id="m-e1dc5bb9cd71"></span><code>MainWindow.OnThirdPartyTemplateSaveRequested(byte[])</code><br>427–427 | SaveImportTemplateAsync @427 | No extracted literal effects. |
| <span id="m-de38b5c5ef7b"></span><code>MainWindow.OnCompletedImportSaveRequested(byte[],string)</code><br>431–457 | SaveImportTemplateAsync @449; ReferenceEquals @449; ReportImportResultSave @451 | No extracted literal effects. |
| <span id="m-6a9b1f87c787"></span><code>MainWindow.OnInventoryTemplateSaveRequested(byte[])</code><br>459–459 | SaveImportTemplateAsync @459 | No extracted literal effects. |
| <span id="m-2954ca54f8d2"></span><code>MainWindow.SaveImportTemplateAsync(byte[],string,Func&lt;bool&gt;?)</code><br>461–519 | Invoke @469; GetDownloadsFolderPath @471; IsNullOrWhiteSpace @473; Exists @473; TryGetFolderFromPathAsync @475; SaveFilePickerAsync @479; OpenWriteAsync @497; SetLength @501; WriteAsync @503; ReportCodeBehindError @513 | No extracted literal effects. |
| <span id="m-afc2c7372de9"></span><code>MainWindow.GetDownloadsFolderPath()</code><br>523–553 | IsWindows @527; SHGetKnownFolderPath @533; PtrToStringUni @541; FreeCoTaskMem @549 | No extracted literal effects. |
| <span id="m-faa296aa0097"></span><code>MainWindow.SHGetKnownFolderPath(Guid,uint,IntPtr,IntPtr)</code><br>557–559 | — | No extracted literal effects. |
| <span id="m-2e01f20b57b8"></span><code>MainWindow.OnCopyToClipboardRequested(string)</code><br>563–589 | SetTextAsync @575; ReportCodeBehindError @585 | No extracted literal effects. |
| <span id="m-e8a133cfe92f"></span><code>MainWindow.OnElementGotFocus(object?,GotFocusEventArgs)</code><br>593–605 | — | No extracted literal effects. |
| <span id="m-1c14ea0710ee"></span><code>MainWindow.OnPriceInputGotFocus(object?,GotFocusEventArgs)</code><br>609–617 | Post @615 | No extracted literal effects. |
| <span id="m-7404cfb5a33a"></span><code>MainWindow.OnPriceInputPointerReleased(object?,PointerReleasedEventArgs)</code><br>621–639 | FindAncestorOfType(TextBox) @635; SelectAll @637 | No extracted literal effects. |
| <span id="m-046103eec0e5"></span><code>MainWindow.GetActiveEditableTextBox()</code><br>643–687 | IsAttachedToVisualTree @649; FindControl(TextBox) @671; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @671; FindControl(TextBox) @671 | No extracted literal effects. |
| <span id="m-effa37f8d9b2"></span><code>MainWindow.InsertTextIntoTextBox(TextBox,string)</code><br>691–747 | Min @701; Max @703; Insert @713; Remove @713; Clamp @731; Insert @733 | No extracted literal effects. |
| <span id="m-5cd91be1c8c0"></span><code>MainWindow.HandleBackspaceOnTextBox(TextBox)</code><br>751–809 | Min @761; Max @763; Remove @773; Clamp @789; DeleteGraphemeAt @795 | No extracted literal effects. |
| <span id="m-eb899f2b9eec"></span><code>MainWindow.HandleClearOnTextBox(TextBox)</code><br>813–825 | — | No extracted literal effects. |
| <span id="m-066dcee95b96"></span><code>MainWindow.HandleNumericDigitOnTextBox(TextBox,string)</code><br>829–889 | Min @839; Max @841; Remove @853; Contains @859; IsNullOrEmpty @875; InsertTextIntoTextBox @887 | No extracted literal effects. |
| <span id="m-a9c41bfc0b89"></span><code>MainWindow.WireTouchControls()</code><br>893–1197 | AddHandler @897; FindControl(GetSeek.UI.Components.Controls.TouchKeyboardControl) @901; FindControl(Border) @903; WireDraggableFloatingSurface @913; GetActiveEditableTextBox @923; HandleNumericDigitOnTextBox @929; Execute @937; InsertTextIntoTextBox @955; HandleBackspaceOnTextBox @981; HandleClearOnTextBox @1007; FindControl(GetSeek.UI.Components.Controls.TouchNumpadControl) @1045; Execute @1071; Execute @1107; Execute @1143; Execute @1181 | No extracted literal effects. |
| <span id="m-864917bbf661"></span><code>MainWindow.WireDraggableFloatingSurface(Control,Control)</code><br>1201–1315 | AddHandler @1229; GetCurrentPoint @1233; FindAncestorOfType(Button) @1237; FindAncestorOfType(TextBox) @1239; FindAncestorOfType(Avalonia.Controls.Primitives.ScrollBar) @1241; GetPosition @1253; Capture @1259; ReferenceEquals @1297; EndDrag @1311 | No extracted literal effects. |
| <span id="m-8b5fb034cf12"></span><code>MainWindow.OnChooseQrImage(object?,RoutedEventArgs)</code><br>1319–1319 | ChoosePaymentImageAsync @1319 | No extracted literal effects. |
| <span id="m-cdeedbde25bb"></span><code>MainWindow.OnChooseBankImage(object?,RoutedEventArgs)</code><br>1321–1321 | ChoosePaymentImageAsync @1321 | No extracted literal effects. |
| <span id="m-4633756ee6a3"></span><code>MainWindow.ChoosePaymentImageAsync(bool)</code><br>1325–1421 | OpenFilePickerAsync @1335; Localize @1341; OpenReadAsync @1367; Localize @1373; ReadAsync @1385; WriteAsync @1399; AsMemory @1399; ToArray @1403; SetManualPaymentImage @1407; ReportCodeBehindError @1415 | No extracted literal effects. |
| <span id="m-c0d44ee565ca"></span><code>MainWindow.OnChooseExpenseReceiptImage(object?,RoutedEventArgs)</code><br>1425–1477 | OpenFilePickerAsync @1435; OpenReadAsync @1463; SetExpenseFormAttachmentAsync @1465; ReportCodeBehindError @1473 | No extracted literal effects. |
| <span id="m-290bc1d64bec"></span><code>MainWindow.OnKeyDown(KeyEventArgs)</code><br>1481–1635 | OnKeyDown @1517; CanCaptureUnfocusedBarcodeWedge @1533; Clear @1537; ToString @1559; HandleBarcodeScanned @1571; GetPrintableCharacterFromKey @1589; IsNullOrEmpty @1591; Append @1601 | No extracted literal effects. |
| <span id="m-c3507bb487bc"></span><code>MainWindow.CanCaptureUnfocusedBarcodeWedge()</code><br>1639–1675 | GetTopLevel @1657; GetFocusedElement @1657; FindAncestorOfType(GetSeek.UI.Components.Controls.CompactDateField) @1661; GetType @1663 | No extracted literal effects. |
| <span id="m-32877eceb55c"></span><code>MainWindow.OnPreviewKeyboardAction(object?,KeyEventArgs)</code><br>1679–1871 | FirstOrDefault(GetSeek.UI.Components.Controls.CompactDateField) @1687; OfType(GetSeek.UI.Components.Controls.CompactDateField) @1687; GetVisualDescendants @1687; FirstOrDefault(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1707; OfType(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1707; TryHandleEscapeKey @1727; HandlePhysicalBackspace @1749; GetTopLevel @1765; GetFocusedElement @1765; IsWithinThirdPartyImportOverlay @1767; TryActivateFocusedButton @1771; FindControl(GetSeek.UI.Components.Controls.ModalShell) @1783; FindControl(Button) @1783; Focus @1783; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1815; ReferenceEquals @1817; IsVisualAncestorOf @1817; SelectOption @1827; Trim @1837; IsNullOrEmpty @1839; TryAddUniqueExactMatchToCart @1843; Clear @1847 | No extracted literal effects. |
| <span id="m-79cd5dcf47fa"></span><code>MainWindow.TryActivateFocusedButton()</code><br>1875–1929 | GetTopLevel @1883; GetFocusedElement @1885; CanExecute @1901; Execute @1915; RaiseEvent @1923 | No extracted literal effects. |
| <span id="m-31347aeaff64"></span><code>MainWindow.IsWithinThirdPartyImportOverlay(Visual)</code><br>1933–1951 | FindControl(GetSeek.UI.Components.Controls.ModalShell) @1937; GetVisualParent @1939 | No extracted literal effects. |
| <span id="m-63d4b4527389"></span><code>MainWindow.FocusThirdPartyImportCloseButton()</code><br>1955–1961 | Post @1959; FindControl(GetSeek.UI.Components.Controls.ModalShell) @1959; FindControl(Button) @1959; Focus @1959 | No extracted literal effects. |
| <span id="m-6bf269dbcd0c"></span><code>MainWindow.HandlePhysicalBackspace()</code><br>1965–2029 | HandleBackspaceOnTextBox @1983; Execute @1995; Execute @2007; Execute @2019 | No extracted literal effects. |
| <span id="m-83b0f92f37c5"></span><code>MainWindow.GetPrintableCharacterFromKey(Key,KeyModifiers)</code><br>2033–2069 | ToString @2045; ToUpperInvariant @2045; ToString @2045 | No extracted literal effects. |
| <span id="m-ad0f2e94f797"></span><code>MainWindow.OnKeyUp(KeyEventArgs)</code><br>2073–2123 | OnKeyUp @2121 | No extracted literal effects. |

</details>

## AXAML, migrations and project inputs

### App.axaml {#src-1e635b06c6de}

<code>Software/src/GetSeek.Desktop/App.axaml</code> · 37 lines · SHA-256 <code>fbcb9d4c8bbedcd7ab20df886f595435317e99118d45946f85f9cb14b023ed01</code>.

### GetSeek.Desktop.csproj {#src-2f265207af15}

<code>Software/src/GetSeek.Desktop/GetSeek.Desktop.csproj</code> · 27 lines · SHA-256 <code>57c435b4d7b778cfe77cd7da0397f3607a8ad46a8db4dfcd71d522dd51ee3bdb</code>.

### MainWindow.axaml {#src-67243af94cf2}

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml</code> · 6373 lines · SHA-256 <code>1873f199cf07573f9f53ca59d01f8f921ca6a8bc55496c304173067b9bf01b7f</code>.
