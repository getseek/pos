"""Local-only staged builds and preview; no public deployment operations."""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import importlib.metadata
import json
from pathlib import Path
import re
import shutil
import socket
import subprocess
import sys
import uuid
import validate

ROOT=Path(__file__).resolve().parents[1]
BUILD=ROOT/'.build'

def run(command):
    subprocess.run([str(c) for c in command],cwd=ROOT,check=True)

def clean_owned(path:Path):
    resolved=path.resolve()
    if resolved.parent!=BUILD.resolve() or path.name in {'site'} or path.is_symlink() or path.is_junction():
        raise ValueError(f'unsafe cleanup target: {path}')
    if resolved.exists(): shutil.rmtree(resolved)

def create_config(path:Path,site:Path):
    text=(ROOT/'zensical.toml').read_text(encoding='utf-8')
    # Zensical 0.0.71 resolves project boundaries from the configuration location.
    # Keep generated configurations at the project root and all paths relative.
    if path.parent!=ROOT or not site.resolve().is_relative_to(BUILD.resolve()):
        raise ValueError('generated configuration/output outside project boundaries')
    text=re.sub(r'(?m)^site_dir = .*$',lambda _: 'site_dir = '+json.dumps(site.relative_to(ROOT).as_posix()),text)
    path.write_text(text,encoding='utf-8',newline='\n')

def build():
    BUILD.mkdir(exist_ok=True)
    run([sys.executable,'-B',ROOT/'scripts/render_registry.py'])
    errors,_=validate.validate_source()
    if errors: raise ValueError('\n'.join(errors))
    candidate=BUILD/('candidate-'+uuid.uuid4().hex)
    config=ROOT/('.premium-build-'+uuid.uuid4().hex+'.toml')
    create_config(config,candidate)
    try:
        run([sys.executable,'-m','zensical','build','--clean','--strict','--config-file',config])
        errors,counts=validate.validate_site(candidate)
        if errors: raise ValueError('\n'.join(errors))
        manifest={'built_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version.split()[0],'zensical':importlib.metadata.version('zensical'),'source_digests':validate.source_fingerprint(),'output_digests':{p.relative_to(candidate).as_posix():validate.digest(p) for p in candidate.rglob('*') if p.is_file()},'counts':counts}
        site=BUILD/'site';previous=BUILD/'previous'
        if previous.exists(): clean_owned(previous)
        if site.exists(): site.rename(previous)
        try: candidate.rename(site)
        except OSError:
            if previous.exists() and not site.exists(): previous.rename(site)
            raise
        (BUILD/'build-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'ok':True,'local_artifact':str(site),'counts':counts,'public_deployment':False}))
    finally:
        if candidate.exists(): clean_owned(candidate)
        config.unlink(missing_ok=True)

def preview():
    BUILD.mkdir(exist_ok=True)
    project=validate.load_json('project.json')
    address=project['preview_address']
    if address!='127.0.0.1:18181': raise ValueError('preview address must remain 127.0.0.1:18181')
    with socket.socket() as probe:
        if hasattr(socket,'SO_EXCLUSIVEADDRUSE'): probe.setsockopt(socket.SOL_SOCKET,socket.SO_EXCLUSIVEADDRUSE,1)
        probe.bind(('127.0.0.1',18181))
    run([sys.executable,'-B',ROOT/'scripts/render_registry.py'])
    errors,_=validate.validate_source()
    if errors: raise ValueError('\n'.join(errors))
    preview_config=ROOT/'.premium-preview.toml'
    create_config(preview_config,BUILD/'preview')
    # Serve's strict flag is documented as unsupported in 0.0.71. The strict
    # build is a separate required gate; never claim serve enforces it.
    run([sys.executable,'-m','zensical','serve','--config-file',preview_config,'--dev-addr',address])

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['build','preview'])
    args=parser.parse_args()
    try:
        if args.action=='build': build()
        else: preview()
    except (OSError,ValueError,subprocess.CalledProcessError) as exc:
        print(f'FAILED: {exc}',file=sys.stderr);return 1
    return 0

if __name__=='__main__': sys.exit(main())
