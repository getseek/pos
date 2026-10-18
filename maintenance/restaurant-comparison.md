# Restaurant implementation comparison — D00

Reviewed: 2026-10-18 (Asia/Bangkok). Reference: `F:\rust_restaurant`, read-only.
This comparison was completed before Premium scaffolding or new infrastructure was created.

## Observed implementation

- Zensical **0.0.71**, Python virtual environment, explicit TOML navigation, semantic Markdown, admonitions, Mermaid, linked tabs, code-copy controls, breadcrumbs, section navigation and three-way light/dark/system appearance.
- Stable document IDs, document register, one authoritative findings register, status/authority separation, immutable review evidence, and requirements-to-architecture traceability.
- The Restaurant content concerns an architecture-stage Rust system. Its current review register states implementation has not started. Those product claims and Rust-specific approval gates do not apply to the existing .NET Premium application.
- Actual `.env.docs`: loopback preview **8000**, static origin **8001**, `STATIC_SERVER=python`, automatic build enabled, rollback enabled. Its example still says `STATIC_SERVER=caddy`; do not confuse the example with the active setting.
- The Python origin supports GET/HEAD, restricts traversal/dotfiles/listing, and also exposes a `/raw/` Markdown route. The watcher stages builds, checks exit status/index/page count, then swaps directories with retry and rollback. It watches Markdown/configuration, but not all image/CSS dependencies.
- A Caddy 2.11.7 executable and a Restaurant JSON configuration exist. No active Caddy process was found. The JSON has a `127.0.0.1` host matcher. Configuration comments report an empty-200 issue through Cloudflare; this pass did not start Caddy or reproduce that historical failure. A forwarded public Host differing from that matcher is a hypothesis to test in Premium D06, not a diagnosed Restaurant defect.
- Existing `cloudflared` 2026.10.1 and the user configuration route `docrestaurant.getseek.net` to port 8001. Do not use that file as Premium configuration.
- The checked task/startup queries returned no matching registered tasks or Win32 startup entries. That does not prove there is no other startup mechanism; preserve the running processes and confirm the effective mechanism before any later operational change.
- The repository has a GitHub Pages deployment workflow with floating package installation. Premium has no remote and will use its own Caddy/tunnel deployment; that workflow is not copied.

## Reuse and adaptation decisions

| Element | Premium decision | Reason |
| --- | --- | --- |
| Explicit navigation and registered documents | Reuse with role/workflow groups and stable `PP-*` IDs. | Keeps every published page discoverable and traceable. |
| Status and evidence discipline | Reuse; separate document maturity, source inspection, historical automated results, manual checks, hardware checks and owner approval. | The current product exists; an architecture or test claim must not become blanket product acceptance. |
| Presentation | Reuse semantic Markdown, light/dark/system, breadcrumbs, code copy, Mermaid and readable tables; add a restrained indigo/teal Premium identity. | Familiar documentation experience, independent branding. |
| Staged builds/rollback | Reuse the principle; strengthen validation beyond a hard-coded 30-page threshold. | Validate expected pages, navigation, links/anchors, assets, metadata and output safety. |
| Build environment | Pin Zensical 0.0.71 for a comparable baseline, plus exact transitive dependencies and artifact hashes. | Reproducible, isolated installation. |
| Runtime configuration | Dedicated project, environment, build/cache directories and ports 18180–18183. | No shared mutable state or process management. |
| Static hosting | Preserve the approved Caddy plan; defer live Caddy to D06 and test GET/HEAD with the public Host header. | Restaurant currently uses Python; do not silently change Premium's stack. |
| Automatic publisher | Do not copy/start the Restaurant watcher. | D02 is local scaffolding only; a preview save must not publish anything. |
| Source serving | No `/raw/` endpoint, directory browsing, or source-root serving. | Only validated generated output is eligible for future hosting. |
| Destructive shell helpers | Do not copy `cmd /c rmdir` cleanup or broad process-stop helpers. | Restrict cleanup and process ownership to Premium-created state. |
| CI and publication | Provide local validation first; defer remote CI, DNS, tunnel creation and startup registration. | No remote was supplied and public deployment is outside D00–D02. |

## Isolation contract

Only `F:\Premium_POS_docs` is writable project state. `F:\Premium_POS` and `F:\rust_restaurant` are read-only analysis inputs. No shared virtual environment, Caddy admin endpoint, tunnel credentials, task names, ports, logs or output directories. No Caddy or tunnel processes are started in D02. Future runtime files belong in `C:\ProgramData\GetSeekDocs\PremiumPos`.

The original approved plan remains a dated planning record. This comparison and the D02 report record current execution facts and differences.
