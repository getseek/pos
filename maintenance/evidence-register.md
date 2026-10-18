# Evidence register

Authoritative machine record: `evidence-register.json`. Reviewed 2026-10-18.

`source-inspected` proves the referenced text exists; `reported` is a document claim; `historical-automated` is persisted test evidence with its original timestamp. None means fresh manual or hardware acceptance.

| ID | Kind | Evidence | Scope/limit |
| --- | --- | --- | --- |
| E-001 | source-inspected | `Software/src/GetSeek.Desktop/Bootstrap/PosBootstrapper.cs` | Separate LocalAppData Real and persistent Demo paths exist; this does not certify a migration or reset journey. |
| E-002 | source-inspected | `Software/src/GetSeek.Desktop/App.axaml.cs` | Explicit --real-workspace/--demo-workspace selection is distinct from the legacy --demo preview. |
| E-003 | source-inspected | `Software/src/GetSeek.DataService/DataServiceComposition.cs` | DataService uses separate ProgramData Private paths; installing it does not demonstrate desktop IPC cutover. |
| E-004 | source-inspected | `Software/src/GetSeek.UI.Components/GetSeek.UI.Components.csproj` | TTF resources and font license are declared; OS rendering remains unverified. |
| E-005 | source-inspected | `Software/src/GetSeek.Infrastructure/GetSeek.Infrastructure.csproj` | Print-font content has copy-to-output and copy-to-publish rules. |
| E-006 | source-inspected | `Software/src/GetSeek.Infrastructure/Persistence/Migrations/DatabaseMigrator.cs` | Current migration registration can be inspected alongside SQL files; no live database was opened. |
| E-007 | reported | `GETSEEK_POS_COMPLETE_DOCUMENTATION.md` | Mixed current and historical claims; older open-audit/1,203-test wording conflicts with the repair audit. |
| E-008 | reported | `docs/unified-teams-completeness-audit-2026-10-15.md` | Repair report claims A01–A12 closure and a 1,228-test acceptance run; verify independently before claiming fresh acceptance. |
| E-009 | source-inspected | `Software/tests/GetSeek.IntegrationTests/GetSeek.IntegrationTests.csproj` | Three historical Compile Remove exclusions remain in the test project. |
| E-010 | source-inspected | `Software/global.json` | SDK policy: 10.0.100 minimum feature selection, latestFeature roll-forward, no prerelease. |
| E-011 | source-inspected | `Software/src/GetSeek.Desktop/ViewModels/MainViewModel.cs` | Historical screenshot sample names/products match source defaults and CreateDemo data; screenshots do not prove current behavior. |
| E-012 | historical-automated | `Software/tests/GetSeek.UnitTests/TestResults/completeness-repaired-final_net10.0_20261015184430.trx` | Persisted TRX parsed; not rerun during this documentation stage. |
| E-013 | historical-automated | `Software/tests/GetSeek.IntegrationTests/TestResults/completeness-repaired-final_net10.0_20261015185038.trx` | Persisted TRX parsed; not rerun during this documentation stage. |
| E-014 | historical-automated | `Software/tests/GetSeek.AcceptanceTests/TestResults/completeness-repaired-final_net10.0_20261015185040.trx` | Persisted TRX parsed; not rerun during this documentation stage. |

Parsed original final TRX files: **1228 passed**, 0 failed, 0 not executed (251 unit + 976 integration + 1 acceptance), on 2026-10-15. Three compile exclusions remain. No application tests, shop writes, physical print, touchscreen, or clean-machine deployment were performed for D00–D02.

SHA-256 digests and original run times are retained in JSON. The final source hash comparison detects changes during this stage; future source-review refreshes must retain the original evidence dates.
