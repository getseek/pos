"""Read every registered page/asset from the fixed loopback preview only."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import urllib.request
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
routes=[]
for d in load('maintenance/document-register.json')['documents']:
    p=Path(d['path']);route=p.parent.as_posix() if p.name=='index.md' else p.with_suffix('').as_posix()
    routes.append('' if route=='.' else route+'/')
routes += [a['path'] for a in load('maintenance/assets.json')['assets']]+['search.json']
def get(route):
    url='http://127.0.0.1:18181/'+route
    try:
        with urllib.request.urlopen(url,timeout=30) as response:
            content=response.read();return {'route':route,'status':response.status,'bytes':len(content)}
    except Exception as exc:return {'route':route,'error':type(exc).__name__}
with ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(get,routes))
failures=[r for r in results if r.get('status')!=200 or not r.get('bytes')]
report={'ok':not failures,'routes_checked':len(results),'pages_checked':len(load('maintenance/document-register.json')['documents']),'errors':failures,'results':results}
(ROOT/'.build/http-smoke.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='results'}))
raise SystemExit(bool(failures))
