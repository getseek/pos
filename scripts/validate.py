"""Fail-closed documentation validation. Normal builds never read application inputs."""
from __future__ import annotations
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import tomllib
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
ALLOWED_MATURITY = {'DRAFT', 'REVIEWED', 'HISTORICAL'}
ALLOWED_EVIDENCE = {'source-inspected', 'reported', 'historical-automated', 'fresh-automated', 'manual', 'hardware'}
FORBIDDEN_EXTENSIONS = {'.py','.pyc','.ps1','.toml','.yaml','.yml','.trx','.db','.sqlite','.sqlite3','.pem','.key','.md','.cs','.csproj','.sql','.log','.zip'}
FORBIDDEN_PARTS = {'.git','.venv','maintenance','plans','scripts','software','__pycache__','private-review'}
SECRET_PATTERNS = [
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b'),
    re.compile(r'\b(?:ghp_|github_pat_)[A-Za-z0-9_]{24,}\b'),
    re.compile(r'(?i)\b(?:api[_-]?key|password|secret|tunnel_token)\s*[:=]\s*[\"\x27]?[A-Za-z0-9+/_=-]{16,}'),
]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_json(path: str):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))

def metadata(path: Path):
    text=path.read_text(encoding='utf-8')
    match=re.match(r'\A---\n(.*?)\n---\n',text,re.S)
    if not match:
        raise ValueError(f'{path.name}: missing YAML metadata')
    value=yaml.safe_load(match.group(1))
    if not isinstance(value,dict):
        raise ValueError(f'{path.name}: metadata must be a mapping')
    return value,text[match.end():]

def nav_paths(value):
    if isinstance(value,str):
        yield value
    elif isinstance(value,list):
        for child in value:
            yield from nav_paths(child)
    elif isinstance(value,dict):
        for child in value.values():
            yield from nav_paths(child)

def heading_count(text: str):
    """Ignore shell/Python comments inside fenced examples when counting H1s."""
    count=0;fence=None
    for line in text.splitlines():
        match=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line)
        if match:
            marker=match.group(1)
            if fence is None: fence=marker
            elif marker[0]==fence[0] and len(marker)>=len(fence) and not match.group(2).strip(): fence=None
            continue
        if fence is None and re.match(r'^# ',line): count+=1
    return count

def secret_findings(text: str):
    return [f'potential credential signature {i+1}' for i,p in enumerate(SECRET_PATTERNS) if p.search(text)]

def public_path_errors(relative: Path):
    errors=[]
    if any(p.lower() in FORBIDDEN_PARTS or p.startswith('.') for p in relative.parts):
        errors.append(f'private/hidden path in output: {relative.as_posix()}')
    if relative.suffix.lower() in FORBIDDEN_EXTENSIONS or relative.name.startswith('.env'):
        errors.append(f'forbidden output file type: {relative.as_posix()}')
    return errors

def source_fingerprint():
    inputs=[ROOT/'zensical.toml',ROOT/'project.json',ROOT/'requirements.lock']
    inputs+=sorted((ROOT/'maintenance').glob('*.json'))
    inputs+=sorted((ROOT/'.github/workflows').glob('*.yml'))
    inputs+=sorted(p for p in DOCS.rglob('*') if p.is_file())
    for folder in ('scripts','tests','overrides'):
        inputs+=sorted(p for p in (ROOT/folder).rglob('*') if p.is_file() and p.suffix in {'.py','.ps1','.cs','.csproj','.props','.Config','.html'})
    return {p.relative_to(ROOT).as_posix():digest(p) for p in inputs if p.is_file()}

