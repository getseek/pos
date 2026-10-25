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

<code>Software/src/GetSeek.Desktop/Models/UiModels.cs</code> · 890 lines.

SHA-256: <code>27eb5b1e6007d0e4bbecb5df84dbe3bf1304c005015dff19b5c3187e1588d0fa</code>.

Declarations: <code>CurrencyFormatter</code> (line 6), <code>CategoryItem : ReactiveObject</code> (line 20), <code>ProductCategoryOption</code> (line 47), <code>ExpenseCategoryOption</code> (line 64), <code>ProductPurposeOption</code> (line 79), <code>UomOption</code> (line 84), <code>StoreUomPreferenceItem : ReactiveObject</code> (line 138), <code>ProductItem : ReactiveObject</code> (line 160), <code>OrderItem : ReactiveObject</code> (line 192), <code>ParkedCart</code> (line 303), <code>StaleCartPriceReviewUiRow</code> (line 317), <code>LotCandidateItem</code> (line 325), <code>SerialCandidateItem : ReactiveObject</code> (line 340), <code>OrderStatusChip : ReactiveObject</code> (line 364), <code>OrderLogItem : ReactiveObject</code> (line 404), <code>InventoryItem : ReactiveObject</code> (line 435), <code>KitComponentDraftItem : ReactiveObject</code> (line 568), <code>PayrollMonthOption : IEquatable&lt;PayrollMonthOption&gt;</code> (line 600), <code>StaffMember : ReactiveObject</code> (line 624), <code>TeamMemberShiftItem : ReactiveObject</code> (line 684), <code>UserPermissionOverrideItem : ReactiveObject</code> (line 695), <code>ReportTenderItem : ReactiveObject</code> (line 753), <code>ShiftReportSummary : ReactiveObject</code> (line 762), <code>FacilityItem : ReactiveObject</code> (line 802), <code>BinLocationItem : ReactiveObject</code> (line 812), <code>ItemLocationEligibilityItem : ReactiveObject</code> (line 826), <code>ReceiveTrackingKind</code> (line 841), <code>ReceiveLineItem : ReactiveObject</code> (line 853).

<details markdown>
<summary>Methods, calls, table effects and failures (11)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-7303823d0b7e"></span><code>CurrencyFormatter.Format(decimal,string,int)</code><br>8–17 | Clamp @10; Round @14; ToString @16 | No extracted literal effects. |
| <span id="m-1667c822cb94"></span><code>ProductCategoryOption.ToString()</code><br>61–61 | — | No extracted literal effects. |
| <span id="m-6c53d4e69e32"></span><code>ExpenseCategoryOption.ToString()</code><br>76–76 | — | No extracted literal effects. |
| <span id="m-3a2f50acce63"></span><code>ProductPurposeOption.ToString()</code><br>81–81 | — | No extracted literal effects. |
| <span id="m-b2cf49c707d1"></span><code>UomOption.ToString()</code><br>135–135 | — | No extracted literal effects. |
| <span id="m-17e4b6792d49"></span><code>LotCandidateItem.ToString()</code><br>336–336 | — | No extracted literal effects. |
| <span id="m-5ac7af0232e8"></span><code>SerialCandidateItem.ToString()</code><br>361–361 | — | No extracted literal effects. |
| <span id="m-723795936d7c"></span><code>PayrollMonthOption.Equals(PayrollMonthOption?)</code><br>613–614 | — | No extracted literal effects. |
| <span id="m-01a30e10d9e7"></span><code>PayrollMonthOption.Equals(object?)</code><br>616–617 | Equals @617 | No extracted literal effects. |
| <span id="m-a92bd4bc1bb0"></span><code>PayrollMonthOption.GetHashCode()</code><br>619–619 | GetHashCode @619 | No extracted literal effects. |
| <span id="m-359cd6f7dbeb"></span><code>PayrollMonthOption.ToString()</code><br>621–621 | — | No extracted literal effects. |

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

<code>Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs</code> · 13,101 lines.

SHA-256: <code>7b0aa35adaf840d92e9b261eddd71dde40827cdc86a39d076d5852aa7435e90d</code>.

Declarations: <code>MainViewModel : ReactiveObject, IDisposable</code> (line 63), <code>TestLicenseServiceForVm : ILicenseService</code> (line 8690).

