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

<code>Software/src/GetSeek.Desktop/Models/UiModels.cs</code> · 885 lines.

SHA-256: <code>211e33a7d5ed72bb58b6b65a70ce2d8ed3fed73aee455ca5b96c0802958bb025</code>.

Declarations: <code>CurrencyFormatter</code> (line 6), <code>CategoryItem : ReactiveObject</code> (line 20), <code>ProductCategoryOption</code> (line 47), <code>ExpenseCategoryOption</code> (line 64), <code>ProductPurposeOption</code> (line 79), <code>UomOption</code> (line 84), <code>StoreUomPreferenceItem : ReactiveObject</code> (line 138), <code>ProductItem : ReactiveObject</code> (line 160), <code>OrderItem : ReactiveObject</code> (line 187), <code>ParkedCart</code> (line 298), <code>StaleCartPriceReviewUiRow</code> (line 312), <code>LotCandidateItem</code> (line 320), <code>SerialCandidateItem : ReactiveObject</code> (line 335), <code>OrderStatusChip : ReactiveObject</code> (line 359), <code>OrderLogItem : ReactiveObject</code> (line 399), <code>InventoryItem : ReactiveObject</code> (line 430), <code>KitComponentDraftItem : ReactiveObject</code> (line 563), <code>PayrollMonthOption : IEquatable&lt;PayrollMonthOption&gt;</code> (line 595), <code>StaffMember : ReactiveObject</code> (line 619), <code>TeamMemberShiftItem : ReactiveObject</code> (line 679), <code>UserPermissionOverrideItem : ReactiveObject</code> (line 690), <code>ReportTenderItem : ReactiveObject</code> (line 748), <code>ShiftReportSummary : ReactiveObject</code> (line 757), <code>FacilityItem : ReactiveObject</code> (line 797), <code>BinLocationItem : ReactiveObject</code> (line 807), <code>ItemLocationEligibilityItem : ReactiveObject</code> (line 821), <code>ReceiveTrackingKind</code> (line 836), <code>ReceiveLineItem : ReactiveObject</code> (line 848).

<details markdown>
<summary>Methods, calls, table effects and failures (11)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7303823d0b7e"></span><code>CurrencyFormatter.Format(decimal,string,int)</code><br>8–17 | Clamp @10; Round @14; ToString @16 | No extracted literal effects. |
| <span id="m-1667c822cb94"></span><code>ProductCategoryOption.ToString()</code><br>61–61 | — | No extracted literal effects. |
| <span id="m-6c53d4e69e32"></span><code>ExpenseCategoryOption.ToString()</code><br>76–76 | — | No extracted literal effects. |
| <span id="m-3a2f50acce63"></span><code>ProductPurposeOption.ToString()</code><br>81–81 | — | No extracted literal effects. |
| <span id="m-b2cf49c707d1"></span><code>UomOption.ToString()</code><br>135–135 | — | No extracted literal effects. |
| <span id="m-178c1a4e38c1"></span><code>LotCandidateItem.ToString()</code><br>331–331 | — | No extracted literal effects. |
| <span id="m-06e58ae7eebf"></span><code>SerialCandidateItem.ToString()</code><br>356–356 | — | No extracted literal effects. |
| <span id="m-b574f7b3d543"></span><code>PayrollMonthOption.Equals(PayrollMonthOption?)</code><br>608–609 | — | No extracted literal effects. |
| <span id="m-ab14cc602edb"></span><code>PayrollMonthOption.Equals(object?)</code><br>611–612 | Equals @612 | No extracted literal effects. |
| <span id="m-3cf63cb700a8"></span><code>PayrollMonthOption.GetHashCode()</code><br>614–614 | GetHashCode @614 | No extracted literal effects. |
| <span id="m-8683a7b3df4c"></span><code>PayrollMonthOption.ToString()</code><br>616–616 | — | No extracted literal effects. |

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

SHA-256: <code>01a7f3aa3eaba2ec269b44a3cad5338c0665e4781c788fd7c4423f4a08f95258</code>.

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

## MainViewModel.ImportReview.cs {#src-90113acc8bd5}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ImportReview.cs</code> · 137 lines.

SHA-256: <code>0092997d42e4f8dd19b2601011d2b9bbde7b67a5ae0b4abcff5d542dbf24d77b</code>.

Declarations: <code>MainViewModel</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f756c8667b34"></span><code>MainViewModel.ExportMasterDataAsync(string)</code><br>21–37 | CheckSessionUnlocked @23; ConfigureAwait @28; ExportAsync @28; DispatchToUi @29; ReferenceEquals @31; Invoke @32; SafeError @35 | No extracted literal effects. |
| <span id="m-a62e023b1fbe"></span><code>MainViewModel.MakeImportTable(string,PagedTableState&lt;ImportRowPreview&gt;,Func&lt;IReadOnlyList&lt;ImportRowPreview&gt;&gt;)</code><br>73–90 | ApplyPagedResult @75; ToArray @75; Take @75; Skip @75; rows @75; BindRefresh @76; Localize @82; ToString @83; LocalizeImportAction @85; LocalizeTable @87; Max @88; Ceiling @88 | No extracted literal effects. |
| <span id="m-85af36c6dc44"></span><code>MainViewModel.LocalizeImportAction(string)</code><br>91–97 | Localize @93; StartsWith @96 | No extracted literal effects. |
| <span id="m-d17d533504d3"></span><code>MainViewModel.RefreshImportLocalization()</code><br>98–105 | RaisePropertyChanged @100; nameof @100; ApplyPagedResult @104; ToArray @104 | No extracted literal effects. |
| <span id="m-58392d80041f"></span><code>MainViewModel.SetImportReviewRows(bool,IReadOnlyList&lt;ImportRowPreview&gt;)</code><br>106–112 | ApplyPagedResult @111; ToArray @111; Take @111 | No extracted literal effects. |
| <span id="m-b0757883924b"></span><code>MainViewModel.ResetImportReviewRows(bool)</code><br>114–122 | SetImportReviewRows @117; Empty(ImportRowPreview) @117; ClearSelection @119 | No extracted literal effects. |
| <span id="m-24dd68498ca8"></span><code>MainViewModel.ResetInventoryImport()</code><br>124–136 | Clear @131; RaisePropertyChanged @134; nameof @134; ResetImportReviewRows @135 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Search.cs</code> · 874 lines.

SHA-256: <code>848b24ea8771a05896be36f13f18e530f1580cbf9e70d42ba2a209365c9f3579</code>.

Declarations: <code>MainViewModel</code> (line 15), <code>DelegatingSearchSuggestionReader : ISearchSuggestionReader</code> (line 849), <code>DelegatingSearchUsageWriter : ISearchUsageWriter</code> (line 862).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b0189613797b"></span><code>MainViewModel.ConfigureSearchPorts(ISearchSuggestionReader,ISearchUsageWriter?,IOperationalLogger?)</code><br>29–36 | nameof @31; Increment @34; InvalidateAllSearchScopes @35 | No extracted literal effects. |
| <span id="m-4baa396d90bb"></span><code>MainViewModel.GetRealWorkspaceIdentity()</code><br>734–739 | — | No extracted literal effects. |
| <span id="m-9d53b7263f48"></span><code>MainViewModel.CreateSearchState(SearchContext,Func&lt;object?&gt;?,Action&lt;SearchOption?&gt;?,Action&lt;string, SearchEntityKey?&gt;?,Func&lt;SearchContext&gt;?,AsyncSearchSelectionHandler?)</code><br>741–770 | Localize @760; GetRealWorkspaceIdentity @763; Add @768 | No extracted literal effects. |
| <span id="m-089acf32fd69"></span><code>MainViewModel.RecordSuccessfulSearchUseAsync(SearchContext,SearchEntityKey,string,CancellationToken)</code><br>772–818 | IsNullOrWhiteSpace @778; CanOpenSeparateConnection @783; LogFailure @791; ConfigureAwait @804; RecordUseAsync @804 | No extracted literal effects. |
| <span id="m-63da219daa71"></span><code>MainViewModel.InvalidateAllSearchScopes(bool)</code><br>820–830 | Invalidate @824; TriggerSearchAsync @827 | No extracted literal effects. |
| <span id="m-03ea0806fbac"></span><code>MainViewModel.ClearAllSearchStates()</code><br>832–838 | Clear @836 | No extracted literal effects. |
| <span id="m-85c3fe7d1e95"></span><code>MainViewModel.DisposeSearchStates()</code><br>840–847 | Dispose @844; Clear @846 | No extracted literal effects. |
| <span id="m-3559227d8c84"></span><code>DelegatingSearchSuggestionReader.GetSuggestionsAsync(SearchRequest,CancellationToken)</code><br>851–859 | readerSupplier @853; GetSuggestionsAsync @858 | InvalidOperationException @856 |
| <span id="m-e6f96a915849"></span><code>DelegatingSearchUsageWriter.RecordUseAsync(SearchUseRequest,CancellationToken)</code><br>864–872 | writerSupplier @866; RecordUseAsync @871 | InvalidOperationException @869 |

</details>

## MainViewModel.Tables.cs {#src-3f4385d56088}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Tables.cs</code> · 1,323 lines.

SHA-256: <code>4f6fbffa44581aab9769f21ce8b943b34e1513a770c7484798c5c82084fc6803</code>.

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
| <span id="m-2ce7e046cb91"></span><code>MainViewModel.RebuildSharedDataTableDefinitions()</code><br>504–892 | CreateColumns @511; TextColumn @512; Localize @515; ToString @519; LocalizeTable @522; Max @533; Ceiling @533; CreateLifecycleStatusHeader @581; LifecycleStatusFilterToolTip @587; OpenSelectedBatchOperation @604; OpenSelectedThirdPartyBatchOperation @665; OpenSelectedRegistryBatchOperation @794; FormatCanonicalUnitFactor @852; RaisePropertyChanged @881; nameof @881; BuildSalaryTables @890; BuildExpensesTable @891 | No extracted literal effects. |
| <span id="m-9805f03616e1"></span><code>MainViewModel.RefreshManagedCategoriesTable()</code><br>894–905 | ThenBy @899; OrderByDescending @899; OrderBy @899; ApplyLocalPage @904 | No extracted literal effects. |
| <span id="m-004f6f12b2f2"></span><code>MainViewModel.RefreshManagedUnitsTable()</code><br>907–921 | OrderByDescending @912; OrderBy @912; ThenBy @913; ParseCanonicalFactor @916; ApplyLocalPage @920 | No extracted literal effects. |
| <span id="m-bccb4200673f"></span><code>MainViewModel.ApplyLocalPage(IEnumerable&lt;T&gt;,PagedTableState&lt;T&gt;)</code><br>923–932 | ToArray @925; Max @926; Ceiling @926; ApplyPagedResult @929; ToArray @930; Take @930; Skip @930 | No extracted literal effects. |
| <span id="m-fc2f7e3396e3"></span><code>MainViewModel.ParseCanonicalFactor(string?)</code><br>934–935 | TryParse @935 | No extracted literal effects. |
| <span id="m-be011c50673e"></span><code>MainViewModel.FormatCanonicalUnitFactor(UomOption)</code><br>937–938 | IsNullOrWhiteSpace @938 | No extracted literal effects. |
| <span id="m-d6f93707234b"></span><code>MainViewModel.RefreshManagedExpenseCategoriesTable()</code><br>940–951 | OrderByDescending @945; OrderBy @945; ThenBy @946; ApplyLocalPage @950 | No extracted literal effects. |
| <span id="m-cfe1d2b30e7f"></span><code>MainViewModel.CreateManagedCategoryStatusCell(object)</code><br>953–957 | CreateStatusToggle @956; ToggleManagedCategoryActiveAsync @956 | No extracted literal effects. |
| <span id="m-5cddb0761c50"></span><code>MainViewModel.CreateManagedExpenseCategoryStatusCell(object)</code><br>959–963 | CreateStatusToggle @962; ToggleManagedExpenseCategoryActiveAsync @962 | No extracted literal effects. |
| <span id="m-80478c5c2f27"></span><code>MainViewModel.CreateManagedUnitStatusCell(object)</code><br>965–969 | CreateStatusToggle @968; ToggleManagedUnitActiveAsync @968 | No extracted literal effects. |
| <span id="m-d898172aec0a"></span><code>MainViewModel.CreateStatusToggle(bool,Func&lt;Task&gt;)</code><br>971–984 | toggle @982 | No extracted literal effects. |
| <span id="m-9d746ad318a1"></span><code>MainViewModel.CreateColumns(IReadOnlyList&lt;DataTableColumnDescriptor&gt;)</code><br>986–986 | — | No extracted literal effects. |
| <span id="m-b4cb2587d04d"></span><code>MainViewModel.TextColumn(string,string,Func&lt;object, string?&gt;,string?,double,double,DataTableCellStyle)</code><br>988–998 | — | No extracted literal effects. |
| <span id="m-c81ab828276c"></span><code>MainViewModel.LocalizeTable(string)</code><br>1000–1000 | Localize @1000 | No extracted literal effects. |
| <span id="m-9b0c8d114586"></span><code>MainViewModel.SelectionHeaderToolTip(bool)</code><br>1002–1003 | Localize @1002 | No extracted literal effects. |
| <span id="m-0040e4c4cf63"></span><code>MainViewModel.LifecycleStatusFilterToolTip(LifecycleStatusScope)</code><br>1005–1010 | Localize @1005 | No extracted literal effects. |
| <span id="m-8a1f40965f33"></span><code>MainViewModel.CreateLifecycleStatusHeader(LifecycleStatusScope)</code><br>1012–1026 | Add @1022 | No extracted literal effects. |
| <span id="m-affc6cbe2dfc"></span><code>MainViewModel.CreateInventoryLifecycleStatusCell(object)</code><br>1028–1037 | — | No extracted literal effects. |
| <span id="m-684462e2a7e2"></span><code>MainViewModel.CreateInventoryProductCell(object)</code><br>1039–1060 | Add @1045 | No extracted literal effects. |
| <span id="m-ef65270e9c42"></span><code>MainViewModel.CreateInventoryStockCell(object)</code><br>1062–1069 | CreateInventoryTwoLineCell @1068 | No extracted literal effects. |
| <span id="m-1fdeb4c4e5bd"></span><code>MainViewModel.CreateInventoryPricingCell(object)</code><br>1071–1075 | CreateInventoryTwoLineCell @1074 | No extracted literal effects. |
| <span id="m-a3fc0f9027e0"></span><code>MainViewModel.CreateInventoryTwoLineCell(string,string,DataTableCellStyle,DataTableCellStyle)</code><br>1077–1095 | Add @1080; InventoryCellStyleClass @1085 | No extracted literal effects. |
| <span id="m-294b75d44d0b"></span><code>MainViewModel.InventoryCellStyleClass(DataTableCellStyle)</code><br>1097–1107 | — | No extracted literal effects. |
| <span id="m-b122b63a4fff"></span><code>MainViewModel.CreateThirdPartyStatusCell(object)</code><br>1109–1133 | Contains @1126; HasPermission @1127; SetTip @1130; RequestThirdPartyStatusChange @1131 | No extracted literal effects. |
| <span id="m-c17e2dc50d67"></span><code>MainViewModel.CreatePricingItemPriceCell(object)</code><br>1135–1212 | HasPermission @1149; nameof @1155; Cancel @1174; SaveQuickItemPriceAsync @1177; ContinueWith @1188; Delay @1188; DispatchToUi @1192; CommitChange @1192 | No extracted literal effects. |
| <span id="m-6cfe2f2b1121"></span><code>MainViewModel.CreatePricingItemMethodCell(object)</code><br>1214–1248 | FirstOrDefault @1220; Equals @1220; HasPermission @1227; nameof @1233; SaveQuickItemPricingMethodAsync @1244 | No extracted literal effects. |
| <span id="m-bbc0fe876769"></span><code>MainViewModel.CreateThirdPartyPriceLevelCell(object)</code><br>1250–1271 | FirstOrDefault @1256; Equals @1256; HasPermission @1261; SaveThirdPartyPriceLevelAsync @1268 | No extracted literal effects. |
| <span id="m-6b7bb5e63ede"></span><code>MainViewModel.LocalizeInventoryStatus(string)</code><br>1273–1281 | Localize @1275 | No extracted literal effects. |
| <span id="m-6a0555b89de3"></span><code>MainViewModel.WorkspaceScopePrefix()</code><br>1283–1283 | Join @1283 | No extracted literal effects. |
| <span id="m-d5580a525e2e"></span><code>MainViewModel.NotifySelectionScopeChange(bool)</code><br>1285–1289 | Localize @1288 | No extracted literal effects. |
| <span id="m-b358d3e43a33"></span><code>MainViewModel.InventorySelectionScope()</code><br>1291–1292 | Join @1291; WorkspaceScopePrefix @1291; Trim @1291; ToString @1292 | No extracted literal effects. |
| <span id="m-35b0bd3b27e2"></span><code>MainViewModel.ThirdPartySelectionScope()</code><br>1294–1295 | Join @1294; WorkspaceScopePrefix @1294; Trim @1294; ToString @1295 | No extracted literal effects. |
| <span id="m-3a2be4b4be60"></span><code>MainViewModel.CreateInventoryToolbarButton(string,System.Windows.Input.ICommand,bool,string?)</code><br>1297–1311 | IsNullOrEmpty @1307; Add @1308 | No extracted literal effects. |
| <span id="m-bba1a90690bd"></span><code>MainViewModel.RefreshSharedDataTableDefinitions()</code><br>1313–1319 | RebuildSharedDataTableDefinitions @1315; BuildSalaryTables @1316; BuildExpensesTable @1317; BuildTeamsTable @1318 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdParties.cs</code> · 4,938 lines.

