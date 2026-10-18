# D00 infrastructure baseline

Captured UTC: `2026-10-18T03:11:45.5929300+00:00`. User timezone: Asia/Bangkok.

The machine-readable record is `snapshots/d00-before.json`. It stores SHA-256 digests, sanitized process identity and route/health observations, not credential contents or process command lines.

| Check | Result |
| --- | --- |
| Restaurant preview, loopback 8000 | HTTP 200; expected Restaurant Dashboard title. |
| Restaurant origin, loopback 8001 | HTTP 200; expected Restaurant Dashboard title. |
| Restaurant public HTTPS | HTTP 200; expected Restaurant Dashboard title. |
| Premium public DNS | NXDOMAIN at capture; no public route created. |
| Premium ports 18180–18183 | No listeners/exclusions; exclusive bind probes passed and immediately released. |
| Protected Restaurant source/config files | 55 file digests captured. |
| Protected application inputs | 2417 file digests captured, including source/assets/tests/guides; generated bin/obj/test-result/runtime trees excluded. |
| External tunnel/Caddy configuration | Digests captured for existing files; contents not copied into Premium publication. |
| Matching scheduled tasks/startup entries | 0 / 0; queries do not establish all possible startup mechanisms. |
| Existing Caddy executable | `v2.11.7`; located, not started or reconfigured. |
| Existing cloudflared executable | `cloudflared version 2026.10.1 (built 2026-10-15T09:15 UTC)`; located, not restarted. |

Compare a fresh end-of-D02 snapshot against these digests, protected listener owners, task definitions and HTTP health. Runtime-generated HTML can differ in body hash without a source change; use title/status and protected source digests together.

See [the implementation comparison](restaurant-comparison.md) for reusable patterns and deliberate differences. The effective Restaurant process startup mechanism and historical Caddy behavior remain investigation items for operational work; neither prevents isolated local scaffolding.