<details markdown>
<summary>Methods, calls, table effects and failures (254)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-4d3c549b9d46"></span><code>MainViewModel.RefreshCurrentTime()</code><br>121–121 | RaisePropertyChanged @121; nameof @121 | No extracted literal effects. |
| <span id="m-47378cde4176"></span><code>MainViewModel.SetStatusNotificationOnUi(string)</code><br>391–404 | RaiseAndSetIfChanged @393; IsNullOrWhiteSpace @394; Insert @396; RemoveAt @397; RaisePropertyChanged @398; nameof @398; Stop @401; Start @403 | No extracted literal effects. |
| <span id="m-fa69ff5d121c"></span><code>MainViewModel.ClearNotifications()</code><br>426–433 | Stop @428; Clear @430; RaisePropertyChanged @431; nameof @431; RaiseAndSetIfChanged @432 | No extracted literal effects. |
| <span id="m-f09d63cff8ad"></span><code>MainViewModel.CycleInventoryLifecycleStatusScope()</code><br>683–688 | — | No extracted literal effects. |
| <span id="m-30496ef3dd21"></span><code>MainViewModel.IsLockScreenLockedOut(int)</code><br>1202–1218 | Ceiling @1209 | No extracted literal effects. |
| <span id="m-5f62c8bc965d"></span><code>MainViewModel.RefreshUnlockCandidates()</code><br>1260–1285 | GetUnlockCandidates @1263; Clear @1266; Add @1269; Any @1271; CheckAccess @1277; action @1279; Post @1283 | No extracted literal effects. |
| <span id="m-0d03cc83cf82"></span><code>MainViewModel.UpdateReceiveKitBreakdownAsync()</code><br>1643–1663 | GetValueOrDefault @1651; ConfigureAwait @1656; BuildBreakdownSummaryAsync @1656 | No extracted literal effects. |
| <span id="m-ef70572bdea7"></span><code>MainViewModel.UpdateCartKitBreakdownAsync(OrderItem)</code><br>1665–1677 | ConfigureAwait @1670; BuildBreakdownSummaryAsync @1670 | No extracted literal effects. |
| <span id="m-2e8dafe20278"></span><code>MainViewModel.OnProductPricingDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>2102–2121 | RaisePropertyChanged @2104; nameof @2104; RecomputeProductPricingPreview @2120 | No extracted literal effects. |
| <span id="m-66abffa3c005"></span><code>MainViewModel.RecomputeProductPricingPreview()</code><br>2130–2180 | Clear @2132; RaisePropertyChanged @2133; nameof @2133; ToMinorUnits @2142; Parse @2147; TryParse @2151; Equals @2165; Increment @2168; Localize @2169; ToArray @2171; RecomputeKitPricingPreviewAsync @2172; ResolveSelectedProductSaleUnitFactor @2177; Round @2178; RebuildProductPricingPreview @2179 | No extracted literal effects. |
| <span id="m-a8a43fe4b8b3"></span><code>MainViewModel.RecomputeKitPricingPreviewAsync(long,string,string,decimal,string,long,decimal,IReadOnlyList&lt;KitComponentDraftItem&gt;)</code><br>2182–2252 | ConfigureAwait @2186; WaitAsync @2186; Read @2189; DispatchToUi @2193; SetProductPricingPreviewNotice @2193; CalculateItemOrKitAsync @2207; ResolveSelectedProductSaleUnitFactor @2231; Round @2232; RebuildProductPricingPreview @2236; Release @2250 | No extracted literal effects. |
| <span id="m-ce9c0b7c7191"></span><code>MainViewModel.SetProductPricingPreviewNotice(string)</code><br>2254–2258 | Localize @2256; RaisePropertyChanged @2257; nameof @2257 | No extracted literal effects. |
| <span id="m-b446322f4afb"></span><code>MainViewModel.RebuildProductPricingPreview(long,string,decimal,string,long,decimal)</code><br>2260–2324 | Clear @2263; RaisePropertyChanged @2265; nameof @2265; Equals @2266; SetProductPricingPreviewNotice @2268; ParsePricingMethod @2272; ParseRoundingRule @2273; IsRoundingRuleCompatible @2274; TryConvertRoundingIncrement @2281; ToMinorUnits @2288; ResolveEffectiveBasePrice @2289; ToList @2293; OrderBy @2293; Where @2293; FirstOrDefault @2300; TryParse @2311; ToString @2312; ResolveTierPrice @2315; Add @2317; Format @2319; ToDisplayAmount @2319; FirstOrDefault @2320 | No extracted literal effects. |
| <span id="m-b5c70e993c13"></span><code>MainViewModel.ResolveSelectedProductSaleUnitFactor()</code><br>2378–2393 | FirstOrDefault @2381; Equals @2381; TryParse @2385 | No extracted literal effects. |
| <span id="m-47b5c563cfe2"></span><code>MainViewModel.ExactMinorToCurrency(decimal)</code><br>2401–2402 | ScalingFactor @2402; Clamp @2402 | No extracted literal effects. |
| <span id="m-0b5686a17a23"></span><code>MainViewModel.BuildCostSourcesTooltip(long,long,long,long?,string,DateTime?)</code><br>2459–2479 | Format @2467; ToDecimal @2468; Localize @2471; Format @2471; ToLocalTime @2473; Join @2478 | No extracted literal effects. |
| <span id="m-dc830a0b78f4"></span><code>MainViewModel.AddKitComponent()</code><br>2639–2676 | IsNullOrWhiteSpace @2654; FirstOrDefault @2656; Equals @2657; Add @2664; RaisePropertyChanged @2675; nameof @2675 | No extracted literal effects. |
| <span id="m-ecd3ae52246a"></span><code>MainViewModel.RemoveKitComponent(KitComponentDraftItem?)</code><br>2678–2685 | Remove @2682; RaisePropertyChanged @2683; nameof @2683 | No extracted literal effects. |
| <span id="m-757bd6987816"></span><code>MainViewModel.RefreshVirtualKitAvailability()</code><br>2696–2709 | Increment @2698; ToArray @2705; Select @2705; LoadVirtualKitAvailabilityAsync @2708 | No extracted literal effects. |
| <span id="m-fc9271236fdc"></span><code>MainViewModel.LoadVirtualKitAvailabilityAsync(long,IReadOnlyList&lt;KitComponentInput&gt;)</code><br>2711–2751 | ConfigureAwait @2715; GetKitAvailabilityAsync @2715; DispatchToUi @2717; Read @2719; Localize @2722; Max @2731; ResolveSelectedProductSaleUnitFactor @2731; GetValueOrDefault @2732; Clamp @2733; Pow @2734; Floor @2735; Format @2737; ToString @2739 | No extracted literal effects. |
| <span id="m-7806a523ed18"></span><code>MainViewModel.ApplyThemePreference(string)</code><br>3593–3601 | IsNullOrWhiteSpace @3595 | No extracted literal effects. |
| <span id="m-9c5bc8eb9005"></span><code>MainViewModel.InitializeUiPreferences()</code><br>3603–3614 | Load @3605; IsNullOrWhiteSpace @3609; Resolve @3611; Apply @3613 | No extracted literal effects. |
| <span id="m-4093548aec41"></span><code>MainViewModel.OpenImport()</code><br>3643–3651 | CheckSessionUnlocked @3645; Increment @3647; ResetInventoryImport @3648; Invoke @3650 | No extracted literal effects. |
| <span id="m-183ab98d035b"></span><code>MainViewModel.PreviewImportFileAsync(string)</code><br>3653–3714 | Increment @3656; ResetInventoryImport @3661; IsNullOrWhiteSpace @3666; Exists @3666; FinishFailedImport @3668; ConfigureAwait @3680; ReadAllBytesAsync @3680; ToHexString @3681; HashData @3681; TemplateContextAsync @3685; Run @3686; Read @3686; ValidateInventoryAsync @3687; CompletedWorkbook @3688; DispatchToUi @3695; ReferenceEquals @3697; Add @3698; Localize @3699; SetImportReviewRows @3703; RaisePropertyChanged @3704; nameof @3704; ReportException @3710 | No extracted literal effects. |
| <span id="m-08bf162772ec"></span><code>MainViewModel.ConfirmImportAsync()</code><br>3716–3770 | IsCurrentImportAttempt @3732; ConfigureAwait(ImportProductsCommand, ImportProductsResult) @3746; ExecuteAsync(ImportProductsCommand, ImportProductsResult) @3746; ConfigureAwait @3750; RecoverImportOutcomeAsync @3750; Localize @3753; DispatchToUi @3754; FinishImportAttempt @3754; LoadInventoryAsync @3755; ReportException @3756; ReportError @3760; FinishFailedImport @3761; ImportCommandIssue @3761 | No extracted literal effects. |
| <span id="m-2f2add464096"></span><code>MainViewModel.ReportError(string,string?,string,Exception?,string?)</code><br>3782–3792 | Report @3784; DispatchToUi @3785; Insert @3787 | No extracted literal effects. |
| <span id="m-d6e90debedc2"></span><code>MainViewModel.ConfigureDiagnosticsWorkspace(string)</code><br>3794–3798 | RaisePropertyChanged @3797; nameof @3797 | No extracted literal effects. |
| <span id="m-6faa1f0cc7ec"></span><code>MainViewModel.ReportException(string,Exception)</code><br>3800–3803 | ReportError @3802 | No extracted literal effects. |
| <span id="m-bcc7b3ce8d63"></span><code>MainViewModel.SafeError(string,Exception)</code><br>3809–3814 | ReportError @3812 | No extracted literal effects. |
| <span id="m-cb76e384cdef"></span><code>MainViewModel.SafePipelineError(string,string?,string?)</code><br>3823–3829 | IsNullOrWhiteSpace @3825; Trim @3825; ReportError @3827 | No extracted literal effects. |
| <span id="m-44881953d59a"></span><code>MainViewModel.OnErrorSinkEntry(ErrorLogEntry)</code><br>3831–3834 | DispatchToUi @3833; Insert @3833 | No extracted literal effects. |
| <span id="m-bcf7fd260821"></span><code>MainViewModel.DispatchToUi(Action)</code><br>3840–3854 | CheckAccess @3842; action @3844; GetResult @3852; GetAwaiter @3852; InvokeAsync @3852 | No extracted literal effects. |
| <span id="m-37b7599fc39f"></span><code>MainViewModel.ConfigureModalCoordinator()</code><br>4514–4579 | Register @4516; Execute @4516; Execute @4517; Execute @4518; Execute @4519; Execute @4524; Execute @4525; Execute @4526; Execute @4527; Execute @4528; Execute @4529; Execute @4530; Execute @4531; Execute @4532; Execute @4533; Execute @4534; Execute @4535; Execute @4536; Execute @4537; Execute @4538; Execute @4539; Execute @4540; Execute @4541; Execute @4542; Execute @4543; Execute @4544; Execute @4545; Execute @4546; Execute @4547; Execute @4548; Execute @4549; Execute @4550; Execute @4551; Execute @4552; Execute @4553; Execute @4554; Execute @4555; Execute @4557; Execute @4558; RequestClosePersonForm @4559; KeepEditingPersonForm @4560; CloseSalaryMonthDetailModal @4561; CloseSalaryPaymentModal @4562; CloseSalaryAdjustmentModal @4563; CloseSalaryFinalizeModal @4564; RequestCloseExpenseForm @4565; KeepEditingExpenseForm @4566; CloseExpenseCategoryModal @4567; CloseExpensePaymentModal @4568; CloseExpenseDetailModal @4569; ClosePaymentReturnModal @4570; CloseWasteExpenseConfirmation @4571; InitializeSalaryTables @4576; InitializeExpensesTables @4577; InitializeTeamsCommands @4578 | No extracted literal effects. |
| <span id="m-fdc40c361cb4"></span><code>MainViewModel.CreateDemo()</code><br>4581–4588 | SetActiveCashier @4584; Parse @4584; RefreshUnlockCandidates @4586 | No extracted literal effects. |
| <span id="m-b8906d6e66f2"></span><code>MainViewModel.CreateInitializing()</code><br>4590–4598 | — | No extracted literal effects. |
| <span id="m-a88c3ad62939"></span><code>MainViewModel.CreateStartupError(string,string)</code><br>4600–4610 | — | No extracted literal effects. |
| <span id="m-d2044bf6a5b1"></span><code>MainViewModel.CreateProduction(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?,ISessionUnlockValidator?,ISessionContext?,CommandPipeline?,DbConnection?,IUnitOfWork?,IDisposable?,bool)</code><br>4612–4630 | ConfigureDiagnosticsWorkspace @4626; ResolveDiagnosticsWorkspace @4626; ApplyPersistedState @4627; RefreshUnlockCandidates @4628 | No extracted literal effects. |
| <span id="m-29ed0477b9fd"></span><code>MainViewModel.OpenDemoWorkspace()</code><br>4632–4660 | CheckSessionUnlocked @4634; HasPermission @4635; Equals @4646; GetFileNameWithoutExtension @4646; GetEntryAssembly @4648; Add @4650; Start @4653; ReportException @4658 | No extracted literal effects. |
| <span id="m-f0dbd10727c9"></span><code>MainViewModel.OpenRealWorkspace()</code><br>4662–4685 | CheckSessionUnlocked @4664; HasPermission @4665; Equals @4675; GetFileNameWithoutExtension @4675; Add @4676; GetEntryAssembly @4676; Start @4678; ReportException @4683 | No extracted literal effects. |
| <span id="m-fe4336eef696"></span><code>MainViewModel.Dispose()</code><br>4687–4708 | ClearImportResults @4690; Increment @4691; ResetFinancialWorkspace @4693; Dispose @4694; Stop @4695; CancelBatchPricingPreviewExpiry @4698; Dispose @4699; Dispose @4700; DisposeSearchStates @4706; SuppressFinalize @4707 | No extracted literal effects. |
| <span id="m-8ecbacb91668"></span><code>MainViewModel.OnNotificationDismissTimerTick(object?,EventArgs)</code><br>4710–4714 | Stop @4712 | No extracted literal effects. |
| <span id="m-6bac6bb0427c"></span><code>MainViewModel.InitializeCleanProduction()</code><br>4716–4754 | Clear @4726; Clear @4727; Clear @4728; Clear @4729; Clear @4730; Clear @4731; Clear @4732; Clear @4733; Clear @4734; Clear @4735 | No extracted literal effects. |
| <span id="m-ad005cf674ff"></span><code>MainViewModel.ApplyPersistedState(StoreProfileProjection,IReadOnlyList&lt;CatalogItemProjection&gt;,ActiveShiftProjection?)</code><br>4756–4871 | RaisePropertyChanged @4770; nameof @4770; Clear @4772; Clear @4773; Clear @4774; CreateCommand @4781; ExecuteReader @4783; Read @4784; TryParse @4786; GetString @4786; Add @4787; Add @4795; GroupBy @4796; Count @4798; Contains @4803; Add @4826; Add @4827; All @4830; SafeError @4833; SetActiveCashier @4841; ToString @4845; ToString @4848; ToLocalTime @4848; NotifyTotalsChanged @4870 | FROM item_kits @4782 |
| <span id="m-5e0e1ea71b33"></span><code>MainViewModel.InitializeDemoData()</code><br>4873–4953 | Add @4879; Add @4898; Add @4911; Add @4915; Add @4920; Add @4926; ApplyActivityFilter @4932; Add @4935; ApplyInventoryFilter @4944; Add @4947; Parse @4947; NotifyTotalsChanged @4952 | No extracted literal effects. |
| <span id="m-62fc6a89c86e"></span><code>MainViewModel.CheckSessionUnlocked(string)</code><br>4955–4968 | — | No extracted literal effects. |
| <span id="m-20496249e49e"></span><code>MainViewModel.SelectMenu(string)</code><br>4970–5041 | CheckSessionUnlocked @4972; NormalizeMenuKey @4976; LoadInvoicesAsync @4982; LoadCommercialAsync @4983; LoadActivityInvoicesAsync @4990; LoadTeamsStaffAsync @4993; LoadCatalogRegistryAsync @4994; UpdateDemoSeedingAvailabilityAsync @4997; UpdateReceiptDesignPreview @5000; RefreshDiagnosticsAsync @5001; LoadPriceLevelSettingsAsync @5002; LoadInventoryAsync @5005; LoadPriceProposalsAsync @5007; LoadReportDataAsync @5010; LoadFinancialRegisterAsync @5011; LoadCustomersAsync @5014; LoadSuppliersAsync @5015; LoadThirdPartiesAsync @5016; LoadManufacturingDataAsync @5021; LoadManagedUnitsAsync @5029; LoadManagedCategoriesAsync @5032; LoadSalaryWorkspaceAsync @5035; LoadExpensesWorkspaceAsync @5038 | No extracted literal effects. |
| <span id="m-8b1cc29612aa"></span><code>MainViewModel.NormalizeMenuKey(string)</code><br>5043–5062 | — | No extracted literal effects. |
| <span id="m-c872970ae2b7"></span><code>MainViewModel.LogOut()</code><br>5064–5085 | Clear @5066; RaisePropertyChanged @5069; nameof @5069; ClearNotifications @5071; ResetCashReview @5075; Lock @5078; RefreshUnlockCandidates @5083; UpdateDemoSeedingAvailabilityAsync @5084 | No extracted literal effects. |
| <span id="m-62ac3501e406"></span><code>MainViewModel.UnlockSession()</code><br>5087–5090 | UnlockSession @5089 | No extracted literal effects. |
| <span id="m-4f12e1bf8a99"></span><code>MainViewModel.UnlockSession(string?)</code><br>5092–5191 | IsLockScreenLockedOut @5100; IsNullOrWhiteSpace @5116; AuthenticateSelectedUser @5125; Lock @5130; AddSeconds @5136; AddMinutes @5153; Initialize @5172; Unlock @5173; Any @5177; Equals @5177; RaisePropertyChanged @5178; nameof @5178; LoadActivityInvoicesAsync @5182; LoadTrackOrdersAsync @5183; UpdateDemoSeedingAvailabilityAsync @5184; StartAutomaticDemoDatasetLoadAsync @5185 | No extracted literal effects. |
| <span id="m-f9e98e702030"></span><code>MainViewModel.PowerAction()</code><br>5193–5199 | CheckSessionUnlocked @5195 | No extracted literal effects. |
| <span id="m-9e1fb31e8023"></span><code>MainViewModel.CycleTable()</code><br>5201–5207 | CheckSessionUnlocked @5203 | No extracted literal effects. |
| <span id="m-ed34294ebcee"></span><code>MainViewModel.CycleDiningType()</code><br>5209–5215 | CheckSessionUnlocked @5211 | No extracted literal effects. |
| <span id="m-910ab8ecebab"></span><code>MainViewModel.CycleCustomer()</code><br>5217–5220 | OpenCustomerChooser @5219 | No extracted literal effects. |
| <span id="m-98b1b8b34a3a"></span><code>MainViewModel.OpenPromoDialog()</code><br>5222–5237 | CheckSessionUnlocked @5224; IsNullOrWhiteSpace @5231; RaisePropertyChanged @5235; nameof @5235 | No extracted literal effects. |
| <span id="m-750d45a18d69"></span><code>MainViewModel.ApplyPromoDialogAsync()</code><br>5239–5308 | CheckSessionUnlocked @5241; ToLowerInvariant @5254; Trim @5254; IsNullOrWhiteSpace @5261; Trim @5261; ToList @5269; Select @5269; ToMinorUnits @5273; Equals @5289; Calculate @5293; NotifyTotalsChanged @5305; ConfigureAwait @5307; SaveDurableCartAsync @5307 | No extracted literal effects. |
| <span id="m-d9e41fe1e07f"></span><code>MainViewModel.TogglePromo()</code><br>5310–5327 | CheckSessionUnlocked @5312; RemovePromo @5321; OpenPromoDialog @5325 | No extracted literal effects. |
| <span id="m-755ee106e22e"></span><code>MainViewModel.RemovePromo()</code><br>5329–5339 | NotifyTotalsChanged @5336; SaveDurableCartAsync @5338 | No extracted literal effects. |
| <span id="m-5ed5ec0fb85d"></span><code>MainViewModel.RemovePromoDialogAsync()</code><br>5341–5352 | CheckSessionUnlocked @5343; NotifyTotalsChanged @5349; ConfigureAwait @5351; SaveDurableCartAsync @5351 | No extracted literal effects. |
| <span id="m-21e4eba6110b"></span><code>MainViewModel.CancelPromoDialog()</code><br>5354–5358 | — | No extracted literal effects. |
| <span id="m-6e12cfa681a6"></span><code>MainViewModel.RecalculateCart()</code><br>5360–5414 | ToMinorUnits @5376; Add @5377; Equals @5398; Calculate @5402; ToDictionary @5405; TryGetValue @5408 | No extracted literal effects. |
| <span id="m-e74f2f92d045"></span><code>MainViewModel.CyclePaymentMethod()</code><br>5416–5423 | CheckSessionUnlocked @5418; ResetCashReview @5419 | No extracted literal effects. |
| <span id="m-50a0b70b3671"></span><code>MainViewModel.SelectCategory(CategoryItem)</code><br>5425–5433 | CheckSessionUnlocked @5427; ApplyFilter @5431 | No extracted literal effects. |
| <span id="m-a647024153e5"></span><code>MainViewModel.ApplyFilter()</code><br>5435–5457 | FirstOrDefault @5437; Clear @5440; AsEnumerable @5441; Where @5445; Equals @5445; IsNullOrWhiteSpace @5448; Contains @5450; Add @5455 | No extracted literal effects. |
| <span id="m-83a928abc5c2"></span><code>MainViewModel.AddToCart(ProductItem)</code><br>5459–5459 | AddToCart @5459 | No extracted literal effects. |
| <span id="m-569d18f19a1c"></span><code>MainViewModel.AddToCart(ProductItem,string?)</code><br>5461–5505 | CheckSessionUnlocked @5463; ResetCashReview @5464; ResolveProductSaleUnitFactor @5467; Round @5474; FirstOrDefault @5475; UpdateCartKitBreakdownAsync @5484; Add @5496; NotifyTotalsChanged @5499; SaveDurableCartAsync @5501; IsNullOrWhiteSpace @5503; ToString @5503; NewGuid @5503; RecordSuccessfulSearchUseAsync @5504; FromGuid @5504 | No extracted literal effects. |
| <span id="m-c3e6e05a7ddb"></span><code>MainViewModel.IncreaseQty(OrderItem)</code><br>5507–5520 | CheckSessionUnlocked @5509; ResetCashReview @5510; UpdateCartKitBreakdownAsync @5517; NotifyTotalsChanged @5518; SaveDurableCartAsync @5519 | No extracted literal effects. |
| <span id="m-58b26ee774be"></span><code>MainViewModel.DecreaseQty(OrderItem)</code><br>5522–5537 | CheckSessionUnlocked @5524; ResetCashReview @5525; UpdateCartKitBreakdownAsync @5529; Remove @5533; NotifyTotalsChanged @5535; SaveDurableCartAsync @5536 | No extracted literal effects. |
| <span id="m-6a854e017e77"></span><code>MainViewModel.LoadManualPaymentSettingsAsync()</code><br>5539–5545 | ConfigureAwait @5542; LoadAsync @5542; RefreshSavedPaymentImages @5543; CancelManualPaymentSettings @5544 | No extracted literal effects. |
| <span id="m-8a5bec08ad25"></span><code>MainViewModel.SetManualPaymentImage(bool,byte[],string)</code><br>5547–5576 | ValidImage @5554; CreatePaymentBitmap @5559; Dispose @5562; RaisePropertyChanged @5574; nameof @5574 | No extracted literal effects. |
| <span id="m-7c83e882b095"></span><code>MainViewModel.CancelManualPaymentSettings()</code><br>5578–5594 | Dispose @5588; CreatePaymentBitmap @5590; RaisePropertyChanged @5592; nameof @5592 | No extracted literal effects. |
| <span id="m-fef81a76012a"></span><code>MainViewModel.CreatePaymentBitmap(byte[])</code><br>5596–5600 | — | No extracted literal effects. |
| <span id="m-4f8c185d1b7d"></span><code>MainViewModel.RefreshSavedPaymentImages()</code><br>5602–5610 | Dispose @5604; CreatePaymentBitmap @5606; RaisePropertyChanged @5608; nameof @5608 | No extracted literal effects. |
| <span id="m-93a6da867e5f"></span><code>MainViewModel.ApplyManualPaymentSettingsAsync()</code><br>5612–5631 | ConfigureAwait @5621; ExecuteAsync @5621; DispatchToUi @5624; SafePipelineError @5624; LoadAsync @5627; RefreshSavedPaymentImages @5628; CancelManualPaymentSettings @5629 | No extracted literal effects. |
| <span id="m-da801f4842f8"></span><code>MainViewModel.ConfirmManualPaymentAsync()</code><br>5633–5652 | IsNullOrWhiteSpace @5637; Trim @5638; ToMinorUnits @5644; ConfigureAwait @5650; PlaceOrderAsync @5650 | No extracted literal effects. |
| <span id="m-02e9058b9d87"></span><code>MainViewModel.PlaceOrderAsync()</code><br>5654–5666 | PlaceOrderInternalAsync @5660 | No extracted literal effects. |
| <span id="m-84f3836fda7a"></span><code>MainViewModel.PlaceOrderInternalAsync()</code><br>5668–5869 | Localize @5672; ExecuteDemoPlaceOrder @5678; ConfigureAwait @5704; SaveDurableCartAsync @5704; ToMinorUnits @5712; Trim @5714; Equals @5725; Equals @5732; ResetCashReview @5734; Max @5792; Add @5797; ConfigureAwait(TakePaymentCommand, SalesInvoice) @5815; ExecuteAsync(TakePaymentCommand, SalesInvoice) @5815; Format @5827; ToDecimal @5827; DispatchToUi @5829; Clear @5833; NewGuid @5842; NotifyTotalsChanged @5843; LoadActivityInvoicesAsync @5850; OpenStaleCartPriceReviewAsync @5855; RequestElevationForCheckout @5857; SafePipelineError @5861; SafeError @5867 | No extracted literal effects. |
| <span id="m-16f0b5ecb23f"></span><code>MainViewModel.OpenStaleCartPriceReviewAsync()</code><br>5871–5903 | DispatchToUi @5875; ConfigureAwait(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5878; ExecuteAsync(ReviewStaleCartPricesCommand, StaleCartPriceReview) @5878; SafePipelineError @5883; ToArray @5887; Select @5887; Where @5887; FormatCartReviewMoney @5891; Clear @5898; Add @5899 | No extracted literal effects. |
| <span id="m-49c6823f0a64"></span><code>MainViewModel.FormatCartReviewMoney(long,string)</code><br>5905–5910 | ScalingFactor @5907; Format @5909; Equals @5909 | No extracted literal effects. |
| <span id="m-6a6c6ae18d4f"></span><code>MainViewModel.AcceptStaleCartPriceReviewAsync()</code><br>5912–5943 | CheckSessionUnlocked @5914; ConfigureAwait(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5916; ExecuteAsync(AcceptStaleCartPriceReviewCommand, StaleCartPriceReview) @5916; DispatchToUi @5921; SafePipelineError @5921; ConfigureAwait @5922; OpenStaleCartPriceReviewAsync @5922; FirstOrDefault @5929; ScalingFactor @5932; ResetCashReview @5936; Clear @5939; NotifyTotalsChanged @5940 | No extracted literal effects. |
| <span id="m-af344822afe8"></span><code>MainViewModel.CancelStaleCartPriceReview()</code><br>5945–5952 | Clear @5949; ResetCashReview @5950 | No extracted literal effects. |
| <span id="m-8545635edb24"></span><code>MainViewModel.ConfirmCashReviewAsync()</code><br>5954–5980 | CheckSessionUnlocked @5956; ResetCashReview @5963; ToMinorUnits @5974; ConfigureAwait @5979; PlaceOrderAsync @5979 | No extracted literal effects. |
| <span id="m-1a2594966b04"></span><code>MainViewModel.CancelCashReview()</code><br>5982–5986 | ResetCashReview @5984 | No extracted literal effects. |
| <span id="m-b05efdcceb38"></span><code>MainViewModel.ResetCashReview()</code><br>5988–5997 | — | No extracted literal effects. |
| <span id="m-fcaeb530e95f"></span><code>MainViewModel.ExecuteDemoPlaceOrder()</code><br>5999–6018 | RaisePropertyChanged @6010; nameof @6010; Clear @6013; ResetCashReview @6014; NotifyTotalsChanged @6015 | No extracted literal effects. |
| <span id="m-dc31a0d18b2e"></span><code>MainViewModel.SaveDurableCartAsync()</code><br>6020–6085 | ConfigureAwait @6024; WaitAsync @6024; ClearActiveCartAsync @6029; ToMinorUnits @6039; Add @6040; ToUpperInvariant @6043; ToString @6043; IsNullOrWhiteSpace @6046; SaveActiveCartAsync @6059; DispatchToUi @6078; SafeError @6078; Release @6083 | No extracted literal effects. |
| <span id="m-0bcace2b789d"></span><code>MainViewModel.RestoreActiveCartAsync()</code><br>6087–6146 | ConfigureAwait @6093; GetActiveCartAsync @6093; Clear @6105; FirstOrDefault @6108; ToDecimal @6112; Add @6122; NotifyTotalsChanged @6139 | No extracted literal effects. |
| <span id="m-062396c755dc"></span><code>MainViewModel.LoadActivityInvoicesAsync()</code><br>6148–6225 | ApplyPagedResult @6152; ToList @6153; ApplyActivityFilter @6157; HasPermission @6162; ConfigureAwait @6169; GetPagedActivityInvoicesAsync @6169; ToPageRequest @6172; ToDecimal @6178; Add @6179; ToString @6184; ToLocalTime @6184; DispatchToUi @6203; Clear @6205; Add @6208; SafeError @6222 | No extracted literal effects. |
| <span id="m-fe916f2cea16"></span><code>MainViewModel.LoadTrackOrdersAsync()</code><br>6227–6304 | HasPermission @6232; ConfigureAwait @6239; GetActiveOrdersAsync @6239; Clear @6240; ToDecimal @6244; Join @6278; Select @6278; Add @6280; ToString @6295; ToLocalTime @6295 | No extracted literal effects. |
| <span id="m-cfc1be65a986"></span><code>MainViewModel.SelectTrackOrderAsync(OrderStatusChip?)</code><br>6306–6333 | CheckSessionUnlocked @6308; Clear @6311; ConfigureAwait @6317; GetOrderByIdAsync @6317; Add @6322; DispatchToUi @6328; SafeError @6328 | No extracted literal effects. |
| <span id="m-c3ab8ff39e66"></span><code>MainViewModel.CloseOrderDetailsModal()</code><br>6335–6340 | Clear @6339 | No extracted literal effects. |
| <span id="m-7539d16b6b10"></span><code>MainViewModel.MarkPreparingAsync()</code><br>6342–6375 | CheckSessionUnlocked @6344; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6360; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6360; ConfigureAwait @6369; LoadTrackOrdersAsync @6369; DispatchToUi @6373; SafePipelineError @6373 | No extracted literal effects. |
| <span id="m-dd6670f07490"></span><code>MainViewModel.MarkReadyAsync()</code><br>6377–6410 | CheckSessionUnlocked @6379; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6395; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6395; ConfigureAwait @6404; LoadTrackOrdersAsync @6404; DispatchToUi @6408; SafePipelineError @6408 | No extracted literal effects. |
| <span id="m-b3341f62999a"></span><code>MainViewModel.MarkServedAsync()</code><br>6412–6445 | CheckSessionUnlocked @6414; ConfigureAwait(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6430; ExecuteAsync(UpdateRestaurantOrderStatusCommand, RestaurantOrder) @6430; ConfigureAwait @6439; LoadTrackOrdersAsync @6439; DispatchToUi @6443; SafePipelineError @6443 | No extracted literal effects. |
| <span id="m-b532768c53cd"></span><code>MainViewModel.CancelActiveOrderAsync()</code><br>6447–6475 | CheckSessionUnlocked @6449; Remove @6453; CloseOrderDetailsModal @6454; ConfigureAwait(CancelRestaurantOrderCommand, RestaurantOrder) @6463; ExecuteAsync(CancelRestaurantOrderCommand, RestaurantOrder) @6463; ConfigureAwait @6469; LoadTrackOrdersAsync @6469; DispatchToUi @6473; SafePipelineError @6473 | No extracted literal effects. |
| <span id="m-e300e34c0e7c"></span><code>MainViewModel.SettleActiveOrderAsync()</code><br>6477–6573 | CheckSessionUnlocked @6479; CloseOrderDetailsModal @6485; ConfigureAwait @6492; GetOrderByIdAsync @6492; Zero @6514; NewGuid @6520; ToList @6523; Select @6523; ToUpperInvariant @6526; ToString @6526; SaveActiveCartAsync @6535; ConfigureAwait(TakePaymentCommand, SalesInvoice) @6551; ExecuteAsync(TakePaymentCommand, SalesInvoice) @6551; DispatchToUi @6554; SafePipelineError @6554; ConfigureAwait(SettleRestaurantOrderCommand, RestaurantOrder) @6560; ExecuteAsync(SettleRestaurantOrderCommand, RestaurantOrder) @6560; LoadTrackOrdersAsync @6566; LoadActivityInvoicesAsync @6567 | No extracted literal effects. |
| <span id="m-aa3d52b91298"></span><code>MainViewModel.SelectOrderLog(OrderLogItem)</code><br>6575–6582 | CheckSessionUnlocked @6577 | No extracted literal effects. |
| <span id="m-df72290f920b"></span><code>MainViewModel.FilterActivity(string)</code><br>6601–6607 | CheckSessionUnlocked @6603; ApplyActivityFilter @6605 | No extracted literal effects. |
| <span id="m-ecf9459a6628"></span><code>MainViewModel.ApplyActivityFilter()</code><br>6609–6648 | Clear @6611; AsEnumerable @6612; Where @6617; IsNullOrWhiteSpace @6620; Trim @6622; Contains @6624; Contains @6625; Contains @6626; IsNullOrEmpty @6630; Equals @6632; ToList @6636; Add @6638; ApplyPagedResult @6642 | No extracted literal effects. |
| <span id="m-f54382d8bcd5"></span><code>MainViewModel.PrintAuditReceiptAsync()</code><br>6650–6686 | CheckSessionUnlocked @6652; ConfigureAwait(QueueReceiptReprintCommand, string) @6672; ExecuteAsync(QueueReceiptReprintCommand, string) @6672; IsNullOrWhiteSpace @6673; ReportError @6675; RefreshOutputStatusAsync @6680; DispatchToUi @6684; SafeError @6684 | No extracted literal effects. |
| <span id="m-9bffe5b3d1cc"></span><code>MainViewModel.LoadOutputDevicesAsync()</code><br>6688–6731 | RefreshOutputPrinterQueues @6693; ReadAsync @6694; Equals @6701; IsNullOrWhiteSpace @6701; TryReadGeometry @6703; ComputeCapabilityFingerprint @6707; ConfigureAwait @6711; InvalidateThermalVerificationAsync @6711; LoadCashFinancialSettingsAsync @6723; LoadReceiptDesignAsync @6724; RefreshOutputStatusAsync @6725; DispatchToUi @6729; SafeError @6729 | No extracted literal effects. |
| <span id="m-0f0822925da5"></span><code>MainViewModel.SaveOutputDevicesAsync()</code><br>6733–6759 | ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6746; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6746; ReportError @6749; LoadOutputDevicesAsync @6752; DispatchToUi @6757; SafeError @6757 | No extracted literal effects. |
| <span id="m-7920bf1c2778"></span><code>MainViewModel.VerifyThermalPrinterAsync()</code><br>6761–6834 | Equals @6775; IsNullOrWhiteSpace @6780; IsWindows @6785; TryReadGeometry @6790; ConfigureAwait(UpdateOutputDeviceSettingsCommand, bool) @6807; ExecuteAsync(UpdateOutputDeviceSettingsCommand, bool) @6807; ReportError @6810; Render @6813; ToString @6814; ConfigureAwait @6815; Run @6815; Send @6815; ComputeCapabilityFingerprint @6816; ConfigureAwait(RecordThermalTestSpoolAcceptedCommand, bool) @6817; ExecuteAsync(RecordThermalTestSpoolAcceptedCommand, bool) @6817; RefreshOutputStatusAsync @6828; DispatchToUi @6832; SafeError @6832 | No extracted literal effects. |
| <span id="m-f0a0cea541d4"></span><code>MainViewModel.ConfirmThermalPrinterPhysicalOutputAsync()</code><br>6836–6873 | IsWindows @6850; IsNullOrWhiteSpace @6850; TryReadGeometry @6852; ComputeCapabilityFingerprint @6856; ConfigureAwait(ConfirmThermalPhysicalOutputCommand, bool) @6857; ExecuteAsync(ConfirmThermalPhysicalOutputCommand, bool) @6857; ReportError @6861; ConfigureAwait @6867; RefreshOutputStatusAsync @6867; DispatchToUi @6871; SafeError @6871 | InvalidOperationException @6851; InvalidOperationException @6855 |
| <span id="m-c5ab7b815927"></span><code>MainViewModel.LoadCashFinancialSettingsAsync()</code><br>6875–6912 | CreateCommand @6880; ConfigureAwait @6889; ExecuteReaderAsync @6889; ReadAsync @6890; GetInt32 @6893; GetString @6893; GetInt64 @6893; Parse @6894; RaisePropertyChanged @6896; nameof @6896; NotifyTotalsChanged @6905; DispatchToUi @6910; SafeError @6910 | FROM store_config @6881 |
| <span id="m-8503188ead58"></span><code>MainViewModel.SaveCashFinancialSettingsAsync()</code><br>6914–6942 | ConfigureAwait @6927; ExecuteAsync @6927; ReportError @6930; NotifyTotalsChanged @6935; DispatchToUi @6940; SafeError @6940 | No extracted literal effects. |
| <span id="m-72309acc4d05"></span><code>MainViewModel.LoadReceiptDesignAsync()</code><br>6944–6988 | DispatchToUi @6948; CreateCommand @6953; ConfigureAwait @6959; ExecuteReaderAsync @6959; ReadAsync @6960; Deserialize(ReceiptDesignDocument) @6962; GetString @6962; SafeError @6981 | FROM receipt_designs @6954; JOIN receipt_design_versions @6954 |
| <span id="m-51e76f18fa5b"></span><code>MainViewModel.SaveReceiptDesignAsync()</code><br>6990–7017 | ConfigureAwait @7003; ExecuteAsync @7003; ReportError @7008; DispatchToUi @7015; SafeError @7015 | No extracted literal effects. |
| <span id="m-33f8f207b431"></span><code>MainViewModel.RefreshOutputPrinterQueues()</code><br>7019–7031 | IsWindows @7021; Select @7022; Enumerate @7022; Empty(string) @7023; ToArray @7024; OrderBy @7024; Distinct @7024; Where @7024; Append @7024; IsNullOrWhiteSpace @7025; Clear @7029; Add @7030 | No extracted literal effects. |
| <span id="m-92c6c594622c"></span><code>MainViewModel.UpdateReceiptDesignPreview()</code><br>7033–7091 | CheckAccess @7035; DispatchToUi @7037; CreateSampleData @7043; Equals @7049; IsWindows @7056; TryReadGeometry @7057; BuildPaperDocument @7066; RenderPreviewPngPages @7069; SetReceiptDesignPreviewPages @7071; Localize @7073; BuildThermalLines @7078; RenderPreviewPng @7080; Empty(byte[]) @7087; ReportException @7089 | No extracted literal effects. |
| <span id="m-53778abbb08d"></span><code>MainViewModel.SetReceiptDesignPreviewPages(IReadOnlyList&lt;byte[]&gt;)</code><br>7093–7098 | ShowReceiptDesignPreviewPage @7097 | No extracted literal effects. |
| <span id="m-3f98d794a44e"></span><code>MainViewModel.MoveReceiptPreviewPage(int)</code><br>7100–7106 | ShowReceiptDesignPreviewPage @7105 | No extracted literal effects. |
| <span id="m-eded9e45cbd5"></span><code>MainViewModel.ShowReceiptDesignPreviewPage()</code><br>7108–7122 | RaisePropertyChanged @7119; nameof @7119 | No extracted literal effects. |
| <span id="m-37a6983f8c4c"></span><code>MainViewModel.RefreshOutputStatusAsync()</code><br>7124–7153 | ReadAsync @7127; Localize @7130; CreateCommand @7132; ConfigureAwait @7134; ExecuteScalarAsync @7134; ToString @7134; IsNullOrWhiteSpace @7135; ExecuteReaderAsync @7149; ReadAsync @7150; Trim @7151; GetString @7151 | FROM hardware_jobs @7133; FROM hardware_jobs @7148 |
| <span id="m-109b0906f97d"></span><code>MainViewModel.ApplyInventoryFilter()</code><br>7155–7171 | Clear @7157; AsEnumerable @7158; Where @7161; IsNullOrWhiteSpace @7163; Contains @7165; Contains @7166; Contains @7167; Add @7170 | No extracted literal effects. |
| <span id="m-dc5bcd2d8103"></span><code>MainViewModel.GenerateXReport()</code><br>7173–7192 | CheckSessionUnlocked @7175; ToString @7179; GenerateXReportInternalAsync @7191 | No extracted literal effects. |
| <span id="m-5d791c3fff57"></span><code>MainViewModel.GenerateXReportInternalAsync()</code><br>7194–7209 | ConfigureAwait @7198; LoadReportDataAsync @7198; DispatchToUi @7207; SafeError @7207 | No extracted literal effects. |
| <span id="m-c6be24f6028a"></span><code>MainViewModel.CloseShiftZReport()</code><br>7211–7214 | OpenCloseShiftModal @7213 | No extracted literal effects. |
| <span id="m-511f8dcc04e1"></span><code>MainViewModel.QuickAdjustStock(InventoryItem)</code><br>7216–7225 | CheckSessionUnlocked @7223 | No extracted literal effects. |
| <span id="m-306323eadd6b"></span><code>MainViewModel.SaveSettings()</code><br>7227–7231 | CheckSessionUnlocked @7229 | No extracted literal effects. |
| <span id="m-275ace5db49a"></span><code>MainViewModel.ApplySettingsAsync()</code><br>7233–7320 | CheckSessionUnlocked @7242; NotifyTotalsChanged @7261; ExecuteAsync @7289; DispatchToUi @7313; SafePipelineError @7313; SafeError @7318 | No extracted literal effects. |
| <span id="m-1898548cd67d"></span><code>MainViewModel.CancelSettings()</code><br>7322–7343 | CheckSessionUnlocked @7324; NotifyTotalsChanged @7336 | No extracted literal effects. |
| <span id="m-df37e534e698"></span><code>MainViewModel.RefreshDiagnosticsAsync()</code><br>7346–7376 | ProbeDatabaseAsync @7359; ProbeLicense @7365; RefreshOutputStatusAsync @7368; ProbeHardwareStubs @7369; DispatchToUi @7374; SafeError @7374 | No extracted literal effects. |
| <span id="m-ed266e09de1d"></span><code>MainViewModel.RaiseWorkspaceResetLabels()</code><br>7437–7475 | RaisePropertyChanged @7439; nameof @7439; FormatRealResetPreviewSummary @7474 | No extracted literal effects. |
| <span id="m-3428eb662297"></span><code>MainViewModel.FormatRealResetPreviewSummary(RealResetPreview)</code><br>7477–7490 | Localize @7478; ToString @7480; GetValueOrDefault @7480; ToString @7485; ToString @7486; ToString @7487 | No extracted literal effects. |
| <span id="m-a1fda82e5952"></span><code>MainViewModel.UpdateDemoSeedingAvailabilityAsync()</code><br>7599–7691 | Post @7603; ConfigureAwait @7610; GetWorkspaceEnvironmentAsync @7610; Equals @7611; GetDatasetStateAsync @7613; CreateCommand @7619; CreateParameter @7626; ToString @7628; Add @7629; ExecuteScalarAsync @7630; HasPermission @7635; ToInt64 @7640; ExecuteScalarAsync @7640; ExecuteScalarAsync @7644; ExecuteScalarAsync @7651; ExecuteScalarAsync @7657; Localize @7676 | FROM items @7639; FROM sales_invoices @7643; FROM third_parties @7656; FROM users @7620; JOIN user_roles @7620 · DYNAMIC SQL: inspect manually |
| <span id="m-60770d369812"></span><code>MainViewModel.OpenDemoResetConfirmation()</code><br>7693–7703 | CheckSessionUnlocked @7695; HasPermission @7696 | No extracted literal effects. |
| <span id="m-dae307e8321e"></span><code>MainViewModel.ConfirmDemoResetAsync()</code><br>7705–7710 | ConfigureAwait @7709; ResetDatabaseAsync @7709 | No extracted literal effects. |
| <span id="m-4bcad22b3b66"></span><code>MainViewModel.SeedLargeScaleDemoDataAsync()</code><br>7712–7713 | ConfigureAwait @7713; EnsureDefaultDemoDatasetAsync @7713 | No extracted literal effects. |
| <span id="m-59ed02da469e"></span><code>MainViewModel.StartAutomaticDemoDatasetLoadAsync()</code><br>7715–7721 | EnsureDefaultDemoDatasetAsync @7719 | No extracted literal effects. |
| <span id="m-dc37a49ff771"></span><code>MainViewModel.EnsureDefaultDemoDatasetAsync(bool)</code><br>7723–7827 | Localize @7728; ConfigureAwait @7735; WaitAsync @7735; GetWorkspaceEnvironmentAsync @7738; Equals @7739; HasPermission @7746; Post @7760; LocalizeDemoSeedProgress @7762; EnsureInitialDatasetAsync @7768; Join @7792; Select @7792; ReloadCatalogAsync @7802; LoadInventoryAsync @7803; LoadThirdPartiesAsync @7804; LoadManufacturingDataAsync @7805; LoadSuppliersAsync @7806; UpdateDemoSeedingAvailabilityAsync @7807; ToUpperInvariant @7812; ToString @7812; NewGuid @7812; LogDiagnosticError @7813; ReportError @7818; Release @7825 | No extracted literal effects. |
| <span id="m-48013c0e69f8"></span><code>MainViewModel.LocalizeDemoSeedProgress(string)</code><br>7829–7843 | Localize @7831 | No extracted literal effects. |
| <span id="m-f555e608cc83"></span><code>MainViewModel.ResetDatabaseAsync()</code><br>7845–7942 | Localize @7849; ConfigureAwait @7853; WaitAsync @7853; HasPermission @7857; GetWorkspaceEnvironmentAsync @7864; Equals @7865; ResetDatabaseAsync @7873; GetStoreProfileAsync @7876; Post @7877; Clear @7880; Clear @7881; Clear @7882; NewGuid @7883; RaisePropertyChanged @7886; nameof @7886; Lock @7887; Defaults @7900; RefreshUnlockCandidates @7913; LoadCashFinancialSettingsAsync @7914; LoadOutputDevicesAsync @7915; LoadManualPaymentSettingsAsync @7916; LoadReceiptDesignAsync @7917; ReloadCatalogAsync @7918; LoadInventoryAsync @7919; LoadThirdPartiesAsync @7920; LoadManufacturingDataAsync @7921; LoadActivityInvoicesAsync @7922; UpdateDemoSeedingAvailabilityAsync @7923; ToUpperInvariant @7928; ToString @7928; LogDiagnosticError @7929; ReportError @7935; Release @7940 | No extracted literal effects. |
| <span id="m-472b9671fb93"></span><code>MainViewModel.OpenRealShopResetAsync()</code><br>7944–7986 | CheckSessionUnlocked @7946; HasPermission @7948; ConfigureAwait @7956; GetWorkspaceEnvironmentAsync @7956; Equals @7957; PreviewAsync @7960; FormatRealResetPreviewSummary @7961; Post @7962; RaisePropertyChanged @7979; nameof @7979; SafeError @7984 | UnauthorizedAccessException @7958 |
| <span id="m-4b6df59b7c19"></span><code>MainViewModel.ConfirmRealShopResetAsync()</code><br>7988–8074 | HasPermission @7991; ConfigureAwait @8009; ExecuteAsync @8009; GetStoreProfileAsync @8018; Post @8021; Clear @8025; Clear @8026; Clear @8027; Clear @8028; NewGuid @8029; Lock @8032; RaisePropertyChanged @8046; nameof @8046; LoadCashFinancialSettingsAsync @8047; LoadOutputDevicesAsync @8048; LoadManualPaymentSettingsAsync @8049; LoadReceiptDesignAsync @8050; RefreshUnlockCandidates @8058; LoadInventoryAsync @8059; LoadActivityInvoicesAsync @8060; UpdateDemoSeedingAvailabilityAsync @8061; ToUpperInvariant @8066; ToString @8066; LogDiagnosticError @8067 | No extracted literal effects. |
| <span id="m-6e3e411843b3"></span><code>MainViewModel.CancelRealShopReset()</code><br>8076–8083 | RaisePropertyChanged @8082; nameof @8082 | No extracted literal effects. |
| <span id="m-dc80159876df"></span><code>MainViewModel.ExportReceiptDocumentAsync(Guid)</code><br>8087–8104 | ConfigureAwait @8089; ExportDocumentAsync @8089; Post @8093; GetFileName @8097 | No extracted literal effects. |
| <span id="m-e3e08b0bac19"></span><code>MainViewModel.OpenDocumentsFolder()</code><br>8106–8128 | Exists @8111; CreateDirectory @8113; Start @8115; ToUpperInvariant @8124; ToString @8124; NewGuid @8124; LogDiagnosticError @8125 | No extracted literal effects. |
| <span id="m-253f82dbc754"></span><code>MainViewModel.OpenNumpadForOrderItem(OrderItem)</code><br>8130–8140 | CheckSessionUnlocked @8132; RaisePropertyChanged @8134; nameof @8134; Localize @8136; ToString @8137 | No extracted literal effects. |
| <span id="m-35396ca17c6e"></span><code>MainViewModel.OpenNumpadForOrderItemPrice(OrderItem)</code><br>8147–8163 | CheckSessionUnlocked @8149; HasPermission @8150; RaisePropertyChanged @8156; nameof @8156; Localize @8159; ToString @8160 | No extracted literal effects. |
| <span id="m-aff9d71c8d12"></span><code>MainViewModel.CommitNumpad()</code><br>8165–8242 | CheckSessionUnlocked @8167; ResetCashReview @8168; TryParse @8174; IsNullOrWhiteSpace @8176; Trim @8182; NotifyTotalsChanged @8192; SaveDurableCartAsync @8193; Min @8199; ToMinorUnits @8201; Round @8202; TryParse @8217; UpdateCartKitBreakdownAsync @8225; Remove @8231; RaisePropertyChanged @8240; nameof @8240 | No extracted literal effects. |
| <span id="m-92b3d328dc9b"></span><code>MainViewModel.ToggleBusinessProfile()</code><br>8248–8266 | CheckSessionUnlocked @8256 | No extracted literal effects. |
| <span id="m-49eeee829528"></span><code>MainViewModel.StageBusinessProfile()</code><br>8273–8303 | CheckSessionUnlocked @8275; HasPermission @8279 | No extracted literal effects. |
| <span id="m-32fd070dfe0e"></span><code>MainViewModel.ToggleServiceStyle()</code><br>8305–8314 | — | No extracted literal effects. |
| <span id="m-264634408842"></span><code>MainViewModel.NotifyTotalsChanged()</code><br>8316–8339 | RecalculateCart @8318; RaisePropertyChanged @8320; nameof @8320 | No extracted literal effects. |
| <span id="m-3c0c8f7acf40"></span><code>MainViewModel.ProvisionInitialAdminAsync()</code><br>8341–8428 | IsNullOrWhiteSpace @8344; Trim @8344; All @8354; Trim @8371; Trim @8372; NewGuid @8376; ToString @8381; ConfigureAwait @8385; BeginTransactionAsync @8385; HandleAsync @8386; AppendAsync @8391; ToString @8392; Serialize @8397; CommitAsync @8400; Initialize @8406; Unlock @8407; RaisePropertyChanged @8412; nameof @8412; LoadTeamsStaffAsync @8415; StartAutomaticDemoDatasetLoadAsync @8416; RollbackAsync @8420; DispatchToUi @8421; SafePipelineError @8421; SafeError @8426 | No extracted literal effects. |
| <span id="m-b7d1f78c6b2d"></span><code>MainViewModel.CreateStaffMemberAsync()</code><br>8430–8437 | IsNullOrWhiteSpace @8432; ConfigureAwait @8436; SaveTeamMemberAsync @8436 | No extracted literal effects. |
| <span id="m-34bb84ce3ff8"></span><code>MainViewModel.OpenChangePinModal(StaffMember?)</code><br>8439–8457 | CheckSessionUnlocked @8442; HasPermission @8444 | No extracted literal effects. |
| <span id="m-e0a431eda0fd"></span><code>MainViewModel.CancelChangePin()</code><br>8459–8466 | — | No extracted literal effects. |
| <span id="m-405f738eafbc"></span><code>MainViewModel.ConfirmChangePinAsync()</code><br>8468–8544 | Trim @8476; IsNullOrWhiteSpace @8479; All @8485; Equals @8498; Equals @8499; SetQuickPin @8511; ConfigureAwait(UpdateUserQuickPinCommand, bool) @8524; ExecuteAsync(UpdateUserQuickPinCommand, bool) @8524; ConfigureAwait @8532; LoadTeamsStaffAsync @8532; DispatchToUi @8537; SafePipelineError @8537; SafeError @8542 | No extracted literal effects. |
| <span id="m-93d8d981cc35"></span><code>MainViewModel.OpenPermissionEditorAsync(StaffMember?)</code><br>8546–8620 | HasPermission @8552; ConfigureAwait @8561; ResolveEffectivePermissionsAsync @8561; Contains @8594; Contains @8595; Add @8597; Contains @8603; DispatchToUi @8609; Clear @8611; Add @8612; SafeError @8618 | No extracted literal effects. |
| <span id="m-47ef7bd73b6f"></span><code>MainViewModel.SetOverrideModeAsync(UserPermissionOverrideItem?,string)</code><br>8622–8664 | OnTeamMemberFieldChanged @8628; ConfigureAwait @8645; ExecuteAsync @8645; DispatchToUi @8649; SafePipelineError @8657; SafeError @8662 | No extracted literal effects. |
| <span id="m-1fd29c79f44d"></span><code>MainViewModel.ClosePermissionEditor()</code><br>8666–8671 | — | No extracted literal effects. |
| <span id="m-06931bc4e641"></span><code>MainViewModel.SetDbConnectionForTesting(DbConnection,SqliteUnitOfWork)</code><br>8673–8688 | ClearImportResults @8675 | No extracted literal effects. |
| <span id="m-f2225737055d"></span><code>TestLicenseServiceForVm.IsModuleLicensed(string)</code><br>8692–8692 | — | No extracted literal effects. |
| <span id="m-36e3d4373755"></span><code>TestLicenseServiceForVm.VerifyDeviceBinding()</code><br>8693–8693 | — | No extracted literal effects. |
| <span id="m-5038c0f4513b"></span><code>TestLicenseServiceForVm.CheckClockTamperAsync(DateTime,CancellationToken)</code><br>8694–8694 | FromResult @8694 | No extracted literal effects. |
| <span id="m-756227677341"></span><code>MainViewModel.OpenShiftForStaffAsync(Guid,decimal)</code><br>8697–8782 | HasPermission @8706; FromDecimal @8721; ConfigureAwait(OpenShiftCommand, Shift) @8725; ExecuteAsync(OpenShiftCommand, Shift) @8725; SetActiveCashier @8740; RefreshUnlockCandidates @8741; ToUpperInvariant @8758; ToString @8758; ToString @8760; ConfigureAwait @8770; LoadTeamsStaffAsync @8770; LoadTrackOrdersAsync @8771; DispatchToUi @8775; SafePipelineError @8775; SafeError @8780 | No extracted literal effects. |
| <span id="m-487f37151856"></span><code>MainViewModel.LoadInventoryAsync()</code><br>8784–8938 | ApplyPagedResult @8788; ToList @8789; ApplyInventoryFilter @8793; Clear @8801; Empty(InventoryItem) @8803; ConfigureAwait @8808; GetPagedInventoryItemsAsync @8808; ToPageRequest @8813; CreateCommand @8826; ExecuteReaderAsync @8828; ReadAsync @8829; Add @8831; Parse @8831; GetString @8831; ExecuteReaderAsync @8841; ReadAsync @8842; TryParse @8844; GetString @8844; IsDBNull @8844; Add @8855; TryGetValue @8857; Contains @8865; ToDecimal @8868; Localize @8876; ToLocalTime @8882; BuildCostSourcesTooltip @8884; DispatchToUi @8911; Add @8914; SafeError @8936 | FROM item_kits @8827; FROM item_pricing @8840 |
| <span id="m-5f157b24d9c2"></span><code>MainViewModel.OpenReceiveStock(InventoryItem?)</code><br>8940–8996 | CheckSessionUnlocked @8942; FirstOrDefault @8943; Clear @8954; Add @8956; CreateCommand @8961; CreateParameter @8972; Add @8975; ExecuteReader @8976; Read @8977; GetString @8979; Contains @8980; FirstOrDefault @8992; ResetReceiveLines @8993; UpdateReceiveKitBreakdownAsync @8994 | FROM uoms @8962; JOIN uoms @8962 |
| <span id="m-7070db7e3cab"></span><code>MainViewModel.ConfirmReceiveStockAsync()</code><br>8998–9099 | IsNullOrWhiteSpace @9011; Localize @9028; HasPermission @9032; BuildReceiptLines @9038; Sum @9055; Trim @9065; ToMinorUnits @9070; ConfigureAwait(ReceiveStockCommand, StockMovement) @9075; ExecuteAsync(ReceiveStockCommand, StockMovement) @9075; Clear @9085; ConfigureAwait @9087; LoadInventoryAsync @9087; LoadItemHistoryAsync @9088; DispatchToUi @9092; SafePipelineError @9092; SafeError @9097 | No extracted literal effects. |
| <span id="m-bbc820dea0b3"></span><code>MainViewModel.ResetReceiveLines()</code><br>9105–9122 | Clear @9107; Add @9111; RaisePropertyChanged @9117; nameof @9117; Invoke @9120 | No extracted literal effects. |
| <span id="m-c2090beb1fcf"></span><code>MainViewModel.AddReceiveLine()</code><br>9125–9148 | IsNullOrWhiteSpace @9132; Add @9138; RaisePropertyChanged @9143; nameof @9143; Invoke @9146 | No extracted literal effects. |
| <span id="m-cb5f0c7e5d3d"></span><code>MainViewModel.RemoveReceiveLine(ReceiveLineItem)</code><br>9151–9168 | Remove @9158; Add @9161; RaisePropertyChanged @9167; nameof @9167 | No extracted literal effects. |
| <span id="m-f767f018421f"></span><code>MainViewModel.AppendReceiveSerialScan(string)</code><br>9174–9195 | IsNullOrWhiteSpace @9176; LastOrDefault @9181; Add @9185; Trim @9188; ReferenceEquals @9189; RaisePropertyChanged @9193; nameof @9193; Invoke @9194 | No extracted literal effects. |
| <span id="m-cec581c91cfa"></span><code>MainViewModel.BuildReceiptLines(string?)</code><br>9198–9275 | Add @9210; IsNullOrWhiteSpace @9218; Trim @9222; FirstOrDefault @9231; GroupBy @9231; Count @9233; Trim @9260 | No extracted literal effects. |
| <span id="m-78ffb233de22"></span><code>MainViewModel.LoadSuppliersAsync()</code><br>9277–9313 | CreateCommand @9282; ConfigureAwait @9289; ExecuteReaderAsync @9289; Clear @9290; ReadAsync @9291; Add @9293; ParseGuidSafe @9294; GetString @9294; IsDBNull @9298; GetInt32 @9302; Parse @9304; DispatchToUi @9311; SafeError @9311 | FROM third_parties @9283 |
| <span id="m-ec26f81870a5"></span><code>MainViewModel.OpenAdjustStock(InventoryItem?)</code><br>9315–9333 | CheckSessionUnlocked @9317; FirstOrDefault @9323 | No extracted literal effects. |
| <span id="m-d4e199833df9"></span><code>MainViewModel.ConfirmAdjustStockAsync()</code><br>9335–9426 | IsNullOrWhiteSpace @9358; HasPermission @9369; Trim @9387; Trim @9389; ConfigureAwait(AdjustStockCommand, StockMovement) @9393; ExecuteAsync(AdjustStockCommand, StockMovement) @9393; ConfigureAwait @9409; LoadInventoryAsync @9409; LoadItemHistoryAsync @9410; OpenWasteExpenseConfirmation @9414; DispatchToUi @9419; SafePipelineError @9419; SafeError @9424 | No extracted literal effects. |
| <span id="m-69541661f4c8"></span><code>MainViewModel.OpenAddProduct()</code><br>9428–9496 | ResetProductStockDraft @9430; CheckSessionUnlocked @9431; HasPermission @9432; RaisePropertyChanged @9440; nameof @9440; ClearItemHistory @9442; LoadCatalogRegistryAsync @9449; InitializeProductPricingDraft @9452; Clear @9467; Clear @9468; Where @9469; Add @9471; FirstOrDefault @9473; Clear @9484; CaptureProductModalBaselineAsync @9495 | No extracted literal effects. |
| <span id="m-68227c721b10"></span><code>MainViewModel.OpenEditProduct(InventoryItem)</code><br>9498–9498 | OpenEditProduct @9498 | No extracted literal effects. |
| <span id="m-96f2f847c9ba"></span><code>MainViewModel.OpenEditProduct(InventoryItem,int)</code><br>9500–9580 | ResetProductStockDraft @9502; CheckSessionUnlocked @9504; HasPermission @9505; RaisePropertyChanged @9513; nameof @9513; ClearItemHistory @9515; LoadCatalogRegistryAsync @9523; InitializeProductPricingDraft @9529; ToMinorUnits @9530; LoadExactProductCostSnapshotsAsync @9536; ToDecimal @9540; Clear @9547; Clear @9548; Where @9549; Add @9551; FirstOrDefault @9553; LoadItemLocationEligibilitiesAsync @9572; LoadProductKitAsync @9573; LoadPrimaryBarcodeAsync @9574; LoadProductPricingDraftAsync @9575; LoadItemHistoryAsync @9576; LoadItemPriceHistoryAsync @9577; CaptureProductModalBaselineAsync @9579 | No extracted literal effects. |
| <span id="m-4b321c5b0b88"></span><code>MainViewModel.InitializeProductPricingDraft(decimal)</code><br>9582–9595 | OrderBy @9585; Where @9585; Add @9587 | No extracted literal effects. |
| <span id="m-ab1aef425773"></span><code>MainViewModel.LoadProductPricingDraftAsync(Guid,decimal)</code><br>9597–9670 | CreateCommand @9604; CreateParameter @9611; ToString @9613; Add @9614; ConfigureAwait @9615; ExecuteReaderAsync @9615; ReadAsync @9616; GetInt32 @9618; IsDBNull @9619; GetString @9619; ParseStoredPricingPercentForDisplay @9620; ToDisplayAmount @9624; GetInt64 @9624; OrderBy @9644; Where @9644; TryGetValue @9647; Add @9653; InvokeAsync @9655; RaisePropertyChanged @9660; nameof @9660; CaptureProductPricingSnapshot @9663; DispatchToUi @9668; SafeError @9668 | FROM item_price_levels @9635; FROM item_pricing @9606 |
| <span id="m-d7bf802384d4"></span><code>MainViewModel.LoadProductCategoryPricingSuggestionAsync(Guid)</code><br>9672–9707 | CreateCommand @9679; CreateParameter @9685; ToString @9687; Add @9688; ConfigureAwait @9689; ExecuteReaderAsync @9689; ReadAsync @9690; Parse @9693; GetString @9693; GetInt32 @9693; GetInt64 @9694; IsDBNull @9694; Parse @9695; InvokeAsync @9697; DispatchToUi @9705; SafeError @9705 | FROM product_category_pricing_rules @9680 |
| <span id="m-0ec3ea53920e"></span><code>MainViewModel.CaptureProductModalBaselineAsync(Guid?,bool,Task[])</code><br>9709–9738 | ConfigureAwait @9713; WhenAll @9713; InvokeAsync @9714; CaptureProductModalSnapshot @9718; CaptureProductPricingSnapshot @9719; RaisePropertyChanged @9720; nameof @9720 | No extracted literal effects. |
| <span id="m-e4300cde7e0e"></span><code>MainViewModel.CaptureProductModalSnapshot()</code><br>9740–9788 | Serialize @9740; ToArray @9763; Select @9763; Select @9780; OrderBy @9780; OrderBy @9784 | No extracted literal effects. |
| <span id="m-273cfe17af36"></span><code>MainViewModel.CaptureProductPricingSnapshot()</code><br>9790–9802 | Serialize @9790; ToArray @9801; Select @9801 | No extracted literal effects. |
| <span id="m-81161011ac1a"></span><code>MainViewModel.OnProductDraftPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9804–9836 | nameof @9806; RaisePropertyChanged @9807; RaiseTraceabilityState @9812; StartsWith @9816; RecomputeProductPricingPreview @9827; RefreshVirtualKitAvailability @9829 | No extracted literal effects. |
| <span id="m-35f6e72334c8"></span><code>MainViewModel.OnProductKitComponentsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>9838–9852 | RaisePropertyChanged @9846; nameof @9846; RecomputeProductPricingPreview @9849; RefreshVirtualKitAvailability @9850 | No extracted literal effects. |
| <span id="m-d51789ad7fa1"></span><code>MainViewModel.OnProductKitComponentPropertyChanged(object?,PropertyChangedEventArgs)</code><br>9854–9862 | RaisePropertyChanged @9856; nameof @9856; RecomputeProductPricingPreview @9859; RefreshVirtualKitAvailability @9860 | No extracted literal effects. |
| <span id="m-da7cd1382622"></span><code>MainViewModel.RequestCloseProductModal()</code><br>9864–9877 | DiscardProductModal @9876 | No extracted literal effects. |
| <span id="m-15fce7e06914"></span><code>MainViewModel.DiscardProductModal()</code><br>9879–9888 | RaisePropertyChanged @9884; nameof @9884; ClearItemHistory @9886 | No extracted literal effects. |
| <span id="m-7ec1d73a2d38"></span><code>MainViewModel.LoadPrimaryBarcodeAsync(Guid)</code><br>9890–9908 | CreateCommand @9895; CreateParameter @9897; ToString @9899; Add @9900; ConfigureAwait @9901; ExecuteScalarAsync @9901; DispatchToUi @9904; ToString @9904 | FROM barcodes @9896 |
| <span id="m-63c90f8a455d"></span><code>MainViewModel.LoadProductKitAsync(Guid)</code><br>9910–9961 | CreateCommand @9915; CreateParameter @9922; ToString @9924; Add @9925; ConfigureAwait @9929; ExecuteReaderAsync @9929; ReadAsync @9930; IsDBNull @9933; GetString @9933; GetDouble @9934; ResolveQuantity @9935; Add @9936; Parse @9938; DispatchToUi @9946; Clear @9949; Add @9950; RaisePropertyChanged @9953; nameof @9953; RecomputeProductPricingPreview @9956; RefreshVirtualKitAvailability @9957 | FROM item_kits @9916; JOIN item_kit_components @9916; JOIN items @9916 |
| <span id="m-c16a90d38ce5"></span><code>MainViewModel.ConfirmSaveProductAsync()</code><br>9963–9963 | SaveProductConfigurationAsync @9963 | No extracted literal effects. |
| <span id="m-1d17ee94ca1f"></span><code>MainViewModel.SaveProductConfigurationAsync(bool)</code><br>9965–10170 | ConfigureAwait @9970; LoadCatalogRegistryAsync @9970; HasPermission @9972; IsNullOrWhiteSpace @9977; Localize @9999; Equals @10009; ToMinorUnits @10054; GetValueOrDefault @10066; Trim @10067; Trim @10068; Trim @10069; Trim @10076; Trim @10078; ToList @10123; Select @10123; CaptureProductPricingSnapshot @10127; ToCommand @10129; ConfigureAwait(SaveProductConfigurationCommand, CatalogItemDto) @10137; ExecuteAsync(SaveProductConfigurationCommand, CatalogItemDto) @10137; DispatchToUi @10140; RaiseTraceabilityState @10146; CaptureProductModalSnapshot @10148; RaisePropertyChanged @10150; nameof @10150; ReloadCatalogAsync @10157; LoadInventoryAsync @10158; LoadItemHistoryAsync @10159; SafePipelineError @10163; SafeError @10168 | No extracted literal effects. |
| <span id="m-8504d2d6becf"></span><code>MainViewModel.DeactivateProductAsync(InventoryItem)</code><br>10172–10208 | CheckSessionUnlocked @10174; HasPermission @10175; ConfigureAwait(DeactivateProductCommand, bool) @10191; ExecuteAsync(DeactivateProductCommand, bool) @10191; ConfigureAwait @10196; ReloadCatalogAsync @10196; LoadInventoryAsync @10197; DispatchToUi @10201; SafePipelineError @10201; SafeError @10206 | No extracted literal effects. |
| <span id="m-8322612cc844"></span><code>MainViewModel.ReloadCatalogAsync(CancellationToken)</code><br>10210–10285 | ConfigureAwait @10216; GetActiveItemsAsync @10216; Clear @10218; Clear @10219; Clear @10220; CreateCommand @10225; ExecuteReaderAsync @10227; ReadAsync @10228; TryParse @10230; GetString @10230; Add @10231; Add @10238; GroupBy @10239; Count @10241; Contains @10246; Add @10269; Add @10270; All @10273; SafeError @10276; ApplyFilter @10279 | FROM item_kits @10226 |
| <span id="m-8498fd1333f6"></span><code>MainViewModel.ParseGuidSafe(string?)</code><br>10287–10293 | IsNullOrWhiteSpace @10289; TryParse @10290; HashData @10291; GetBytes @10291; AsSpan @10292 | No extracted literal effects. |
| <span id="m-4581bd01db82"></span><code>MainViewModel.LoadFacilitiesAndBinsAsync()</code><br>10295–10361 | CreateCommand @10301; ConfigureAwait @10304; ExecuteReaderAsync @10304; ReadAsync @10306; Add @10308; GetString @10310; GetInt32 @10314; Clear @10320; Add @10321; ExecuteReaderAsync @10333; ReadAsync @10335; Add @10337; GetString @10339; IsDBNull @10343; GetInt32 @10347; Clear @10353; Add @10354; DispatchToUi @10359; SafeError @10359 | FROM bins @10326; FROM facilities @10303; JOIN facilities @10326 |
| <span id="m-9d32305c4f43"></span><code>MainViewModel.LoadCatalogRegistryAsync(string?,string?,string?,string?)</code><br>10576–10680 | CreateCommand @10586; ConfigureAwait @10593; ExecuteReaderAsync @10593; ReadAsync @10594; Add @10596; ParseGuidSafe @10598; GetString @10598; IsDBNull @10601; GetInt32 @10602; Add @10622; DispatchToUi @10637; Clear @10639; Clear @10640; Clear @10641; Equals @10645; Add @10646; Add @10648; Add @10650; Clear @10652; Add @10653; FirstOrDefault @10656; Equals @10656; FirstOrDefault @10661; FirstOrDefault @10668; ApplySaleUnitDefaultsToCatalog @10673; SafeError @10678 | FROM product_categories @10588; FROM uoms @10614 |
| <span id="m-f63d658ad8d5"></span><code>MainViewModel.ApplySaleUnitDefaultsToCatalog()</code><br>10682–10696 | ResolveProductSaleUnitFactor @10686; Round @10692; ApplyFilter @10695 | No extracted literal effects. |
| <span id="m-9218ca00f00f"></span><code>MainViewModel.ResolveProductSaleUnitFactor(ProductItem)</code><br>10698–10716 | FirstOrDefault @10700; Equals @10701; TryParse @10708 | No extracted literal effects. |
| <span id="m-a7ec1dfcb1a9"></span><code>MainViewModel.OpenCategoryManagerAsync()</code><br>10718–10740 | CheckSessionUnlocked @10720; HasPermission @10721; ConfigureAwait @10736; LoadManagedCategoriesAsync @10736; CaptureCategoryFormSnapshot @10738; RaisePropertyChanged @10739; nameof @10739 | No extracted literal effects. |
| <span id="m-e59061b1f5ea"></span><code>MainViewModel.CloseCategoryManager()</code><br>10742–10751 | — | No extracted literal effects. |
| <span id="m-a475aaaa07cf"></span><code>MainViewModel.OpenUnitManagerAsync()</code><br>10753–10775 | CheckSessionUnlocked @10755; HasPermission @10756; ConfigureAwait @10771; LoadManagedUnitsAsync @10771; CaptureUnitFormSnapshot @10773; RaisePropertyChanged @10774; nameof @10774 | No extracted literal effects. |
| <span id="m-f4141541ba24"></span><code>MainViewModel.CloseUnitManager()</code><br>10777–10786 | — | No extracted literal effects. |
| <span id="m-a6bf597a2af2"></span><code>MainViewModel.LoadManagedCategoriesAsync()</code><br>10788–10851 | Clear @10791; Clear @10792; Clear @10793; CreateCommand @10794; ConfigureAwait @10800; ExecuteReaderAsync @10800; ReadAsync @10801; Add @10803; ParseGuidSafe @10805; GetString @10805; IsDBNull @10808; GetInt32 @10809; Where @10817; Equals @10817; Add @10818; TryParse @10831; Add @10832; RefreshTargetedCategoryCollections @10845; DispatchToUi @10846; RefreshManagedCategoriesTable @10848; RefreshManagedExpenseCategoriesTable @10849 | FROM expense_categories @10822; FROM product_categories @10796; JOIN expense_records @10822 |
| <span id="m-00ff610cb064"></span><code>MainViewModel.OpenEditCategoryFromTableAsync(ProductCategoryOption)</code><br>10853–10860 | OpenCategoryManagerAsync @10855; FirstOrDefault @10856; EditManagedCategory @10859 | No extracted literal effects. |
| <span id="m-0e34dedc845a"></span><code>MainViewModel.OpenEditExpenseCategoryFromTableAsync(ExpenseCategoryOption)</code><br>10862–10870 | OpenCategoryManagerAsync @10865; FirstOrDefault @10866; EditManagedExpenseCategory @10869 | No extracted literal effects. |
| <span id="m-23982be02e9c"></span><code>MainViewModel.RefreshTargetedCategoryCollections()</code><br>10872–10891 | DispatchToUi @10874; Clear @10876; Clear @10877; Clear @10878; Where @10880; Equals @10883; Add @10884; Add @10886; Add @10888 | No extracted literal effects. |
| <span id="m-6d93f075b554"></span><code>MainViewModel.EditManagedCategory(ProductCategoryOption)</code><br>10893–10905 | CaptureCategoryFormSnapshot @10903; RaisePropertyChanged @10904; nameof @10904 | No extracted literal effects. |
| <span id="m-ff2146a7e440"></span><code>MainViewModel.EditManagedExpenseCategory(ExpenseCategoryOption)</code><br>10907–10920 | CaptureCategoryFormSnapshot @10918; RaisePropertyChanged @10919; nameof @10919 | No extracted literal effects. |
| <span id="m-5a89025e6ec9"></span><code>MainViewModel.CaptureCategoryFormSnapshot()</code><br>10922–10932 | Serialize @10922 | No extracted literal effects. |
| <span id="m-922672040430"></span><code>MainViewModel.CaptureUnitFormSnapshot()</code><br>10934–10944 | Serialize @10934 | No extracted literal effects. |
| <span id="m-4e873ed7f50b"></span><code>MainViewModel.KeepEditingRegistryForm()</code><br>10946–10946 | — | No extracted literal effects. |
| <span id="m-ea93b5637fe8"></span><code>MainViewModel.DiscardRegistryForm()</code><br>10948–10964 | Equals @10951; RaisePropertyChanged @10955; nameof @10955 | No extracted literal effects. |
| <span id="m-9a588bced628"></span><code>MainViewModel.SaveManagedCategoryAsync()</code><br>10966–11093 | Equals @10977; HasPermission @10979; FirstOrDefault @10988; Trim @10993; Trim @10994; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @10996; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @10996; DispatchToUi @10999; SafePipelineError @10999; IsNullOrWhiteSpace @11007; ConfigureAwait(CreateExpenseCategoryCommand, Guid) @11009; ExecuteAsync(CreateExpenseCategoryCommand, Guid) @11009; ConfigureAwait @11018; LoadManagedCategoriesAsync @11018; LoadExpenseCategoriesAsync @11019; CaptureCategoryFormSnapshot @11029; RaisePropertyChanged @11030; nameof @11030; Trim @11048; ConfigureAwait(UpdateCategoryCommand, ProductCategoryDto) @11050; ExecuteAsync(UpdateCategoryCommand, ProductCategoryDto) @11050; ConfigureAwait(CreateCategoryCommand, ProductCategoryDto) @11066; ExecuteAsync(CreateCategoryCommand, ProductCategoryDto) @11066; LoadCatalogRegistryAsync @11075; ReloadCatalogAsync @11076; SafeError @11091 | No extracted literal effects. |
| <span id="m-3c04ac2bec2d"></span><code>MainViewModel.ToggleManagedCategoryActiveAsync(ProductCategoryOption)</code><br>11095–11140 | HasPermission @11105; ConfigureAwait(DeactivateCategoryCommand, bool) @11118; ExecuteAsync(DeactivateCategoryCommand, bool) @11118; ConfigureAwait(ReactivateCategoryCommand, bool) @11123; ExecuteAsync(ReactivateCategoryCommand, bool) @11123; DispatchToUi @11128; SafePipelineError @11128; ConfigureAwait @11132; LoadManagedCategoriesAsync @11132; LoadCatalogRegistryAsync @11133; ReloadCatalogAsync @11134; SafeError @11138 | No extracted literal effects. |
| <span id="m-ac7b92c9edcf"></span><code>MainViewModel.ToggleManagedExpenseCategoryActiveAsync(ExpenseCategoryOption)</code><br>11142–11182 | HasPermission @11152; ConfigureAwait(UpdateExpenseCategoryCommand, bool) @11168; ExecuteAsync(UpdateExpenseCategoryCommand, bool) @11168; DispatchToUi @11171; SafePipelineError @11171; ConfigureAwait @11175; LoadManagedCategoriesAsync @11175; LoadExpenseCategoriesAsync @11176; SafeError @11180 | No extracted literal effects. |
| <span id="m-9ad8e4fb85d7"></span><code>MainViewModel.LoadManagedUnitsAsync()</code><br>11184–11284 | Clear @11187; CreateCommand @11190; ConfigureAwait @11196; ExecuteReaderAsync @11196; ReadAsync @11197; Add @11199; GetString @11201; IsDBNull @11203; GetInt32 @11207; IsNullOrWhiteSpace @11218; Equals @11222; Add @11229; Clear @11233; ExecuteReaderAsync @11238; ReadAsync @11239; GetString @11241; Where @11263; Add @11265; TryGetValue @11268; FirstOrDefault @11275; Add @11279; DispatchToUi @11282; UpdateConversionPreview @11283 | FROM store_uom_preferences @11237; FROM uoms @11192 |
| <span id="m-54fca161e16d"></span><code>MainViewModel.OpenEditUnitFromTableAsync(UomOption)</code><br>11286–11293 | OpenUnitManagerAsync @11288; FirstOrDefault @11289; Equals @11289; EditManagedUnit @11292 | No extracted literal effects. |
| <span id="m-6c38353cdbed"></span><code>MainViewModel.UpdateConversionPreview()</code><br>11295–11331 | IsNullOrWhiteSpace @11297; FirstOrDefault @11303; Equals @11303; TryParse @11318 | No extracted literal effects. |
| <span id="m-bf187e33bdf5"></span><code>MainViewModel.SaveStoreUomPreferenceAsync(StoreUomPreferenceItem?)</code><br>11333–11354 | ConfigureAwait(UpdateStoreUomPreferenceCommand, bool) @11340; ExecuteAsync(UpdateStoreUomPreferenceCommand, bool) @11340; DispatchToUi @11343; SafePipelineError @11347; SafeError @11352 | No extracted literal effects. |
| <span id="m-c97200f71470"></span><code>MainViewModel.EditManagedUnit(UomOption)</code><br>11356–11369 | IsNullOrWhiteSpace @11362; TryParse @11365; CaptureUnitFormSnapshot @11367; RaisePropertyChanged @11368; nameof @11368 | No extracted literal effects. |
| <span id="m-e272b8859711"></span><code>MainViewModel.SaveManagedUnitAsync()</code><br>11371–11433 | IsNullOrWhiteSpace @11383; Trim @11387; Trim @11388; Trim @11391; ConfigureAwait(UpdateUomCommand, UomDefinitionDto) @11392; ExecuteAsync(UpdateUomCommand, UomDefinitionDto) @11392; DispatchToUi @11395; SafePipelineError @11395; Trim @11402; Equals @11405; ConfigureAwait(CreateUomCommand, UomDefinitionDto) @11410; ExecuteAsync(CreateUomCommand, UomDefinitionDto) @11410; ConfigureAwait @11418; LoadManagedUnitsAsync @11418; LoadCatalogRegistryAsync @11419; CaptureUnitFormSnapshot @11426; RaisePropertyChanged @11427; nameof @11427; SafeError @11431 | No extracted literal effects. |
| <span id="m-b0628b633ef5"></span><code>MainViewModel.ToggleManagedUnitActiveAsync(UomOption)</code><br>11435–11473 | ConfigureAwait(DeactivateUomCommand, bool) @11452; ExecuteAsync(DeactivateUomCommand, bool) @11452; ConfigureAwait(ReactivateUomCommand, bool) @11457; ExecuteAsync(ReactivateUomCommand, bool) @11457; DispatchToUi @11462; SafePipelineError @11462; ConfigureAwait @11466; LoadManagedUnitsAsync @11466; LoadCatalogRegistryAsync @11467; SafeError @11471 | No extracted literal effects. |
| <span id="m-553a110d7ed9"></span><code>MainViewModel.LoadItemLocationEligibilitiesAsync(Guid)</code><br>11475–11513 | CreateCommand @11480; CreateParameter @11487; ToString @11489; Add @11490; ConfigureAwait @11492; ExecuteReaderAsync @11492; Clear @11493; ReadAsync @11494; Add @11496; ParseGuidSafe @11498; GetString @11498; GetInt32 @11501; IsDBNull @11503; ToDecimal @11503; GetDouble @11503; DispatchToUi @11511; SafeError @11511 | FROM item_locations @11481 |
| <span id="m-fc954b84ba1c"></span><code>MainViewModel.OpenLocationsModal()</code><br>11516–11542 | CheckSessionUnlocked @11518; HasPermission @11519; LoadFacilitiesAndBinsAsync @11540 | No extracted literal effects. |
| <span id="m-19f9ee9165ff"></span><code>MainViewModel.OpenAddFacility()</code><br>11544–11552 | — | No extracted literal effects. |
| <span id="m-bf3945e32b32"></span><code>MainViewModel.OpenEditFacility(FacilityItem?)</code><br>11554–11563 | — | No extracted literal effects. |
| <span id="m-9aa4ca3aa673"></span><code>MainViewModel.ConfirmSaveFacilityAsync()</code><br>11565–11624 | HasPermission @11568; IsNullOrWhiteSpace @11573; IsNullOrEmpty @11589; Trim @11591; Trim @11591; ConfigureAwait(UpdateFacilityCommand, FacilityDto) @11592; ExecuteAsync(UpdateFacilityCommand, FacilityDto) @11592; OpenAddFacility @11596; ConfigureAwait @11597; LoadFacilitiesAndBinsAsync @11597; DispatchToUi @11601; SafePipelineError @11601; ConfigureAwait(CreateFacilityCommand, FacilityDto) @11607; ExecuteAsync(CreateFacilityCommand, FacilityDto) @11607; SafeError @11622 | No extracted literal effects. |
| <span id="m-e09e1d82c730"></span><code>MainViewModel.DeactivateFacilityAsync(FacilityItem?)</code><br>11626–11657 | HasPermission @11629; ConfigureAwait(DeactivateFacilityCommand, bool) @11641; ExecuteAsync(DeactivateFacilityCommand, bool) @11641; OpenAddFacility @11645; ConfigureAwait @11646; LoadFacilitiesAndBinsAsync @11646; DispatchToUi @11650; SafePipelineError @11650; SafeError @11655 | No extracted literal effects. |
| <span id="m-758e30c2039d"></span><code>MainViewModel.OpenAddBin()</code><br>11659–11670 | FirstOrDefault @11669 | No extracted literal effects. |
| <span id="m-e4ad2997ab68"></span><code>MainViewModel.OpenEditBin(BinLocationItem?)</code><br>11672–11684 | FirstOrDefault @11682 | No extracted literal effects. |
| <span id="m-d7360ee4860d"></span><code>MainViewModel.ConfirmSaveBinAsync()</code><br>11686–11761 | HasPermission @11689; IsNullOrWhiteSpace @11699; IsNullOrEmpty @11710; Trim @11715; Trim @11716; Trim @11717; Trim @11718; Trim @11719; ConfigureAwait(UpdateLocationBinCommand, BinLocationDto) @11722; ExecuteAsync(UpdateLocationBinCommand, BinLocationDto) @11722; OpenAddBin @11726; ConfigureAwait @11727; LoadFacilitiesAndBinsAsync @11727; DispatchToUi @11731; SafePipelineError @11731; ConfigureAwait(CreateLocationBinCommand, BinLocationDto) @11744; ExecuteAsync(CreateLocationBinCommand, BinLocationDto) @11744; SafeError @11759 | No extracted literal effects. |
| <span id="m-7108b24317bc"></span><code>MainViewModel.DeactivateBinAsync(BinLocationItem?)</code><br>11763–11794 | HasPermission @11766; ConfigureAwait(DeactivateLocationBinCommand, bool) @11778; ExecuteAsync(DeactivateLocationBinCommand, bool) @11778; OpenAddBin @11782; ConfigureAwait @11783; LoadFacilitiesAndBinsAsync @11783; DispatchToUi @11787; SafePipelineError @11787; SafeError @11792 | No extracted literal effects. |
| <span id="m-2439faeeff8c"></span><code>MainViewModel.SaveItemLocationEligibilityAsync()</code><br>11796–11849 | HasPermission @11804; IsNullOrWhiteSpace @11809; Trim @11821; ConfigureAwait(SetItemLocationEligibilityCommand, ItemLocationDto) @11829; ExecuteAsync(SetItemLocationEligibilityCommand, ItemLocationDto) @11829; ConfigureAwait @11837; LoadItemLocationEligibilitiesAsync @11837; DispatchToUi @11842; SafePipelineError @11842; SafeError @11847 | No extracted literal effects. |
| <span id="m-0a34a28dc320"></span><code>MainViewModel.RemoveItemLocationEligibilityAsync(ItemLocationEligibilityItem?)</code><br>11851–11881 | HasPermission @11854; ConfigureAwait(RemoveItemLocationEligibilityCommand, bool) @11866; ExecuteAsync(RemoveItemLocationEligibilityCommand, bool) @11866; ConfigureAwait @11869; LoadItemLocationEligibilitiesAsync @11869; DispatchToUi @11874; SafePipelineError @11874; SafeError @11879 | No extracted literal effects. |
| <span id="m-432c261b70e2"></span><code>MainViewModel.LoadCustomersAsync()</code><br>11884–11917 | NewGuid @11892; Clear @11898; Add @11899; FilterCustomers @11901; ConfigureAwait @11908; GetCustomersAsync @11908; DispatchToUi @11915; SafeError @11915 | No extracted literal effects. |
| <span id="m-42691e98e722"></span><code>MainViewModel.FilterCustomers()</code><br>11919–11932 | Clear @11921; Trim @11922; IsNullOrWhiteSpace @11923; Where @11925; Contains @11925; Contains @11926; Contains @11927; Add @11930 | No extracted literal effects. |
| <span id="m-b84f75b2a0bf"></span><code>MainViewModel.OpenLotSerialPickerAsync(OrderItem)</code><br>11934–11970 | CheckSessionUnlocked @11936; CreateCommand @11945; CreateParameter @11948; ToString @11950; Add @11951; ConfigureAwait @11952; ExecuteScalarAsync @11952; ToString @11953; Equals @11956; LoadPickerCandidatesAsync @11968; DispatchToUi @11969 | FROM items @11947 |
| <span id="m-9fc03d89661b"></span><code>MainViewModel.LoadPickerCandidatesAsync()</code><br>11972–12033 | ConfigureAwait @11979; GetLotCandidatesAsync @11979; DispatchToUi @11982; Clear @11984; Add @11987; ToString @11996; GetSerialCandidatesAsync @12004; Clear @12009; Add @12012; ToString @12021 | No extracted literal effects. |
| <span id="m-7523ee7a282a"></span><code>MainViewModel.CloseLotSerialPicker()</code><br>12035–12041 | Clear @12038; Clear @12039 | No extracted literal effects. |
| <span id="m-6a4f71f878c5"></span><code>MainViewModel.ConfirmLotSerialSelectionAsync()</code><br>12043–12102 | FirstOrDefault @12056; ConfigureAwait(SelectLotForCartLineCommand, bool) @12064; ExecuteAsync(SelectLotForCartLineCommand, bool) @12064; DispatchToUi @12067; SafePipelineError @12067; ToList @12073; Where @12073; ConfigureAwait(SelectSerialForCartLineCommand, bool) @12083; ExecuteAsync(SelectSerialForCartLineCommand, bool) @12083; SafeError @12100 | No extracted literal effects. |
| <span id="m-ee0dcfecb822"></span><code>MainViewModel.OpenCustomerChooser()</code><br>12104–12112 | CheckSessionUnlocked @12106; Clear @12109; LoadCustomersAsync @12110 | No extracted literal effects. |
| <span id="m-a74090c7a249"></span><code>MainViewModel.CloseCustomerChooser()</code><br>12114–12117 | — | No extracted literal effects. |
| <span id="m-d87eacd7bfed"></span><code>MainViewModel.SelectCustomer(CustomerDto?,string?)</code><br>12119–12136 | SaveDurableCartAsync @12129; IsNullOrWhiteSpace @12133; ToString @12133; NewGuid @12133; RecordSuccessfulSearchUseAsync @12134; FromGuid @12134 | No extracted literal effects. |
| <span id="m-c4744e1ce7a4"></span><code>MainViewModel.SelectWalkInCustomer()</code><br>12138–12147 | SaveDurableCartAsync @12146 | No extracted literal effects. |
| <span id="m-c4e40b32709b"></span><code>MainViewModel.DeactivateCustomerAsync(CustomerDto?)</code><br>12149–12194 | CheckSessionUnlocked @12151; IndexOf @12155; SelectWalkInCustomer @12161; FilterCustomers @12163; ConfigureAwait(DeactivateCustomerCommand, bool) @12175; ExecuteAsync(DeactivateCustomerCommand, bool) @12175; ConfigureAwait @12182; LoadCustomersAsync @12182; DispatchToUi @12187; SafePipelineError @12187; SafeError @12192 | No extracted literal effects. |
| <span id="m-bc49c5f6c21a"></span><code>MainViewModel.LoadManufacturingDataAsync()</code><br>12323–12362 | Add @12329; NewGuid @12330; RefreshManufacturingTablesAsync @12344; ConfigureAwait @12352; GetKitsAsync @12352; Clear @12353; Add @12354; DispatchToUi @12360; SafeError @12360 | No extracted literal effects. |
| <span id="m-5e227259836f"></span><code>MainViewModel.OpenProductionModal(BomDto?)</code><br>12366–12382 | CheckSessionUnlocked @12368; SetProductionActionMode @12370; FirstOrDefault @12375; LoadProductionIngredientLotsAsync @12380; TakeProductionSnapshot @12381 | No extracted literal effects. |
| <span id="m-b4c58a1839f8"></span><code>MainViewModel.CloseProductionModal()</code><br>12384–12398 | — | No extracted literal effects. |
| <span id="m-01e78cd250eb"></span><code>MainViewModel.ExecuteProductionRunFromUiAsync()</code><br>12400–12499 | ExecuteExistingProductionAsync @12403; Resolve @12425; NewGuid @12428; ToUpperInvariant @12430; ToString @12430; Insert @12448; IsNullOrWhiteSpace @12470; Trim @12470; ToDictionary @12472; Where @12472; ConfigureAwait(ExecuteProductionRunCommand, ProductionRunDto) @12476; ExecuteAsync(ExecuteProductionRunCommand, ProductionRunDto) @12476; DispatchToUi @12479; SafePipelineError @12479; RecordSuccessfulSearchUseAsync @12486; FromGuid @12486; ConfigureAwait @12489; LoadManufacturingDataAsync @12489; LoadInventoryAsync @12490; SafeError @12496 | No extracted literal effects. |
| <span id="m-542bd824fd48"></span><code>MainViewModel.CloseXReportModal()</code><br>12598–12601 | — | No extracted literal effects. |
| <span id="m-b4dd047e25dd"></span><code>MainViewModel.OpenCloseShiftModal()</code><br>12603–12633 | CheckSessionUnlocked @12605; Clear @12623; Where @12624; GetUnlockCandidates @12624; Equals @12625; Add @12629 | No extracted literal effects. |
| <span id="m-8fe76360f646"></span><code>MainViewModel.CloseCloseShiftModal()</code><br>12635–12639 | — | No extracted literal effects. |
| <span id="m-9ff50b8d85d3"></span><code>MainViewModel.CloseZReportModal()</code><br>12641–12644 | — | No extracted literal effects. |
| <span id="m-cb1bd5eac106"></span><code>MainViewModel.LoadReportDataAsync()</code><br>12646–12763 | ToString @12666; DispatchToUi @12682; ConfigureAwait @12710; ExecuteAsync @12710; Join @12712; Select(string, Money) @12712; InvoiceMoney @12712; ToDecimal @12715; ToDecimal @12716; ToDecimal @12717; ToDecimal @12718; ToDecimal @12720; ToDecimal @12722; ToDecimal @12723; ToDecimal @12724; ToDecimal @12725; ToDecimal @12726; ToUpperInvariant @12728; ToString @12728; ToString @12730; ToString @12731; Sum @12737; ToDecimal @12737; ToDecimal @12740; Add @12742; Format @12747; SafeError @12755 | No extracted literal effects. |
| <span id="m-2672c77ef222"></span><code>MainViewModel.ConfirmCloseShiftAsync()</code><br>12765–12854 | CheckSessionUnlocked @12768; IsNullOrWhiteSpace @12785; AuthenticateSelectedUser @12793; Trim @12795; Round @12804; Trim @12808; ConfigureAwait(CloseShiftCommand, Shift) @12812; ExecuteAsync(CloseShiftCommand, Shift) @12812; DispatchToUi @12830; SafePipelineError @12830; ConfigureAwait @12837; ExecuteAsync @12837; SetActiveCashier @12841; RefreshUnlockCandidates @12842; RaisePropertyChanged @12843; nameof @12843; LoadReportDataAsync @12847; LoadTeamsStaffAsync @12848; SafeError @12852 | No extracted literal effects. |
| <span id="m-1217ba352fa5"></span><code>MainViewModel.GetOrLoadProductById(Guid)</code><br>12856–12931 | FirstOrDefault @12858; CreateCommand @12865; CreateParameter @12880; ToString @12882; Add @12883; ExecuteReader @12885; Read @12886; Parse @12888; GetString @12888; GetInt64 @12891; Pow @12893; IsDBNull @12895; TryParse @12901; GetInt32 @12902; Add @12924 | FROM barcodes @12866; FROM items @12866; JOIN barcodes @12866; JOIN product_categories @12866 |
| <span id="m-4552b8e998bc"></span><code>MainViewModel.TryAddUniqueExactMatchToCart(string)</code><br>12933–13048 | IsNullOrWhiteSpace @12935; Trim @12938; ToList @12941; Where @12941; IsNullOrEmpty @12942; Equals @12942; ToString @12944; AddToCart @12950; CreateCommand @12966; CreateParameter @12984; Add @12987; ExecuteReader @12989; Read @12991; Parse @12993; GetString @12993; ContainsKey @12994; GetInt64 @12998; Pow @13000; IsDBNull @13002; TryParse @13008; GetInt32 @13009; First @13037; Add @13038 | FROM barcodes @12967; FROM items @12967; JOIN barcodes @12967; JOIN product_categories @12967 |
| <span id="m-163806d1a9b3"></span><code>MainViewModel.HandleBarcodeScanned(string)</code><br>13050–13093 | IsNullOrWhiteSpace @13052; Trim @13055; AppendReceiveSerialScan @13061; TryAddUniqueExactMatchToCart @13067; Clear @13069; ToList @13074; Where @13074; Equals @13074; AddToCart @13077 | No extracted literal effects. |

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
