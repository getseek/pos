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
- `project.json` `publication_enabled` flips to `true` only after the owner
  confirms DNS and the first successful public verification sweep.
