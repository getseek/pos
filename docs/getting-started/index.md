---
id: PP-START-001
revision: "1.0"
status: DRAFT
reviewed_on: "2026-10-18"
evidence: ["E-010", "E-001", "E-002"]
features: ["PP-F001", "PP-F002"]
---

# Requirements and launch

<div class="meta">DRAFT · source review 18 October 2026 · documentation foundation D02</div>

The current application is a Windows desktop POS built with .NET 10, Avalonia 11 and SQLite. The source launcher is a development workflow, not a self-contained installer.

## Before launching from source

| Requirement | What to check |
| --- | --- |
| .NET SDK | A stable .NET 10 SDK selected by `Software/global.json`; Runtime-only installation cannot compile the project. |
| Complete source | Keep project references, SQL migrations, native dependencies and font assets together. |
| Package restore | The first restore normally needs network access. An existing offline NuGet source points to a machine-specific Visual Studio directory and may need review on another computer. |
| Workspace choice | Decide whether you are opening operational Real Shop data, persistent Demo, or the legacy in-memory preview. |
| Hardware | Printer drivers, queue selection and physical output require their own checks. |

The SDK policy requests `10.0.100`, allows later stable .NET 10 feature bands with `latestFeature`, and rejects prereleases. A matching SDK must be selected from inside the application's `Software` directory.

## Inspect the development environment

These commands are application-development references. They are not run by this documentation project:

```powershell
# Run from the application's Software directory.
dotnet --list-sdks
dotnet --version
```

Use the application's `Start_GetSeek_POS.bat` entry point or an explicit workspace command only when you intend to start that application. Review [Real Shop and Demo](workspaces.md) first. No application build, database migration, reset, or real sale was executed while creating this documentation foundation.

## If setup fails

- If the SDK cannot be selected, inspect `dotnet --version` from `Software` and the checked-in SDK policy.
- If restore reports `NU1301` for an absent Visual Studio offline-package directory, inspect that source in the destination copy's NuGet configuration. Retain nuget.org; do not conceal warnings or disable package auditing to make a build appear successful.
- If an existing shop unexpectedly shows initial Admin setup, stop and review the selected Windows user and data paths before provisioning a replacement shop.

For the actual solution structure, see [application architecture](../development/index.md). Clean-machine application installation remains a separate verification task.