SHA-256: <code>5a53687c96b5bbb039bd5b07573d0ba2a9360d72724ea7ff42a9529f6e1134ae</code>.

Declarations: <code>MainViewModel</code> (line 32), <code>ThirdPartyFormSnapshot</code> (line 160), <code>ItemTierPricingRow : ReactiveObject</code> (line 4713), <code>PricingRoundingOption</code> (line 4865), <code>PricingIncrementOption</code> (line 4866), <code>PricingMethodOption</code> (line 4867), <code>PricingCostBasisOption</code> (line 4868), <code>CategoryPricingPreviewProduct</code> (line 4869), <code>TierWeightModeOption</code> (line 4873), <code>PriceOfferRow</code> (line 4875), <code>PendingShelfLabelRow : ReactiveObject</code> (line 4896), <code>KitPriceAlertRow</code> (line 4918).

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
| <span id="m-502bf9c5f982"></span><code>MainViewModel.Localize(string,object?[])</code><br>3585–3585 | Localize @3585 | No extracted literal effects. |
| <span id="m-c3077b399c30"></span><code>MainViewModel.RaiseLocalizedLabels()</code><br>3591–4340 | RaisePropertyChanged @3593; nameof @3593; RefreshManufacturingLocalization @4091; RefreshTraceabilityLocalization @4092; RefreshCommercialLocalization @4093; RefreshImportLocalization @4094 | No extracted literal effects. |
| <span id="m-e8923764b8e5"></span><code>MainViewModel.RefreshThirdPartyList()</code><br>4345–4352 | Clear @4347; Add @4350 | No extracted literal effects. |
| <span id="m-01dce47f62a5"></span><code>MainViewModel.NullIfBlank(string?)</code><br>4354–4354 | IsNullOrWhiteSpace @4354; Trim @4354 | No extracted literal effects. |
| <span id="m-4a133fcad37d"></span><code>MainViewModel.ParsePercent(string?)</code><br>4356–4357 | TryParse @4357 | No extracted literal effects. |
| <span id="m-8a92469e9cc6"></span><code>MainViewModel.ParseStoredPricingPercentForDisplay(string?,int)</code><br>4359–4360 | ParseStoredPercentage @4360 | No extracted literal effects. |
| <span id="m-d5e34a3c03ad"></span><code>MainViewModel.IsIncrementRoundingRule(string?)</code><br>4362–4364 | Equals @4363 | No extracted literal effects. |
| <span id="m-7ef5ad4c0887"></span><code>MainViewModel.ParseDate(string?)</code><br>4366–4367 | TryParse @4367 | No extracted literal effects. |
| <span id="m-333f9a2a6764"></span><code>MainViewModel.OpenNewPriceOffer()</code><br>4465–4475 | ToString @4469; ToString @4470; AddDays @4470; FirstOrDefault @4472 | No extracted literal effects. |
| <span id="m-dd048e867e73"></span><code>MainViewModel.OpenEditPriceOfferAsync(PriceOfferRow)</code><br>4477–4500 | CreateCommand @4480; CreateParameter @4483; ToString @4483; Add @4483; ConfigureAwait @4484; ExecuteReaderAsync @4484; ReadAsync @4484; Parse @4485; GetString @4485; GetInt32 @4485; IsDBNull @4487; TryParse @4487; ToString @4487; ToUniversalTime @4487; ToString @4487; ToUniversalTime @4488; AddDays @4488; FirstOrDefault @4490; TryParse @4492; FirstOrDefault @4493; Pow @4496; GetInt64 @4497 | FROM price_offers @4480; JOIN items @4480 |
| <span id="m-9e53cb0d3201"></span><code>MainViewModel.SavePriceOfferAsync()</code><br>4502–4519 | CheckSessionUnlocked @4504; TryParse @4505; ToString @4505; Round @4505; Pow @4505; IsNullOrWhiteSpace @4506; ConfigureAwait(SavePriceOfferCommand, Guid) @4515; ExecuteAsync(SavePriceOfferCommand, Guid) @4515; ReportError @4516; DispatchToUi @4517; ConfigureAwait @4518; LoadPriceOffersAsync @4518 | No extracted literal effects. |
| <span id="m-6c04f2124bb0"></span><code>MainViewModel.TogglePriceOfferAsync(PriceOfferRow)</code><br>4521–4529 | CheckSessionUnlocked @4523; ConfigureAwait(SetPriceOfferStatusCommand, bool) @4525; ExecuteAsync(SetPriceOfferStatusCommand, bool) @4525; ReportError @4527; ConfigureAwait @4528; LoadPriceOffersAsync @4528 | No extracted literal effects. |
| <span id="m-67f63f670515"></span><code>MainViewModel.LoadPriceOffersAsync()</code><br>4531–4570 | CreateCommand @4536; ConfigureAwait @4546; ExecuteReaderAsync @4546; ReadAsync @4547; Add @4549; Parse @4550; GetString @4550; GetDouble @4554; GetInt64 @4557; IsDBNull @4558; GetInt32 @4560; DispatchToUi @4563; Clear @4565; Add @4566 | FROM price_offers @4537; JOIN items @4537; JOIN product_categories @4537 |
| <span id="m-0450a1327bb8"></span><code>MainViewModel.LoadPendingShelfLabelsAsync()</code><br>4572–4611 | CreateCommand @4577; ConfigureAwait @4586; ExecuteReaderAsync @4586; ReadAsync @4587; Add @4589; Parse @4590; GetString @4590; GetInt64 @4594; GetInt32 @4599; Add @4600; Remove @4600; RaisePropertyChanged @4600; nameof @4600; Localize @4601; DispatchToUi @4604; Clear @4606; Add @4607 | FROM pending_shelf_labels @4578; JOIN items @4578 |
| <span id="m-0e62841512c6"></span><code>MainViewModel.LoadKitPriceReviewAlertsAsync()</code><br>4613–4652 | CreateCommand @4618; ConfigureAwait @4630; ExecuteReaderAsync @4630; ReadAsync @4631; Add @4633; Parse @4634; GetString @4634; GetInt64 @4638; GetInt32 @4642; DispatchToUi @4645; Clear @4647; Add @4648 | FROM kit_price_review_alerts @4619; JOIN items @4619 |
| <span id="m-6794f53e9aa5"></span><code>MainViewModel.SetKitPriceAlertStatusAsync(KitPriceAlertRow,string,string)</code><br>4654–4662 | CheckSessionUnlocked @4656; ConfigureAwait(ResolveKitPriceAlertCommand, bool) @4657; ExecuteAsync(ResolveKitPriceAlertCommand, bool) @4657; ReportError @4659; ConfigureAwait @4661; LoadKitPriceReviewAlertsAsync @4661 | No extracted literal effects. |
| <span id="m-a86dff198435"></span><code>MainViewModel.MarkShelfLabelsPrintedAsync()</code><br>4664–4667 | ConfigureAwait @4666; SetSelectedShelfLabelStatusAsync @4666 | No extracted literal effects. |
| <span id="m-2ad24c7b52c2"></span><code>MainViewModel.QueueSelectedShelfLabelsAsync()</code><br>4669–4681 | CheckSessionUnlocked @4671; ToArray @4672; Select @4672; Where @4672; Contains @4672; ConfigureAwait(QueueShelfLabelPrintCommand, string) @4675; ExecuteAsync(QueueShelfLabelPrintCommand, string) @4675; ReportError @4677; Clear @4678; RaisePropertyChanged @4678; nameof @4678; ConfigureAwait @4680; LoadPendingShelfLabelsAsync @4680 | No extracted literal effects. |
| <span id="m-ac51d65d2e5a"></span><code>MainViewModel.SetSelectedShelfLabelStatusAsync(string)</code><br>4683–4697 | CheckSessionUnlocked @4685; ToArray @4686; Select @4686; Where @4686; Contains @4686; ConfigureAwait(SetShelfLabelStatusCommand, int) @4689; ExecuteAsync(SetShelfLabelStatusCommand, int) @4689; Trim @4690; ReportError @4692; Clear @4693; RaisePropertyChanged @4694; nameof @4694; ConfigureAwait @4696; LoadPendingShelfLabelsAsync @4696 | No extracted literal effects. |
| <span id="m-b485f8118286"></span><code>MainViewModel.AddSqlParam(DbCommand,string,object)</code><br>4703–4709 | CreateParameter @4705; Add @4708 | No extracted literal effects. |
| <span id="m-cc76b177cf1d"></span><code>ItemTierPricingRow.RecalculateEffectivePrice()</code><br>4841–4862 | Max @4846; TryParse @4855 | No extracted literal effects. |

</details>

## MainViewModel.ThirdPartyImport.cs {#src-63148b75a5e2}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdPartyImport.cs</code> · 266 lines.

SHA-256: <code>7c801d831c615ee4b5e5bf042c7fb7f0724afedee16f78978c398a3ae4cdbaf8</code>.

Declarations: <code>MainViewModel</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (5)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-1f14c7360e7b"></span><code>MainViewModel.OpenThirdPartyImport()</code><br>116–130 | CheckSessionUnlocked @118; Increment @125; ResetThirdPartyImport @127; Invoke @129 | No extracted literal effects. |
| <span id="m-9fb52a37592b"></span><code>MainViewModel.PreviewThirdPartyImportFileAsync(string)</code><br>132–188 | Increment @135; ResetThirdPartyImport @139; IsNullOrWhiteSpace @142; Exists @142; ConfigureAwait @155; ReadAllBytesAsync @155; ToHexStringLower @156; HashData @156; ReadThirdPartiesAsync @157; ValidateThirdPartiesAsync @164; TemplateContextAsync @165; CompletedWorkbook @166; DispatchToUi @167; ReferenceEquals @169; SetImportReviewRows @170; ToArray @170; Select @170; Clear @174; Add @175; Clear @176; Add @177; RaisePropertyChanged @178; nameof @178; Localize @179; SafeError @185 | No extracted literal effects. |
| <span id="m-4e3fd7b60eb2"></span><code>MainViewModel.ConfirmThirdPartyImportAsync()</code><br>190–241 | ConfigureAwait(ImportThirdPartiesCommand, ImportThirdPartiesResult) @209; ExecuteAsync(ImportThirdPartiesCommand, ImportThirdPartiesResult) @209; ReportError @216; DispatchToUi @217; Localize @222; ResetThirdPartyImport @228; Invoke @230; ConfigureAwait @232; LoadThirdPartiesAsync @232; LoadThirdPartiesLegacyListsAsync @233; ReportException @237 | No extracted literal effects. |
| <span id="m-1f9d175704be"></span><code>MainViewModel.CancelThirdPartyImport()</code><br>243–249 | ResetThirdPartyImport @248 | No extracted literal effects. |
| <span id="m-2497bbbae0c1"></span><code>MainViewModel.ResetThirdPartyImport()</code><br>251–263 | Clear @259; Clear @260; ResetImportReviewRows @261; RaisePropertyChanged @262; nameof @262 | No extracted literal effects. |

