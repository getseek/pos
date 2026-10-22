# Cloudflare Tunnel deployment — 19 October 2026

The owner selected the **Cloudflare Tunnel** route for
`https://docpremiumpos.getseek.net/`, mirroring the existing Restaurant
hosting. This **reverses the GitHub Pages selection of 18 October 2026**
(`deployment/github-pages.md`, retained as dated history). The approved
original Caddy plan in `plans/` also remains historical. Existing Restaurant
hosting (tunnel `getseek-docs`, origin `127.0.0.1:8001`) stays independent
and untouched.

## Approved topology

```
public HTTPS  docpremiumpos.getseek.net
      │  (proxied CNAME, owner-created DNS)
      ▼
new named Cloudflare Tunnel  premium-pos-docs   (own UUID, own credentials;
      │                                           config: ~/.cloudflared/config-premium.yml)
      ▼
Python stdlib static origin  127.0.0.1:18180  (GET/HEAD only, no listing,
      │                                        dotfiles/traversal denied)
      ▼
validated static release     F:\Premium_POS_docs\.build\site
```

- **Origin choice**: the Restaurant comparison (PP-DOC-005) established the
  active Restaurant origin is the Python static server (`STATIC_SERVER=python`);
  Caddy showed an empty-200 defect behind cloudflared and is not used. Premium
  follows the proven Python origin on the reserved origin port 18180. The
  reserved ports 18182/18183 remain unused.
- **Public, no Access**: the owner selected a fully public site (matching
  Restaurant). DNS proxying is not authentication; there is no Access
  application in front.
- **Build before serve**: only `.build/site` produced by
  `scripts/Build-Docs.ps1` + `Validate-Docs.ps1` is served — never the repo,
  never `docs/` directly. `zensical.toml` already carries the public
  `site_url` (`https://docpremiumpos.getseek.net/`), so canonical URLs and the
  sitemap are correct for this host.
- **Credentials**: tunnel UUID credentials live only under
  `~/.cloudflared/` (outside Git, referenced by path).
- **DNS**: the owner creates the single CNAME record
  (`docpremiumpos` → `<premium-tunnel-uuid>.cfargotunnel.com`, proxied).
  No DNS record, zone or Restaurant configuration is created or modified by
  any Premium script in this repository.

## Boundaries

- Premium uses its **own** tunnel UUID and its **own** config file; the
  Restaurant `~/.cloudflared/config.yml`, tunnel and origin are never edited
  or restarted by Premium operations.
- No Caddy installation, service, scheduled task or startup entry is created
  by this decision. Permanent startup automation remains a separate,
  explicitly approved future step.
- `project.json` `publication_enabled` is governed by the repository's own
  validator invariant (`publication must remain disabled during local
  review`): it remains `false` until the owner advances the review stage or
  explicitly amends that rule. Tunnel serving is independent of this flag —
  the live site at `docpremiumpos.getseek.net` does not read it.

## Runtime record (owner-ordered cleanup + full recheck, verified 2026-10-22)

Session-spawned services were killed at the owner's request and the stack was
rebuilt purely on the logon wrappers:

| Component | Launch | Detail |
|---|---|---|
| Origin | `Startup\GetSeekDocs-Premium-Origin.cmd` → `python serve_site.py 18180 F:\Premium_POS_docs\.build\site` | loopback-only; GET/HEAD; dir→index; custom 404 body; PUT 405; dotfiles/traversal/listing blocked |
| Tunnel | `Startup\GetSeekDocs-Premium-Tunnel.cmd` → `cloudflared --config config-premium.yml tunnel run premium-pos-docs` | metrics `127.0.0.1:20242`; QUIC edges bkk/sin; own UUID `ff21cfb3…` |

- **Longevity evidence**: the tunnel+origin served continuously 2026-10-19 →
  2026-10-22 (logs show real crawler/asset traffic). QUIC idle-timeout
  terminations observed and self-healed (re-registration within seconds) —
  normal, not defects.
- **Recorded lesson**: processes spawned from agent sessions die when the
  session restarts — the Startup wrappers (Explorer/logon context) are the
  durable mechanism. Full reboot proof remains the pending final test.
- **Recheck sweep 2026-10-22**: homepage, sections, search index (1.76 MB),
  sitemap → 200; custom 404 → 404 with built page; PUT → 405; tunnel
  counters matched all 8 probes exactly (6×200, 1×404, 1×405).
- **Cloudflare Email Obfuscation** rewrites every HTML page (≈1.3 KB script
  before `</body>`); live bytes are otherwise byte-identical to `.build/site`.
  Disable per-hostname in the dashboard if byte-exactness or crawler-visible
  emails matter.
- **cloudflared 2026.10.1** in use; the edge now recommends **2026.10.3** —
  upgrade pending owner approval (system software).
- **GitHub Pages mirror**: prepared but inactive; pushes currently blocked by
  an expired GitHub credential (owner re-auth required); last pushed state
  `3d2c175`, local `main` ahead.
