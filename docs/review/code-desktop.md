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

<code>Software/src/GetSeek.Desktop/Models/UiModels.cs</code> · 913 lines.

SHA-256: <code>f90c09bf8b88327e87e932397054fe6784c7aa1650699335de224e181cc05d12</code>.

Declarations: <code>CurrencyFormatter</code> (line 6), <code>CategoryItem : ReactiveObject</code> (line 20), <code>ProductCategoryOption</code> (line 48), <code>ExpenseCategoryOption</code> (line 65), <code>ProductPurposeOption</code> (line 80), <code>UomOption</code> (line 85), <code>StoreUomPreferenceItem : ReactiveObject</code> (line 139), <code>ProductItem : ReactiveObject</code> (line 161), <code>OrderItem : ReactiveObject</code> (line 194), <code>ParkedCart</code> (line 305), <code>StaleCartPriceReviewUiRow</code> (line 319), <code>LotCandidateItem</code> (line 327), <code>SerialCandidateItem : ReactiveObject</code> (line 342), <code>OrderStatusChip : ReactiveObject</code> (line 366), <code>OrderLogItem : ReactiveObject</code> (line 406), <code>InventoryItem : ReactiveObject</code> (line 437), <code>KitComponentDraftItem : ReactiveObject</code> (line 591), <code>PayrollMonthOption : IEquatable&lt;PayrollMonthOption&gt;</code> (line 623), <code>StaffMember : ReactiveObject</code> (line 647), <code>TeamMemberShiftItem : ReactiveObject</code> (line 707), <code>UserPermissionOverrideItem : ReactiveObject</code> (line 718), <code>ReportTenderItem : ReactiveObject</code> (line 776), <code>ShiftReportSummary : ReactiveObject</code> (line 785), <code>FacilityItem : ReactiveObject</code> (line 825), <code>BinLocationItem : ReactiveObject</code> (line 835), <code>ItemLocationEligibilityItem : ReactiveObject</code> (line 849), <code>ReceiveTrackingKind</code> (line 864), <code>ReceiveLineItem : ReactiveObject</code> (line 876).

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
| <span id="m-9ac9f66a88ca"></span><code>PayrollMonthOption.Equals(PayrollMonthOption?)</code><br>636–637 | — | No extracted literal effects. |
| <span id="m-ac5bb8bced2e"></span><code>PayrollMonthOption.Equals(object?)</code><br>639–640 | Equals @640 | No extracted literal effects. |
| <span id="m-4db4ef5498e1"></span><code>PayrollMonthOption.GetHashCode()</code><br>642–642 | GetHashCode @642 | No extracted literal effects. |
| <span id="m-ce943f3ac98b"></span><code>PayrollMonthOption.ToString()</code><br>644–644 | — | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Services/UiPreferencesService.cs</code> · 4,847 lines.

SHA-256: <code>ccdb5222ae402837ed7a2c1a58f03a6fbb80b0dcf8d9f916326b030e11fc3fc5</code>.

Declarations: <code>UiPreferences</code> (line 12), <code>IUiPreferencesService</code> (line 20), <code>UiPreferencesService : IUiPreferencesService</code> (line 30), <code>ILocalizationService</code> (line 86), <code>LocalizationService : ILocalizationService</code> (line 96), <code>ThemeManager</code> (line 4738).

<details markdown>
<summary>Methods, calls, table effects and failures (12)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-69a3b01d8029"></span><code>IUiPreferencesService.Load()</code><br>22–22 | — | No extracted literal effects. |
| <span id="m-592fdd3892e2"></span><code>IUiPreferencesService.Save(UiPreferences)</code><br>23–23 | — | No extracted literal effects. |
| <span id="m-c2b8dbfc95d6"></span><code>UiPreferencesService.Load()</code><br>47–64 | Exists @51; ReadAllText @53; Deserialize(UiPreferences) @54 | No extracted literal effects. |
| <span id="m-7261564d0166"></span><code>UiPreferencesService.Save(UiPreferences)</code><br>66–82 | GetDirectoryName @70; IsNullOrEmpty @71; CreateDirectory @73; WriteAllText @76; Serialize @76 | No extracted literal effects. |
| <span id="m-6065c0c3e12d"></span><code>ILocalizationService.Localize(string,object?[])</code><br>89–89 | — | No extracted literal effects. |
| <span id="m-7b8b12a62ebb"></span><code>LocalizationService.Localize(string,object?[])</code><br>4705–4735 | ToLowerInvariant @4707; Trim @4707; TryGetValue @4715; TryGetValue @4718; Format @4728 | No extracted literal effects. |
| <span id="m-7036048311f3"></span><code>ThemeManager.Resolve(string?)</code><br>4755–4756 | IsNullOrWhiteSpace @4756; ContainsKey @4756 | No extracted literal effects. |
| <span id="m-0bd68d4887d1"></span><code>ThemeManager.DisplayName(string?)</code><br>4758–4758 | Resolve @4758 | No extracted literal effects. |
| <span id="m-26103399fa9c"></span><code>ThemeManager.NextTheme(string?)</code><br>4761–4774 | Equals @4766 | No extracted literal effects. |
| <span id="m-3f3bfe8f6106"></span><code>ThemeManager.Apply(string?)</code><br>4777–4811 | Equals @4780; Resolve @4782; SwapThemeSlot @4796; CheckAccess @4801; Post @4803; ApplyCore @4807 | No extracted literal effects. |
| <span id="m-e52763bd7b92"></span><code>ThemeManager.IsThemeInclude(object)</code><br>4814–4816 | Contains @4816 | No extracted literal effects. |
| <span id="m-7c5579b20e25"></span><code>ThemeManager.SwapThemeSlot(IList&lt;IResourceProvider&gt;,string)</code><br>4818–4841 | ToList(ResourceInclude) @4822; Where(ResourceInclude) @4822; OfType(ResourceInclude) @4822; Remove @4824; Equals @4829; Add @4840 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.ThirdParties.cs</code> · 4,956 lines.

SHA-256: <code>9bb014c6b2568afcf3f7c8517526d16c38c8015c753ef92a1b2c0c2b00ebdc0f</code>.

Declarations: <code>MainViewModel</code> (line 32), <code>ThirdPartyFormSnapshot</code> (line 160), <code>ItemTierPricingRow : ReactiveObject</code> (line 4731), <code>PricingRoundingOption</code> (line 4883), <code>PricingIncrementOption</code> (line 4884), <code>PricingMethodOption</code> (line 4885), <code>PricingCostBasisOption</code> (line 4886), <code>CategoryPricingPreviewProduct</code> (line 4887), <code>TierWeightModeOption</code> (line 4891), <code>PriceOfferRow</code> (line 4893), <code>PendingShelfLabelRow : ReactiveObject</code> (line 4914), <code>KitPriceAlertRow</code> (line 4936).

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
| <span id="m-3650c34e7a63"></span><code>MainViewModel.Localize(string,object?[])</code><br>3597–3597 | Localize @3597 | No extracted literal effects. |
| <span id="m-2a26c6a9d15e"></span><code>MainViewModel.RaiseLocalizedLabels()</code><br>3603–4358 | RaisePropertyChanged @3605; nameof @3605; RefreshManufacturingLocalization @4109; RefreshTraceabilityLocalization @4110; RefreshCommercialLocalization @4111; RefreshImportLocalization @4112 | No extracted literal effects. |
| <span id="m-2f8cae36ab9e"></span><code>MainViewModel.RefreshThirdPartyList()</code><br>4363–4370 | Clear @4365; Add @4368 | No extracted literal effects. |
| <span id="m-c6d475fca489"></span><code>MainViewModel.NullIfBlank(string?)</code><br>4372–4372 | IsNullOrWhiteSpace @4372; Trim @4372 | No extracted literal effects. |
| <span id="m-dd1e40178361"></span><code>MainViewModel.ParsePercent(string?)</code><br>4374–4375 | TryParse @4375 | No extracted literal effects. |
| <span id="m-0a098a7a6082"></span><code>MainViewModel.ParseStoredPricingPercentForDisplay(string?,int)</code><br>4377–4378 | ParseStoredPercentage @4378 | No extracted literal effects. |
| <span id="m-f0f04ac7274c"></span><code>MainViewModel.IsIncrementRoundingRule(string?)</code><br>4380–4382 | Equals @4381 | No extracted literal effects. |
| <span id="m-d358a0570836"></span><code>MainViewModel.ParseDate(string?)</code><br>4384–4385 | TryParse @4385 | No extracted literal effects. |
| <span id="m-b42d65599bf7"></span><code>MainViewModel.OpenNewPriceOffer()</code><br>4483–4493 | ToString @4487; ToString @4488; AddDays @4488; FirstOrDefault @4490 | No extracted literal effects. |
| <span id="m-6b41aa7df3c5"></span><code>MainViewModel.OpenEditPriceOfferAsync(PriceOfferRow)</code><br>4495–4518 | CreateCommand @4498; CreateParameter @4501; ToString @4501; Add @4501; ConfigureAwait @4502; ExecuteReaderAsync @4502; ReadAsync @4502; Parse @4503; GetString @4503; GetInt32 @4503; IsDBNull @4505; TryParse @4505; ToString @4505; ToUniversalTime @4505; ToString @4505; ToUniversalTime @4506; AddDays @4506; FirstOrDefault @4508; TryParse @4510; FirstOrDefault @4511; Pow @4514; GetInt64 @4515 | FROM price_offers @4498; JOIN items @4498 |
| <span id="m-9587537ee2ae"></span><code>MainViewModel.SavePriceOfferAsync()</code><br>4520–4537 | CheckSessionUnlocked @4522; TryParse @4523; ToString @4523; Round @4523; Pow @4523; IsNullOrWhiteSpace @4524; ConfigureAwait(SavePriceOfferCommand, Guid) @4533; ExecuteAsync(SavePriceOfferCommand, Guid) @4533; ReportError @4534; DispatchToUi @4535; ConfigureAwait @4536; LoadPriceOffersAsync @4536 | No extracted literal effects. |
| <span id="m-cbb776b6493e"></span><code>MainViewModel.TogglePriceOfferAsync(PriceOfferRow)</code><br>4539–4547 | CheckSessionUnlocked @4541; ConfigureAwait(SetPriceOfferStatusCommand, bool) @4543; ExecuteAsync(SetPriceOfferStatusCommand, bool) @4543; ReportError @4545; ConfigureAwait @4546; LoadPriceOffersAsync @4546 | No extracted literal effects. |
| <span id="m-505b3bdf682b"></span><code>MainViewModel.LoadPriceOffersAsync()</code><br>4549–4588 | CreateCommand @4554; ConfigureAwait @4564; ExecuteReaderAsync @4564; ReadAsync @4565; Add @4567; Parse @4568; GetString @4568; GetDouble @4572; GetInt64 @4575; IsDBNull @4576; GetInt32 @4578; DispatchToUi @4581; Clear @4583; Add @4584 | FROM price_offers @4555; JOIN items @4555; JOIN product_categories @4555 |
| <span id="m-38682ee37bb5"></span><code>MainViewModel.LoadPendingShelfLabelsAsync()</code><br>4590–4629 | CreateCommand @4595; ConfigureAwait @4604; ExecuteReaderAsync @4604; ReadAsync @4605; Add @4607; Parse @4608; GetString @4608; GetInt64 @4612; GetInt32 @4617; Add @4618; Remove @4618; RaisePropertyChanged @4618; nameof @4618; Localize @4619; DispatchToUi @4622; Clear @4624; Add @4625 | FROM pending_shelf_labels @4596; JOIN items @4596 |
| <span id="m-55cac059ca04"></span><code>MainViewModel.LoadKitPriceReviewAlertsAsync()</code><br>4631–4670 | CreateCommand @4636; ConfigureAwait @4648; ExecuteReaderAsync @4648; ReadAsync @4649; Add @4651; Parse @4652; GetString @4652; GetInt64 @4656; GetInt32 @4660; DispatchToUi @4663; Clear @4665; Add @4666 | FROM kit_price_review_alerts @4637; JOIN items @4637 |
| <span id="m-c0c00fb48972"></span><code>MainViewModel.SetKitPriceAlertStatusAsync(KitPriceAlertRow,string,string)</code><br>4672–4680 | CheckSessionUnlocked @4674; ConfigureAwait(ResolveKitPriceAlertCommand, bool) @4675; ExecuteAsync(ResolveKitPriceAlertCommand, bool) @4675; ReportError @4677; ConfigureAwait @4679; LoadKitPriceReviewAlertsAsync @4679 | No extracted literal effects. |
| <span id="m-c6afa4616e31"></span><code>MainViewModel.MarkShelfLabelsPrintedAsync()</code><br>4682–4685 | ConfigureAwait @4684; SetSelectedShelfLabelStatusAsync @4684 | No extracted literal effects. |
| <span id="m-a9edff8710af"></span><code>MainViewModel.QueueSelectedShelfLabelsAsync()</code><br>4687–4699 | CheckSessionUnlocked @4689; ToArray @4690; Select @4690; Where @4690; Contains @4690; ConfigureAwait(QueueShelfLabelPrintCommand, string) @4693; ExecuteAsync(QueueShelfLabelPrintCommand, string) @4693; ReportError @4695; Clear @4696; RaisePropertyChanged @4696; nameof @4696; ConfigureAwait @4698; LoadPendingShelfLabelsAsync @4698 | No extracted literal effects. |
| <span id="m-6a6c87277f16"></span><code>MainViewModel.SetSelectedShelfLabelStatusAsync(string)</code><br>4701–4715 | CheckSessionUnlocked @4703; ToArray @4704; Select @4704; Where @4704; Contains @4704; ConfigureAwait(SetShelfLabelStatusCommand, int) @4707; ExecuteAsync(SetShelfLabelStatusCommand, int) @4707; Trim @4708; ReportError @4710; Clear @4711; RaisePropertyChanged @4712; nameof @4712; ConfigureAwait @4714; LoadPendingShelfLabelsAsync @4714 | No extracted literal effects. |
| <span id="m-278d46af60f0"></span><code>MainViewModel.AddSqlParam(DbCommand,string,object)</code><br>4721–4727 | CreateParameter @4723; Add @4726 | No extracted literal effects. |
| <span id="m-a6edd81b756b"></span><code>ItemTierPricingRow.RecalculateEffectivePrice()</code><br>4859–4880 | Max @4864; TryParse @4873 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 13,603 lines.

