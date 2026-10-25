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

<code>Software/src/GetSeek.Desktop/Models/UiModels.cs</code> · 892 lines.

SHA-256: <code>c545a2ab9b4f1fa4e4692903add31096f46ad207db8109d926951dedb768ceeb</code>.

Declarations: <code>CurrencyFormatter</code> (line 6), <code>CategoryItem : ReactiveObject</code> (line 20), <code>ProductCategoryOption</code> (line 48), <code>ExpenseCategoryOption</code> (line 65), <code>ProductPurposeOption</code> (line 80), <code>UomOption</code> (line 85), <code>StoreUomPreferenceItem : ReactiveObject</code> (line 139), <code>ProductItem : ReactiveObject</code> (line 161), <code>OrderItem : ReactiveObject</code> (line 194), <code>ParkedCart</code> (line 305), <code>StaleCartPriceReviewUiRow</code> (line 319), <code>LotCandidateItem</code> (line 327), <code>SerialCandidateItem : ReactiveObject</code> (line 342), <code>OrderStatusChip : ReactiveObject</code> (line 366), <code>OrderLogItem : ReactiveObject</code> (line 406), <code>InventoryItem : ReactiveObject</code> (line 437), <code>KitComponentDraftItem : ReactiveObject</code> (line 570), <code>PayrollMonthOption : IEquatable&lt;PayrollMonthOption&gt;</code> (line 602), <code>StaffMember : ReactiveObject</code> (line 626), <code>TeamMemberShiftItem : ReactiveObject</code> (line 686), <code>UserPermissionOverrideItem : ReactiveObject</code> (line 697), <code>ReportTenderItem : ReactiveObject</code> (line 755), <code>ShiftReportSummary : ReactiveObject</code> (line 764), <code>FacilityItem : ReactiveObject</code> (line 804), <code>BinLocationItem : ReactiveObject</code> (line 814), <code>ItemLocationEligibilityItem : ReactiveObject</code> (line 828), <code>ReceiveTrackingKind</code> (line 843), <code>ReceiveLineItem : ReactiveObject</code> (line 855).

<details markdown>
<summary>Methods, calls, table effects and failures (11)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7303823d0b7e"></span><code>CurrencyFormatter.Format(decimal,string,int)</code><br>8–17 | Clamp @10; Round @14; ToString @16 | No extracted literal effects. |
| <span id="m-bfe1e76935c9"></span><code>ProductCategoryOption.ToString()</code><br>62–62 | — | No extracted literal effects. |
| <span id="m-bb0cf46280a9"></span><code>ExpenseCategoryOption.ToString()</code><br>77–77 | — | No extracted literal effects. |
| <span id="m-c4b775694cc8"></span><code>ProductPurposeOption.ToString()</code><br>82–82 | — | No extracted literal effects. |
| <span id="m-7c1bacac4559"></span><code>UomOption.ToString()</code><br>136–136 | — | No extracted literal effects. |
| <span id="m-9cf5d29f9ea2"></span><code>LotCandidateItem.ToString()</code><br>338–338 | — | No extracted literal effects. |
| <span id="m-ab58a00200ae"></span><code>SerialCandidateItem.ToString()</code><br>363–363 | — | No extracted literal effects. |
| <span id="m-bf6e37b344e8"></span><code>PayrollMonthOption.Equals(PayrollMonthOption?)</code><br>615–616 | — | No extracted literal effects. |
| <span id="m-e2623c526780"></span><code>PayrollMonthOption.Equals(object?)</code><br>618–619 | Equals @619 | No extracted literal effects. |
| <span id="m-8446843b35d9"></span><code>PayrollMonthOption.GetHashCode()</code><br>621–621 | GetHashCode @621 | No extracted literal effects. |
| <span id="m-1b61bc5587a1"></span><code>PayrollMonthOption.ToString()</code><br>623–623 | — | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Services/UiPreferencesService.cs</code> · 4,814 lines.

SHA-256: <code>e943969445a5b83eeade887648b74f65fb5232af7560eaa48e8400465ab24f64</code>.

Declarations: <code>UiPreferences</code> (line 12), <code>IUiPreferencesService</code> (line 20), <code>UiPreferencesService : IUiPreferencesService</code> (line 30), <code>ILocalizationService</code> (line 86), <code>LocalizationService : ILocalizationService</code> (line 96), <code>ThemeManager</code> (line 4705).

<details markdown>
<summary>Methods, calls, table effects and failures (12)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-69a3b01d8029"></span><code>IUiPreferencesService.Load()</code><br>22–22 | — | No extracted literal effects. |
| <span id="m-592fdd3892e2"></span><code>IUiPreferencesService.Save(UiPreferences)</code><br>23–23 | — | No extracted literal effects. |
| <span id="m-c2b8dbfc95d6"></span><code>UiPreferencesService.Load()</code><br>47–64 | Exists @51; ReadAllText @53; Deserialize(UiPreferences) @54 | No extracted literal effects. |
| <span id="m-7261564d0166"></span><code>UiPreferencesService.Save(UiPreferences)</code><br>66–82 | GetDirectoryName @70; IsNullOrEmpty @71; CreateDirectory @73; WriteAllText @76; Serialize @76 | No extracted literal effects. |
| <span id="m-6065c0c3e12d"></span><code>ILocalizationService.Localize(string,object?[])</code><br>89–89 | — | No extracted literal effects. |
| <span id="m-7b2740cfa1a1"></span><code>LocalizationService.Localize(string,object?[])</code><br>4672–4702 | ToLowerInvariant @4674; Trim @4674; TryGetValue @4682; TryGetValue @4685; Format @4695 | No extracted literal effects. |
| <span id="m-25887db87510"></span><code>ThemeManager.Resolve(string?)</code><br>4722–4723 | IsNullOrWhiteSpace @4723; ContainsKey @4723 | No extracted literal effects. |
| <span id="m-c2242f68ff3a"></span><code>ThemeManager.DisplayName(string?)</code><br>4725–4725 | Resolve @4725 | No extracted literal effects. |
| <span id="m-82b950b969a5"></span><code>ThemeManager.NextTheme(string?)</code><br>4728–4741 | Equals @4733 | No extracted literal effects. |
| <span id="m-a7f478a82d50"></span><code>ThemeManager.Apply(string?)</code><br>4744–4778 | Equals @4747; Resolve @4749; SwapThemeSlot @4763; CheckAccess @4768; Post @4770; ApplyCore @4774 | No extracted literal effects. |
| <span id="m-e587861d65e5"></span><code>ThemeManager.IsThemeInclude(object)</code><br>4781–4783 | Contains @4783 | No extracted literal effects. |
| <span id="m-b46ad55809f8"></span><code>ThemeManager.SwapThemeSlot(IList&lt;IResourceProvider&gt;,string)</code><br>4785–4808 | ToList(ResourceInclude) @4789; Where(ResourceInclude) @4789; OfType(ResourceInclude) @4789; Remove @4791; Equals @4796; Add @4807 | No extracted literal effects. |

</details>

## CatalogOrderPageHelper.cs {#src-88c3ed51d197}

<code>Software/src/GetSeek.Desktop/ViewModels/CatalogOrderPageHelper.cs</code> · 412 lines.

SHA-256: <code>14185534066da6c31e4b8f52562d9ade7e3f78a412f9c2360e6184a27a5ac6de</code>.

Declarations: <code>CatalogFamily</code> (line 8), <code>AllItemCycleState</code> (line 14), <code>NocodeCycleState</code> (line 22), <code>CatalogCycleStateMachine</code> (line 29), <code>CatalogFilterRequest</code> (line 130), <code>CatalogFilterResult</code> (line 143), <code>CatalogOrderPageHelper</code> (line 151).

<details markdown>
<summary>Methods, calls, table effects and failures (20)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-164e1cc848a1"></span><code>CatalogCycleStateMachine.GetNextAllItemState(AllItemCycleState)</code><br>36–43 | — | No extracted literal effects. |
| <span id="m-d9e1690320fe"></span><code>CatalogCycleStateMachine.GetNextNocodeState(NocodeCycleState)</code><br>45–51 | — | No extracted literal effects. |
| <span id="m-2398c1c795dc"></span><code>CatalogCycleStateMachine.GetAllItemCaption(AllItemCycleState)</code><br>53–60 | — | No extracted literal effects. |
| <span id="m-97ec0beeddae"></span><code>CatalogCycleStateMachine.GetNocodeCaption(NocodeCycleState)</code><br>62–68 | — | No extracted literal effects. |
| <span id="m-8cb721343433"></span><code>CatalogCycleStateMachine.SelectOrCycleAllItem()</code><br>77–87 | GetNextAllItemState @85 | No extracted literal effects. |
| <span id="m-21ed82ef5058"></span><code>CatalogCycleStateMachine.SelectOrCycleNocode()</code><br>89–104 | GetNextNocodeState @102 | No extracted literal effects. |
| <span id="m-1acc312b3384"></span><code>CatalogCycleStateMachine.CycleActive()</code><br>106–116 | GetNextAllItemState @110; GetNextNocodeState @114 | No extracted literal effects. |
| <span id="m-0a37cf8b31c0"></span><code>CatalogCycleStateMachine.SelectFamily(CatalogFamily)</code><br>118–127 | — | No extracted literal effects. |
| <span id="m-c49527109c9a"></span><code>CatalogOrderPageHelper.CompareAtoZ(ProductItem,ProductItem)</code><br>157–166 | Compare @159; CompareTo @165 | No extracted literal effects. |
| <span id="m-3533d8411905"></span><code>CatalogOrderPageHelper.CompareZtoA(ProductItem,ProductItem)</code><br>168–178 | Compare @171; CompareTo @177 | No extracted literal effects. |
| <span id="m-4f8055dcfba6"></span><code>CatalogOrderPageHelper.CompareMostSold(ProductItem,ProductItem)</code><br>180–186 | CompareTo @182; CompareAtoZ @185 | No extracted literal effects. |
| <span id="m-8ccf35c59649"></span><code>CatalogOrderPageHelper.CompareNonBarcodeFirst(ProductItem,ProductItem)</code><br>188–195 | CompareAtoZ @194 | No extracted literal effects. |
| <span id="m-42f067c000d2"></span><code>CatalogOrderPageHelper.CompareBarcodeFirst(ProductItem,ProductItem)</code><br>197–204 | CompareAtoZ @203 | No extracted literal effects. |
| <span id="m-7db5475b48f2"></span><code>CatalogOrderPageHelper.CompareMostSoldNonBarcode(ProductItem,ProductItem)</code><br>206–217 | CompareMostSold @214; CompareAtoZ @216 | No extracted literal effects. |
| <span id="m-0cf4e4086419"></span><code>CatalogOrderPageHelper.CompareMostSoldAll(ProductItem,ProductItem)</code><br>219–222 | CompareMostSold @221 | No extracted literal effects. |
| <span id="m-e2932c611236"></span><code>CatalogOrderPageHelper.HasMatchingBarcode(ProductItem,Func&lt;string, bool&gt;)</code><br>224–236 | IsNullOrEmpty @230; predicate @230 | No extracted literal effects. |
| <span id="m-f8c043fa54bd"></span><code>CatalogOrderPageHelper.MatchesSearch(ProductItem,string)</code><br>238–252 | IsNullOrWhiteSpace @240; IsNullOrEmpty @242; Contains @242; Contains @245; HasMatchingBarcode @248; Contains @248 | No extracted literal effects. |
| <span id="m-d1cc6c170f2e"></span><code>CatalogOrderPageHelper.GetSearchRelevanceTier(ProductItem,string)</code><br>254–284 | IsNullOrEmpty @257; Equals @257; HasMatchingBarcode @258; StartsWith @270; StartsWith @271; StartsWith @277 | No extracted literal effects. |
| <span id="m-6668214f5720"></span><code>CatalogOrderPageHelper.CompareSearchRelevance(ProductItem,ProductItem,string)</code><br>286–295 | GetSearchRelevanceTier @288; CompareTo @292; CompareAtoZ @294 | No extracted literal effects. |
| <span id="m-d5f577f3cc10"></span><code>CatalogOrderPageHelper.FilterAndPage(CatalogFilterRequest)</code><br>297–411 | ThrowIfNull @299; IsNullOrWhiteSpace @301; Trim @301; Equals @312; MatchesSearch @346; Add @351; Sort @357; CompareSearchRelevance @357; Contains @386; Empty(ProductItem) @395; Clamp @400; ToList @402; Take @402; Skip @402 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.Catalog.cs</code> · 320 lines.

