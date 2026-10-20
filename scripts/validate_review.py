"""Validate frozen review evidence and connections without reading app source."""
import hashlib
import json
from pathlib import PurePosixPath,Path
import re
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))

def validate_records(data,workflows,decisions,feature_ids,rules=()):
    errors=[];files=data['files']+data['other_files'];sources={f['path']:f for f in files}
    if len(sources)!=len(files):errors.append('review: duplicate source paths')
    for f in files:
        p=PurePosixPath(f['path'])
        if p.is_absolute() or '..' in p.parts or '\\' in f['path'] or not f['path'].startswith('Software/') or ':' in f['path']:
            errors.append('review: unsafe source path '+f['path'])
        if not re.fullmatch('[a-f0-9]{64}',f['sha256']) or f['lines']<1:errors.append('review: invalid source digest/lines '+f['path'])
        if f.get('syntax_errors'):errors.append('review: C# syntax errors in '+f['path'])
    methods={m['id']:(f,m) for f in data['files'] if not f['test'] for m in f['methods']}
    count=sum(len(f['methods']) for f in data['files'] if not f['test'])
    if len(methods)!=count:errors.append('review: duplicate method IDs')
    for f,m in methods.values():
        if not 1<=m['line']<=m['end']<=f['lines']:errors.append('review: method line range '+m['id'])
    def reference(r):
        if r['path'] not in sources:errors.append('review: unknown source '+r['path']);return
        f=sources[r['path']]
        if r.get('sha256',f['sha256'])!=f['sha256']:errors.append('review: stale source digest '+r['path'])
        if not 1<=r.get('line',1)<=f['lines']:errors.append('review: source line outside file '+r['path'])
    commands={c['name']:c for c in data['commands']}
    if len(commands)!=len(data['commands']):errors.append('review: duplicate commands')
    for c in commands.values():
        reference(c)
        if not c['methods']:errors.append('review: command has no handler method '+c['name'])
        for mid in c['methods']:
            if mid not in methods:errors.append('review: unknown handler method '+mid)
        if not c['declarations']:errors.append('review: command declaration missing '+c['name'])
        for r in c['declarations']+c['producers']:reference(r)
    assigned=[];features=set();slugs=set()
    for w in workflows:
        if w['slug'] in slugs:errors.append('review: duplicate workflow slug')
        slugs.add(w['slug']);features.update(w['features']);assigned+=w['commands']
        for c in w['commands']:
            if c not in commands:errors.append('review: unknown workflow command '+c)
        if len(w['steps'])<3 or not w['sources']:errors.append('review: incomplete workflow '+w['slug'])
        for r in w['sources']:reference(r)
    if set(assigned)!=set(commands) or len(assigned)!=len(set(assigned)):errors.append('review: command coverage must assign every handler exactly once')
    if features!=set(feature_ids):errors.append('review: feature coverage mismatch')
    table_map={t['name']:t for t in data['schema']['tables']}
    for t in table_map.values():
        columns={c['name'] for c in t['columns']}
        for fk in t['foreign_keys']:
            if fk['from'] not in columns or fk['parent'] not in table_map:errors.append('review: invalid foreign-key endpoint '+t['name']);continue
            if fk['to'] and fk['to'] not in {c['name'] for c in table_map[fk['parent']]['columns']}:errors.append('review: unknown parent column '+t['name'])
    migrations=data['schema']['migrations']
    if [m['version'] for m in migrations]!=list(range(1,85)):errors.append('review: migration sequence is not 1–84')
    for m in migrations:reference(m)
    if data['schema']['foreign_key_check']:errors.append('review: reconstructed schema foreign-key violations')
    ids=set()
    for f in decisions:
        if f['id'] in ids:errors.append('review: duplicate decision ID')
        ids.add(f['id'])
        if f['workflow'] not in slugs:errors.append('review: unknown decision workflow')
        if len(f['options'])<2 or len({o['id'] for o in f['options']})!=len(f['options']):errors.append('review: decision choices incomplete')
        for r in f['sources']:reference(r)
        for o in f['options']:
            if not o['steps'] or not o['acceptance'] or not o['tradeoff']:errors.append('review: decision steps/checks missing')
        if not f['runtime_status'] or not f['rollback']:errors.append('review: decision evidence/rollback missing')
    for rule in rules:
        if rule.get("verification")!="source-only; runtime not rerun" or not rule.get("statement") or not rule.get("sources"):
            errors.append("review: business rule evidence/maturity invalid")
        for r in rule.get("sources",[]):reference(r)
    return errors

def validate():
    data=load('maintenance/code-review-index.json')
    errors=validate_records(data,load('maintenance/review-workflows.json')['workflows'],load('maintenance/review-decisions.json')['findings'],[f['id'] for f in load('maintenance/features.json')['features']],load('maintenance/review-rules.json')['rules'])
    evidence=next(e for e in load('maintenance/evidence-register.json')['evidence'] if e['id']=='E-015')
    if evidence['sha256']!=hashlib.sha256((ROOT/'maintenance/code-review-index.json').read_bytes()).hexdigest():errors.append('review: E-015 snapshot digest stale')
    return errors