def validate_source():
    errors=[]
    project=load_json('project.json')
    config=tomllib.loads((ROOT/'zensical.toml').read_text(encoding='utf-8'))['project']
    if config.get('docs_dir')!='docs' or config.get('site_dir')!='.build/site':
        errors.append('content/output roots must be docs and .build/site')
    if config.get('site_url')!=f"https://{project['domain']}/" or config.get('dev_addr')!=project['preview_address']:
        errors.append('canonical URL/preview address disagrees with project.json')
    if project['preview_address']!='127.0.0.1:18181' or project['ports']!={'origin':18180,'preview':18181,'admin':18182,'metrics':18183}:
        errors.append('approved isolation addresses/ports changed')
    if project.get('publication_enabled') is not False:
        errors.append('publication must remain disabled during local review')
    if not (ROOT/'requirements.lock').is_file():
        errors.append('hashed requirements.lock missing')
    else:
        requirements=[s for s in (ROOT/'requirements.lock').read_text().splitlines() if s.strip() and not s.startswith('#')]
        if not requirements or any('==' not in s or '--hash=sha256:' not in s for s in requirements):
            errors.append('each dependency must be pinned and hashed')
    evidence=load_json('maintenance/evidence-register.json')['evidence']
    evidence_ids=[e['id'] for e in evidence]
    if len(evidence_ids)!=len(set(evidence_ids)):
        errors.append('duplicate evidence IDs')
    for item in evidence:
        if item['kind'] not in ALLOWED_EVIDENCE or not re.fullmatch('[a-f0-9]{64}',item.get('sha256','')):
            errors.append(f"invalid evidence kind/digest: {item['id']}")
    features=load_json('maintenance/features.json')['features']
    feature_ids=[f['id'] for f in features]
    if len(feature_ids)!=len(set(feature_ids)):
        errors.append('duplicate feature IDs')
    for feature in features:
        if feature.get('source_review') not in {'located','source-reviewed'}:
            errors.append(f"invalid feature source-review status: {feature['id']}")
        if not feature.get('limitations') or not feature.get('source'):
            errors.append(f"missing source or verification limits: {feature['id']}")
        if not set(feature.get('evidence_ids',[]))<=set(evidence_ids):
            errors.append(f"unknown evidence reference: {feature['id']}")
        for source in feature.get('source',[]):
            if not re.fullmatch('[a-f0-9]{64}',source.get('sha256','')):
                errors.append(f"missing source digest: {feature['id']}")
        target=DOCS/feature['target_page']
        if feature['document_status']=='scaffolded' and not target.is_file():
            errors.append(f"scaffolded feature target missing: {feature['id']}")
    registry=load_json('maintenance/document-register.json')['documents']
    actual={p.relative_to(DOCS).as_posix() for p in DOCS.rglob('*.md')}
    paths=[d['path'] for d in registry]
    ids=[d['id'] for d in registry]
    if len(paths)!=len(set(paths)) or len(ids)!=len(set(ids)):
        errors.append('duplicate document register path/ID')
    if set(paths)!=actual:
        errors.append(f'document register mismatch; missing={sorted(actual-set(paths))}, phantom={sorted(set(paths)-actual)}')
    nav=list(nav_paths(config['nav']))
    if len(nav)!=len(set(nav)) or set(nav)!=actual:
        errors.append(f'navigation must include every page exactly once; missing={sorted(actual-set(nav))}, phantom={sorted(set(nav)-actual)}')
    for doc in registry:
        path=DOCS/doc['path']
        if not path.is_file(): continue
        try:
            meta,body=metadata(path)
            for key in ('id','revision','status'):
                if str(meta.get(key))!=str(doc.get(key)):
                    errors.append(f"{doc['path']}: metadata/register {key} mismatch")
            if meta.get('status') not in ALLOWED_MATURITY or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',str(meta.get('reviewed_on',''))):
                errors.append(f"{doc['path']}: invalid review date/maturity")
            if not set(meta.get('evidence',[]))<=set(evidence_ids) or not set(meta.get('features',[]))<=set(feature_ids):
                errors.append(f"{doc['path']}: unknown evidence/feature reference")
            if heading_count(body)!=1:
                errors.append(f"{doc['path']}: expected one H1")
            errors += [f"{doc['path']}: {e}" for e in secret_findings(body)]
        except (ValueError,yaml.YAMLError) as exc:
            errors.append(str(exc))
    assets=load_json('maintenance/assets.json')['assets']
    asset_paths=[a['path'] for a in assets]
    if len(asset_paths)!=len(set(asset_paths)):
        errors.append('duplicate asset registry paths')
    all_files=[p for p in DOCS.rglob('*') if p.is_file()]
    for p in DOCS.rglob('*'):
        if p.is_symlink() or (hasattr(p,'is_junction') and p.is_junction()) or not p.resolve().is_relative_to(DOCS.resolve()):
            errors.append(f'linked/escaping content path: {p.name}')
    actual_assets={p.relative_to(DOCS).as_posix() for p in all_files if p.suffix!='.md'}
    if actual_assets!=set(asset_paths):
        errors.append(f'asset register mismatch; unreviewed={sorted(actual_assets-set(asset_paths))}, missing={sorted(set(asset_paths)-actual_assets)}')
    for asset in assets:
        p=DOCS/asset['path']
        if asset.get('classification')!='public' or not asset.get('reviewed_on') or not asset.get('provenance') or not asset.get('license'):
            errors.append(f"asset review incomplete: {asset['path']}")
        if p.is_file() and digest(p)!=asset['sha256']:
            errors.append(f"unreviewed asset change: {asset['path']}")
        if p.suffix in {'.css','.svg','.txt','.js'} and p.is_file():
            errors += [f"{asset['path']}: {e}" for e in secret_findings(p.read_text(encoding='utf-8'))]
        if p.suffix.lower() in {'.py','.ps1','.toml','.yaml','.yml','.json','.db','.pem','.key'} or any(part.startswith('.') for part in Path(asset['path']).parts):
            errors.append(f"nonpublic asset type/path: {asset['path']}")
    import validate_review
    errors += validate_review.validate()
    return errors,{'pages':len(actual),'navigation_entries':len(nav),'registered_assets':len(assets),'features':len(features),'evidence_records':len(evidence)}

