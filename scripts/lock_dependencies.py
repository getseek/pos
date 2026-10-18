"""Explicit lock refresh; never called by normal builds. Windows x64 CPython 3.13."""
from pathlib import Path
import argparse, hashlib, importlib.metadata, json, re, subprocess, sys, uuid
ROOT=Path(__file__).resolve().parents[1]

def normal(name):return re.sub(r'[-_.]+','-',name).lower()
def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--update',action='store_true',required=True);parser.parse_args()
    assert sys.version_info[:2]==(3,13),'Lock currently targets CPython 3.13.'
    assert importlib.metadata.version('zensical')=='0.0.71'
    build=ROOT/'.build';build.mkdir(exist_ok=True)
    wheelhouse=build/('wheelhouse-'+uuid.uuid4().hex);wheelhouse.mkdir()
    freeze=subprocess.check_output([sys.executable,'-m','pip','freeze','--local'],text=True)
    pins={normal(line.split('==')[0]):line for line in freeze.splitlines() if '==' in line}
    resolved=wheelhouse/'resolved.txt';resolved.write_text('\n'.join(sorted(pins.values()))+'\n',encoding='utf-8')
    subprocess.run([sys.executable,'-m','pip','--isolated','download','--index-url','https://pypi.org/simple','--disable-pip-version-check','--cache-dir',str(build/'pip-cache'),'--only-binary=:all:','--requirement',str(resolved),'--dest',str(wheelhouse)],check=True,cwd=ROOT)
    hashes={}
    for wheel in wheelhouse.glob('*.whl'):
        parts=wheel.name.split('-');name=normal(parts[0]);version=parts[1]
        assert name in pins and pins[name].split('==')[1]==version,(name,version)
        hashes[name]=hashlib.sha256(wheel.read_bytes()).hexdigest()
    assert set(hashes)==set(pins),'Missing wheels for resolved requirements.'
    lines=['# Generated with explicit --update on CPython 3.13, Windows x64.','# One exact tested wheel hash per dependency; other platforms need a reviewed lock.']
    lines += [pins[name]+' --hash=sha256:'+hashes[name] for name in sorted(pins)]
    (ROOT/'requirements.lock').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    record={'python':sys.version.split()[0],'platform':sys.platform,'wheelhouse':str(wheelhouse),'packages':len(pins)}
    (build/'dependency-lock.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record))
if __name__=='__main__':main()
