---
id: PP-REVIEW-CODE-CONTRACTS
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-015"]
features: []
---

# GetSeek.Contracts source catalogue

<div class="meta">DRAFT · code snapshot 18 October 2026 · source review, not runtime acceptance</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.Contracts.csproj:1](code-contracts.md#src-b67f3bc057cb). Dependencies: none declared.

## ServicePipeClient.cs {#src-8c946f8dd93a}

<code>Software/src/GetSeek.Contracts/ServicePipeClient.cs</code> · 49 lines.

SHA-256: <code>557f72545114d30b89ae30335f790296f28ece8afe9b434a2da5d862913bff8f</code>.

Declarations: <code>ServicePipeNames</code> (line 5), <code>ServicePipeClient</code> (line 11).

<details markdown>
<summary>Methods, calls, table effects and failures (2)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-6bbe9c3c581f"></span><code>ServicePipeClient.SendAsync(ServiceRequestEnvelope,TimeSpan,CancellationToken)</code><br>21–37 | ThrowIfNull @26; FromMinutes @27; nameof @28; CreateLinkedTokenSource @30; CancelAfter @31; ConfigureAwait @33; ConnectAsync @33; WriteRequestAsync @34; ReadResponseAsync @35; ValidateResponse @36 | ArgumentOutOfRangeException @28 |
| <span id="m-48d595e66090"></span><code>ServicePipeClient.ValidateResponse(ServiceRequestEnvelope,ServiceResponseEnvelope)</code><br>39–48 | ThrowIfNull @41 | InvalidDataException @44; InvalidDataException @46 |

</details>

## ServiceProtocol.cs {#src-1279cf3e9022}

<code>Software/src/GetSeek.Contracts/ServiceProtocol.cs</code> · 251 lines.

SHA-256: <code>2fdad33b1e9b9ad2750efa5c8bb13e2619a7c2ff5bcdc774e21b318937cc7141</code>.

Declarations: <code>WorkspaceKind</code> (line 7), <code>ServiceRequestEnvelope</code> (line 13), <code>ServiceResponseEnvelope</code> (line 21), <code>ServiceRequestBody</code> (line 30), <code>PingRequest : ServiceRequestBody</code> (line 47), <code>GetWorkspaceSetupRequest : ServiceRequestBody</code> (line 48), <code>ProvisionInitialAdministratorRequest : ServiceRequestBody</code> (line 49), <code>GetUnlockCandidatesRequest : ServiceRequestBody</code> (line 50), <code>AuthenticateSelectedOperatorRequest : ServiceRequestBody</code> (line 51), <code>LogoutSessionRequest : ServiceRequestBody</code> (line 52), <code>GetInventoryPageRequest : ServiceRequestBody</code> (line 53), <code>ThirdPartyLifecycleFilter</code> (line 54), <code>GetThirdPartyPageRequest : ServiceRequestBody</code> (line 60), <code>ImportProductsChunkRequest : ServiceRequestBody</code> (line 68), <code>CheckoutOutcomeRequest : ServiceRequestBody</code> (line 69), <code>ReceiptExportRequest : ServiceRequestBody</code> (line 70), <code>ServiceResponseBody</code> (line 72), <code>PingResponse : ServiceResponseBody</code> (line 89), <code>WorkspaceSetupResponse : ServiceResponseBody</code> (line 90), <code>InitialAdministratorResponse : ServiceResponseBody</code> (line 91), <code>OperatorCandidateDto</code> (line 92), <code>UnlockCandidatesResponse : ServiceResponseBody</code> (line 93), <code>OperatorSessionResponse : ServiceResponseBody</code> (line 94), <code>AuthenticationFailureResponse : ServiceResponseBody</code> (line 95), <code>SessionEndedResponse : ServiceResponseBody</code> (line 96), <code>InventoryPageRowDto</code> (line 97), <code>InventoryPageResponse : ServiceResponseBody</code> (line 98), <code>ThirdPartyPageRowDto</code> (line 99), <code>ThirdPartyPageResponse : ServiceResponseBody</code> (line 100), <code>CheckoutOutcomeResponse : ServiceResponseBody</code> (line 101), <code>ExportedFileResponse : ServiceResponseBody</code> (line 102), <code>ServiceProtocolLimits</code> (line 104), <code>ServiceContractValidator</code> (line 115), <code>ServiceProtocolFrameCodec</code> (line 176).

<details markdown>
<summary>Methods, calls, table effects and failures (8)</summary>

| Method and lines | Invocation syntax | Literal SQL / failures / throws |
| --- | --- | --- |
| <span id="m-8cf4ebd8c023"></span><code>ServiceContractValidator.Validate(ServiceRequestEnvelope)</code><br>117–157 | ThrowIfNull @119; IsNullOrWhiteSpace @128; IsSixToThirtyTwoAsciiDigits @131; ValidatePage @136; Contains @137; Contains @141 | InvalidDataException @120; InvalidDataException @121; InvalidDataException @122; InvalidDataException @123; InvalidDataException @124; InvalidDataException @132; InvalidDataException @134; InvalidDataException @137; InvalidDataException @141; InvalidDataException @142; InvalidDataException @144; InvalidDataException @149; InvalidDataException @153; InvalidDataException @155 |
| <span id="m-a8403f0fd892"></span><code>ServiceContractValidator.ValidatePage(int,int,string?)</code><br>164–169 | — | InvalidDataException @168 |
| <span id="m-4819e2b4a7ba"></span><code>ServiceContractValidator.IsSixToThirtyTwoAsciiDigits(string)</code><br>171–172 | All @172 | No extracted literal effects. |
| <span id="m-4e03c73d9fe4"></span><code>ServiceProtocolFrameCodec.WriteRequestAsync(Stream,ServiceRequestEnvelope,CancellationToken)</code><br>184–194 | Validate @186; SerializeToUtf8Bytes @187; WriteInt32LittleEndian @190; ConfigureAwait @191; WriteAsync @191; FlushAsync @193 | InvalidDataException @188 |
| <span id="m-480a7938fbed"></span><code>ServiceProtocolFrameCodec.ReadRequestAsync(Stream,CancellationToken)</code><br>196–208 | ConfigureAwait @199; ReadExactlyAsync @199; ReadInt32LittleEndian @200; Deserialize(ServiceRequestEnvelope) @204; Validate @206 | InvalidDataException @201 |
| <span id="m-3b509f16c4d1"></span><code>ServiceProtocolFrameCodec.WriteResponseAsync(Stream,ServiceResponseEnvelope,CancellationToken)</code><br>210–223 | SerializeToUtf8Bytes @216; WriteInt32LittleEndian @219; ConfigureAwait @220; WriteAsync @220; FlushAsync @222 | InvalidDataException @213; InvalidDataException @215; InvalidDataException @217 |
| <span id="m-024af8f827d2"></span><code>ServiceProtocolFrameCodec.ReadResponseAsync(Stream,CancellationToken)</code><br>225–239 | ConfigureAwait @228; ReadExactlyAsync @228; ReadInt32LittleEndian @229; Deserialize(ServiceResponseEnvelope) @233 | InvalidDataException @230; InvalidDataException @237 |
| <span id="m-574caffb5b29"></span><code>ServiceProtocolFrameCodec.ReadExactlyAsync(Stream,Memory&lt;byte&gt;,CancellationToken)</code><br>241–250 | ConfigureAwait @246; ReadAsync @246 | EndOfStreamException @247 |

</details>

## AXAML, migrations and project inputs

### GetSeek.Contracts.csproj {#src-b67f3bc057cb}

<code>Software/src/GetSeek.Contracts/GetSeek.Contracts.csproj</code> · 7 lines · SHA-256 <code>3472fccce5613343d3b55f6c2bbc48cbfd3de01f9cf32fd8607b8ac3a7e26395</code>.