class HTMLPage(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True)
        self.ids=set();self.refs=[];self.canonical=[];self.mermaid=0;self.images=0
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        if tag=='a' and a.get('name'): self.ids.add(a['name'])
        for key in ('href','src','poster'):
            if a.get(key): self.refs.append((tag,key,a[key]))
        if tag=='link' and a.get('rel')=='canonical': self.canonical.append(a.get('href'))
        if 'mermaid' in a.get('class','').split(): self.mermaid+=1
        if tag=='img': self.images+=1

def resolve_reference(site:Path,current:Path,url:str,domain:str):
    parsed=urlsplit(url)
    if parsed.scheme in {'mailto','tel','data'}: return None,None
    if parsed.scheme and parsed.scheme not in {'http','https'}:
        raise ValueError(f'unsupported URL scheme: {parsed.scheme}')
    if parsed.netloc and parsed.hostname!=domain:
        return None,None
    decoded=unquote(parsed.path)
    if '\\' in decoded or '\x00' in decoded:
        raise ValueError('backslash/NUL in local URL')
    if not decoded:
        target=current
    elif decoded.startswith('/') or parsed.netloc:
        target=site/decoded.lstrip('/')
    else:
        target=current.parent/decoded
    target=target.resolve()
    if not target.is_relative_to(site.resolve()):
        raise ValueError('link escapes generated site')
    if target.is_dir(): target=target/'index.html'
    return target,unquote(parsed.fragment)

