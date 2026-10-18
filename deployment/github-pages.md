# GitHub Pages deployment — 18 October 2026

> **SUPERSEDED 19 October 2026** — the owner selected the Cloudflare Tunnel
> route for `docpremiumpos.getseek.net`; see `deployment/cloudflare-tunnel.md`.
> This document is retained as dated history. The GitHub workflow files remain
> inactive local preparation and are not part of the tunnel deployment.

The user selected **GitHub Pages**, repository **https://github.com/getseek/pos**, after local setup and checks. The approved original plan remains historical. This choice supersedes the planned Premium Caddy origin and Cloudflare Tunnel runtime. Existing Restaurant hosting remains independent and untouched.

The public repository was inspected through the GitHub API and Git refs: size 0, no refs, default branch main, Pages not enabled. No existing files need to be overwritten. No noninteractive GitHub credential was available on this machine during the access check. This document describes prepared deployment; it is not evidence of a successful GitHub run.

## What the workflow does

`.github/workflows/docs.yml` checks pull requests and main pushes. It uses Windows x64 and CPython 3.13, installs the exact hashed lock, builds strictly, validates the staged site, runs documentation regressions, and checks freshness. It uploads only `.build/site`, never the application, maintenance registries, credentials, scripts or local logs.

All actions are pinned to full commit IDs resolved from the official action repositories on 2026-10-18. Review and refresh those pins deliberately. The source analysis helper is optional and is not run by CI; CI builds solely from frozen local registries.

Publication is a separate job, only for a manual workflow run with **publish=true on main**, after validation succeeds. That job uses `pages: write` and `id-token: write`, a `github-pages` environment, and the official artifact/configure/deploy actions. Ordinary saves, pushes and pull requests do not publish. GitHub environment protection can add an owner-controlled release gate.

## Initial repository setup

1. Authenticate Git with an account that can write `getseek/pos`. Authenticate through Git Credential Manager or an approved GitHub CLI flow; do not paste a token into documentation or shell history.
2. Confirm the selected repository is still empty before the first push. Push the standalone documentation repository's main branch without force or unrelated-history replacement.
3. In repository Settings → Pages, choose **GitHub Actions** as the build source. Configure the `github-pages` environment and main-branch protection as needed.
4. Confirm the validation workflow succeeds remotely. Local passing checks are not a substitute for this first CI run.
5. Configure the custom domain only after its DNS ownership and routing are ready. Add the project CNAME asset and Pages custom-domain setting as one reviewed change; no CNAME was added during local preparation to avoid redirecting a working GitHub URL to unconfigured DNS.
6. Run the workflow manually with **publish=true**. Inspect its environment URL and deployment status.
7. Verify every route, assets, search, diagrams, HTTPS and canonical URLs on the deployed hostname. A successful workflow alone does not prove DNS or certificate readiness.

The intended canonical domain remains `docpremiumpos.getseek.net`. Do not alter the Restaurant hostname, tunnel, origin, Caddy settings or scheduled tasks. Premium ports 18180–18183 remain reserved historical isolation settings; only loopback preview 18181 is running locally.

## Search, reading and public content

Every registered public Markdown page must be generated, linked in navigation and represented in `search.json`. All review sections and source-location catalogues are readable on the website. Search is local to the generated site and needs no account or search service. Mermaid is vendored with a pinned integrity-checked asset, so diagrams need no external renderer download.

Source-location metadata is intentionally published. Raw application source, credentials, live shop data, TRX and local logs remain outside the site artifact. The user authorized public access to reviewed documentation; this does not turn historical/planned or unverified behavior into implemented capability.

## Rollback and later changes

Keep a known-good Git revision and CI artifact. Re-run a validated prior revision to republish it. For domain problems, diagnose Pages/DNS separately before changing application or Restaurant infrastructure. For documentation problems, fix Markdown or the registry and repeat all checks. Browser review choices are local drafts; they never execute application changes.

Reference: [GitHub's custom Pages workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