SHA-256: <code>e9357edd6ec1d3acab1d01b263805ad1999a4f9d3eaa2932289fc77b94aeaa82</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 8911).

<details markdown>
<summary>Methods, calls, table effects and failures (258)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4d3c549b9d46"></span><code>MainViewModel.RefreshCurrentTime()</code><br>121–121 | RaisePropertyChanged @121; nameof @121 | No extracted literal effects. |
| <span id="m-47378cde4176"></span><code>MainViewModel.SetStatusNotificationOnUi(string)</code><br>391–404 | RaiseAndSetIfChanged @393; IsNullOrWhiteSpace @394; Insert @396; RemoveAt @397; RaisePropertyChanged @398; nameof @398; Stop @401; Start @403 | No extracted literal effects. |
| <span id="m-fa69ff5d121c"></span><code>MainViewModel.ClearNotifications()</code><br>426–433 | Stop @428; Clear @430; RaisePropertyChanged @431; nameof @431; RaiseAndSetIfChanged @432 | No extracted literal effects. |
| <span id="m-22bc8b985b15"></span><code>MainViewModel.CycleInventoryLifecycleStatusScope()</code><br>691–696 | — | No extracted literal effects. |
| <span id="m-e3c36273b1fc"></span><code>MainViewModel.IsLockScreenLockedOut(int)</code><br>1210–1226 | Ceiling @1217 | No extracted literal effects. |
| <span id="m-4c275cc37ee9"></span><code>MainViewModel.RefreshUnlockCandidates()</code><br>1268–1293 | GetUnlockCandidates @1271; Clear @1274; Add @1277; Any @1279; CheckAccess @1285; action @1287; Post @1291 | No extracted literal effects. |
| <span id="m-f8afbfa12927"></span><code>MainViewModel.UpdateReceiveKitBreakdownAsync()</code><br>1651–1671 | GetValueOrDefault @1659; ConfigureAwait @1664; BuildBreakdownSummaryAsync @1664 | No extracted literal effects. |
| <span id="m-8c4a2131dbb3"></span><code>MainViewModel.UpdateCartKitBreakdownAsync(OrderItem)</code><br>1673–1685 | ConfigureAwait @1678; BuildBreakdownSummaryAsync @1678 | No extracted literal effects. |
| <span id="m-b28b42f765a9"></span><code>MainViewModel.OnProductPricingDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>2155–2174 | RaisePropertyChanged @2157; nameof @2157; RecomputeProductPricingPreview @2173 | No extracted literal effects. |
| <span id="m-d35a32974b93"></span><code>MainViewModel.RecomputeProductPricingPreview()</code><br>2183–2233 | Clear @2185; RaisePropertyChanged @2186; nameof @2186; ToMinorUnits @2195; Parse @2200; TryParse @2204; Equals @2218; Increment @2221; Localize @2222; ToArray @2224; RecomputeKitPricingPreviewAsync @2225; ResolveSelectedProductSaleUnitFactor @2230; Round @2231; RebuildProductPricingPreview @2232 | No extracted literal effects. |
| <span id="m-d4735ed65fb0"></span><code>MainViewModel.RecomputeKitPricingPreviewAsync(long,string,string,decimal,string,long,decimal,IReadOnlyList&lt;KitComponentDraftItem&gt;)</code><br>2235–2305 | ConfigureAwait @2239; WaitAsync @2239; Read @2242; DispatchToUi @2246; SetProductPricingPreviewNotice @2246; CalculateItemOrKitAsync @2260; ResolveSelectedProductSaleUnitFactor @2284; Round @2285; RebuildProductPricingPreview @2289; Release @2303 | No extracted literal effects. |
| <span id="m-98b20a87689b"></span><code>MainViewModel.SetProductPricingPreviewNotice(string)</code><br>2307–2311 | Localize @2309; RaisePropertyChanged @2310; nameof @2310 | No extracted literal effects. |
| <span id="m-8083f33166b4"></span><code>MainViewModel.RebuildProductPricingPreview(long,string,decimal,string,long,decimal)</code><br>2313–2377 | Clear @2316; RaisePropertyChanged @2318; nameof @2318; Equals @2319; SetProductPricingPreviewNotice @2321; ParsePricingMethod @2325; ParseRoundingRule @2326; IsRoundingRuleCompatible @2327; TryConvertRoundingIncrement @2334; ToMinorUnits @2341; ResolveEffectiveBasePrice @2342; ToList @2346; OrderBy @2346; Where @2346; FirstOrDefault @2353; TryParse @2364; ToString @2365; ResolveTierPrice @2368; Add @2370; Format @2372; ToDisplayAmount @2372; FirstOrDefault @2373 | No extracted literal effects. |
| <span id="m-53cfd37fd349"></span><code>MainViewModel.ResolveSelectedProductSaleUnitFactor()</code><br>2431–2446 | FirstOrDefault @2434; Equals @2434; TryParse @2438 | No extracted literal effects. |
| <span id="m-bb01abdc1623"></span><code>MainViewModel.ExactMinorToCurrency(decimal)</code><br>2454–2455 | ScalingFactor @2455; Clamp @2455 | No extracted literal effects. |
| <span id="m-fa05530c28d0"></span><code>MainViewModel.BuildCostSourcesTooltip(long,long,long,long?,string,DateTime?)</code><br>2512–2532 | Format @2520; ToDecimal @2521; Localize @2524; Format @2524; ToLocalTime @2526; Join @2531 | No extracted literal effects. |
| <span id="m-46c275d509f0"></span><code>MainViewModel.AddKitComponent()</code><br>2692–2729 | IsNullOrWhiteSpace @2707; FirstOrDefault @2709; Equals @2710; Add @2717; RaisePropertyChanged @2728; nameof @2728 | No extracted literal effects. |
| <span id="m-3b4d32b5918d"></span><code>MainViewModel.RemoveKitComponent(KitComponentDraftItem?)</code><br>2731–2738 | Remove @2735; RaisePropertyChanged @2736; nameof @2736 | No extracted literal effects. |
| <span id="m-26195fd22361"></span><code>MainViewModel.RefreshVirtualKitAvailability()</code><br>2749–2762 | Increment @2751; ToArray @2758; Select @2758; LoadVirtualKitAvailabilityAsync @2761 | No extracted literal effects. |
| <span id="m-66f7ee567d29"></span><code>MainViewModel.LoadVirtualKitAvailabilityAsync(long,IReadOnlyList&lt;KitComponentInput&gt;)</code><br>2764–2804 | ConfigureAwait @2768; GetKitAvailabilityAsync @2768; DispatchToUi @2770; Read @2772; Localize @2775; Max @2784; ResolveSelectedProductSaleUnitFactor @2784; GetValueOrDefault @2785; Clamp @2786; Pow @2787; Floor @2788; Format @2790; ToString @2792 | No extracted literal effects. |
| <span id="m-09d68b81c2c3"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3653–3661 | IsNullOrWhiteSpace @3655 | No extracted literal effects. |
| <span id="m-69cf77e251cf"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3663–3674 | Load @3665; IsNullOrWhiteSpace @3669; Resolve @3671; Apply @3673 | No extracted literal effects. |
| <span id="m-cee5d2b446d5"></span><code>MainViewModel.OpenImport()</code><br>3703–3711 | CheckSessionUnlocked @3705; Increment @3707; ResetInventoryImport @3708; Invoke @3710 | No extracted literal effects. |
| <span id="m-35714b4c5285"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3713–3774 | Increment @3716; ResetInventoryImport @3721; IsNullOrWhiteSpace @3726; Exists @3726; FinishFailedImport @3728; ConfigureAwait @3740; ReadAllBytesAsync @3740; ToHexString @3741; HashData @3741; TemplateContextAsync @3745; Run @3746; Read @3746; ValidateInventoryAsync @3747; CompletedWorkbook @3748; DispatchToUi @3755; ReferenceEquals @3757; Add @3758; Localize @3759; SetImportReviewRows @3763; RaisePropertyChanged @3764; nameof @3764; ReportException @3770 | No extracted literal effects. |
| <span id="m-db2d07f42965"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3776–3830 | IsCurrentImportAttempt @3792; ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3806; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3806; ConfigureAwait @3810; RecoverImportOutcomeAsync @3810; Localize @3813; DispatchToUi @3814; FinishImportAttempt @3814; LoadInventoryAsync @3815; ReportException @3816; ReportError @3820; FinishFailedImport @3821; ImportCommandIssue @3821 | No extracted literal effects. |
| <span id="m-04b72b64f3c9"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3842–3852 | Report @3844; DispatchToUi @3845; Insert @3847 | No extracted literal effects. |
| <span id="m-a97b9d0f3033"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3854–3858 | RaisePropertyChanged @3857; nameof @3857 | No extracted literal effects. |
| <span id="m-a6b687d0a0c1"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3860–3863 | ReportError @3862 | No extracted literal effects. |
| <span id="m-456df3f820eb"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3869–3874 | ReportError @3872 | No extracted literal effects. |
| <span id="m-27fe16516f9b"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3883–3889 | IsNullOrWhiteSpace @3885; Trim @3885; ReportError @3887 | No extracted literal effects. |
| <span id="m-17135715318f"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3891–3894 | DispatchToUi @3893; Insert @3893 | No extracted literal effects. |
| <span id="m-cc3cf8e9629e"></span><code>MainViewModel.DispatchToUi(Action)</code><br>3900–3914 | CheckAccess @3902; action @3904; GetResult @3912; GetAwaiter @3912; InvokeAsync @3912 | No extracted literal effects. |
| <span id="m-08adc67fcc90"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4581–4646 | Register @4583; Execute @4583; Execute @4584; Execute @4585; Execute @4586; Execute @4591; Execute @4592; Execute @4593; Execute @4594; Execute @4595; Execute @4596; Execute @4597; Execute @4598; Execute @4599; Execute @4600; Execute @4601; Execute @4602; Execute @4603; Execute @4604; Execute @4605; Execute @4606; Execute @4607; Execute @4608; Execute @4609; Execute @4610; Execute @4611; Execute @4612; Execute @4613; Execute @4614; Execute @4615; Execute @4616; Execute @4617; Execute @4618; Execute @4619; Execute @4620; Execute @4621; Execute @4622; Execute @4624; Execute @4625; RequestClosePersonForm @4626; KeepEditingPersonForm @4627; CloseSalaryMonthDetailModal @4628; CloseSalaryPaymentModal @4629; CloseSalaryAdjustmentModal @4630; CloseSalaryFinalizeModal @4631; RequestCloseExpenseForm @4632; KeepEditingExpenseForm @4633; CloseExpenseCategoryModal @4634; CloseExpensePaymentModal @4635; CloseExpenseDetailModal @4636; ClosePaymentReturnModal @4637; CloseWasteExpenseConfirmation @4638; InitializeSalaryTables @4643; InitializeExpensesTables @4644; InitializeTeamsCommands @4645 | No extracted literal effects. |
| <span id="m-6ac33b89926f"></span><code>MainViewModel.CreateDemo()</code><br>4648–4655 | SetActiveCashier @4651; Parse @4651; RefreshUnlockCandidates @4653 | No extracted literal effects. |
| <span id="m-35a4e344c539"></span><code>MainViewModel.CreateInitializing()</code><br>4657–4665 | — | No extracted literal effects. |
| <span id="m-63eac7ccebc9"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4667–4677 | — | No extracted literal effects. |
| <span id="m-e902129afca7"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4679–4697 | ConfigureDiagnosticsWorkspace @4693; ResolveDiagnosticsWorkspace @4693; ApplyPersistedState @4694; RefreshUnlockCandidates @4695 | No extracted literal effects. |
| <span id="m-5bcfdd0a6c72"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4699–4727 | CheckSessionUnlocked @4701; HasPermission @4702; Equals @4713; GetFileNameWithoutExtension @4713; GetEntryAssembly @4715; Add @4717; Start @4720; ReportException @4725 | No extracted literal effects. |
| <span id="m-fad5d23af38f"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4729–4752 | CheckSessionUnlocked @4731; HasPermission @4732; Equals @4742; GetFileNameWithoutExtension @4742; Add @4743; GetEntryAssembly @4743; Start @4745; ReportException @4750 | No extracted literal effects. |
| <span id="m-df38a2ba68d9"></span><code>MainViewModel.Dispose()</code><br>4754–4775 | ClearImportResults @4757; Increment @4758; ResetFinancialWorkspace @4760; Dispose @4761; Stop @4762; CancelBatchPricingPreviewExpiry @4765; Dispose @4766; Dispose @4767; DisposeSearchStates @4773; SuppressFinalize @4774 | No extracted literal effects. |
| <span id="m-c9a17e7242c4"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4777–4781 | Stop @4779 | No extracted literal effects. |
| <span id="m-170a5e368028"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4783–4821 | Clear @4793; Clear @4794; Clear @4795; Clear @4796; Clear @4797; Clear @4798; Clear @4799; Clear @4800; Clear @4801; Clear @4802 | No extracted literal effects. |
| <span id="m-ecf2a0d5c4eb"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4823–4939 | RaisePropertyChanged @4837; nameof @4837; Clear @4839; Clear @4840; Clear @4841; CreateCommand @4848; ExecuteReader @4850; Read @4851; TryParse @4853; GetString @4853; Add @4854; Add @4862; GroupBy @4863; Count @4865; Contains @4870; Add @4894; ApplyFilter @4896; All @4898; SafeError @4901; SetActiveCashier @4909; ToString @4913; ToString @4916; ToLocalTime @4916; NotifyTotalsChanged @4938 | FROM item_kits @4849 |
| <span id="m-078f11684711"></span><code>MainViewModel.InitializeDemoData()</code><br>4941–5018 | Add @4947; Add @4966; ApplyFilter @4977; Add @4980; Add @4985; Add @4991; ApplyActivityFilter @4997; Add @5000; ApplyInventoryFilter @5009; Add @5012; Parse @5012; NotifyTotalsChanged @5017 | No extracted literal effects. |
| <span id="m-3e317e855406"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>5020–5033 | — | No extracted literal effects. |
| <span id="m-3155e4e42401"></span><code>MainViewModel.SelectMenu(string)</code><br>5035–5108 | CheckSessionUnlocked @5037; NormalizeMenuKey @5041; LoadInvoicesAsync @5047; LoadCommercialAsync @5048; LoadActivityInvoicesAsync @5055; LoadTeamsStaffAsync @5058; LoadCatalogRegistryAsync @5059; UpdateDemoSeedingAvailabilityAsync @5062; UpdateReceiptDesignPreview @5065; RefreshDiagnosticsAsync @5066; LoadPriceLevelSettingsAsync @5067; RefreshWorkspaceCategories @5071; LoadInventoryAsync @5072; LoadPriceProposalsAsync @5074; LoadReportDataAsync @5077; LoadFinancialRegisterAsync @5078; LoadCustomersAsync @5081; LoadSuppliersAsync @5082; LoadThirdPartiesAsync @5083; LoadManufacturingDataAsync @5088; LoadManagedUnitsAsync @5096; LoadManagedCategoriesAsync @5099; LoadSalaryWorkspaceAsync @5102; LoadExpensesWorkspaceAsync @5105 | No extracted literal effects. |
| <span id="m-f31d96aa313b"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>5110–5129 | — | No extracted literal effects. |
| <span id="m-f1fc3e761538"></span><code>MainViewModel.LogOut()</code><br>5131–5152 | Clear @5133; RaisePropertyChanged @5136; nameof @5136; ClearNotifications @5138; ResetCashReview @5142; Lock @5145; RefreshUnlockCandidates @5150; UpdateDemoSeedingAvailabilityAsync @5151 | No extracted literal effects. |
| <span id="m-3471c4d576eb"></span><code>MainViewModel.UnlockSession()</code><br>5154–5157 | UnlockSession @5156 | No extracted literal effects. |
| <span id="m-aa048a4a24ad"></span><code>MainViewModel.UnlockSession(string?)</code><br>5159–5258 | IsLockScreenLockedOut @5167; IsNullOrWhiteSpace @5183; AuthenticateSelectedUser @5192; Lock @5197; AddSeconds @5203; AddMinutes @5220; Initialize @5239; Unlock @5240; Any @5244; Equals @5244; RaisePropertyChanged @5245; nameof @5245; LoadActivityInvoicesAsync @5249; LoadTrackOrdersAsync @5250; UpdateDemoSeedingAvailabilityAsync @5251; StartAutomaticDemoDatasetLoadAsync @5252 | No extracted literal effects. |
| <span id="m-85b2b737f45a"></span><code>MainViewModel.PowerAction()</code><br>5260–5266 | CheckSessionUnlocked @5262 | No extracted literal effects. |
| <span id="m-8ebce606837a"></span><code>MainViewModel.CycleTable()</code><br>5268–5274 | CheckSessionUnlocked @5270 | No extracted literal effects. |
| <span id="m-19f94abd1c46"></span><code>MainViewModel.CycleDiningType()</code><br>5276–5282 | CheckSessionUnlocked @5278 | No extracted literal effects. |
| <span id="m-8263b1d0eae5"></span><code>MainViewModel.CycleCustomer()</code><br>5284–5287 | OpenCustomerChooser @5286 | No extracted literal effects. |
| <span id="m-7df680fce55a"></span><code>MainViewModel.OpenPromoDialog()</code><br>5289–5304 | CheckSessionUnlocked @5291; IsNullOrWhiteSpace @5298; RaisePropertyChanged @5302; nameof @5302 | No extracted literal effects. |
| <span id="m-3259204470c8"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5306–5375 | CheckSessionUnlocked @5308; ToLowerInvariant @5321; Trim @5321; IsNullOrWhiteSpace @5328; Trim @5328; ToList @5336; Select @5336; ToMinorUnits @5340; Equals @5356; Calculate @5360; NotifyTotalsChanged @5372; ConfigureAwait @5374; SaveDurableCartAsync @5374 | No extracted literal effects. |
| <span id="m-d84fc0f8d9cb"></span><code>MainViewModel.TogglePromo()</code><br>5377–5394 | CheckSessionUnlocked @5379; RemovePromo @5388; OpenPromoDialog @5392 | No extracted literal effects. |
| <span id="m-fb59a76c8a04"></span><code>MainViewModel.RemovePromo()</code><br>5396–5406 | NotifyTotalsChanged @5403; SaveDurableCartAsync @5405 | No extracted literal effects. |
| <span id="m-e53095fe8337"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5408–5419 | CheckSessionUnlocked @5410; NotifyTotalsChanged @5416; ConfigureAwait @5418; SaveDurableCartAsync @5418 | No extracted literal effects. |
| <span id="m-85154752275c"></span><code>MainViewModel.CancelPromoDialog()</code><br>5421–5425 | — | No extracted literal effects. |
| <span id="m-b6e3eae1e321"></span><code>MainViewModel.RecalculateCart()</code><br>5427–5481 | ToMinorUnits @5443; Add @5444; Equals @5465; Calculate @5469; ToDictionary @5472; TryGetValue @5475 | No extracted literal effects. |
| <span id="m-1ea71dc66f9f"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5483–5490 | CheckSessionUnlocked @5485; ResetCashReview @5486 | No extracted literal effects. |
| <span id="m-034a40158670"></span><code>MainViewModel.SelectCategory(CategoryItem?)</code><br>5492–5532 | CheckSessionUnlocked @5494; RaisePropertyChanged @5502; nameof @5502; ApplyFilter @5503 | No extracted literal effects. |
| <span id="m-fb781c745fb7"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5534–5534 | AddToCart @5534 | No extracted literal effects. |
| <span id="m-92c655815505"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5536–5580 | CheckSessionUnlocked @5538; ResetCashReview @5539; ResolveProductSaleUnitFactor @5542; Round @5549; FirstOrDefault @5550; UpdateCartKitBreakdownAsync @5559; Add @5571; NotifyTotalsChanged @5574; SaveDurableCartAsync @5576; IsNullOrWhiteSpace @5578; ToString @5578; NewGuid @5578; RecordSuccessfulSearchUseAsync @5579; FromGuid @5579 | No extracted literal effects. |
| <span id="m-673dd7eb26ac"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5582–5595 | CheckSessionUnlocked @5584; ResetCashReview @5585; UpdateCartKitBreakdownAsync @5592; NotifyTotalsChanged @5593; SaveDurableCartAsync @5594 | No extracted literal effects. |
| <span id="m-384d13e7dcae"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5597–5612 | CheckSessionUnlocked @5599; ResetCashReview @5600; UpdateCartKitBreakdownAsync @5604; Remove @5608; NotifyTotalsChanged @5610; SaveDurableCartAsync @5611 | No extracted literal effects. |
| <span id="m-338b8ae4594f"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5614–5620 | ConfigureAwait @5617; LoadAsync @5617; RefreshSavedPaymentImages @5618; CancelManualPaymentSettings @5619 | No extracted literal effects. |
| <span id="m-c33416d0b032"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5622–5651 | ValidImage @5629; CreatePaymentBitmap @5634; Dispose @5637; RaisePropertyChanged @5649; nameof @5649 | No extracted literal effects. |
| <span id="m-1eb7514c68dd"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5653–5669 | Dispose @5663; CreatePaymentBitmap @5665; RaisePropertyChanged @5667; nameof @5667 | No extracted literal effects. |
| <span id="m-83e512b0263d"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5671–5675 | — | No extracted literal effects. |
| <span id="m-fff0c331fe9d"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5677–5685 | Dispose @5679; CreatePaymentBitmap @5681; RaisePropertyChanged @5683; nameof @5683 | No extracted literal effects. |
| <span id="m-eee596517057"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5687–5706 | ConfigureAwait @5696; ExecuteAsync @5696; DispatchToUi @5699; SafePipelineError @5699; LoadAsync @5702; RefreshSavedPaymentImages @5703; CancelManualPaymentSettings @5704 | No extracted literal effects. |
| <span id="m-a6e77a62383c"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5708–5727 | IsNullOrWhiteSpace @5712; Trim @5713; ToMinorUnits @5719; ConfigureAwait @5725; PlaceOrderAsync @5725 | No extracted literal effects. |
| <span id="m-bb5fc232d018"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5729–5741 | PlaceOrderInternalAsync @5735 | No extracted literal effects. |
| <span id="m-bad8990e6da8"></span><code>MainViewModel.PlaceOrderInternalAsync()</code><br>5743–5944 | Localize @5747; ExecuteDemoPlaceOrder @5753; ConfigureAwait @5779; SaveDurableCartAsync @5779; ToMinorUnits @5787; Trim @5789; Equals @5800; Equals @5807; ResetCashReview @5809; Max @5867; Add @5872; ConfigureAwait(TakePaymentCommand, SalesInvoice) @5890; ExecuteAsync(TakePaymentCommand, SalesInvoice) @5890; Format @5902; ToDecimal @5902; DispatchToUi @5904; Clear @5908; NewGuid @5917; NotifyTotalsChanged @5918; LoadActivityInvoicesAsync @5925; OpenStaleCartPriceReviewAsync @5930; RequestElevationForCheckout @5932; SafePipelineError @5936; SafeError @5942 | No extracted literal effects. |
| <span id="m-90a3e524cf83"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>5946–5978 | DispatchToUi @5950; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5953; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5953; SafePipelineError @5958; ToArray @5962; Select @5962; Where @5962; FormatCartReviewMoney @5966; Clear @5973; Add @5974 | No extracted literal effects. |
| <span id="m-a44587809ebd"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>5980–5985 | ScalingFactor @5982; Format @5984; Equals @5984 | No extracted literal effects. |
| <span id="m-7113bf7c2e98"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>5987–6018 | CheckSessionUnlocked @5989; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5991; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5991; DispatchToUi @5996; SafePipelineError @5996; ConfigureAwait @5997; OpenStaleCartPriceReviewAsync @5997; FirstOrDefault @6004; ScalingFactor @6007; ResetCashReview @6011; Clear @6014; NotifyTotalsChanged @6015 | No extracted literal effects. |
| <span id="m-6bd94efd7c99"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>6020–6027 | Clear @6024; ResetCashReview @6025 | No extracted literal effects. |
| <span id="m-bc2a79def604"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>6029–6055 | CheckSessionUnlocked @6031; ResetCashReview @6038; ToMinorUnits @6049; ConfigureAwait @6054; PlaceOrderAsync @6054 | No extracted literal effects. |
| <span id="m-29c89a596852"></span><code>MainViewModel.CancelCashReview()</code><br>6057–6061 | ResetCashReview @6059 | No extracted literal effects. |
| <span id="m-0e8d97261491"></span><code>MainViewModel.ResetCashReview()</code><br>6063–6072 | — | No extracted literal effects. |
| <span id="m-94afce6ca895"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>6074–6093 | RaisePropertyChanged @6085; nameof @6085; Clear @6088; ResetCashReview @6089; NotifyTotalsChanged @6090 | No extracted literal effects. |
| <span id="m-29c58cf74344"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>6095–6160 | ConfigureAwait @6099; WaitAsync @6099; ClearActiveCartAsync @6104; ToMinorUnits @6114; Add @6115; ToUpperInvariant @6118; ToString @6118; IsNullOrWhiteSpace @6121; SaveActiveCartAsync @6134; DispatchToUi @6153; SafeError @6153; Release @6158 | No extracted literal effects. |
| <span id="m-c0eaa5606f4a"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>6162–6221 | ConfigureAwait @6168; GetActiveCartAsync @6168; Clear @6180; FirstOrDefault @6183; ToDecimal @6187; Add @6197; NotifyTotalsChanged @6214 | No extracted literal effects. |
| <span id="m-a341c1a84ccd"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>6223–6300 | ApplyPagedResult @6227; ToList @6228; ApplyActivityFilter @6232; HasPermission @6237; ConfigureAwait @6244; GetPagedActivityInvoicesAsync @6244; ToPageRequest @6247; ToDecimal @6253; Add @6254; ToString @6259; ToLocalTime @6259; DispatchToUi @6278; Clear @6280; Add @6283; SafeError @6297 | No extracted literal effects. |
| <span id="m-46fd2e83d8f1"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>6302–6379 | HasPermission @6307; ConfigureAwait @6314; GetActiveOrdersAsync @6314; Clear @6315; ToDecimal @6319; Join @6353; Select @6353; Add @6355; ToString @6370; ToLocalTime @6370 | No extracted literal effects. |
| <span id="m-1598dd07b128"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6381–6408 | CheckSessionUnlocked @6383; Clear @6386; ConfigureAwait @6392; GetOrderByIdAsync @6392; Add @6397; DispatchToUi @6403; SafeError @6403 | No extracted literal effects. |
| <span id="m-77ae0eba0277"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6410–6415 | Clear @6414 | No extracted literal effects. |
| <span id="m-d6fdeb0bf075"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6417–6450 | CheckSessionUnlocked @6419; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6435; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6435; ConfigureAwait @6444; LoadTrackOrdersAsync @6444; DispatchToUi @6448; SafePipelineError @6448 | No extracted literal effects. |
| <span id="m-79d7e8889598"></span><code>MainViewModel.MarkReadyAsync()</code><br>6452–6485 | CheckSessionUnlocked @6454; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6470; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6470; ConfigureAwait @6479; LoadTrackOrdersAsync @6479; DispatchToUi @6483; SafePipelineError @6483 | No extracted literal effects. |
| <span id="m-0493c80bd56b"></span><code>MainViewModel.MarkServedAsync()</code><br>6487–6520 | CheckSessionUnlocked @6489; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6505; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6505; ConfigureAwait @6514; LoadTrackOrdersAsync @6514; DispatchToUi @6518; SafePipelineError @6518 | No extracted literal effects. |
| <span id="m-d7de95ae5e58"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6522–6550 | CheckSessionUnlocked @6524; Remove @6528; CloseOrderDetailsModal @6529; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6538; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6538; ConfigureAwait @6544; LoadTrackOrdersAsync @6544; DispatchToUi @6548; SafePipelineError @6548 | No extracted literal effects. |
| <span id="m-6773ddcadbc8"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6552–6648 | CheckSessionUnlocked @6554; CloseOrderDetailsModal @6560; ConfigureAwait @6567; GetOrderByIdAsync @6567; Zero @6589; NewGuid @6595; ToList @6598; Select @6598; ToUpperInvariant @6601; ToString @6601; SaveActiveCartAsync @6610; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6626; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6626; DispatchToUi @6629; SafePipelineError @6629; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6635; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6635; LoadTrackOrdersAsync @6641; LoadActivityInvoicesAsync @6642 | No extracted literal effects. |
| <span id="m-d6e74198c7fb"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6650–6657 | CheckSessionUnlocked @6652 | No extracted literal effects. |
| <span id="m-c2de4f65a201"></span><code>MainViewModel.FilterActivity(string)</code><br>6676–6682 | CheckSessionUnlocked @6678; ApplyActivityFilter @6680 | No extracted literal effects. |
| <span id="m-bb4b797b139c"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6684–6723 | Clear @6686; AsEnumerable @6687; Where @6692; IsNullOrWhiteSpace @6695; Trim @6697; Contains @6699; Contains @6700; Contains @6701; IsNullOrEmpty @6705; Equals @6707; ToList @6711; Add @6713; ApplyPagedResult @6717 | No extracted literal effects. |
| <span id="m-60e291ecbad6"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6725–6761 | CheckSessionUnlocked @6727; ConfigureAwait(QueueReceiptReprintCommand, string) @6747; ExecuteAsync(QueueReceiptReprintCommand, string) @6747; IsNullOrWhiteSpace @6748; ReportError @6750; RefreshOutputStatusAsync @6755; DispatchToUi @6759; SafeError @6759 | No extracted literal effects. |
| <span id="m-2dbf10838f4f"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6763–6806 | RefreshOutputPrinterQueues @6768; ReadAsync @6769; Equals @6776; IsNullOrWhiteSpace @6776; TryReadGeometry @6778; ComputeCapabilityFingerprint @6782; ConfigureAwait @6786; InvalidateThermalVerificationAsync @6786; LoadCashFinancialSettingsAsync @6798; LoadReceiptDesignAsync @6799; RefreshOutputStatusAsync @6800; DispatchToUi @6804; SafeError @6804 | No extracted literal effects. |
| <span id="m-09a36bda7146"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6808–6834 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6821; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6821; ReportError @6824; LoadOutputDevicesAsync @6827; DispatchToUi @6832; SafeError @6832 | No extracted literal effects. |
| <span id="m-be72610b5849"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6836–6909 | Equals @6850; IsNullOrWhiteSpace @6855; IsWindows @6860; TryReadGeometry @6865; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6882; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6882; ReportError @6885; Render @6888; ToString @6889; ConfigureAwait @6890; Run @6890; Send @6890; ComputeCapabilityFingerprint @6891; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @6892; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @6892; RefreshOutputStatusAsync @6903; DispatchToUi @6907; SafeError @6907 | No extracted literal effects. |
| <span id="m-21ca2cb6afa4"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>6911–6948 | IsWindows @6925; IsNullOrWhiteSpace @6925; TryReadGeometry @6927; ComputeCapabilityFingerprint @6931; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @6932; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @6932; ReportError @6936; ConfigureAwait @6942; RefreshOutputStatusAsync @6942; DispatchToUi @6946; SafeError @6946 | InvalidOperationException @6926; InvalidOperationException @6930 |
| <span id="m-163682da893a"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>6950–6987 | CreateCommand @6955; ConfigureAwait @6964; ExecuteReaderAsync @6964; ReadAsync @6965; GetInt32 @6968; GetString @6968; GetInt64 @6968; Parse @6969; RaisePropertyChanged @6971; nameof @6971; NotifyTotalsChanged @6980; DispatchToUi @6985; SafeError @6985 | FROM store_config @6956 |
| <span id="m-ad26e7930fd5"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>6989–7017 | ConfigureAwait @7002; ExecuteAsync @7002; ReportError @7005; NotifyTotalsChanged @7010; DispatchToUi @7015; SafeError @7015 | No extracted literal effects. |
| <span id="m-1f09d55f2a4d"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>7019–7063 | DispatchToUi @7023; CreateCommand @7028; ConfigureAwait @7034; ExecuteReaderAsync @7034; ReadAsync @7035; Deserialize(ReceiptDesignDocument) @7037; GetString @7037; SafeError @7056 | FROM receipt_designs @7029; JOIN receipt_design_versions @7029 |
| <span id="m-012d45eae20a"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>7065–7092 | ConfigureAwait @7078; ExecuteAsync @7078; ReportError @7083; DispatchToUi @7090; SafeError @7090 | No extracted literal effects. |
| <span id="m-d1ee6a8daf94"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>7094–7106 | IsWindows @7096; Select @7097; Enumerate @7097; Empty(string) @7098; ToArray @7099; OrderBy @7099; Distinct @7099; Where @7099; Append @7099; IsNullOrWhiteSpace @7100; Clear @7104; Add @7105 | No extracted literal effects. |
| <span id="m-2de7910f5c75"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>7108–7166 | CheckAccess @7110; DispatchToUi @7112; CreateSampleData @7118; Equals @7124; IsWindows @7131; TryReadGeometry @7132; BuildPaperDocument @7141; RenderPreviewPngPages @7144; SetReceiptDesignPreviewPages @7146; Localize @7148; BuildThermalLines @7153; RenderPreviewPng @7155; Empty(byte[]) @7162; ReportException @7164 | No extracted literal effects. |
| <span id="m-0ac710424589"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>7168–7173 | ShowReceiptDesignPreviewPage @7172 | No extracted literal effects. |
| <span id="m-fcf45444acf9"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>7175–7181 | ShowReceiptDesignPreviewPage @7180 | No extracted literal effects. |
| <span id="m-5702636e4035"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>7183–7197 | RaisePropertyChanged @7194; nameof @7194 | No extracted literal effects. |
| <span id="m-4cec120787c0"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>7199–7228 | ReadAsync @7202; Localize @7205; CreateCommand @7207; ConfigureAwait @7209; ExecuteScalarAsync @7209; ToString @7209; IsNullOrWhiteSpace @7210; ExecuteReaderAsync @7224; ReadAsync @7225; Trim @7226; GetString @7226 | FROM hardware_jobs @7208; FROM hardware_jobs @7223 |
| <span id="m-da45fe01f161"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>7230–7250 | Clear @7232; AsEnumerable @7233; Where @7236; Equals @7236; IsNullOrWhiteSpace @7242; Contains @7244; Contains @7245; Contains @7246; Add @7249 | No extracted literal effects. |
| <span id="m-95e141a6b36d"></span><code>MainViewModel.SelectInventoryKind(string)</code><br>7252–7296 | NormalizeItemKind @7254; SelectCatalogKind @7257; Clear @7261; ClearSelection @7266; InvalidateSelectedBatchPreview @7267; IsNullOrEmpty @7270; RaisePropertyChanged @7278; nameof @7278; ResetToFirstPage @7281; NotifySelectionScopeChange @7282; SetSelectionScope @7282; InventorySelectionScope @7282; RefreshWorkspaceCategories @7285; LoadInventoryAsync @7288 | No extracted literal effects. |
| <span id="m-7b355bf77884"></span><code>MainViewModel.RefreshWorkspaceCategories()</code><br>7298–7357 | Clear @7300; Equals @7301; IsNullOrEmpty @7305; Add @7310; Localize @7313; Add @7324; RaisePropertyChanged @7356; nameof @7356 | No extracted literal effects. |
| <span id="m-6cf466b9b900"></span><code>MainViewModel.SelectWorkspaceCategory(CategoryItem?)</code><br>7359–7392 | Equals @7362; Localize @7364; RaisePropertyChanged @7376; nameof @7376; ClearSelection @7387; InvalidateSelectedBatchPreview @7388; ResetToFirstPage @7389; NotifySelectionScopeChange @7390; SetSelectionScope @7390; InventorySelectionScope @7390; LoadInventoryAsync @7391 | No extracted literal effects. |
| <span id="m-9a61cba8fc9b"></span><code>MainViewModel.GenerateXReport()</code><br>7394–7413 | CheckSessionUnlocked @7396; ToString @7400; GenerateXReportInternalAsync @7412 | No extracted literal effects. |
| <span id="m-de7f88e416d3"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>7415–7430 | ConfigureAwait @7419; LoadReportDataAsync @7419; DispatchToUi @7428; SafeError @7428 | No extracted literal effects. |
| <span id="m-357515b1c2ea"></span><code>MainViewModel.CloseShiftZReport()</code><br>7432–7435 | OpenCloseShiftModal @7434 | No extracted literal effects. |
| <span id="m-03361d6c2ced"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>7437–7446 | CheckSessionUnlocked @7444 | No extracted literal effects. |
| <span id="m-b78a29d11681"></span><code>MainViewModel.SaveSettings()</code><br>7448–7452 | CheckSessionUnlocked @7450 | No extracted literal effects. |
| <span id="m-381d19ea3530"></span><code>MainViewModel.ApplySettingsAsync()</code><br>7454–7541 | CheckSessionUnlocked @7463; NotifyTotalsChanged @7482; ExecuteAsync @7510; DispatchToUi @7534; SafePipelineError @7534; SafeError @7539 | No extracted literal effects. |
| <span id="m-900422753e06"></span><code>MainViewModel.CancelSettings()</code><br>7543–7564 | CheckSessionUnlocked @7545; NotifyTotalsChanged @7557 | No extracted literal effects. |
| <span id="m-d1e9eaa0b66d"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7567–7597 | ProbeDatabaseAsync @7580; ProbeLicense @7586; RefreshOutputStatusAsync @7589; ProbeHardwareStubs @7590; DispatchToUi @7595; SafeError @7595 | No extracted literal effects. |
| <span id="m-f5b9bf96ff2b"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7658–7696 | RaisePropertyChanged @7660; nameof @7660; FormatRealResetPreviewSummary @7695 | No extracted literal effects. |
| <span id="m-b02121990d6c"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7698–7711 | Localize @7699; ToString @7701; GetValueOrDefault @7701; ToString @7706; ToString @7707; ToString @7708 | No extracted literal effects. |
| <span id="m-0b14a2008c93"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7820–7912 | Post @7824; ConfigureAwait @7831; GetWorkspaceEnvironmentAsync @7831; Equals @7832; GetDatasetStateAsync @7834; CreateCommand @7840; CreateParameter @7847; ToString @7849; Add @7850; ExecuteScalarAsync @7851; HasPermission @7856; ToInt64 @7861; ExecuteScalarAsync @7861; ExecuteScalarAsync @7865; ExecuteScalarAsync @7872; ExecuteScalarAsync @7878; Localize @7897 | FROM items @7860; FROM sales_invoices @7864; FROM third_parties @7877; FROM users @7841; JOIN user_roles @7841 · DYNAMIC SQL: inspect manually |
| <span id="m-b145c1693ffb"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>7914–7924 | CheckSessionUnlocked @7916; HasPermission @7917 | No extracted literal effects. |
| <span id="m-9537ba530e8a"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>7926–7931 | ConfigureAwait @7930; ResetDatabaseAsync @7930 | No extracted literal effects. |
| <span id="m-95bfa5685e5b"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>7933–7934 | ConfigureAwait @7934; EnsureDefaultDemoDatasetAsync @7934 | No extracted literal effects. |
| <span id="m-3ee58e52c126"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>7936–7942 | EnsureDefaultDemoDatasetAsync @7940 | No extracted literal effects. |
| <span id="m-c7fdabd71e18"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>7944–8048 | Localize @7949; ConfigureAwait @7956; WaitAsync @7956; GetWorkspaceEnvironmentAsync @7959; Equals @7960; HasPermission @7967; Post @7981; LocalizeDemoSeedProgress @7983; EnsureInitialDatasetAsync @7989; Join @8013; Select @8013; ReloadCatalogAsync @8023; LoadInventoryAsync @8024; LoadThirdPartiesAsync @8025; LoadManufacturingDataAsync @8026; LoadSuppliersAsync @8027; UpdateDemoSeedingAvailabilityAsync @8028; ToUpperInvariant @8033; ToString @8033; NewGuid @8033; LogDiagnosticError @8034; ReportError @8039; Release @8046 | No extracted literal effects. |
| <span id="m-2bdbb338337b"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>8050–8064 | Localize @8052 | No extracted literal effects. |
| <span id="m-89bdd40c4718"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>8066–8163 | Localize @8070; ConfigureAwait @8074; WaitAsync @8074; HasPermission @8078; GetWorkspaceEnvironmentAsync @8085; Equals @8086; ResetDatabaseAsync @8094; GetStoreProfileAsync @8097; Post @8098; Clear @8101; Clear @8102; Clear @8103; NewGuid @8104; RaisePropertyChanged @8107; nameof @8107; Lock @8108; Defaults @8121; RefreshUnlockCandidates @8134; LoadCashFinancialSettingsAsync @8135; LoadOutputDevicesAsync @8136; LoadManualPaymentSettingsAsync @8137; LoadReceiptDesignAsync @8138; ReloadCatalogAsync @8139; LoadInventoryAsync @8140; LoadThirdPartiesAsync @8141; LoadManufacturingDataAsync @8142; LoadActivityInvoicesAsync @8143; UpdateDemoSeedingAvailabilityAsync @8144; ToUpperInvariant @8149; ToString @8149; LogDiagnosticError @8150; ReportError @8156; Release @8161 | No extracted literal effects. |
| <span id="m-e4f55bbd5e64"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>8165–8207 | CheckSessionUnlocked @8167; HasPermission @8169; ConfigureAwait @8177; GetWorkspaceEnvironmentAsync @8177; Equals @8178; PreviewAsync @8181; FormatRealResetPreviewSummary @8182; Post @8183; RaisePropertyChanged @8200; nameof @8200; SafeError @8205 | UnauthorizedAccessException @8179 |
| <span id="m-75cdea8025d9"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>8209–8295 | HasPermission @8212; ConfigureAwait @8230; ExecuteAsync @8230; GetStoreProfileAsync @8239; Post @8242; Clear @8246; Clear @8247; Clear @8248; Clear @8249; NewGuid @8250; Lock @8253; RaisePropertyChanged @8267; nameof @8267; LoadCashFinancialSettingsAsync @8268; LoadOutputDevicesAsync @8269; LoadManualPaymentSettingsAsync @8270; LoadReceiptDesignAsync @8271; RefreshUnlockCandidates @8279; LoadInventoryAsync @8280; LoadActivityInvoicesAsync @8281; UpdateDemoSeedingAvailabilityAsync @8282; ToUpperInvariant @8287; ToString @8287; LogDiagnosticError @8288 | No extracted literal effects. |
| <span id="m-38d009ad5885"></span><code>MainViewModel.CancelRealShopReset()</code><br>8297–8304 | RaisePropertyChanged @8303; nameof @8303 | No extracted literal effects. |
| <span id="m-720b89e6c360"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>8308–8325 | ConfigureAwait @8310; ExportDocumentAsync @8310; Post @8314; GetFileName @8318 | No extracted literal effects. |
| <span id="m-4767c3ca0952"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>8327–8349 | Exists @8332; CreateDirectory @8334; Start @8336; ToUpperInvariant @8345; ToString @8345; NewGuid @8345; LogDiagnosticError @8346 | No extracted literal effects. |
| <span id="m-f14ff03b684a"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>8351–8361 | CheckSessionUnlocked @8353; RaisePropertyChanged @8355; nameof @8355; Localize @8357; ToString @8358 | No extracted literal effects. |
| <span id="m-e51bedb591da"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>8368–8384 | CheckSessionUnlocked @8370; HasPermission @8371; RaisePropertyChanged @8377; nameof @8377; Localize @8380; ToString @8381 | No extracted literal effects. |
| <span id="m-4f49324b8d0f"></span><code>MainViewModel.CommitNumpad()</code><br>8386–8463 | CheckSessionUnlocked @8388; ResetCashReview @8389; TryParse @8395; IsNullOrWhiteSpace @8397; Trim @8403; NotifyTotalsChanged @8413; SaveDurableCartAsync @8414; Min @8420; ToMinorUnits @8422; Round @8423; TryParse @8438; UpdateCartKitBreakdownAsync @8446; Remove @8452; RaisePropertyChanged @8461; nameof @8461 | No extracted literal effects. |
| <span id="m-3cda17b92be7"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>8469–8487 | CheckSessionUnlocked @8477 | No extracted literal effects. |
| <span id="m-c6e3168308c0"></span><code>MainViewModel.StageBusinessProfile()</code><br>8494–8524 | CheckSessionUnlocked @8496; HasPermission @8500 | No extracted literal effects. |
| <span id="m-9ddf8e462dc7"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8526–8535 | — | No extracted literal effects. |
| <span id="m-6f369e53fbea"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8537–8560 | RecalculateCart @8539; RaisePropertyChanged @8541; nameof @8541 | No extracted literal effects. |
| <span id="m-b2dc4b2cabf8"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8562–8649 | IsNullOrWhiteSpace @8565; Trim @8565; All @8575; Trim @8592; Trim @8593; NewGuid @8597; ToString @8602; ConfigureAwait @8606; BeginTransactionAsync @8606; HandleAsync @8607; AppendAsync @8612; ToString @8613; Serialize @8618; CommitAsync @8621; Initialize @8627; Unlock @8628; RaisePropertyChanged @8633; nameof @8633; LoadTeamsStaffAsync @8636; StartAutomaticDemoDatasetLoadAsync @8637; RollbackAsync @8641; DispatchToUi @8642; SafePipelineError @8642; SafeError @8647 | No extracted literal effects. |
| <span id="m-f061901b97e7"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8651–8658 | IsNullOrWhiteSpace @8653; ConfigureAwait @8657; SaveTeamMemberAsync @8657 | No extracted literal effects. |
| <span id="m-e5ee052967fd"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8660–8678 | CheckSessionUnlocked @8663; HasPermission @8665 | No extracted literal effects. |
| <span id="m-47343a40ba49"></span><code>MainViewModel.CancelChangePin()</code><br>8680–8687 | — | No extracted literal effects. |
| <span id="m-e23227f426d4"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8689–8765 | Trim @8697; IsNullOrWhiteSpace @8700; All @8706; Equals @8719; Equals @8720; SetQuickPin @8732; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8745; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8745; ConfigureAwait @8753; LoadTeamsStaffAsync @8753; DispatchToUi @8758; SafePipelineError @8758; SafeError @8763 | No extracted literal effects. |
| <span id="m-621581d8c65f"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8767–8841 | HasPermission @8773; ConfigureAwait @8782; ResolveEffectivePermissionsAsync @8782; Contains @8815; Contains @8816; Add @8818; Contains @8824; DispatchToUi @8830; Clear @8832; Add @8833; SafeError @8839 | No extracted literal effects. |
| <span id="m-eab24956a6dd"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8843–8885 | OnTeamMemberFieldChanged @8849; ConfigureAwait @8866; ExecuteAsync @8866; DispatchToUi @8870; SafePipelineError @8878; SafeError @8883 | No extracted literal effects. |
| <span id="m-623075bd8735"></span><code>MainViewModel.ClosePermissionEditor()</code><br>8887–8892 | — | No extracted literal effects. |
| <span id="m-a8a345fe5aee"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>8894–8909 | ClearImportResults @8896 | No extracted literal effects. |
| <span id="m-ede90159bfcf"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>8913–8913 | — | No extracted literal effects. |
| <span id="m-070bc12f5de5"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>8914–8914 | — | No extracted literal effects. |
| <span id="m-65ca87fbd57d"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>8915–8915 | FromResult @8915 | No extracted literal effects. |
| <span id="m-7fe46d9ba055"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>8918–9003 | HasPermission @8927; FromDecimal @8942; ConfigureAwait(OpenShiftCommand, Shift) @8946; ExecuteAsync(OpenShiftCommand, Shift) @8946; SetActiveCashier @8961; RefreshUnlockCandidates @8962; ToUpperInvariant @8979; ToString @8979; ToString @8981; ConfigureAwait @8991; LoadTeamsStaffAsync @8991; LoadTrackOrdersAsync @8992; DispatchToUi @8996; SafePipelineError @8996; SafeError @9001 | No extracted literal effects. |
| <span id="m-9e56f086b841"></span><code>MainViewModel.LoadInventoryAsync()</code><br>9005–9164 | ApplyPagedResult @9009; ToList @9010; Where @9010; Equals @9010; Count @9011; ApplyInventoryFilter @9014; Clear @9023; Empty(InventoryItem) @9025; ConfigureAwait @9030; GetPagedInventoryItemsAsync @9030; ToPageRequest @9035; CreateCommand @9050; ExecuteReaderAsync @9052; ReadAsync @9053; Add @9055; Parse @9055; GetString @9055; ExecuteReaderAsync @9065; ReadAsync @9066; TryParse @9068; GetString @9068; IsDBNull @9068; Add @9079; TryGetValue @9082; Contains @9090; ToDecimal @9093; Localize @9101; ToLocalTime @9107; BuildCostSourcesTooltip @9109; DispatchToUi @9136; Add @9140; SafeError @9162 | FROM item_kits @9051; FROM item_pricing @9064 |
| <span id="m-4249b0755bbd"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>9166–9222 | CheckSessionUnlocked @9168; FirstOrDefault @9169; Clear @9180; Add @9182; CreateCommand @9187; CreateParameter @9198; Add @9201; ExecuteReader @9202; Read @9203; GetString @9205; Contains @9206; FirstOrDefault @9218; ResetReceiveLines @9219; UpdateReceiveKitBreakdownAsync @9220 | FROM uoms @9188; JOIN uoms @9188 |
| <span id="m-65d1d6f8fea3"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>9224–9325 | IsNullOrWhiteSpace @9237; Localize @9254; HasPermission @9258; BuildReceiptLines @9264; Sum @9281; Trim @9291; ToMinorUnits @9296; ConfigureAwait(ReceiveStockCommand, StockMovement) @9301; ExecuteAsync(ReceiveStockCommand, StockMovement) @9301; Clear @9311; ConfigureAwait @9313; LoadInventoryAsync @9313; LoadItemHistoryAsync @9314; DispatchToUi @9318; SafePipelineError @9318; SafeError @9323 | No extracted literal effects. |
| <span id="m-da01e6fae498"></span><code>MainViewModel.ResetReceiveLines()</code><br>9331–9348 | Clear @9333; Add @9337; RaisePropertyChanged @9343; nameof @9343; Invoke @9346 | No extracted literal effects. |
| <span id="m-0e6bfe397077"></span><code>MainViewModel.AddReceiveLine()</code><br>9351–9374 | IsNullOrWhiteSpace @9358; Add @9364; RaisePropertyChanged @9369; nameof @9369; Invoke @9372 | No extracted literal effects. |
| <span id="m-afe17ac7fd63"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>9377–9394 | Remove @9384; Add @9387; RaisePropertyChanged @9393; nameof @9393 | No extracted literal effects. |
| <span id="m-5772f22065ee"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>9400–9421 | IsNullOrWhiteSpace @9402; LastOrDefault @9407; Add @9411; Trim @9414; ReferenceEquals @9415; RaisePropertyChanged @9419; nameof @9419; Invoke @9420 | No extracted literal effects. |
| <span id="m-572124905ac0"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>9424–9501 | Add @9436; IsNullOrWhiteSpace @9444; Trim @9448; FirstOrDefault @9457; GroupBy @9457; Count @9459; Trim @9486 | No extracted literal effects. |
| <span id="m-d9e0ca026546"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>9503–9539 | CreateCommand @9508; ConfigureAwait @9515; ExecuteReaderAsync @9515; Clear @9516; ReadAsync @9517; Add @9519; ParseGuidSafe @9520; GetString @9520; IsDBNull @9524; GetInt32 @9528; Parse @9530; DispatchToUi @9537; SafeError @9537 | FROM third_parties @9509 |
| <span id="m-2aa54cf1fca0"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9541–9559 | CheckSessionUnlocked @9543; FirstOrDefault @9549 | No extracted literal effects. |
| <span id="m-d4801a5a89a5"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9561–9652 | IsNullOrWhiteSpace @9584; HasPermission @9595; Trim @9613; Trim @9615; ConfigureAwait(AdjustStockCommand, StockMovement) @9619; ExecuteAsync(AdjustStockCommand, StockMovement) @9619; ConfigureAwait @9635; LoadInventoryAsync @9635; LoadItemHistoryAsync @9636; OpenWasteExpenseConfirmation @9640; DispatchToUi @9645; SafePipelineError @9645; SafeError @9650 | No extracted literal effects. |
| <span id="m-8338f60542b4"></span><code>MainViewModel.OpenAddService()</code><br>9654–9716 | ResetProductStockDraft @9656; CheckSessionUnlocked @9657; HasPermission @9658; RaisePropertyChanged @9667; nameof @9667; ClearItemHistory @9676; LoadCatalogRegistryAsync @9683; InitializeProductPricingDraft @9686; Clear @9701; Clear @9702; Clear @9711; CaptureProductModalBaselineAsync @9715 | No extracted literal effects. |
| <span id="m-dcf664358a31"></span><code>MainViewModel.OpenAddProduct()</code><br>9718–9794 | ResetProductStockDraft @9720; CheckSessionUnlocked @9721; RaisePropertyChanged @9723; nameof @9723; HasPermission @9730; ClearItemHistory @9740; LoadCatalogRegistryAsync @9747; InitializeProductPricingDraft @9750; Clear @9765; Clear @9766; Where @9767; Add @9769; FirstOrDefault @9771; Clear @9782; CaptureProductModalBaselineAsync @9793 | No extracted literal effects. |
| <span id="m-721c0f48da2a"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9796–9796 | OpenEditProduct @9796 | No extracted literal effects. |
| <span id="m-f99fa28f8ce8"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9798–9887 | ResetProductStockDraft @9800; CheckSessionUnlocked @9802; RaisePropertyChanged @9805; nameof @9805; HasPermission @9812; ClearItemHistory @9822; LoadCatalogRegistryAsync @9830; InitializeProductPricingDraft @9836; ToMinorUnits @9837; LoadExactProductCostSnapshotsAsync @9843; ToDecimal @9847; Clear @9854; Clear @9855; Where @9856; Add @9858; FirstOrDefault @9860; LoadItemLocationEligibilitiesAsync @9879; LoadProductKitAsync @9880; LoadPrimaryBarcodeAsync @9881; LoadProductPricingDraftAsync @9882; LoadItemHistoryAsync @9883; LoadItemPriceHistoryAsync @9884; CaptureProductModalBaselineAsync @9886 | No extracted literal effects. |
| <span id="m-7dd22a8cba5b"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>9889–9902 | OrderBy @9892; Where @9892; Add @9894 | No extracted literal effects. |
| <span id="m-3a63c3232fa5"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>9904–9977 | CreateCommand @9911; CreateParameter @9918; ToString @9920; Add @9921; ConfigureAwait @9922; ExecuteReaderAsync @9922; ReadAsync @9923; GetInt32 @9925; IsDBNull @9926; GetString @9926; ParseStoredPricingPercentForDisplay @9927; ToDisplayAmount @9931; GetInt64 @9931; OrderBy @9951; Where @9951; TryGetValue @9954; Add @9960; InvokeAsync @9962; RaisePropertyChanged @9967; nameof @9967; CaptureProductPricingSnapshot @9970; DispatchToUi @9975; SafeError @9975 | FROM item_price_levels @9942; FROM item_pricing @9913 |
| <span id="m-397f2b412fdb"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>9979–10014 | CreateCommand @9986; CreateParameter @9992; ToString @9994; Add @9995; ConfigureAwait @9996; ExecuteReaderAsync @9996; ReadAsync @9997; Parse @10000; GetString @10000; GetInt32 @10000; GetInt64 @10001; IsDBNull @10001; Parse @10002; InvokeAsync @10004; DispatchToUi @10012; SafeError @10012 | FROM product_category_pricing_rules @9987 |
| <span id="m-0058a9eb061e"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>10016–10045 | ConfigureAwait @10020; WhenAll @10020; InvokeAsync @10021; CaptureProductModalSnapshot @10025; CaptureProductPricingSnapshot @10026; RaisePropertyChanged @10027; nameof @10027 | No extracted literal effects. |
| <span id="m-b8b002897901"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>10047–10095 | Serialize @10047; ToArray @10070; Select @10070; Select @10087; OrderBy @10087; OrderBy @10091 | No extracted literal effects. |
| <span id="m-8c345bf17f75"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>10097–10109 | Serialize @10097; ToArray @10108; Select @10108 | No extracted literal effects. |
| <span id="m-c0caf42f1fcc"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>10111–10143 | nameof @10113; RaisePropertyChanged @10114; RaiseTraceabilityState @10119; StartsWith @10123; RecomputeProductPricingPreview @10134; RefreshVirtualKitAvailability @10136 | No extracted literal effects. |
| <span id="m-ccc5972fa4ee"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>10145–10159 | RaisePropertyChanged @10153; nameof @10153; RecomputeProductPricingPreview @10156; RefreshVirtualKitAvailability @10157 | No extracted literal effects. |
| <span id="m-c7f26835e412"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>10161–10169 | RaisePropertyChanged @10163; nameof @10163; RecomputeProductPricingPreview @10166; RefreshVirtualKitAvailability @10167 | No extracted literal effects. |
| <span id="m-2aa4fd8083da"></span><code>MainViewModel.RequestCloseProductModal()</code><br>10171–10184 | DiscardProductModal @10183 | No extracted literal effects. |
| <span id="m-4652dc4e482d"></span><code>MainViewModel.DiscardProductModal()</code><br>10186–10195 | RaisePropertyChanged @10191; nameof @10191; ClearItemHistory @10193 | No extracted literal effects. |
| <span id="m-8e2d57470ebf"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>10197–10215 | CreateCommand @10202; CreateParameter @10204; ToString @10206; Add @10207; ConfigureAwait @10208; ExecuteScalarAsync @10208; DispatchToUi @10211; ToString @10211 | FROM barcodes @10203 |
| <span id="m-fde1a5f252e1"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>10217–10268 | CreateCommand @10222; CreateParameter @10229; ToString @10231; Add @10232; ConfigureAwait @10236; ExecuteReaderAsync @10236; ReadAsync @10237; IsDBNull @10240; GetString @10240; GetDouble @10241; ResolveQuantity @10242; Add @10243; Parse @10245; DispatchToUi @10253; Clear @10256; Add @10257; RaisePropertyChanged @10260; nameof @10260; RecomputeProductPricingPreview @10263; RefreshVirtualKitAvailability @10264 | FROM item_kits @10223; JOIN item_kit_components @10223; JOIN items @10223 |
| <span id="m-2c7c3486cc58"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>10270–10270 | SaveProductConfigurationAsync @10270 | No extracted literal effects. |
| <span id="m-e11302282f19"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>10272–10621 | ConfigureAwait @10277; LoadCatalogRegistryAsync @10277; HasPermission @10279; IsNullOrWhiteSpace @10284; Equals @10309; ValidateUnitEligibility @10322; ToMinorUnits @10342; GetValueOrDefault @10349; Trim @10350; Trim @10351; Trim @10353; Empty(KitComponentInput) @10386; CaptureProductPricingSnapshot @10389; ToCommand @10391; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @10402; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @10402; DispatchToUi @10405; RaiseTraceabilityState @10412; CaptureProductModalSnapshot @10415; RaisePropertyChanged @10417; nameof @10417; SelectInventoryKind @10423; ReloadCatalogAsync @10425; LoadInventoryAsync @10426; LoadItemHistoryAsync @10427; SafePipelineError @10431; SafeError @10437; Localize @10449; GetValueOrDefault @10516; Trim @10519; Trim @10526; ToList @10573; Select @10573 | No extracted literal effects. |
| <span id="m-53ad41ed3f77"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>10623–10659 | CheckSessionUnlocked @10625; HasPermission @10626; ConfigureAwait(DeactivateProductCommand, bool) @10642; ExecuteAsync(DeactivateProductCommand, bool) @10642; ConfigureAwait @10647; ReloadCatalogAsync @10647; LoadInventoryAsync @10648; DispatchToUi @10652; SafePipelineError @10652; SafeError @10657 | No extracted literal effects. |
| <span id="m-491e644e2b38"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>10661–10736 | ConfigureAwait @10667; GetActiveItemsAsync @10667; Clear @10669; Clear @10670; Clear @10671; CreateCommand @10676; ExecuteReaderAsync @10678; ReadAsync @10679; TryParse @10681; GetString @10681; Add @10682; Add @10689; GroupBy @10690; Count @10692; Contains @10697; Add @10721; All @10724; SafeError @10727; ApplyFilter @10730 | FROM item_kits @10677 |
| <span id="m-864dde572c38"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>10738–10744 | IsNullOrWhiteSpace @10740; TryParse @10741; HashData @10742; GetBytes @10742; AsSpan @10743 | No extracted literal effects. |
| <span id="m-5e8a1d4bcda1"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>10746–10812 | CreateCommand @10752; ConfigureAwait @10755; ExecuteReaderAsync @10755; ReadAsync @10757; Add @10759; GetString @10761; GetInt32 @10765; Clear @10771; Add @10772; ExecuteReaderAsync @10784; ReadAsync @10786; Add @10788; GetString @10790; IsDBNull @10794; GetInt32 @10798; Clear @10804; Add @10805; DispatchToUi @10810; SafeError @10810 | FROM bins @10777; FROM facilities @10754; JOIN facilities @10777 |
| <span id="m-2edfc6a3b08e"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>11038–11160 | CreateCommand @11048; ConfigureAwait @11055; ExecuteReaderAsync @11055; ReadAsync @11056; Add @11058; ParseGuidSafe @11060; GetString @11060; IsDBNull @11063; GetInt32 @11064; Add @11084; DispatchToUi @11099; Clear @11101; Clear @11102; Clear @11103; Clear @11104; Equals @11108; Add @11109; Add @11111; Add @11113; Add @11115; Clear @11117; Add @11118; FirstOrDefault @11123; Equals @11123; FirstOrDefault @11129; ToList @11135; FirstOrDefault @11136; FirstOrDefault @11140; FirstOrDefault @11145; ApplySaleUnitDefaultsToCatalog @11150; RaisePropertyChanged @11151; nameof @11151; RefreshWorkspaceCategories @11153; SafeError @11158 | FROM product_categories @11050; FROM uoms @11076 |
| <span id="m-54a71686e01b"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>11162–11176 | ResolveProductSaleUnitFactor @11166; Round @11172; ApplyFilter @11175 | No extracted literal effects. |
| <span id="m-322148e759af"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>11178–11196 | FirstOrDefault @11180; Equals @11181; TryParse @11188 | No extracted literal effects. |
| <span id="m-a195cf63686c"></span><code>MainViewModel.OpenAddCategoryForCurrentKindAsync()</code><br>11198–11213 | CheckSessionUnlocked @11200; HasPermission @11201; OpenCategoryManagerAsync @11207; CaptureCategoryFormSnapshot @11210; RaisePropertyChanged @11211; nameof @11211 | No extracted literal effects. |
| <span id="m-2e632838a81f"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>11215–11237 | CheckSessionUnlocked @11217; HasPermission @11218; ConfigureAwait @11233; LoadManagedCategoriesAsync @11233; CaptureCategoryFormSnapshot @11235; RaisePropertyChanged @11236; nameof @11236 | No extracted literal effects. |
| <span id="m-df9cdc1ef401"></span><code>MainViewModel.CloseCategoryManager()</code><br>11239–11248 | — | No extracted literal effects. |
| <span id="m-0c570f74777c"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>11250–11272 | CheckSessionUnlocked @11252; HasPermission @11253; ConfigureAwait @11268; LoadManagedUnitsAsync @11268; CaptureUnitFormSnapshot @11270; RaisePropertyChanged @11271; nameof @11271 | No extracted literal effects. |
| <span id="m-59cd8e68cca3"></span><code>MainViewModel.CloseUnitManager()</code><br>11274–11283 | — | No extracted literal effects. |
| <span id="m-5423c3d040d6"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>11285–11348 | Clear @11288; Clear @11289; Clear @11290; CreateCommand @11291; ConfigureAwait @11297; ExecuteReaderAsync @11297; ReadAsync @11298; Add @11300; ParseGuidSafe @11302; GetString @11302; IsDBNull @11305; GetInt32 @11306; Where @11314; Equals @11314; Add @11315; TryParse @11328; Add @11329; RefreshTargetedCategoryCollections @11342; DispatchToUi @11343; RefreshManagedCategoriesTable @11345; RefreshManagedExpenseCategoriesTable @11346 | FROM expense_categories @11319; FROM product_categories @11293; JOIN expense_records @11319 |
| <span id="m-52bbf20a144d"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>11350–11357 | OpenCategoryManagerAsync @11352; FirstOrDefault @11353; EditManagedCategory @11356 | No extracted literal effects. |
| <span id="m-749c215f2c8b"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>11359–11367 | OpenCategoryManagerAsync @11362; FirstOrDefault @11363; EditManagedExpenseCategory @11366 | No extracted literal effects. |
| <span id="m-9336a42ffeca"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>11369–11391 | DispatchToUi @11371; Clear @11373; Clear @11374; Clear @11375; Clear @11376; Where @11378; Equals @11381; Add @11382; Add @11384; Add @11386; Add @11388 | No extracted literal effects. |
| <span id="m-afc69642387b"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>11393–11405 | CaptureCategoryFormSnapshot @11403; RaisePropertyChanged @11404; nameof @11404 | No extracted literal effects. |
| <span id="m-25b5e1164601"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>11407–11420 | CaptureCategoryFormSnapshot @11418; RaisePropertyChanged @11419; nameof @11419 | No extracted literal effects. |
| <span id="m-40b03bd087de"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>11422–11432 | Serialize @11422 | No extracted literal effects. |
| <span id="m-1b422e7fabc0"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>11434–11444 | Serialize @11434 | No extracted literal effects. |
| <span id="m-e83171faa2ae"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>11446–11446 | — | No extracted literal effects. |
| <span id="m-18b20d261030"></span><code>MainViewModel.DiscardRegistryForm()</code><br>11448–11464 | Equals @11451; RaisePropertyChanged @11455; nameof @11455 | No extracted literal effects. |
| <span id="m-b81555105792"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>11466–11593 | Equals @11477; HasPermission @11479; FirstOrDefault @11488; Trim @11493; Trim @11494; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11496; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11496; DispatchToUi @11499; SafePipelineError @11499; IsNullOrWhiteSpace @11507; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @11509; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @11509; ConfigureAwait @11518; LoadManagedCategoriesAsync @11518; LoadExpenseCategoriesAsync @11519; CaptureCategoryFormSnapshot @11529; RaisePropertyChanged @11530; nameof @11530; Trim @11548; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @11550; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @11550; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @11566; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @11566; LoadCatalogRegistryAsync @11575; ReloadCatalogAsync @11576; SafeError @11591 | No extracted literal effects. |
| <span id="m-3483847dd9b2"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>11595–11640 | HasPermission @11605; ConfigureAwait(DeactivateCategoryCommand, bool) @11618; ExecuteAsync(DeactivateCategoryCommand, bool) @11618; ConfigureAwait(ReactivateCategoryCommand, bool) @11623; ExecuteAsync(ReactivateCategoryCommand, bool) @11623; DispatchToUi @11628; SafePipelineError @11628; ConfigureAwait @11632; LoadManagedCategoriesAsync @11632; LoadCatalogRegistryAsync @11633; ReloadCatalogAsync @11634; SafeError @11638 | No extracted literal effects. |
| <span id="m-0f57cefc7662"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>11642–11682 | HasPermission @11652; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11668; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11668; DispatchToUi @11671; SafePipelineError @11671; ConfigureAwait @11675; LoadManagedCategoriesAsync @11675; LoadExpenseCategoriesAsync @11676; SafeError @11680 | No extracted literal effects. |
| <span id="m-6c2435280143"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>11684–11784 | Clear @11687; CreateCommand @11690; ConfigureAwait @11696; ExecuteReaderAsync @11696; ReadAsync @11697; Add @11699; GetString @11701; IsDBNull @11703; GetInt32 @11707; IsNullOrWhiteSpace @11718; Equals @11722; Add @11729; Clear @11733; ExecuteReaderAsync @11738; ReadAsync @11739; GetString @11741; Where @11763; Add @11765; TryGetValue @11768; FirstOrDefault @11775; Add @11779; DispatchToUi @11782; UpdateConversionPreview @11783 | FROM store_uom_preferences @11737; FROM uoms @11692 |
| <span id="m-50c5ca2db640"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>11786–11793 | OpenUnitManagerAsync @11788; FirstOrDefault @11789; Equals @11789; EditManagedUnit @11792 | No extracted literal effects. |
| <span id="m-1a494b859661"></span><code>MainViewModel.UpdateConversionPreview()</code><br>11795–11831 | IsNullOrWhiteSpace @11797; FirstOrDefault @11803; Equals @11803; TryParse @11818 | No extracted literal effects. |
| <span id="m-542b5330dec8"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11833–11854 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11840; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11840; DispatchToUi @11843; SafePipelineError @11847; SafeError @11852 | No extracted literal effects. |
| <span id="m-a62e18ef2450"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11856–11869 | IsNullOrWhiteSpace @11862; TryParse @11865; CaptureUnitFormSnapshot @11867; RaisePropertyChanged @11868; nameof @11868 | No extracted literal effects. |
| <span id="m-52be5360693f"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>11871–11933 | IsNullOrWhiteSpace @11883; Trim @11887; Trim @11888; Trim @11891; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @11892; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @11892; DispatchToUi @11895; SafePipelineError @11895; Trim @11902; Equals @11905; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @11910; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @11910; ConfigureAwait @11918; LoadManagedUnitsAsync @11918; LoadCatalogRegistryAsync @11919; CaptureUnitFormSnapshot @11926; RaisePropertyChanged @11927; nameof @11927; SafeError @11931 | No extracted literal effects. |
| <span id="m-abcbbc06b0e2"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>11935–11973 | ConfigureAwait(DeactivateUomCommand, bool) @11952; ExecuteAsync(DeactivateUomCommand, bool) @11952; ConfigureAwait(ReactivateUomCommand, bool) @11957; ExecuteAsync(ReactivateUomCommand, bool) @11957; DispatchToUi @11962; SafePipelineError @11962; ConfigureAwait @11966; LoadManagedUnitsAsync @11966; LoadCatalogRegistryAsync @11967; SafeError @11971 | No extracted literal effects. |
| <span id="m-e0f613e07fbb"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>11975–12013 | CreateCommand @11980; CreateParameter @11987; ToString @11989; Add @11990; ConfigureAwait @11992; ExecuteReaderAsync @11992; Clear @11993; ReadAsync @11994; Add @11996; ParseGuidSafe @11998; GetString @11998; GetInt32 @12001; IsDBNull @12003; ToDecimal @12003; GetDouble @12003; DispatchToUi @12011; SafeError @12011 | FROM item_locations @11981 |
| <span id="m-9cdc753d73f3"></span><code>MainViewModel.OpenLocationsModal()</code><br>12016–12042 | CheckSessionUnlocked @12018; HasPermission @12019; LoadFacilitiesAndBinsAsync @12040 | No extracted literal effects. |
| <span id="m-fb257d07537d"></span><code>MainViewModel.OpenAddFacility()</code><br>12044–12052 | — | No extracted literal effects. |
| <span id="m-64bf8709a8ba"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>12054–12063 | — | No extracted literal effects. |
| <span id="m-e98dd5e63ded"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>12065–12124 | HasPermission @12068; IsNullOrWhiteSpace @12073; IsNullOrEmpty @12089; Trim @12091; Trim @12091; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @12092; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @12092; OpenAddFacility @12096; ConfigureAwait @12097; LoadFacilitiesAndBinsAsync @12097; DispatchToUi @12101; SafePipelineError @12101; ConfigureAwait(CreateFacilityCommand, FacilityDto) @12107; ExecuteAsync(CreateFacilityCommand, FacilityDto) @12107; SafeError @12122 | No extracted literal effects. |
| <span id="m-b3182e47dd50"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>12126–12157 | HasPermission @12129; ConfigureAwait(DeactivateFacilityCommand, bool) @12141; ExecuteAsync(DeactivateFacilityCommand, bool) @12141; OpenAddFacility @12145; ConfigureAwait @12146; LoadFacilitiesAndBinsAsync @12146; DispatchToUi @12150; SafePipelineError @12150; SafeError @12155 | No extracted literal effects. |
| <span id="m-5a9904bfe37b"></span><code>MainViewModel.OpenAddBin()</code><br>12159–12170 | FirstOrDefault @12169 | No extracted literal effects. |
| <span id="m-ace64ef33198"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>12172–12184 | FirstOrDefault @12182 | No extracted literal effects. |
| <span id="m-0ff75261b012"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>12186–12261 | HasPermission @12189; IsNullOrWhiteSpace @12199; IsNullOrEmpty @12210; Trim @12215; Trim @12216; Trim @12217; Trim @12218; Trim @12219; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @12222; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @12222; OpenAddBin @12226; ConfigureAwait @12227; LoadFacilitiesAndBinsAsync @12227; DispatchToUi @12231; SafePipelineError @12231; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @12244; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @12244; SafeError @12259 | No extracted literal effects. |
| <span id="m-6633397f97a8"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>12263–12294 | HasPermission @12266; ConfigureAwait(DeactivateLocationBinCommand, bool) @12278; ExecuteAsync(DeactivateLocationBinCommand, bool) @12278; OpenAddBin @12282; ConfigureAwait @12283; LoadFacilitiesAndBinsAsync @12283; DispatchToUi @12287; SafePipelineError @12287; SafeError @12292 | No extracted literal effects. |
| <span id="m-c0acbc8644aa"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>12296–12349 | HasPermission @12304; IsNullOrWhiteSpace @12309; Trim @12321; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @12329; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @12329; ConfigureAwait @12337; LoadItemLocationEligibilitiesAsync @12337; DispatchToUi @12342; SafePipelineError @12342; SafeError @12347 | No extracted literal effects. |
| <span id="m-f24ad7accc3e"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>12351–12381 | HasPermission @12354; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @12366; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @12366; ConfigureAwait @12369; LoadItemLocationEligibilitiesAsync @12369; DispatchToUi @12374; SafePipelineError @12374; SafeError @12379 | No extracted literal effects. |
| <span id="m-259cc8ce396f"></span><code>MainViewModel.LoadCustomersAsync()</code><br>12384–12417 | NewGuid @12392; Clear @12398; Add @12399; FilterCustomers @12401; ConfigureAwait @12408; GetCustomersAsync @12408; DispatchToUi @12415; SafeError @12415 | No extracted literal effects. |
| <span id="m-9910b9fd9a76"></span><code>MainViewModel.FilterCustomers()</code><br>12419–12432 | Clear @12421; Trim @12422; IsNullOrWhiteSpace @12423; Where @12425; Contains @12425; Contains @12426; Contains @12427; Add @12430 | No extracted literal effects. |
| <span id="m-d27752202bd2"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>12434–12470 | CheckSessionUnlocked @12436; CreateCommand @12445; CreateParameter @12448; ToString @12450; Add @12451; ConfigureAwait @12452; ExecuteScalarAsync @12452; ToString @12453; Equals @12456; LoadPickerCandidatesAsync @12468; DispatchToUi @12469 | FROM items @12447 |
| <span id="m-72965eab1e5d"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>12472–12533 | ConfigureAwait @12479; GetLotCandidatesAsync @12479; DispatchToUi @12482; Clear @12484; Add @12487; ToString @12496; GetSerialCandidatesAsync @12504; Clear @12509; Add @12512; ToString @12521 | No extracted literal effects. |
| <span id="m-b09749e7674d"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>12535–12541 | Clear @12538; Clear @12539 | No extracted literal effects. |
| <span id="m-8f9f320488ef"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>12543–12602 | FirstOrDefault @12556; ConfigureAwait(SelectLotForCartLineCommand, bool) @12564; ExecuteAsync(SelectLotForCartLineCommand, bool) @12564; DispatchToUi @12567; SafePipelineError @12567; ToList @12573; Where @12573; ConfigureAwait(SelectSerialForCartLineCommand, bool) @12583; ExecuteAsync(SelectSerialForCartLineCommand, bool) @12583; SafeError @12600 | No extracted literal effects. |
| <span id="m-dd41f0b2b3fb"></span><code>MainViewModel.OpenCustomerChooser()</code><br>12604–12612 | CheckSessionUnlocked @12606; Clear @12609; LoadCustomersAsync @12610 | No extracted literal effects. |
| <span id="m-b2104001217b"></span><code>MainViewModel.CloseCustomerChooser()</code><br>12614–12617 | — | No extracted literal effects. |
| <span id="m-d9bd936b438e"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>12619–12636 | SaveDurableCartAsync @12629; IsNullOrWhiteSpace @12633; ToString @12633; NewGuid @12633; RecordSuccessfulSearchUseAsync @12634; FromGuid @12634 | No extracted literal effects. |
| <span id="m-fcfdb332c731"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>12638–12647 | SaveDurableCartAsync @12646 | No extracted literal effects. |
| <span id="m-bb22bd989a18"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>12649–12694 | CheckSessionUnlocked @12651; IndexOf @12655; SelectWalkInCustomer @12661; FilterCustomers @12663; ConfigureAwait(DeactivateCustomerCommand, bool) @12675; ExecuteAsync(DeactivateCustomerCommand, bool) @12675; ConfigureAwait @12682; LoadCustomersAsync @12682; DispatchToUi @12687; SafePipelineError @12687; SafeError @12692 | No extracted literal effects. |
| <span id="m-7b14777006a9"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>12823–12862 | Add @12829; NewGuid @12830; RefreshManufacturingTablesAsync @12844; ConfigureAwait @12852; GetKitsAsync @12852; Clear @12853; Add @12854; DispatchToUi @12860; SafeError @12860 | No extracted literal effects. |
| <span id="m-f8891de1fb75"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12866–12882 | CheckSessionUnlocked @12868; SetProductionActionMode @12870; FirstOrDefault @12875; LoadProductionIngredientLotsAsync @12880; TakeProductionSnapshot @12881 | No extracted literal effects. |
| <span id="m-36b8a79fb355"></span><code>MainViewModel.CloseProductionModal()</code><br>12884–12898 | — | No extracted literal effects. |
| <span id="m-c89319f62304"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>12900–12999 | ExecuteExistingProductionAsync @12903; Resolve @12925; NewGuid @12928; ToUpperInvariant @12930; ToString @12930; Insert @12948; IsNullOrWhiteSpace @12970; Trim @12970; ToDictionary @12972; Where @12972; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @12976; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @12976; DispatchToUi @12979; SafePipelineError @12979; RecordSuccessfulSearchUseAsync @12986; FromGuid @12986; ConfigureAwait @12989; LoadManufacturingDataAsync @12989; LoadInventoryAsync @12990; SafeError @12996 | No extracted literal effects. |
| <span id="m-f11db94c16d5"></span><code>MainViewModel.CloseXReportModal()</code><br>13098–13101 | — | No extracted literal effects. |
| <span id="m-42f81119c5ff"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>13103–13133 | CheckSessionUnlocked @13105; Clear @13123; Where @13124; GetUnlockCandidates @13124; Equals @13125; Add @13129 | No extracted literal effects. |
| <span id="m-3b2ba26ebe34"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>13135–13139 | — | No extracted literal effects. |
| <span id="m-63ac9046793b"></span><code>MainViewModel.CloseZReportModal()</code><br>13141–13144 | — | No extracted literal effects. |
| <span id="m-67f6ae964e74"></span><code>MainViewModel.LoadReportDataAsync()</code><br>13146–13263 | ToString @13166; DispatchToUi @13182; ConfigureAwait @13210; ExecuteAsync @13210; Join @13212; Select(string, Money) @13212; InvoiceMoney @13212; ToDecimal @13215; ToDecimal @13216; ToDecimal @13217; ToDecimal @13218; ToDecimal @13220; ToDecimal @13222; ToDecimal @13223; ToDecimal @13224; ToDecimal @13225; ToDecimal @13226; ToUpperInvariant @13228; ToString @13228; ToString @13230; ToString @13231; Sum @13237; ToDecimal @13237; ToDecimal @13240; Add @13242; Format @13247; SafeError @13255 | No extracted literal effects. |
| <span id="m-4efbe39bbda5"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>13265–13354 | CheckSessionUnlocked @13268; IsNullOrWhiteSpace @13285; AuthenticateSelectedUser @13293; Trim @13295; Round @13304; Trim @13308; ConfigureAwait(CloseShiftCommand, Shift) @13312; ExecuteAsync(CloseShiftCommand, Shift) @13312; DispatchToUi @13330; SafePipelineError @13330; ConfigureAwait @13337; ExecuteAsync @13337; SetActiveCashier @13341; RefreshUnlockCandidates @13342; RaisePropertyChanged @13343; nameof @13343; LoadReportDataAsync @13347; LoadTeamsStaffAsync @13348; SafeError @13352 | No extracted literal effects. |
| <span id="m-109716fbaa97"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>13356–13432 | FirstOrDefault @13358; CreateCommand @13365; CreateParameter @13380; ToString @13382; Add @13383; ExecuteReader @13385; Read @13386; Parse @13388; GetString @13388; GetInt64 @13391; Pow @13393; IsDBNull @13395; TryParse @13401; GetInt32 @13402; Add @13425 | FROM barcodes @13366; FROM items @13366; JOIN barcodes @13366; JOIN product_categories @13366 |
| <span id="m-cb568efc6fac"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>13434–13550 | IsNullOrWhiteSpace @13436; Trim @13439; ToList @13442; Where @13442; IsNullOrEmpty @13443; Equals @13443; ToString @13445; AddToCart @13451; CreateCommand @13467; CreateParameter @13485; Add @13488; ExecuteReader @13490; Read @13492; Parse @13494; GetString @13494; ContainsKey @13495; GetInt64 @13499; Pow @13501; IsDBNull @13503; TryParse @13509; GetInt32 @13510; First @13539; Add @13540 | FROM barcodes @13468; FROM items @13468; JOIN barcodes @13468; JOIN product_categories @13468 |
| <span id="m-14394bf60f6d"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>13552–13595 | IsNullOrWhiteSpace @13554; Trim @13557; AppendReceiveSerialScan @13563; TryAddUniqueExactMatchToCart @13569; Clear @13571; ToList @13576; Where @13576; Equals @13576; AddToCart @13579 | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/Views/MainWindow.axaml</code> · 6220 lines · SHA-256 <code>dd5e4b37b2437a1c357520f357099b818335b744771fb558987e91d8511c9934</code>.
