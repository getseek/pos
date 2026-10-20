---
id: PP-REVIEW-METHOD
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: []
---

# Methodology and refresh

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

## What was checked

- Every C# file under `Software/src` and `Software/tests`, excluding generated `bin`, `obj` and test-output directories, was parsed using the installed .NET SDK's Roslyn syntax libraries. No application project was compiled or loaded.
- Type bases identify typed handler declarations. Explicit `new CommandType(...)` sites identify potential producers; they do not prove dispatch or reachability. Handler methods are matched by their first parameter type.
- Method-body invocation names, uppercase literal `Failure(...)` codes, throw statements and literal SQL table references were extracted. Repeated invocation syntax names in a method are deduplicated with the first line retained.
- SQL references are filtered to reconstructed table names. Interpolated SQL is flagged for manual review. Aliases, views, triggers, nested helper effects, generated SQL and dynamic dispatch are not semantically resolved.
- AXAML inventory covers literal `Command="{Binding ...}"` attributes. Code-behind events, data-context resolution and runtime binding errors require a separate UI check.
- Project edges come from project-reference declarations. Database edges come from SQLite foreign-key metadata after in-memory SQL replay.
- Startup flags, pipeline boundaries, first-run provisioning, service ownership, error reporting and worker failure handling received selected manual source inspection. Broad cataloguing does not imply every method received a manual correctness audit.

Roslyn syntax trees describe declarations and syntax; semantic models are a separate analysis step. [Microsoft's syntax-analysis documentation](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/get-started/syntax-analysis) explains this distinction.

## Reproduce an explicit source refresh

Ordinary documentation builds use frozen JSON registries and never read the application. Refresh is a deliberate read-only analysis operation from `F:\Premium_POS_docs`:

```powershell
dotnet restore .\scripts\source-indexer\SourceIndexer.csproj --configfile .\scripts\source-indexer\NuGet.Config
dotnet build .\scripts\source-indexer\SourceIndexer.csproj -c Release --no-restore
dotnet .\.build\source-indexer\bin\Release\net10.0\SourceIndexer.dll F:\Premium_POS .\.build\code-index.raw.json
.\.venv\Scripts\python.exe -B .\scripts\refresh_review.py --application-root F:\Premium_POS --raw-index .\.build\code-index.raw.json
```

The analysis helper targets .NET 10 and references SDK-bundled Roslyn assemblies; it has no NuGet package dependency and clears package feeds. Its build outputs live under the documentation `.build` directory. A .NET 10 SDK is required only for source refresh, not normal documentation builds. Python replays migration SQL only into `:memory:` and rejects a documentation root inside the app.

After refresh, review changed hashes and extraction limits, update source-linked workflow/decision records and E-015's digest, then run the standard build, validation and documentation tests. Do not rerun the one-time configuration initializer as a substitute for a source review. Changed source can invalidate manually reviewed conclusions even when syntax still parses.

## Diagram runtime

Mermaid 11.17.2 is vendored from an official npm tarball verified against its SHA-512 integrity. The asset and MIT license are registered by SHA-256; a small theme override loads it before the theme so the floating external CDN loader is not used. Flowcharts retain intrinsic dimensions inside a horizontally scrollable region instead of shrinking long technical labels. [Mermaid usage guidance](https://mermaid.js.org/config/usage.html) describes local hosting and renderer initialization.

## Safety and publication

Only metadata and reviewed diagrams are rendered. Full source, raw syntax output, databases, PINs, tokens, logs and TRX are outside `docs/`. Validation checks all registered source paths/line ranges/digests, command coverage, foreign-key endpoints, decision options, page metadata, navigation, links and assets. A source snapshot is a dated reference, not a runtime import or continuous assertion about the live app.

The website remains a loopback preview on port 18181. The user selected GitHub Pages at getseek/pos after local checks; the prepared workflow publishes only on an explicit manual run after validation. Repository authentication, Pages/domain settings and a successful remote deployment remain separate evidence. Application fixes, application test execution and physical-device acceptance are not performed by the review pages or their choice controls.
