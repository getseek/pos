---
id: PP-REVIEW-CODE-UI.COMPONENTS
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# GetSeek.UI.Components source catalogue

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.UI.Components.csproj:1](code-ui.components.md#src-6da00d4f185c). Dependencies: none declared.

## BatchConfirmationControl.axaml.cs {#src-9c54ebd365b6}

<code>Software/src/GetSeek.UI.Components/Controls/BatchConfirmationControl.axaml.cs</code> · 49 lines.

SHA-256: <code>bf69cb91253b0e5fdee4af005562ae0dfa8f013cc0d208601dca0566e53f5f76</code>.

Declarations: <code>BatchConfirmationControl : UserControl</code> (line 7).

## CompactDateField.axaml.cs {#src-fc74d2e419b3}

<code>Software/src/GetSeek.UI.Components/Controls/CompactDateField.axaml.cs</code> · 539 lines.

SHA-256: <code>6ffca96cd057cf5cf80e6a7beb206d29bbad9c4fb1e97086349a127de2a4422a</code>.

Declarations: <code>CompactDateField : UserControl</code> (line 13), <code>SimpleRelayCommand : ICommand</code> (line 533).

<details markdown>
<summary>Methods, calls, table effects and failures (22)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f15417c2f783"></span><code>CompactDateField.OnTextBoxPointerPressed(object?,PointerPressedEventArgs)</code><br>208–221 | FindControl(Button) @211; IsVisualChildOf @212 | No extracted literal effects. |
| <span id="m-00a8db97635f"></span><code>CompactDateField.IsVisualChildOf(Visual,Visual)</code><br>223–232 | ReferenceEquals @228; GetVisualParent @229 | No extracted literal effects. |
| <span id="m-6cf280c808b4"></span><code>CompactDateField.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>234–269 | OnPropertyChanged @236; OnValueChanged @240; GetNewValue(DateOnly?) @240; OnSelectedDateTimeChanged @244; GetNewValue(DateTime?) @244; OnSelectedDateTimeOffsetChanged @248; GetNewValue(DateTimeOffset?) @248; OnSelectedIsoTextChanged @252; GetNewValue(string?) @252; OnRangeChanged @256; GetNewValue(bool) @260; Add @262; Remove @266 | No extracted literal effects. |
| <span id="m-3d1a64c3db85"></span><code>CompactDateField.OnValueChanged(DateOnly?)</code><br>271–283 | UpdateDerivedValues @277 | No extracted literal effects. |
| <span id="m-35b4ec799396"></span><code>CompactDateField.OnSelectedDateTimeChanged(DateTime?)</code><br>285–299 | FromDateTime @291; UpdateDerivedValues @293 | No extracted literal effects. |
| <span id="m-6b05cb508075"></span><code>CompactDateField.OnSelectedDateTimeOffsetChanged(DateTimeOffset?)</code><br>301–315 | FromDateTime @307; UpdateDerivedValues @309 | No extracted literal effects. |
| <span id="m-2c2d59891d01"></span><code>CompactDateField.OnSelectedIsoTextChanged(string?)</code><br>317–335 | IsNullOrWhiteSpace @324; TryParseExact @324; Trim @324; UpdateDerivedValues @329 | No extracted literal effects. |
| <span id="m-5594de15fe25"></span><code>CompactDateField.UpdateDerivedValues(DateOnly?)</code><br>337–346 | ToDateTime @339; ToString @341; ToString @343 | No extracted literal effects. |
| <span id="m-49fb66596214"></span><code>CompactDateField.OnRangeChanged()</code><br>348–352 | ToDateTime @350; ToDateTime @351 | No extracted literal effects. |
| <span id="m-79993802731a"></span><code>CompactDateField.ToggleDropDown()</code><br>354–358 | — | No extracted literal effects. |
| <span id="m-e545d8622d5b"></span><code>CompactDateField.ClearDate()</code><br>360–366 | FocusTextBox @365 | No extracted literal effects. |
| <span id="m-125de55253f2"></span><code>CompactDateField.SetToday()</code><br>368–377 | FromDateTime @370; FocusTextBox @376 | No extracted literal effects. |
| <span id="m-f74524871937"></span><code>CompactDateField.OnCalendarSelectedDatesChanged(object?,SelectionChangedEventArgs)</code><br>379–389 | FromDateTime @384; FocusTextBox @387 | No extracted literal effects. |
| <span id="m-fccac1e5bd88"></span><code>CompactDateField.OnTextBoxLostFocus(object?,RoutedEventArgs)</code><br>391–394 | CommitText @393 | No extracted literal effects. |
| <span id="m-888b09b4b381"></span><code>CompactDateField.OnTextBoxKeyDown(object?,KeyEventArgs)</code><br>396–403 | CommitText @400 | No extracted literal effects. |
| <span id="m-c654afd1d85a"></span><code>CompactDateField.OnControlKeyDown(object?,KeyEventArgs)</code><br>405–413 | FocusTextBox @411 | No extracted literal effects. |
| <span id="m-5823d27280b5"></span><code>CompactDateField.FocusTextBox()</code><br>415–419 | FindControl(TextBox) @417; Focus @418 | No extracted literal effects. |
| <span id="m-5943c21f1105"></span><code>CompactDateField.CommitText()</code><br>421–464 | Trim @423; IsNullOrWhiteSpace @424; ToString @433; Equals @443; ToString @443; TryParseDate @453; ToString @456 | No extracted literal effects. |
| <span id="m-e4de81f7d60f"></span><code>CompactDateField.TryParseDate(string,DateOnly?,DateOnly?,DateOnly)</code><br>466–467 | TryParseDate @467 | No extracted literal effects. |
| <span id="m-c62d6420af7c"></span><code>CompactDateField.TryParseDate(string,DateOnly?,DateOnly?,DateOnly?,DateOnly)</code><br>469–531 | IsNullOrWhiteSpace @472; Replace @474; Trim @474; TryParseExact @480; EndsWith @484 | No extracted literal effects. |
| <span id="m-cba3b16c3095"></span><code>SimpleRelayCommand.CanExecute(object?)</code><br>536–536 | — | No extracted literal effects. |
| <span id="m-4f6096a239bc"></span><code>SimpleRelayCommand.Execute(object?)</code><br>537–537 | execute @537 | No extracted literal effects. |

</details>

## DataTableContracts.cs {#src-61f9fc3ef974}

<code>Software/src/GetSeek.UI.Components/Controls/DataTableContracts.cs</code> · 133 lines.

SHA-256: <code>ae22600bad719e26cfee924021d86d732cb0a16a305f640b3a3901b018149656</code>.

Declarations: <code>IDataTableState : INotifyPropertyChanged</code> (line 11), <code>DataTableCellStyle</code> (line 33), <code>DataTableColumnDescriptor</code> (line 46), <code>DataTableActionDescriptor</code> (line 69), <code>DataTableToolbarActionDescriptor</code> (line 78), <code>DataTableToolbarControlDescriptor</code> (line 91), <code>DataTableDefinition</code> (line 99).

<details markdown>
<summary>Methods, calls, table effects and failures (9)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-a82c02346adf"></span><code>IDataTableState.GetSelectedIdsForPreview()</code><br>22–22 | — | No extracted literal effects. |
| <span id="m-e7ae9101939b"></span><code>IDataTableState.IsRowSelected(string)</code><br>23–23 | — | No extracted literal effects. |
| <span id="m-5fb406a0400a"></span><code>IDataTableState.SelectRow(string,bool)</code><br>24–24 | — | No extracted literal effects. |
| <span id="m-d69498485017"></span><code>IDataTableState.SelectPage(IEnumerable&lt;string&gt;)</code><br>25–25 | — | No extracted literal effects. |
| <span id="m-167da8daeb45"></span><code>IDataTableState.SetPageSelection(IEnumerable&lt;string&gt;,bool)</code><br>26–26 | — | No extracted literal effects. |
| <span id="m-09418422b254"></span><code>IDataTableState.ClearSelection()</code><br>27–27 | — | No extracted literal effects. |
| <span id="m-1b7c14812a9c"></span><code>IDataTableState.NextPage()</code><br>28–28 | — | No extracted literal effects. |
| <span id="m-d7a00355e3e4"></span><code>IDataTableState.PreviousPage()</code><br>29–29 | — | No extracted literal effects. |
| <span id="m-77dc3019c844"></span><code>IDataTableState.ToggleSort(string)</code><br>30–30 | — | No extracted literal effects. |

</details>

## DataTableSelectionToolbar.cs {#src-44d903844eb9}

<code>Software/src/GetSeek.UI.Components/Controls/DataTableSelectionToolbar.cs</code> · 142 lines.

SHA-256: <code>5a3b05d8bbd05626b40c2cf648295ec0f5c8f25ff12e31977fd32b0c827c0015</code>.

Declarations: <code>DataTableSelectionToolbar : StackPanel</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (4)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f7b920db2714"></span><code>DataTableSelectionToolbar.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>36–58 | OnPropertyChanged @38; GetNewValue(DataTableDefinition?) @49; Rebuild @57 | No extracted literal effects. |
| <span id="m-089476e63ec1"></span><code>DataTableSelectionToolbar.OnStateChanged(object?,PropertyChangedEventArgs)</code><br>60–60 | Rebuild @60 | No extracted literal effects. |
| <span id="m-981670dfb88d"></span><code>DataTableSelectionToolbar.OnRowsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>61–61 | Rebuild @61 | No extracted literal effects. |
| <span id="m-dc38e688a1e5"></span><code>DataTableSelectionToolbar.Rebuild()</code><br>63–141 | Clear @65; ToArray @73; Count @74; IsRowSelected @74; RowIdSelector @74; Invoke @79; Add @82; ClearSelection @103; AddRange @113; Select @113; Invoke @134 | No extracted literal effects. |

</details>

## DataTableWorkspaceFrame.axaml.cs {#src-781f2631af75}

<code>Software/src/GetSeek.UI.Components/Controls/DataTableWorkspaceFrame.axaml.cs</code> · 126 lines.

SHA-256: <code>48a8eef16d1b7eaedb0cff6f9661eb6c8f28cb7bf11734d69eabcf3df3290f54</code>.

Declarations: <code>DataTableWorkspaceFrame : UserControl</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-c44e528466f2"></span><code>DataTableWorkspaceFrame.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>87–122 | OnPropertyChanged @89; GetNewValue(DataTableDefinition?) @92; GetNewValue(Control?) @96; UpdateToolbarVisibility @97; GetNewValue(bool) @111 | No extracted literal effects. |
| <span id="m-5f7a5fef89ad"></span><code>DataTableWorkspaceFrame.UpdateToolbarVisibility()</code><br>124–125 | — | No extracted literal effects. |

</details>

## ModalActionBar.cs {#src-f2d9570ce556}

<code>Software/src/GetSeek.UI.Components/Controls/ModalActionBar.cs</code> · 143 lines.

SHA-256: <code>62e2280b2565eaabb58a16408c186a39956c1e66f362ea2d06362627438a2643</code>.

Declarations: <code>ModalActionBar : Panel</code> (line 12), <code>ActionRow</code> (line 142).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5e96c23d4ff5"></span><code>ModalActionBar.MeasureOverride(Size)</code><br>25–118 | IsFinite @27; Max @27; ToArray @30; Where @30; Measure @41; Max @44; Floor @48; Min @52; Add @64; Repeat @66; Measure @86; ToArray @90; ToArray @90; FinishRow @105; Add @107; Add @108 | No extracted literal effects. |
| <span id="m-b3fe2e17e127"></span><code>ModalActionBar.ArrangeOverride(Size)</code><br>120–140 | IsFinite @122; Max @122; Arrange @132 | No extracted literal effects. |

</details>

## ModalLayers.cs {#src-f9ded22b3dcb}

<code>Software/src/GetSeek.UI.Components/Controls/ModalLayers.cs</code> · 76 lines.

SHA-256: <code>9afee3536492e24813661038348f8e115a226e267112777cb7e278c3cdf51142</code>.

Declarations: <code>ModalLayers</code> (line 4).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d65cf3eb276d"></span><code>ModalLayers.IsSurfaceState(string?)</code><br>10–10 | Contains @10 | No extracted literal effects. |

</details>

## ModalShell.axaml.cs {#src-b4641452c5a4}

<code>Software/src/GetSeek.UI.Components/Controls/ModalShell.axaml.cs</code> · 243 lines.

SHA-256: <code>212f999b041591449a9695d33d2ae6bea07c9c16af7f2bc5f17582cd58743234</code>.

Declarations: <code>ModalShell : UserControl</code> (line 17).

<details markdown>
<summary>Methods, calls, table effects and failures (10)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f44f23b4dbea"></span><code>ModalShell.UpdateSaveButton()</code><br>117–121 | — | No extracted literal effects. |
| <span id="m-d7ec885460b2"></span><code>ModalShell.UpdateSecondaryActionButton()</code><br>123–147 | Contains @130; IndexOf @132; Insert @135; Add @139; Remove @145 | No extracted literal effects. |
| <span id="m-1dc7215b06bd"></span><code>ModalShell.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>149–179 | OnPropertyChanged @151; GetNewValue(Control?) @153; GetNewValue(ICommand?) @162; UpdateSaveButton @164; UpdateSecondaryActionButton @166; IsNullOrWhiteSpace @168; GetNewValue(string) @168; GetNewValue(bool) @171; GetTopLevel @173; GetFocusedElement @173; Post @174 | No extracted literal effects. |
| <span id="m-d1dba3455191"></span><code>ModalShell.OnScrimPointerPressed(object?,PointerPressedEventArgs)</code><br>181–184 | ReferenceEquals @183; GetPosition @183 | No extracted literal effects. |
| <span id="m-fcb8b25df314"></span><code>ModalShell.OnScrimPointerReleased(object?,PointerReleasedEventArgs)</code><br>186–196 | ReferenceEquals @190; GetPosition @193; Pow @194; RequestDismiss @195 | No extracted literal effects. |
| <span id="m-5668fa800c87"></span><code>ModalShell.OnKeyDown(object?,KeyEventArgs)</code><br>198–205 | RequestDismiss @203 | No extracted literal effects. |
| <span id="m-7d2a61d1caf6"></span><code>ModalShell.RequestDismiss()</code><br>207–215 | CanExecute @213; Execute @214 | No extracted literal effects. |
| <span id="m-fb95146e93e8"></span><code>ModalShell.FocusFirstEditableControl()</code><br>217–225 | Any(WorkspaceOverlayHost) @222; OfType(WorkspaceOverlayHost) @222; GetVisualAncestors @222; IsEditableTarget @223; FirstOrDefault(Control) @223; OfType(Control) @223; GetVisualDescendants @223; Focus @224 | No extracted literal effects. |
| <span id="m-c78d3f1a2074"></span><code>ModalShell.IsEditableTarget(Control?)</code><br>227–229 | — | No extracted literal effects. |
| <span id="m-0397b9640766"></span><code>ModalShell.RestoreLauncherFocus()</code><br>231–242 | Any(WorkspaceOverlayHost) @233; OfType(WorkspaceOverlayHost) @233; GetVisualAncestors @233; IsEditableTarget @238; Focus @240 | No extracted literal effects. |

</details>

## PageSizeSelector.axaml.cs {#src-11b41ff3d57e}

<code>Software/src/GetSeek.UI.Components/Controls/PageSizeSelector.axaml.cs</code> · 55 lines.

SHA-256: <code>0d49c40f88d2e92f5cabd2e663895bd28120a7c4fca12acdb7e42b5ddda5265a</code>.

Declarations: <code>PageSizeSelector : UserControl</code> (line 6).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-fc34e044806b"></span><code>PageSizeSelector.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>33–40 | OnPropertyChanged @35; UpdateSelection @38 | No extracted literal effects. |
| <span id="m-e606abe0d049"></span><code>PageSizeSelector.UpdateSelection(int)</code><br>42–54 | TryParse @47; ToString @47 | No extracted literal effects. |

</details>

## Pager.axaml.cs {#src-a48b61cc79a5}

<code>Software/src/GetSeek.UI.Components/Controls/Pager.axaml.cs</code> · 58 lines.

SHA-256: <code>e070f1a7cf3e78cc31250f287233c01151313b57291fd2064bbf19bbce0cc5f3</code>.

Declarations: <code>Pager : UserControl</code> (line 7).

## ResponsiveWorkspaceSplit.axaml.cs {#src-9b5645207b64}

<code>Software/src/GetSeek.UI.Components/Controls/ResponsiveWorkspaceSplit.axaml.cs</code> · 224 lines.

SHA-256: <code>2b2a66eb4d1b07610e157f2f695d96e54e90df7306be4bd89cfdb271f92c1316</code>.

Declarations: <code>ResponsiveWorkspaceSplit : UserControl</code> (line 15).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-b143ca5e5e3c"></span><code>ResponsiveWorkspaceSplit.ResolveBreakpoint()</code><br>94–95 | Max @95 | No extracted literal effects. |
| <span id="m-a123b181c7b9"></span><code>ResponsiveWorkspaceSplit.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>97–127 | OnPropertyChanged @99; GetNewValue(Control?) @105; UpdateLayoutMode @123; InvalidateMeasure @124 | No extracted literal effects. |
| <span id="m-5baae67d8462"></span><code>ResponsiveWorkspaceSplit.MeasureOverride(Size)</code><br>129–136 | IsNaN @131; IsInfinity @131; UpdateLayoutMode @133; MeasureOverride @135 | No extracted literal effects. |
| <span id="m-970367480ae7"></span><code>ResponsiveWorkspaceSplit.OnAttachedToVisualTree(VisualTreeAttachmentEventArgs)</code><br>138–154 | OnAttachedToVisualTree @140; UpdateLayoutMode @152 | No extracted literal effects. |
| <span id="m-32f6babff06f"></span><code>ResponsiveWorkspaceSplit.OnSizeChanged(SizeChangedEventArgs)</code><br>156–163 | OnSizeChanged @158; UpdateLayoutMode @161 | No extracted literal effects. |
| <span id="m-b54c25872904"></span><code>ResponsiveWorkspaceSplit.UpdateLayoutMode(double)</code><br>165–223 | IsNaN @167; IsInfinity @167; ResolveBreakpoint @172; Set @182; Max @189; Clear @194; Add @195; Clear @197; Add @198; SetColumn @202; SetRow @203 | No extracted literal effects. |

</details>

## SearchOption.cs {#src-f2c868b1c931}

<code>Software/src/GetSeek.UI.Components/Controls/SearchOption.cs</code> · 12 lines.

SHA-256: <code>b7f9fd845f34e1f62135df2b016799ddb16c46885fcb74076bb1c4cc3e521775</code>.

Declarations: <code>SearchOption</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-d281023b4b11"></span><code>SearchOption.ToString()</code><br>9–11 | IsNullOrWhiteSpace @9 | No extracted literal effects. |

</details>

## SharedDataTable.axaml.cs {#src-122906318cb3}

<code>Software/src/GetSeek.UI.Components/Controls/SharedDataTable.axaml.cs</code> · 643 lines.

SHA-256: <code>4a59a32d8e8346dfeb895f3a8c363781707f9c02c44a41ca6d0fe80a7e316ce5</code>.

Declarations: <code>SharedDataTable : UserControl</code> (line 19).

<details markdown>
<summary>Methods, calls, table effects and failures (27)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f01cb2621b9d"></span><code>SharedDataTable.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>49–58 | OnPropertyChanged @51; DetachDefinition @54; GetNewValue(DataTableDefinition?) @55; Rebuild @56 | No extracted literal effects. |
| <span id="m-c1ea919de656"></span><code>SharedDataTable.Rebuild()</code><br>60–119 | Clear @65; Clear @66; DetachDefinition @74; BuildHeader @81; Add @91; BuildRow @91; Invoke @112 | No extracted literal effects. |
| <span id="m-dfda2ba5a342"></span><code>SharedDataTable.BuildHeader(DataTableDefinition)</code><br>121–225 | GetTableColumnDefinitions @126; GetSelectablePageIds @133; All @134; Any @135; SetTip @143; Invoke @143; SetPageSelection @144; SetColumn @145; Add @146; CreateHorizontalViewport @150; CreateDataGrid @152; ToArray @152; Where @152; Select @153; HeaderText @160; Max @162; HeaderAction @169; SortHeaderText @176; ToggleSort @184; Count @205; Take @205; Add @211; Add @224 | No extracted literal effects. |
| <span id="m-c082c77c3bcb"></span><code>SharedDataTable.GetTableColumnDefinitions(DataTableDefinition)</code><br>227–239 | Where @236; ToString @237; Max @237 | No extracted literal effects. |
| <span id="m-3335fa4cf083"></span><code>SharedDataTable.SelectionGlyph(bool?)</code><br>241–246 | — | No extracted literal effects. |
| <span id="m-cb3e8ecbe847"></span><code>SharedDataTable.GetSelectablePageIds(DataTableDefinition)</code><br>248–254 | ToArray @249; Distinct @249; Where @249; Select @249; Where @249; Invoke @250; IsNullOrWhiteSpace @252 | No extracted literal effects. |
| <span id="m-b6ffbf0aa033"></span><code>SharedDataTable.SortHeaderText(IDataTableState,DataTableColumnDescriptor)</code><br>256–261 | Equals @258; HeaderText @259 | No extracted literal effects. |
| <span id="m-314984e0edef"></span><code>SharedDataTable.HeaderText(DataTableColumnDescriptor)</code><br>263–263 | Invoke @263 | No extracted literal effects. |
| <span id="m-b98b61a3792f"></span><code>SharedDataTable.BuildRow(DataTableDefinition,object,int)</code><br>265–435 | GetTableColumnDefinitions @270; Invoke @278; RowIdSelector @279; IsRowSelected @283; SelectRow @288; SetColumn @289; Add @290; CreateHorizontalViewport @294; CreateDataGrid @295; ToArray @295; Where @295; Select @296; StyleClass @316; Add @327; SetTip @328; Count @331; Take @331; BeginRowActivation @333; TrackRowActivation @334; EndRowActivation @335; Add @340; Add @345; IsInteractiveSource @359; Post @362; Any(Control) @364; OfType(Control) @364; GetVisualDescendants @364; Remove @366; Add @380; CanExecute @385; Open @397; Add @398; Where(Control) @424 | No extracted literal effects. |
| <span id="m-472735eeacea"></span><code>SharedDataTable.StyleClass(DataTableCellStyle)</code><br>437–447 | — | No extracted literal effects. |
| <span id="m-ba8e0c420355"></span><code>SharedDataTable.CreateDataGrid(IReadOnlyList&lt;DataTableColumnDescriptor&gt;)</code><br>449–460 | Add @454; Max @454 | No extracted literal effects. |
| <span id="m-c21ff5be850e"></span><code>SharedDataTable.CreateHorizontalViewport()</code><br>462–484 | SetDataGridWidth @473; BeginHorizontalPan @474; ContinueHorizontalPan @475; EndHorizontalPan @476; ClearHorizontalPan @480; Add @482 | No extracted literal effects. |
| <span id="m-d9569dde0709"></span><code>SharedDataTable.BeginHorizontalPan(ScrollViewer,PointerPressedEventArgs)</code><br>486–496 | GetCurrentPoint @489; IsInteractiveSource @490; GetPosition @494 | No extracted literal effects. |
| <span id="m-4f614851a979"></span><code>SharedDataTable.ContinueHorizontalPan(ScrollViewer,PointerEventArgs)</code><br>498–523 | GetPosition @502; Abs @508; ClearHorizontalPan @510; Capture @516; Clamp @520; Max @520 | No extracted literal effects. |
| <span id="m-3c0e058b50fd"></span><code>SharedDataTable.EndHorizontalPan(ScrollViewer,PointerReleasedEventArgs)</code><br>525–533 | ClearHorizontalPan @530 | No extracted literal effects. |
| <span id="m-118aba6c6b32"></span><code>SharedDataTable.ClearHorizontalPan()</code><br>535–544 | Capture @543 | No extracted literal effects. |
| <span id="m-e046b7286fc3"></span><code>SharedDataTable.IsInteractiveSource(object?,ScrollViewer)</code><br>546–558 | GetVisualParent @549; Contains @552 | No extracted literal effects. |
| <span id="m-2aa86e6673df"></span><code>SharedDataTable.SetDataGridWidth(ScrollViewer)</code><br>560–565 | Sum @563; Max @563 | No extracted literal effects. |
| <span id="m-8739eeca8dba"></span><code>SharedDataTable.OnHorizontalScrollChanged(object?,ScrollChangedEventArgs)</code><br>567–580 | ReferenceEquals @575 | No extracted literal effects. |
| <span id="m-bbb4830d615c"></span><code>SharedDataTable.BeginRowActivation(object,ScrollViewer,PointerPressedEventArgs)</code><br>586–595 | IsInteractiveSource @589; Invoke @590; CanExecute @591; GetPosition @593 | No extracted literal effects. |
| <span id="m-d837f3e5e125"></span><code>SharedDataTable.TrackRowActivation(PointerEventArgs)</code><br>597–605 | GetPosition @600 | No extracted literal effects. |
| <span id="m-f81e53710441"></span><code>SharedDataTable.EndRowActivation(DataTableDefinition,object,PointerReleasedEventArgs)</code><br>607–615 | TrackRowActivation @610; Invoke @613; CanExecute @613; Execute @614 | No extracted literal effects. |
| <span id="m-47e43ddd8426"></span><code>SharedDataTable.OnPageSizeChanged(object?,SelectionChangedEventArgs)</code><br>617–621 | — | No extracted literal effects. |
| <span id="m-207fc55c8c55"></span><code>SharedDataTable.OnStateChanged(object?,System.ComponentModel.PropertyChangedEventArgs)</code><br>623–623 | QueueRebuild @623 | No extracted literal effects. |
| <span id="m-551e305344e8"></span><code>SharedDataTable.OnRowsChanged(object?,NotifyCollectionChangedEventArgs)</code><br>624–624 | QueueRebuild @624 | No extracted literal effects. |
| <span id="m-ba718a6a0101"></span><code>SharedDataTable.QueueRebuild()</code><br>626–635 | Post @630; Rebuild @633 | No extracted literal effects. |
| <span id="m-1a5715a25395"></span><code>SharedDataTable.DetachDefinition(DataTableDefinition?)</code><br>637–642 | — | No extracted literal effects. |

</details>

## ShortcutBadge.axaml.cs {#src-ea8a84a0aa3b}

<code>Software/src/GetSeek.UI.Components/Controls/ShortcutBadge.axaml.cs</code> · 21 lines.

SHA-256: <code>386412a6cee9c7b5cb12578471d60679b2ef60944a0394871b105868cbe21440</code>.

Declarations: <code>ShortcutBadge : UserControl</code> (line 6).

## SortableHeader.axaml.cs {#src-7238ef4c7ca5}

<code>Software/src/GetSeek.UI.Components/Controls/SortableHeader.axaml.cs</code> · 82 lines.

SHA-256: <code>8e6bf8f700fdc16f5b32e5cd08842070f6973b96dc048a04dd6e901fc4d245de</code>.

Declarations: <code>SortableHeader : UserControl</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-48ebcc1f4ad7"></span><code>SortableHeader.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>69–76 | OnPropertyChanged @71; RaisePropertyChanged @74 | No extracted literal effects. |

</details>

## StatusBadgePill.axaml.cs {#src-86c7ca833bec}

<code>Software/src/GetSeek.UI.Components/Controls/StatusBadgePill.axaml.cs</code> · 64 lines.

SHA-256: <code>4f0f8a81d46c7e31b0375e7c1b9f1e9e1e6e9062784a038bc74c55266b1437a3</code>.

Declarations: <code>StatusBadgePill : UserControl</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-08215b5b5505"></span><code>StatusBadgePill.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>42–47 | OnPropertyChanged @44; UpdateVisualState @46 | No extracted literal effects. |
| <span id="m-7e2a1f6ff3d9"></span><code>StatusBadgePill.UpdateVisualState()</code><br>49–63 | Remove @53; Remove @56; Add @58; Add @61 | No extracted literal effects. |

</details>

## TouchKeyboardControl.axaml.cs {#src-005a919ff1b2}

<code>Software/src/GetSeek.UI.Components/Controls/TouchKeyboardControl.axaml.cs</code> · 322 lines.

SHA-256: <code>01d53c33967ec3c1403164cea91257ffb424a8c874acd20cfdd595ca36b2994c</code>.

Declarations: <code>TouchKeyboardControl : UserControl</code> (line 10).

<details markdown>
<summary>Methods, calls, table effects and failures (7)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-f5f4b33f0b79"></span><code>TouchKeyboardControl.WireHeaderEvents()</code><br>138–145 | FindControl(Button) @140; Invoke @141; CycleLayout @144 | No extracted literal effects. |
| <span id="m-54921c23fbf7"></span><code>TouchKeyboardControl.CycleLayout()</code><br>147–152 | GetNextLayout @149; Invoke @151 | No extracted literal effects. |
| <span id="m-a48053b9c390"></span><code>TouchKeyboardControl.SetLayout(string)</code><br>154–157 | — | No extracted literal effects. |
| <span id="m-6e0092076936"></span><code>TouchKeyboardControl.RebuildKeyboard()</code><br>159–281 | Resolve @161; Clear @164; FindControl(StackPanel) @166; Clear @174; Clear @175; Clear @176; Clear @177; Add @184; CreateKeyButton @184; Parse @193; Invoke @195; Add @203; Add @212; Parse @234; ToggleShift @236; Add @237; UpdateKeyCaptions @280 | No extracted literal effects. |
| <span id="m-6a9ed7743249"></span><code>TouchKeyboardControl.CreateKeyButton(TouchKeyDef)</code><br>283–301 | GetDisplayText @287; Parse @290; GetEmittedText @295; Invoke @296; Add @299 | No extracted literal effects. |
| <span id="m-55fa90b8db3c"></span><code>TouchKeyboardControl.ToggleShift()</code><br>303–313 | Parse @309; UpdateKeyCaptions @312 | No extracted literal effects. |
| <span id="m-1552ce56ec51"></span><code>TouchKeyboardControl.UpdateKeyCaptions()</code><br>315–321 | GetDisplayText @319 | No extracted literal effects. |

</details>

## TouchKeyboardLayout.cs {#src-1e62a98a330a}

<code>Software/src/GetSeek.UI.Components/Controls/TouchKeyboardLayout.cs</code> · 284 lines.

SHA-256: <code>33135e9f8c0efc420d62648fe1a71979aafcc46671b33637500c6c9b57a50f8e</code>.

Declarations: <code>TouchKeyKind</code> (line 6), <code>TouchKeyDef</code> (line 18), <code>TouchKeyboardLayout</code> (line 58), <code>TouchKeyboardRegistry</code> (line 66).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-470cb5fc21ae"></span><code>TouchKeyDef.GetDisplayText(bool)</code><br>28–31 | IsNullOrEmpty @30 | No extracted literal effects. |
| <span id="m-909a08653f6a"></span><code>TouchKeyDef.GetEmittedText(bool)</code><br>33–36 | IsNullOrEmpty @35 | No extracted literal effects. |
| <span id="m-dc18b535910e"></span><code>TouchKeyDef.Char(string,string,double)</code><br>38–46 | — | No extracted literal effects. |
| <span id="m-6c76efc7a526"></span><code>TouchKeyDef.Action(TouchKeyKind,string,double,string)</code><br>48–55 | — | No extracted literal effects. |
| <span id="m-24a943526618"></span><code>TouchKeyboardRegistry.Resolve(string?)</code><br>257–271 | IsNullOrWhiteSpace @259; Equals @262 | No extracted literal effects. |
| <span id="m-1a5eddc420a4"></span><code>TouchKeyboardRegistry.GetNextLayout(string)</code><br>273–283 | Equals @277 | No extracted literal effects. |

</details>

## TouchNumpadControl.axaml.cs {#src-b0a0a83fd54a}

<code>Software/src/GetSeek.UI.Components/Controls/TouchNumpadControl.axaml.cs</code> · 88 lines.

SHA-256: <code>5113a0234fc6c24624e104440228f71120be76702d1ff2df1e89c6c66844fc00</code>.

Declarations: <code>TouchNumpadControl : UserControl</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-5b33e667b27e"></span><code>TouchNumpadControl.WireEvents()</code><br>60–87 | FindControl(Button) @62; Invoke @63; GetVisualDescendants @74; Contains @76 | No extracted literal effects. |

</details>

## WorkspaceFilterBar.axaml.cs {#src-dc49018894e7}

<code>Software/src/GetSeek.UI.Components/Controls/WorkspaceFilterBar.axaml.cs</code> · 57 lines.

SHA-256: <code>357cda47eac18d09b1a4c073ab86862475ba6d4bd58c2cfa8db5ade2d7ec4c33</code>.

Declarations: <code>WorkspaceFilterBar : UserControl</code> (line 7).

<details markdown>
<summary>Methods, calls, table effects and failures (3)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-8a0b7808822d"></span><code>WorkspaceFilterBar.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>22–34 | OnPropertyChanged @24; GetNewValue(DataTableDefinition?) @27; RebuildToolbarControls @29; ApplyFilterLayout @30 | No extracted literal effects. |
| <span id="m-a67762fb16bd"></span><code>WorkspaceFilterBar.ApplyFilterLayout()</code><br>36–42 | — | No extracted literal effects. |
| <span id="m-b75c1e4fdfda"></span><code>WorkspaceFilterBar.RebuildToolbarControls(DataTableDefinition?)</code><br>43–56 | Clear @45; Invoke @51; Add @54; CreateControl @54 | No extracted literal effects. |

</details>

## WorkspaceHeader.axaml.cs {#src-a0a5fdab675a}

<code>Software/src/GetSeek.UI.Components/Controls/WorkspaceHeader.axaml.cs</code> · 42 lines.

SHA-256: <code>c33a233364ff2d74b0874201aae4607c6e0238e9a626e7602aa34ae9ffafb6e6</code>.

Declarations: <code>WorkspaceHeader : UserControl</code> (line 8).

<details markdown>
<summary>Methods, calls, table effects and failures (1)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-50ba970fac27"></span><code>WorkspaceHeader.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>32–41 | OnPropertyChanged @34; GetNewValue(Control?) @36; GetNewValue(bool) @40 | No extracted literal effects. |

</details>

## WorkspaceOverlayHost.cs {#src-c4be2419c9fd}

<code>Software/src/GetSeek.UI.Components/Controls/WorkspaceOverlayHost.cs</code> · 262 lines.

SHA-256: <code>1dd81eb4b904a18d8aa071e1e4fecf40fd133156469e4c2c39efdf37c12343ea</code>.

Declarations: <code>WorkspaceOverlayHost : Panel</code> (line 12), <code>PopupConstraintRegistration : IDisposable</code> (line 116), <code>Geometry</code> (line 261).

<details markdown>
<summary>Methods, calls, table effects and failures (15)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-99446f8e98ea"></span><code>WorkspaceOverlayHost.OnOverlayChanged(object?,AvaloniaPropertyChangedEventArgs)</code><br>51–59 | GetTopLevel @56; GetFocusedElement @56; Post @57 | No extracted literal effects. |
| <span id="m-4ca64f9e0c54"></span><code>WorkspaceOverlayHost.UpdateFocus()</code><br>61–85 | FirstOrDefault @64; OrderByDescending @64; Where @64; Reverse @64; GetIsDialogSurface @64; ReferenceEquals @66; Remove @69; Contains @71; GetVisualDescendants @71; Focus @73; Focus @79; FirstOrDefault(Control) @82; OfType(Control) @82; GetVisualDescendants @82; Focus @84 | No extracted literal effects. |
| <span id="m-c2d4cd37c6b3"></span><code>WorkspaceOverlayHost.ConstrainPopup(Popup)</code><br>88–103 | ThrowIfNull @90; TryGetValue @94; Dispose @96 | No extracted literal effects. |
| <span id="m-0ab65c863bb1"></span><code>WorkspaceOverlayHost.UnregisterConstraint(Popup,PopupConstraintRegistration)</code><br>105–114 | TryGetValue @109; ReferenceEquals @109; Remove @111 | No extracted literal effects. |
| <span id="m-3c4812ac7682"></span><code>PopupConstraintRegistration.OnCustomPlacement(CustomPopupPlacement)</code><br>149–156 | CalculatePopupAnchor @152 | No extracted literal effects. |
| <span id="m-632801f18974"></span><code>PopupConstraintRegistration.OnPopupOpened(object?,EventArgs)</code><br>158–162 | ClampChild @161 | No extracted literal effects. |
| <span id="m-2662c3b39d60"></span><code>PopupConstraintRegistration.OnHostSizeChanged(object?,SizeChangedEventArgs)</code><br>164–174 | ClampChild @167 | No extracted literal effects. |
| <span id="m-22f33ba1ff22"></span><code>PopupConstraintRegistration.ClampChild()</code><br>176–183 | Max @180 | No extracted literal effects. |
| <span id="m-0ec886c15ace"></span><code>PopupConstraintRegistration.Dispose()</code><br>185–201 | Exchange @187; ReferenceEquals @193; UnregisterConstraint @199; SuppressFinalize @200 | No extracted literal effects. |
| <span id="m-e2e64c38f733"></span><code>WorkspaceOverlayHost.CalculatePopupAnchor(Visual,Size)</code><br>204–212 | TranslatePoint @206; Clamp @207; Max @208 | No extracted literal effects. |
| <span id="m-633bf9eaf3b8"></span><code>WorkspaceOverlayHost.GetIsDialogSurface(Control)</code><br>214–214 | GetValue @214 | No extracted literal effects. |
| <span id="m-60dcb7163d58"></span><code>WorkspaceOverlayHost.SetIsDialogSurface(Control,bool)</code><br>215–215 | SetValue @215 | No extracted literal effects. |
| <span id="m-a8250a0313a0"></span><code>WorkspaceOverlayHost.MeasureOverride(Size)</code><br>217–232 | Where @220; GetIsDialogSurface @220; ClampSurface @222; Measure @223; Max @224; Where(Control) @227; OfType(Control) @227; GetVisualDescendants @227; Contains @229; MeasureOverride @231 | No extracted literal effects. |
| <span id="m-abebca086f19"></span><code>WorkspaceOverlayHost.ArrangeOverride(Size)</code><br>234–241 | ArrangeOverride @236; Where @238; GetIsDialogSurface @238; Arrange @239; Max @239 | No extracted literal effects. |
| <span id="m-bb9e2d2b8319"></span><code>WorkspaceOverlayHost.ClampSurface(Control,Size)</code><br>243–259 | TryGetValue @245; Add @248; Max @250; SetCurrentValue @253; Min @254; IsNaN @255 | No extracted literal effects. |

</details>

## WorkspaceSearchBox.axaml.cs {#src-56b0be930463}

<code>Software/src/GetSeek.UI.Components/Controls/WorkspaceSearchBox.axaml.cs</code> · 399 lines.

SHA-256: <code>18e61921483b9a25f810b036aa5575d085d887c8e58838aaae1cb15ccd7c874a</code>.

Declarations: <code>WorkspaceSearchBox : UserControl, IDisposable</code> (line 13), <code>SimpleCommand : ICommand</code> (line 386), <code>SimpleParamCommand : ICommand</code> (line 393).

<details markdown>
<summary>Methods, calls, table effects and failures (13)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-9fdc96bd4237"></span><code>WorkspaceSearchBox.OnAttachedToVisualTree(object?,VisualTreeAttachmentEventArgs)</code><br>213–223 | Dispose @215; FindAncestorOfType(WorkspaceOverlayHost) @218; ConstrainPopup @221 | No extracted literal effects. |
| <span id="m-9b660f1071e9"></span><code>WorkspaceSearchBox.OnDetachedFromVisualTree(object?,VisualTreeAttachmentEventArgs)</code><br>225–229 | Dispose @227 | No extracted literal effects. |
| <span id="m-a93fe299da70"></span><code>WorkspaceSearchBox.Dispose()</code><br>231–236 | Dispose @233; SuppressFinalize @235 | No extracted literal effects. |
| <span id="m-2cd00978cf58"></span><code>WorkspaceSearchBox.OnPropertyChanged(AvaloniaPropertyChangedEventArgs)</code><br>238–266 | OnPropertyChanged @240; ApplyDimensions @244; UpdateOptionStates @250; GetNewValue(bool) @252; GetSearchResourceDouble @257; Max @258; FindAncestorOfType(WorkspaceOverlayHost) @259 | No extracted literal effects. |
| <span id="m-7a5a3943cd27"></span><code>WorkspaceSearchBox.GetSearchResourceDouble(string,double)</code><br>268–275 | TryFindResource @270; TryFindResource @272 | No extracted literal effects. |
| <span id="m-3df52f34c611"></span><code>WorkspaceSearchBox.ApplyDimensions()</code><br>277–294 | Add @281; Remove @287; ClearValue @288 | No extracted literal effects. |
| <span id="m-f1ab6a30fb0b"></span><code>WorkspaceSearchBox.UpdateOptionStates()</code><br>296–307 | GetEnumerator @301; MoveNext @302; IsNullOrWhiteSpace @306 | No extracted literal effects. |
| <span id="m-4ab483fef30f"></span><code>WorkspaceSearchBox.SelectOption(SearchOption)</code><br>321–326 | — | No extracted literal effects. |
| <span id="m-95c20553f819"></span><code>WorkspaceSearchBox.OnSearchTextBoxKeyDown(object?,KeyEventArgs)</code><br>328–384 | ScrollIntoView @358; SelectOption @380 | No extracted literal effects. |
| <span id="m-4d6c57fb1258"></span><code>SimpleCommand.CanExecute(object?)</code><br>389–389 | — | No extracted literal effects. |
| <span id="m-5d8a96fd4b20"></span><code>SimpleCommand.Execute(object?)</code><br>390–390 | execute @390 | No extracted literal effects. |
| <span id="m-f59584a152ee"></span><code>SimpleParamCommand.CanExecute(object?)</code><br>396–396 | — | No extracted literal effects. |
| <span id="m-0073ebba7087"></span><code>SimpleParamCommand.Execute(object?)</code><br>397–397 | execute @397 | No extracted literal effects. |

</details>

## UnicodeTextHelper.cs {#src-fb71511563af}

<code>Software/src/GetSeek.UI.Components/Utilities/UnicodeTextHelper.cs</code> · 163 lines.

SHA-256: <code>c9f85fe2bcf4ceb6184f6063282f2c739b2056cedd1ee38ba2c7d250c9024b3b</code>.

Declarations: <code>UnicodeTextHelper</code> (line 12).

<details markdown>
<summary>Methods, calls, table effects and failures (6)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-fc7a0194d12e"></span><code>UnicodeTextHelper.DeleteLastTextElement(string?)</code><br>18–36 | IsNullOrEmpty @20; GetTextElementEnumerator @23; MoveNext @26 | No extracted literal effects. |
| <span id="m-55db63591af9"></span><code>UnicodeTextHelper.DeleteGraphemeAt(string?,int,bool)</code><br>42–103 | IsNullOrEmpty @44; Clamp @47; GetGraphemeBoundaries @49; Remove @71 | No extracted literal effects. |
| <span id="m-45287e1f128d"></span><code>UnicodeTextHelper.GetPreviousGraphemeIndex(string?,int)</code><br>108–122 | IsNullOrEmpty @110; GetTextElementEnumerator @113; MoveNext @115 | No extracted literal effects. |
| <span id="m-cebbdfb3b6ae"></span><code>UnicodeTextHelper.GetNextGraphemeIndex(string?,int)</code><br>127–139 | IsNullOrEmpty @129; GetTextElementEnumerator @132; MoveNext @133 | No extracted literal effects. |
| <span id="m-a59bb935b647"></span><code>UnicodeTextHelper.GetTextElementCount(string?)</code><br>144–150 | IsNullOrEmpty @146 | No extracted literal effects. |
| <span id="m-90d0ce151d9a"></span><code>UnicodeTextHelper.GetGraphemeBoundaries(string)</code><br>152–162 | GetTextElementEnumerator @155; MoveNext @156; Add @158 | No extracted literal effects. |

</details>

## AXAML, migrations and project inputs

### BatchConfirmationControl.axaml {#src-bb0121dad6cf}

<code>Software/src/GetSeek.UI.Components/Controls/BatchConfirmationControl.axaml</code> · 37 lines · SHA-256 <code>060fb43277cd5b80c3217631a9979d5c8163d092a9605c276004a42c2f473739</code>.

### CompactDateField.axaml {#src-6766f6101f59}

<code>Software/src/GetSeek.UI.Components/Controls/CompactDateField.axaml</code> · 99 lines · SHA-256 <code>e4e23924f7dfe12b36b758cf384b376a5f5404e81a6de72ee17956c439595c06</code>.

### DataTableWorkspaceFrame.axaml {#src-f2490ec284cc}

<code>Software/src/GetSeek.UI.Components/Controls/DataTableWorkspaceFrame.axaml</code> · 27 lines · SHA-256 <code>83160da4d6ad2debb1174eb5d2ffa03ed9a07deeaf677b082ffa2af7747a926c</code>.

### ModalShell.axaml {#src-411c91026435}

<code>Software/src/GetSeek.UI.Components/Controls/ModalShell.axaml</code> · 70 lines · SHA-256 <code>0c63cdcca17dc3370a2e18d2cb671217fa9c740178b5445bbc1a524e9a73811a</code>.

### Pager.axaml {#src-c6096e07ed76}

<code>Software/src/GetSeek.UI.Components/Controls/Pager.axaml</code> · 28 lines · SHA-256 <code>ed9f6ffe1f21b8368636f5fe8f8ad4d7946e3a9e09a0116ef8de593894dccf3a</code>.

### PageSizeSelector.axaml {#src-6e1366f1f284}

<code>Software/src/GetSeek.UI.Components/Controls/PageSizeSelector.axaml</code> · 21 lines · SHA-256 <code>96988cd514e7625e0807c645b30bd767274bf8657ca34240615299e86e6ce02b</code>.

### ResponsiveWorkspaceSplit.axaml {#src-fa1cb6249d63}

<code>Software/src/GetSeek.UI.Components/Controls/ResponsiveWorkspaceSplit.axaml</code> · 8 lines · SHA-256 <code>a746cbed81058464dfbabda1722a558d20c0c8d7ece555b5345a5feee4d7fe8e</code>.

### SharedDataTable.axaml {#src-ee1c40faec29}

<code>Software/src/GetSeek.UI.Components/Controls/SharedDataTable.axaml</code> · 45 lines · SHA-256 <code>ef87f59b85e6ff1581aa0cf1e6f7cec7488d9e2c1bbb2037c8845855672b0741</code>.

### ShortcutBadge.axaml {#src-d10914aff0c1}

<code>Software/src/GetSeek.UI.Components/Controls/ShortcutBadge.axaml</code> · 18 lines · SHA-256 <code>24bff1c25485b66a656ce38c5d69ea428fc71c9681394db314d5cd9f3e327453</code>.

### SortableHeader.axaml {#src-f86ce74ce1d6}

<code>Software/src/GetSeek.UI.Components/Controls/SortableHeader.axaml</code> · 24 lines · SHA-256 <code>e9d9f5546bddce6d826765371598e8d4bd17de257783e19296e1246cd58bc6e0</code>.

### StatusBadgePill.axaml {#src-3674664bda00}

<code>Software/src/GetSeek.UI.Components/Controls/StatusBadgePill.axaml</code> · 21 lines · SHA-256 <code>53e009da5854f4dd8757f01b47516520fb4b0f58c6df8cd4b9cc187856131ef3</code>.

### TouchKeyboardControl.axaml {#src-a34470da23bf}

<code>Software/src/GetSeek.UI.Components/Controls/TouchKeyboardControl.axaml</code> · 106 lines · SHA-256 <code>8bafcf84e644ae1953050d33cd3e76511738e651610fb63124c70d09c7f3b14a</code>.

### TouchNumpadControl.axaml {#src-e3b723f73928}

<code>Software/src/GetSeek.UI.Components/Controls/TouchNumpadControl.axaml</code> · 117 lines · SHA-256 <code>c0881866e933ead04810b89bff3e2020f1ea9a848ebd40c9254bc6b2fa6b5cc3</code>.

### WorkspaceFilterBar.axaml {#src-a4e0d8950520}

<code>Software/src/GetSeek.UI.Components/Controls/WorkspaceFilterBar.axaml</code> · 25 lines · SHA-256 <code>5a8007e105154c05702ca0c4cf893eebf5be35d4f280d44f1f6816408fa36286</code>.

### WorkspaceHeader.axaml {#src-800f7abba97e}

<code>Software/src/GetSeek.UI.Components/Controls/WorkspaceHeader.axaml</code> · 25 lines · SHA-256 <code>55df680faa48dc352371d5f9092c4bc253d2c6dfdf5594d74945750e38fb788b</code>.

### WorkspaceSearchBox.axaml {#src-f8b5ead12853}

<code>Software/src/GetSeek.UI.Components/Controls/WorkspaceSearchBox.axaml</code> · 151 lines · SHA-256 <code>56c5b79cd6ba28c7990b2ecfde6fc25ca643d70383fc08f82abf8bf17282463c</code>.

### GetSeek.UI.Components.csproj {#src-6da00d4f185c}

<code>Software/src/GetSeek.UI.Components/GetSeek.UI.Components.csproj</code> · 19 lines · SHA-256 <code>89314e6bc79115c03dad5a53be65c3a4a2350823f120bf0675293077c56e0992</code>.

### Buttons.axaml {#src-6035e6dc52fb}

<code>Software/src/GetSeek.UI.Components/Themes/Buttons.axaml</code> · 350 lines · SHA-256 <code>627786f3ca36a7912cbba1292397fc17ed2f96b88161a90f88daf1e932d84a1d</code>.

### Inputs.axaml {#src-545b9a70ff81}

<code>Software/src/GetSeek.UI.Components/Themes/Inputs.axaml</code> · 183 lines · SHA-256 <code>e36d2b27a583f0249d4f15c8714f7af8228726e65f673ec6d65604cafce9372a</code>.

### OneTheme.Dark.axaml {#src-9fb48496d97f}

<code>Software/src/GetSeek.UI.Components/Themes/OneTheme.Dark.axaml</code> · 132 lines · SHA-256 <code>c3b6959e7049e28e3a60a2d0a746a8929216697586019de029a5c1b616b6aa07</code>.

### OneTheme.Light.axaml {#src-b0bb877f31a5}

<code>Software/src/GetSeek.UI.Components/Themes/OneTheme.Light.axaml</code> · 133 lines · SHA-256 <code>d2422be319785f7c38022c5d3a8af742ecddc47ac6cd3d5b242cb2eb1686dbd5</code>.
