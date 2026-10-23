# Import preview cleanup — Patch A, 23 October 2026

Maturity: IN REVIEW. Owner acceptance pending.

Three production ViewModel files changed: MainViewModel.cs, MainViewModel.ImportReview.cs and MainViewModel.ThirdPartyImport.cs. One new test file: ImportReviewLifecycleTests.cs. Import command handlers, workbook parsers/templates, pricing and database schema were not changed.

The import dialogs now discard completed preview state after successful confirmation; existing imported records, status notification and completed XLSX download request remain. Cancel/replacement clears backing and paged rows. Command rejection retains input and error details. Failure XLSX support is a separate pending patch.

Fresh checks: baseline 24 passed; six new regression cases before fix: 4 failed, 2 passed; after fix: 30 passed, 0 failed. Initial sandbox testhost failed to connect; successful runs used unsandboxed execution. Raw TRX, logs, backups and patch are outside public docs in F:/Premium_POS/artifacts/import-preview-cleanup/20261023-111339. E-022 pins the final TRX. This is not full-suite, manual shop, native file dialog, physical-device or owner verification.

PP-F013 and PP-F014 and PP-MAP-IMPORTS link the inspected source and tests. Checkout/service-style rule source anchors were re-inspected after MainViewModel line shifts; their runtime status remains source-only. Derived pages are regenerated, not edited manually. Existing unrelated pending UI/test documentation changes are preserved.
