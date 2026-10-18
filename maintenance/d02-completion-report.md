# D00–D02 completion report — Premium POS documentation

Date: **18 October 2026**, Asia/Bangkok. Project: **F:\Premium_POS_docs**.  
Scope completed: **D00 baseline, D01 inventory/coverage, D02 standalone scaffold and local preview**.  
Local preview: **http://127.0.0.1:18181/**. Public deployment: **disabled**.

## 1. Delivered result

A standalone Git-backed Zensical documentation foundation with 13 registered public pages, role/workflow navigation, full-text search, local assets/fonts, three Mermaid business/maintenance process diagrams, and two explicitly historical synthetic Demo screenshots. The site uses the Restaurant documentation's applicable navigation, semantic Markdown, status/register discipline, appearance and staged-build principles without copying its operational state or architecture-stage product claims.

The detailed user/administrator/developer manuals remain D03/D04 work. All current page maturities are DRAFT, and feature records distinguish located code from inspected source and actual verification. No application implementation was changed or newly certified.

## 2. D00 — infrastructure baseline and comparison

Inspected `F:\rust_restaurant`: agent/document/review rules, document/current-review registers, navigation/theme configuration, active and example environment settings, build/static-origin/watcher/lifecycle scripts, existing Caddy JSON, and CI workflow. Completed `maintenance/restaurant-comparison.md` before creating new infrastructure components.

Observed Restaurant Zensical **0.0.71**, preview **127.0.0.1:8000**, origin **127.0.0.1:8001**, Python static serving, and its existing Cloudflare route. A Caddy **2.11.7** executable/configuration exists but no active Caddy process was observed; cloudflared is **2026.10.1**. Restaurant comments report historical Caddy empty-200 behavior. A `127.0.0.1` host matcher was observed; forwarded-Host mismatch is an investigation hypothesis, not a reproduced diagnosis. Premium's later Caddy gate must test the public Host header independently.

All three Restaurant HTTP endpoints (preview, origin, public HTTPS) returned 200 with the expected title at baseline and final verification. Matching task/startup queries returned zero records; the effective launch mechanism remains an operational discovery item, not something this task replaced. The existing tunnel and Caddy configuration digests are unchanged.

Premium ports **18180–18183** passed initial exclusive bind probes and exclusion checks. At completion only Premium's local preview occupies **127.0.0.1:18181**; 18180, 18182 and 18183 remain available. Premium public DNS remains absent. No Caddy server, tunnel, DNS record, Windows task, firewall rule or ProgramData runtime directory was created.

Preservation result: **2,417 baselined application files unchanged**, no application file added/removed, external tunnel/Caddy configuration digests unchanged, protected listener owners/launch identities unchanged, and registered task/startup records unchanged. All three Restaurant endpoints remain HTTP 200 with the expected title. The two loopback endpoint body digests match the baseline; the final public response body digest differs, so byte-for-byte public response preservation is not claimed.

The reference-tree comparison found **53 of 55 original Restaurant file digests unchanged**. These two Restaurant documentation inputs changed during the task:

- `docs/architecture/requirements-traceability.md`
- `docs/reviews/owner-review-plan.md`

An additional Restaurant archive file appeared:

- `docs/reviews/archive/r1-owner-brief-2026-10-18.md`

This task issued no writes to the Restaurant tree. These changes are recorded as concurrent reference-tree activity and were not edited, reverted, or incorporated as Premium authority. The final Restaurant inventory contains 56 files. Full Restaurant source/body immutability therefore cannot be asserted; the existing infrastructure identity/configuration and site health checks pass independently.

## 3. D01 — inventory and source of truth

Inventoried **431 application source files**, **144 test source files**, **8 application projects**, **83 migration SQL files**, **46 Markdown review inputs**, and **27 existing screenshots**. Created **22 stable feature/workflow IDs** with audience roles, implementation entry-point paths/digests, evidence references, future guide targets, document maturity and explicit limits.

Authoritative records:

