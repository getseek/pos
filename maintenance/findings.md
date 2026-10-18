# Current documentation findings

Reviewed 2026-10-18. This is Premium's single active findings register; historical application audits remain evidence inputs.

| ID | Finding | Status and disposition | Evidence |
| --- | --- | --- | --- |
| PP-DOC-001 | Master document retains 1,203/open-audit language while a repair audit reports 1,228 passing tests. | Reconciled for historical count only: parsed final TRX files total 1,228. A01–A12 repair acceptance remains a dated claim until focused behavior review. | E-007, E-008, E-012–014 |
| PP-DOC-002 | Older text says Thai/Myanmar fonts are not confirmed bundled. | Source contradiction resolved: UI project declares bundled TTFs; Infrastructure copies print fonts. Physical rendering remains unverified. | E-004, E-005 |
| PP-DOC-003 | Desktop and DataService storage can be confused. | Source paths separated in orientation; service installation does not demonstrate desktop cutover. Runtime integration remains unverified. | E-001, E-003 |
| PP-DOC-004 | Main master document mixes current information and extensive historical archive. | Open: migrate selectively; never publish the master wholesale. | E-007; content-inventory.json |
| PP-DOC-005 | Restaurant example selects Caddy while active configuration selects Python. | Comparison recorded; do not copy operational configuration. Premium Caddy GET/HEAD/public-Host compatibility is a D06 gate. | restaurant-comparison.md |
| PP-DOC-006 | Three historical test files are excluded from compilation. | Disclosed; historical all-pass total does not include these files. Do not imply all source tests executed. | E-009 |
| PP-DOC-007 | No Git remote, public DNS or Premium runtime identity established. | Deferred to later phases; no remote, tunnel, task or public deployment is created in D02. | D00 snapshot; approved plan |
| PP-DOC-008 | Historical screenshots differ from current UI and cannot prove a workflow. | Publish only inspected synthetic Demo captures, visibly dated/limited; inventory remains outside publication. | E-011; future assets registry |