SHA-256: <code>f203b0ffc9e09f97af6b7b0512b85280f11f1424a16651a96eec684762b11892</code>.

Declarations: <code>MainViewModel</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-aed3065fc6b4"></span><code>MainViewModel.InitializeCatalogCommands()</code><br>68–76 | Create @70; Create(int) @73 | No extracted literal effects. |
| <span id="m-35d099b2d30b"></span><code>MainViewModel.SelectOrCycleAllItem()</code><br>78–88 | SelectOrCycleAllItem @80; RaisePropertyChanged @81; nameof @81; ApplyFilter @87 | No extracted literal effects. |
| <span id="m-17cf8fe3098c"></span><code>MainViewModel.SelectOrCycleNocode()</code><br>90–100 | SelectOrCycleNocode @92; RaisePropertyChanged @93; nameof @93; ApplyFilter @99 | No extracted literal effects. |
| <span id="m-6f90fe5406ee"></span><code>MainViewModel.CycleActiveCatalogOrdering()</code><br>102–113 | CycleActive @104; RaisePropertyChanged @105; nameof @105; ApplyFilter @112 | No extracted literal effects. |
| <span id="m-3ba11dc6be6d"></span><code>MainViewModel.SetCatalogPageSize(int)</code><br>115–133 | Contains @122; RaisePropertyChanged @129; nameof @129; ApplyFilter @132 | No extracted literal effects. |
| <span id="m-d6d4507482b6"></span><code>MainViewModel.NextCatalogPage()</code><br>135–143 | RaisePropertyChanged @140; nameof @140; ApplyFilter @141 | No extracted literal effects. |
| <span id="m-e3dadbe8e98b"></span><code>MainViewModel.PreviousCatalogPage()</code><br>145–153 | RaisePropertyChanged @150; nameof @150; ApplyFilter @151 | No extracted literal effects. |
| <span id="m-67cb9440a57e"></span><code>MainViewModel.GoToCatalogPage(int)</code><br>155–160 | RaisePropertyChanged @158; nameof @158; ApplyFilter @159 | No extracted literal effects. |
| <span id="m-727fd86e4bec"></span><code>MainViewModel.SelectCatalogKind(string)</code><br>162–200 | Equals @164; RaisePropertyChanged @168; nameof @168; Clear @171; Any @176; IsNullOrEmpty @180; LoadCategoriesForKind @193; ApplyFilter @199 | No extracted literal effects. |
| <span id="m-216a40b0241a"></span><code>MainViewModel.LoadCategoriesForKind(string)</code><br>202–228 | ToList @204; Where @204; Equals @204; Clear @205; GroupBy @206; IsNullOrEmpty @210; Add @218; Count @222; RaisePropertyChanged @227; nameof @227 | No extracted literal effects. |
| <span id="m-0f6ac6371174"></span><code>MainViewModel.OnSearchQueryChanged(string?,string?)</code><br>230–254 | IsNullOrWhiteSpace @232; RaisePropertyChanged @239; nameof @239; ApplyFilter @253 | No extracted literal effects. |
| <span id="m-f8002353fdc8"></span><code>MainViewModel.SelectCategoryById(Guid?)</code><br>256–282 | SelectCategory @260; FirstOrDefault @264; FirstOrDefault @274; RaisePropertyChanged @277; nameof @277; ApplyFilter @280 | No extracted literal effects. |
| <span id="m-8086b42a97bc"></span><code>MainViewModel.ApplyFilter()</code><br>284–319 | FilterAndPage @299; RaisePropertyChanged @305; nameof @305; Clear @314; Add @317 | No extracted literal effects. |

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

SHA-256: <code>5cd0260e9ee82a9258e342a02244879cfc5a95896e68b37a5800a09238a3ec67</code>.

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 13,119 lines.

SHA-256: <code>0b29ddb3ebe9790ebf71e00ca4c9ea000c83728e94bac29fbdb5cb4f5e4b0f08</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 8700).