| Record | Purpose |
| --- | --- |
| `maintenance/source-inventory.json` | Application/test source and migration/project inventory with digests. |
| `maintenance/content-inventory.json` | Existing guides/archive markers and screenshot review dispositions. |
| `maintenance/features.json` | Workflow/role → source digest → evidence → guide target/maturity/limit. |
| `maintenance/evidence-register.json` | Stable evidence IDs, types, original paths/digests and historical run timestamps. |
| `maintenance/document-register.json` | One stable ID/revision/maturity record for each public Markdown page. |
| `maintenance/assets.json` | Reviewed public asset paths, digests, provenance, classification and licenses. |

Readable inventory, coverage and evidence views live beside these records. `maintenance/findings.md` is the single active Premium documentation findings register. Public feature/document reference pages are deterministically generated from the local JSON records.

Parsed the actual final persisted TRX files from **15 October 2026**: **251 unit + 976 integration + 1 acceptance = 1,228 passed**, zero failed/not executed. Three historical integration compile exclusions remain explicitly disclosed. No application build/test was run in this stage. This reconciles the historical 1,203/1,228 count conflict without claiming a fresh A01–A12 repair acceptance audit.

Source confirms bundled Noto Sans Thai/Myanmar TTF resources and print-font copy rules, correcting older “not confirmed bundled” language. OS/DPI, clean-machine and physical-print behavior remain unverified. Desktop LocalAppData paths and DataService ProgramData paths are separately recorded; service installation is not represented as completed desktop IPC cutover.

## 4. D02 — scaffold, Git, presentation and tooling

- Independent `.venv`, CPython **3.13.3 x64**, Zensical **0.0.71**, and **11** exactly versioned dependencies with SHA-256 wheel hashes. No Restaurant environment/package/configuration changed.
- Separate local Git repository on `main`; original approved plan retained unchanged. No remote or push/deployment automation configured.
- Explicit role/workflow navigation; breadcrumbs, page TOCs, linked next/previous navigation, code copy, Mermaid, search, system/light/dark appearance and a Premium icon/CSS identity.
- Nine reviewed public assets: one brand SVG, one stylesheet, four local Thai/Myanmar font files, one font license, and two historical Demo PNGs. All are physically present inside this repository; no application-tree links/imports are needed for normal builds.
- Strict staged build, generated-output validation, local artifact replacement only after success, retained previous local artifact, and source/output digest manifest. Preview uses a separate output directory.
- Foreground and hidden preview entry points with fixed loopback port, per-project logs/session identity, and a stop helper that verifies PID start time, command identity and descendants. Windows venv wrapper processes are accounted for; OS console hosts are left to exit with their clients.
- Publication is explicitly disabled. `deployment/README.md` documents the future isolated Caddy/tunnel boundary; there are no active deployment/service/task installers in this stage.

## 5. Validation performed

| Gate | Actual result |
| --- | --- |
| Environment | CPython 3.13.3 x64 and Zensical 0.0.71 verified. |
| Strict Zensical build | Passed: **No issues found**. |
| Source/register/navigation checks | **13 pages**, **13 explicit entries**, **9 reviewed assets**, **22 features**, **14 evidence records**; no errors. |
| Generated-output checks | **14 HTML pages** including 404, **33 output files**, **503 internal references**, **3 Mermaid blocks**, **2 search artifacts**; canonical URLs/sitemap/assets passed. |
| Regression tests | **19 passed**, including private paths/file types/credential signatures, encoded traversal, forbidden URL schemes, code-fence heading handling, broken generated links/anchors, asset tampering, and failed candidate preservation/cleanup. |
| Fresh dependency environment | Installed all 11 dependencies offline from the exact hashed wheels into `.build/repro-env`; `pip check` passed. A strict build also succeeded with that fresh interpreter. |
| Local page HTTP smoke | All 13 registered routes returned **200**; HEAD `/` returned **200**. |
| Missing/private routes | Missing page, `.git/config`, internal evidence JSON, and lockfile requests each returned **404**. |
| Preview lifecycle | Project-owned stop removed the 18181 listener; project-owned start restored it and all page checks passed. |
| Browser QA | Desktop 1280×800 and mobile 390×844 inspected; search “persistent Demo” produced six results and navigated to the workspace guide; mobile drawer opened; light/dark/system controls worked. |
| Visual content | Mermaid workspace process rendered; screenshot assets loaded; Thai/Myanmar samples rendered without placeholder boxes; no document-wide horizontal overflow in inspected views. Wide tables retain their own horizontal scroll. |
| Console errors | No page errors observed in the inspected browser log. |
| Isolation | All application file digests and existing infrastructure identities/config/tasks match. Restaurant remains healthy; concurrent reference-document changes and public-body digest drift are disclosed above. |