def validate_site(site:Path):
    errors=[];site=site.resolve();domain=load_json('project.json')['domain']
    if not site.is_dir(): return [f'generated site missing: {site}'],{}
    files=sorted(p for p in site.rglob('*') if p.is_file())
    parsed={}
    for p in site.rglob('*'):
        if p.is_symlink() or (hasattr(p,'is_junction') and p.is_junction()) or not p.resolve().is_relative_to(site):
            errors.append(f'linked/escaping output path: {p.name}')
    for p in files:
        relative=p.relative_to(site)
        errors+=public_path_errors(relative)
        if p.suffix=='.html':
            text=p.read_text(encoding='utf-8')
            parsed[p]=HTMLPage(text)
            errors += [f'{relative.as_posix()}: {e}' for e in secret_findings(text)]
    links=0
    for p,page in parsed.items():
        for tag,key,url in page.refs:
            try:
                target,fragment=resolve_reference(site,p,url,domain)
                if target is None:
                    if key in {'src','poster'} and urlsplit(url).netloc:
                        errors.append(f'{p.relative_to(site)}: remote runtime asset: {url}')
                    continue
                links+=1
                if not target.is_file(): errors.append(f'{p.relative_to(site)}: missing {key} target {url}')
                elif fragment and target in parsed and fragment not in parsed[target].ids:
                    errors.append(f'{p.relative_to(site)}: missing anchor {url}')
            except ValueError as exc: errors.append(f'{p.relative_to(site)}: {exc}: {url}')
    for p in [f for f in files if f.suffix=='.css']:
        text=p.read_text(encoding='utf-8')
        for url in re.findall(r'url\(\s*[\"\x27]?([^\)\"\x27]+)',text):
            try:
                target,_=resolve_reference(site,p,url,domain)
                if target is not None and not target.is_file(): errors.append(f'{p.relative_to(site)}: missing CSS asset {url}')
                elif target is None and urlsplit(url).netloc: errors.append(f'{p.relative_to(site)}: remote CSS asset {url}')
            except ValueError as exc: errors.append(f'{p.relative_to(site)}: {exc}')
    registry=load_json('maintenance/document-register.json')['documents']
    for doc in registry:
        relative=Path(doc['path'])
        html=(site/relative.parent/'index.html') if relative.name=='index.md' else (site/relative.with_suffix('')/'index.html')
        expected='https://'+domain+'/'
        route=html.relative_to(site).as_posix().removesuffix('index.html')
        expected+=route
        if html not in parsed: errors.append(f"registered page not generated: {doc['path']}")
        elif parsed[html].canonical!=[expected]: errors.append(f"canonical URL mismatch: {doc['path']}")
    for asset in load_json('maintenance/assets.json')['assets']:
        out=site/asset['path']
        if not out.is_file() or digest(out)!=asset['sha256']: errors.append(f"asset not copied intact: {asset['path']}")
    if not (site/'404.html').is_file(): errors.append('404 page missing')
    sitemap=site/'sitemap.xml'
    if not sitemap.is_file(): errors.append('sitemap missing')
    else:
        try:
            locations=[e.text for e in ET.parse(sitemap).iter() if e.tag.endswith('}loc')]
            if len(locations)<len(registry) or any(not s.startswith('https://'+domain+'/') for s in locations): errors.append('sitemap page count/domain mismatch')
        except ET.ParseError: errors.append('invalid sitemap XML')
    search_files=[p for p in files if 'search' in p.as_posix().lower() and p.suffix in {'.json','.js','.wasm'}]
    if not search_files: errors.append('search runtime/index missing')
    search_index=site/'search.json'
    if not search_index.is_file(): errors.append('search index missing')
    else:
        try:
            items=json.loads(search_index.read_text(encoding='utf-8'))['items']
            indexed={item['location'].split('#')[0] for item in items}
            expected_routes=set()
            for doc in registry:
                relative=Path(doc['path'])
                route=relative.parent.as_posix() if relative.name=='index.md' else relative.with_suffix('').as_posix()
                expected_routes.add('' if route=='.' else route+'/')
            missing=expected_routes-indexed
            if missing: errors.append('pages missing from search index: '+', '.join(sorted(missing)))
        except (ValueError,KeyError,TypeError): errors.append('invalid search index structure')
    return errors,{'html_pages':len(parsed),'internal_references_checked':links,'output_files':len(files),'mermaid_blocks':sum(p.mermaid for p in parsed.values()),'search_files':len(search_files)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site',type=Path)
    parser.add_argument('--report',type=Path)
    parser.add_argument('--check-freshness',action='store_true')
    args=parser.parse_args()
    try:
        errors,counts=validate_source()
        if args.site:
            site_errors,site_counts=validate_site(args.site)
            errors+=site_errors;counts.update(site_counts)
        if args.check_freshness:
            manifest=load_json('.build/build-manifest.json')
            if manifest['source_digests']!=source_fingerprint(): errors.append('validated build is stale; run Build-Docs.ps1')
            output={p.relative_to(args.site).as_posix():digest(p) for p in args.site.rglob('*') if p.is_file()}
            if output!=manifest['output_digests']: errors.append('generated output changed after validation; rebuild')
    except (OSError,ValueError,KeyError) as exc:
        errors=[f'validation input error: {exc}'];counts={}
    report={'ok':not errors,**counts,'errors':errors}
    if args.report:
        if not args.report.resolve().is_relative_to(ROOT/'.build'): raise ValueError('reports must be under project .build')
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 0 if not errors else 1

if __name__=='__main__': sys.exit(main())
