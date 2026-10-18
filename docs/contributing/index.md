---
id: PP-CONTRIB-001
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: []
features: []
---

# Authoring and validation

<div class="meta">DRAFT · source review 18 October 2026 · documentation foundation D02</div>

## Maintain a traceable page

1. Identify the business task, audience, source entry points and relevant evidence IDs.
2. Create a focused Markdown page with a stable `PP-*` ID, revision, DRAFT/REVIEWED/HISTORICAL maturity, review date, evidence list and feature list.
3. Add the page to `maintenance/document-register.json` and explicit TOML navigation. Every public page must appear exactly once.
4. Update the feature coverage record without converting located code or old test results into fresh verification.
5. Review screenshots/assets, provenance, classification, license and digest in `maintenance/assets.json` before adding them under `docs/`.
6. Build, validate, run the validator regression checks and inspect the affected preview pages before a local Git commit.

## Write useful workflow instructions

Task pages should state purpose, prerequisites/effective permissions, numbered steps, expected recorded result, recovery guidance, and Real/Demo differences. Prefer sanitized examples. Distinguish record creation from payment, queued output from physical success, and a source snapshot from current runtime evidence.

Do not copy archived specifications or large audit logs into public content. Internal registers remain outside `docs/`; generated reference views expose only their intended public fields. Keep the original approved plan as dated history.

## Automated gates

The local validator checks navigation/register coverage, metadata and evidence references, approved asset digests, forbidden file types/paths, credential signatures, linked content, generated links/anchors, CSS assets, canonical URLs, sitemap, search artifacts and stale/modified builds. It does not establish business correctness or prove that every possible sensitive string has been recognized; explicit asset/output review remains part of the publishing process.

```powershell
.\scripts\Build-Docs.ps1
.\scripts\Validate-Docs.ps1
.\scripts\Test-Docs.ps1
git status --short
```

No Git remote or push automation is configured. Review [documentation operations](../operations/index.md) before changing dependencies or local preview behavior.