</details>

## MainViewModel.cs {#src-16497b924a99}

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 13,030 lines.

SHA-256: <code>d89d72855cdd7ab59eff3ede2a8a70f2e9a1576597f5f227d68b9755f168a60b</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 8657).

<details markdown>
<summary>Methods, calls, table effects and failures (254)</summary>

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
| <span id="m-fd888f29fcf7"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3586–3594 | IsNullOrWhiteSpace @3588 | No extracted literal effects. |
| <span id="m-e218d27a15d8"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3596–3607 | Load @3598; IsNullOrWhiteSpace @3602; Resolve @3604; Apply @3606 | No extracted literal effects. |
| <span id="m-1cda6e82a85a"></span><code>MainViewModel.OpenImport()</code><br>3636–3644 | CheckSessionUnlocked @3638; Increment @3640; ResetInventoryImport @3641; Invoke @3643 | No extracted literal effects. |
| <span id="m-2c940385c3ae"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3646–3698 | Increment @3649; ResetInventoryImport @3654; IsNullOrWhiteSpace @3658; Exists @3658; ConfigureAwait @3672; ReadAllBytesAsync @3672; ToHexString @3673; HashData @3673; TemplateContextAsync @3677; Run @3678; Read @3678; ValidateInventoryAsync @3679; CompletedWorkbook @3680; DispatchToUi @3681; ReferenceEquals @3683; Add @3684; Localize @3685; SetImportReviewRows @3688; RaisePropertyChanged @3689; nameof @3689; SafeError @3695 | No extracted literal effects. |
| <span id="m-4b0acfb39132"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3700–3756 | ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3727; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3727; Localize @3733; DispatchToUi @3734; ResetInventoryImport @3738; Invoke @3740; ConfigureAwait @3742; LoadInventoryAsync @3742; ReportError @3746; ReportException @3752 | No extracted literal effects. |
| <span id="m-c03168c4591b"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3768–3778 | Report @3770; DispatchToUi @3771; Insert @3773 | No extracted literal effects. |
| <span id="m-896bfaae754f"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3780–3784 | RaisePropertyChanged @3783; nameof @3783 | No extracted literal effects. |
| <span id="m-49e5d75db1c7"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3786–3789 | ReportError @3788 | No extracted literal effects. |
| <span id="m-9e09ac7d421c"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3795–3800 | ReportError @3798 | No extracted literal effects. |
| <span id="m-fc4d707a34f9"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3809–3815 | IsNullOrWhiteSpace @3811; Trim @3811; ReportError @3813 | No extracted literal effects. |
| <span id="m-4fb67843f4c1"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3817–3820 | DispatchToUi @3819; Insert @3819 | No extracted literal effects. |
| <span id="m-25a308cb0a81"></span><code>MainViewModel.DispatchToUi(Action)</code><br>3826–3840 | CheckAccess @3828; action @3830; GetResult @3838; GetAwaiter @3838; InvokeAsync @3838 | No extracted literal effects. |
| <span id="m-90da6c0ba719"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4500–4565 | Register @4502; Execute @4502; Execute @4503; Execute @4504; Execute @4505; Execute @4510; Execute @4511; Execute @4512; Execute @4513; Execute @4514; Execute @4515; Execute @4516; Execute @4517; Execute @4518; Execute @4519; Execute @4520; Execute @4521; Execute @4522; Execute @4523; Execute @4524; Execute @4525; Execute @4526; Execute @4527; Execute @4528; Execute @4529; Execute @4530; Execute @4531; Execute @4532; Execute @4533; Execute @4534; Execute @4535; Execute @4536; Execute @4537; Execute @4538; Execute @4539; Execute @4540; Execute @4541; Execute @4543; Execute @4544; RequestClosePersonForm @4545; KeepEditingPersonForm @4546; CloseSalaryMonthDetailModal @4547; CloseSalaryPaymentModal @4548; CloseSalaryAdjustmentModal @4549; CloseSalaryFinalizeModal @4550; RequestCloseExpenseForm @4551; KeepEditingExpenseForm @4552; CloseExpenseCategoryModal @4553; CloseExpensePaymentModal @4554; CloseExpenseDetailModal @4555; ClosePaymentReturnModal @4556; CloseWasteExpenseConfirmation @4557; InitializeSalaryTables @4562; InitializeExpensesTables @4563; InitializeTeamsCommands @4564 | No extracted literal effects. |
| <span id="m-a12e7f0cf709"></span><code>MainViewModel.CreateDemo()</code><br>4567–4574 | SetActiveCashier @4570; Parse @4570; RefreshUnlockCandidates @4572 | No extracted literal effects. |
| <span id="m-bcaccf35960d"></span><code>MainViewModel.CreateInitializing()</code><br>4576–4584 | — | No extracted literal effects. |
| <span id="m-3af74c617628"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4586–4596 | — | No extracted literal effects. |
| <span id="m-292c9e911e4a"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4598–4616 | ConfigureDiagnosticsWorkspace @4612; ResolveDiagnosticsWorkspace @4612; ApplyPersistedState @4613; RefreshUnlockCandidates @4614 | No extracted literal effects. |
| <span id="m-b3ec80a7ec14"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4618–4646 | CheckSessionUnlocked @4620; HasPermission @4621; Equals @4632; GetFileNameWithoutExtension @4632; GetEntryAssembly @4634; Add @4636; Start @4639; ReportException @4644 | No extracted literal effects. |
| <span id="m-35fa15415726"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4648–4671 | CheckSessionUnlocked @4650; HasPermission @4651; Equals @4661; GetFileNameWithoutExtension @4661; Add @4662; GetEntryAssembly @4662; Start @4664; ReportException @4669 | No extracted literal effects. |
| <span id="m-50e7b6565eb7"></span><code>MainViewModel.Dispose()</code><br>4673–4692 | Increment @4675; ResetFinancialWorkspace @4677; Dispose @4678; Stop @4679; CancelBatchPricingPreviewExpiry @4682; Dispose @4683; Dispose @4684; DisposeSearchStates @4690; SuppressFinalize @4691 | No extracted literal effects. |
| <span id="m-70b87bfd4881"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4694–4698 | Stop @4696 | No extracted literal effects. |
| <span id="m-45a8b6be2ba3"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4700–4738 | Clear @4710; Clear @4711; Clear @4712; Clear @4713; Clear @4714; Clear @4715; Clear @4716; Clear @4717; Clear @4718; Clear @4719 | No extracted literal effects. |
| <span id="m-1386ef2367b5"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4740–4843 | RaisePropertyChanged @4754; nameof @4754; Clear @4756; Clear @4757; Clear @4758; CreateCommand @4765; ExecuteReader @4767; Read @4768; TryParse @4770; GetString @4770; Add @4771; Add @4779; GroupBy @4780; Count @4782; Contains @4787; Add @4804; Add @4805; SetActiveCashier @4813; ToString @4817; ToString @4820; ToLocalTime @4820; NotifyTotalsChanged @4842 | FROM item_kits @4766 |
| <span id="m-2986336e84ae"></span><code>MainViewModel.InitializeDemoData()</code><br>4845–4925 | Add @4851; Add @4870; Add @4883; Add @4887; Add @4892; Add @4898; ApplyActivityFilter @4904; Add @4907; ApplyInventoryFilter @4916; Add @4919; Parse @4919; NotifyTotalsChanged @4924 | No extracted literal effects. |
| <span id="m-f7c358b77501"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>4927–4940 | — | No extracted literal effects. |
| <span id="m-7affd0c1a636"></span><code>MainViewModel.SelectMenu(string)</code><br>4942–5013 | CheckSessionUnlocked @4944; NormalizeMenuKey @4948; LoadInvoicesAsync @4954; LoadCommercialAsync @4955; LoadActivityInvoicesAsync @4962; LoadTeamsStaffAsync @4965; LoadCatalogRegistryAsync @4966; UpdateDemoSeedingAvailabilityAsync @4969; UpdateReceiptDesignPreview @4972; RefreshDiagnosticsAsync @4973; LoadPriceLevelSettingsAsync @4974; LoadInventoryAsync @4977; LoadPriceProposalsAsync @4979; LoadReportDataAsync @4982; LoadFinancialRegisterAsync @4983; LoadCustomersAsync @4986; LoadSuppliersAsync @4987; LoadThirdPartiesAsync @4988; LoadManufacturingDataAsync @4993; LoadManagedUnitsAsync @5001; LoadManagedCategoriesAsync @5004; LoadSalaryWorkspaceAsync @5007; LoadExpensesWorkspaceAsync @5010 | No extracted literal effects. |
| <span id="m-27ec9a51a721"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>5015–5034 | — | No extracted literal effects. |
| <span id="m-67dc6df6b297"></span><code>MainViewModel.LogOut()</code><br>5036–5057 | Clear @5038; RaisePropertyChanged @5041; nameof @5041; ClearNotifications @5043; ResetCashReview @5047; Lock @5050; RefreshUnlockCandidates @5055; UpdateDemoSeedingAvailabilityAsync @5056 | No extracted literal effects. |
| <span id="m-0d28d4a85846"></span><code>MainViewModel.UnlockSession()</code><br>5059–5062 | UnlockSession @5061 | No extracted literal effects. |
| <span id="m-30b4a61b0f2b"></span><code>MainViewModel.UnlockSession(string?)</code><br>5064–5163 | IsLockScreenLockedOut @5072; IsNullOrWhiteSpace @5088; AuthenticateSelectedUser @5097; Lock @5102; AddSeconds @5108; AddMinutes @5125; Initialize @5144; Unlock @5145; Any @5149; Equals @5149; RaisePropertyChanged @5150; nameof @5150; LoadActivityInvoicesAsync @5154; LoadTrackOrdersAsync @5155; UpdateDemoSeedingAvailabilityAsync @5156; StartAutomaticDemoDatasetLoadAsync @5157 | No extracted literal effects. |
| <span id="m-c27d5a07a486"></span><code>MainViewModel.PowerAction()</code><br>5165–5171 | CheckSessionUnlocked @5167 | No extracted literal effects. |
| <span id="m-8b430264294b"></span><code>MainViewModel.CycleTable()</code><br>5173–5179 | CheckSessionUnlocked @5175 | No extracted literal effects. |
| <span id="m-59ea7b419f3b"></span><code>MainViewModel.CycleDiningType()</code><br>5181–5187 | CheckSessionUnlocked @5183 | No extracted literal effects. |
| <span id="m-0ed3b611d650"></span><code>MainViewModel.CycleCustomer()</code><br>5189–5192 | OpenCustomerChooser @5191 | No extracted literal effects. |
| <span id="m-d1cbb30b8d4b"></span><code>MainViewModel.OpenPromoDialog()</code><br>5194–5209 | CheckSessionUnlocked @5196; IsNullOrWhiteSpace @5203; RaisePropertyChanged @5207; nameof @5207 | No extracted literal effects. |
| <span id="m-fda865cce6d2"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5211–5280 | CheckSessionUnlocked @5213; ToLowerInvariant @5226; Trim @5226; IsNullOrWhiteSpace @5233; Trim @5233; ToList @5241; Select @5241; ToMinorUnits @5245; Equals @5261; Calculate @5265; NotifyTotalsChanged @5277; ConfigureAwait @5279; SaveDurableCartAsync @5279 | No extracted literal effects. |
| <span id="m-0190eae23153"></span><code>MainViewModel.TogglePromo()</code><br>5282–5299 | CheckSessionUnlocked @5284; RemovePromo @5293; OpenPromoDialog @5297 | No extracted literal effects. |
| <span id="m-8cfc3393468e"></span><code>MainViewModel.RemovePromo()</code><br>5301–5311 | NotifyTotalsChanged @5308; SaveDurableCartAsync @5310 | No extracted literal effects. |
| <span id="m-e8556e3b5c90"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5313–5324 | CheckSessionUnlocked @5315; NotifyTotalsChanged @5321; ConfigureAwait @5323; SaveDurableCartAsync @5323 | No extracted literal effects. |
| <span id="m-796ce943f27f"></span><code>MainViewModel.CancelPromoDialog()</code><br>5326–5330 | — | No extracted literal effects. |
| <span id="m-e219d6fefa38"></span><code>MainViewModel.RecalculateCart()</code><br>5332–5386 | ToMinorUnits @5348; Add @5349; Equals @5370; Calculate @5374; ToDictionary @5377; TryGetValue @5380 | No extracted literal effects. |
| <span id="m-66db6cb8ae8c"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5388–5395 | CheckSessionUnlocked @5390; ResetCashReview @5391 | No extracted literal effects. |
| <span id="m-4ba398572cf0"></span><code>MainViewModel.SelectCategory(CategoryItem)</code><br>5397–5405 | CheckSessionUnlocked @5399; ApplyFilter @5403 | No extracted literal effects. |
| <span id="m-f52173ac4922"></span><code>MainViewModel.ApplyFilter()</code><br>5407–5429 | FirstOrDefault @5409; Clear @5412; AsEnumerable @5413; Where @5417; Equals @5417; IsNullOrWhiteSpace @5420; Contains @5422; Add @5427 | No extracted literal effects. |
| <span id="m-44805e7c8d90"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5431–5431 | AddToCart @5431 | No extracted literal effects. |
| <span id="m-0ac75d1aab71"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5433–5477 | CheckSessionUnlocked @5435; ResetCashReview @5436; ResolveProductSaleUnitFactor @5439; Round @5446; FirstOrDefault @5447; UpdateCartKitBreakdownAsync @5456; Add @5468; NotifyTotalsChanged @5471; SaveDurableCartAsync @5473; IsNullOrWhiteSpace @5475; ToString @5475; NewGuid @5475; RecordSuccessfulSearchUseAsync @5476; FromGuid @5476 | No extracted literal effects. |
| <span id="m-a8fe04230b76"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5479–5492 | CheckSessionUnlocked @5481; ResetCashReview @5482; UpdateCartKitBreakdownAsync @5489; NotifyTotalsChanged @5490; SaveDurableCartAsync @5491 | No extracted literal effects. |
| <span id="m-44bc51f178e3"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5494–5509 | CheckSessionUnlocked @5496; ResetCashReview @5497; UpdateCartKitBreakdownAsync @5501; Remove @5505; NotifyTotalsChanged @5507; SaveDurableCartAsync @5508 | No extracted literal effects. |
| <span id="m-543df1857952"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5511–5517 | ConfigureAwait @5514; LoadAsync @5514; RefreshSavedPaymentImages @5515; CancelManualPaymentSettings @5516 | No extracted literal effects. |
| <span id="m-af1898f19a26"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5519–5548 | ValidImage @5526; CreatePaymentBitmap @5531; Dispose @5534; RaisePropertyChanged @5546; nameof @5546 | No extracted literal effects. |
| <span id="m-425be3551c8e"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5550–5566 | Dispose @5560; CreatePaymentBitmap @5562; RaisePropertyChanged @5564; nameof @5564 | No extracted literal effects. |
| <span id="m-6525b3470a17"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5568–5572 | — | No extracted literal effects. |
| <span id="m-1fe459b4f853"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5574–5582 | Dispose @5576; CreatePaymentBitmap @5578; RaisePropertyChanged @5580; nameof @5580 | No extracted literal effects. |
| <span id="m-c9140859c1e5"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5584–5603 | ConfigureAwait @5593; ExecuteAsync @5593; DispatchToUi @5596; SafePipelineError @5596; LoadAsync @5599; RefreshSavedPaymentImages @5600; CancelManualPaymentSettings @5601 | No extracted literal effects. |
| <span id="m-3da51a459b7e"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5605–5624 | IsNullOrWhiteSpace @5609; Trim @5610; ToMinorUnits @5616; ConfigureAwait @5622; PlaceOrderAsync @5622 | No extracted literal effects. |
| <span id="m-46534660cabb"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5626–5638 | PlaceOrderInternalAsync @5632 | No extracted literal effects. |
| <span id="m-53d899c761a6"></span><code>MainViewModel.PlaceOrderInternalAsync()</code><br>5640–5841 | Localize @5644; ExecuteDemoPlaceOrder @5650; ConfigureAwait @5676; SaveDurableCartAsync @5676; ToMinorUnits @5684; Trim @5686; Equals @5697; Equals @5704; ResetCashReview @5706; Max @5764; Add @5769; ConfigureAwait(TakePaymentCommand, SalesInvoice) @5787; ExecuteAsync(TakePaymentCommand, SalesInvoice) @5787; Format @5799; ToDecimal @5799; DispatchToUi @5801; Clear @5805; NewGuid @5814; NotifyTotalsChanged @5815; LoadActivityInvoicesAsync @5822; OpenStaleCartPriceReviewAsync @5827; RequestElevationForCheckout @5829; SafePipelineError @5833; SafeError @5839 | No extracted literal effects. |
| <span id="m-16d6b944fa98"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>5843–5875 | DispatchToUi @5847; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5850; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5850; SafePipelineError @5855; ToArray @5859; Select @5859; Where @5859; FormatCartReviewMoney @5863; Clear @5870; Add @5871 | No extracted literal effects. |
| <span id="m-7f90dc485b96"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>5877–5882 | ScalingFactor @5879; Format @5881; Equals @5881 | No extracted literal effects. |
| <span id="m-03dc82deef88"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>5884–5915 | CheckSessionUnlocked @5886; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5888; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5888; DispatchToUi @5893; SafePipelineError @5893; ConfigureAwait @5894; OpenStaleCartPriceReviewAsync @5894; FirstOrDefault @5901; ScalingFactor @5904; ResetCashReview @5908; Clear @5911; NotifyTotalsChanged @5912 | No extracted literal effects. |
| <span id="m-1be87979e914"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>5917–5924 | Clear @5921; ResetCashReview @5922 | No extracted literal effects. |
| <span id="m-fbd0a9035c4c"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>5926–5952 | CheckSessionUnlocked @5928; ResetCashReview @5935; ToMinorUnits @5946; ConfigureAwait @5951; PlaceOrderAsync @5951 | No extracted literal effects. |
| <span id="m-a53cfde90e66"></span><code>MainViewModel.CancelCashReview()</code><br>5954–5958 | ResetCashReview @5956 | No extracted literal effects. |
| <span id="m-5ed391ea77e5"></span><code>MainViewModel.ResetCashReview()</code><br>5960–5969 | — | No extracted literal effects. |
| <span id="m-a9260b8fbb72"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>5971–5990 | RaisePropertyChanged @5982; nameof @5982; Clear @5985; ResetCashReview @5986; NotifyTotalsChanged @5987 | No extracted literal effects. |
| <span id="m-a3ed6c4fe197"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>5992–6057 | ConfigureAwait @5996; WaitAsync @5996; ClearActiveCartAsync @6001; ToMinorUnits @6011; Add @6012; ToUpperInvariant @6015; ToString @6015; IsNullOrWhiteSpace @6018; SaveActiveCartAsync @6031; DispatchToUi @6050; SafeError @6050; Release @6055 | No extracted literal effects. |
| <span id="m-8b9eb7b35607"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>6059–6114 | ConfigureAwait @6065; GetActiveCartAsync @6065; Clear @6077; FirstOrDefault @6080; ToDecimal @6084; Add @6090; NotifyTotalsChanged @6107 | No extracted literal effects. |
| <span id="m-57280ba2fd04"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>6116–6193 | ApplyPagedResult @6120; ToList @6121; ApplyActivityFilter @6125; HasPermission @6130; ConfigureAwait @6137; GetPagedActivityInvoicesAsync @6137; ToPageRequest @6140; ToDecimal @6146; Add @6147; ToString @6152; ToLocalTime @6152; DispatchToUi @6171; Clear @6173; Add @6176; SafeError @6190 | No extracted literal effects. |
| <span id="m-d662164c31b0"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>6195–6272 | HasPermission @6200; ConfigureAwait @6207; GetActiveOrdersAsync @6207; Clear @6208; ToDecimal @6212; Join @6246; Select @6246; Add @6248; ToString @6263; ToLocalTime @6263 | No extracted literal effects. |
| <span id="m-af909711848c"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6274–6301 | CheckSessionUnlocked @6276; Clear @6279; ConfigureAwait @6285; GetOrderByIdAsync @6285; Add @6290; DispatchToUi @6296; SafeError @6296 | No extracted literal effects. |
| <span id="m-fd84a5320271"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6303–6308 | Clear @6307 | No extracted literal effects. |
| <span id="m-e3ecce3df511"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6310–6343 | CheckSessionUnlocked @6312; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6328; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6328; ConfigureAwait @6337; LoadTrackOrdersAsync @6337; DispatchToUi @6341; SafePipelineError @6341 | No extracted literal effects. |
| <span id="m-a39d0545647a"></span><code>MainViewModel.MarkReadyAsync()</code><br>6345–6378 | CheckSessionUnlocked @6347; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6363; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6363; ConfigureAwait @6372; LoadTrackOrdersAsync @6372; DispatchToUi @6376; SafePipelineError @6376 | No extracted literal effects. |
| <span id="m-1ae4632ae639"></span><code>MainViewModel.MarkServedAsync()</code><br>6380–6413 | CheckSessionUnlocked @6382; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6398; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6398; ConfigureAwait @6407; LoadTrackOrdersAsync @6407; DispatchToUi @6411; SafePipelineError @6411 | No extracted literal effects. |
| <span id="m-ae131e6e639c"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6415–6443 | CheckSessionUnlocked @6417; Remove @6421; CloseOrderDetailsModal @6422; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6431; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6431; ConfigureAwait @6437; LoadTrackOrdersAsync @6437; DispatchToUi @6441; SafePipelineError @6441 | No extracted literal effects. |
| <span id="m-c15854583364"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6445–6541 | CheckSessionUnlocked @6447; CloseOrderDetailsModal @6453; ConfigureAwait @6460; GetOrderByIdAsync @6460; Zero @6482; NewGuid @6488; ToList @6491; Select @6491; ToUpperInvariant @6494; ToString @6494; SaveActiveCartAsync @6503; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6519; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6519; DispatchToUi @6522; SafePipelineError @6522; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6528; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6528; LoadTrackOrdersAsync @6534; LoadActivityInvoicesAsync @6535 | No extracted literal effects. |
| <span id="m-d622123187dd"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6543–6550 | CheckSessionUnlocked @6545 | No extracted literal effects. |
| <span id="m-8e0c40a8372e"></span><code>MainViewModel.FilterActivity(string)</code><br>6569–6575 | CheckSessionUnlocked @6571; ApplyActivityFilter @6573 | No extracted literal effects. |
| <span id="m-27b988882d57"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6577–6616 | Clear @6579; AsEnumerable @6580; Where @6585; IsNullOrWhiteSpace @6588; Trim @6590; Contains @6592; Contains @6593; Contains @6594; IsNullOrEmpty @6598; Equals @6600; ToList @6604; Add @6606; ApplyPagedResult @6610 | No extracted literal effects. |
| <span id="m-1a360b6f9396"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6618–6654 | CheckSessionUnlocked @6620; ConfigureAwait(QueueReceiptReprintCommand, string) @6640; ExecuteAsync(QueueReceiptReprintCommand, string) @6640; IsNullOrWhiteSpace @6641; ReportError @6643; RefreshOutputStatusAsync @6648; DispatchToUi @6652; SafeError @6652 | No extracted literal effects. |
| <span id="m-f3a0ccabedcf"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6656–6699 | RefreshOutputPrinterQueues @6661; ReadAsync @6662; Equals @6669; IsNullOrWhiteSpace @6669; TryReadGeometry @6671; ComputeCapabilityFingerprint @6675; ConfigureAwait @6679; InvalidateThermalVerificationAsync @6679; LoadCashFinancialSettingsAsync @6691; LoadReceiptDesignAsync @6692; RefreshOutputStatusAsync @6693; DispatchToUi @6697; SafeError @6697 | No extracted literal effects. |
| <span id="m-fa3c078ea346"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6701–6727 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6714; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6714; ReportError @6717; LoadOutputDevicesAsync @6720; DispatchToUi @6725; SafeError @6725 | No extracted literal effects. |
| <span id="m-4d57d53c288b"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6729–6802 | Equals @6743; IsNullOrWhiteSpace @6748; IsWindows @6753; TryReadGeometry @6758; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6775; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6775; ReportError @6778; Render @6781; ToString @6782; ConfigureAwait @6783; Run @6783; Send @6783; ComputeCapabilityFingerprint @6784; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @6785; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @6785; RefreshOutputStatusAsync @6796; DispatchToUi @6800; SafeError @6800 | No extracted literal effects. |
| <span id="m-f8d2a36bbbe9"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>6804–6841 | IsWindows @6818; IsNullOrWhiteSpace @6818; TryReadGeometry @6820; ComputeCapabilityFingerprint @6824; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @6825; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @6825; ReportError @6829; ConfigureAwait @6835; RefreshOutputStatusAsync @6835; DispatchToUi @6839; SafeError @6839 | InvalidOperationException @6819; InvalidOperationException @6823 |
| <span id="m-a27408e40c4c"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>6843–6880 | CreateCommand @6848; ConfigureAwait @6857; ExecuteReaderAsync @6857; ReadAsync @6858; GetInt32 @6861; GetString @6861; GetInt64 @6861; Parse @6862; RaisePropertyChanged @6864; nameof @6864; NotifyTotalsChanged @6873; DispatchToUi @6878; SafeError @6878 | FROM store_config @6849 |
| <span id="m-38e2e289872c"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>6882–6910 | ConfigureAwait @6895; ExecuteAsync @6895; ReportError @6898; NotifyTotalsChanged @6903; DispatchToUi @6908; SafeError @6908 | No extracted literal effects. |
| <span id="m-a95764e16f8c"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>6912–6956 | DispatchToUi @6916; CreateCommand @6921; ConfigureAwait @6927; ExecuteReaderAsync @6927; ReadAsync @6928; Deserialize(ReceiptDesignDocument) @6930; GetString @6930; SafeError @6949 | FROM receipt_designs @6922; JOIN receipt_design_versions @6922 |
| <span id="m-6b687fa883e3"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>6958–6985 | ConfigureAwait @6971; ExecuteAsync @6971; ReportError @6976; DispatchToUi @6983; SafeError @6983 | No extracted literal effects. |
| <span id="m-9a8a13bd6752"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>6987–6999 | IsWindows @6989; Select @6990; Enumerate @6990; Empty(string) @6991; ToArray @6992; OrderBy @6992; Distinct @6992; Where @6992; Append @6992; IsNullOrWhiteSpace @6993; Clear @6997; Add @6998 | No extracted literal effects. |
| <span id="m-0e1a31708aa9"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>7001–7059 | CheckAccess @7003; DispatchToUi @7005; CreateSampleData @7011; Equals @7017; IsWindows @7024; TryReadGeometry @7025; BuildPaperDocument @7034; RenderPreviewPngPages @7037; SetReceiptDesignPreviewPages @7039; Localize @7041; BuildThermalLines @7046; RenderPreviewPng @7048; Empty(byte[]) @7055; ReportException @7057 | No extracted literal effects. |
| <span id="m-aa6aeb97418c"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>7061–7066 | ShowReceiptDesignPreviewPage @7065 | No extracted literal effects. |
| <span id="m-ce769fd0578a"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>7068–7074 | ShowReceiptDesignPreviewPage @7073 | No extracted literal effects. |
| <span id="m-46c78938718d"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>7076–7090 | RaisePropertyChanged @7087; nameof @7087 | No extracted literal effects. |
| <span id="m-960351cc3260"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>7092–7121 | ReadAsync @7095; Localize @7098; CreateCommand @7100; ConfigureAwait @7102; ExecuteScalarAsync @7102; ToString @7102; IsNullOrWhiteSpace @7103; ExecuteReaderAsync @7117; ReadAsync @7118; Trim @7119; GetString @7119 | FROM hardware_jobs @7101; FROM hardware_jobs @7116 |
| <span id="m-6e0607d8f532"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>7123–7139 | Clear @7125; AsEnumerable @7126; Where @7129; IsNullOrWhiteSpace @7131; Contains @7133; Contains @7134; Contains @7135; Add @7138 | No extracted literal effects. |
| <span id="m-fb0eedca2e87"></span><code>MainViewModel.GenerateXReport()</code><br>7141–7160 | CheckSessionUnlocked @7143; ToString @7147; GenerateXReportInternalAsync @7159 | No extracted literal effects. |
| <span id="m-f61f24a4012f"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>7162–7177 | ConfigureAwait @7166; LoadReportDataAsync @7166; DispatchToUi @7175; SafeError @7175 | No extracted literal effects. |
| <span id="m-dfd06ba72cad"></span><code>MainViewModel.CloseShiftZReport()</code><br>7179–7182 | OpenCloseShiftModal @7181 | No extracted literal effects. |
| <span id="m-1d0462e6ad6e"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>7184–7193 | CheckSessionUnlocked @7191 | No extracted literal effects. |
| <span id="m-8ddfe954b569"></span><code>MainViewModel.SaveSettings()</code><br>7195–7199 | CheckSessionUnlocked @7197 | No extracted literal effects. |
| <span id="m-9fcffbd82547"></span><code>MainViewModel.ApplySettingsAsync()</code><br>7201–7288 | CheckSessionUnlocked @7210; NotifyTotalsChanged @7229; ExecuteAsync @7257; DispatchToUi @7281; SafePipelineError @7281; SafeError @7286 | No extracted literal effects. |
| <span id="m-f4458dad518a"></span><code>MainViewModel.CancelSettings()</code><br>7290–7311 | CheckSessionUnlocked @7292; NotifyTotalsChanged @7304 | No extracted literal effects. |
| <span id="m-19d97a5c027c"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7314–7344 | ProbeDatabaseAsync @7327; ProbeLicense @7333; RefreshOutputStatusAsync @7336; ProbeHardwareStubs @7337; DispatchToUi @7342; SafeError @7342 | No extracted literal effects. |
| <span id="m-762976e4c81f"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7405–7443 | RaisePropertyChanged @7407; nameof @7407; FormatRealResetPreviewSummary @7442 | No extracted literal effects. |
| <span id="m-7353e547581f"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7445–7458 | Localize @7446; ToString @7448; GetValueOrDefault @7448; ToString @7453; ToString @7454; ToString @7455 | No extracted literal effects. |
| <span id="m-50396dd8611c"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7567–7659 | Post @7571; ConfigureAwait @7578; GetWorkspaceEnvironmentAsync @7578; Equals @7579; GetDatasetStateAsync @7581; CreateCommand @7587; CreateParameter @7594; ToString @7596; Add @7597; ExecuteScalarAsync @7598; HasPermission @7603; ToInt64 @7608; ExecuteScalarAsync @7608; ExecuteScalarAsync @7612; ExecuteScalarAsync @7619; ExecuteScalarAsync @7625; Localize @7644 | FROM items @7607; FROM sales_invoices @7611; FROM third_parties @7624; FROM users @7588; JOIN user_roles @7588 · DYNAMIC SQL: inspect manually |
| <span id="m-9707b455e269"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>7661–7671 | CheckSessionUnlocked @7663; HasPermission @7664 | No extracted literal effects. |
| <span id="m-581d516dc836"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>7673–7678 | ConfigureAwait @7677; ResetDatabaseAsync @7677 | No extracted literal effects. |
| <span id="m-a4fe494cfc13"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>7680–7681 | ConfigureAwait @7681; EnsureDefaultDemoDatasetAsync @7681 | No extracted literal effects. |
| <span id="m-d665a5795c86"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>7683–7689 | EnsureDefaultDemoDatasetAsync @7687 | No extracted literal effects. |
| <span id="m-32ae1aeb3798"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>7691–7795 | Localize @7696; ConfigureAwait @7703; WaitAsync @7703; GetWorkspaceEnvironmentAsync @7706; Equals @7707; HasPermission @7714; Post @7728; LocalizeDemoSeedProgress @7730; EnsureInitialDatasetAsync @7736; Join @7760; Select @7760; ReloadCatalogAsync @7770; LoadInventoryAsync @7771; LoadThirdPartiesAsync @7772; LoadManufacturingDataAsync @7773; LoadSuppliersAsync @7774; UpdateDemoSeedingAvailabilityAsync @7775; ToUpperInvariant @7780; ToString @7780; NewGuid @7780; LogDiagnosticError @7781; ReportError @7786; Release @7793 | No extracted literal effects. |
| <span id="m-cfa813675cae"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>7797–7811 | Localize @7799 | No extracted literal effects. |
| <span id="m-c5bf99ee5baf"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>7813–7910 | Localize @7817; ConfigureAwait @7821; WaitAsync @7821; HasPermission @7825; GetWorkspaceEnvironmentAsync @7832; Equals @7833; ResetDatabaseAsync @7841; GetStoreProfileAsync @7844; Post @7845; Clear @7848; Clear @7849; Clear @7850; NewGuid @7851; RaisePropertyChanged @7854; nameof @7854; Lock @7855; Defaults @7868; RefreshUnlockCandidates @7881; LoadCashFinancialSettingsAsync @7882; LoadOutputDevicesAsync @7883; LoadManualPaymentSettingsAsync @7884; LoadReceiptDesignAsync @7885; ReloadCatalogAsync @7886; LoadInventoryAsync @7887; LoadThirdPartiesAsync @7888; LoadManufacturingDataAsync @7889; LoadActivityInvoicesAsync @7890; UpdateDemoSeedingAvailabilityAsync @7891; ToUpperInvariant @7896; ToString @7896; LogDiagnosticError @7897; ReportError @7903; Release @7908 | No extracted literal effects. |
| <span id="m-59af15347925"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>7912–7954 | CheckSessionUnlocked @7914; HasPermission @7916; ConfigureAwait @7924; GetWorkspaceEnvironmentAsync @7924; Equals @7925; PreviewAsync @7928; FormatRealResetPreviewSummary @7929; Post @7930; RaisePropertyChanged @7947; nameof @7947; SafeError @7952 | UnauthorizedAccessException @7926 |
| <span id="m-930eab522770"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>7956–8042 | HasPermission @7959; ConfigureAwait @7977; ExecuteAsync @7977; GetStoreProfileAsync @7986; Post @7989; Clear @7993; Clear @7994; Clear @7995; Clear @7996; NewGuid @7997; Lock @8000; RaisePropertyChanged @8014; nameof @8014; LoadCashFinancialSettingsAsync @8015; LoadOutputDevicesAsync @8016; LoadManualPaymentSettingsAsync @8017; LoadReceiptDesignAsync @8018; RefreshUnlockCandidates @8026; LoadInventoryAsync @8027; LoadActivityInvoicesAsync @8028; UpdateDemoSeedingAvailabilityAsync @8029; ToUpperInvariant @8034; ToString @8034; LogDiagnosticError @8035 | No extracted literal effects. |
| <span id="m-72795af12493"></span><code>MainViewModel.CancelRealShopReset()</code><br>8044–8051 | RaisePropertyChanged @8050; nameof @8050 | No extracted literal effects. |
| <span id="m-b672c9528034"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>8055–8072 | ConfigureAwait @8057; ExportDocumentAsync @8057; Post @8061; GetFileName @8065 | No extracted literal effects. |
| <span id="m-a67ce7e07df0"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>8074–8096 | Exists @8079; CreateDirectory @8081; Start @8083; ToUpperInvariant @8092; ToString @8092; NewGuid @8092; LogDiagnosticError @8093 | No extracted literal effects. |
| <span id="m-cc16b2334624"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>8098–8108 | CheckSessionUnlocked @8100; RaisePropertyChanged @8102; nameof @8102; Localize @8104; ToString @8105 | No extracted literal effects. |
| <span id="m-3ea587666c75"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>8115–8131 | CheckSessionUnlocked @8117; HasPermission @8118; RaisePropertyChanged @8124; nameof @8124; Localize @8127; ToString @8128 | No extracted literal effects. |
| <span id="m-913213c8828d"></span><code>MainViewModel.CommitNumpad()</code><br>8133–8210 | CheckSessionUnlocked @8135; ResetCashReview @8136; TryParse @8142; IsNullOrWhiteSpace @8144; Trim @8150; NotifyTotalsChanged @8160; SaveDurableCartAsync @8161; Min @8167; ToMinorUnits @8169; Round @8170; TryParse @8185; UpdateCartKitBreakdownAsync @8193; Remove @8199; RaisePropertyChanged @8208; nameof @8208 | No extracted literal effects. |
| <span id="m-7b021fdc8a05"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>8216–8234 | CheckSessionUnlocked @8224 | No extracted literal effects. |
| <span id="m-048368c28658"></span><code>MainViewModel.StageBusinessProfile()</code><br>8241–8271 | CheckSessionUnlocked @8243; HasPermission @8247 | No extracted literal effects. |
| <span id="m-bf7828153aeb"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8273–8282 | — | No extracted literal effects. |
| <span id="m-74886005c9b2"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8284–8307 | RecalculateCart @8286; RaisePropertyChanged @8288; nameof @8288 | No extracted literal effects. |
| <span id="m-b223ebec6099"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8309–8396 | IsNullOrWhiteSpace @8312; Trim @8312; All @8322; Trim @8339; Trim @8340; NewGuid @8344; ToString @8349; ConfigureAwait @8353; BeginTransactionAsync @8353; HandleAsync @8354; AppendAsync @8359; ToString @8360; Serialize @8365; CommitAsync @8368; Initialize @8374; Unlock @8375; RaisePropertyChanged @8380; nameof @8380; LoadTeamsStaffAsync @8383; StartAutomaticDemoDatasetLoadAsync @8384; RollbackAsync @8388; DispatchToUi @8389; SafePipelineError @8389; SafeError @8394 | No extracted literal effects. |
| <span id="m-9104a5d8a903"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8398–8405 | IsNullOrWhiteSpace @8400; ConfigureAwait @8404; SaveTeamMemberAsync @8404 | No extracted literal effects. |
| <span id="m-e072b53f465b"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8407–8425 | CheckSessionUnlocked @8410; HasPermission @8412 | No extracted literal effects. |
| <span id="m-4443685441ad"></span><code>MainViewModel.CancelChangePin()</code><br>8427–8434 | — | No extracted literal effects. |
| <span id="m-d77146c8ec6e"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8436–8512 | Trim @8444; IsNullOrWhiteSpace @8447; All @8453; Equals @8466; Equals @8467; SetQuickPin @8479; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8492; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8492; ConfigureAwait @8500; LoadTeamsStaffAsync @8500; DispatchToUi @8505; SafePipelineError @8505; SafeError @8510 | No extracted literal effects. |
| <span id="m-e647d996bc2d"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8514–8588 | HasPermission @8520; ConfigureAwait @8529; ResolveEffectivePermissionsAsync @8529; Contains @8562; Contains @8563; Add @8565; Contains @8571; DispatchToUi @8577; Clear @8579; Add @8580; SafeError @8586 | No extracted literal effects. |
| <span id="m-efa8d4fc8897"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8590–8632 | OnTeamMemberFieldChanged @8596; ConfigureAwait @8613; ExecuteAsync @8613; DispatchToUi @8617; SafePipelineError @8625; SafeError @8630 | No extracted literal effects. |
| <span id="m-48a1ed325bd3"></span><code>MainViewModel.ClosePermissionEditor()</code><br>8634–8639 | — | No extracted literal effects. |
| <span id="m-107b22c97139"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>8641–8655 | — | No extracted literal effects. |
| <span id="m-26ef681d3568"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>8659–8659 | — | No extracted literal effects. |
| <span id="m-73c1378151bd"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>8660–8660 | — | No extracted literal effects. |
| <span id="m-f50d9d26530c"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>8661–8661 | FromResult @8661 | No extracted literal effects. |
| <span id="m-6908c7e936c3"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>8664–8749 | HasPermission @8673; FromDecimal @8688; ConfigureAwait(OpenShiftCommand, Shift) @8692; ExecuteAsync(OpenShiftCommand, Shift) @8692; SetActiveCashier @8707; RefreshUnlockCandidates @8708; ToUpperInvariant @8725; ToString @8725; ToString @8727; ConfigureAwait @8737; LoadTeamsStaffAsync @8737; LoadTrackOrdersAsync @8738; DispatchToUi @8742; SafePipelineError @8742; SafeError @8747 | No extracted literal effects. |
| <span id="m-df081c219556"></span><code>MainViewModel.LoadInventoryAsync()</code><br>8751–8905 | ApplyPagedResult @8755; ToList @8756; ApplyInventoryFilter @8760; Clear @8768; Empty(InventoryItem) @8770; ConfigureAwait @8775; GetPagedInventoryItemsAsync @8775; ToPageRequest @8780; CreateCommand @8793; ExecuteReaderAsync @8795; ReadAsync @8796; Add @8798; Parse @8798; GetString @8798; ExecuteReaderAsync @8808; ReadAsync @8809; TryParse @8811; GetString @8811; IsDBNull @8811; Add @8822; TryGetValue @8824; Contains @8832; ToDecimal @8835; Localize @8843; ToLocalTime @8849; BuildCostSourcesTooltip @8851; DispatchToUi @8878; Add @8881; SafeError @8903 | FROM item_kits @8794; FROM item_pricing @8807 |
| <span id="m-44a41aacf0be"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>8907–8963 | CheckSessionUnlocked @8909; FirstOrDefault @8910; Clear @8921; Add @8923; CreateCommand @8928; CreateParameter @8939; Add @8942; ExecuteReader @8943; Read @8944; GetString @8946; Contains @8947; FirstOrDefault @8959; ResetReceiveLines @8960; UpdateReceiveKitBreakdownAsync @8961 | FROM uoms @8929; JOIN uoms @8929 |
| <span id="m-37367487914d"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>8965–9066 | IsNullOrWhiteSpace @8978; Localize @8995; HasPermission @8999; BuildReceiptLines @9005; Sum @9022; Trim @9032; ToMinorUnits @9037; ConfigureAwait(ReceiveStockCommand, StockMovement) @9042; ExecuteAsync(ReceiveStockCommand, StockMovement) @9042; Clear @9052; ConfigureAwait @9054; LoadInventoryAsync @9054; LoadItemHistoryAsync @9055; DispatchToUi @9059; SafePipelineError @9059; SafeError @9064 | No extracted literal effects. |
| <span id="m-d2ae06114999"></span><code>MainViewModel.ResetReceiveLines()</code><br>9072–9089 | Clear @9074; Add @9078; RaisePropertyChanged @9084; nameof @9084; Invoke @9087 | No extracted literal effects. |
| <span id="m-3dfa5f4532e3"></span><code>MainViewModel.AddReceiveLine()</code><br>9092–9115 | IsNullOrWhiteSpace @9099; Add @9105; RaisePropertyChanged @9110; nameof @9110; Invoke @9113 | No extracted literal effects. |
| <span id="m-619d931d0939"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>9118–9135 | Remove @9125; Add @9128; RaisePropertyChanged @9134; nameof @9134 | No extracted literal effects. |
| <span id="m-b9ca92350e60"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>9141–9162 | IsNullOrWhiteSpace @9143; LastOrDefault @9148; Add @9152; Trim @9155; ReferenceEquals @9156; RaisePropertyChanged @9160; nameof @9160; Invoke @9161 | No extracted literal effects. |
| <span id="m-756d4733437f"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>9165–9242 | Add @9177; IsNullOrWhiteSpace @9185; Trim @9189; FirstOrDefault @9198; GroupBy @9198; Count @9200; Trim @9227 | No extracted literal effects. |
| <span id="m-67f3a0848a8d"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>9244–9280 | CreateCommand @9249; ConfigureAwait @9256; ExecuteReaderAsync @9256; Clear @9257; ReadAsync @9258; Add @9260; ParseGuidSafe @9261; GetString @9261; IsDBNull @9265; GetInt32 @9269; Parse @9271; DispatchToUi @9278; SafeError @9278 | FROM third_parties @9250 |
| <span id="m-115a9605851c"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9282–9300 | CheckSessionUnlocked @9284; FirstOrDefault @9290 | No extracted literal effects. |
| <span id="m-d64b5b084dc8"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9302–9393 | IsNullOrWhiteSpace @9325; HasPermission @9336; Trim @9354; Trim @9356; ConfigureAwait(AdjustStockCommand, StockMovement) @9360; ExecuteAsync(AdjustStockCommand, StockMovement) @9360; ConfigureAwait @9376; LoadInventoryAsync @9376; LoadItemHistoryAsync @9377; OpenWasteExpenseConfirmation @9381; DispatchToUi @9386; SafePipelineError @9386; SafeError @9391 | No extracted literal effects. |
| <span id="m-55631fd6d912"></span><code>MainViewModel.OpenAddProduct()</code><br>9395–9463 | ResetProductStockDraft @9397; CheckSessionUnlocked @9398; HasPermission @9399; RaisePropertyChanged @9407; nameof @9407; ClearItemHistory @9409; LoadCatalogRegistryAsync @9416; InitializeProductPricingDraft @9419; Clear @9434; Clear @9435; Where @9436; Add @9438; FirstOrDefault @9440; Clear @9451; CaptureProductModalBaselineAsync @9462 | No extracted literal effects. |
| <span id="m-8b6cf4389347"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9465–9465 | OpenEditProduct @9465 | No extracted literal effects. |
| <span id="m-71c6e9aaa628"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9467–9547 | ResetProductStockDraft @9469; CheckSessionUnlocked @9471; HasPermission @9472; RaisePropertyChanged @9480; nameof @9480; ClearItemHistory @9482; LoadCatalogRegistryAsync @9490; InitializeProductPricingDraft @9496; ToMinorUnits @9497; LoadExactProductCostSnapshotsAsync @9503; ToDecimal @9507; Clear @9514; Clear @9515; Where @9516; Add @9518; FirstOrDefault @9520; LoadItemLocationEligibilitiesAsync @9539; LoadProductKitAsync @9540; LoadPrimaryBarcodeAsync @9541; LoadProductPricingDraftAsync @9542; LoadItemHistoryAsync @9543; LoadItemPriceHistoryAsync @9544; CaptureProductModalBaselineAsync @9546 | No extracted literal effects. |
| <span id="m-a4f35bbdb180"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>9549–9562 | OrderBy @9552; Where @9552; Add @9554 | No extracted literal effects. |
| <span id="m-5d81ed8aef94"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>9564–9637 | CreateCommand @9571; CreateParameter @9578; ToString @9580; Add @9581; ConfigureAwait @9582; ExecuteReaderAsync @9582; ReadAsync @9583; GetInt32 @9585; IsDBNull @9586; GetString @9586; ParseStoredPricingPercentForDisplay @9587; ToDisplayAmount @9591; GetInt64 @9591; OrderBy @9611; Where @9611; TryGetValue @9614; Add @9620; InvokeAsync @9622; RaisePropertyChanged @9627; nameof @9627; CaptureProductPricingSnapshot @9630; DispatchToUi @9635; SafeError @9635 | FROM item_price_levels @9602; FROM item_pricing @9573 |
| <span id="m-260b4ecea17b"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>9639–9674 | CreateCommand @9646; CreateParameter @9652; ToString @9654; Add @9655; ConfigureAwait @9656; ExecuteReaderAsync @9656; ReadAsync @9657; Parse @9660; GetString @9660; GetInt32 @9660; GetInt64 @9661; IsDBNull @9661; Parse @9662; InvokeAsync @9664; DispatchToUi @9672; SafeError @9672 | FROM product_category_pricing_rules @9647 |
| <span id="m-f3c09219f160"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>9676–9705 | ConfigureAwait @9680; WhenAll @9680; InvokeAsync @9681; CaptureProductModalSnapshot @9685; CaptureProductPricingSnapshot @9686; RaisePropertyChanged @9687; nameof @9687 | No extracted literal effects. |
| <span id="m-bdac05d9c368"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>9707–9755 | Serialize @9707; ToArray @9730; Select @9730; Select @9747; OrderBy @9747; OrderBy @9751 | No extracted literal effects. |
| <span id="m-d2049ed5c39e"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>9757–9769 | Serialize @9757; ToArray @9768; Select @9768 | No extracted literal effects. |
| <span id="m-9bdcc803af9b"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9771–9803 | nameof @9773; RaisePropertyChanged @9774; RaiseTraceabilityState @9779; StartsWith @9783; RecomputeProductPricingPreview @9794; RefreshVirtualKitAvailability @9796 | No extracted literal effects. |
| <span id="m-c5dc623be940"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>9805–9819 | RaisePropertyChanged @9813; nameof @9813; RecomputeProductPricingPreview @9816; RefreshVirtualKitAvailability @9817 | No extracted literal effects. |
| <span id="m-8b25c76b348a"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9821–9829 | RaisePropertyChanged @9823; nameof @9823; RecomputeProductPricingPreview @9826; RefreshVirtualKitAvailability @9827 | No extracted literal effects. |
| <span id="m-a6f9caa00065"></span><code>MainViewModel.RequestCloseProductModal()</code><br>9831–9844 | DiscardProductModal @9843 | No extracted literal effects. |
| <span id="m-682a2af312ae"></span><code>MainViewModel.DiscardProductModal()</code><br>9846–9855 | RaisePropertyChanged @9851; nameof @9851; ClearItemHistory @9853 | No extracted literal effects. |
| <span id="m-63feeff1eaca"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>9857–9875 | CreateCommand @9862; CreateParameter @9864; ToString @9866; Add @9867; ConfigureAwait @9868; ExecuteScalarAsync @9868; DispatchToUi @9871; ToString @9871 | FROM barcodes @9863 |
| <span id="m-2a50ff761dab"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>9877–9928 | CreateCommand @9882; CreateParameter @9889; ToString @9891; Add @9892; ConfigureAwait @9896; ExecuteReaderAsync @9896; ReadAsync @9897; IsDBNull @9900; GetString @9900; GetDouble @9901; ResolveQuantity @9902; Add @9903; Parse @9905; DispatchToUi @9913; Clear @9916; Add @9917; RaisePropertyChanged @9920; nameof @9920; RecomputeProductPricingPreview @9923; RefreshVirtualKitAvailability @9924 | FROM item_kits @9883; JOIN item_kit_components @9883; JOIN items @9883 |
| <span id="m-20842e859fa8"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>9930–9930 | SaveProductConfigurationAsync @9930 | No extracted literal effects. |
| <span id="m-cbda432a3c0e"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>9932–10137 | ConfigureAwait @9937; LoadCatalogRegistryAsync @9937; HasPermission @9939; IsNullOrWhiteSpace @9944; Localize @9966; Equals @9976; ToMinorUnits @10021; GetValueOrDefault @10033; Trim @10034; Trim @10035; Trim @10036; Trim @10043; Trim @10045; ToList @10090; Select @10090; CaptureProductPricingSnapshot @10094; ToCommand @10096; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @10104; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @10104; DispatchToUi @10107; RaiseTraceabilityState @10113; CaptureProductModalSnapshot @10115; RaisePropertyChanged @10117; nameof @10117; ReloadCatalogAsync @10124; LoadInventoryAsync @10125; LoadItemHistoryAsync @10126; SafePipelineError @10130; SafeError @10135 | No extracted literal effects. |
| <span id="m-8624cea29e97"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>10139–10175 | CheckSessionUnlocked @10141; HasPermission @10142; ConfigureAwait(DeactivateProductCommand, bool) @10158; ExecuteAsync(DeactivateProductCommand, bool) @10158; ConfigureAwait @10163; ReloadCatalogAsync @10163; LoadInventoryAsync @10164; DispatchToUi @10168; SafePipelineError @10168; SafeError @10173 | No extracted literal effects. |
| <span id="m-042f22f0f636"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>10177–10236 | ConfigureAwait @10183; GetActiveItemsAsync @10183; Clear @10185; Clear @10186; Clear @10187; CreateCommand @10192; ExecuteReaderAsync @10194; ReadAsync @10195; TryParse @10197; GetString @10197; Add @10198; Add @10205; GroupBy @10206; Count @10208; Contains @10213; Add @10226; Add @10227; ApplyFilter @10230 | FROM item_kits @10193 |
| <span id="m-aecd704ea059"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>10238–10244 | IsNullOrWhiteSpace @10240; TryParse @10241; HashData @10242; GetBytes @10242; AsSpan @10243 | No extracted literal effects. |
| <span id="m-0e8193594c26"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>10246–10312 | CreateCommand @10252; ConfigureAwait @10255; ExecuteReaderAsync @10255; ReadAsync @10257; Add @10259; GetString @10261; GetInt32 @10265; Clear @10271; Add @10272; ExecuteReaderAsync @10284; ReadAsync @10286; Add @10288; GetString @10290; IsDBNull @10294; GetInt32 @10298; Clear @10304; Add @10305; DispatchToUi @10310; SafeError @10310 | FROM bins @10277; FROM facilities @10254; JOIN facilities @10277 |
| <span id="m-6a151a44e458"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>10527–10631 | CreateCommand @10537; ConfigureAwait @10544; ExecuteReaderAsync @10544; ReadAsync @10545; Add @10547; ParseGuidSafe @10549; GetString @10549; IsDBNull @10552; GetInt32 @10553; Add @10573; DispatchToUi @10588; Clear @10590; Clear @10591; Clear @10592; Equals @10596; Add @10597; Add @10599; Add @10601; Clear @10603; Add @10604; FirstOrDefault @10607; Equals @10607; FirstOrDefault @10612; FirstOrDefault @10619; ApplySaleUnitDefaultsToCatalog @10624; SafeError @10629 | FROM product_categories @10539; FROM uoms @10565 |
| <span id="m-4720e2bc2611"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>10633–10647 | ResolveProductSaleUnitFactor @10637; Round @10643; ApplyFilter @10646 | No extracted literal effects. |
| <span id="m-db088eb12f24"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>10649–10667 | FirstOrDefault @10651; Equals @10652; TryParse @10659 | No extracted literal effects. |
| <span id="m-f547dfc4fa1b"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>10669–10691 | CheckSessionUnlocked @10671; HasPermission @10672; ConfigureAwait @10687; LoadManagedCategoriesAsync @10687; CaptureCategoryFormSnapshot @10689; RaisePropertyChanged @10690; nameof @10690 | No extracted literal effects. |
| <span id="m-6edba70b0baa"></span><code>MainViewModel.CloseCategoryManager()</code><br>10693–10702 | — | No extracted literal effects. |
| <span id="m-6e8ad03b2a45"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>10704–10726 | CheckSessionUnlocked @10706; HasPermission @10707; ConfigureAwait @10722; LoadManagedUnitsAsync @10722; CaptureUnitFormSnapshot @10724; RaisePropertyChanged @10725; nameof @10725 | No extracted literal effects. |
| <span id="m-d2fcd5aa418e"></span><code>MainViewModel.CloseUnitManager()</code><br>10728–10737 | — | No extracted literal effects. |
| <span id="m-9336cd4990e5"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>10739–10802 | Clear @10742; Clear @10743; Clear @10744; CreateCommand @10745; ConfigureAwait @10751; ExecuteReaderAsync @10751; ReadAsync @10752; Add @10754; ParseGuidSafe @10756; GetString @10756; IsDBNull @10759; GetInt32 @10760; Where @10768; Equals @10768; Add @10769; TryParse @10782; Add @10783; RefreshTargetedCategoryCollections @10796; DispatchToUi @10797; RefreshManagedCategoriesTable @10799; RefreshManagedExpenseCategoriesTable @10800 | FROM expense_categories @10773; FROM product_categories @10747; JOIN expense_records @10773 |
| <span id="m-7f9a61eaa34b"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>10804–10811 | OpenCategoryManagerAsync @10806; FirstOrDefault @10807; EditManagedCategory @10810 | No extracted literal effects. |
| <span id="m-798867a63b84"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>10813–10821 | OpenCategoryManagerAsync @10816; FirstOrDefault @10817; EditManagedExpenseCategory @10820 | No extracted literal effects. |
| <span id="m-f348bb53a379"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>10823–10842 | DispatchToUi @10825; Clear @10827; Clear @10828; Clear @10829; Where @10831; Equals @10834; Add @10835; Add @10837; Add @10839 | No extracted literal effects. |
| <span id="m-bae16835ca6f"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>10844–10856 | CaptureCategoryFormSnapshot @10854; RaisePropertyChanged @10855; nameof @10855 | No extracted literal effects. |
| <span id="m-0b954b9c212a"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>10858–10871 | CaptureCategoryFormSnapshot @10869; RaisePropertyChanged @10870; nameof @10870 | No extracted literal effects. |
| <span id="m-21bc72fae2fa"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>10873–10883 | Serialize @10873 | No extracted literal effects. |
| <span id="m-c78c96dfa90d"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>10885–10895 | Serialize @10885 | No extracted literal effects. |
| <span id="m-d36f8d515f5e"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>10897–10897 | — | No extracted literal effects. |
| <span id="m-b561ded545ef"></span><code>MainViewModel.DiscardRegistryForm()</code><br>10899–10915 | Equals @10902; RaisePropertyChanged @10906; nameof @10906 | No extracted literal effects. |
| <span id="m-9812d0dc4a8d"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>10917–11044 | Equals @10928; HasPermission @10930; FirstOrDefault @10939; Trim @10944; Trim @10945; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @10947; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @10947; DispatchToUi @10950; SafePipelineError @10950; IsNullOrWhiteSpace @10958; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @10960; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @10960; ConfigureAwait @10969; LoadManagedCategoriesAsync @10969; LoadExpenseCategoriesAsync @10970; CaptureCategoryFormSnapshot @10980; RaisePropertyChanged @10981; nameof @10981; Trim @10999; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @11001; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @11001; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @11017; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @11017; LoadCatalogRegistryAsync @11026; ReloadCatalogAsync @11027; SafeError @11042 | No extracted literal effects. |
| <span id="m-d859fd629172"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>11046–11091 | HasPermission @11056; ConfigureAwait(DeactivateCategoryCommand, bool) @11069; ExecuteAsync(DeactivateCategoryCommand, bool) @11069; ConfigureAwait(ReactivateCategoryCommand, bool) @11074; ExecuteAsync(ReactivateCategoryCommand, bool) @11074; DispatchToUi @11079; SafePipelineError @11079; ConfigureAwait @11083; LoadManagedCategoriesAsync @11083; LoadCatalogRegistryAsync @11084; ReloadCatalogAsync @11085; SafeError @11089 | No extracted literal effects. |
| <span id="m-ba5dd6609058"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>11093–11133 | HasPermission @11103; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11119; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11119; DispatchToUi @11122; SafePipelineError @11122; ConfigureAwait @11126; LoadManagedCategoriesAsync @11126; LoadExpenseCategoriesAsync @11127; SafeError @11131 | No extracted literal effects. |
| <span id="m-189e987a8b91"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>11135–11235 | Clear @11138; CreateCommand @11141; ConfigureAwait @11147; ExecuteReaderAsync @11147; ReadAsync @11148; Add @11150; GetString @11152; IsDBNull @11154; GetInt32 @11158; IsNullOrWhiteSpace @11169; Equals @11173; Add @11180; Clear @11184; ExecuteReaderAsync @11189; ReadAsync @11190; GetString @11192; Where @11214; Add @11216; TryGetValue @11219; FirstOrDefault @11226; Add @11230; DispatchToUi @11233; UpdateConversionPreview @11234 | FROM store_uom_preferences @11188; FROM uoms @11143 |
| <span id="m-f7c83a234bcb"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>11237–11244 | OpenUnitManagerAsync @11239; FirstOrDefault @11240; Equals @11240; EditManagedUnit @11243 | No extracted literal effects. |
| <span id="m-bb69b94dd222"></span><code>MainViewModel.UpdateConversionPreview()</code><br>11246–11282 | IsNullOrWhiteSpace @11248; FirstOrDefault @11254; Equals @11254; TryParse @11269 | No extracted literal effects. |
| <span id="m-5f9d45500404"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11284–11305 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11291; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11291; DispatchToUi @11294; SafePipelineError @11298; SafeError @11303 | No extracted literal effects. |
| <span id="m-b43a1770f714"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11307–11320 | IsNullOrWhiteSpace @11313; TryParse @11316; CaptureUnitFormSnapshot @11318; RaisePropertyChanged @11319; nameof @11319 | No extracted literal effects. |
| <span id="m-cd6411ebb4c4"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>11322–11384 | IsNullOrWhiteSpace @11334; Trim @11338; Trim @11339; Trim @11342; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @11343; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @11343; DispatchToUi @11346; SafePipelineError @11346; Trim @11353; Equals @11356; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @11361; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @11361; ConfigureAwait @11369; LoadManagedUnitsAsync @11369; LoadCatalogRegistryAsync @11370; CaptureUnitFormSnapshot @11377; RaisePropertyChanged @11378; nameof @11378; SafeError @11382 | No extracted literal effects. |
| <span id="m-cc324d2f659e"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>11386–11424 | ConfigureAwait(DeactivateUomCommand, bool) @11403; ExecuteAsync(DeactivateUomCommand, bool) @11403; ConfigureAwait(ReactivateUomCommand, bool) @11408; ExecuteAsync(ReactivateUomCommand, bool) @11408; DispatchToUi @11413; SafePipelineError @11413; ConfigureAwait @11417; LoadManagedUnitsAsync @11417; LoadCatalogRegistryAsync @11418; SafeError @11422 | No extracted literal effects. |
| <span id="m-111606e060ff"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>11426–11464 | CreateCommand @11431; CreateParameter @11438; ToString @11440; Add @11441; ConfigureAwait @11443; ExecuteReaderAsync @11443; Clear @11444; ReadAsync @11445; Add @11447; ParseGuidSafe @11449; GetString @11449; GetInt32 @11452; IsDBNull @11454; ToDecimal @11454; GetDouble @11454; DispatchToUi @11462; SafeError @11462 | FROM item_locations @11432 |
| <span id="m-4d2fea58d49d"></span><code>MainViewModel.OpenLocationsModal()</code><br>11467–11493 | CheckSessionUnlocked @11469; HasPermission @11470; LoadFacilitiesAndBinsAsync @11491 | No extracted literal effects. |
| <span id="m-4e59d51d407b"></span><code>MainViewModel.OpenAddFacility()</code><br>11495–11503 | — | No extracted literal effects. |
| <span id="m-c06dcb857251"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>11505–11514 | — | No extracted literal effects. |
| <span id="m-12b4c99d4f06"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>11516–11575 | HasPermission @11519; IsNullOrWhiteSpace @11524; IsNullOrEmpty @11540; Trim @11542; Trim @11542; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @11543; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @11543; OpenAddFacility @11547; ConfigureAwait @11548; LoadFacilitiesAndBinsAsync @11548; DispatchToUi @11552; SafePipelineError @11552; ConfigureAwait(CreateFacilityCommand, FacilityDto) @11558; ExecuteAsync(CreateFacilityCommand, FacilityDto) @11558; SafeError @11573 | No extracted literal effects. |
| <span id="m-88bf9ee02c45"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>11577–11608 | HasPermission @11580; ConfigureAwait(DeactivateFacilityCommand, bool) @11592; ExecuteAsync(DeactivateFacilityCommand, bool) @11592; OpenAddFacility @11596; ConfigureAwait @11597; LoadFacilitiesAndBinsAsync @11597; DispatchToUi @11601; SafePipelineError @11601; SafeError @11606 | No extracted literal effects. |
| <span id="m-5835df567e73"></span><code>MainViewModel.OpenAddBin()</code><br>11610–11621 | FirstOrDefault @11620 | No extracted literal effects. |
| <span id="m-3b71c95bfb6e"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>11623–11635 | FirstOrDefault @11633 | No extracted literal effects. |
| <span id="m-b894c7dca13b"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>11637–11712 | HasPermission @11640; IsNullOrWhiteSpace @11650; IsNullOrEmpty @11661; Trim @11666; Trim @11667; Trim @11668; Trim @11669; Trim @11670; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @11673; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @11673; OpenAddBin @11677; ConfigureAwait @11678; LoadFacilitiesAndBinsAsync @11678; DispatchToUi @11682; SafePipelineError @11682; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @11695; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @11695; SafeError @11710 | No extracted literal effects. |
| <span id="m-37dc11c0b8ec"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>11714–11745 | HasPermission @11717; ConfigureAwait(DeactivateLocationBinCommand, bool) @11729; ExecuteAsync(DeactivateLocationBinCommand, bool) @11729; OpenAddBin @11733; ConfigureAwait @11734; LoadFacilitiesAndBinsAsync @11734; DispatchToUi @11738; SafePipelineError @11738; SafeError @11743 | No extracted literal effects. |
| <span id="m-3bf78276d852"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>11747–11800 | HasPermission @11755; IsNullOrWhiteSpace @11760; Trim @11772; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @11780; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @11780; ConfigureAwait @11788; LoadItemLocationEligibilitiesAsync @11788; DispatchToUi @11793; SafePipelineError @11793; SafeError @11798 | No extracted literal effects. |
| <span id="m-8a9a7d91d559"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>11802–11832 | HasPermission @11805; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @11817; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @11817; ConfigureAwait @11820; LoadItemLocationEligibilitiesAsync @11820; DispatchToUi @11825; SafePipelineError @11825; SafeError @11830 | No extracted literal effects. |
| <span id="m-dace6df8e65c"></span><code>MainViewModel.LoadCustomersAsync()</code><br>11835–11868 | NewGuid @11843; Clear @11849; Add @11850; FilterCustomers @11852; ConfigureAwait @11859; GetCustomersAsync @11859; DispatchToUi @11866; SafeError @11866 | No extracted literal effects. |
| <span id="m-c47903903755"></span><code>MainViewModel.FilterCustomers()</code><br>11870–11883 | Clear @11872; Trim @11873; IsNullOrWhiteSpace @11874; Where @11876; Contains @11876; Contains @11877; Contains @11878; Add @11881 | No extracted literal effects. |
| <span id="m-1b02bf50dbd3"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>11885–11921 | CheckSessionUnlocked @11887; CreateCommand @11896; CreateParameter @11899; ToString @11901; Add @11902; ConfigureAwait @11903; ExecuteScalarAsync @11903; ToString @11904; Equals @11907; LoadPickerCandidatesAsync @11919; DispatchToUi @11920 | FROM items @11898 |
| <span id="m-7165df543aff"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>11923–11984 | ConfigureAwait @11930; GetLotCandidatesAsync @11930; DispatchToUi @11933; Clear @11935; Add @11938; ToString @11947; GetSerialCandidatesAsync @11955; Clear @11960; Add @11963; ToString @11972 | No extracted literal effects. |
| <span id="m-31d730f9f96a"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>11986–11992 | Clear @11989; Clear @11990 | No extracted literal effects. |
| <span id="m-bfe18ab7a40a"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>11994–12053 | FirstOrDefault @12007; ConfigureAwait(SelectLotForCartLineCommand, bool) @12015; ExecuteAsync(SelectLotForCartLineCommand, bool) @12015; DispatchToUi @12018; SafePipelineError @12018; ToList @12024; Where @12024; ConfigureAwait(SelectSerialForCartLineCommand, bool) @12034; ExecuteAsync(SelectSerialForCartLineCommand, bool) @12034; SafeError @12051 | No extracted literal effects. |
| <span id="m-8cf3b1ef8708"></span><code>MainViewModel.OpenCustomerChooser()</code><br>12055–12063 | CheckSessionUnlocked @12057; Clear @12060; LoadCustomersAsync @12061 | No extracted literal effects. |
| <span id="m-d7c085b5d1db"></span><code>MainViewModel.CloseCustomerChooser()</code><br>12065–12068 | — | No extracted literal effects. |
| <span id="m-1c8f323a9720"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>12070–12087 | SaveDurableCartAsync @12080; IsNullOrWhiteSpace @12084; ToString @12084; NewGuid @12084; RecordSuccessfulSearchUseAsync @12085; FromGuid @12085 | No extracted literal effects. |
| <span id="m-75c67116c6f4"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>12089–12098 | SaveDurableCartAsync @12097 | No extracted literal effects. |
| <span id="m-69925695fd71"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>12100–12145 | CheckSessionUnlocked @12102; IndexOf @12106; SelectWalkInCustomer @12112; FilterCustomers @12114; ConfigureAwait(DeactivateCustomerCommand, bool) @12126; ExecuteAsync(DeactivateCustomerCommand, bool) @12126; ConfigureAwait @12133; LoadCustomersAsync @12133; DispatchToUi @12138; SafePipelineError @12138; SafeError @12143 | No extracted literal effects. |
| <span id="m-f50986e16b23"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>12274–12313 | Add @12280; NewGuid @12281; RefreshManufacturingTablesAsync @12295; ConfigureAwait @12303; GetKitsAsync @12303; Clear @12304; Add @12305; DispatchToUi @12311; SafeError @12311 | No extracted literal effects. |
| <span id="m-254562ef0c4e"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12317–12333 | CheckSessionUnlocked @12319; SetProductionActionMode @12321; FirstOrDefault @12326; LoadProductionIngredientLotsAsync @12331; TakeProductionSnapshot @12332 | No extracted literal effects. |
| <span id="m-a08333365323"></span><code>MainViewModel.CloseProductionModal()</code><br>12335–12349 | — | No extracted literal effects. |
| <span id="m-492f8bb653a6"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>12351–12450 | ExecuteExistingProductionAsync @12354; Resolve @12376; NewGuid @12379; ToUpperInvariant @12381; ToString @12381; Insert @12399; IsNullOrWhiteSpace @12421; Trim @12421; ToDictionary @12423; Where @12423; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @12427; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @12427; DispatchToUi @12430; SafePipelineError @12430; RecordSuccessfulSearchUseAsync @12437; FromGuid @12437; ConfigureAwait @12440; LoadManufacturingDataAsync @12440; LoadInventoryAsync @12441; SafeError @12447 | No extracted literal effects. |
| <span id="m-5bb7562eb39e"></span><code>MainViewModel.CloseXReportModal()</code><br>12549–12552 | — | No extracted literal effects. |
| <span id="m-14a7278337d4"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>12554–12584 | CheckSessionUnlocked @12556; Clear @12574; Where @12575; GetUnlockCandidates @12575; Equals @12576; Add @12580 | No extracted literal effects. |
| <span id="m-83b73c0f6ab9"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>12586–12590 | — | No extracted literal effects. |
| <span id="m-5f1700e6a7a4"></span><code>MainViewModel.CloseZReportModal()</code><br>12592–12595 | — | No extracted literal effects. |
| <span id="m-30dfa66b305e"></span><code>MainViewModel.LoadReportDataAsync()</code><br>12597–12714 | ToString @12617; DispatchToUi @12633; ConfigureAwait @12661; ExecuteAsync @12661; Join @12663; Select(string, Money) @12663; InvoiceMoney @12663; ToDecimal @12666; ToDecimal @12667; ToDecimal @12668; ToDecimal @12669; ToDecimal @12671; ToDecimal @12673; ToDecimal @12674; ToDecimal @12675; ToDecimal @12676; ToDecimal @12677; ToUpperInvariant @12679; ToString @12679; ToString @12681; ToString @12682; Sum @12688; ToDecimal @12688; ToDecimal @12691; Add @12693; Format @12698; SafeError @12706 | No extracted literal effects. |
| <span id="m-d55b601b70bb"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>12716–12805 | CheckSessionUnlocked @12719; IsNullOrWhiteSpace @12736; AuthenticateSelectedUser @12744; Trim @12746; Round @12755; Trim @12759; ConfigureAwait(CloseShiftCommand, Shift) @12763; ExecuteAsync(CloseShiftCommand, Shift) @12763; DispatchToUi @12781; SafePipelineError @12781; ConfigureAwait @12788; ExecuteAsync @12788; SetActiveCashier @12792; RefreshUnlockCandidates @12793; RaisePropertyChanged @12794; nameof @12794; LoadReportDataAsync @12798; LoadTeamsStaffAsync @12799; SafeError @12803 | No extracted literal effects. |
| <span id="m-5bc92d01d591"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>12807–12871 | FirstOrDefault @12809; CreateCommand @12816; CreateParameter @12828; ToString @12830; Add @12831; ExecuteReader @12833; Read @12834; Parse @12836; GetString @12836; GetInt64 @12839; Pow @12841; IsDBNull @12843; Add @12864 | FROM items @12817; JOIN barcodes @12817; JOIN product_categories @12817 |
| <span id="m-71b0c5a9cb20"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>12873–12977 | IsNullOrWhiteSpace @12875; Trim @12878; ToList @12881; Where @12881; IsNullOrEmpty @12882; Equals @12882; ToString @12884; AddToCart @12890; CreateCommand @12906; CreateParameter @12921; Add @12924; ExecuteReader @12926; Read @12928; Parse @12930; GetString @12930; ContainsKey @12931; GetInt64 @12935; Pow @12937; IsDBNull @12939; First @12966; Add @12967 | FROM items @12907; JOIN barcodes @12907; JOIN product_categories @12907 |
| <span id="m-84ef42f2d7fe"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>12979–13022 | IsNullOrWhiteSpace @12981; Trim @12984; AppendReceiveSerialScan @12990; TryAddUniqueExactMatchToCart @12996; Clear @12998; ToList @13003; Where @13003; Equals @13003; AddToCart @13006 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml.cs</code> · 2,054 lines.