Machine-readable local evidence is retained in ignored `.build/validation.json`, `build-manifest.json`, `repro-validation.json`, `dependency-lock.json`, `preview-http-checks.json`, `isolation-comparison.json`, and `maintenance/snapshots/d00-before.json` / `d00-after.json`. These are execution records, not public site inputs. Preview startup logs/session state are also ignored.

## 6. Problems discovered and disposition

| Problem | Resolution / remaining limit |
| --- | --- |
| `py` reported no installed Python registrations; shell Python aliases were unsuitable evidence of a working environment. | Selected and tested the actual CPython executable; created an independent environment. Fresh setup requires an explicit interpreter path. |
| First heading validator counted shell comments inside fenced examples. | Corrected fenced-code handling and added regression cases. |
| Zensical 0.0.71 rejected the initial staging path arrangement. | Generated configuration stays at the project root with relative output paths; generated files are ignored. |
| `zensical serve --strict` is explicitly unsupported by the installed version. | Strict build is a separate enforced gate; preview is never claimed as the publication gate. |
| Windows virtual-environment launchers and hidden console hosts complicate process ownership. | Stop helper validates the owned descendant chain, preserves OS host processes, and was exercised with actual stop/restart. |
| Existing Restaurant active/example settings differ; Caddy origin behavior is historical. | Recorded the difference; no Restaurant fix attempted. New Caddy compatibility is a D06 requirement. |
| Old documentation status, font packaging and service-storage wording conflict. | Recorded precise evidence/limits; historical test count and font declarations reconciled; functional journey acceptance remains open. |
| Hash lock is platform-specific. | Supported/tested target is Windows x64 CPython 3.13. Other targets need a reviewed lock. |
| Two Restaurant documents changed and one archive input appeared during the task. | Recorded concurrent changes without touching/reverting them. All application files and existing infrastructure match the baseline; full Restaurant content immutability is not claimed. |

## 7. Remaining work and publication gates

1. **D03:** complete cashier/stock/production/payroll/manager/administrator task manuals, actual effective permission prerequisites, results/recovery steps and new sanitized captures where needed.
2. **D04:** complete technical/source references, schema/commands/financial invariants, application deployment/data/reset/hardware guidance; resolve each open documentation claim against focused current evidence. Historical test totals alone do not close these tasks.
3. **D05:** content review and complete site QA, source/asset privacy review, broader browser/accessibility checks, and publication-readiness assessment. D02 passing gates are scaffold gates, not a finished-manual release approval.
4. **D06:** a dedicated, versioned Caddy configuration/runtime on 18180 with admin on 18182, public-Host GET/HEAD tests, correct cache/compression/error behavior, immutable releases and exercised rollback.
5. **D07:** a new independent tunnel/configuration/credentials/metrics on 18183 and DNS route only after all local/content gates pass and account/zone access is established.
6. **D08:** uniquely named Premium startup tasks, runtime identity/ACLs/log retention, failure/reboot recovery and operational handoff.

No Git remote was supplied. Caddy/tunnel/runtime identity/DNS/startup work remains intentionally unimplemented. The preview remains running for local review and can be stopped with `scripts/Stop-Preview.ps1`.

## 8. Files created or updated

See [the complete project file inventory](files-created-d00-d02.md). `README.md` was updated from the planning entry point. The existing approved plan was preserved. All other listed implementation files were created for D00–D02. Ignored environments/build outputs/baseline snapshots are listed separately as local generated state.
