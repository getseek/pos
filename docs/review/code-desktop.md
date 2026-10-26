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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 13,744 lines.

SHA-256: <code>99493ef73fd665659edf895b8a8af6dd5f93456224b5979fcc6787113be48acf</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 9042).

<details markdown>
<summary>Methods, calls, table effects and failures (263)</summary>

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
| <span id="m-59de57264066"></span><code>MainViewModel.ApplyDefaultCatalogueMode(string)</code><br>3690–3693 | — | No extracted literal effects. |
| <span id="m-65778fee7689"></span><code>MainViewModel.ResetCatalogueToDefault()</code><br>3695–3703 | ParseAllItemState @3697; RaisePropertyChanged @3699; nameof @3699; ApplyFilter @3702 | No extracted literal effects. |
| <span id="m-e1a25541bf15"></span><code>MainViewModel.RefreshDefaultItemCatalogueOptions()</code><br>3705–3720 | nameof @3709; Localize @3709; FirstOrDefault @3715; Equals @3715; RaisePropertyChanged @3716 | No extracted literal effects. |
| <span id="m-f4cea5c93291"></span><code>MainViewModel.UpdateSelectedDefaultItemCatalogueOption()</code><br>3722–3726 | FirstOrDefault @3724; Equals @3724; RaisePropertyChanged @3725; nameof @3725 | No extracted literal effects. |
| <span id="m-021bf67b9a9c"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3755–3763 | IsNullOrWhiteSpace @3757 | No extracted literal effects. |
| <span id="m-baadfa81bf2e"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3765–3779 | Load @3767; IsNullOrWhiteSpace @3771; Resolve @3773; NormalizeCatalogueMode @3775; ParseAllItemState @3776; RefreshDefaultItemCatalogueOptions @3777; Apply @3778 | No extracted literal effects. |
| <span id="m-f3e2bc346571"></span><code>MainViewModel.OpenImport()</code><br>3808–3816 | CheckSessionUnlocked @3810; Increment @3812; ResetInventoryImport @3813; Invoke @3815 | No extracted literal effects. |
| <span id="m-10fe98b7f8c6"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3818–3879 | Increment @3821; ResetInventoryImport @3826; IsNullOrWhiteSpace @3831; Exists @3831; FinishFailedImport @3833; ConfigureAwait @3845; ReadAllBytesAsync @3845; ToHexString @3846; HashData @3846; TemplateContextAsync @3850; Run @3851; Read @3851; ValidateInventoryAsync @3852; CompletedWorkbook @3853; DispatchToUi @3860; ReferenceEquals @3862; Add @3863; Localize @3864; SetImportReviewRows @3868; RaisePropertyChanged @3869; nameof @3869; ReportException @3875 | No extracted literal effects. |
| <span id="m-1847ad5c342c"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3881–3935 | IsCurrentImportAttempt @3897; ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3911; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3911; ConfigureAwait @3915; RecoverImportOutcomeAsync @3915; Localize @3918; DispatchToUi @3919; FinishImportAttempt @3919; LoadInventoryAsync @3920; ReportException @3921; ReportError @3925; FinishFailedImport @3926; ImportCommandIssue @3926 | No extracted literal effects. |
| <span id="m-2fdd8e5817f7"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3947–3957 | Report @3949; DispatchToUi @3950; Insert @3952 | No extracted literal effects. |
| <span id="m-8407681ef5c0"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3959–3963 | RaisePropertyChanged @3962; nameof @3962 | No extracted literal effects. |
| <span id="m-fdadfc48ccab"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3965–3968 | ReportError @3967 | No extracted literal effects. |
| <span id="m-779976988004"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3974–3979 | ReportError @3977 | No extracted literal effects. |
| <span id="m-7b824325e77a"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3988–3994 | IsNullOrWhiteSpace @3990; Trim @3990; ReportError @3992 | No extracted literal effects. |
| <span id="m-e8fb06200a1e"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3996–3999 | DispatchToUi @3998; Insert @3998 | No extracted literal effects. |
| <span id="m-c92d9704f5af"></span><code>MainViewModel.DispatchToUi(Action)</code><br>4005–4019 | CheckAccess @4007; action @4009; GetResult @4017; GetAwaiter @4017; InvokeAsync @4017 | No extracted literal effects. |
| <span id="m-62e0e1aca4ff"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4689–4754 | Register @4691; Execute @4691; Execute @4692; Execute @4693; Execute @4694; Execute @4699; Execute @4700; Execute @4701; Execute @4702; Execute @4703; Execute @4704; Execute @4705; Execute @4706; Execute @4707; Execute @4708; Execute @4709; Execute @4710; Execute @4711; Execute @4712; Execute @4713; Execute @4714; Execute @4715; Execute @4716; Execute @4717; Execute @4718; Execute @4719; Execute @4720; Execute @4721; Execute @4722; Execute @4723; Execute @4724; Execute @4725; Execute @4726; Execute @4727; Execute @4728; Execute @4729; Execute @4730; Execute @4732; Execute @4733; RequestClosePersonForm @4734; KeepEditingPersonForm @4735; CloseSalaryMonthDetailModal @4736; CloseSalaryPaymentModal @4737; CloseSalaryAdjustmentModal @4738; CloseSalaryFinalizeModal @4739; RequestCloseExpenseForm @4740; KeepEditingExpenseForm @4741; CloseExpenseCategoryModal @4742; CloseExpensePaymentModal @4743; CloseExpenseDetailModal @4744; ClosePaymentReturnModal @4745; CloseWasteExpenseConfirmation @4746; InitializeSalaryTables @4751; InitializeExpensesTables @4752; InitializeTeamsCommands @4753 | No extracted literal effects. |
| <span id="m-de43a83b781a"></span><code>MainViewModel.CreateDemo()</code><br>4756–4763 | SetActiveCashier @4759; Parse @4759; RefreshUnlockCandidates @4761 | No extracted literal effects. |
| <span id="m-cc5e3399a9eb"></span><code>MainViewModel.CreateInitializing()</code><br>4765–4773 | — | No extracted literal effects. |
| <span id="m-8813b5a28312"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4775–4785 | — | No extracted literal effects. |
| <span id="m-e1ef413b9a73"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4787–4805 | ConfigureDiagnosticsWorkspace @4801; ResolveDiagnosticsWorkspace @4801; ApplyPersistedState @4802; RefreshUnlockCandidates @4803 | No extracted literal effects. |
| <span id="m-d3d872fe1c00"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4807–4835 | CheckSessionUnlocked @4809; HasPermission @4810; Equals @4821; GetFileNameWithoutExtension @4821; GetEntryAssembly @4823; Add @4825; Start @4828; ReportException @4833 | No extracted literal effects. |
| <span id="m-d7d9996857b1"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4837–4860 | CheckSessionUnlocked @4839; HasPermission @4840; Equals @4850; GetFileNameWithoutExtension @4850; Add @4851; GetEntryAssembly @4851; Start @4853; ReportException @4858 | No extracted literal effects. |
| <span id="m-d088ae072624"></span><code>MainViewModel.Dispose()</code><br>4862–4883 | ClearImportResults @4865; Increment @4866; ResetFinancialWorkspace @4868; Dispose @4869; Stop @4870; CancelBatchPricingPreviewExpiry @4873; Dispose @4874; Dispose @4875; DisposeSearchStates @4881; SuppressFinalize @4882 | No extracted literal effects. |
| <span id="m-5ce2af20bd7c"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4885–4889 | Stop @4887 | No extracted literal effects. |
| <span id="m-9b1e8677f397"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4891–4929 | Clear @4901; Clear @4902; Clear @4903; Clear @4904; Clear @4905; Clear @4906; Clear @4907; Clear @4908; Clear @4909; Clear @4910 | No extracted literal effects. |
| <span id="m-987d91e2050c"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4931–5048 | RaisePropertyChanged @4945; nameof @4945; Clear @4947; Clear @4948; Clear @4949; CreateCommand @4956; ExecuteReader @4958; Read @4959; TryParse @4961; GetString @4961; Add @4962; GroupBy @4971; Add @4973; Count @4973; Contains @4978; Equals @5001; Add @5003; ApplyFilter @5005; All @5007; SafeError @5010; SetActiveCashier @5018; ToString @5022; ToString @5025; ToLocalTime @5025; NotifyTotalsChanged @5047 | FROM item_kits @4957 |
| <span id="m-f52db5cee0a8"></span><code>MainViewModel.InitializeDemoData()</code><br>5050–5128 | Add @5057; Add @5076; ApplyFilter @5087; Add @5090; Add @5095; Add @5101; ApplyActivityFilter @5107; Add @5110; ApplyInventoryFilter @5119; Add @5122; Parse @5122; NotifyTotalsChanged @5127 | No extracted literal effects. |
| <span id="m-f7c609cc3435"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>5130–5143 | — | No extracted literal effects. |
| <span id="m-9af037f57a3c"></span><code>MainViewModel.SelectMenu(string)</code><br>5145–5218 | CheckSessionUnlocked @5147; NormalizeMenuKey @5151; LoadInvoicesAsync @5157; LoadCommercialAsync @5158; LoadActivityInvoicesAsync @5165; LoadTeamsStaffAsync @5168; LoadCatalogRegistryAsync @5169; UpdateDemoSeedingAvailabilityAsync @5172; UpdateReceiptDesignPreview @5175; RefreshDiagnosticsAsync @5176; LoadPriceLevelSettingsAsync @5177; RefreshWorkspaceCategories @5181; LoadInventoryAsync @5182; LoadPriceProposalsAsync @5184; LoadReportDataAsync @5187; LoadFinancialRegisterAsync @5188; LoadCustomersAsync @5191; LoadSuppliersAsync @5192; LoadThirdPartiesAsync @5193; LoadManufacturingDataAsync @5198; LoadManagedUnitsAsync @5206; LoadManagedCategoriesAsync @5209; LoadSalaryWorkspaceAsync @5212; LoadExpensesWorkspaceAsync @5215 | No extracted literal effects. |
| <span id="m-468b0b5b36b5"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>5220–5239 | — | No extracted literal effects. |
| <span id="m-ebd810533005"></span><code>MainViewModel.LogOut()</code><br>5241–5262 | Clear @5243; RaisePropertyChanged @5246; nameof @5246; ClearNotifications @5248; ResetCashReview @5252; Lock @5255; RefreshUnlockCandidates @5260; UpdateDemoSeedingAvailabilityAsync @5261 | No extracted literal effects. |
| <span id="m-6c594e23709b"></span><code>MainViewModel.UnlockSession()</code><br>5264–5267 | UnlockSession @5266 | No extracted literal effects. |
| <span id="m-e77058b285f2"></span><code>MainViewModel.UnlockSession(string?)</code><br>5269–5368 | IsLockScreenLockedOut @5277; IsNullOrWhiteSpace @5293; AuthenticateSelectedUser @5302; Lock @5307; AddSeconds @5313; AddMinutes @5330; Initialize @5349; Unlock @5350; Any @5354; Equals @5354; RaisePropertyChanged @5355; nameof @5355; LoadActivityInvoicesAsync @5359; LoadTrackOrdersAsync @5360; UpdateDemoSeedingAvailabilityAsync @5361; StartAutomaticDemoDatasetLoadAsync @5362 | No extracted literal effects. |
| <span id="m-947f4bae1fc5"></span><code>MainViewModel.PowerAction()</code><br>5370–5376 | CheckSessionUnlocked @5372 | No extracted literal effects. |
| <span id="m-639752e31ed7"></span><code>MainViewModel.CycleTable()</code><br>5378–5384 | CheckSessionUnlocked @5380 | No extracted literal effects. |
| <span id="m-ffb04c9fe440"></span><code>MainViewModel.CycleDiningType()</code><br>5386–5392 | CheckSessionUnlocked @5388 | No extracted literal effects. |
| <span id="m-538ae5c3b1fc"></span><code>MainViewModel.CycleCustomer()</code><br>5394–5397 | OpenCustomerChooser @5396 | No extracted literal effects. |
| <span id="m-c20c3e7c9516"></span><code>MainViewModel.OpenPromoDialog()</code><br>5399–5414 | CheckSessionUnlocked @5401; IsNullOrWhiteSpace @5408; RaisePropertyChanged @5412; nameof @5412 | No extracted literal effects. |
| <span id="m-8c52afc4fcb9"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5416–5485 | CheckSessionUnlocked @5418; ToLowerInvariant @5431; Trim @5431; IsNullOrWhiteSpace @5438; Trim @5438; ToList @5446; Select @5446; ToMinorUnits @5450; Equals @5466; Calculate @5470; NotifyTotalsChanged @5482; ConfigureAwait @5484; SaveDurableCartAsync @5484 | No extracted literal effects. |
| <span id="m-8e4421f287c8"></span><code>MainViewModel.TogglePromo()</code><br>5487–5504 | CheckSessionUnlocked @5489; RemovePromo @5498; OpenPromoDialog @5502 | No extracted literal effects. |
| <span id="m-8c49e115b56a"></span><code>MainViewModel.RemovePromo()</code><br>5506–5516 | NotifyTotalsChanged @5513; SaveDurableCartAsync @5515 | No extracted literal effects. |
| <span id="m-1aeb4110f1f8"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5518–5529 | CheckSessionUnlocked @5520; NotifyTotalsChanged @5526; ConfigureAwait @5528; SaveDurableCartAsync @5528 | No extracted literal effects. |
| <span id="m-53962287f7a0"></span><code>MainViewModel.CancelPromoDialog()</code><br>5531–5535 | — | No extracted literal effects. |
| <span id="m-ee149b3cb753"></span><code>MainViewModel.RecalculateCart()</code><br>5537–5591 | ToMinorUnits @5553; Add @5554; Equals @5575; Calculate @5579; ToDictionary @5582; TryGetValue @5585 | No extracted literal effects. |
| <span id="m-7de02a9a5487"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5593–5600 | CheckSessionUnlocked @5595; ResetCashReview @5596 | No extracted literal effects. |
| <span id="m-1e1c34263d83"></span><code>MainViewModel.SelectCategory(CategoryItem?)</code><br>5602–5648 | CheckSessionUnlocked @5604; RaisePropertyChanged @5612; nameof @5612; ApplyFilter @5613; Localize @5616 | No extracted literal effects. |
| <span id="m-00a26ef552ec"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5650–5650 | AddToCart @5650 | No extracted literal effects. |
| <span id="m-ac6442cc7ae4"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5652–5696 | CheckSessionUnlocked @5654; ResetCashReview @5655; ResolveProductSaleUnitFactor @5658; Round @5665; FirstOrDefault @5666; UpdateCartKitBreakdownAsync @5675; Add @5687; NotifyTotalsChanged @5690; SaveDurableCartAsync @5692; IsNullOrWhiteSpace @5694; ToString @5694; NewGuid @5694; RecordSuccessfulSearchUseAsync @5695; FromGuid @5695 | No extracted literal effects. |
| <span id="m-8fe95f48d849"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5698–5711 | CheckSessionUnlocked @5700; ResetCashReview @5701; UpdateCartKitBreakdownAsync @5708; NotifyTotalsChanged @5709; SaveDurableCartAsync @5710 | No extracted literal effects. |
| <span id="m-7b96d43f746c"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5713–5728 | CheckSessionUnlocked @5715; ResetCashReview @5716; UpdateCartKitBreakdownAsync @5720; Remove @5724; NotifyTotalsChanged @5726; SaveDurableCartAsync @5727 | No extracted literal effects. |
| <span id="m-2c4f6cd58b12"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5730–5736 | ConfigureAwait @5733; LoadAsync @5733; RefreshSavedPaymentImages @5734; CancelManualPaymentSettings @5735 | No extracted literal effects. |
| <span id="m-a091e628e048"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5738–5767 | ValidImage @5745; CreatePaymentBitmap @5750; Dispose @5753; RaisePropertyChanged @5765; nameof @5765 | No extracted literal effects. |
| <span id="m-08169e1e36cf"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5769–5785 | Dispose @5779; CreatePaymentBitmap @5781; RaisePropertyChanged @5783; nameof @5783 | No extracted literal effects. |
| <span id="m-fd86a70bddd2"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5787–5791 | — | No extracted literal effects. |
| <span id="m-969850c1dfcc"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5793–5801 | Dispose @5795; CreatePaymentBitmap @5797; RaisePropertyChanged @5799; nameof @5799 | No extracted literal effects. |
| <span id="m-61d485e6229b"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5803–5822 | ConfigureAwait @5812; ExecuteAsync @5812; DispatchToUi @5815; SafePipelineError @5815; LoadAsync @5818; RefreshSavedPaymentImages @5819; CancelManualPaymentSettings @5820 | No extracted literal effects. |
| <span id="m-be1ef2c42861"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5824–5843 | IsNullOrWhiteSpace @5828; Trim @5829; ToMinorUnits @5835; ConfigureAwait @5841; PlaceOrderAsync @5841 | No extracted literal effects. |
| <span id="m-bcf2453ab6b3"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5845–5857 | PlaceOrderInternalAsync @5851 | No extracted literal effects. |
| <span id="m-335b897c4a05"></span><code>MainViewModel.PlaceOrderInternalAsync()</code><br>5859–6060 | Localize @5863; ExecuteDemoPlaceOrder @5869; ConfigureAwait @5895; SaveDurableCartAsync @5895; ToMinorUnits @5903; Trim @5905; Equals @5916; Equals @5923; ResetCashReview @5925; Max @5983; Add @5988; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6006; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6006; Format @6018; ToDecimal @6018; DispatchToUi @6020; Clear @6024; NewGuid @6033; NotifyTotalsChanged @6034; LoadActivityInvoicesAsync @6041; OpenStaleCartPriceReviewAsync @6046; RequestElevationForCheckout @6048; SafePipelineError @6052; SafeError @6058 | No extracted literal effects. |
| <span id="m-6b129dd5cd24"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>6062–6094 | DispatchToUi @6066; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @6069; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @6069; SafePipelineError @6074; ToArray @6078; Select @6078; Where @6078; FormatCartReviewMoney @6082; Clear @6089; Add @6090 | No extracted literal effects. |
| <span id="m-3331cc6b0924"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>6096–6101 | ScalingFactor @6098; Format @6100; Equals @6100 | No extracted literal effects. |
| <span id="m-9e624fc24793"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>6103–6134 | CheckSessionUnlocked @6105; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @6107; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @6107; DispatchToUi @6112; SafePipelineError @6112; ConfigureAwait @6113; OpenStaleCartPriceReviewAsync @6113; FirstOrDefault @6120; ScalingFactor @6123; ResetCashReview @6127; Clear @6130; NotifyTotalsChanged @6131 | No extracted literal effects. |
| <span id="m-db457ed020a2"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>6136–6143 | Clear @6140; ResetCashReview @6141 | No extracted literal effects. |
| <span id="m-3afd56050fe4"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>6145–6171 | CheckSessionUnlocked @6147; ResetCashReview @6154; ToMinorUnits @6165; ConfigureAwait @6170; PlaceOrderAsync @6170 | No extracted literal effects. |
| <span id="m-8362f4679b15"></span><code>MainViewModel.CancelCashReview()</code><br>6173–6177 | ResetCashReview @6175 | No extracted literal effects. |
| <span id="m-6d476788dd15"></span><code>MainViewModel.ResetCashReview()</code><br>6179–6188 | — | No extracted literal effects. |
| <span id="m-4c6afcd856a7"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>6190–6209 | RaisePropertyChanged @6201; nameof @6201; Clear @6204; ResetCashReview @6205; NotifyTotalsChanged @6206 | No extracted literal effects. |
| <span id="m-1b2651aed214"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>6211–6276 | ConfigureAwait @6215; WaitAsync @6215; ClearActiveCartAsync @6220; ToMinorUnits @6230; Add @6231; ToUpperInvariant @6234; ToString @6234; IsNullOrWhiteSpace @6237; SaveActiveCartAsync @6250; DispatchToUi @6269; SafeError @6269; Release @6274 | No extracted literal effects. |
| <span id="m-ced00539228d"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>6278–6337 | ConfigureAwait @6284; GetActiveCartAsync @6284; Clear @6296; FirstOrDefault @6299; ToDecimal @6303; Add @6313; NotifyTotalsChanged @6330 | No extracted literal effects. |
| <span id="m-f88af3925e67"></span><code>MainViewModel.SanitizeOrderHistorySummary(string?,bool)</code><br>6339–6352 | IsNullOrWhiteSpace @6341; Replace @6346; Trim @6351; Trim @6351 | No extracted literal effects. |
| <span id="m-af51fb21eb76"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>6354–6431 | ApplyPagedResult @6358; ToList @6359; ApplyActivityFilter @6363; HasPermission @6368; ConfigureAwait @6375; GetPagedActivityInvoicesAsync @6375; ToPageRequest @6378; ToDecimal @6384; Add @6385; ToString @6390; ToLocalTime @6390; SanitizeOrderHistorySummary @6391; DispatchToUi @6409; Clear @6411; Add @6414; SafeError @6428 | No extracted literal effects. |
| <span id="m-ed08104acb8c"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>6433–6510 | HasPermission @6438; ConfigureAwait @6445; GetActiveOrdersAsync @6445; Clear @6446; ToDecimal @6450; Join @6484; Select @6484; Add @6486; ToString @6501; ToLocalTime @6501; SanitizeOrderHistorySummary @6502 | No extracted literal effects. |
| <span id="m-b1ad43577f89"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6512–6539 | CheckSessionUnlocked @6514; Clear @6517; ConfigureAwait @6523; GetOrderByIdAsync @6523; Add @6528; DispatchToUi @6534; SafeError @6534 | No extracted literal effects. |
| <span id="m-a395097a57cf"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6541–6546 | Clear @6545 | No extracted literal effects. |
| <span id="m-6562aee239af"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6548–6581 | CheckSessionUnlocked @6550; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6566; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6566; ConfigureAwait @6575; LoadTrackOrdersAsync @6575; DispatchToUi @6579; SafePipelineError @6579 | No extracted literal effects. |
| <span id="m-b4d83915ef8a"></span><code>MainViewModel.MarkReadyAsync()</code><br>6583–6616 | CheckSessionUnlocked @6585; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6601; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6601; ConfigureAwait @6610; LoadTrackOrdersAsync @6610; DispatchToUi @6614; SafePipelineError @6614 | No extracted literal effects. |
| <span id="m-6306b051c179"></span><code>MainViewModel.MarkServedAsync()</code><br>6618–6651 | CheckSessionUnlocked @6620; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6636; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6636; ConfigureAwait @6645; LoadTrackOrdersAsync @6645; DispatchToUi @6649; SafePipelineError @6649 | No extracted literal effects. |
| <span id="m-99c264fdab4a"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6653–6681 | CheckSessionUnlocked @6655; Remove @6659; CloseOrderDetailsModal @6660; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6669; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6669; ConfigureAwait @6675; LoadTrackOrdersAsync @6675; DispatchToUi @6679; SafePipelineError @6679 | No extracted literal effects. |
| <span id="m-360b403af824"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6683–6779 | CheckSessionUnlocked @6685; CloseOrderDetailsModal @6691; ConfigureAwait @6698; GetOrderByIdAsync @6698; Zero @6720; NewGuid @6726; ToList @6729; Select @6729; ToUpperInvariant @6732; ToString @6732; SaveActiveCartAsync @6741; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6757; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6757; DispatchToUi @6760; SafePipelineError @6760; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6766; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6766; LoadTrackOrdersAsync @6772; LoadActivityInvoicesAsync @6773 | No extracted literal effects. |
| <span id="m-d83cd0d0a498"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6781–6788 | CheckSessionUnlocked @6783 | No extracted literal effects. |
| <span id="m-bba0b95743d5"></span><code>MainViewModel.FilterActivity(string)</code><br>6807–6813 | CheckSessionUnlocked @6809; ApplyActivityFilter @6811 | No extracted literal effects. |
| <span id="m-54e4eb901883"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6815–6854 | Clear @6817; AsEnumerable @6818; Where @6823; IsNullOrWhiteSpace @6826; Trim @6828; Contains @6830; Contains @6831; Contains @6832; IsNullOrEmpty @6836; Equals @6838; ToList @6842; Add @6844; ApplyPagedResult @6848 | No extracted literal effects. |
| <span id="m-860ae2d62da2"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6856–6892 | CheckSessionUnlocked @6858; ConfigureAwait(QueueReceiptReprintCommand, string) @6878; ExecuteAsync(QueueReceiptReprintCommand, string) @6878; IsNullOrWhiteSpace @6879; ReportError @6881; RefreshOutputStatusAsync @6886; DispatchToUi @6890; SafeError @6890 | No extracted literal effects. |
| <span id="m-5777eaad2f7b"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6894–6937 | RefreshOutputPrinterQueues @6899; ReadAsync @6900; Equals @6907; IsNullOrWhiteSpace @6907; TryReadGeometry @6909; ComputeCapabilityFingerprint @6913; ConfigureAwait @6917; InvalidateThermalVerificationAsync @6917; LoadCashFinancialSettingsAsync @6929; LoadReceiptDesignAsync @6930; RefreshOutputStatusAsync @6931; DispatchToUi @6935; SafeError @6935 | No extracted literal effects. |
| <span id="m-10ffbcbfc257"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6939–6965 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6952; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6952; ReportError @6955; LoadOutputDevicesAsync @6958; DispatchToUi @6963; SafeError @6963 | No extracted literal effects. |
| <span id="m-ea41f59c2078"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6967–7040 | Equals @6981; IsNullOrWhiteSpace @6986; IsWindows @6991; TryReadGeometry @6996; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @7013; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @7013; ReportError @7016; Render @7019; ToString @7020; ConfigureAwait @7021; Run @7021; Send @7021; ComputeCapabilityFingerprint @7022; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @7023; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @7023; RefreshOutputStatusAsync @7034; DispatchToUi @7038; SafeError @7038 | No extracted literal effects. |
| <span id="m-383a82f71e0f"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>7042–7079 | IsWindows @7056; IsNullOrWhiteSpace @7056; TryReadGeometry @7058; ComputeCapabilityFingerprint @7062; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @7063; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @7063; ReportError @7067; ConfigureAwait @7073; RefreshOutputStatusAsync @7073; DispatchToUi @7077; SafeError @7077 | InvalidOperationException @7057; InvalidOperationException @7061 |
| <span id="m-f5421514dc6b"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>7081–7118 | CreateCommand @7086; ConfigureAwait @7095; ExecuteReaderAsync @7095; ReadAsync @7096; GetInt32 @7099; GetString @7099; GetInt64 @7099; Parse @7100; RaisePropertyChanged @7102; nameof @7102; NotifyTotalsChanged @7111; DispatchToUi @7116; SafeError @7116 | FROM store_config @7087 |
| <span id="m-5f4f3ca88c77"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>7120–7148 | ConfigureAwait @7133; ExecuteAsync @7133; ReportError @7136; NotifyTotalsChanged @7141; DispatchToUi @7146; SafeError @7146 | No extracted literal effects. |
| <span id="m-f3d1f327ca49"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>7150–7194 | DispatchToUi @7154; CreateCommand @7159; ConfigureAwait @7165; ExecuteReaderAsync @7165; ReadAsync @7166; Deserialize(ReceiptDesignDocument) @7168; GetString @7168; SafeError @7187 | FROM receipt_designs @7160; JOIN receipt_design_versions @7160 |
| <span id="m-177890bfc0f6"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>7196–7223 | ConfigureAwait @7209; ExecuteAsync @7209; ReportError @7214; DispatchToUi @7221; SafeError @7221 | No extracted literal effects. |
| <span id="m-5d559d7d56ab"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>7225–7237 | IsWindows @7227; Select @7228; Enumerate @7228; Empty(string) @7229; ToArray @7230; OrderBy @7230; Distinct @7230; Where @7230; Append @7230; IsNullOrWhiteSpace @7231; Clear @7235; Add @7236 | No extracted literal effects. |
| <span id="m-39bf61ea40df"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>7239–7297 | CheckAccess @7241; DispatchToUi @7243; CreateSampleData @7249; Equals @7255; IsWindows @7262; TryReadGeometry @7263; BuildPaperDocument @7272; RenderPreviewPngPages @7275; SetReceiptDesignPreviewPages @7277; Localize @7279; BuildThermalLines @7284; RenderPreviewPng @7286; Empty(byte[]) @7293; ReportException @7295 | No extracted literal effects. |
| <span id="m-fa9a3710eb2d"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>7299–7304 | ShowReceiptDesignPreviewPage @7303 | No extracted literal effects. |
| <span id="m-4ff5b3009adb"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>7306–7312 | ShowReceiptDesignPreviewPage @7311 | No extracted literal effects. |
| <span id="m-de49c0652c65"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>7314–7328 | RaisePropertyChanged @7325; nameof @7325 | No extracted literal effects. |
| <span id="m-2fd38c9ae6aa"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>7330–7359 | ReadAsync @7333; Localize @7336; CreateCommand @7338; ConfigureAwait @7340; ExecuteScalarAsync @7340; ToString @7340; IsNullOrWhiteSpace @7341; ExecuteReaderAsync @7355; ReadAsync @7356; Trim @7357; GetString @7357 | FROM hardware_jobs @7339; FROM hardware_jobs @7354 |
| <span id="m-54ea55939e0b"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>7361–7381 | Clear @7363; AsEnumerable @7364; Where @7367; Equals @7367; IsNullOrWhiteSpace @7373; Contains @7375; Contains @7376; Contains @7377; Add @7380 | No extracted literal effects. |
| <span id="m-c4a2eb2ed897"></span><code>MainViewModel.SelectInventoryKind(string)</code><br>7383–7427 | NormalizeItemKind @7385; SelectCatalogKind @7388; Clear @7392; ClearSelection @7397; InvalidateSelectedBatchPreview @7398; IsNullOrEmpty @7401; RaisePropertyChanged @7409; nameof @7409; ResetToFirstPage @7412; NotifySelectionScopeChange @7413; SetSelectionScope @7413; InventorySelectionScope @7413; RefreshWorkspaceCategories @7416; LoadInventoryAsync @7419 | No extracted literal effects. |
| <span id="m-1d192d9ca99f"></span><code>MainViewModel.RefreshWorkspaceCategories()</code><br>7429–7488 | Clear @7431; Equals @7432; IsNullOrEmpty @7436; Add @7441; Localize @7444; Add @7455; RaisePropertyChanged @7487; nameof @7487 | No extracted literal effects. |
| <span id="m-7f7e12e99813"></span><code>MainViewModel.SelectWorkspaceCategory(CategoryItem?)</code><br>7490–7523 | Equals @7493; Localize @7495; RaisePropertyChanged @7507; nameof @7507; ClearSelection @7518; InvalidateSelectedBatchPreview @7519; ResetToFirstPage @7520; NotifySelectionScopeChange @7521; SetSelectionScope @7521; InventorySelectionScope @7521; LoadInventoryAsync @7522 | No extracted literal effects. |
| <span id="m-f3c1f94b1a73"></span><code>MainViewModel.GenerateXReport()</code><br>7525–7544 | CheckSessionUnlocked @7527; ToString @7531; GenerateXReportInternalAsync @7543 | No extracted literal effects. |
| <span id="m-1ec6ea2a7425"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>7546–7561 | ConfigureAwait @7550; LoadReportDataAsync @7550; DispatchToUi @7559; SafeError @7559 | No extracted literal effects. |
| <span id="m-95df91e8e4fe"></span><code>MainViewModel.CloseShiftZReport()</code><br>7563–7566 | OpenCloseShiftModal @7565 | No extracted literal effects. |
| <span id="m-c8aed41fe32f"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>7568–7577 | CheckSessionUnlocked @7575 | No extracted literal effects. |
| <span id="m-bb4795977e55"></span><code>MainViewModel.SaveSettings()</code><br>7579–7583 | CheckSessionUnlocked @7581 | No extracted literal effects. |
| <span id="m-41fab778bef3"></span><code>MainViewModel.ApplySettingsAsync()</code><br>7585–7672 | CheckSessionUnlocked @7594; NotifyTotalsChanged @7613; ExecuteAsync @7641; DispatchToUi @7665; SafePipelineError @7665; SafeError @7670 | No extracted literal effects. |
| <span id="m-cdb62d1022e9"></span><code>MainViewModel.CancelSettings()</code><br>7674–7695 | CheckSessionUnlocked @7676; NotifyTotalsChanged @7688 | No extracted literal effects. |
| <span id="m-86e3f7d4b1c3"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7698–7728 | ProbeDatabaseAsync @7711; ProbeLicense @7717; RefreshOutputStatusAsync @7720; ProbeHardwareStubs @7721; DispatchToUi @7726; SafeError @7726 | No extracted literal effects. |
| <span id="m-78edda02f9d8"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7789–7827 | RaisePropertyChanged @7791; nameof @7791; FormatRealResetPreviewSummary @7826 | No extracted literal effects. |
| <span id="m-cf7f6b45ba10"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7829–7842 | Localize @7830; ToString @7832; GetValueOrDefault @7832; ToString @7837; ToString @7838; ToString @7839 | No extracted literal effects. |
| <span id="m-881f4f25f850"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7951–8043 | Post @7955; ConfigureAwait @7962; GetWorkspaceEnvironmentAsync @7962; Equals @7963; GetDatasetStateAsync @7965; CreateCommand @7971; CreateParameter @7978; ToString @7980; Add @7981; ExecuteScalarAsync @7982; HasPermission @7987; ToInt64 @7992; ExecuteScalarAsync @7992; ExecuteScalarAsync @7996; ExecuteScalarAsync @8003; ExecuteScalarAsync @8009; Localize @8028 | FROM items @7991; FROM sales_invoices @7995; FROM third_parties @8008; FROM users @7972; JOIN user_roles @7972 · DYNAMIC SQL: inspect manually |
| <span id="m-342cb5f06f21"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>8045–8055 | CheckSessionUnlocked @8047; HasPermission @8048 | No extracted literal effects. |
| <span id="m-6cfc2edfa9b9"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>8057–8062 | ConfigureAwait @8061; ResetDatabaseAsync @8061 | No extracted literal effects. |
| <span id="m-789e3f3451d3"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>8064–8065 | ConfigureAwait @8065; EnsureDefaultDemoDatasetAsync @8065 | No extracted literal effects. |
| <span id="m-157613039ed4"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>8067–8073 | EnsureDefaultDemoDatasetAsync @8071 | No extracted literal effects. |
| <span id="m-3162045830ed"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>8075–8179 | Localize @8080; ConfigureAwait @8087; WaitAsync @8087; GetWorkspaceEnvironmentAsync @8090; Equals @8091; HasPermission @8098; Post @8112; LocalizeDemoSeedProgress @8114; EnsureInitialDatasetAsync @8120; Join @8144; Select @8144; ReloadCatalogAsync @8154; LoadInventoryAsync @8155; LoadThirdPartiesAsync @8156; LoadManufacturingDataAsync @8157; LoadSuppliersAsync @8158; UpdateDemoSeedingAvailabilityAsync @8159; ToUpperInvariant @8164; ToString @8164; NewGuid @8164; LogDiagnosticError @8165; ReportError @8170; Release @8177 | No extracted literal effects. |
| <span id="m-45c26e0e1dc0"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>8181–8195 | Localize @8183 | No extracted literal effects. |
| <span id="m-2eb86c698415"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>8197–8294 | Localize @8201; ConfigureAwait @8205; WaitAsync @8205; HasPermission @8209; GetWorkspaceEnvironmentAsync @8216; Equals @8217; ResetDatabaseAsync @8225; GetStoreProfileAsync @8228; Post @8229; Clear @8232; Clear @8233; Clear @8234; NewGuid @8235; RaisePropertyChanged @8238; nameof @8238; Lock @8239; Defaults @8252; RefreshUnlockCandidates @8265; LoadCashFinancialSettingsAsync @8266; LoadOutputDevicesAsync @8267; LoadManualPaymentSettingsAsync @8268; LoadReceiptDesignAsync @8269; ReloadCatalogAsync @8270; LoadInventoryAsync @8271; LoadThirdPartiesAsync @8272; LoadManufacturingDataAsync @8273; LoadActivityInvoicesAsync @8274; UpdateDemoSeedingAvailabilityAsync @8275; ToUpperInvariant @8280; ToString @8280; LogDiagnosticError @8281; ReportError @8287; Release @8292 | No extracted literal effects. |
| <span id="m-3e47415295b8"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>8296–8338 | CheckSessionUnlocked @8298; HasPermission @8300; ConfigureAwait @8308; GetWorkspaceEnvironmentAsync @8308; Equals @8309; PreviewAsync @8312; FormatRealResetPreviewSummary @8313; Post @8314; RaisePropertyChanged @8331; nameof @8331; SafeError @8336 | UnauthorizedAccessException @8310 |
| <span id="m-1f84cc21846e"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>8340–8426 | HasPermission @8343; ConfigureAwait @8361; ExecuteAsync @8361; GetStoreProfileAsync @8370; Post @8373; Clear @8377; Clear @8378; Clear @8379; Clear @8380; NewGuid @8381; Lock @8384; RaisePropertyChanged @8398; nameof @8398; LoadCashFinancialSettingsAsync @8399; LoadOutputDevicesAsync @8400; LoadManualPaymentSettingsAsync @8401; LoadReceiptDesignAsync @8402; RefreshUnlockCandidates @8410; LoadInventoryAsync @8411; LoadActivityInvoicesAsync @8412; UpdateDemoSeedingAvailabilityAsync @8413; ToUpperInvariant @8418; ToString @8418; LogDiagnosticError @8419 | No extracted literal effects. |
| <span id="m-5d9d40a6ba33"></span><code>MainViewModel.CancelRealShopReset()</code><br>8428–8435 | RaisePropertyChanged @8434; nameof @8434 | No extracted literal effects. |
| <span id="m-4ab15fe429e5"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>8439–8456 | ConfigureAwait @8441; ExportDocumentAsync @8441; Post @8445; GetFileName @8449 | No extracted literal effects. |
| <span id="m-5d782a5aeb5a"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>8458–8480 | Exists @8463; CreateDirectory @8465; Start @8467; ToUpperInvariant @8476; ToString @8476; NewGuid @8476; LogDiagnosticError @8477 | No extracted literal effects. |
| <span id="m-6f22320784c3"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>8482–8492 | CheckSessionUnlocked @8484; RaisePropertyChanged @8486; nameof @8486; Localize @8488; ToString @8489 | No extracted literal effects. |
| <span id="m-643d613cdae1"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>8499–8515 | CheckSessionUnlocked @8501; HasPermission @8502; RaisePropertyChanged @8508; nameof @8508; Localize @8511; ToString @8512 | No extracted literal effects. |
| <span id="m-eb094d64bb69"></span><code>MainViewModel.CommitNumpad()</code><br>8517–8594 | CheckSessionUnlocked @8519; ResetCashReview @8520; TryParse @8526; IsNullOrWhiteSpace @8528; Trim @8534; NotifyTotalsChanged @8544; SaveDurableCartAsync @8545; Min @8551; ToMinorUnits @8553; Round @8554; TryParse @8569; UpdateCartKitBreakdownAsync @8577; Remove @8583; RaisePropertyChanged @8592; nameof @8592 | No extracted literal effects. |
| <span id="m-8c74a5a92d3a"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>8600–8618 | CheckSessionUnlocked @8608 | No extracted literal effects. |
| <span id="m-dff4914ec492"></span><code>MainViewModel.StageBusinessProfile()</code><br>8625–8655 | CheckSessionUnlocked @8627; HasPermission @8631 | No extracted literal effects. |
| <span id="m-584986bab4f6"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8657–8666 | — | No extracted literal effects. |
| <span id="m-0f29818244ec"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8668–8691 | RecalculateCart @8670; RaisePropertyChanged @8672; nameof @8672 | No extracted literal effects. |
| <span id="m-549626a4114a"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8693–8780 | IsNullOrWhiteSpace @8696; Trim @8696; All @8706; Trim @8723; Trim @8724; NewGuid @8728; ToString @8733; ConfigureAwait @8737; BeginTransactionAsync @8737; HandleAsync @8738; AppendAsync @8743; ToString @8744; Serialize @8749; CommitAsync @8752; Initialize @8758; Unlock @8759; RaisePropertyChanged @8764; nameof @8764; LoadTeamsStaffAsync @8767; StartAutomaticDemoDatasetLoadAsync @8768; RollbackAsync @8772; DispatchToUi @8773; SafePipelineError @8773; SafeError @8778 | No extracted literal effects. |
| <span id="m-6a9f526b4a99"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8782–8789 | IsNullOrWhiteSpace @8784; ConfigureAwait @8788; SaveTeamMemberAsync @8788 | No extracted literal effects. |
| <span id="m-1cc44b19c0b4"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8791–8809 | CheckSessionUnlocked @8794; HasPermission @8796 | No extracted literal effects. |
| <span id="m-f4c5d242795a"></span><code>MainViewModel.CancelChangePin()</code><br>8811–8818 | — | No extracted literal effects. |
| <span id="m-df4c036412ce"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8820–8896 | Trim @8828; IsNullOrWhiteSpace @8831; All @8837; Equals @8850; Equals @8851; SetQuickPin @8863; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8876; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8876; ConfigureAwait @8884; LoadTeamsStaffAsync @8884; DispatchToUi @8889; SafePipelineError @8889; SafeError @8894 | No extracted literal effects. |
| <span id="m-55e3704b30a6"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8898–8972 | HasPermission @8904; ConfigureAwait @8913; ResolveEffectivePermissionsAsync @8913; Contains @8946; Contains @8947; Add @8949; Contains @8955; DispatchToUi @8961; Clear @8963; Add @8964; SafeError @8970 | No extracted literal effects. |
| <span id="m-dc4ce388ce94"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8974–9016 | OnTeamMemberFieldChanged @8980; ConfigureAwait @8997; ExecuteAsync @8997; DispatchToUi @9001; SafePipelineError @9009; SafeError @9014 | No extracted literal effects. |
| <span id="m-47b4f28888e3"></span><code>MainViewModel.ClosePermissionEditor()</code><br>9018–9023 | — | No extracted literal effects. |
| <span id="m-299bd8ff8067"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>9025–9040 | ClearImportResults @9027 | No extracted literal effects. |
| <span id="m-2a6966998466"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>9044–9044 | — | No extracted literal effects. |
| <span id="m-0adeb4bb6999"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>9045–9045 | — | No extracted literal effects. |
| <span id="m-b15ea89331cf"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>9046–9046 | FromResult @9046 | No extracted literal effects. |
| <span id="m-13170ac4b213"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>9049–9134 | HasPermission @9058; FromDecimal @9073; ConfigureAwait(OpenShiftCommand, Shift) @9077; ExecuteAsync(OpenShiftCommand, Shift) @9077; SetActiveCashier @9092; RefreshUnlockCandidates @9093; ToUpperInvariant @9110; ToString @9110; ToString @9112; ConfigureAwait @9122; LoadTeamsStaffAsync @9122; LoadTrackOrdersAsync @9123; DispatchToUi @9127; SafePipelineError @9127; SafeError @9132 | No extracted literal effects. |
| <span id="m-d9b47ef1876e"></span><code>MainViewModel.LoadInventoryAsync()</code><br>9136–9295 | ApplyPagedResult @9140; ToList @9141; Where @9141; Equals @9141; Count @9142; ApplyInventoryFilter @9145; Clear @9154; Empty(InventoryItem) @9156; ConfigureAwait @9161; GetPagedInventoryItemsAsync @9161; ToPageRequest @9166; CreateCommand @9181; ExecuteReaderAsync @9183; ReadAsync @9184; Add @9186; Parse @9186; GetString @9186; ExecuteReaderAsync @9196; ReadAsync @9197; TryParse @9199; GetString @9199; IsDBNull @9199; Add @9210; TryGetValue @9213; Contains @9221; ToDecimal @9224; Localize @9232; ToLocalTime @9238; BuildCostSourcesTooltip @9240; DispatchToUi @9267; Add @9271; SafeError @9293 | FROM item_kits @9182; FROM item_pricing @9195 |
| <span id="m-249f6d863ef1"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>9297–9353 | CheckSessionUnlocked @9299; FirstOrDefault @9300; Clear @9311; Add @9313; CreateCommand @9318; CreateParameter @9329; Add @9332; ExecuteReader @9333; Read @9334; GetString @9336; Contains @9337; FirstOrDefault @9349; ResetReceiveLines @9350; UpdateReceiveKitBreakdownAsync @9351 | FROM uoms @9319; JOIN uoms @9319 |
| <span id="m-714299ecef12"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>9355–9456 | IsNullOrWhiteSpace @9368; Localize @9385; HasPermission @9389; BuildReceiptLines @9395; Sum @9412; Trim @9422; ToMinorUnits @9427; ConfigureAwait(ReceiveStockCommand, StockMovement) @9432; ExecuteAsync(ReceiveStockCommand, StockMovement) @9432; Clear @9442; ConfigureAwait @9444; LoadInventoryAsync @9444; LoadItemHistoryAsync @9445; DispatchToUi @9449; SafePipelineError @9449; SafeError @9454 | No extracted literal effects. |
| <span id="m-9998be64636d"></span><code>MainViewModel.ResetReceiveLines()</code><br>9462–9479 | Clear @9464; Add @9468; RaisePropertyChanged @9474; nameof @9474; Invoke @9477 | No extracted literal effects. |
| <span id="m-e0a230178b77"></span><code>MainViewModel.AddReceiveLine()</code><br>9482–9505 | IsNullOrWhiteSpace @9489; Add @9495; RaisePropertyChanged @9500; nameof @9500; Invoke @9503 | No extracted literal effects. |
| <span id="m-8b1ad47c56f5"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>9508–9525 | Remove @9515; Add @9518; RaisePropertyChanged @9524; nameof @9524 | No extracted literal effects. |
| <span id="m-086fcdf39b19"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>9531–9552 | IsNullOrWhiteSpace @9533; LastOrDefault @9538; Add @9542; Trim @9545; ReferenceEquals @9546; RaisePropertyChanged @9550; nameof @9550; Invoke @9551 | No extracted literal effects. |
| <span id="m-d3113ec16b77"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>9555–9632 | Add @9567; IsNullOrWhiteSpace @9575; Trim @9579; FirstOrDefault @9588; GroupBy @9588; Count @9590; Trim @9617 | No extracted literal effects. |
| <span id="m-0468b644e1bc"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>9634–9670 | CreateCommand @9639; ConfigureAwait @9646; ExecuteReaderAsync @9646; Clear @9647; ReadAsync @9648; Add @9650; ParseGuidSafe @9651; GetString @9651; IsDBNull @9655; GetInt32 @9659; Parse @9661; DispatchToUi @9668; SafeError @9668 | FROM third_parties @9640 |
| <span id="m-57103f1934dd"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9672–9690 | CheckSessionUnlocked @9674; FirstOrDefault @9680 | No extracted literal effects. |
| <span id="m-3751fbaa89a9"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9692–9783 | IsNullOrWhiteSpace @9715; HasPermission @9726; Trim @9744; Trim @9746; ConfigureAwait(AdjustStockCommand, StockMovement) @9750; ExecuteAsync(AdjustStockCommand, StockMovement) @9750; ConfigureAwait @9766; LoadInventoryAsync @9766; LoadItemHistoryAsync @9767; OpenWasteExpenseConfirmation @9771; DispatchToUi @9776; SafePipelineError @9776; SafeError @9781 | No extracted literal effects. |
| <span id="m-92826ccf9224"></span><code>MainViewModel.OpenAddService()</code><br>9785–9847 | ResetProductStockDraft @9787; CheckSessionUnlocked @9788; HasPermission @9789; RaisePropertyChanged @9798; nameof @9798; ClearItemHistory @9807; LoadCatalogRegistryAsync @9814; InitializeProductPricingDraft @9817; Clear @9832; Clear @9833; Clear @9842; CaptureProductModalBaselineAsync @9846 | No extracted literal effects. |
| <span id="m-f551c8b5da06"></span><code>MainViewModel.OpenAddProduct()</code><br>9849–9925 | ResetProductStockDraft @9851; CheckSessionUnlocked @9852; RaisePropertyChanged @9854; nameof @9854; HasPermission @9861; ClearItemHistory @9871; LoadCatalogRegistryAsync @9878; InitializeProductPricingDraft @9881; Clear @9896; Clear @9897; Where @9898; Add @9900; FirstOrDefault @9902; Clear @9913; CaptureProductModalBaselineAsync @9924 | No extracted literal effects. |
| <span id="m-0323c4ee19b0"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9927–9927 | OpenEditProduct @9927 | No extracted literal effects. |
| <span id="m-f3e737a15b9e"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9929–10018 | ResetProductStockDraft @9931; CheckSessionUnlocked @9933; RaisePropertyChanged @9936; nameof @9936; HasPermission @9943; ClearItemHistory @9953; LoadCatalogRegistryAsync @9961; InitializeProductPricingDraft @9967; ToMinorUnits @9968; LoadExactProductCostSnapshotsAsync @9974; ToDecimal @9978; Clear @9985; Clear @9986; Where @9987; Add @9989; FirstOrDefault @9991; LoadItemLocationEligibilitiesAsync @10010; LoadProductKitAsync @10011; LoadPrimaryBarcodeAsync @10012; LoadProductPricingDraftAsync @10013; LoadItemHistoryAsync @10014; LoadItemPriceHistoryAsync @10015; CaptureProductModalBaselineAsync @10017 | No extracted literal effects. |
| <span id="m-e5f5c6eb00c2"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>10020–10033 | OrderBy @10023; Where @10023; Add @10025 | No extracted literal effects. |
| <span id="m-45bfc2a88ec6"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>10035–10108 | CreateCommand @10042; CreateParameter @10049; ToString @10051; Add @10052; ConfigureAwait @10053; ExecuteReaderAsync @10053; ReadAsync @10054; GetInt32 @10056; IsDBNull @10057; GetString @10057; ParseStoredPricingPercentForDisplay @10058; ToDisplayAmount @10062; GetInt64 @10062; OrderBy @10082; Where @10082; TryGetValue @10085; Add @10091; InvokeAsync @10093; RaisePropertyChanged @10098; nameof @10098; CaptureProductPricingSnapshot @10101; DispatchToUi @10106; SafeError @10106 | FROM item_price_levels @10073; FROM item_pricing @10044 |
| <span id="m-5f055b1e2516"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>10110–10145 | CreateCommand @10117; CreateParameter @10123; ToString @10125; Add @10126; ConfigureAwait @10127; ExecuteReaderAsync @10127; ReadAsync @10128; Parse @10131; GetString @10131; GetInt32 @10131; GetInt64 @10132; IsDBNull @10132; Parse @10133; InvokeAsync @10135; DispatchToUi @10143; SafeError @10143 | FROM product_category_pricing_rules @10118 |
| <span id="m-1b855e0fd5ea"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>10147–10176 | ConfigureAwait @10151; WhenAll @10151; InvokeAsync @10152; CaptureProductModalSnapshot @10156; CaptureProductPricingSnapshot @10157; RaisePropertyChanged @10158; nameof @10158 | No extracted literal effects. |
| <span id="m-8414037be843"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>10178–10226 | Serialize @10178; ToArray @10201; Select @10201; Select @10218; OrderBy @10218; OrderBy @10222 | No extracted literal effects. |
| <span id="m-c2063b5cb8be"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>10228–10240 | Serialize @10228; ToArray @10239; Select @10239 | No extracted literal effects. |
| <span id="m-ea7b5c7bdc1a"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>10242–10274 | nameof @10244; RaisePropertyChanged @10245; RaiseTraceabilityState @10250; StartsWith @10254; RecomputeProductPricingPreview @10265; RefreshVirtualKitAvailability @10267 | No extracted literal effects. |
| <span id="m-f2152b64458b"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>10276–10290 | RaisePropertyChanged @10284; nameof @10284; RecomputeProductPricingPreview @10287; RefreshVirtualKitAvailability @10288 | No extracted literal effects. |
| <span id="m-528db323ff2d"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>10292–10300 | RaisePropertyChanged @10294; nameof @10294; RecomputeProductPricingPreview @10297; RefreshVirtualKitAvailability @10298 | No extracted literal effects. |
| <span id="m-a52cebacbeff"></span><code>MainViewModel.RequestCloseProductModal()</code><br>10302–10315 | DiscardProductModal @10314 | No extracted literal effects. |
| <span id="m-7e40884b1274"></span><code>MainViewModel.DiscardProductModal()</code><br>10317–10326 | RaisePropertyChanged @10322; nameof @10322; ClearItemHistory @10324 | No extracted literal effects. |
| <span id="m-d1acfe7bd76c"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>10328–10346 | CreateCommand @10333; CreateParameter @10335; ToString @10337; Add @10338; ConfigureAwait @10339; ExecuteScalarAsync @10339; DispatchToUi @10342; ToString @10342 | FROM barcodes @10334 |
| <span id="m-ae9bc5d9f370"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>10348–10399 | CreateCommand @10353; CreateParameter @10360; ToString @10362; Add @10363; ConfigureAwait @10367; ExecuteReaderAsync @10367; ReadAsync @10368; IsDBNull @10371; GetString @10371; GetDouble @10372; ResolveQuantity @10373; Add @10374; Parse @10376; DispatchToUi @10384; Clear @10387; Add @10388; RaisePropertyChanged @10391; nameof @10391; RecomputeProductPricingPreview @10394; RefreshVirtualKitAvailability @10395 | FROM item_kits @10354; JOIN item_kit_components @10354; JOIN items @10354 |
| <span id="m-dcf4e37c3542"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>10401–10401 | SaveProductConfigurationAsync @10401 | No extracted literal effects. |
| <span id="m-29de576fdd3a"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>10403–10752 | ConfigureAwait @10408; LoadCatalogRegistryAsync @10408; HasPermission @10410; IsNullOrWhiteSpace @10415; Equals @10440; ValidateUnitEligibility @10453; ToMinorUnits @10473; GetValueOrDefault @10480; Trim @10481; Trim @10482; Trim @10484; Empty(KitComponentInput) @10517; CaptureProductPricingSnapshot @10520; ToCommand @10522; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @10533; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @10533; DispatchToUi @10536; RaiseTraceabilityState @10543; CaptureProductModalSnapshot @10546; RaisePropertyChanged @10548; nameof @10548; SelectInventoryKind @10554; ReloadCatalogAsync @10556; LoadInventoryAsync @10557; LoadItemHistoryAsync @10558; SafePipelineError @10562; SafeError @10568; Localize @10580; GetValueOrDefault @10647; Trim @10650; Trim @10657; ToList @10704; Select @10704 | No extracted literal effects. |
| <span id="m-ed3909265435"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>10754–10790 | CheckSessionUnlocked @10756; HasPermission @10757; ConfigureAwait(DeactivateProductCommand, bool) @10773; ExecuteAsync(DeactivateProductCommand, bool) @10773; ConfigureAwait @10778; ReloadCatalogAsync @10778; LoadInventoryAsync @10779; DispatchToUi @10783; SafePipelineError @10783; SafeError @10788 | No extracted literal effects. |
| <span id="m-783897a9d141"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>10792–10868 | ConfigureAwait @10798; GetActiveItemsAsync @10798; Clear @10800; Clear @10801; Clear @10802; CreateCommand @10807; ExecuteReaderAsync @10809; ReadAsync @10810; TryParse @10812; GetString @10812; Add @10813; GroupBy @10821; Add @10823; Count @10823; Contains @10828; Equals @10851; Add @10853; All @10856; SafeError @10859; ApplyFilter @10862 | FROM item_kits @10808 |
| <span id="m-24b44d4f92ed"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>10870–10876 | IsNullOrWhiteSpace @10872; TryParse @10873; HashData @10874; GetBytes @10874; AsSpan @10875 | No extracted literal effects. |
| <span id="m-51a9aa748874"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>10878–10944 | CreateCommand @10884; ConfigureAwait @10887; ExecuteReaderAsync @10887; ReadAsync @10889; Add @10891; GetString @10893; GetInt32 @10897; Clear @10903; Add @10904; ExecuteReaderAsync @10916; ReadAsync @10918; Add @10920; GetString @10922; IsDBNull @10926; GetInt32 @10930; Clear @10936; Add @10937; DispatchToUi @10942; SafeError @10942 | FROM bins @10909; FROM facilities @10886; JOIN facilities @10909 |
| <span id="m-5c720b8c797c"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>11170–11292 | CreateCommand @11180; ConfigureAwait @11187; ExecuteReaderAsync @11187; ReadAsync @11188; Add @11190; ParseGuidSafe @11192; GetString @11192; IsDBNull @11195; GetInt32 @11196; Add @11216; DispatchToUi @11231; Clear @11233; Clear @11234; Clear @11235; Clear @11236; Equals @11240; Add @11241; Add @11243; Add @11245; Add @11247; Clear @11249; Add @11250; FirstOrDefault @11255; Equals @11255; FirstOrDefault @11261; ToList @11267; FirstOrDefault @11268; FirstOrDefault @11272; FirstOrDefault @11277; ApplySaleUnitDefaultsToCatalog @11282; RaisePropertyChanged @11283; nameof @11283; RefreshWorkspaceCategories @11285; SafeError @11290 | FROM product_categories @11182; FROM uoms @11208 |
| <span id="m-043d83209fed"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>11294–11308 | ResolveProductSaleUnitFactor @11298; Round @11304; ApplyFilter @11307 | No extracted literal effects. |
| <span id="m-d6ec0100b201"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>11310–11328 | FirstOrDefault @11312; Equals @11313; TryParse @11320 | No extracted literal effects. |
| <span id="m-f50f644268a6"></span><code>MainViewModel.OpenAddCategoryForCurrentKindAsync()</code><br>11330–11345 | CheckSessionUnlocked @11332; HasPermission @11333; OpenCategoryManagerAsync @11339; CaptureCategoryFormSnapshot @11342; RaisePropertyChanged @11343; nameof @11343 | No extracted literal effects. |
| <span id="m-ee70b5ff948b"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>11347–11369 | CheckSessionUnlocked @11349; HasPermission @11350; ConfigureAwait @11365; LoadManagedCategoriesAsync @11365; CaptureCategoryFormSnapshot @11367; RaisePropertyChanged @11368; nameof @11368 | No extracted literal effects. |
| <span id="m-25647187d572"></span><code>MainViewModel.CloseCategoryManager()</code><br>11371–11380 | — | No extracted literal effects. |
| <span id="m-a16111bcfa15"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>11382–11404 | CheckSessionUnlocked @11384; HasPermission @11385; ConfigureAwait @11400; LoadManagedUnitsAsync @11400; CaptureUnitFormSnapshot @11402; RaisePropertyChanged @11403; nameof @11403 | No extracted literal effects. |
| <span id="m-5ea6049d0102"></span><code>MainViewModel.CloseUnitManager()</code><br>11406–11415 | — | No extracted literal effects. |
| <span id="m-392a9a7ccb59"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>11417–11480 | Clear @11420; Clear @11421; Clear @11422; CreateCommand @11423; ConfigureAwait @11429; ExecuteReaderAsync @11429; ReadAsync @11430; Add @11432; ParseGuidSafe @11434; GetString @11434; IsDBNull @11437; GetInt32 @11438; Where @11446; Equals @11446; Add @11447; TryParse @11460; Add @11461; RefreshTargetedCategoryCollections @11474; DispatchToUi @11475; RefreshManagedCategoriesTable @11477; RefreshManagedExpenseCategoriesTable @11478 | FROM expense_categories @11451; FROM product_categories @11425; JOIN expense_records @11451 |
| <span id="m-6b5ad0881f2f"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>11482–11489 | OpenCategoryManagerAsync @11484; FirstOrDefault @11485; EditManagedCategory @11488 | No extracted literal effects. |
| <span id="m-3038bc7830db"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>11491–11499 | OpenCategoryManagerAsync @11494; FirstOrDefault @11495; EditManagedExpenseCategory @11498 | No extracted literal effects. |
| <span id="m-715180b45453"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>11501–11523 | DispatchToUi @11503; Clear @11505; Clear @11506; Clear @11507; Clear @11508; Where @11510; Equals @11513; Add @11514; Add @11516; Add @11518; Add @11520 | No extracted literal effects. |
| <span id="m-718ab2f5854b"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>11525–11537 | CaptureCategoryFormSnapshot @11535; RaisePropertyChanged @11536; nameof @11536 | No extracted literal effects. |
| <span id="m-e0a3b80bff02"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>11539–11552 | CaptureCategoryFormSnapshot @11550; RaisePropertyChanged @11551; nameof @11551 | No extracted literal effects. |
| <span id="m-e9fc9370d97d"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>11554–11564 | Serialize @11554 | No extracted literal effects. |
| <span id="m-b65626d7bcea"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>11566–11576 | Serialize @11566 | No extracted literal effects. |
| <span id="m-c303c2442d7e"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>11578–11578 | — | No extracted literal effects. |
| <span id="m-3aad4c3db7e8"></span><code>MainViewModel.DiscardRegistryForm()</code><br>11580–11596 | Equals @11583; RaisePropertyChanged @11587; nameof @11587 | No extracted literal effects. |
| <span id="m-f5bc94d23ed0"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>11598–11725 | Equals @11609; HasPermission @11611; FirstOrDefault @11620; Trim @11625; Trim @11626; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11628; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11628; DispatchToUi @11631; SafePipelineError @11631; IsNullOrWhiteSpace @11639; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @11641; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @11641; ConfigureAwait @11650; LoadManagedCategoriesAsync @11650; LoadExpenseCategoriesAsync @11651; CaptureCategoryFormSnapshot @11661; RaisePropertyChanged @11662; nameof @11662; Trim @11680; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @11682; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @11682; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @11698; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @11698; LoadCatalogRegistryAsync @11707; ReloadCatalogAsync @11708; SafeError @11723 | No extracted literal effects. |
| <span id="m-0fb43dbf98fb"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>11727–11772 | HasPermission @11737; ConfigureAwait(DeactivateCategoryCommand, bool) @11750; ExecuteAsync(DeactivateCategoryCommand, bool) @11750; ConfigureAwait(ReactivateCategoryCommand, bool) @11755; ExecuteAsync(ReactivateCategoryCommand, bool) @11755; DispatchToUi @11760; SafePipelineError @11760; ConfigureAwait @11764; LoadManagedCategoriesAsync @11764; LoadCatalogRegistryAsync @11765; ReloadCatalogAsync @11766; SafeError @11770 | No extracted literal effects. |
| <span id="m-91229d9786fe"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>11774–11814 | HasPermission @11784; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11800; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11800; DispatchToUi @11803; SafePipelineError @11803; ConfigureAwait @11807; LoadManagedCategoriesAsync @11807; LoadExpenseCategoriesAsync @11808; SafeError @11812 | No extracted literal effects. |
| <span id="m-793783aa340b"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>11816–11916 | Clear @11819; CreateCommand @11822; ConfigureAwait @11828; ExecuteReaderAsync @11828; ReadAsync @11829; Add @11831; GetString @11833; IsDBNull @11835; GetInt32 @11839; IsNullOrWhiteSpace @11850; Equals @11854; Add @11861; Clear @11865; ExecuteReaderAsync @11870; ReadAsync @11871; GetString @11873; Where @11895; Add @11897; TryGetValue @11900; FirstOrDefault @11907; Add @11911; DispatchToUi @11914; UpdateConversionPreview @11915 | FROM store_uom_preferences @11869; FROM uoms @11824 |
| <span id="m-9ddde9d7bdcd"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>11918–11925 | OpenUnitManagerAsync @11920; FirstOrDefault @11921; Equals @11921; EditManagedUnit @11924 | No extracted literal effects. |
| <span id="m-90114c9036ab"></span><code>MainViewModel.UpdateConversionPreview()</code><br>11927–11963 | IsNullOrWhiteSpace @11929; FirstOrDefault @11935; Equals @11935; TryParse @11950 | No extracted literal effects. |
| <span id="m-f734ae0e4b97"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11965–11986 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11972; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11972; DispatchToUi @11975; SafePipelineError @11979; SafeError @11984 | No extracted literal effects. |
| <span id="m-cb51fc63a667"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11988–12001 | IsNullOrWhiteSpace @11994; TryParse @11997; CaptureUnitFormSnapshot @11999; RaisePropertyChanged @12000; nameof @12000 | No extracted literal effects. |
| <span id="m-449833a55966"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>12003–12065 | IsNullOrWhiteSpace @12015; Trim @12019; Trim @12020; Trim @12023; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @12024; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @12024; DispatchToUi @12027; SafePipelineError @12027; Trim @12034; Equals @12037; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @12042; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @12042; ConfigureAwait @12050; LoadManagedUnitsAsync @12050; LoadCatalogRegistryAsync @12051; CaptureUnitFormSnapshot @12058; RaisePropertyChanged @12059; nameof @12059; SafeError @12063 | No extracted literal effects. |
| <span id="m-0fe1f492b102"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>12067–12105 | ConfigureAwait(DeactivateUomCommand, bool) @12084; ExecuteAsync(DeactivateUomCommand, bool) @12084; ConfigureAwait(ReactivateUomCommand, bool) @12089; ExecuteAsync(ReactivateUomCommand, bool) @12089; DispatchToUi @12094; SafePipelineError @12094; ConfigureAwait @12098; LoadManagedUnitsAsync @12098; LoadCatalogRegistryAsync @12099; SafeError @12103 | No extracted literal effects. |
| <span id="m-333567cf607f"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>12107–12145 | CreateCommand @12112; CreateParameter @12119; ToString @12121; Add @12122; ConfigureAwait @12124; ExecuteReaderAsync @12124; Clear @12125; ReadAsync @12126; Add @12128; ParseGuidSafe @12130; GetString @12130; GetInt32 @12133; IsDBNull @12135; ToDecimal @12135; GetDouble @12135; DispatchToUi @12143; SafeError @12143 | FROM item_locations @12113 |
| <span id="m-5584365dcacf"></span><code>MainViewModel.OpenLocationsModal()</code><br>12148–12174 | CheckSessionUnlocked @12150; HasPermission @12151; LoadFacilitiesAndBinsAsync @12172 | No extracted literal effects. |
| <span id="m-1c5776313e2d"></span><code>MainViewModel.OpenAddFacility()</code><br>12176–12184 | — | No extracted literal effects. |
| <span id="m-f24fdc68c698"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>12186–12195 | — | No extracted literal effects. |
| <span id="m-42407eddc84f"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>12197–12256 | HasPermission @12200; IsNullOrWhiteSpace @12205; IsNullOrEmpty @12221; Trim @12223; Trim @12223; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @12224; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @12224; OpenAddFacility @12228; ConfigureAwait @12229; LoadFacilitiesAndBinsAsync @12229; DispatchToUi @12233; SafePipelineError @12233; ConfigureAwait(CreateFacilityCommand, FacilityDto) @12239; ExecuteAsync(CreateFacilityCommand, FacilityDto) @12239; SafeError @12254 | No extracted literal effects. |
| <span id="m-51790f134c61"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>12258–12289 | HasPermission @12261; ConfigureAwait(DeactivateFacilityCommand, bool) @12273; ExecuteAsync(DeactivateFacilityCommand, bool) @12273; OpenAddFacility @12277; ConfigureAwait @12278; LoadFacilitiesAndBinsAsync @12278; DispatchToUi @12282; SafePipelineError @12282; SafeError @12287 | No extracted literal effects. |
| <span id="m-3b256c709f1f"></span><code>MainViewModel.OpenAddBin()</code><br>12291–12302 | FirstOrDefault @12301 | No extracted literal effects. |
| <span id="m-c5af57e0c398"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>12304–12316 | FirstOrDefault @12314 | No extracted literal effects. |
| <span id="m-a6c4f010560e"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>12318–12393 | HasPermission @12321; IsNullOrWhiteSpace @12331; IsNullOrEmpty @12342; Trim @12347; Trim @12348; Trim @12349; Trim @12350; Trim @12351; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @12354; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @12354; OpenAddBin @12358; ConfigureAwait @12359; LoadFacilitiesAndBinsAsync @12359; DispatchToUi @12363; SafePipelineError @12363; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @12376; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @12376; SafeError @12391 | No extracted literal effects. |
| <span id="m-769c974c10d1"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>12395–12426 | HasPermission @12398; ConfigureAwait(DeactivateLocationBinCommand, bool) @12410; ExecuteAsync(DeactivateLocationBinCommand, bool) @12410; OpenAddBin @12414; ConfigureAwait @12415; LoadFacilitiesAndBinsAsync @12415; DispatchToUi @12419; SafePipelineError @12419; SafeError @12424 | No extracted literal effects. |
| <span id="m-31603049a53a"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>12428–12481 | HasPermission @12436; IsNullOrWhiteSpace @12441; Trim @12453; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @12461; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @12461; ConfigureAwait @12469; LoadItemLocationEligibilitiesAsync @12469; DispatchToUi @12474; SafePipelineError @12474; SafeError @12479 | No extracted literal effects. |
| <span id="m-b644d22744de"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>12483–12513 | HasPermission @12486; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @12498; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @12498; ConfigureAwait @12501; LoadItemLocationEligibilitiesAsync @12501; DispatchToUi @12506; SafePipelineError @12506; SafeError @12511 | No extracted literal effects. |
| <span id="m-e1fff2bb019c"></span><code>MainViewModel.LoadCustomersAsync()</code><br>12516–12549 | NewGuid @12524; Clear @12530; Add @12531; FilterCustomers @12533; ConfigureAwait @12540; GetCustomersAsync @12540; DispatchToUi @12547; SafeError @12547 | No extracted literal effects. |
| <span id="m-811c2be87e1b"></span><code>MainViewModel.FilterCustomers()</code><br>12551–12564 | Clear @12553; Trim @12554; IsNullOrWhiteSpace @12555; Where @12557; Contains @12557; Contains @12558; Contains @12559; Add @12562 | No extracted literal effects. |
| <span id="m-abf2459d7a6d"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>12566–12602 | CheckSessionUnlocked @12568; CreateCommand @12577; CreateParameter @12580; ToString @12582; Add @12583; ConfigureAwait @12584; ExecuteScalarAsync @12584; ToString @12585; Equals @12588; LoadPickerCandidatesAsync @12600; DispatchToUi @12601 | FROM items @12579 |
| <span id="m-d3567d354fd3"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>12604–12665 | ConfigureAwait @12611; GetLotCandidatesAsync @12611; DispatchToUi @12614; Clear @12616; Add @12619; ToString @12628; GetSerialCandidatesAsync @12636; Clear @12641; Add @12644; ToString @12653 | No extracted literal effects. |
| <span id="m-71b65f548db8"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>12667–12673 | Clear @12670; Clear @12671 | No extracted literal effects. |
| <span id="m-a2d28d6dc022"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>12675–12734 | FirstOrDefault @12688; ConfigureAwait(SelectLotForCartLineCommand, bool) @12696; ExecuteAsync(SelectLotForCartLineCommand, bool) @12696; DispatchToUi @12699; SafePipelineError @12699; ToList @12705; Where @12705; ConfigureAwait(SelectSerialForCartLineCommand, bool) @12715; ExecuteAsync(SelectSerialForCartLineCommand, bool) @12715; SafeError @12732 | No extracted literal effects. |
| <span id="m-b597c3d9251b"></span><code>MainViewModel.OpenCustomerChooser()</code><br>12736–12744 | CheckSessionUnlocked @12738; Clear @12741; LoadCustomersAsync @12742 | No extracted literal effects. |
| <span id="m-082e61428c03"></span><code>MainViewModel.CloseCustomerChooser()</code><br>12746–12749 | — | No extracted literal effects. |
| <span id="m-cadf583acd6d"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>12751–12768 | SaveDurableCartAsync @12761; IsNullOrWhiteSpace @12765; ToString @12765; NewGuid @12765; RecordSuccessfulSearchUseAsync @12766; FromGuid @12766 | No extracted literal effects. |
| <span id="m-e842810d9841"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>12770–12779 | SaveDurableCartAsync @12778 | No extracted literal effects. |
| <span id="m-701efbf9f998"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>12781–12826 | CheckSessionUnlocked @12783; IndexOf @12787; SelectWalkInCustomer @12793; FilterCustomers @12795; ConfigureAwait(DeactivateCustomerCommand, bool) @12807; ExecuteAsync(DeactivateCustomerCommand, bool) @12807; ConfigureAwait @12814; LoadCustomersAsync @12814; DispatchToUi @12819; SafePipelineError @12819; SafeError @12824 | No extracted literal effects. |
| <span id="m-63961dfbd06f"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>12955–12994 | Add @12961; NewGuid @12962; RefreshManufacturingTablesAsync @12976; ConfigureAwait @12984; GetKitsAsync @12984; Clear @12985; Add @12986; DispatchToUi @12992; SafeError @12992 | No extracted literal effects. |
| <span id="m-ca92405c17a7"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12998–13014 | CheckSessionUnlocked @13000; SetProductionActionMode @13002; FirstOrDefault @13007; LoadProductionIngredientLotsAsync @13012; TakeProductionSnapshot @13013 | No extracted literal effects. |
| <span id="m-756a75e56eba"></span><code>MainViewModel.CloseProductionModal()</code><br>13016–13030 | — | No extracted literal effects. |
| <span id="m-fb7eca4acb19"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>13032–13131 | ExecuteExistingProductionAsync @13035; Resolve @13057; NewGuid @13060; ToUpperInvariant @13062; ToString @13062; Insert @13080; IsNullOrWhiteSpace @13102; Trim @13102; ToDictionary @13104; Where @13104; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @13108; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @13108; DispatchToUi @13111; SafePipelineError @13111; RecordSuccessfulSearchUseAsync @13118; FromGuid @13118; ConfigureAwait @13121; LoadManufacturingDataAsync @13121; LoadInventoryAsync @13122; SafeError @13128 | No extracted literal effects. |
| <span id="m-a669e8e1f49e"></span><code>MainViewModel.CloseXReportModal()</code><br>13230–13233 | — | No extracted literal effects. |
| <span id="m-4f9eb1255891"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>13235–13265 | CheckSessionUnlocked @13237; Clear @13255; Where @13256; GetUnlockCandidates @13256; Equals @13257; Add @13261 | No extracted literal effects. |
| <span id="m-eab60aa576e8"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>13267–13271 | — | No extracted literal effects. |
| <span id="m-cfb6984df2e9"></span><code>MainViewModel.CloseZReportModal()</code><br>13273–13276 | — | No extracted literal effects. |
| <span id="m-c177bd09170d"></span><code>MainViewModel.LoadReportDataAsync()</code><br>13278–13395 | ToString @13298; DispatchToUi @13314; ConfigureAwait @13342; ExecuteAsync @13342; Join @13344; Select(string, Money) @13344; InvoiceMoney @13344; ToDecimal @13347; ToDecimal @13348; ToDecimal @13349; ToDecimal @13350; ToDecimal @13352; ToDecimal @13354; ToDecimal @13355; ToDecimal @13356; ToDecimal @13357; ToDecimal @13358; ToUpperInvariant @13360; ToString @13360; ToString @13362; ToString @13363; Sum @13369; ToDecimal @13369; ToDecimal @13372; Add @13374; Format @13379; SafeError @13387 | No extracted literal effects. |
| <span id="m-a0b4dc6a1bf0"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>13397–13486 | CheckSessionUnlocked @13400; IsNullOrWhiteSpace @13417; AuthenticateSelectedUser @13425; Trim @13427; Round @13436; Trim @13440; ConfigureAwait(CloseShiftCommand, Shift) @13444; ExecuteAsync(CloseShiftCommand, Shift) @13444; DispatchToUi @13462; SafePipelineError @13462; ConfigureAwait @13469; ExecuteAsync @13469; SetActiveCashier @13473; RefreshUnlockCandidates @13474; RaisePropertyChanged @13475; nameof @13475; LoadReportDataAsync @13479; LoadTeamsStaffAsync @13480; SafeError @13484 | No extracted literal effects. |
| <span id="m-0325f2501ddc"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>13488–13564 | FirstOrDefault @13490; CreateCommand @13497; CreateParameter @13512; ToString @13514; Add @13515; ExecuteReader @13517; Read @13518; Parse @13520; GetString @13520; GetInt64 @13523; Pow @13525; IsDBNull @13527; TryParse @13533; GetInt32 @13534; Add @13557 | FROM barcodes @13498; FROM items @13498; JOIN barcodes @13498; JOIN product_categories @13498 |
| <span id="m-822c0a5de2e8"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>13566–13691 | IsNullOrWhiteSpace @13568; Trim @13571; ToList @13574; Where @13574; IsNullOrEmpty @13575; Equals @13575; Any @13576; ToString @13578; AddToCart @13588; CreateCommand @13604; CreateParameter @13622; Add @13625; ExecuteReader @13627; Read @13629; Parse @13631; GetString @13631; ContainsKey @13632; GetInt64 @13636; Pow @13638; IsDBNull @13640; TryParse @13646; GetInt32 @13647; First @13676; Add @13681 | FROM barcodes @13605; FROM items @13605; JOIN barcodes @13605; JOIN product_categories @13605 |
| <span id="m-91c3ff443107"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>13693–13736 | IsNullOrWhiteSpace @13695; Trim @13698; AppendReceiveSerialScan @13704; TryAddUniqueExactMatchToCart @13710; Clear @13712; ToList @13717; Where @13717; Equals @13717; Equals @13717; AddToCart @13720 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml</code> · 6373 lines · SHA-256 <code>69216c2ac08cd2ed0216b5b144ee5c1561e20e9d7d4c8137d11b8ea47be92fa5</code>.
