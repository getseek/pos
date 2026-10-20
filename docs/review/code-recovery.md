---
id: PP-REVIEW-CODE-RECOVERY
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-20"
evidence: ["E-015"]
features: []
---

# GetSeek.Recovery source catalogue

<div class="meta">DRAFT · code snapshot 20 October 2026 · source review and targeted automated checks</div>

Every application C# file in this project is listed below, with a frozen SHA-256 and one row per method declaration. **Calls are unique invocation syntax names with the first observed line, not resolved callee edges.** Overloads, extension methods, dependency injection, reflection and runtime branches require manual/semantic review. SQL line numbers identify string literal starts. Constructors, property bodies and AXAML events are not method declarations in this extractor.

Project: [GetSeek.Recovery.csproj:1](code-recovery.md#src-b243c08d1014). Dependencies: <code>GetSeek.Infrastructure</code>, <code>GetSeek.Application</code>, <code>GetSeek.Domain</code>.

## Program.cs {#src-84079254141c}

<code>Software/src/GetSeek.Recovery/Program.cs</code> · 2 lines.

SHA-256: <code>9e33f889e8187d1b4c18d6ce2196d5e1cb05353d0991092381b066b16398dee9</code>.

Declarations: .

## AXAML, migrations and project inputs

### GetSeek.Recovery.csproj {#src-b243c08d1014}

<code>Software/src/GetSeek.Recovery/GetSeek.Recovery.csproj</code> · 16 lines · SHA-256 <code>a9a5ce417830150f1f874ebdb11cf9b956745692c60f13665e1a0fc1792cbe1d</code>.
