"""Explicit, read-only source refresh. Never called by normal documentation builds.

Run the docs-owned Roslyn indexer first. SQL is replayed only into :memory:.
No application assembly is loaded and no application database is opened.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
DATE='2026-10-18'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,value):
    # Normalize CR escapes: the Roslyn raw index carries lone \r from CRLF sources;
    # files written with CR then compare stale forever because read_text() normalizes
    # them on load (render --check could never pass once a multi-line snippet landed
    # in a generated page). Canonical index content is LF-only.
    text=json.dumps(value,ensure_ascii=False,indent=2).replace('\\r\\n','\\n').replace('\\r','\\n')
    p.write_text(text+'\n',encoding='utf-8',newline='\n')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--application-root',type=Path,required=True)
    parser.add_argument('--raw-index',type=Path,required=True)
    args=parser.parse_args();app=args.application_root.resolve()
    if ROOT.is_relative_to(app): raise ValueError('Documentation must be outside the application.')
    raw=json.loads(args.raw_index.read_text(encoding='utf-8'))
    files=[]
    for f in raw['files']:
        p=app/f['path']
        if sha(p)!=f['sha256']: raise ValueError('Source changed during extraction: '+f['path'])
        files.append({**f,'lines':len(p.read_text(encoding='utf-8-sig').splitlines())})
    connection=sqlite3.connect(':memory:')
    connection.executescript('CREATE TABLE schema_version(version INTEGER PRIMARY KEY,applied_at_utc TEXT,description TEXT);')
    migrations=[]
    for p in sorted((app/'Software/src/GetSeek.Infrastructure/Persistence/Migrations').glob('*.sql')):
        connection.executescript(p.read_text(encoding='utf-8-sig'))
        connection.execute('INSERT INTO schema_version VALUES(?,?,?)',(int(p.name[:3]),DATE,p.stem))
        migrations.append({'path':p.relative_to(app).as_posix(),'sha256':sha(p),'version':int(p.name[:3])})
    def quoted(s):return '"'+s.replace('"','""')+'"'
    tables=[]
    for name, in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name").fetchall():
        columns=[{'name':r[1],'type':r[2],'not_null':bool(r[3]),'pk':r[5]} for r in connection.execute('PRAGMA table_info('+quoted(name)+')')]
        foreign_keys=[{'id':r[0],'sequence':r[1],'parent':r[2],'from':r[3],'to':r[4],'on_update':r[5],'on_delete':r[6]} for r in connection.execute('PRAGMA foreign_key_list('+quoted(name)+')')]
        tables.append({'name':name,'columns':columns,'foreign_keys':foreign_keys})
    fk_errors=connection.execute('PRAGMA foreign_key_check').fetchall()
    known={t['name'] for t in tables}
    for f in files:
        for m in f['methods']:
            # Keep literal table references only. This is not semantic SQL analysis.
            m['sql']=[s for s in m['sql'] if s['table'] in known]
            # Publish call names and line locations, not expressions/literal arguments.
            m['calls']=[{'name':c['name'],'line':c['line'],'receiver':c['receiver'],'generic_types':c['generic_types']} for c in m['calls']]
            m['errors']=[{'line':e['line'],'code':e['code']} for e in m['errors'] if re.fullmatch('[A-Z][A-Z0-9_]+',e['code'])]
            m.pop('guards',None);m.pop('variables',None)
        # Constants other than permission names are unnecessary public metadata.
        f['constants']=[c for c in f['constants'] if c['owner']=='Permissions']
    projects=[];bindings=[];other_files=[]
    for p in sorted((app/'Software/src').rglob('*')):
        if not p.is_file() or any(part in {'bin','obj'} for part in p.relative_to(app).parts):continue
        if p.suffix not in {'.axaml','.sql','.csproj'}:continue
        path=p.relative_to(app).as_posix();text=p.read_text(encoding='utf-8-sig')
        other_files.append({'path':path,'sha256':sha(p),'lines':len(text.splitlines()),'project':p.relative_to(app/'Software/src').parts[0]})
        if p.suffix=='.csproj':
            tree=ET.fromstring(text)
            projects.append({'name':p.stem,'path':path,'references':[Path(e.attrib['Include'].replace('\\','/')).stem for e in tree.iter('ProjectReference')]})
        if p.suffix=='.axaml':
            for number,line in enumerate(text.splitlines(),1):
                for match in re.finditer(r'\bCommand="\{Binding\s+([^},\s]+)',line):
                    bindings.append({'path':path,'line':number,'binding':match.group(1)})
    methods=[(f,m) for f in files if not f['test'] for m in f['methods']]
    types={}
    for f in files:
        if not f['test']:
            for t in f['types']:types.setdefault(t['name'],[]).append((f,t))
    commands=[]
    for f in files:
        if f['test']:continue
        for t in f['types']:
            for base in t['bases']:
                match=re.fullmatch(r'ICommandHandler<\s*(\w+)\s*,\s*(.+)>',base,re.S)
                if not match:continue
                name,result=match.groups()
                declarations=types.get(name,[])
                handler_methods=[m for m in f['methods'] if m['owner']==t['name'] and m['name']=='HandleAsync' and m['parameters'] and m['parameters'][0]['type']==name]
                producers=[]
                for origin,m in methods:
                    for creation in m['creates']:
                        if creation['type']==name:producers.append({'path':origin['path'],'method':m['name'],'line':creation['line'],'method_id':m['id']})
                commands.append({'name':name,'result':result.strip(),'handler':t['name'],'path':f['path'],'line':t['line'],
                    'declarations':[{'path':a['path'],'line':b['line'],'properties':b['properties']} for a,b in declarations],
                    'methods':[m['id'] for m in handler_methods],'producers':producers})
    for p in sorted((app/'Software/tests').glob('*/*.csproj')):
        other_files.append({'path':p.relative_to(app).as_posix(),'sha256':sha(p),'lines':len(p.read_text(encoding='utf-8-sig').splitlines()),'project':p.parent.name})
    snapshot={'schema_version':1,'reviewed_on':DATE,'methodology':raw['extractor'],
        'scope':'Syntax inventory and selected manual control-flow review. No semantic binding, application build, test execution or device operation.',
        'files':files,'other_files':other_files,'projects':projects,'bindings':bindings,'commands':sorted(commands,key=lambda c:c['name']),
        'schema':{'method':'84 SQL files replayed sequentially into Python SQLite :memory:; not the .NET migration runner or a live database.',
            'sqlite_version':sqlite3.sqlite_version,'migrations':migrations,'tables':tables,'foreign_key_check':fk_errors}}
    # Only reviewed metadata is retained. Raw syntax calls stay outside publication.
    for f in snapshot['files']:
        for m in f['methods']:
            if f['test']:
                for name in ('calls','creates','errors','sql','throws','parameters'):
                    m[name]=[]
            seen=set();calls=[]
            for c in m['calls']:
                key=(c['name'],c['receiver'],tuple(c['generic_types']))
                if key not in seen:seen.add(key);calls.append(c)
            m['calls']=calls
    save(ROOT/'maintenance/code-review-index.json',snapshot)
    print(json.dumps({'application_files':sum(not f['test'] for f in files),'test_files':sum(f['test'] for f in files),'commands':len(commands),'tables':len(tables),'foreign_key_columns':sum(len(t['foreign_keys']) for t in tables),'schema_fk_violations':len(fk_errors)}))

if __name__=='__main__':main()
