# Premium POS documentation

Standalone project: **F:\Premium_POS_docs**. Canonical target: **https://docpremiumpos.getseek.net/**. Current scope: **D00–D02 complete, plus the authorized source review atlas; local only**.

Zensical + Markdown + Git form the authoring/build system. The user selected GitHub Pages at `getseek/pos` for hosting on 18 October 2026; this supersedes the planned Premium Caddy and Cloudflare Tunnel runtime. See `deployment/github-pages.md`. No public DNS, tunnel, task, or Restaurant configuration is changed by the D02 scripts.

## Start locally

Use PowerShell from this directory. The existing `.venv` is isolated from the Restaurant project. On a fresh checkout, supply an actual CPython 3.13 x64 interpreter:

```powershell
.\scripts\Initialize-Environment.ps1 -PythonPath 'C:\Path\To\Python313\python.exe'
.\scripts\Check-Environment.ps1
.\scripts\Build-Docs.ps1
.\scripts\Validate-Docs.ps1
.\scripts\Test-Docs.ps1
.\scripts\Preview-Docs.ps1
```

Preview: **http://127.0.0.1:18181/**. For a hidden, project-owned preview use `scripts/Start-Preview.ps1`; inspect `.build/preview.stderr.log` and stop it with `scripts/Stop-Preview.ps1`. These commands never manage Restaurant processes. The current lock targets Windows x64 / CPython 3.13 / Zensical 0.0.71; dependencies are exact and hashed.

## Project map

| Location | Purpose |
| --- | --- |
| `docs/` | The only publishable authored content root: Markdown and reviewed local assets. |
| `zensical.toml` / `project.json` | Site navigation/presentation and checked isolation settings. |
| `maintenance/` | Source, evidence, feature, document and asset registers; comparison, findings and completion reports. |
| `scripts/` / `tests/` | Staged builds, reference generation, validation, dependency setup and preview lifecycle. |
| `.build/` | Ignored staged/validated/previous/preview output, manifests, lock wheels, reports and local logs. |
| `deployment/` | Explicit boundary and prerequisites for future isolated Caddy/tunnel hosting. |
| `plans/` | The original approved implementation plan, retained as dated history. |

All normal build/validation/preview operations use only this repository. Application and Restaurant references were read for discovery; they are not runtime or build dependencies. Fonts and the two reviewed historical Demo screenshots have been copied into this project with provenance/license records.

## Source of truth and validation

`maintenance/features.json` connects stable workflow IDs, roles, source entry-point hashes, evidence IDs, guide targets and limitations. `maintenance/evidence-register.json` distinguishes source inspection, reported claims and historical automated results. `document-register.json` and `assets.json` govern public pages and reviewed assets. The feature-status and document-register website pages are derived by `scripts/render_registry.py`.

Builds render reference views, validate source, run a strict staged Zensical build, check generated links/anchors/assets/canonical URLs/search/output safety, and only then replace `.build/site`. The previous local artifact remains in `.build/previous`. `Validate-Docs.ps1` also detects stale inputs or altered output. No website is published by a build or preview save.

For an explicit dependency update, review `requirements.in`, use a disposable project environment and run `scripts/lock_dependencies.py --update`; inspect the complete lock and repeat a fresh install, build and regression checks. Normal builds do not resolve new package versions.

## Source review atlas

Open [the local review atlas](http://127.0.0.1:18181/review/) for 25 workflow maps, runtime/command/access diagrams, all 172 handled command routes, 137 reconstructed tables, source catalogues, errors and browser-only change choices. This is source evidence with explicit analysis limits, not blanket application acceptance. The full source snapshot and review configuration live under `maintenance/`; ordinary builds read only this repository. The optional Roslyn helper requires .NET 10 only for an explicit read-only source refresh.

See `docs/review/method.md` for reproduction and `maintenance/review-completion-report.md` for validations and remaining work. Application source, real databases, Restaurant infrastructure and public deployment remain outside this work.

## Implementation records

- [Approved implementation plan](plans/documentation-site-zensical-caddy-cloudflare-plan-2026-10-18.md)
- [Restaurant implementation comparison](maintenance/restaurant-comparison.md)
- [D00 baseline](maintenance/d00-baseline.md)
- [D01 inventory summary](maintenance/d01-summary.md)
- [D00–D02 completion report](maintenance/d02-completion-report.md)
- [Workflow coverage](maintenance/coverage-matrix.md)
- [Evidence register](maintenance/evidence-register.md)
- [Current findings](maintenance/findings.md)

Reserved Premium ports: **18180** origin, **18181** preview, **18182** admin, **18183** metrics. Existing Restaurant ports 8000/8001 and its tunnel remain separate. See the completion report for actual checks and remaining work.

Latest scope instruction: finish local documentation first; GitHub deployment remains inactive. The prepared workflow is retained for later use and has not run remotely.
