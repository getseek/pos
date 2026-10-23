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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 13,041 lines.

SHA-256: <code>ca5b63e5ad55c91a9ec5fadab0d67cdbf54b3c81810c8658cf695f7d87f672ba</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 8668).

<details markdown>
<summary>Methods, calls, table effects and failures (254)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4d3c549b9d46"></span><code>MainViewModel.RefreshCurrentTime()</code><br>121–121 | RaisePropertyChanged @121; nameof @121 | No extracted literal effects. |
| <span id="m-47378cde4176"></span><code>MainViewModel.SetStatusNotificationOnUi(string)</code><br>391–404 | RaiseAndSetIfChanged @393; IsNullOrWhiteSpace @394; Insert @396; RemoveAt @397; RaisePropertyChanged @398; nameof @398; Stop @401; Start @403 | No extracted literal effects. |
| <span id="m-fa69ff5d121c"></span><code>MainViewModel.ClearNotifications()</code><br>426–433 | Stop @428; Clear @430; RaisePropertyChanged @431; nameof @431; RaiseAndSetIfChanged @432 | No extracted literal effects. |
| <span id="m-1aafdc317eca"></span><code>MainViewModel.CycleInventoryLifecycleStatusScope()</code><br>677–682 | — | No extracted literal effects. |
| <span id="m-99c6f60a0157"></span><code>MainViewModel.IsLockScreenLockedOut(int)</code><br>1196–1212 | Ceiling @1203 | No extracted literal effects. |
| <span id="m-c83857be5fd1"></span><code>MainViewModel.RefreshUnlockCandidates()</code><br>1254–1279 | GetUnlockCandidates @1257; Clear @1260; Add @1263; Any @1265; CheckAccess @1271; action @1273; Post @1277 | No extracted literal effects. |
| <span id="m-157529f90012"></span><code>MainViewModel.UpdateReceiveKitBreakdownAsync()</code><br>1637–1657 | GetValueOrDefault @1645; ConfigureAwait @1650; BuildBreakdownSummaryAsync @1650 | No extracted literal effects. |
| <span id="m-41fa84ec3c34"></span><code>MainViewModel.UpdateCartKitBreakdownAsync(OrderItem)</code><br>1659–1671 | ConfigureAwait @1664; BuildBreakdownSummaryAsync @1664 | No extracted literal effects. |
| <span id="m-8ef63b94ba90"></span><code>MainViewModel.OnProductPricingDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>2096–2115 | RaisePropertyChanged @2098; nameof @2098; RecomputeProductPricingPreview @2114 | No extracted literal effects. |
| <span id="m-42b3b20aa310"></span><code>MainViewModel.RecomputeProductPricingPreview()</code><br>2124–2174 | Clear @2126; RaisePropertyChanged @2127; nameof @2127; ToMinorUnits @2136; Parse @2141; TryParse @2145; Equals @2159; Increment @2162; Localize @2163; ToArray @2165; RecomputeKitPricingPreviewAsync @2166; ResolveSelectedProductSaleUnitFactor @2171; Round @2172; RebuildProductPricingPreview @2173 | No extracted literal effects. |
| <span id="m-4bfd6bde6cfe"></span><code>MainViewModel.RecomputeKitPricingPreviewAsync(long,string,string,decimal,string,long,decimal,IReadOnlyList&lt;KitComponentDraftItem&gt;)</code><br>2176–2246 | ConfigureAwait @2180; WaitAsync @2180; Read @2183; DispatchToUi @2187; SetProductPricingPreviewNotice @2187; CalculateItemOrKitAsync @2201; ResolveSelectedProductSaleUnitFactor @2225; Round @2226; RebuildProductPricingPreview @2230; Release @2244 | No extracted literal effects. |
| <span id="m-d2e52490d546"></span><code>MainViewModel.SetProductPricingPreviewNotice(string)</code><br>2248–2252 | Localize @2250; RaisePropertyChanged @2251; nameof @2251 | No extracted literal effects. |
| <span id="m-ae65052e0be9"></span><code>MainViewModel.RebuildProductPricingPreview(long,string,decimal,string,long,decimal)</code><br>2254–2318 | Clear @2257; RaisePropertyChanged @2259; nameof @2259; Equals @2260; SetProductPricingPreviewNotice @2262; ParsePricingMethod @2266; ParseRoundingRule @2267; IsRoundingRuleCompatible @2268; TryConvertRoundingIncrement @2275; ToMinorUnits @2282; ResolveEffectiveBasePrice @2283; ToList @2287; OrderBy @2287; Where @2287; FirstOrDefault @2294; TryParse @2305; ToString @2306; ResolveTierPrice @2309; Add @2311; Format @2313; ToDisplayAmount @2313; FirstOrDefault @2314 | No extracted literal effects. |
| <span id="m-5e2807d197ad"></span><code>MainViewModel.ResolveSelectedProductSaleUnitFactor()</code><br>2372–2387 | FirstOrDefault @2375; Equals @2375; TryParse @2379 | No extracted literal effects. |
| <span id="m-4a7383fd2f00"></span><code>MainViewModel.ExactMinorToCurrency(decimal)</code><br>2395–2396 | ScalingFactor @2396; Clamp @2396 | No extracted literal effects. |
| <span id="m-d16ca03db6d1"></span><code>MainViewModel.BuildCostSourcesTooltip(long,long,long,long?,string,DateTime?)</code><br>2453–2473 | Format @2461; ToDecimal @2462; Localize @2465; Format @2465; ToLocalTime @2467; Join @2472 | No extracted literal effects. |
| <span id="m-df1dea762ad3"></span><code>MainViewModel.AddKitComponent()</code><br>2633–2670 | IsNullOrWhiteSpace @2648; FirstOrDefault @2650; Equals @2651; Add @2658; RaisePropertyChanged @2669; nameof @2669 | No extracted literal effects. |
| <span id="m-6dd0a88ae9bd"></span><code>MainViewModel.RemoveKitComponent(KitComponentDraftItem?)</code><br>2672–2679 | Remove @2676; RaisePropertyChanged @2677; nameof @2677 | No extracted literal effects. |
| <span id="m-10b55ea59b23"></span><code>MainViewModel.RefreshVirtualKitAvailability()</code><br>2690–2703 | Increment @2692; ToArray @2699; Select @2699; LoadVirtualKitAvailabilityAsync @2702 | No extracted literal effects. |
| <span id="m-67567dd12ab2"></span><code>MainViewModel.LoadVirtualKitAvailabilityAsync(long,IReadOnlyList&lt;KitComponentInput&gt;)</code><br>2705–2745 | ConfigureAwait @2709; GetKitAvailabilityAsync @2709; DispatchToUi @2711; Read @2713; Localize @2716; Max @2725; ResolveSelectedProductSaleUnitFactor @2725; GetValueOrDefault @2726; Clamp @2727; Pow @2728; Floor @2729; Format @2731; ToString @2733 | No extracted literal effects. |
| <span id="m-f1489a6cfc6c"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3587–3595 | IsNullOrWhiteSpace @3589 | No extracted literal effects. |
| <span id="m-da4c6e2ff7f1"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3597–3608 | Load @3599; IsNullOrWhiteSpace @3603; Resolve @3605; Apply @3607 | No extracted literal effects. |
| <span id="m-44f87c41771a"></span><code>MainViewModel.OpenImport()</code><br>3637–3645 | CheckSessionUnlocked @3639; Increment @3641; ResetInventoryImport @3642; Invoke @3644 | No extracted literal effects. |
| <span id="m-e125d430b500"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3647–3708 | Increment @3650; ResetInventoryImport @3655; IsNullOrWhiteSpace @3660; Exists @3660; FinishFailedImport @3662; ConfigureAwait @3674; ReadAllBytesAsync @3674; ToHexString @3675; HashData @3675; TemplateContextAsync @3679; Run @3680; Read @3680; ValidateInventoryAsync @3681; CompletedWorkbook @3682; DispatchToUi @3689; ReferenceEquals @3691; Add @3692; Localize @3693; SetImportReviewRows @3697; RaisePropertyChanged @3698; nameof @3698; ReportException @3704 | No extracted literal effects. |
| <span id="m-356914adc286"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3710–3764 | IsCurrentImportAttempt @3726; ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3740; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3740; ConfigureAwait @3744; RecoverImportOutcomeAsync @3744; Localize @3747; DispatchToUi @3748; FinishImportAttempt @3748; LoadInventoryAsync @3749; ReportException @3750; ReportError @3754; FinishFailedImport @3755; ImportCommandIssue @3755 | No extracted literal effects. |
| <span id="m-6fee2431d5c9"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3776–3786 | Report @3778; DispatchToUi @3779; Insert @3781 | No extracted literal effects. |
| <span id="m-e4e8449caa4e"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3788–3792 | RaisePropertyChanged @3791; nameof @3791 | No extracted literal effects. |
| <span id="m-e2bcbf48fa71"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3794–3797 | ReportError @3796 | No extracted literal effects. |
| <span id="m-a00162cc29c6"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3803–3808 | ReportError @3806 | No extracted literal effects. |
| <span id="m-6e0a886f2ebe"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3817–3823 | IsNullOrWhiteSpace @3819; Trim @3819; ReportError @3821 | No extracted literal effects. |
| <span id="m-ad17a22186bd"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3825–3828 | DispatchToUi @3827; Insert @3827 | No extracted literal effects. |
| <span id="m-629e6f1fd481"></span><code>MainViewModel.DispatchToUi(Action)</code><br>3834–3848 | CheckAccess @3836; action @3838; GetResult @3846; GetAwaiter @3846; InvokeAsync @3846 | No extracted literal effects. |
| <span id="m-31a504196f66"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4508–4573 | Register @4510; Execute @4510; Execute @4511; Execute @4512; Execute @4513; Execute @4518; Execute @4519; Execute @4520; Execute @4521; Execute @4522; Execute @4523; Execute @4524; Execute @4525; Execute @4526; Execute @4527; Execute @4528; Execute @4529; Execute @4530; Execute @4531; Execute @4532; Execute @4533; Execute @4534; Execute @4535; Execute @4536; Execute @4537; Execute @4538; Execute @4539; Execute @4540; Execute @4541; Execute @4542; Execute @4543; Execute @4544; Execute @4545; Execute @4546; Execute @4547; Execute @4548; Execute @4549; Execute @4551; Execute @4552; RequestClosePersonForm @4553; KeepEditingPersonForm @4554; CloseSalaryMonthDetailModal @4555; CloseSalaryPaymentModal @4556; CloseSalaryAdjustmentModal @4557; CloseSalaryFinalizeModal @4558; RequestCloseExpenseForm @4559; KeepEditingExpenseForm @4560; CloseExpenseCategoryModal @4561; CloseExpensePaymentModal @4562; CloseExpenseDetailModal @4563; ClosePaymentReturnModal @4564; CloseWasteExpenseConfirmation @4565; InitializeSalaryTables @4570; InitializeExpensesTables @4571; InitializeTeamsCommands @4572 | No extracted literal effects. |
| <span id="m-752ebadfa80c"></span><code>MainViewModel.CreateDemo()</code><br>4575–4582 | SetActiveCashier @4578; Parse @4578; RefreshUnlockCandidates @4580 | No extracted literal effects. |
| <span id="m-182beb9af2b8"></span><code>MainViewModel.CreateInitializing()</code><br>4584–4592 | — | No extracted literal effects. |
| <span id="m-4ac18dd1ad12"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4594–4604 | — | No extracted literal effects. |
| <span id="m-40d336b8faa4"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4606–4624 | ConfigureDiagnosticsWorkspace @4620; ResolveDiagnosticsWorkspace @4620; ApplyPersistedState @4621; RefreshUnlockCandidates @4622 | No extracted literal effects. |
| <span id="m-8bbddaa5b496"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4626–4654 | CheckSessionUnlocked @4628; HasPermission @4629; Equals @4640; GetFileNameWithoutExtension @4640; GetEntryAssembly @4642; Add @4644; Start @4647; ReportException @4652 | No extracted literal effects. |
| <span id="m-41155419f1fe"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4656–4679 | CheckSessionUnlocked @4658; HasPermission @4659; Equals @4669; GetFileNameWithoutExtension @4669; Add @4670; GetEntryAssembly @4670; Start @4672; ReportException @4677 | No extracted literal effects. |
| <span id="m-9f211085e206"></span><code>MainViewModel.Dispose()</code><br>4681–4702 | ClearImportResults @4684; Increment @4685; ResetFinancialWorkspace @4687; Dispose @4688; Stop @4689; CancelBatchPricingPreviewExpiry @4692; Dispose @4693; Dispose @4694; DisposeSearchStates @4700; SuppressFinalize @4701 | No extracted literal effects. |
| <span id="m-293152c7a140"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4704–4708 | Stop @4706 | No extracted literal effects. |
| <span id="m-5f5599410746"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4710–4748 | Clear @4720; Clear @4721; Clear @4722; Clear @4723; Clear @4724; Clear @4725; Clear @4726; Clear @4727; Clear @4728; Clear @4729 | No extracted literal effects. |
| <span id="m-bfc64abad527"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4750–4853 | RaisePropertyChanged @4764; nameof @4764; Clear @4766; Clear @4767; Clear @4768; CreateCommand @4775; ExecuteReader @4777; Read @4778; TryParse @4780; GetString @4780; Add @4781; Add @4789; GroupBy @4790; Count @4792; Contains @4797; Add @4814; Add @4815; SetActiveCashier @4823; ToString @4827; ToString @4830; ToLocalTime @4830; NotifyTotalsChanged @4852 | FROM item_kits @4776 |
| <span id="m-195fe269848e"></span><code>MainViewModel.InitializeDemoData()</code><br>4855–4935 | Add @4861; Add @4880; Add @4893; Add @4897; Add @4902; Add @4908; ApplyActivityFilter @4914; Add @4917; ApplyInventoryFilter @4926; Add @4929; Parse @4929; NotifyTotalsChanged @4934 | No extracted literal effects. |
| <span id="m-086f32d5a6c7"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>4937–4950 | — | No extracted literal effects. |
| <span id="m-821db0343f99"></span><code>MainViewModel.SelectMenu(string)</code><br>4952–5023 | CheckSessionUnlocked @4954; NormalizeMenuKey @4958; LoadInvoicesAsync @4964; LoadCommercialAsync @4965; LoadActivityInvoicesAsync @4972; LoadTeamsStaffAsync @4975; LoadCatalogRegistryAsync @4976; UpdateDemoSeedingAvailabilityAsync @4979; UpdateReceiptDesignPreview @4982; RefreshDiagnosticsAsync @4983; LoadPriceLevelSettingsAsync @4984; LoadInventoryAsync @4987; LoadPriceProposalsAsync @4989; LoadReportDataAsync @4992; LoadFinancialRegisterAsync @4993; LoadCustomersAsync @4996; LoadSuppliersAsync @4997; LoadThirdPartiesAsync @4998; LoadManufacturingDataAsync @5003; LoadManagedUnitsAsync @5011; LoadManagedCategoriesAsync @5014; LoadSalaryWorkspaceAsync @5017; LoadExpensesWorkspaceAsync @5020 | No extracted literal effects. |
| <span id="m-ebf4c22b081f"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>5025–5044 | — | No extracted literal effects. |
| <span id="m-4ed0cc3e3292"></span><code>MainViewModel.LogOut()</code><br>5046–5067 | Clear @5048; RaisePropertyChanged @5051; nameof @5051; ClearNotifications @5053; ResetCashReview @5057; Lock @5060; RefreshUnlockCandidates @5065; UpdateDemoSeedingAvailabilityAsync @5066 | No extracted literal effects. |
| <span id="m-4f70bb659a1c"></span><code>MainViewModel.UnlockSession()</code><br>5069–5072 | UnlockSession @5071 | No extracted literal effects. |
| <span id="m-5f4962433ce9"></span><code>MainViewModel.UnlockSession(string?)</code><br>5074–5173 | IsLockScreenLockedOut @5082; IsNullOrWhiteSpace @5098; AuthenticateSelectedUser @5107; Lock @5112; AddSeconds @5118; AddMinutes @5135; Initialize @5154; Unlock @5155; Any @5159; Equals @5159; RaisePropertyChanged @5160; nameof @5160; LoadActivityInvoicesAsync @5164; LoadTrackOrdersAsync @5165; UpdateDemoSeedingAvailabilityAsync @5166; StartAutomaticDemoDatasetLoadAsync @5167 | No extracted literal effects. |
| <span id="m-2c8cf0eb2c8e"></span><code>MainViewModel.PowerAction()</code><br>5175–5181 | CheckSessionUnlocked @5177 | No extracted literal effects. |
| <span id="m-db80454b4fb3"></span><code>MainViewModel.CycleTable()</code><br>5183–5189 | CheckSessionUnlocked @5185 | No extracted literal effects. |
| <span id="m-05e23db8c48c"></span><code>MainViewModel.CycleDiningType()</code><br>5191–5197 | CheckSessionUnlocked @5193 | No extracted literal effects. |
| <span id="m-b887e27fd6be"></span><code>MainViewModel.CycleCustomer()</code><br>5199–5202 | OpenCustomerChooser @5201 | No extracted literal effects. |
| <span id="m-91fe1abaf36f"></span><code>MainViewModel.OpenPromoDialog()</code><br>5204–5219 | CheckSessionUnlocked @5206; IsNullOrWhiteSpace @5213; RaisePropertyChanged @5217; nameof @5217 | No extracted literal effects. |
| <span id="m-b8173af134c0"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5221–5290 | CheckSessionUnlocked @5223; ToLowerInvariant @5236; Trim @5236; IsNullOrWhiteSpace @5243; Trim @5243; ToList @5251; Select @5251; ToMinorUnits @5255; Equals @5271; Calculate @5275; NotifyTotalsChanged @5287; ConfigureAwait @5289; SaveDurableCartAsync @5289 | No extracted literal effects. |
| <span id="m-efd7d5a1d58a"></span><code>MainViewModel.TogglePromo()</code><br>5292–5309 | CheckSessionUnlocked @5294; RemovePromo @5303; OpenPromoDialog @5307 | No extracted literal effects. |
| <span id="m-d5eae394278a"></span><code>MainViewModel.RemovePromo()</code><br>5311–5321 | NotifyTotalsChanged @5318; SaveDurableCartAsync @5320 | No extracted literal effects. |
| <span id="m-1cb1152b8404"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5323–5334 | CheckSessionUnlocked @5325; NotifyTotalsChanged @5331; ConfigureAwait @5333; SaveDurableCartAsync @5333 | No extracted literal effects. |
| <span id="m-d53d1f13afaf"></span><code>MainViewModel.CancelPromoDialog()</code><br>5336–5340 | — | No extracted literal effects. |
| <span id="m-4f4ae7e8294c"></span><code>MainViewModel.RecalculateCart()</code><br>5342–5396 | ToMinorUnits @5358; Add @5359; Equals @5380; Calculate @5384; ToDictionary @5387; TryGetValue @5390 | No extracted literal effects. |
| <span id="m-c3f855f34b30"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5398–5405 | CheckSessionUnlocked @5400; ResetCashReview @5401 | No extracted literal effects. |
| <span id="m-5b382587e03d"></span><code>MainViewModel.SelectCategory(CategoryItem)</code><br>5407–5415 | CheckSessionUnlocked @5409; ApplyFilter @5413 | No extracted literal effects. |
| <span id="m-485f528e75df"></span><code>MainViewModel.ApplyFilter()</code><br>5417–5439 | FirstOrDefault @5419; Clear @5422; AsEnumerable @5423; Where @5427; Equals @5427; IsNullOrWhiteSpace @5430; Contains @5432; Add @5437 | No extracted literal effects. |
| <span id="m-21c2a48ffb31"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5441–5441 | AddToCart @5441 | No extracted literal effects. |
| <span id="m-d3a3fde20aff"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5443–5487 | CheckSessionUnlocked @5445; ResetCashReview @5446; ResolveProductSaleUnitFactor @5449; Round @5456; FirstOrDefault @5457; UpdateCartKitBreakdownAsync @5466; Add @5478; NotifyTotalsChanged @5481; SaveDurableCartAsync @5483; IsNullOrWhiteSpace @5485; ToString @5485; NewGuid @5485; RecordSuccessfulSearchUseAsync @5486; FromGuid @5486 | No extracted literal effects. |
| <span id="m-94d318dc9c91"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5489–5502 | CheckSessionUnlocked @5491; ResetCashReview @5492; UpdateCartKitBreakdownAsync @5499; NotifyTotalsChanged @5500; SaveDurableCartAsync @5501 | No extracted literal effects. |
| <span id="m-e4d3940d0c9b"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5504–5519 | CheckSessionUnlocked @5506; ResetCashReview @5507; UpdateCartKitBreakdownAsync @5511; Remove @5515; NotifyTotalsChanged @5517; SaveDurableCartAsync @5518 | No extracted literal effects. |
| <span id="m-27f8198781ca"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5521–5527 | ConfigureAwait @5524; LoadAsync @5524; RefreshSavedPaymentImages @5525; CancelManualPaymentSettings @5526 | No extracted literal effects. |
| <span id="m-747e42310962"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5529–5558 | ValidImage @5536; CreatePaymentBitmap @5541; Dispose @5544; RaisePropertyChanged @5556; nameof @5556 | No extracted literal effects. |
| <span id="m-e562a3dcc6f6"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5560–5576 | Dispose @5570; CreatePaymentBitmap @5572; RaisePropertyChanged @5574; nameof @5574 | No extracted literal effects. |
| <span id="m-cfe37d37aef1"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5578–5582 | — | No extracted literal effects. |
| <span id="m-137ffa1a940d"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5584–5592 | Dispose @5586; CreatePaymentBitmap @5588; RaisePropertyChanged @5590; nameof @5590 | No extracted literal effects. |
| <span id="m-2c28ea806a51"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5594–5613 | ConfigureAwait @5603; ExecuteAsync @5603; DispatchToUi @5606; SafePipelineError @5606; LoadAsync @5609; RefreshSavedPaymentImages @5610; CancelManualPaymentSettings @5611 | No extracted literal effects. |
| <span id="m-f22f3ffdac54"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5615–5634 | IsNullOrWhiteSpace @5619; Trim @5620; ToMinorUnits @5626; ConfigureAwait @5632; PlaceOrderAsync @5632 | No extracted literal effects. |
| <span id="m-be022c84a055"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5636–5648 | PlaceOrderInternalAsync @5642 | No extracted literal effects. |
| <span id="m-537a509abcf3"></span><code>MainViewModel.PlaceOrderInternalAsync()</code><br>5650–5851 | Localize @5654; ExecuteDemoPlaceOrder @5660; ConfigureAwait @5686; SaveDurableCartAsync @5686; ToMinorUnits @5694; Trim @5696; Equals @5707; Equals @5714; ResetCashReview @5716; Max @5774; Add @5779; ConfigureAwait(TakePaymentCommand, SalesInvoice) @5797; ExecuteAsync(TakePaymentCommand, SalesInvoice) @5797; Format @5809; ToDecimal @5809; DispatchToUi @5811; Clear @5815; NewGuid @5824; NotifyTotalsChanged @5825; LoadActivityInvoicesAsync @5832; OpenStaleCartPriceReviewAsync @5837; RequestElevationForCheckout @5839; SafePipelineError @5843; SafeError @5849 | No extracted literal effects. |
| <span id="m-831369f6cfec"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>5853–5885 | DispatchToUi @5857; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5860; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5860; SafePipelineError @5865; ToArray @5869; Select @5869; Where @5869; FormatCartReviewMoney @5873; Clear @5880; Add @5881 | No extracted literal effects. |
| <span id="m-6211272711be"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>5887–5892 | ScalingFactor @5889; Format @5891; Equals @5891 | No extracted literal effects. |
| <span id="m-8c8239fe58c5"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>5894–5925 | CheckSessionUnlocked @5896; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5898; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5898; DispatchToUi @5903; SafePipelineError @5903; ConfigureAwait @5904; OpenStaleCartPriceReviewAsync @5904; FirstOrDefault @5911; ScalingFactor @5914; ResetCashReview @5918; Clear @5921; NotifyTotalsChanged @5922 | No extracted literal effects. |
| <span id="m-e92914301b26"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>5927–5934 | Clear @5931; ResetCashReview @5932 | No extracted literal effects. |
| <span id="m-a1c3ac2f23e3"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>5936–5962 | CheckSessionUnlocked @5938; ResetCashReview @5945; ToMinorUnits @5956; ConfigureAwait @5961; PlaceOrderAsync @5961 | No extracted literal effects. |
| <span id="m-6a7bc5b99e0e"></span><code>MainViewModel.CancelCashReview()</code><br>5964–5968 | ResetCashReview @5966 | No extracted literal effects. |
| <span id="m-44f1365a9d44"></span><code>MainViewModel.ResetCashReview()</code><br>5970–5979 | — | No extracted literal effects. |
| <span id="m-47c70e487f7a"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>5981–6000 | RaisePropertyChanged @5992; nameof @5992; Clear @5995; ResetCashReview @5996; NotifyTotalsChanged @5997 | No extracted literal effects. |
| <span id="m-bda657e6bae9"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>6002–6067 | ConfigureAwait @6006; WaitAsync @6006; ClearActiveCartAsync @6011; ToMinorUnits @6021; Add @6022; ToUpperInvariant @6025; ToString @6025; IsNullOrWhiteSpace @6028; SaveActiveCartAsync @6041; DispatchToUi @6060; SafeError @6060; Release @6065 | No extracted literal effects. |
| <span id="m-a31e279b68a8"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>6069–6124 | ConfigureAwait @6075; GetActiveCartAsync @6075; Clear @6087; FirstOrDefault @6090; ToDecimal @6094; Add @6100; NotifyTotalsChanged @6117 | No extracted literal effects. |
| <span id="m-c3a45b7fe0ec"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>6126–6203 | ApplyPagedResult @6130; ToList @6131; ApplyActivityFilter @6135; HasPermission @6140; ConfigureAwait @6147; GetPagedActivityInvoicesAsync @6147; ToPageRequest @6150; ToDecimal @6156; Add @6157; ToString @6162; ToLocalTime @6162; DispatchToUi @6181; Clear @6183; Add @6186; SafeError @6200 | No extracted literal effects. |
| <span id="m-8a4577ff8ae4"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>6205–6282 | HasPermission @6210; ConfigureAwait @6217; GetActiveOrdersAsync @6217; Clear @6218; ToDecimal @6222; Join @6256; Select @6256; Add @6258; ToString @6273; ToLocalTime @6273 | No extracted literal effects. |
| <span id="m-2ee438f8293f"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6284–6311 | CheckSessionUnlocked @6286; Clear @6289; ConfigureAwait @6295; GetOrderByIdAsync @6295; Add @6300; DispatchToUi @6306; SafeError @6306 | No extracted literal effects. |
| <span id="m-25e1c719b0b0"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6313–6318 | Clear @6317 | No extracted literal effects. |
| <span id="m-3715ae10db76"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6320–6353 | CheckSessionUnlocked @6322; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6338; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6338; ConfigureAwait @6347; LoadTrackOrdersAsync @6347; DispatchToUi @6351; SafePipelineError @6351 | No extracted literal effects. |
| <span id="m-bc12b897f161"></span><code>MainViewModel.MarkReadyAsync()</code><br>6355–6388 | CheckSessionUnlocked @6357; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6373; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6373; ConfigureAwait @6382; LoadTrackOrdersAsync @6382; DispatchToUi @6386; SafePipelineError @6386 | No extracted literal effects. |
| <span id="m-9e19f3dec627"></span><code>MainViewModel.MarkServedAsync()</code><br>6390–6423 | CheckSessionUnlocked @6392; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6408; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6408; ConfigureAwait @6417; LoadTrackOrdersAsync @6417; DispatchToUi @6421; SafePipelineError @6421 | No extracted literal effects. |
| <span id="m-62336b24d813"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6425–6453 | CheckSessionUnlocked @6427; Remove @6431; CloseOrderDetailsModal @6432; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6441; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6441; ConfigureAwait @6447; LoadTrackOrdersAsync @6447; DispatchToUi @6451; SafePipelineError @6451 | No extracted literal effects. |
| <span id="m-95970de57f32"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6455–6551 | CheckSessionUnlocked @6457; CloseOrderDetailsModal @6463; ConfigureAwait @6470; GetOrderByIdAsync @6470; Zero @6492; NewGuid @6498; ToList @6501; Select @6501; ToUpperInvariant @6504; ToString @6504; SaveActiveCartAsync @6513; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6529; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6529; DispatchToUi @6532; SafePipelineError @6532; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6538; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6538; LoadTrackOrdersAsync @6544; LoadActivityInvoicesAsync @6545 | No extracted literal effects. |
| <span id="m-8abdc46d841b"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6553–6560 | CheckSessionUnlocked @6555 | No extracted literal effects. |
| <span id="m-8d6f1c391752"></span><code>MainViewModel.FilterActivity(string)</code><br>6579–6585 | CheckSessionUnlocked @6581; ApplyActivityFilter @6583 | No extracted literal effects. |
| <span id="m-b491f01f1095"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6587–6626 | Clear @6589; AsEnumerable @6590; Where @6595; IsNullOrWhiteSpace @6598; Trim @6600; Contains @6602; Contains @6603; Contains @6604; IsNullOrEmpty @6608; Equals @6610; ToList @6614; Add @6616; ApplyPagedResult @6620 | No extracted literal effects. |
| <span id="m-55245f46f3bb"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6628–6664 | CheckSessionUnlocked @6630; ConfigureAwait(QueueReceiptReprintCommand, string) @6650; ExecuteAsync(QueueReceiptReprintCommand, string) @6650; IsNullOrWhiteSpace @6651; ReportError @6653; RefreshOutputStatusAsync @6658; DispatchToUi @6662; SafeError @6662 | No extracted literal effects. |
| <span id="m-f369c135f16f"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6666–6709 | RefreshOutputPrinterQueues @6671; ReadAsync @6672; Equals @6679; IsNullOrWhiteSpace @6679; TryReadGeometry @6681; ComputeCapabilityFingerprint @6685; ConfigureAwait @6689; InvalidateThermalVerificationAsync @6689; LoadCashFinancialSettingsAsync @6701; LoadReceiptDesignAsync @6702; RefreshOutputStatusAsync @6703; DispatchToUi @6707; SafeError @6707 | No extracted literal effects. |
| <span id="m-848d0f14319c"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6711–6737 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6724; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6724; ReportError @6727; LoadOutputDevicesAsync @6730; DispatchToUi @6735; SafeError @6735 | No extracted literal effects. |
| <span id="m-2ffca5ce6768"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6739–6812 | Equals @6753; IsNullOrWhiteSpace @6758; IsWindows @6763; TryReadGeometry @6768; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6785; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6785; ReportError @6788; Render @6791; ToString @6792; ConfigureAwait @6793; Run @6793; Send @6793; ComputeCapabilityFingerprint @6794; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @6795; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @6795; RefreshOutputStatusAsync @6806; DispatchToUi @6810; SafeError @6810 | No extracted literal effects. |
| <span id="m-3d1f13285676"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>6814–6851 | IsWindows @6828; IsNullOrWhiteSpace @6828; TryReadGeometry @6830; ComputeCapabilityFingerprint @6834; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @6835; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @6835; ReportError @6839; ConfigureAwait @6845; RefreshOutputStatusAsync @6845; DispatchToUi @6849; SafeError @6849 | InvalidOperationException @6829; InvalidOperationException @6833 |
| <span id="m-ce4e46a2f044"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>6853–6890 | CreateCommand @6858; ConfigureAwait @6867; ExecuteReaderAsync @6867; ReadAsync @6868; GetInt32 @6871; GetString @6871; GetInt64 @6871; Parse @6872; RaisePropertyChanged @6874; nameof @6874; NotifyTotalsChanged @6883; DispatchToUi @6888; SafeError @6888 | FROM store_config @6859 |
| <span id="m-232991a8e11a"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>6892–6920 | ConfigureAwait @6905; ExecuteAsync @6905; ReportError @6908; NotifyTotalsChanged @6913; DispatchToUi @6918; SafeError @6918 | No extracted literal effects. |
| <span id="m-5610b0e19d62"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>6922–6966 | DispatchToUi @6926; CreateCommand @6931; ConfigureAwait @6937; ExecuteReaderAsync @6937; ReadAsync @6938; Deserialize(ReceiptDesignDocument) @6940; GetString @6940; SafeError @6959 | FROM receipt_designs @6932; JOIN receipt_design_versions @6932 |
| <span id="m-a6eb9a0bf2e5"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>6968–6995 | ConfigureAwait @6981; ExecuteAsync @6981; ReportError @6986; DispatchToUi @6993; SafeError @6993 | No extracted literal effects. |
| <span id="m-533153b57e51"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>6997–7009 | IsWindows @6999; Select @7000; Enumerate @7000; Empty(string) @7001; ToArray @7002; OrderBy @7002; Distinct @7002; Where @7002; Append @7002; IsNullOrWhiteSpace @7003; Clear @7007; Add @7008 | No extracted literal effects. |
| <span id="m-3c9e4bbe8231"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>7011–7069 | CheckAccess @7013; DispatchToUi @7015; CreateSampleData @7021; Equals @7027; IsWindows @7034; TryReadGeometry @7035; BuildPaperDocument @7044; RenderPreviewPngPages @7047; SetReceiptDesignPreviewPages @7049; Localize @7051; BuildThermalLines @7056; RenderPreviewPng @7058; Empty(byte[]) @7065; ReportException @7067 | No extracted literal effects. |
| <span id="m-a995947059ba"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>7071–7076 | ShowReceiptDesignPreviewPage @7075 | No extracted literal effects. |
| <span id="m-c391ececd110"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>7078–7084 | ShowReceiptDesignPreviewPage @7083 | No extracted literal effects. |
| <span id="m-1126708b3d47"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>7086–7100 | RaisePropertyChanged @7097; nameof @7097 | No extracted literal effects. |
| <span id="m-610052e7b640"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>7102–7131 | ReadAsync @7105; Localize @7108; CreateCommand @7110; ConfigureAwait @7112; ExecuteScalarAsync @7112; ToString @7112; IsNullOrWhiteSpace @7113; ExecuteReaderAsync @7127; ReadAsync @7128; Trim @7129; GetString @7129 | FROM hardware_jobs @7111; FROM hardware_jobs @7126 |
| <span id="m-ceee321865d6"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>7133–7149 | Clear @7135; AsEnumerable @7136; Where @7139; IsNullOrWhiteSpace @7141; Contains @7143; Contains @7144; Contains @7145; Add @7148 | No extracted literal effects. |
| <span id="m-02a4813772a8"></span><code>MainViewModel.GenerateXReport()</code><br>7151–7170 | CheckSessionUnlocked @7153; ToString @7157; GenerateXReportInternalAsync @7169 | No extracted literal effects. |
| <span id="m-b2cd2d41c6b9"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>7172–7187 | ConfigureAwait @7176; LoadReportDataAsync @7176; DispatchToUi @7185; SafeError @7185 | No extracted literal effects. |
| <span id="m-7ddb08422003"></span><code>MainViewModel.CloseShiftZReport()</code><br>7189–7192 | OpenCloseShiftModal @7191 | No extracted literal effects. |
| <span id="m-4c0e069bf202"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>7194–7203 | CheckSessionUnlocked @7201 | No extracted literal effects. |
| <span id="m-e79abcaae15c"></span><code>MainViewModel.SaveSettings()</code><br>7205–7209 | CheckSessionUnlocked @7207 | No extracted literal effects. |
| <span id="m-83b5d6a41424"></span><code>MainViewModel.ApplySettingsAsync()</code><br>7211–7298 | CheckSessionUnlocked @7220; NotifyTotalsChanged @7239; ExecuteAsync @7267; DispatchToUi @7291; SafePipelineError @7291; SafeError @7296 | No extracted literal effects. |
| <span id="m-8230fd0913a5"></span><code>MainViewModel.CancelSettings()</code><br>7300–7321 | CheckSessionUnlocked @7302; NotifyTotalsChanged @7314 | No extracted literal effects. |
| <span id="m-d9fa71d0c32e"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7324–7354 | ProbeDatabaseAsync @7337; ProbeLicense @7343; RefreshOutputStatusAsync @7346; ProbeHardwareStubs @7347; DispatchToUi @7352; SafeError @7352 | No extracted literal effects. |
| <span id="m-2bf2dd7bb931"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7415–7453 | RaisePropertyChanged @7417; nameof @7417; FormatRealResetPreviewSummary @7452 | No extracted literal effects. |
| <span id="m-c218882e9f7d"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7455–7468 | Localize @7456; ToString @7458; GetValueOrDefault @7458; ToString @7463; ToString @7464; ToString @7465 | No extracted literal effects. |
| <span id="m-a4ac81bca9a6"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7577–7669 | Post @7581; ConfigureAwait @7588; GetWorkspaceEnvironmentAsync @7588; Equals @7589; GetDatasetStateAsync @7591; CreateCommand @7597; CreateParameter @7604; ToString @7606; Add @7607; ExecuteScalarAsync @7608; HasPermission @7613; ToInt64 @7618; ExecuteScalarAsync @7618; ExecuteScalarAsync @7622; ExecuteScalarAsync @7629; ExecuteScalarAsync @7635; Localize @7654 | FROM items @7617; FROM sales_invoices @7621; FROM third_parties @7634; FROM users @7598; JOIN user_roles @7598 · DYNAMIC SQL: inspect manually |
| <span id="m-dacd9e49b4c1"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>7671–7681 | CheckSessionUnlocked @7673; HasPermission @7674 | No extracted literal effects. |
| <span id="m-bc1fafb3eac0"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>7683–7688 | ConfigureAwait @7687; ResetDatabaseAsync @7687 | No extracted literal effects. |
| <span id="m-63cca0683382"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>7690–7691 | ConfigureAwait @7691; EnsureDefaultDemoDatasetAsync @7691 | No extracted literal effects. |
| <span id="m-3d6692ff65a6"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>7693–7699 | EnsureDefaultDemoDatasetAsync @7697 | No extracted literal effects. |
| <span id="m-f50edfb6a7db"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>7701–7805 | Localize @7706; ConfigureAwait @7713; WaitAsync @7713; GetWorkspaceEnvironmentAsync @7716; Equals @7717; HasPermission @7724; Post @7738; LocalizeDemoSeedProgress @7740; EnsureInitialDatasetAsync @7746; Join @7770; Select @7770; ReloadCatalogAsync @7780; LoadInventoryAsync @7781; LoadThirdPartiesAsync @7782; LoadManufacturingDataAsync @7783; LoadSuppliersAsync @7784; UpdateDemoSeedingAvailabilityAsync @7785; ToUpperInvariant @7790; ToString @7790; NewGuid @7790; LogDiagnosticError @7791; ReportError @7796; Release @7803 | No extracted literal effects. |
| <span id="m-fec0a52790bc"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>7807–7821 | Localize @7809 | No extracted literal effects. |
| <span id="m-9744b1afaf60"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>7823–7920 | Localize @7827; ConfigureAwait @7831; WaitAsync @7831; HasPermission @7835; GetWorkspaceEnvironmentAsync @7842; Equals @7843; ResetDatabaseAsync @7851; GetStoreProfileAsync @7854; Post @7855; Clear @7858; Clear @7859; Clear @7860; NewGuid @7861; RaisePropertyChanged @7864; nameof @7864; Lock @7865; Defaults @7878; RefreshUnlockCandidates @7891; LoadCashFinancialSettingsAsync @7892; LoadOutputDevicesAsync @7893; LoadManualPaymentSettingsAsync @7894; LoadReceiptDesignAsync @7895; ReloadCatalogAsync @7896; LoadInventoryAsync @7897; LoadThirdPartiesAsync @7898; LoadManufacturingDataAsync @7899; LoadActivityInvoicesAsync @7900; UpdateDemoSeedingAvailabilityAsync @7901; ToUpperInvariant @7906; ToString @7906; LogDiagnosticError @7907; ReportError @7913; Release @7918 | No extracted literal effects. |
| <span id="m-02079d9af3de"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>7922–7964 | CheckSessionUnlocked @7924; HasPermission @7926; ConfigureAwait @7934; GetWorkspaceEnvironmentAsync @7934; Equals @7935; PreviewAsync @7938; FormatRealResetPreviewSummary @7939; Post @7940; RaisePropertyChanged @7957; nameof @7957; SafeError @7962 | UnauthorizedAccessException @7936 |
| <span id="m-066271bb7f47"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>7966–8052 | HasPermission @7969; ConfigureAwait @7987; ExecuteAsync @7987; GetStoreProfileAsync @7996; Post @7999; Clear @8003; Clear @8004; Clear @8005; Clear @8006; NewGuid @8007; Lock @8010; RaisePropertyChanged @8024; nameof @8024; LoadCashFinancialSettingsAsync @8025; LoadOutputDevicesAsync @8026; LoadManualPaymentSettingsAsync @8027; LoadReceiptDesignAsync @8028; RefreshUnlockCandidates @8036; LoadInventoryAsync @8037; LoadActivityInvoicesAsync @8038; UpdateDemoSeedingAvailabilityAsync @8039; ToUpperInvariant @8044; ToString @8044; LogDiagnosticError @8045 | No extracted literal effects. |
| <span id="m-9df3cfaa31a8"></span><code>MainViewModel.CancelRealShopReset()</code><br>8054–8061 | RaisePropertyChanged @8060; nameof @8060 | No extracted literal effects. |
| <span id="m-39360d1ebf79"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>8065–8082 | ConfigureAwait @8067; ExportDocumentAsync @8067; Post @8071; GetFileName @8075 | No extracted literal effects. |
| <span id="m-e0c021b19766"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>8084–8106 | Exists @8089; CreateDirectory @8091; Start @8093; ToUpperInvariant @8102; ToString @8102; NewGuid @8102; LogDiagnosticError @8103 | No extracted literal effects. |
| <span id="m-3ef014542dc5"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>8108–8118 | CheckSessionUnlocked @8110; RaisePropertyChanged @8112; nameof @8112; Localize @8114; ToString @8115 | No extracted literal effects. |
| <span id="m-bfbce92ec88d"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>8125–8141 | CheckSessionUnlocked @8127; HasPermission @8128; RaisePropertyChanged @8134; nameof @8134; Localize @8137; ToString @8138 | No extracted literal effects. |
| <span id="m-df73c19228ba"></span><code>MainViewModel.CommitNumpad()</code><br>8143–8220 | CheckSessionUnlocked @8145; ResetCashReview @8146; TryParse @8152; IsNullOrWhiteSpace @8154; Trim @8160; NotifyTotalsChanged @8170; SaveDurableCartAsync @8171; Min @8177; ToMinorUnits @8179; Round @8180; TryParse @8195; UpdateCartKitBreakdownAsync @8203; Remove @8209; RaisePropertyChanged @8218; nameof @8218 | No extracted literal effects. |
| <span id="m-5096da0f0de2"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>8226–8244 | CheckSessionUnlocked @8234 | No extracted literal effects. |
| <span id="m-af8a38c204df"></span><code>MainViewModel.StageBusinessProfile()</code><br>8251–8281 | CheckSessionUnlocked @8253; HasPermission @8257 | No extracted literal effects. |
| <span id="m-eaf22538fc4e"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8283–8292 | — | No extracted literal effects. |
| <span id="m-bab406f43595"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8294–8317 | RecalculateCart @8296; RaisePropertyChanged @8298; nameof @8298 | No extracted literal effects. |
| <span id="m-c93372552435"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8319–8406 | IsNullOrWhiteSpace @8322; Trim @8322; All @8332; Trim @8349; Trim @8350; NewGuid @8354; ToString @8359; ConfigureAwait @8363; BeginTransactionAsync @8363; HandleAsync @8364; AppendAsync @8369; ToString @8370; Serialize @8375; CommitAsync @8378; Initialize @8384; Unlock @8385; RaisePropertyChanged @8390; nameof @8390; LoadTeamsStaffAsync @8393; StartAutomaticDemoDatasetLoadAsync @8394; RollbackAsync @8398; DispatchToUi @8399; SafePipelineError @8399; SafeError @8404 | No extracted literal effects. |
| <span id="m-e2dbe9a12bb4"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8408–8415 | IsNullOrWhiteSpace @8410; ConfigureAwait @8414; SaveTeamMemberAsync @8414 | No extracted literal effects. |
| <span id="m-c7b8ec4f38ae"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8417–8435 | CheckSessionUnlocked @8420; HasPermission @8422 | No extracted literal effects. |
| <span id="m-b6d88a43bd69"></span><code>MainViewModel.CancelChangePin()</code><br>8437–8444 | — | No extracted literal effects. |
| <span id="m-7a601b37ed8c"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8446–8522 | Trim @8454; IsNullOrWhiteSpace @8457; All @8463; Equals @8476; Equals @8477; SetQuickPin @8489; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8502; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8502; ConfigureAwait @8510; LoadTeamsStaffAsync @8510; DispatchToUi @8515; SafePipelineError @8515; SafeError @8520 | No extracted literal effects. |
| <span id="m-17ea9934b085"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8524–8598 | HasPermission @8530; ConfigureAwait @8539; ResolveEffectivePermissionsAsync @8539; Contains @8572; Contains @8573; Add @8575; Contains @8581; DispatchToUi @8587; Clear @8589; Add @8590; SafeError @8596 | No extracted literal effects. |
| <span id="m-5e909b43a89d"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8600–8642 | OnTeamMemberFieldChanged @8606; ConfigureAwait @8623; ExecuteAsync @8623; DispatchToUi @8627; SafePipelineError @8635; SafeError @8640 | No extracted literal effects. |
| <span id="m-e440aef8201b"></span><code>MainViewModel.ClosePermissionEditor()</code><br>8644–8649 | — | No extracted literal effects. |
| <span id="m-8a8d6cbb0dc5"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>8651–8666 | ClearImportResults @8653 | No extracted literal effects. |
| <span id="m-12036e61ad24"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>8670–8670 | — | No extracted literal effects. |
| <span id="m-eaafcebbf510"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>8671–8671 | — | No extracted literal effects. |
| <span id="m-85362977469a"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>8672–8672 | FromResult @8672 | No extracted literal effects. |
| <span id="m-c6ef96b12d2c"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>8675–8760 | HasPermission @8684; FromDecimal @8699; ConfigureAwait(OpenShiftCommand, Shift) @8703; ExecuteAsync(OpenShiftCommand, Shift) @8703; SetActiveCashier @8718; RefreshUnlockCandidates @8719; ToUpperInvariant @8736; ToString @8736; ToString @8738; ConfigureAwait @8748; LoadTeamsStaffAsync @8748; LoadTrackOrdersAsync @8749; DispatchToUi @8753; SafePipelineError @8753; SafeError @8758 | No extracted literal effects. |
| <span id="m-054644fcf91a"></span><code>MainViewModel.LoadInventoryAsync()</code><br>8762–8916 | ApplyPagedResult @8766; ToList @8767; ApplyInventoryFilter @8771; Clear @8779; Empty(InventoryItem) @8781; ConfigureAwait @8786; GetPagedInventoryItemsAsync @8786; ToPageRequest @8791; CreateCommand @8804; ExecuteReaderAsync @8806; ReadAsync @8807; Add @8809; Parse @8809; GetString @8809; ExecuteReaderAsync @8819; ReadAsync @8820; TryParse @8822; GetString @8822; IsDBNull @8822; Add @8833; TryGetValue @8835; Contains @8843; ToDecimal @8846; Localize @8854; ToLocalTime @8860; BuildCostSourcesTooltip @8862; DispatchToUi @8889; Add @8892; SafeError @8914 | FROM item_kits @8805; FROM item_pricing @8818 |
| <span id="m-c36fa7035298"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>8918–8974 | CheckSessionUnlocked @8920; FirstOrDefault @8921; Clear @8932; Add @8934; CreateCommand @8939; CreateParameter @8950; Add @8953; ExecuteReader @8954; Read @8955; GetString @8957; Contains @8958; FirstOrDefault @8970; ResetReceiveLines @8971; UpdateReceiveKitBreakdownAsync @8972 | FROM uoms @8940; JOIN uoms @8940 |
| <span id="m-382024453774"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>8976–9077 | IsNullOrWhiteSpace @8989; Localize @9006; HasPermission @9010; BuildReceiptLines @9016; Sum @9033; Trim @9043; ToMinorUnits @9048; ConfigureAwait(ReceiveStockCommand, StockMovement) @9053; ExecuteAsync(ReceiveStockCommand, StockMovement) @9053; Clear @9063; ConfigureAwait @9065; LoadInventoryAsync @9065; LoadItemHistoryAsync @9066; DispatchToUi @9070; SafePipelineError @9070; SafeError @9075 | No extracted literal effects. |
| <span id="m-bb46933b0191"></span><code>MainViewModel.ResetReceiveLines()</code><br>9083–9100 | Clear @9085; Add @9089; RaisePropertyChanged @9095; nameof @9095; Invoke @9098 | No extracted literal effects. |
| <span id="m-ac6286ac6e91"></span><code>MainViewModel.AddReceiveLine()</code><br>9103–9126 | IsNullOrWhiteSpace @9110; Add @9116; RaisePropertyChanged @9121; nameof @9121; Invoke @9124 | No extracted literal effects. |
| <span id="m-67530ee00ab1"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>9129–9146 | Remove @9136; Add @9139; RaisePropertyChanged @9145; nameof @9145 | No extracted literal effects. |
| <span id="m-2832a9e4bdb0"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>9152–9173 | IsNullOrWhiteSpace @9154; LastOrDefault @9159; Add @9163; Trim @9166; ReferenceEquals @9167; RaisePropertyChanged @9171; nameof @9171; Invoke @9172 | No extracted literal effects. |
| <span id="m-6e9b0b8815aa"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>9176–9253 | Add @9188; IsNullOrWhiteSpace @9196; Trim @9200; FirstOrDefault @9209; GroupBy @9209; Count @9211; Trim @9238 | No extracted literal effects. |
| <span id="m-0156f8cc1848"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>9255–9291 | CreateCommand @9260; ConfigureAwait @9267; ExecuteReaderAsync @9267; Clear @9268; ReadAsync @9269; Add @9271; ParseGuidSafe @9272; GetString @9272; IsDBNull @9276; GetInt32 @9280; Parse @9282; DispatchToUi @9289; SafeError @9289 | FROM third_parties @9261 |
| <span id="m-8de9067b5c82"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9293–9311 | CheckSessionUnlocked @9295; FirstOrDefault @9301 | No extracted literal effects. |
| <span id="m-7800e89deed8"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9313–9404 | IsNullOrWhiteSpace @9336; HasPermission @9347; Trim @9365; Trim @9367; ConfigureAwait(AdjustStockCommand, StockMovement) @9371; ExecuteAsync(AdjustStockCommand, StockMovement) @9371; ConfigureAwait @9387; LoadInventoryAsync @9387; LoadItemHistoryAsync @9388; OpenWasteExpenseConfirmation @9392; DispatchToUi @9397; SafePipelineError @9397; SafeError @9402 | No extracted literal effects. |
| <span id="m-576d8e0515f6"></span><code>MainViewModel.OpenAddProduct()</code><br>9406–9474 | ResetProductStockDraft @9408; CheckSessionUnlocked @9409; HasPermission @9410; RaisePropertyChanged @9418; nameof @9418; ClearItemHistory @9420; LoadCatalogRegistryAsync @9427; InitializeProductPricingDraft @9430; Clear @9445; Clear @9446; Where @9447; Add @9449; FirstOrDefault @9451; Clear @9462; CaptureProductModalBaselineAsync @9473 | No extracted literal effects. |
| <span id="m-1f94dccf3a9c"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9476–9476 | OpenEditProduct @9476 | No extracted literal effects. |
| <span id="m-c75fc416f670"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9478–9558 | ResetProductStockDraft @9480; CheckSessionUnlocked @9482; HasPermission @9483; RaisePropertyChanged @9491; nameof @9491; ClearItemHistory @9493; LoadCatalogRegistryAsync @9501; InitializeProductPricingDraft @9507; ToMinorUnits @9508; LoadExactProductCostSnapshotsAsync @9514; ToDecimal @9518; Clear @9525; Clear @9526; Where @9527; Add @9529; FirstOrDefault @9531; LoadItemLocationEligibilitiesAsync @9550; LoadProductKitAsync @9551; LoadPrimaryBarcodeAsync @9552; LoadProductPricingDraftAsync @9553; LoadItemHistoryAsync @9554; LoadItemPriceHistoryAsync @9555; CaptureProductModalBaselineAsync @9557 | No extracted literal effects. |
| <span id="m-81838c145ff5"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>9560–9573 | OrderBy @9563; Where @9563; Add @9565 | No extracted literal effects. |
| <span id="m-41559e3293a3"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>9575–9648 | CreateCommand @9582; CreateParameter @9589; ToString @9591; Add @9592; ConfigureAwait @9593; ExecuteReaderAsync @9593; ReadAsync @9594; GetInt32 @9596; IsDBNull @9597; GetString @9597; ParseStoredPricingPercentForDisplay @9598; ToDisplayAmount @9602; GetInt64 @9602; OrderBy @9622; Where @9622; TryGetValue @9625; Add @9631; InvokeAsync @9633; RaisePropertyChanged @9638; nameof @9638; CaptureProductPricingSnapshot @9641; DispatchToUi @9646; SafeError @9646 | FROM item_price_levels @9613; FROM item_pricing @9584 |
| <span id="m-21cd73ba22e9"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>9650–9685 | CreateCommand @9657; CreateParameter @9663; ToString @9665; Add @9666; ConfigureAwait @9667; ExecuteReaderAsync @9667; ReadAsync @9668; Parse @9671; GetString @9671; GetInt32 @9671; GetInt64 @9672; IsDBNull @9672; Parse @9673; InvokeAsync @9675; DispatchToUi @9683; SafeError @9683 | FROM product_category_pricing_rules @9658 |
| <span id="m-3c172bdad827"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>9687–9716 | ConfigureAwait @9691; WhenAll @9691; InvokeAsync @9692; CaptureProductModalSnapshot @9696; CaptureProductPricingSnapshot @9697; RaisePropertyChanged @9698; nameof @9698 | No extracted literal effects. |
| <span id="m-5de70f9a13c9"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>9718–9766 | Serialize @9718; ToArray @9741; Select @9741; Select @9758; OrderBy @9758; OrderBy @9762 | No extracted literal effects. |
| <span id="m-e10f34b3e724"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>9768–9780 | Serialize @9768; ToArray @9779; Select @9779 | No extracted literal effects. |
| <span id="m-4d69d078ce51"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9782–9814 | nameof @9784; RaisePropertyChanged @9785; RaiseTraceabilityState @9790; StartsWith @9794; RecomputeProductPricingPreview @9805; RefreshVirtualKitAvailability @9807 | No extracted literal effects. |
| <span id="m-634c3baf0afa"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>9816–9830 | RaisePropertyChanged @9824; nameof @9824; RecomputeProductPricingPreview @9827; RefreshVirtualKitAvailability @9828 | No extracted literal effects. |
| <span id="m-d6a6517b51df"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9832–9840 | RaisePropertyChanged @9834; nameof @9834; RecomputeProductPricingPreview @9837; RefreshVirtualKitAvailability @9838 | No extracted literal effects. |
| <span id="m-a80dac9f5303"></span><code>MainViewModel.RequestCloseProductModal()</code><br>9842–9855 | DiscardProductModal @9854 | No extracted literal effects. |
| <span id="m-c7c5ae5d494a"></span><code>MainViewModel.DiscardProductModal()</code><br>9857–9866 | RaisePropertyChanged @9862; nameof @9862; ClearItemHistory @9864 | No extracted literal effects. |
| <span id="m-901a16013238"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>9868–9886 | CreateCommand @9873; CreateParameter @9875; ToString @9877; Add @9878; ConfigureAwait @9879; ExecuteScalarAsync @9879; DispatchToUi @9882; ToString @9882 | FROM barcodes @9874 |
| <span id="m-1866e5bd3436"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>9888–9939 | CreateCommand @9893; CreateParameter @9900; ToString @9902; Add @9903; ConfigureAwait @9907; ExecuteReaderAsync @9907; ReadAsync @9908; IsDBNull @9911; GetString @9911; GetDouble @9912; ResolveQuantity @9913; Add @9914; Parse @9916; DispatchToUi @9924; Clear @9927; Add @9928; RaisePropertyChanged @9931; nameof @9931; RecomputeProductPricingPreview @9934; RefreshVirtualKitAvailability @9935 | FROM item_kits @9894; JOIN item_kit_components @9894; JOIN items @9894 |
| <span id="m-8609904f48bd"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>9941–9941 | SaveProductConfigurationAsync @9941 | No extracted literal effects. |
| <span id="m-42a4a6716772"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>9943–10148 | ConfigureAwait @9948; LoadCatalogRegistryAsync @9948; HasPermission @9950; IsNullOrWhiteSpace @9955; Localize @9977; Equals @9987; ToMinorUnits @10032; GetValueOrDefault @10044; Trim @10045; Trim @10046; Trim @10047; Trim @10054; Trim @10056; ToList @10101; Select @10101; CaptureProductPricingSnapshot @10105; ToCommand @10107; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @10115; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @10115; DispatchToUi @10118; RaiseTraceabilityState @10124; CaptureProductModalSnapshot @10126; RaisePropertyChanged @10128; nameof @10128; ReloadCatalogAsync @10135; LoadInventoryAsync @10136; LoadItemHistoryAsync @10137; SafePipelineError @10141; SafeError @10146 | No extracted literal effects. |
| <span id="m-c0d8f694a67d"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>10150–10186 | CheckSessionUnlocked @10152; HasPermission @10153; ConfigureAwait(DeactivateProductCommand, bool) @10169; ExecuteAsync(DeactivateProductCommand, bool) @10169; ConfigureAwait @10174; ReloadCatalogAsync @10174; LoadInventoryAsync @10175; DispatchToUi @10179; SafePipelineError @10179; SafeError @10184 | No extracted literal effects. |
| <span id="m-11b918baec69"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>10188–10247 | ConfigureAwait @10194; GetActiveItemsAsync @10194; Clear @10196; Clear @10197; Clear @10198; CreateCommand @10203; ExecuteReaderAsync @10205; ReadAsync @10206; TryParse @10208; GetString @10208; Add @10209; Add @10216; GroupBy @10217; Count @10219; Contains @10224; Add @10237; Add @10238; ApplyFilter @10241 | FROM item_kits @10204 |
| <span id="m-14b627e67e5f"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>10249–10255 | IsNullOrWhiteSpace @10251; TryParse @10252; HashData @10253; GetBytes @10253; AsSpan @10254 | No extracted literal effects. |
| <span id="m-5e7ab16c58dd"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>10257–10323 | CreateCommand @10263; ConfigureAwait @10266; ExecuteReaderAsync @10266; ReadAsync @10268; Add @10270; GetString @10272; GetInt32 @10276; Clear @10282; Add @10283; ExecuteReaderAsync @10295; ReadAsync @10297; Add @10299; GetString @10301; IsDBNull @10305; GetInt32 @10309; Clear @10315; Add @10316; DispatchToUi @10321; SafeError @10321 | FROM bins @10288; FROM facilities @10265; JOIN facilities @10288 |
| <span id="m-4ca78621d7a2"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>10538–10642 | CreateCommand @10548; ConfigureAwait @10555; ExecuteReaderAsync @10555; ReadAsync @10556; Add @10558; ParseGuidSafe @10560; GetString @10560; IsDBNull @10563; GetInt32 @10564; Add @10584; DispatchToUi @10599; Clear @10601; Clear @10602; Clear @10603; Equals @10607; Add @10608; Add @10610; Add @10612; Clear @10614; Add @10615; FirstOrDefault @10618; Equals @10618; FirstOrDefault @10623; FirstOrDefault @10630; ApplySaleUnitDefaultsToCatalog @10635; SafeError @10640 | FROM product_categories @10550; FROM uoms @10576 |
| <span id="m-bbd920bc9f16"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>10644–10658 | ResolveProductSaleUnitFactor @10648; Round @10654; ApplyFilter @10657 | No extracted literal effects. |
| <span id="m-e3b27b842f44"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>10660–10678 | FirstOrDefault @10662; Equals @10663; TryParse @10670 | No extracted literal effects. |
| <span id="m-4305392f65ee"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>10680–10702 | CheckSessionUnlocked @10682; HasPermission @10683; ConfigureAwait @10698; LoadManagedCategoriesAsync @10698; CaptureCategoryFormSnapshot @10700; RaisePropertyChanged @10701; nameof @10701 | No extracted literal effects. |
| <span id="m-9e4d1f8c108f"></span><code>MainViewModel.CloseCategoryManager()</code><br>10704–10713 | — | No extracted literal effects. |
| <span id="m-b06e1b1e1da4"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>10715–10737 | CheckSessionUnlocked @10717; HasPermission @10718; ConfigureAwait @10733; LoadManagedUnitsAsync @10733; CaptureUnitFormSnapshot @10735; RaisePropertyChanged @10736; nameof @10736 | No extracted literal effects. |
| <span id="m-87698c7eb5ef"></span><code>MainViewModel.CloseUnitManager()</code><br>10739–10748 | — | No extracted literal effects. |
| <span id="m-7b0df34915b1"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>10750–10813 | Clear @10753; Clear @10754; Clear @10755; CreateCommand @10756; ConfigureAwait @10762; ExecuteReaderAsync @10762; ReadAsync @10763; Add @10765; ParseGuidSafe @10767; GetString @10767; IsDBNull @10770; GetInt32 @10771; Where @10779; Equals @10779; Add @10780; TryParse @10793; Add @10794; RefreshTargetedCategoryCollections @10807; DispatchToUi @10808; RefreshManagedCategoriesTable @10810; RefreshManagedExpenseCategoriesTable @10811 | FROM expense_categories @10784; FROM product_categories @10758; JOIN expense_records @10784 |
| <span id="m-0fc1c428a518"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>10815–10822 | OpenCategoryManagerAsync @10817; FirstOrDefault @10818; EditManagedCategory @10821 | No extracted literal effects. |
| <span id="m-93530d4d7315"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>10824–10832 | OpenCategoryManagerAsync @10827; FirstOrDefault @10828; EditManagedExpenseCategory @10831 | No extracted literal effects. |
| <span id="m-9443359fe574"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>10834–10853 | DispatchToUi @10836; Clear @10838; Clear @10839; Clear @10840; Where @10842; Equals @10845; Add @10846; Add @10848; Add @10850 | No extracted literal effects. |
| <span id="m-d45cc0c97faf"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>10855–10867 | CaptureCategoryFormSnapshot @10865; RaisePropertyChanged @10866; nameof @10866 | No extracted literal effects. |
| <span id="m-0c65274088dc"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>10869–10882 | CaptureCategoryFormSnapshot @10880; RaisePropertyChanged @10881; nameof @10881 | No extracted literal effects. |
| <span id="m-df5b5c857dc9"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>10884–10894 | Serialize @10884 | No extracted literal effects. |
| <span id="m-ac0604d07d1f"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>10896–10906 | Serialize @10896 | No extracted literal effects. |
| <span id="m-b583a93bda9a"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>10908–10908 | — | No extracted literal effects. |
| <span id="m-2e67a833eff4"></span><code>MainViewModel.DiscardRegistryForm()</code><br>10910–10926 | Equals @10913; RaisePropertyChanged @10917; nameof @10917 | No extracted literal effects. |
| <span id="m-e6680ca60f15"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>10928–11055 | Equals @10939; HasPermission @10941; FirstOrDefault @10950; Trim @10955; Trim @10956; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @10958; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @10958; DispatchToUi @10961; SafePipelineError @10961; IsNullOrWhiteSpace @10969; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @10971; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @10971; ConfigureAwait @10980; LoadManagedCategoriesAsync @10980; LoadExpenseCategoriesAsync @10981; CaptureCategoryFormSnapshot @10991; RaisePropertyChanged @10992; nameof @10992; Trim @11010; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @11012; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @11012; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @11028; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @11028; LoadCatalogRegistryAsync @11037; ReloadCatalogAsync @11038; SafeError @11053 | No extracted literal effects. |
| <span id="m-0e8f19e416fd"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>11057–11102 | HasPermission @11067; ConfigureAwait(DeactivateCategoryCommand, bool) @11080; ExecuteAsync(DeactivateCategoryCommand, bool) @11080; ConfigureAwait(ReactivateCategoryCommand, bool) @11085; ExecuteAsync(ReactivateCategoryCommand, bool) @11085; DispatchToUi @11090; SafePipelineError @11090; ConfigureAwait @11094; LoadManagedCategoriesAsync @11094; LoadCatalogRegistryAsync @11095; ReloadCatalogAsync @11096; SafeError @11100 | No extracted literal effects. |
| <span id="m-d839e2dbd418"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>11104–11144 | HasPermission @11114; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11130; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11130; DispatchToUi @11133; SafePipelineError @11133; ConfigureAwait @11137; LoadManagedCategoriesAsync @11137; LoadExpenseCategoriesAsync @11138; SafeError @11142 | No extracted literal effects. |
| <span id="m-a6d03e037c50"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>11146–11246 | Clear @11149; CreateCommand @11152; ConfigureAwait @11158; ExecuteReaderAsync @11158; ReadAsync @11159; Add @11161; GetString @11163; IsDBNull @11165; GetInt32 @11169; IsNullOrWhiteSpace @11180; Equals @11184; Add @11191; Clear @11195; ExecuteReaderAsync @11200; ReadAsync @11201; GetString @11203; Where @11225; Add @11227; TryGetValue @11230; FirstOrDefault @11237; Add @11241; DispatchToUi @11244; UpdateConversionPreview @11245 | FROM store_uom_preferences @11199; FROM uoms @11154 |
| <span id="m-f4cbdee00a61"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>11248–11255 | OpenUnitManagerAsync @11250; FirstOrDefault @11251; Equals @11251; EditManagedUnit @11254 | No extracted literal effects. |
| <span id="m-1bd5cb10eec4"></span><code>MainViewModel.UpdateConversionPreview()</code><br>11257–11293 | IsNullOrWhiteSpace @11259; FirstOrDefault @11265; Equals @11265; TryParse @11280 | No extracted literal effects. |
| <span id="m-f33824180be4"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11295–11316 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11302; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11302; DispatchToUi @11305; SafePipelineError @11309; SafeError @11314 | No extracted literal effects. |
| <span id="m-d44dd3781102"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11318–11331 | IsNullOrWhiteSpace @11324; TryParse @11327; CaptureUnitFormSnapshot @11329; RaisePropertyChanged @11330; nameof @11330 | No extracted literal effects. |
| <span id="m-1e15b143d6b1"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>11333–11395 | IsNullOrWhiteSpace @11345; Trim @11349; Trim @11350; Trim @11353; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @11354; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @11354; DispatchToUi @11357; SafePipelineError @11357; Trim @11364; Equals @11367; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @11372; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @11372; ConfigureAwait @11380; LoadManagedUnitsAsync @11380; LoadCatalogRegistryAsync @11381; CaptureUnitFormSnapshot @11388; RaisePropertyChanged @11389; nameof @11389; SafeError @11393 | No extracted literal effects. |
| <span id="m-7a9ff028d95b"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>11397–11435 | ConfigureAwait(DeactivateUomCommand, bool) @11414; ExecuteAsync(DeactivateUomCommand, bool) @11414; ConfigureAwait(ReactivateUomCommand, bool) @11419; ExecuteAsync(ReactivateUomCommand, bool) @11419; DispatchToUi @11424; SafePipelineError @11424; ConfigureAwait @11428; LoadManagedUnitsAsync @11428; LoadCatalogRegistryAsync @11429; SafeError @11433 | No extracted literal effects. |
| <span id="m-af240dc77a8f"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>11437–11475 | CreateCommand @11442; CreateParameter @11449; ToString @11451; Add @11452; ConfigureAwait @11454; ExecuteReaderAsync @11454; Clear @11455; ReadAsync @11456; Add @11458; ParseGuidSafe @11460; GetString @11460; GetInt32 @11463; IsDBNull @11465; ToDecimal @11465; GetDouble @11465; DispatchToUi @11473; SafeError @11473 | FROM item_locations @11443 |
| <span id="m-b40c104116f7"></span><code>MainViewModel.OpenLocationsModal()</code><br>11478–11504 | CheckSessionUnlocked @11480; HasPermission @11481; LoadFacilitiesAndBinsAsync @11502 | No extracted literal effects. |
| <span id="m-5007a2bdd96d"></span><code>MainViewModel.OpenAddFacility()</code><br>11506–11514 | — | No extracted literal effects. |
| <span id="m-7cd4565a771f"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>11516–11525 | — | No extracted literal effects. |
| <span id="m-2d52ad4793fc"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>11527–11586 | HasPermission @11530; IsNullOrWhiteSpace @11535; IsNullOrEmpty @11551; Trim @11553; Trim @11553; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @11554; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @11554; OpenAddFacility @11558; ConfigureAwait @11559; LoadFacilitiesAndBinsAsync @11559; DispatchToUi @11563; SafePipelineError @11563; ConfigureAwait(CreateFacilityCommand, FacilityDto) @11569; ExecuteAsync(CreateFacilityCommand, FacilityDto) @11569; SafeError @11584 | No extracted literal effects. |
| <span id="m-9e991c60fb18"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>11588–11619 | HasPermission @11591; ConfigureAwait(DeactivateFacilityCommand, bool) @11603; ExecuteAsync(DeactivateFacilityCommand, bool) @11603; OpenAddFacility @11607; ConfigureAwait @11608; LoadFacilitiesAndBinsAsync @11608; DispatchToUi @11612; SafePipelineError @11612; SafeError @11617 | No extracted literal effects. |
| <span id="m-d1cae500638f"></span><code>MainViewModel.OpenAddBin()</code><br>11621–11632 | FirstOrDefault @11631 | No extracted literal effects. |
| <span id="m-a1711e34323c"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>11634–11646 | FirstOrDefault @11644 | No extracted literal effects. |
| <span id="m-5d2e179e5d8e"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>11648–11723 | HasPermission @11651; IsNullOrWhiteSpace @11661; IsNullOrEmpty @11672; Trim @11677; Trim @11678; Trim @11679; Trim @11680; Trim @11681; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @11684; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @11684; OpenAddBin @11688; ConfigureAwait @11689; LoadFacilitiesAndBinsAsync @11689; DispatchToUi @11693; SafePipelineError @11693; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @11706; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @11706; SafeError @11721 | No extracted literal effects. |
| <span id="m-b070b5f5cf6a"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>11725–11756 | HasPermission @11728; ConfigureAwait(DeactivateLocationBinCommand, bool) @11740; ExecuteAsync(DeactivateLocationBinCommand, bool) @11740; OpenAddBin @11744; ConfigureAwait @11745; LoadFacilitiesAndBinsAsync @11745; DispatchToUi @11749; SafePipelineError @11749; SafeError @11754 | No extracted literal effects. |
| <span id="m-dbbd759c7c85"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>11758–11811 | HasPermission @11766; IsNullOrWhiteSpace @11771; Trim @11783; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @11791; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @11791; ConfigureAwait @11799; LoadItemLocationEligibilitiesAsync @11799; DispatchToUi @11804; SafePipelineError @11804; SafeError @11809 | No extracted literal effects. |
| <span id="m-b5978320170e"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>11813–11843 | HasPermission @11816; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @11828; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @11828; ConfigureAwait @11831; LoadItemLocationEligibilitiesAsync @11831; DispatchToUi @11836; SafePipelineError @11836; SafeError @11841 | No extracted literal effects. |
| <span id="m-55fcbb2d8c45"></span><code>MainViewModel.LoadCustomersAsync()</code><br>11846–11879 | NewGuid @11854; Clear @11860; Add @11861; FilterCustomers @11863; ConfigureAwait @11870; GetCustomersAsync @11870; DispatchToUi @11877; SafeError @11877 | No extracted literal effects. |
| <span id="m-a2b9e8762eb8"></span><code>MainViewModel.FilterCustomers()</code><br>11881–11894 | Clear @11883; Trim @11884; IsNullOrWhiteSpace @11885; Where @11887; Contains @11887; Contains @11888; Contains @11889; Add @11892 | No extracted literal effects. |
| <span id="m-cf64a221c65b"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>11896–11932 | CheckSessionUnlocked @11898; CreateCommand @11907; CreateParameter @11910; ToString @11912; Add @11913; ConfigureAwait @11914; ExecuteScalarAsync @11914; ToString @11915; Equals @11918; LoadPickerCandidatesAsync @11930; DispatchToUi @11931 | FROM items @11909 |
| <span id="m-684669549902"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>11934–11995 | ConfigureAwait @11941; GetLotCandidatesAsync @11941; DispatchToUi @11944; Clear @11946; Add @11949; ToString @11958; GetSerialCandidatesAsync @11966; Clear @11971; Add @11974; ToString @11983 | No extracted literal effects. |
| <span id="m-7205fc339dda"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>11997–12003 | Clear @12000; Clear @12001 | No extracted literal effects. |
| <span id="m-6d851c73edad"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>12005–12064 | FirstOrDefault @12018; ConfigureAwait(SelectLotForCartLineCommand, bool) @12026; ExecuteAsync(SelectLotForCartLineCommand, bool) @12026; DispatchToUi @12029; SafePipelineError @12029; ToList @12035; Where @12035; ConfigureAwait(SelectSerialForCartLineCommand, bool) @12045; ExecuteAsync(SelectSerialForCartLineCommand, bool) @12045; SafeError @12062 | No extracted literal effects. |
| <span id="m-94ccf668732a"></span><code>MainViewModel.OpenCustomerChooser()</code><br>12066–12074 | CheckSessionUnlocked @12068; Clear @12071; LoadCustomersAsync @12072 | No extracted literal effects. |
| <span id="m-7873981ea712"></span><code>MainViewModel.CloseCustomerChooser()</code><br>12076–12079 | — | No extracted literal effects. |
| <span id="m-c8fda339672f"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>12081–12098 | SaveDurableCartAsync @12091; IsNullOrWhiteSpace @12095; ToString @12095; NewGuid @12095; RecordSuccessfulSearchUseAsync @12096; FromGuid @12096 | No extracted literal effects. |
| <span id="m-e0585454fd1e"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>12100–12109 | SaveDurableCartAsync @12108 | No extracted literal effects. |
| <span id="m-514133f30404"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>12111–12156 | CheckSessionUnlocked @12113; IndexOf @12117; SelectWalkInCustomer @12123; FilterCustomers @12125; ConfigureAwait(DeactivateCustomerCommand, bool) @12137; ExecuteAsync(DeactivateCustomerCommand, bool) @12137; ConfigureAwait @12144; LoadCustomersAsync @12144; DispatchToUi @12149; SafePipelineError @12149; SafeError @12154 | No extracted literal effects. |
| <span id="m-b985b6893ec8"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>12285–12324 | Add @12291; NewGuid @12292; RefreshManufacturingTablesAsync @12306; ConfigureAwait @12314; GetKitsAsync @12314; Clear @12315; Add @12316; DispatchToUi @12322; SafeError @12322 | No extracted literal effects. |
| <span id="m-ebc4bdead086"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12328–12344 | CheckSessionUnlocked @12330; SetProductionActionMode @12332; FirstOrDefault @12337; LoadProductionIngredientLotsAsync @12342; TakeProductionSnapshot @12343 | No extracted literal effects. |
| <span id="m-6a4f72a0715b"></span><code>MainViewModel.CloseProductionModal()</code><br>12346–12360 | — | No extracted literal effects. |
| <span id="m-43f363cef118"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>12362–12461 | ExecuteExistingProductionAsync @12365; Resolve @12387; NewGuid @12390; ToUpperInvariant @12392; ToString @12392; Insert @12410; IsNullOrWhiteSpace @12432; Trim @12432; ToDictionary @12434; Where @12434; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @12438; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @12438; DispatchToUi @12441; SafePipelineError @12441; RecordSuccessfulSearchUseAsync @12448; FromGuid @12448; ConfigureAwait @12451; LoadManufacturingDataAsync @12451; LoadInventoryAsync @12452; SafeError @12458 | No extracted literal effects. |
| <span id="m-097fb18949cf"></span><code>MainViewModel.CloseXReportModal()</code><br>12560–12563 | — | No extracted literal effects. |
| <span id="m-9a2067b9e240"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>12565–12595 | CheckSessionUnlocked @12567; Clear @12585; Where @12586; GetUnlockCandidates @12586; Equals @12587; Add @12591 | No extracted literal effects. |
| <span id="m-1ab533ea34a9"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>12597–12601 | — | No extracted literal effects. |
| <span id="m-e25cdc30d31e"></span><code>MainViewModel.CloseZReportModal()</code><br>12603–12606 | — | No extracted literal effects. |
| <span id="m-abc92ecb176c"></span><code>MainViewModel.LoadReportDataAsync()</code><br>12608–12725 | ToString @12628; DispatchToUi @12644; ConfigureAwait @12672; ExecuteAsync @12672; Join @12674; Select(string, Money) @12674; InvoiceMoney @12674; ToDecimal @12677; ToDecimal @12678; ToDecimal @12679; ToDecimal @12680; ToDecimal @12682; ToDecimal @12684; ToDecimal @12685; ToDecimal @12686; ToDecimal @12687; ToDecimal @12688; ToUpperInvariant @12690; ToString @12690; ToString @12692; ToString @12693; Sum @12699; ToDecimal @12699; ToDecimal @12702; Add @12704; Format @12709; SafeError @12717 | No extracted literal effects. |
| <span id="m-d0b0c7ed5b26"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>12727–12816 | CheckSessionUnlocked @12730; IsNullOrWhiteSpace @12747; AuthenticateSelectedUser @12755; Trim @12757; Round @12766; Trim @12770; ConfigureAwait(CloseShiftCommand, Shift) @12774; ExecuteAsync(CloseShiftCommand, Shift) @12774; DispatchToUi @12792; SafePipelineError @12792; ConfigureAwait @12799; ExecuteAsync @12799; SetActiveCashier @12803; RefreshUnlockCandidates @12804; RaisePropertyChanged @12805; nameof @12805; LoadReportDataAsync @12809; LoadTeamsStaffAsync @12810; SafeError @12814 | No extracted literal effects. |
| <span id="m-91247ed2cac2"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>12818–12882 | FirstOrDefault @12820; CreateCommand @12827; CreateParameter @12839; ToString @12841; Add @12842; ExecuteReader @12844; Read @12845; Parse @12847; GetString @12847; GetInt64 @12850; Pow @12852; IsDBNull @12854; Add @12875 | FROM items @12828; JOIN barcodes @12828; JOIN product_categories @12828 |
| <span id="m-7f9c722917c2"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>12884–12988 | IsNullOrWhiteSpace @12886; Trim @12889; ToList @12892; Where @12892; IsNullOrEmpty @12893; Equals @12893; ToString @12895; AddToCart @12901; CreateCommand @12917; CreateParameter @12932; Add @12935; ExecuteReader @12937; Read @12939; Parse @12941; GetString @12941; ContainsKey @12942; GetInt64 @12946; Pow @12948; IsDBNull @12950; First @12977; Add @12978 | FROM items @12918; JOIN barcodes @12918; JOIN product_categories @12918 |
| <span id="m-22064f0cc685"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>12990–13033 | IsNullOrWhiteSpace @12992; Trim @12995; AppendReceiveSerialScan @13001; TryAddUniqueExactMatchToCart @13007; Clear @13009; ToList @13014; Where @13014; Equals @13014; AddToCart @13017 | No extracted literal effects. |

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
