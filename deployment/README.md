# Deployment boundary at D02

No public deployment is implemented or enabled. Do not point a web server at the project root or `docs/`.

The approved future topology is public HTTPS → a **new** named Cloudflare Tunnel → Caddy on `127.0.0.1:18180` → a validated static release in `C:\ProgramData\GetSeekDocs\PremiumPos`. Dedicated Caddy admin: `127.0.0.1:18182`; dedicated tunnel metrics: `127.0.0.1:18183`.

D06 must validate a Premium-specific Caddy configuration, including GET/HEAD requests with `Host: docpremiumpos.getseek.net`, 404/error handling, compression, cache behavior, dotfile/source denial, and rollback. The Restaurant config's host matcher must not be copied. Locate or install a versioned executable without changing the existing installation.

D07 requires successful local/content gates, its own tunnel UUID, protected credentials outside Git, an explicit independent configuration path and a newly checked DNS route. D08 adds uniquely named startup tasks with a verified runtime identity, ACLs and reboot recovery.

No Caddyfile, tunnel credentials, service installer or task registration is invoked by the D02 scripts. Public release readiness is separate from a successful local scaffold build. See `maintenance/restaurant-comparison.md` and the approved plan before implementing later phases.