<details markdown>
<summary>Methods, calls, table effects and failures (253)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4d3c549b9d46"></span><code>MainViewModel.RefreshCurrentTime()</code><br>121–121 | RaisePropertyChanged @121; nameof @121 | No extracted literal effects. |
| <span id="m-47378cde4176"></span><code>MainViewModel.SetStatusNotificationOnUi(string)</code><br>391–404 | RaiseAndSetIfChanged @393; IsNullOrWhiteSpace @394; Insert @396; RemoveAt @397; RaisePropertyChanged @398; nameof @398; Stop @401; Start @403 | No extracted literal effects. |
| <span id="m-fa69ff5d121c"></span><code>MainViewModel.ClearNotifications()</code><br>426–433 | Stop @428; Clear @430; RaisePropertyChanged @431; nameof @431; RaiseAndSetIfChanged @432 | No extracted literal effects. |
| <span id="m-c2746ce12114"></span><code>MainViewModel.CycleInventoryLifecycleStatusScope()</code><br>685–690 | — | No extracted literal effects. |
| <span id="m-66947125c815"></span><code>MainViewModel.IsLockScreenLockedOut(int)</code><br>1204–1220 | Ceiling @1211 | No extracted literal effects. |
| <span id="m-3ebef3ead614"></span><code>MainViewModel.RefreshUnlockCandidates()</code><br>1262–1287 | GetUnlockCandidates @1265; Clear @1268; Add @1271; Any @1273; CheckAccess @1279; action @1281; Post @1285 | No extracted literal effects. |
| <span id="m-9b2e1d40194d"></span><code>MainViewModel.UpdateReceiveKitBreakdownAsync()</code><br>1645–1665 | GetValueOrDefault @1653; ConfigureAwait @1658; BuildBreakdownSummaryAsync @1658 | No extracted literal effects. |
| <span id="m-752d66859a23"></span><code>MainViewModel.UpdateCartKitBreakdownAsync(OrderItem)</code><br>1667–1679 | ConfigureAwait @1672; BuildBreakdownSummaryAsync @1672 | No extracted literal effects. |
| <span id="m-72988f14f506"></span><code>MainViewModel.OnProductPricingDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>2104–2123 | RaisePropertyChanged @2106; nameof @2106; RecomputeProductPricingPreview @2122 | No extracted literal effects. |
| <span id="m-c11816b8d203"></span><code>MainViewModel.RecomputeProductPricingPreview()</code><br>2132–2182 | Clear @2134; RaisePropertyChanged @2135; nameof @2135; ToMinorUnits @2144; Parse @2149; TryParse @2153; Equals @2167; Increment @2170; Localize @2171; ToArray @2173; RecomputeKitPricingPreviewAsync @2174; ResolveSelectedProductSaleUnitFactor @2179; Round @2180; RebuildProductPricingPreview @2181 | No extracted literal effects. |
| <span id="m-c0f415592449"></span><code>MainViewModel.RecomputeKitPricingPreviewAsync(long,string,string,decimal,string,long,decimal,IReadOnlyList&lt;KitComponentDraftItem&gt;)</code><br>2184–2254 | ConfigureAwait @2188; WaitAsync @2188; Read @2191; DispatchToUi @2195; SetProductPricingPreviewNotice @2195; CalculateItemOrKitAsync @2209; ResolveSelectedProductSaleUnitFactor @2233; Round @2234; RebuildProductPricingPreview @2238; Release @2252 | No extracted literal effects. |
| <span id="m-cf148d526ec4"></span><code>MainViewModel.SetProductPricingPreviewNotice(string)</code><br>2256–2260 | Localize @2258; RaisePropertyChanged @2259; nameof @2259 | No extracted literal effects. |
| <span id="m-2b1ee22b5804"></span><code>MainViewModel.RebuildProductPricingPreview(long,string,decimal,string,long,decimal)</code><br>2262–2326 | Clear @2265; RaisePropertyChanged @2267; nameof @2267; Equals @2268; SetProductPricingPreviewNotice @2270; ParsePricingMethod @2274; ParseRoundingRule @2275; IsRoundingRuleCompatible @2276; TryConvertRoundingIncrement @2283; ToMinorUnits @2290; ResolveEffectiveBasePrice @2291; ToList @2295; OrderBy @2295; Where @2295; FirstOrDefault @2302; TryParse @2313; ToString @2314; ResolveTierPrice @2317; Add @2319; Format @2321; ToDisplayAmount @2321; FirstOrDefault @2322 | No extracted literal effects. |
| <span id="m-f6d73b60a002"></span><code>MainViewModel.ResolveSelectedProductSaleUnitFactor()</code><br>2380–2395 | FirstOrDefault @2383; Equals @2383; TryParse @2387 | No extracted literal effects. |
| <span id="m-0cf5a3e6dd2f"></span><code>MainViewModel.ExactMinorToCurrency(decimal)</code><br>2403–2404 | ScalingFactor @2404; Clamp @2404 | No extracted literal effects. |
| <span id="m-a48ebb4ccd43"></span><code>MainViewModel.BuildCostSourcesTooltip(long,long,long,long?,string,DateTime?)</code><br>2461–2481 | Format @2469; ToDecimal @2470; Localize @2473; Format @2473; ToLocalTime @2475; Join @2480 | No extracted literal effects. |
| <span id="m-f6fa3fda3845"></span><code>MainViewModel.AddKitComponent()</code><br>2641–2678 | IsNullOrWhiteSpace @2656; FirstOrDefault @2658; Equals @2659; Add @2666; RaisePropertyChanged @2677; nameof @2677 | No extracted literal effects. |
| <span id="m-ec7aade99187"></span><code>MainViewModel.RemoveKitComponent(KitComponentDraftItem?)</code><br>2680–2687 | Remove @2684; RaisePropertyChanged @2685; nameof @2685 | No extracted literal effects. |
| <span id="m-bf3d2e5d1e4b"></span><code>MainViewModel.RefreshVirtualKitAvailability()</code><br>2698–2711 | Increment @2700; ToArray @2707; Select @2707; LoadVirtualKitAvailabilityAsync @2710 | No extracted literal effects. |
| <span id="m-f58dbde33ebd"></span><code>MainViewModel.LoadVirtualKitAvailabilityAsync(long,IReadOnlyList&lt;KitComponentInput&gt;)</code><br>2713–2753 | ConfigureAwait @2717; GetKitAvailabilityAsync @2717; DispatchToUi @2719; Read @2721; Localize @2724; Max @2733; ResolveSelectedProductSaleUnitFactor @2733; GetValueOrDefault @2734; Clamp @2735; Pow @2736; Floor @2737; Format @2739; ToString @2741 | No extracted literal effects. |
| <span id="m-3cc02e2ea1f4"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3596–3604 | IsNullOrWhiteSpace @3598 | No extracted literal effects. |
| <span id="m-8503a8edc2d5"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3606–3617 | Load @3608; IsNullOrWhiteSpace @3612; Resolve @3614; Apply @3616 | No extracted literal effects. |
| <span id="m-abac9503116c"></span><code>MainViewModel.OpenImport()</code><br>3646–3654 | CheckSessionUnlocked @3648; Increment @3650; ResetInventoryImport @3651; Invoke @3653 | No extracted literal effects. |
| <span id="m-337a998a1688"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3656–3717 | Increment @3659; ResetInventoryImport @3664; IsNullOrWhiteSpace @3669; Exists @3669; FinishFailedImport @3671; ConfigureAwait @3683; ReadAllBytesAsync @3683; ToHexString @3684; HashData @3684; TemplateContextAsync @3688; Run @3689; Read @3689; ValidateInventoryAsync @3690; CompletedWorkbook @3691; DispatchToUi @3698; ReferenceEquals @3700; Add @3701; Localize @3702; SetImportReviewRows @3706; RaisePropertyChanged @3707; nameof @3707; ReportException @3713 | No extracted literal effects. |
| <span id="m-43d148420722"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3719–3773 | IsCurrentImportAttempt @3735; ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3749; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3749; ConfigureAwait @3753; RecoverImportOutcomeAsync @3753; Localize @3756; DispatchToUi @3757; FinishImportAttempt @3757; LoadInventoryAsync @3758; ReportException @3759; ReportError @3763; FinishFailedImport @3764; ImportCommandIssue @3764 | No extracted literal effects. |
| <span id="m-e8f9f25f92c7"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3785–3795 | Report @3787; DispatchToUi @3788; Insert @3790 | No extracted literal effects. |
| <span id="m-a6a556e9ad7a"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3797–3801 | RaisePropertyChanged @3800; nameof @3800 | No extracted literal effects. |
| <span id="m-9c38701e1274"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3803–3806 | ReportError @3805 | No extracted literal effects. |
| <span id="m-b4a0c07d9d7e"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3812–3817 | ReportError @3815 | No extracted literal effects. |
| <span id="m-ced55f2c214c"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3826–3832 | IsNullOrWhiteSpace @3828; Trim @3828; ReportError @3830 | No extracted literal effects. |
| <span id="m-85b46930a37b"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3834–3837 | DispatchToUi @3836; Insert @3836 | No extracted literal effects. |
| <span id="m-6a79a6b6dd48"></span><code>MainViewModel.DispatchToUi(Action)</code><br>3843–3857 | CheckAccess @3845; action @3847; GetResult @3855; GetAwaiter @3855; InvokeAsync @3855 | No extracted literal effects. |
| <span id="m-e2152ab69fd3"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4518–4583 | Register @4520; Execute @4520; Execute @4521; Execute @4522; Execute @4523; Execute @4528; Execute @4529; Execute @4530; Execute @4531; Execute @4532; Execute @4533; Execute @4534; Execute @4535; Execute @4536; Execute @4537; Execute @4538; Execute @4539; Execute @4540; Execute @4541; Execute @4542; Execute @4543; Execute @4544; Execute @4545; Execute @4546; Execute @4547; Execute @4548; Execute @4549; Execute @4550; Execute @4551; Execute @4552; Execute @4553; Execute @4554; Execute @4555; Execute @4556; Execute @4557; Execute @4558; Execute @4559; Execute @4561; Execute @4562; RequestClosePersonForm @4563; KeepEditingPersonForm @4564; CloseSalaryMonthDetailModal @4565; CloseSalaryPaymentModal @4566; CloseSalaryAdjustmentModal @4567; CloseSalaryFinalizeModal @4568; RequestCloseExpenseForm @4569; KeepEditingExpenseForm @4570; CloseExpenseCategoryModal @4571; CloseExpensePaymentModal @4572; CloseExpenseDetailModal @4573; ClosePaymentReturnModal @4574; CloseWasteExpenseConfirmation @4575; InitializeSalaryTables @4580; InitializeExpensesTables @4581; InitializeTeamsCommands @4582 | No extracted literal effects. |
| <span id="m-3738040c3901"></span><code>MainViewModel.CreateDemo()</code><br>4585–4592 | SetActiveCashier @4588; Parse @4588; RefreshUnlockCandidates @4590 | No extracted literal effects. |
| <span id="m-5add3c400b90"></span><code>MainViewModel.CreateInitializing()</code><br>4594–4602 | — | No extracted literal effects. |
| <span id="m-58977ebfaedd"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4604–4614 | — | No extracted literal effects. |
| <span id="m-89857bb12f33"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4616–4634 | ConfigureDiagnosticsWorkspace @4630; ResolveDiagnosticsWorkspace @4630; ApplyPersistedState @4631; RefreshUnlockCandidates @4632 | No extracted literal effects. |
| <span id="m-7c93516d8fc2"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4636–4664 | CheckSessionUnlocked @4638; HasPermission @4639; Equals @4650; GetFileNameWithoutExtension @4650; GetEntryAssembly @4652; Add @4654; Start @4657; ReportException @4662 | No extracted literal effects. |
| <span id="m-3d5143a6ebc8"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4666–4689 | CheckSessionUnlocked @4668; HasPermission @4669; Equals @4679; GetFileNameWithoutExtension @4679; Add @4680; GetEntryAssembly @4680; Start @4682; ReportException @4687 | No extracted literal effects. |
| <span id="m-f0fa2f73ee89"></span><code>MainViewModel.Dispose()</code><br>4691–4712 | ClearImportResults @4694; Increment @4695; ResetFinancialWorkspace @4697; Dispose @4698; Stop @4699; CancelBatchPricingPreviewExpiry @4702; Dispose @4703; Dispose @4704; DisposeSearchStates @4710; SuppressFinalize @4711 | No extracted literal effects. |
| <span id="m-5a2d6ae79242"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4714–4718 | Stop @4716 | No extracted literal effects. |
| <span id="m-aa7ca91f7cf4"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4720–4758 | Clear @4730; Clear @4731; Clear @4732; Clear @4733; Clear @4734; Clear @4735; Clear @4736; Clear @4737; Clear @4738; Clear @4739 | No extracted literal effects. |
| <span id="m-5a3525d2a06a"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4760–4876 | RaisePropertyChanged @4774; nameof @4774; Clear @4776; Clear @4777; Clear @4778; CreateCommand @4785; ExecuteReader @4787; Read @4788; TryParse @4790; GetString @4790; Add @4791; Add @4799; GroupBy @4800; Count @4802; Contains @4807; Add @4831; ApplyFilter @4833; All @4835; SafeError @4838; SetActiveCashier @4846; ToString @4850; ToString @4853; ToLocalTime @4853; NotifyTotalsChanged @4875 | FROM item_kits @4786 |
| <span id="m-71c2824fd6f6"></span><code>MainViewModel.InitializeDemoData()</code><br>4878–4955 | Add @4884; Add @4903; ApplyFilter @4914; Add @4917; Add @4922; Add @4928; ApplyActivityFilter @4934; Add @4937; ApplyInventoryFilter @4946; Add @4949; Parse @4949; NotifyTotalsChanged @4954 | No extracted literal effects. |
| <span id="m-c78f6fc4c92a"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>4957–4970 | — | No extracted literal effects. |
| <span id="m-c28531bcd97f"></span><code>MainViewModel.SelectMenu(string)</code><br>4972–5043 | CheckSessionUnlocked @4974; NormalizeMenuKey @4978; LoadInvoicesAsync @4984; LoadCommercialAsync @4985; LoadActivityInvoicesAsync @4992; LoadTeamsStaffAsync @4995; LoadCatalogRegistryAsync @4996; UpdateDemoSeedingAvailabilityAsync @4999; UpdateReceiptDesignPreview @5002; RefreshDiagnosticsAsync @5003; LoadPriceLevelSettingsAsync @5004; LoadInventoryAsync @5007; LoadPriceProposalsAsync @5009; LoadReportDataAsync @5012; LoadFinancialRegisterAsync @5013; LoadCustomersAsync @5016; LoadSuppliersAsync @5017; LoadThirdPartiesAsync @5018; LoadManufacturingDataAsync @5023; LoadManagedUnitsAsync @5031; LoadManagedCategoriesAsync @5034; LoadSalaryWorkspaceAsync @5037; LoadExpensesWorkspaceAsync @5040 | No extracted literal effects. |
| <span id="m-6682d126fd52"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>5045–5064 | — | No extracted literal effects. |
| <span id="m-1e786a4c4ecf"></span><code>MainViewModel.LogOut()</code><br>5066–5087 | Clear @5068; RaisePropertyChanged @5071; nameof @5071; ClearNotifications @5073; ResetCashReview @5077; Lock @5080; RefreshUnlockCandidates @5085; UpdateDemoSeedingAvailabilityAsync @5086 | No extracted literal effects. |
| <span id="m-55b68e3fad1b"></span><code>MainViewModel.UnlockSession()</code><br>5089–5092 | UnlockSession @5091 | No extracted literal effects. |
| <span id="m-ed621e424681"></span><code>MainViewModel.UnlockSession(string?)</code><br>5094–5193 | IsLockScreenLockedOut @5102; IsNullOrWhiteSpace @5118; AuthenticateSelectedUser @5127; Lock @5132; AddSeconds @5138; AddMinutes @5155; Initialize @5174; Unlock @5175; Any @5179; Equals @5179; RaisePropertyChanged @5180; nameof @5180; LoadActivityInvoicesAsync @5184; LoadTrackOrdersAsync @5185; UpdateDemoSeedingAvailabilityAsync @5186; StartAutomaticDemoDatasetLoadAsync @5187 | No extracted literal effects. |
| <span id="m-8a92f3351eef"></span><code>MainViewModel.PowerAction()</code><br>5195–5201 | CheckSessionUnlocked @5197 | No extracted literal effects. |
| <span id="m-8fc2911b8d06"></span><code>MainViewModel.CycleTable()</code><br>5203–5209 | CheckSessionUnlocked @5205 | No extracted literal effects. |
| <span id="m-8b67b636ed43"></span><code>MainViewModel.CycleDiningType()</code><br>5211–5217 | CheckSessionUnlocked @5213 | No extracted literal effects. |
| <span id="m-67673165a946"></span><code>MainViewModel.CycleCustomer()</code><br>5219–5222 | OpenCustomerChooser @5221 | No extracted literal effects. |
| <span id="m-a5754b903cc2"></span><code>MainViewModel.OpenPromoDialog()</code><br>5224–5239 | CheckSessionUnlocked @5226; IsNullOrWhiteSpace @5233; RaisePropertyChanged @5237; nameof @5237 | No extracted literal effects. |
| <span id="m-987cf5bb0874"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5241–5310 | CheckSessionUnlocked @5243; ToLowerInvariant @5256; Trim @5256; IsNullOrWhiteSpace @5263; Trim @5263; ToList @5271; Select @5271; ToMinorUnits @5275; Equals @5291; Calculate @5295; NotifyTotalsChanged @5307; ConfigureAwait @5309; SaveDurableCartAsync @5309 | No extracted literal effects. |
| <span id="m-96d06669e04b"></span><code>MainViewModel.TogglePromo()</code><br>5312–5329 | CheckSessionUnlocked @5314; RemovePromo @5323; OpenPromoDialog @5327 | No extracted literal effects. |
| <span id="m-8e100a4fd198"></span><code>MainViewModel.RemovePromo()</code><br>5331–5341 | NotifyTotalsChanged @5338; SaveDurableCartAsync @5340 | No extracted literal effects. |
| <span id="m-91677128eded"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5343–5354 | CheckSessionUnlocked @5345; NotifyTotalsChanged @5351; ConfigureAwait @5353; SaveDurableCartAsync @5353 | No extracted literal effects. |
| <span id="m-ed0c56b5977a"></span><code>MainViewModel.CancelPromoDialog()</code><br>5356–5360 | — | No extracted literal effects. |
| <span id="m-20ba5f061b7a"></span><code>MainViewModel.RecalculateCart()</code><br>5362–5416 | ToMinorUnits @5378; Add @5379; Equals @5400; Calculate @5404; ToDictionary @5407; TryGetValue @5410 | No extracted literal effects. |
| <span id="m-60cdca795f6a"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5418–5425 | CheckSessionUnlocked @5420; ResetCashReview @5421 | No extracted literal effects. |
| <span id="m-174d9e6949dd"></span><code>MainViewModel.SelectCategory(CategoryItem?)</code><br>5427–5467 | CheckSessionUnlocked @5429; RaisePropertyChanged @5437; nameof @5437; ApplyFilter @5438 | No extracted literal effects. |
| <span id="m-dba77798e4ed"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5469–5469 | AddToCart @5469 | No extracted literal effects. |
| <span id="m-65fff0647824"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5471–5515 | CheckSessionUnlocked @5473; ResetCashReview @5474; ResolveProductSaleUnitFactor @5477; Round @5484; FirstOrDefault @5485; UpdateCartKitBreakdownAsync @5494; Add @5506; NotifyTotalsChanged @5509; SaveDurableCartAsync @5511; IsNullOrWhiteSpace @5513; ToString @5513; NewGuid @5513; RecordSuccessfulSearchUseAsync @5514; FromGuid @5514 | No extracted literal effects. |
| <span id="m-72e5f803a1c0"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5517–5530 | CheckSessionUnlocked @5519; ResetCashReview @5520; UpdateCartKitBreakdownAsync @5527; NotifyTotalsChanged @5528; SaveDurableCartAsync @5529 | No extracted literal effects. |
| <span id="m-76c652086359"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5532–5547 | CheckSessionUnlocked @5534; ResetCashReview @5535; UpdateCartKitBreakdownAsync @5539; Remove @5543; NotifyTotalsChanged @5545; SaveDurableCartAsync @5546 | No extracted literal effects. |
| <span id="m-ad868a178c30"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5549–5555 | ConfigureAwait @5552; LoadAsync @5552; RefreshSavedPaymentImages @5553; CancelManualPaymentSettings @5554 | No extracted literal effects. |
| <span id="m-8a47e94d26fc"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5557–5586 | ValidImage @5564; CreatePaymentBitmap @5569; Dispose @5572; RaisePropertyChanged @5584; nameof @5584 | No extracted literal effects. |
| <span id="m-bdd7873d9c6d"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5588–5604 | Dispose @5598; CreatePaymentBitmap @5600; RaisePropertyChanged @5602; nameof @5602 | No extracted literal effects. |
| <span id="m-c74be0ffa570"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5606–5610 | — | No extracted literal effects. |
| <span id="m-b5572dc48753"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5612–5620 | Dispose @5614; CreatePaymentBitmap @5616; RaisePropertyChanged @5618; nameof @5618 | No extracted literal effects. |
| <span id="m-aaa973c5c080"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5622–5641 | ConfigureAwait @5631; ExecuteAsync @5631; DispatchToUi @5634; SafePipelineError @5634; LoadAsync @5637; RefreshSavedPaymentImages @5638; CancelManualPaymentSettings @5639 | No extracted literal effects. |
| <span id="m-4c134641749f"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5643–5662 | IsNullOrWhiteSpace @5647; Trim @5648; ToMinorUnits @5654; ConfigureAwait @5660; PlaceOrderAsync @5660 | No extracted literal effects. |
| <span id="m-dae6baa5015a"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5664–5676 | PlaceOrderInternalAsync @5670 | No extracted literal effects. |
| <span id="m-0d4c06b835c2"></span><code>MainViewModel.PlaceOrderInternalAsync()</code><br>5678–5879 | Localize @5682; ExecuteDemoPlaceOrder @5688; ConfigureAwait @5714; SaveDurableCartAsync @5714; ToMinorUnits @5722; Trim @5724; Equals @5735; Equals @5742; ResetCashReview @5744; Max @5802; Add @5807; ConfigureAwait(TakePaymentCommand, SalesInvoice) @5825; ExecuteAsync(TakePaymentCommand, SalesInvoice) @5825; Format @5837; ToDecimal @5837; DispatchToUi @5839; Clear @5843; NewGuid @5852; NotifyTotalsChanged @5853; LoadActivityInvoicesAsync @5860; OpenStaleCartPriceReviewAsync @5865; RequestElevationForCheckout @5867; SafePipelineError @5871; SafeError @5877 | No extracted literal effects. |
| <span id="m-22b53b0c9a5b"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>5881–5913 | DispatchToUi @5885; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5888; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5888; SafePipelineError @5893; ToArray @5897; Select @5897; Where @5897; FormatCartReviewMoney @5901; Clear @5908; Add @5909 | No extracted literal effects. |
| <span id="m-57c16c0de9b8"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>5915–5920 | ScalingFactor @5917; Format @5919; Equals @5919 | No extracted literal effects. |
| <span id="m-e574afa88abd"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>5922–5953 | CheckSessionUnlocked @5924; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5926; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5926; DispatchToUi @5931; SafePipelineError @5931; ConfigureAwait @5932; OpenStaleCartPriceReviewAsync @5932; FirstOrDefault @5939; ScalingFactor @5942; ResetCashReview @5946; Clear @5949; NotifyTotalsChanged @5950 | No extracted literal effects. |
| <span id="m-be020a06809c"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>5955–5962 | Clear @5959; ResetCashReview @5960 | No extracted literal effects. |
| <span id="m-49e11e437de9"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>5964–5990 | CheckSessionUnlocked @5966; ResetCashReview @5973; ToMinorUnits @5984; ConfigureAwait @5989; PlaceOrderAsync @5989 | No extracted literal effects. |
| <span id="m-d35e5c3a2b1c"></span><code>MainViewModel.CancelCashReview()</code><br>5992–5996 | ResetCashReview @5994 | No extracted literal effects. |
| <span id="m-7dcb3e4e259d"></span><code>MainViewModel.ResetCashReview()</code><br>5998–6007 | — | No extracted literal effects. |
| <span id="m-f51893d3aaac"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>6009–6028 | RaisePropertyChanged @6020; nameof @6020; Clear @6023; ResetCashReview @6024; NotifyTotalsChanged @6025 | No extracted literal effects. |
| <span id="m-49a0e2f52cc8"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>6030–6095 | ConfigureAwait @6034; WaitAsync @6034; ClearActiveCartAsync @6039; ToMinorUnits @6049; Add @6050; ToUpperInvariant @6053; ToString @6053; IsNullOrWhiteSpace @6056; SaveActiveCartAsync @6069; DispatchToUi @6088; SafeError @6088; Release @6093 | No extracted literal effects. |
| <span id="m-458ab2ae04c8"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>6097–6156 | ConfigureAwait @6103; GetActiveCartAsync @6103; Clear @6115; FirstOrDefault @6118; ToDecimal @6122; Add @6132; NotifyTotalsChanged @6149 | No extracted literal effects. |
| <span id="m-5348d672e7f0"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>6158–6235 | ApplyPagedResult @6162; ToList @6163; ApplyActivityFilter @6167; HasPermission @6172; ConfigureAwait @6179; GetPagedActivityInvoicesAsync @6179; ToPageRequest @6182; ToDecimal @6188; Add @6189; ToString @6194; ToLocalTime @6194; DispatchToUi @6213; Clear @6215; Add @6218; SafeError @6232 | No extracted literal effects. |
| <span id="m-c216b9658d86"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>6237–6314 | HasPermission @6242; ConfigureAwait @6249; GetActiveOrdersAsync @6249; Clear @6250; ToDecimal @6254; Join @6288; Select @6288; Add @6290; ToString @6305; ToLocalTime @6305 | No extracted literal effects. |
| <span id="m-6824316ed307"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6316–6343 | CheckSessionUnlocked @6318; Clear @6321; ConfigureAwait @6327; GetOrderByIdAsync @6327; Add @6332; DispatchToUi @6338; SafeError @6338 | No extracted literal effects. |
| <span id="m-a40c4ae5cda6"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6345–6350 | Clear @6349 | No extracted literal effects. |
| <span id="m-00b201383cc3"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6352–6385 | CheckSessionUnlocked @6354; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6370; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6370; ConfigureAwait @6379; LoadTrackOrdersAsync @6379; DispatchToUi @6383; SafePipelineError @6383 | No extracted literal effects. |
| <span id="m-75b29dd66d86"></span><code>MainViewModel.MarkReadyAsync()</code><br>6387–6420 | CheckSessionUnlocked @6389; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6405; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6405; ConfigureAwait @6414; LoadTrackOrdersAsync @6414; DispatchToUi @6418; SafePipelineError @6418 | No extracted literal effects. |
| <span id="m-9507ef512648"></span><code>MainViewModel.MarkServedAsync()</code><br>6422–6455 | CheckSessionUnlocked @6424; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6440; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6440; ConfigureAwait @6449; LoadTrackOrdersAsync @6449; DispatchToUi @6453; SafePipelineError @6453 | No extracted literal effects. |
| <span id="m-88a1fd8bb678"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6457–6485 | CheckSessionUnlocked @6459; Remove @6463; CloseOrderDetailsModal @6464; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6473; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6473; ConfigureAwait @6479; LoadTrackOrdersAsync @6479; DispatchToUi @6483; SafePipelineError @6483 | No extracted literal effects. |
| <span id="m-94e5e98addae"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6487–6583 | CheckSessionUnlocked @6489; CloseOrderDetailsModal @6495; ConfigureAwait @6502; GetOrderByIdAsync @6502; Zero @6524; NewGuid @6530; ToList @6533; Select @6533; ToUpperInvariant @6536; ToString @6536; SaveActiveCartAsync @6545; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6561; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6561; DispatchToUi @6564; SafePipelineError @6564; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6570; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6570; LoadTrackOrdersAsync @6576; LoadActivityInvoicesAsync @6577 | No extracted literal effects. |
| <span id="m-e62db4b52150"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6585–6592 | CheckSessionUnlocked @6587 | No extracted literal effects. |
| <span id="m-ee43cc9548b4"></span><code>MainViewModel.FilterActivity(string)</code><br>6611–6617 | CheckSessionUnlocked @6613; ApplyActivityFilter @6615 | No extracted literal effects. |
| <span id="m-a61f3832edfe"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6619–6658 | Clear @6621; AsEnumerable @6622; Where @6627; IsNullOrWhiteSpace @6630; Trim @6632; Contains @6634; Contains @6635; Contains @6636; IsNullOrEmpty @6640; Equals @6642; ToList @6646; Add @6648; ApplyPagedResult @6652 | No extracted literal effects. |
| <span id="m-eb88be2501b0"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6660–6696 | CheckSessionUnlocked @6662; ConfigureAwait(QueueReceiptReprintCommand, string) @6682; ExecuteAsync(QueueReceiptReprintCommand, string) @6682; IsNullOrWhiteSpace @6683; ReportError @6685; RefreshOutputStatusAsync @6690; DispatchToUi @6694; SafeError @6694 | No extracted literal effects. |
| <span id="m-49616f3cb5ef"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6698–6741 | RefreshOutputPrinterQueues @6703; ReadAsync @6704; Equals @6711; IsNullOrWhiteSpace @6711; TryReadGeometry @6713; ComputeCapabilityFingerprint @6717; ConfigureAwait @6721; InvalidateThermalVerificationAsync @6721; LoadCashFinancialSettingsAsync @6733; LoadReceiptDesignAsync @6734; RefreshOutputStatusAsync @6735; DispatchToUi @6739; SafeError @6739 | No extracted literal effects. |
| <span id="m-16b68be816f7"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6743–6769 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6756; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6756; ReportError @6759; LoadOutputDevicesAsync @6762; DispatchToUi @6767; SafeError @6767 | No extracted literal effects. |
| <span id="m-347ee91cfd17"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6771–6844 | Equals @6785; IsNullOrWhiteSpace @6790; IsWindows @6795; TryReadGeometry @6800; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6817; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6817; ReportError @6820; Render @6823; ToString @6824; ConfigureAwait @6825; Run @6825; Send @6825; ComputeCapabilityFingerprint @6826; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @6827; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @6827; RefreshOutputStatusAsync @6838; DispatchToUi @6842; SafeError @6842 | No extracted literal effects. |
| <span id="m-4cc128386b38"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>6846–6883 | IsWindows @6860; IsNullOrWhiteSpace @6860; TryReadGeometry @6862; ComputeCapabilityFingerprint @6866; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @6867; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @6867; ReportError @6871; ConfigureAwait @6877; RefreshOutputStatusAsync @6877; DispatchToUi @6881; SafeError @6881 | InvalidOperationException @6861; InvalidOperationException @6865 |
| <span id="m-40c8dcb9f945"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>6885–6922 | CreateCommand @6890; ConfigureAwait @6899; ExecuteReaderAsync @6899; ReadAsync @6900; GetInt32 @6903; GetString @6903; GetInt64 @6903; Parse @6904; RaisePropertyChanged @6906; nameof @6906; NotifyTotalsChanged @6915; DispatchToUi @6920; SafeError @6920 | FROM store_config @6891 |
| <span id="m-edb922e60320"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>6924–6952 | ConfigureAwait @6937; ExecuteAsync @6937; ReportError @6940; NotifyTotalsChanged @6945; DispatchToUi @6950; SafeError @6950 | No extracted literal effects. |
| <span id="m-886fc69b700f"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>6954–6998 | DispatchToUi @6958; CreateCommand @6963; ConfigureAwait @6969; ExecuteReaderAsync @6969; ReadAsync @6970; Deserialize(ReceiptDesignDocument) @6972; GetString @6972; SafeError @6991 | FROM receipt_designs @6964; JOIN receipt_design_versions @6964 |
| <span id="m-48006e387a9f"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>7000–7027 | ConfigureAwait @7013; ExecuteAsync @7013; ReportError @7018; DispatchToUi @7025; SafeError @7025 | No extracted literal effects. |
| <span id="m-f4634a1c0d0e"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>7029–7041 | IsWindows @7031; Select @7032; Enumerate @7032; Empty(string) @7033; ToArray @7034; OrderBy @7034; Distinct @7034; Where @7034; Append @7034; IsNullOrWhiteSpace @7035; Clear @7039; Add @7040 | No extracted literal effects. |
| <span id="m-e511d7b85d74"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>7043–7101 | CheckAccess @7045; DispatchToUi @7047; CreateSampleData @7053; Equals @7059; IsWindows @7066; TryReadGeometry @7067; BuildPaperDocument @7076; RenderPreviewPngPages @7079; SetReceiptDesignPreviewPages @7081; Localize @7083; BuildThermalLines @7088; RenderPreviewPng @7090; Empty(byte[]) @7097; ReportException @7099 | No extracted literal effects. |
| <span id="m-4e2941bde164"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>7103–7108 | ShowReceiptDesignPreviewPage @7107 | No extracted literal effects. |
| <span id="m-ce051243d916"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>7110–7116 | ShowReceiptDesignPreviewPage @7115 | No extracted literal effects. |
| <span id="m-14a92a792340"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>7118–7132 | RaisePropertyChanged @7129; nameof @7129 | No extracted literal effects. |
| <span id="m-4deb7972fb82"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>7134–7163 | ReadAsync @7137; Localize @7140; CreateCommand @7142; ConfigureAwait @7144; ExecuteScalarAsync @7144; ToString @7144; IsNullOrWhiteSpace @7145; ExecuteReaderAsync @7159; ReadAsync @7160; Trim @7161; GetString @7161 | FROM hardware_jobs @7143; FROM hardware_jobs @7158 |
| <span id="m-93cb8edd0da6"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>7165–7181 | Clear @7167; AsEnumerable @7168; Where @7171; IsNullOrWhiteSpace @7173; Contains @7175; Contains @7176; Contains @7177; Add @7180 | No extracted literal effects. |
| <span id="m-d6be3a019198"></span><code>MainViewModel.GenerateXReport()</code><br>7183–7202 | CheckSessionUnlocked @7185; ToString @7189; GenerateXReportInternalAsync @7201 | No extracted literal effects. |
| <span id="m-73e5c30d68f3"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>7204–7219 | ConfigureAwait @7208; LoadReportDataAsync @7208; DispatchToUi @7217; SafeError @7217 | No extracted literal effects. |
| <span id="m-76ddc0e7ae84"></span><code>MainViewModel.CloseShiftZReport()</code><br>7221–7224 | OpenCloseShiftModal @7223 | No extracted literal effects. |
| <span id="m-116e510ea1b2"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>7226–7235 | CheckSessionUnlocked @7233 | No extracted literal effects. |
| <span id="m-7f9ac59e2d14"></span><code>MainViewModel.SaveSettings()</code><br>7237–7241 | CheckSessionUnlocked @7239 | No extracted literal effects. |
| <span id="m-a86c2aee6251"></span><code>MainViewModel.ApplySettingsAsync()</code><br>7243–7330 | CheckSessionUnlocked @7252; NotifyTotalsChanged @7271; ExecuteAsync @7299; DispatchToUi @7323; SafePipelineError @7323; SafeError @7328 | No extracted literal effects. |
| <span id="m-f52fc9495c6b"></span><code>MainViewModel.CancelSettings()</code><br>7332–7353 | CheckSessionUnlocked @7334; NotifyTotalsChanged @7346 | No extracted literal effects. |
| <span id="m-31b5aa674c4a"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7356–7386 | ProbeDatabaseAsync @7369; ProbeLicense @7375; RefreshOutputStatusAsync @7378; ProbeHardwareStubs @7379; DispatchToUi @7384; SafeError @7384 | No extracted literal effects. |
| <span id="m-1f17d04d711b"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7447–7485 | RaisePropertyChanged @7449; nameof @7449; FormatRealResetPreviewSummary @7484 | No extracted literal effects. |
| <span id="m-8d9776b35862"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7487–7500 | Localize @7488; ToString @7490; GetValueOrDefault @7490; ToString @7495; ToString @7496; ToString @7497 | No extracted literal effects. |
| <span id="m-8fa2d377bba3"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7609–7701 | Post @7613; ConfigureAwait @7620; GetWorkspaceEnvironmentAsync @7620; Equals @7621; GetDatasetStateAsync @7623; CreateCommand @7629; CreateParameter @7636; ToString @7638; Add @7639; ExecuteScalarAsync @7640; HasPermission @7645; ToInt64 @7650; ExecuteScalarAsync @7650; ExecuteScalarAsync @7654; ExecuteScalarAsync @7661; ExecuteScalarAsync @7667; Localize @7686 | FROM items @7649; FROM sales_invoices @7653; FROM third_parties @7666; FROM users @7630; JOIN user_roles @7630 · DYNAMIC SQL: inspect manually |
| <span id="m-a1e4694611a7"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>7703–7713 | CheckSessionUnlocked @7705; HasPermission @7706 | No extracted literal effects. |
| <span id="m-79c651f21be1"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>7715–7720 | ConfigureAwait @7719; ResetDatabaseAsync @7719 | No extracted literal effects. |
| <span id="m-784325ef4f10"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>7722–7723 | ConfigureAwait @7723; EnsureDefaultDemoDatasetAsync @7723 | No extracted literal effects. |
| <span id="m-6071506c73b5"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>7725–7731 | EnsureDefaultDemoDatasetAsync @7729 | No extracted literal effects. |
| <span id="m-1a9e8430ea8e"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>7733–7837 | Localize @7738; ConfigureAwait @7745; WaitAsync @7745; GetWorkspaceEnvironmentAsync @7748; Equals @7749; HasPermission @7756; Post @7770; LocalizeDemoSeedProgress @7772; EnsureInitialDatasetAsync @7778; Join @7802; Select @7802; ReloadCatalogAsync @7812; LoadInventoryAsync @7813; LoadThirdPartiesAsync @7814; LoadManufacturingDataAsync @7815; LoadSuppliersAsync @7816; UpdateDemoSeedingAvailabilityAsync @7817; ToUpperInvariant @7822; ToString @7822; NewGuid @7822; LogDiagnosticError @7823; ReportError @7828; Release @7835 | No extracted literal effects. |
| <span id="m-a26a327eedec"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>7839–7853 | Localize @7841 | No extracted literal effects. |
| <span id="m-7e518ae3f158"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>7855–7952 | Localize @7859; ConfigureAwait @7863; WaitAsync @7863; HasPermission @7867; GetWorkspaceEnvironmentAsync @7874; Equals @7875; ResetDatabaseAsync @7883; GetStoreProfileAsync @7886; Post @7887; Clear @7890; Clear @7891; Clear @7892; NewGuid @7893; RaisePropertyChanged @7896; nameof @7896; Lock @7897; Defaults @7910; RefreshUnlockCandidates @7923; LoadCashFinancialSettingsAsync @7924; LoadOutputDevicesAsync @7925; LoadManualPaymentSettingsAsync @7926; LoadReceiptDesignAsync @7927; ReloadCatalogAsync @7928; LoadInventoryAsync @7929; LoadThirdPartiesAsync @7930; LoadManufacturingDataAsync @7931; LoadActivityInvoicesAsync @7932; UpdateDemoSeedingAvailabilityAsync @7933; ToUpperInvariant @7938; ToString @7938; LogDiagnosticError @7939; ReportError @7945; Release @7950 | No extracted literal effects. |
| <span id="m-185cc63af242"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>7954–7996 | CheckSessionUnlocked @7956; HasPermission @7958; ConfigureAwait @7966; GetWorkspaceEnvironmentAsync @7966; Equals @7967; PreviewAsync @7970; FormatRealResetPreviewSummary @7971; Post @7972; RaisePropertyChanged @7989; nameof @7989; SafeError @7994 | UnauthorizedAccessException @7968 |
| <span id="m-d4ff361e492a"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>7998–8084 | HasPermission @8001; ConfigureAwait @8019; ExecuteAsync @8019; GetStoreProfileAsync @8028; Post @8031; Clear @8035; Clear @8036; Clear @8037; Clear @8038; NewGuid @8039; Lock @8042; RaisePropertyChanged @8056; nameof @8056; LoadCashFinancialSettingsAsync @8057; LoadOutputDevicesAsync @8058; LoadManualPaymentSettingsAsync @8059; LoadReceiptDesignAsync @8060; RefreshUnlockCandidates @8068; LoadInventoryAsync @8069; LoadActivityInvoicesAsync @8070; UpdateDemoSeedingAvailabilityAsync @8071; ToUpperInvariant @8076; ToString @8076; LogDiagnosticError @8077 | No extracted literal effects. |
| <span id="m-4d903b6a43f9"></span><code>MainViewModel.CancelRealShopReset()</code><br>8086–8093 | RaisePropertyChanged @8092; nameof @8092 | No extracted literal effects. |
| <span id="m-7cb3e262bd5c"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>8097–8114 | ConfigureAwait @8099; ExportDocumentAsync @8099; Post @8103; GetFileName @8107 | No extracted literal effects. |
| <span id="m-1a2c06809bf2"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>8116–8138 | Exists @8121; CreateDirectory @8123; Start @8125; ToUpperInvariant @8134; ToString @8134; NewGuid @8134; LogDiagnosticError @8135 | No extracted literal effects. |
| <span id="m-9a0112d13635"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>8140–8150 | CheckSessionUnlocked @8142; RaisePropertyChanged @8144; nameof @8144; Localize @8146; ToString @8147 | No extracted literal effects. |
| <span id="m-d023cf60281a"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>8157–8173 | CheckSessionUnlocked @8159; HasPermission @8160; RaisePropertyChanged @8166; nameof @8166; Localize @8169; ToString @8170 | No extracted literal effects. |
| <span id="m-b50f73cbb80b"></span><code>MainViewModel.CommitNumpad()</code><br>8175–8252 | CheckSessionUnlocked @8177; ResetCashReview @8178; TryParse @8184; IsNullOrWhiteSpace @8186; Trim @8192; NotifyTotalsChanged @8202; SaveDurableCartAsync @8203; Min @8209; ToMinorUnits @8211; Round @8212; TryParse @8227; UpdateCartKitBreakdownAsync @8235; Remove @8241; RaisePropertyChanged @8250; nameof @8250 | No extracted literal effects. |
| <span id="m-9dd1172ef69b"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>8258–8276 | CheckSessionUnlocked @8266 | No extracted literal effects. |
| <span id="m-d5bc6e08225a"></span><code>MainViewModel.StageBusinessProfile()</code><br>8283–8313 | CheckSessionUnlocked @8285; HasPermission @8289 | No extracted literal effects. |
| <span id="m-3be49b6a57df"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8315–8324 | — | No extracted literal effects. |
| <span id="m-eefdd80643d0"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8326–8349 | RecalculateCart @8328; RaisePropertyChanged @8330; nameof @8330 | No extracted literal effects. |
| <span id="m-529c84c3c2d5"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8351–8438 | IsNullOrWhiteSpace @8354; Trim @8354; All @8364; Trim @8381; Trim @8382; NewGuid @8386; ToString @8391; ConfigureAwait @8395; BeginTransactionAsync @8395; HandleAsync @8396; AppendAsync @8401; ToString @8402; Serialize @8407; CommitAsync @8410; Initialize @8416; Unlock @8417; RaisePropertyChanged @8422; nameof @8422; LoadTeamsStaffAsync @8425; StartAutomaticDemoDatasetLoadAsync @8426; RollbackAsync @8430; DispatchToUi @8431; SafePipelineError @8431; SafeError @8436 | No extracted literal effects. |
| <span id="m-4bcf0194329d"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8440–8447 | IsNullOrWhiteSpace @8442; ConfigureAwait @8446; SaveTeamMemberAsync @8446 | No extracted literal effects. |
| <span id="m-caead2c5daf1"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8449–8467 | CheckSessionUnlocked @8452; HasPermission @8454 | No extracted literal effects. |
| <span id="m-8791198fc3f7"></span><code>MainViewModel.CancelChangePin()</code><br>8469–8476 | — | No extracted literal effects. |
| <span id="m-58c8964962cf"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8478–8554 | Trim @8486; IsNullOrWhiteSpace @8489; All @8495; Equals @8508; Equals @8509; SetQuickPin @8521; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8534; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8534; ConfigureAwait @8542; LoadTeamsStaffAsync @8542; DispatchToUi @8547; SafePipelineError @8547; SafeError @8552 | No extracted literal effects. |
| <span id="m-faa74c79934c"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8556–8630 | HasPermission @8562; ConfigureAwait @8571; ResolveEffectivePermissionsAsync @8571; Contains @8604; Contains @8605; Add @8607; Contains @8613; DispatchToUi @8619; Clear @8621; Add @8622; SafeError @8628 | No extracted literal effects. |
| <span id="m-7ca554704299"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8632–8674 | OnTeamMemberFieldChanged @8638; ConfigureAwait @8655; ExecuteAsync @8655; DispatchToUi @8659; SafePipelineError @8667; SafeError @8672 | No extracted literal effects. |
| <span id="m-c0429d3ff5de"></span><code>MainViewModel.ClosePermissionEditor()</code><br>8676–8681 | — | No extracted literal effects. |
| <span id="m-21a7695558b9"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>8683–8698 | ClearImportResults @8685 | No extracted literal effects. |
| <span id="m-74a5e09c6b10"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>8702–8702 | — | No extracted literal effects. |
| <span id="m-24819b6c24e2"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>8703–8703 | — | No extracted literal effects. |
| <span id="m-8beb982bc529"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>8704–8704 | FromResult @8704 | No extracted literal effects. |
| <span id="m-fc5f9f466855"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>8707–8792 | HasPermission @8716; FromDecimal @8731; ConfigureAwait(OpenShiftCommand, Shift) @8735; ExecuteAsync(OpenShiftCommand, Shift) @8735; SetActiveCashier @8750; RefreshUnlockCandidates @8751; ToUpperInvariant @8768; ToString @8768; ToString @8770; ConfigureAwait @8780; LoadTeamsStaffAsync @8780; LoadTrackOrdersAsync @8781; DispatchToUi @8785; SafePipelineError @8785; SafeError @8790 | No extracted literal effects. |
| <span id="m-2c276b0410a3"></span><code>MainViewModel.LoadInventoryAsync()</code><br>8794–8948 | ApplyPagedResult @8798; ToList @8799; ApplyInventoryFilter @8803; Clear @8811; Empty(InventoryItem) @8813; ConfigureAwait @8818; GetPagedInventoryItemsAsync @8818; ToPageRequest @8823; CreateCommand @8836; ExecuteReaderAsync @8838; ReadAsync @8839; Add @8841; Parse @8841; GetString @8841; ExecuteReaderAsync @8851; ReadAsync @8852; TryParse @8854; GetString @8854; IsDBNull @8854; Add @8865; TryGetValue @8867; Contains @8875; ToDecimal @8878; Localize @8886; ToLocalTime @8892; BuildCostSourcesTooltip @8894; DispatchToUi @8921; Add @8924; SafeError @8946 | FROM item_kits @8837; FROM item_pricing @8850 |
| <span id="m-7115919691f2"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>8950–9006 | CheckSessionUnlocked @8952; FirstOrDefault @8953; Clear @8964; Add @8966; CreateCommand @8971; CreateParameter @8982; Add @8985; ExecuteReader @8986; Read @8987; GetString @8989; Contains @8990; FirstOrDefault @9002; ResetReceiveLines @9003; UpdateReceiveKitBreakdownAsync @9004 | FROM uoms @8972; JOIN uoms @8972 |
| <span id="m-b3d213743ce6"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>9008–9109 | IsNullOrWhiteSpace @9021; Localize @9038; HasPermission @9042; BuildReceiptLines @9048; Sum @9065; Trim @9075; ToMinorUnits @9080; ConfigureAwait(ReceiveStockCommand, StockMovement) @9085; ExecuteAsync(ReceiveStockCommand, StockMovement) @9085; Clear @9095; ConfigureAwait @9097; LoadInventoryAsync @9097; LoadItemHistoryAsync @9098; DispatchToUi @9102; SafePipelineError @9102; SafeError @9107 | No extracted literal effects. |
| <span id="m-494e2ef74405"></span><code>MainViewModel.ResetReceiveLines()</code><br>9115–9132 | Clear @9117; Add @9121; RaisePropertyChanged @9127; nameof @9127; Invoke @9130 | No extracted literal effects. |
| <span id="m-5eeb9456e8d8"></span><code>MainViewModel.AddReceiveLine()</code><br>9135–9158 | IsNullOrWhiteSpace @9142; Add @9148; RaisePropertyChanged @9153; nameof @9153; Invoke @9156 | No extracted literal effects. |
| <span id="m-8f8bfa57f28a"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>9161–9178 | Remove @9168; Add @9171; RaisePropertyChanged @9177; nameof @9177 | No extracted literal effects. |
| <span id="m-b0675cf4c94e"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>9184–9205 | IsNullOrWhiteSpace @9186; LastOrDefault @9191; Add @9195; Trim @9198; ReferenceEquals @9199; RaisePropertyChanged @9203; nameof @9203; Invoke @9204 | No extracted literal effects. |
| <span id="m-5d79eebdf1fa"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>9208–9285 | Add @9220; IsNullOrWhiteSpace @9228; Trim @9232; FirstOrDefault @9241; GroupBy @9241; Count @9243; Trim @9270 | No extracted literal effects. |
| <span id="m-573d86d8e726"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>9287–9323 | CreateCommand @9292; ConfigureAwait @9299; ExecuteReaderAsync @9299; Clear @9300; ReadAsync @9301; Add @9303; ParseGuidSafe @9304; GetString @9304; IsDBNull @9308; GetInt32 @9312; Parse @9314; DispatchToUi @9321; SafeError @9321 | FROM third_parties @9293 |
| <span id="m-3126959da522"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9325–9343 | CheckSessionUnlocked @9327; FirstOrDefault @9333 | No extracted literal effects. |
| <span id="m-74b26d165027"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9345–9436 | IsNullOrWhiteSpace @9368; HasPermission @9379; Trim @9397; Trim @9399; ConfigureAwait(AdjustStockCommand, StockMovement) @9403; ExecuteAsync(AdjustStockCommand, StockMovement) @9403; ConfigureAwait @9419; LoadInventoryAsync @9419; LoadItemHistoryAsync @9420; OpenWasteExpenseConfirmation @9424; DispatchToUi @9429; SafePipelineError @9429; SafeError @9434 | No extracted literal effects. |
| <span id="m-7c8cf3137ce5"></span><code>MainViewModel.OpenAddProduct()</code><br>9438–9506 | ResetProductStockDraft @9440; CheckSessionUnlocked @9441; HasPermission @9442; RaisePropertyChanged @9450; nameof @9450; ClearItemHistory @9452; LoadCatalogRegistryAsync @9459; InitializeProductPricingDraft @9462; Clear @9477; Clear @9478; Where @9479; Add @9481; FirstOrDefault @9483; Clear @9494; CaptureProductModalBaselineAsync @9505 | No extracted literal effects. |
| <span id="m-e740e65fd71b"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9508–9508 | OpenEditProduct @9508 | No extracted literal effects. |
| <span id="m-c6a7d8035d94"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9510–9590 | ResetProductStockDraft @9512; CheckSessionUnlocked @9514; HasPermission @9515; RaisePropertyChanged @9523; nameof @9523; ClearItemHistory @9525; LoadCatalogRegistryAsync @9533; InitializeProductPricingDraft @9539; ToMinorUnits @9540; LoadExactProductCostSnapshotsAsync @9546; ToDecimal @9550; Clear @9557; Clear @9558; Where @9559; Add @9561; FirstOrDefault @9563; LoadItemLocationEligibilitiesAsync @9582; LoadProductKitAsync @9583; LoadPrimaryBarcodeAsync @9584; LoadProductPricingDraftAsync @9585; LoadItemHistoryAsync @9586; LoadItemPriceHistoryAsync @9587; CaptureProductModalBaselineAsync @9589 | No extracted literal effects. |
| <span id="m-9923e1e74668"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>9592–9605 | OrderBy @9595; Where @9595; Add @9597 | No extracted literal effects. |
| <span id="m-a9ba464d2e01"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>9607–9680 | CreateCommand @9614; CreateParameter @9621; ToString @9623; Add @9624; ConfigureAwait @9625; ExecuteReaderAsync @9625; ReadAsync @9626; GetInt32 @9628; IsDBNull @9629; GetString @9629; ParseStoredPricingPercentForDisplay @9630; ToDisplayAmount @9634; GetInt64 @9634; OrderBy @9654; Where @9654; TryGetValue @9657; Add @9663; InvokeAsync @9665; RaisePropertyChanged @9670; nameof @9670; CaptureProductPricingSnapshot @9673; DispatchToUi @9678; SafeError @9678 | FROM item_price_levels @9645; FROM item_pricing @9616 |
| <span id="m-0bfa1de14f91"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>9682–9717 | CreateCommand @9689; CreateParameter @9695; ToString @9697; Add @9698; ConfigureAwait @9699; ExecuteReaderAsync @9699; ReadAsync @9700; Parse @9703; GetString @9703; GetInt32 @9703; GetInt64 @9704; IsDBNull @9704; Parse @9705; InvokeAsync @9707; DispatchToUi @9715; SafeError @9715 | FROM product_category_pricing_rules @9690 |
| <span id="m-074e312f6bd8"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>9719–9748 | ConfigureAwait @9723; WhenAll @9723; InvokeAsync @9724; CaptureProductModalSnapshot @9728; CaptureProductPricingSnapshot @9729; RaisePropertyChanged @9730; nameof @9730 | No extracted literal effects. |
| <span id="m-ce6c33396fd6"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>9750–9798 | Serialize @9750; ToArray @9773; Select @9773; Select @9790; OrderBy @9790; OrderBy @9794 | No extracted literal effects. |
| <span id="m-063327762de9"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>9800–9812 | Serialize @9800; ToArray @9811; Select @9811 | No extracted literal effects. |
| <span id="m-3374757580d3"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9814–9846 | nameof @9816; RaisePropertyChanged @9817; RaiseTraceabilityState @9822; StartsWith @9826; RecomputeProductPricingPreview @9837; RefreshVirtualKitAvailability @9839 | No extracted literal effects. |
| <span id="m-7b4954050bfd"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>9848–9862 | RaisePropertyChanged @9856; nameof @9856; RecomputeProductPricingPreview @9859; RefreshVirtualKitAvailability @9860 | No extracted literal effects. |
| <span id="m-12e1473b6b82"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9864–9872 | RaisePropertyChanged @9866; nameof @9866; RecomputeProductPricingPreview @9869; RefreshVirtualKitAvailability @9870 | No extracted literal effects. |
| <span id="m-076d2b716d6c"></span><code>MainViewModel.RequestCloseProductModal()</code><br>9874–9887 | DiscardProductModal @9886 | No extracted literal effects. |
| <span id="m-bade9d76a1ee"></span><code>MainViewModel.DiscardProductModal()</code><br>9889–9898 | RaisePropertyChanged @9894; nameof @9894; ClearItemHistory @9896 | No extracted literal effects. |
| <span id="m-a353edc03621"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>9900–9918 | CreateCommand @9905; CreateParameter @9907; ToString @9909; Add @9910; ConfigureAwait @9911; ExecuteScalarAsync @9911; DispatchToUi @9914; ToString @9914 | FROM barcodes @9906 |
| <span id="m-63239e99666a"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>9920–9971 | CreateCommand @9925; CreateParameter @9932; ToString @9934; Add @9935; ConfigureAwait @9939; ExecuteReaderAsync @9939; ReadAsync @9940; IsDBNull @9943; GetString @9943; GetDouble @9944; ResolveQuantity @9945; Add @9946; Parse @9948; DispatchToUi @9956; Clear @9959; Add @9960; RaisePropertyChanged @9963; nameof @9963; RecomputeProductPricingPreview @9966; RefreshVirtualKitAvailability @9967 | FROM item_kits @9926; JOIN item_kit_components @9926; JOIN items @9926 |
| <span id="m-76d1d1b57017"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>9973–9973 | SaveProductConfigurationAsync @9973 | No extracted literal effects. |
| <span id="m-fc64dff91dc4"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>9975–10180 | ConfigureAwait @9980; LoadCatalogRegistryAsync @9980; HasPermission @9982; IsNullOrWhiteSpace @9987; Localize @10009; Equals @10019; ToMinorUnits @10064; GetValueOrDefault @10076; Trim @10077; Trim @10078; Trim @10079; Trim @10086; Trim @10088; ToList @10133; Select @10133; CaptureProductPricingSnapshot @10137; ToCommand @10139; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @10147; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @10147; DispatchToUi @10150; RaiseTraceabilityState @10156; CaptureProductModalSnapshot @10158; RaisePropertyChanged @10160; nameof @10160; ReloadCatalogAsync @10167; LoadInventoryAsync @10168; LoadItemHistoryAsync @10169; SafePipelineError @10173; SafeError @10178 | No extracted literal effects. |
| <span id="m-d35a9619e2c3"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>10182–10218 | CheckSessionUnlocked @10184; HasPermission @10185; ConfigureAwait(DeactivateProductCommand, bool) @10201; ExecuteAsync(DeactivateProductCommand, bool) @10201; ConfigureAwait @10206; ReloadCatalogAsync @10206; LoadInventoryAsync @10207; DispatchToUi @10211; SafePipelineError @10211; SafeError @10216 | No extracted literal effects. |
| <span id="m-32cf3789d955"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>10220–10295 | ConfigureAwait @10226; GetActiveItemsAsync @10226; Clear @10228; Clear @10229; Clear @10230; CreateCommand @10235; ExecuteReaderAsync @10237; ReadAsync @10238; TryParse @10240; GetString @10240; Add @10241; Add @10248; GroupBy @10249; Count @10251; Contains @10256; Add @10280; All @10283; SafeError @10286; ApplyFilter @10289 | FROM item_kits @10236 |
| <span id="m-5b2cef8dcd99"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>10297–10303 | IsNullOrWhiteSpace @10299; TryParse @10300; HashData @10301; GetBytes @10301; AsSpan @10302 | No extracted literal effects. |
| <span id="m-59b358418a94"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>10305–10371 | CreateCommand @10311; ConfigureAwait @10314; ExecuteReaderAsync @10314; ReadAsync @10316; Add @10318; GetString @10320; GetInt32 @10324; Clear @10330; Add @10331; ExecuteReaderAsync @10343; ReadAsync @10345; Add @10347; GetString @10349; IsDBNull @10353; GetInt32 @10357; Clear @10363; Add @10364; DispatchToUi @10369; SafeError @10369 | FROM bins @10336; FROM facilities @10313; JOIN facilities @10336 |
| <span id="m-1a04495c5540"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>10586–10693 | CreateCommand @10596; ConfigureAwait @10603; ExecuteReaderAsync @10603; ReadAsync @10604; Add @10606; ParseGuidSafe @10608; GetString @10608; IsDBNull @10611; GetInt32 @10612; Add @10632; DispatchToUi @10647; Clear @10649; Clear @10650; Clear @10651; Clear @10652; Equals @10656; Add @10657; Add @10659; Add @10661; Add @10663; Clear @10665; Add @10666; FirstOrDefault @10669; Equals @10669; FirstOrDefault @10674; FirstOrDefault @10681; ApplySaleUnitDefaultsToCatalog @10686; SafeError @10691 | FROM product_categories @10598; FROM uoms @10624 |
| <span id="m-5eaa934a97f5"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>10695–10709 | ResolveProductSaleUnitFactor @10699; Round @10705; ApplyFilter @10708 | No extracted literal effects. |
| <span id="m-f1c7cdc07c22"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>10711–10729 | FirstOrDefault @10713; Equals @10714; TryParse @10721 | No extracted literal effects. |
| <span id="m-f06370dfad58"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>10731–10753 | CheckSessionUnlocked @10733; HasPermission @10734; ConfigureAwait @10749; LoadManagedCategoriesAsync @10749; CaptureCategoryFormSnapshot @10751; RaisePropertyChanged @10752; nameof @10752 | No extracted literal effects. |
| <span id="m-6d9364f49a94"></span><code>MainViewModel.CloseCategoryManager()</code><br>10755–10764 | — | No extracted literal effects. |
| <span id="m-772c899ea286"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>10766–10788 | CheckSessionUnlocked @10768; HasPermission @10769; ConfigureAwait @10784; LoadManagedUnitsAsync @10784; CaptureUnitFormSnapshot @10786; RaisePropertyChanged @10787; nameof @10787 | No extracted literal effects. |
| <span id="m-9eda49cb277d"></span><code>MainViewModel.CloseUnitManager()</code><br>10790–10799 | — | No extracted literal effects. |
| <span id="m-87d5c5df62a6"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>10801–10864 | Clear @10804; Clear @10805; Clear @10806; CreateCommand @10807; ConfigureAwait @10813; ExecuteReaderAsync @10813; ReadAsync @10814; Add @10816; ParseGuidSafe @10818; GetString @10818; IsDBNull @10821; GetInt32 @10822; Where @10830; Equals @10830; Add @10831; TryParse @10844; Add @10845; RefreshTargetedCategoryCollections @10858; DispatchToUi @10859; RefreshManagedCategoriesTable @10861; RefreshManagedExpenseCategoriesTable @10862 | FROM expense_categories @10835; FROM product_categories @10809; JOIN expense_records @10835 |
| <span id="m-4cb517cdfdce"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>10866–10873 | OpenCategoryManagerAsync @10868; FirstOrDefault @10869; EditManagedCategory @10872 | No extracted literal effects. |
| <span id="m-7cfb5f29ba8f"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>10875–10883 | OpenCategoryManagerAsync @10878; FirstOrDefault @10879; EditManagedExpenseCategory @10882 | No extracted literal effects. |
| <span id="m-58c9a2df0e42"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>10885–10907 | DispatchToUi @10887; Clear @10889; Clear @10890; Clear @10891; Clear @10892; Where @10894; Equals @10897; Add @10898; Add @10900; Add @10902; Add @10904 | No extracted literal effects. |
| <span id="m-02ca5ac3e0e0"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>10909–10921 | CaptureCategoryFormSnapshot @10919; RaisePropertyChanged @10920; nameof @10920 | No extracted literal effects. |
| <span id="m-d09cdeee2bf5"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>10923–10936 | CaptureCategoryFormSnapshot @10934; RaisePropertyChanged @10935; nameof @10935 | No extracted literal effects. |
| <span id="m-d16e1a5872d9"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>10938–10948 | Serialize @10938 | No extracted literal effects. |
| <span id="m-6e42641982fc"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>10950–10960 | Serialize @10950 | No extracted literal effects. |
| <span id="m-f261d6142170"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>10962–10962 | — | No extracted literal effects. |
| <span id="m-2773dcac9c01"></span><code>MainViewModel.DiscardRegistryForm()</code><br>10964–10980 | Equals @10967; RaisePropertyChanged @10971; nameof @10971 | No extracted literal effects. |
| <span id="m-2aad0f56f26f"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>10982–11109 | Equals @10993; HasPermission @10995; FirstOrDefault @11004; Trim @11009; Trim @11010; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11012; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11012; DispatchToUi @11015; SafePipelineError @11015; IsNullOrWhiteSpace @11023; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @11025; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @11025; ConfigureAwait @11034; LoadManagedCategoriesAsync @11034; LoadExpenseCategoriesAsync @11035; CaptureCategoryFormSnapshot @11045; RaisePropertyChanged @11046; nameof @11046; Trim @11064; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @11066; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @11066; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @11082; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @11082; LoadCatalogRegistryAsync @11091; ReloadCatalogAsync @11092; SafeError @11107 | No extracted literal effects. |
| <span id="m-cfc4dfded69c"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>11111–11156 | HasPermission @11121; ConfigureAwait(DeactivateCategoryCommand, bool) @11134; ExecuteAsync(DeactivateCategoryCommand, bool) @11134; ConfigureAwait(ReactivateCategoryCommand, bool) @11139; ExecuteAsync(ReactivateCategoryCommand, bool) @11139; DispatchToUi @11144; SafePipelineError @11144; ConfigureAwait @11148; LoadManagedCategoriesAsync @11148; LoadCatalogRegistryAsync @11149; ReloadCatalogAsync @11150; SafeError @11154 | No extracted literal effects. |
| <span id="m-e8196a71344e"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>11158–11198 | HasPermission @11168; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11184; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11184; DispatchToUi @11187; SafePipelineError @11187; ConfigureAwait @11191; LoadManagedCategoriesAsync @11191; LoadExpenseCategoriesAsync @11192; SafeError @11196 | No extracted literal effects. |
| <span id="m-6220364c3a00"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>11200–11300 | Clear @11203; CreateCommand @11206; ConfigureAwait @11212; ExecuteReaderAsync @11212; ReadAsync @11213; Add @11215; GetString @11217; IsDBNull @11219; GetInt32 @11223; IsNullOrWhiteSpace @11234; Equals @11238; Add @11245; Clear @11249; ExecuteReaderAsync @11254; ReadAsync @11255; GetString @11257; Where @11279; Add @11281; TryGetValue @11284; FirstOrDefault @11291; Add @11295; DispatchToUi @11298; UpdateConversionPreview @11299 | FROM store_uom_preferences @11253; FROM uoms @11208 |
| <span id="m-24a2a6400193"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>11302–11309 | OpenUnitManagerAsync @11304; FirstOrDefault @11305; Equals @11305; EditManagedUnit @11308 | No extracted literal effects. |
| <span id="m-9ebdfdd602e1"></span><code>MainViewModel.UpdateConversionPreview()</code><br>11311–11347 | IsNullOrWhiteSpace @11313; FirstOrDefault @11319; Equals @11319; TryParse @11334 | No extracted literal effects. |
| <span id="m-22a38b2e8803"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11349–11370 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11356; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11356; DispatchToUi @11359; SafePipelineError @11363; SafeError @11368 | No extracted literal effects. |
| <span id="m-7ab49a38ba7d"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11372–11385 | IsNullOrWhiteSpace @11378; TryParse @11381; CaptureUnitFormSnapshot @11383; RaisePropertyChanged @11384; nameof @11384 | No extracted literal effects. |
| <span id="m-0e17894f190c"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>11387–11449 | IsNullOrWhiteSpace @11399; Trim @11403; Trim @11404; Trim @11407; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @11408; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @11408; DispatchToUi @11411; SafePipelineError @11411; Trim @11418; Equals @11421; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @11426; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @11426; ConfigureAwait @11434; LoadManagedUnitsAsync @11434; LoadCatalogRegistryAsync @11435; CaptureUnitFormSnapshot @11442; RaisePropertyChanged @11443; nameof @11443; SafeError @11447 | No extracted literal effects. |
| <span id="m-387deb3245de"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>11451–11489 | ConfigureAwait(DeactivateUomCommand, bool) @11468; ExecuteAsync(DeactivateUomCommand, bool) @11468; ConfigureAwait(ReactivateUomCommand, bool) @11473; ExecuteAsync(ReactivateUomCommand, bool) @11473; DispatchToUi @11478; SafePipelineError @11478; ConfigureAwait @11482; LoadManagedUnitsAsync @11482; LoadCatalogRegistryAsync @11483; SafeError @11487 | No extracted literal effects. |
| <span id="m-53af539a1ffd"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>11491–11529 | CreateCommand @11496; CreateParameter @11503; ToString @11505; Add @11506; ConfigureAwait @11508; ExecuteReaderAsync @11508; Clear @11509; ReadAsync @11510; Add @11512; ParseGuidSafe @11514; GetString @11514; GetInt32 @11517; IsDBNull @11519; ToDecimal @11519; GetDouble @11519; DispatchToUi @11527; SafeError @11527 | FROM item_locations @11497 |
| <span id="m-226de319c4f0"></span><code>MainViewModel.OpenLocationsModal()</code><br>11532–11558 | CheckSessionUnlocked @11534; HasPermission @11535; LoadFacilitiesAndBinsAsync @11556 | No extracted literal effects. |
| <span id="m-8be7bb321945"></span><code>MainViewModel.OpenAddFacility()</code><br>11560–11568 | — | No extracted literal effects. |
| <span id="m-3cfd41a08161"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>11570–11579 | — | No extracted literal effects. |
| <span id="m-6a24d9dfdd93"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>11581–11640 | HasPermission @11584; IsNullOrWhiteSpace @11589; IsNullOrEmpty @11605; Trim @11607; Trim @11607; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @11608; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @11608; OpenAddFacility @11612; ConfigureAwait @11613; LoadFacilitiesAndBinsAsync @11613; DispatchToUi @11617; SafePipelineError @11617; ConfigureAwait(CreateFacilityCommand, FacilityDto) @11623; ExecuteAsync(CreateFacilityCommand, FacilityDto) @11623; SafeError @11638 | No extracted literal effects. |
| <span id="m-78ee8b66d32b"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>11642–11673 | HasPermission @11645; ConfigureAwait(DeactivateFacilityCommand, bool) @11657; ExecuteAsync(DeactivateFacilityCommand, bool) @11657; OpenAddFacility @11661; ConfigureAwait @11662; LoadFacilitiesAndBinsAsync @11662; DispatchToUi @11666; SafePipelineError @11666; SafeError @11671 | No extracted literal effects. |
| <span id="m-efcbf7f1c35d"></span><code>MainViewModel.OpenAddBin()</code><br>11675–11686 | FirstOrDefault @11685 | No extracted literal effects. |
| <span id="m-73986c76b98f"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>11688–11700 | FirstOrDefault @11698 | No extracted literal effects. |
| <span id="m-d4c49ae83341"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>11702–11777 | HasPermission @11705; IsNullOrWhiteSpace @11715; IsNullOrEmpty @11726; Trim @11731; Trim @11732; Trim @11733; Trim @11734; Trim @11735; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @11738; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @11738; OpenAddBin @11742; ConfigureAwait @11743; LoadFacilitiesAndBinsAsync @11743; DispatchToUi @11747; SafePipelineError @11747; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @11760; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @11760; SafeError @11775 | No extracted literal effects. |
| <span id="m-28cacde06fe0"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>11779–11810 | HasPermission @11782; ConfigureAwait(DeactivateLocationBinCommand, bool) @11794; ExecuteAsync(DeactivateLocationBinCommand, bool) @11794; OpenAddBin @11798; ConfigureAwait @11799; LoadFacilitiesAndBinsAsync @11799; DispatchToUi @11803; SafePipelineError @11803; SafeError @11808 | No extracted literal effects. |
| <span id="m-5a786186759c"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>11812–11865 | HasPermission @11820; IsNullOrWhiteSpace @11825; Trim @11837; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @11845; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @11845; ConfigureAwait @11853; LoadItemLocationEligibilitiesAsync @11853; DispatchToUi @11858; SafePipelineError @11858; SafeError @11863 | No extracted literal effects. |
| <span id="m-2c4b9305cc5f"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>11867–11897 | HasPermission @11870; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @11882; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @11882; ConfigureAwait @11885; LoadItemLocationEligibilitiesAsync @11885; DispatchToUi @11890; SafePipelineError @11890; SafeError @11895 | No extracted literal effects. |
| <span id="m-4ef1e4386d03"></span><code>MainViewModel.LoadCustomersAsync()</code><br>11900–11933 | NewGuid @11908; Clear @11914; Add @11915; FilterCustomers @11917; ConfigureAwait @11924; GetCustomersAsync @11924; DispatchToUi @11931; SafeError @11931 | No extracted literal effects. |
| <span id="m-0812ee373555"></span><code>MainViewModel.FilterCustomers()</code><br>11935–11948 | Clear @11937; Trim @11938; IsNullOrWhiteSpace @11939; Where @11941; Contains @11941; Contains @11942; Contains @11943; Add @11946 | No extracted literal effects. |
| <span id="m-f27c893c31ff"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>11950–11986 | CheckSessionUnlocked @11952; CreateCommand @11961; CreateParameter @11964; ToString @11966; Add @11967; ConfigureAwait @11968; ExecuteScalarAsync @11968; ToString @11969; Equals @11972; LoadPickerCandidatesAsync @11984; DispatchToUi @11985 | FROM items @11963 |
| <span id="m-237c278b044c"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>11988–12049 | ConfigureAwait @11995; GetLotCandidatesAsync @11995; DispatchToUi @11998; Clear @12000; Add @12003; ToString @12012; GetSerialCandidatesAsync @12020; Clear @12025; Add @12028; ToString @12037 | No extracted literal effects. |
| <span id="m-7e1288f9b0ca"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>12051–12057 | Clear @12054; Clear @12055 | No extracted literal effects. |
| <span id="m-3bcf034acd44"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>12059–12118 | FirstOrDefault @12072; ConfigureAwait(SelectLotForCartLineCommand, bool) @12080; ExecuteAsync(SelectLotForCartLineCommand, bool) @12080; DispatchToUi @12083; SafePipelineError @12083; ToList @12089; Where @12089; ConfigureAwait(SelectSerialForCartLineCommand, bool) @12099; ExecuteAsync(SelectSerialForCartLineCommand, bool) @12099; SafeError @12116 | No extracted literal effects. |
| <span id="m-d8ffb4a3a1f6"></span><code>MainViewModel.OpenCustomerChooser()</code><br>12120–12128 | CheckSessionUnlocked @12122; Clear @12125; LoadCustomersAsync @12126 | No extracted literal effects. |
| <span id="m-8552c4ffeaef"></span><code>MainViewModel.CloseCustomerChooser()</code><br>12130–12133 | — | No extracted literal effects. |
| <span id="m-dd9fce5d3fb3"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>12135–12152 | SaveDurableCartAsync @12145; IsNullOrWhiteSpace @12149; ToString @12149; NewGuid @12149; RecordSuccessfulSearchUseAsync @12150; FromGuid @12150 | No extracted literal effects. |
| <span id="m-0de9267bfbe1"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>12154–12163 | SaveDurableCartAsync @12162 | No extracted literal effects. |
| <span id="m-ecc30c789edb"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>12165–12210 | CheckSessionUnlocked @12167; IndexOf @12171; SelectWalkInCustomer @12177; FilterCustomers @12179; ConfigureAwait(DeactivateCustomerCommand, bool) @12191; ExecuteAsync(DeactivateCustomerCommand, bool) @12191; ConfigureAwait @12198; LoadCustomersAsync @12198; DispatchToUi @12203; SafePipelineError @12203; SafeError @12208 | No extracted literal effects. |
| <span id="m-714a6223f0d7"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>12339–12378 | Add @12345; NewGuid @12346; RefreshManufacturingTablesAsync @12360; ConfigureAwait @12368; GetKitsAsync @12368; Clear @12369; Add @12370; DispatchToUi @12376; SafeError @12376 | No extracted literal effects. |
| <span id="m-03efa1b8708a"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12382–12398 | CheckSessionUnlocked @12384; SetProductionActionMode @12386; FirstOrDefault @12391; LoadProductionIngredientLotsAsync @12396; TakeProductionSnapshot @12397 | No extracted literal effects. |
| <span id="m-181660bfebd7"></span><code>MainViewModel.CloseProductionModal()</code><br>12400–12414 | — | No extracted literal effects. |
| <span id="m-83daa243f764"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>12416–12515 | ExecuteExistingProductionAsync @12419; Resolve @12441; NewGuid @12444; ToUpperInvariant @12446; ToString @12446; Insert @12464; IsNullOrWhiteSpace @12486; Trim @12486; ToDictionary @12488; Where @12488; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @12492; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @12492; DispatchToUi @12495; SafePipelineError @12495; RecordSuccessfulSearchUseAsync @12502; FromGuid @12502; ConfigureAwait @12505; LoadManufacturingDataAsync @12505; LoadInventoryAsync @12506; SafeError @12512 | No extracted literal effects. |
| <span id="m-3dd01fd3affe"></span><code>MainViewModel.CloseXReportModal()</code><br>12614–12617 | — | No extracted literal effects. |
| <span id="m-a1dd79bf979a"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>12619–12649 | CheckSessionUnlocked @12621; Clear @12639; Where @12640; GetUnlockCandidates @12640; Equals @12641; Add @12645 | No extracted literal effects. |
| <span id="m-8a68f8b4acb5"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>12651–12655 | — | No extracted literal effects. |
| <span id="m-40b844ef89da"></span><code>MainViewModel.CloseZReportModal()</code><br>12657–12660 | — | No extracted literal effects. |
| <span id="m-dca3f3d72b25"></span><code>MainViewModel.LoadReportDataAsync()</code><br>12662–12779 | ToString @12682; DispatchToUi @12698; ConfigureAwait @12726; ExecuteAsync @12726; Join @12728; Select(string, Money) @12728; InvoiceMoney @12728; ToDecimal @12731; ToDecimal @12732; ToDecimal @12733; ToDecimal @12734; ToDecimal @12736; ToDecimal @12738; ToDecimal @12739; ToDecimal @12740; ToDecimal @12741; ToDecimal @12742; ToUpperInvariant @12744; ToString @12744; ToString @12746; ToString @12747; Sum @12753; ToDecimal @12753; ToDecimal @12756; Add @12758; Format @12763; SafeError @12771 | No extracted literal effects. |
| <span id="m-5df73c48cb80"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>12781–12870 | CheckSessionUnlocked @12784; IsNullOrWhiteSpace @12801; AuthenticateSelectedUser @12809; Trim @12811; Round @12820; Trim @12824; ConfigureAwait(CloseShiftCommand, Shift) @12828; ExecuteAsync(CloseShiftCommand, Shift) @12828; DispatchToUi @12846; SafePipelineError @12846; ConfigureAwait @12853; ExecuteAsync @12853; SetActiveCashier @12857; RefreshUnlockCandidates @12858; RaisePropertyChanged @12859; nameof @12859; LoadReportDataAsync @12863; LoadTeamsStaffAsync @12864; SafeError @12868 | No extracted literal effects. |
| <span id="m-54081609d3e6"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>12872–12948 | FirstOrDefault @12874; CreateCommand @12881; CreateParameter @12896; ToString @12898; Add @12899; ExecuteReader @12901; Read @12902; Parse @12904; GetString @12904; GetInt64 @12907; Pow @12909; IsDBNull @12911; TryParse @12917; GetInt32 @12918; Add @12941 | FROM barcodes @12882; FROM items @12882; JOIN barcodes @12882; JOIN product_categories @12882 |
| <span id="m-68f270790ae5"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>12950–13066 | IsNullOrWhiteSpace @12952; Trim @12955; ToList @12958; Where @12958; IsNullOrEmpty @12959; Equals @12959; ToString @12961; AddToCart @12967; CreateCommand @12983; CreateParameter @13001; Add @13004; ExecuteReader @13006; Read @13008; Parse @13010; GetString @13010; ContainsKey @13011; GetInt64 @13015; Pow @13017; IsDBNull @13019; TryParse @13025; GetInt32 @13026; First @13055; Add @13056 | FROM barcodes @12984; FROM items @12984; JOIN barcodes @12984; JOIN product_categories @12984 |
| <span id="m-328f1bcfe53c"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>13068–13111 | IsNullOrWhiteSpace @13070; Trim @13073; AppendReceiveSerialScan @13079; TryAddUniqueExactMatchToCart @13085; Clear @13087; ToList @13092; Where @13092; Equals @13092; AddToCart @13095 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml</code> · 6169 lines · SHA-256 <code>d0811699fd5a980cd8d3d9bf56f1436d928183e238054dc1908ea712d8fe2baa</code>.