SHA-256: <code>6b9056bc2133b3f230bc48b4b7cc35f2f9370fe0a4d10e87f4db354968cd178e</code>.

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
| <span id="m-16cb6e6a24eb"></span><code>MainWindow.OnCompletedImportSaveRequested(byte[],string)</code><br>393–393 | SaveImportTemplateAsync @393 | No extracted literal effects. |
| <span id="m-dd19c492b47b"></span><code>MainWindow.OnInventoryTemplateSaveRequested(byte[])</code><br>395–395 | SaveImportTemplateAsync @395 | No extracted literal effects. |
| <span id="m-55cb4b47c432"></span><code>MainWindow.SaveImportTemplateAsync(byte[],string)</code><br>397–447 | GetDownloadsFolderPath @405; IsNullOrWhiteSpace @407; Exists @407; TryGetFolderFromPathAsync @409; SaveFilePickerAsync @413; OpenWriteAsync @431; SetLength @433; WriteAsync @435; ReportCodeBehindError @443 | No extracted literal effects. |
| <span id="m-e0d876d8e77e"></span><code>MainWindow.GetDownloadsFolderPath()</code><br>451–481 | IsWindows @455; SHGetKnownFolderPath @461; PtrToStringUni @469; FreeCoTaskMem @477 | No extracted literal effects. |
| <span id="m-3b23d8c5f1f4"></span><code>MainWindow.SHGetKnownFolderPath(Guid,uint,IntPtr,IntPtr)</code><br>485–487 | — | No extracted literal effects. |
| <span id="m-4c050ed76a02"></span><code>MainWindow.OnCopyToClipboardRequested(string)</code><br>491–517 | SetTextAsync @503; ReportCodeBehindError @513 | No extracted literal effects. |
| <span id="m-31f7fb708608"></span><code>MainWindow.OnElementGotFocus(object?,GotFocusEventArgs)</code><br>521–533 | — | No extracted literal effects. |
| <span id="m-c00f0f0e9b74"></span><code>MainWindow.OnPriceInputGotFocus(object?,GotFocusEventArgs)</code><br>537–545 | Post @543 | No extracted literal effects. |
| <span id="m-c8947a567a14"></span><code>MainWindow.OnPriceInputPointerReleased(object?,PointerReleasedEventArgs)</code><br>549–567 | FindAncestorOfType(TextBox) @563; SelectAll @565 | No extracted literal effects. |
| <span id="m-f7921fa0e528"></span><code>MainWindow.GetActiveEditableTextBox()</code><br>571–615 | IsAttachedToVisualTree @577; FindControl(TextBox) @599; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @599; FindControl(TextBox) @599 | No extracted literal effects. |
| <span id="m-7a2220ac9f24"></span><code>MainWindow.InsertTextIntoTextBox(TextBox,string)</code><br>619–675 | Min @629; Max @631; Insert @641; Remove @641; Clamp @659; Insert @661 | No extracted literal effects. |
| <span id="m-1531c3eeae21"></span><code>MainWindow.HandleBackspaceOnTextBox(TextBox)</code><br>679–737 | Min @689; Max @691; Remove @701; Clamp @717; DeleteGraphemeAt @723 | No extracted literal effects. |
| <span id="m-99b03e4bf2ba"></span><code>MainWindow.HandleClearOnTextBox(TextBox)</code><br>741–753 | — | No extracted literal effects. |
| <span id="m-10968d9d1150"></span><code>MainWindow.HandleNumericDigitOnTextBox(TextBox,string)</code><br>757–817 | Min @767; Max @769; Remove @781; Contains @787; IsNullOrEmpty @803; InsertTextIntoTextBox @815 | No extracted literal effects. |
| <span id="m-0dca022bf166"></span><code>MainWindow.WireTouchControls()</code><br>821–1125 | AddHandler @825; FindControl(GetSeek.UI.Components.Controls.TouchKeyboardControl) @829; FindControl(Border) @831; WireDraggableFloatingSurface @841; GetActiveEditableTextBox @851; HandleNumericDigitOnTextBox @857; Execute @865; InsertTextIntoTextBox @883; HandleBackspaceOnTextBox @909; HandleClearOnTextBox @935; FindControl(GetSeek.UI.Components.Controls.TouchNumpadControl) @973; Execute @999; Execute @1035; Execute @1071; Execute @1109 | No extracted literal effects. |
| <span id="m-642cfc5eaee1"></span><code>MainWindow.WireDraggableFloatingSurface(Control,Control)</code><br>1129–1243 | AddHandler @1157; GetCurrentPoint @1161; FindAncestorOfType(Button) @1165; FindAncestorOfType(TextBox) @1167; FindAncestorOfType(Avalonia.Controls.Primitives.ScrollBar) @1169; GetPosition @1181; Capture @1187; ReferenceEquals @1225; EndDrag @1239 | No extracted literal effects. |
| <span id="m-a3f93faf10db"></span><code>MainWindow.OnChooseQrImage(object?,RoutedEventArgs)</code><br>1247–1247 | ChoosePaymentImageAsync @1247 | No extracted literal effects. |
| <span id="m-be294d0d73ec"></span><code>MainWindow.OnChooseBankImage(object?,RoutedEventArgs)</code><br>1249–1249 | ChoosePaymentImageAsync @1249 | No extracted literal effects. |
| <span id="m-d458a112b5c3"></span><code>MainWindow.ChoosePaymentImageAsync(bool)</code><br>1253–1349 | OpenFilePickerAsync @1263; Localize @1269; OpenReadAsync @1295; Localize @1301; ReadAsync @1313; WriteAsync @1327; AsMemory @1327; ToArray @1331; SetManualPaymentImage @1335; ReportCodeBehindError @1343 | No extracted literal effects. |
| <span id="m-60362efdc801"></span><code>MainWindow.OnChooseExpenseReceiptImage(object?,RoutedEventArgs)</code><br>1353–1405 | OpenFilePickerAsync @1363; OpenReadAsync @1391; SetExpenseFormAttachmentAsync @1393; ReportCodeBehindError @1401 | No extracted literal effects. |
| <span id="m-df989810082a"></span><code>MainWindow.OnKeyDown(KeyEventArgs)</code><br>1409–1563 | OnKeyDown @1445; CanCaptureUnfocusedBarcodeWedge @1461; Clear @1465; ToString @1487; HandleBarcodeScanned @1499; GetPrintableCharacterFromKey @1517; IsNullOrEmpty @1519; Append @1529 | No extracted literal effects. |
| <span id="m-89ec24c6165b"></span><code>MainWindow.CanCaptureUnfocusedBarcodeWedge()</code><br>1567–1603 | GetTopLevel @1585; GetFocusedElement @1585; FindAncestorOfType(GetSeek.UI.Components.Controls.CompactDateField) @1589; GetType @1591 | No extracted literal effects. |
| <span id="m-1d68680e5129"></span><code>MainWindow.OnPreviewKeyboardAction(object?,KeyEventArgs)</code><br>1607–1799 | FirstOrDefault(GetSeek.UI.Components.Controls.CompactDateField) @1615; OfType(GetSeek.UI.Components.Controls.CompactDateField) @1615; GetVisualDescendants @1615; FirstOrDefault(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1635; OfType(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1635; TryHandleEscapeKey @1655; HandlePhysicalBackspace @1677; GetTopLevel @1693; GetFocusedElement @1693; IsWithinThirdPartyImportOverlay @1695; TryActivateFocusedButton @1699; FindControl(GetSeek.UI.Components.Controls.ModalShell) @1711; FindControl(Button) @1711; Focus @1711; FindControl(GetSeek.UI.Components.Controls.WorkspaceSearchBox) @1743; ReferenceEquals @1745; IsVisualAncestorOf @1745; SelectOption @1755; Trim @1765; IsNullOrEmpty @1767; TryAddUniqueExactMatchToCart @1771; Clear @1775 | No extracted literal effects. |
| <span id="m-09ecf5f4c5c8"></span><code>MainWindow.TryActivateFocusedButton()</code><br>1803–1857 | GetTopLevel @1811; GetFocusedElement @1813; CanExecute @1829; Execute @1843; RaiseEvent @1851 | No extracted literal effects. |
| <span id="m-0c891b95b37c"></span><code>MainWindow.IsWithinThirdPartyImportOverlay(Visual)</code><br>1861–1879 | FindControl(GetSeek.UI.Components.Controls.ModalShell) @1865; GetVisualParent @1867 | No extracted literal effects. |
| <span id="m-412cd51411bd"></span><code>MainWindow.FocusThirdPartyImportCloseButton()</code><br>1883–1889 | Post @1887; FindControl(GetSeek.UI.Components.Controls.ModalShell) @1887; FindControl(Button) @1887; Focus @1887 | No extracted literal effects. |
| <span id="m-12c1a4ba98fe"></span><code>MainWindow.HandlePhysicalBackspace()</code><br>1893–1957 | HandleBackspaceOnTextBox @1911; Execute @1923; Execute @1935; Execute @1947 | No extracted literal effects. |
| <span id="m-341bab645bc1"></span><code>MainWindow.GetPrintableCharacterFromKey(Key,KeyModifiers)</code><br>1961–1997 | ToString @1973; ToUpperInvariant @1973; ToString @1973 | No extracted literal effects. |
| <span id="m-10b1f92bdea1"></span><code>MainWindow.OnKeyUp(KeyEventArgs)</code><br>2001–2051 | OnKeyUp @2049 | No extracted literal effects. |

</details>

## AXAML, migrations and project inputs

### App.axaml {#src-1e635b06c6de}

<code>Software/src/GetSeek.Desktop/App.axaml</code> · 37 lines · SHA-256 <code>fbcb9d4c8bbedcd7ab20df886f595435317e99118d45946f85f9cb14b023ed01</code>.

### GetSeek.Desktop.csproj {#src-2f265207af15}

<code>Software/src/GetSeek.Desktop/GetSeek.Desktop.csproj</code> · 27 lines · SHA-256 <code>57c435b4d7b778cfe77cd7da0397f3607a8ad46a8db4dfcd71d522dd51ee3bdb</code>.

### MainWindow.axaml {#src-67243af94cf2}

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml</code> · 6167 lines · SHA-256 <code>866a969ab9a1a5b67c54f3e8d32424591a03da43090947e0d16ae20a5cfade6e</code>.
