"""Render public reference views solely from the checked-in local registries."""
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]

def load(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))

def header(identifier,title):
    return f'---\nid: {identifier}\nrevision: "1.0"\nstatus: DRAFT\nreviewed_on: "2026-10-20"\nevidence: []\nfeatures: []\n---\n\n# {title}\n\n<div class="meta">DRAFT · source review 20 October 2026 · generated registry view</div>\n\n'

def render():
    features=load('maintenance/features.json')['features']
    evidence=load('maintenance/evidence-register.json')
    docs=load('maintenance/document-register.json')['documents']
    status=header('PP-REF-001','Feature evidence')
    status+='These are discovery records for the existing application. **Located** means an entry point was found. **Source-reviewed** means selected source was inspected. Neither establishes an end-to-end working journey. The source review atlas now expands these entry points; detailed operator manuals and runtime acceptance remain later work.\n\n'
    status+='| Feature ID | Business workflow | Primary role | Source review | Guide maturity | Verification limit |\n| --- | --- | --- | --- | --- | --- |\n'
    for f in features:
        status+=f"| {f['id']} | {f['title']} | {f['primary_role']} | {f['source_review']} | {f['document_status']} | {f['limitations']} |\n"
    status+='\n## Source review maps\n\n'+''.join(f"- [{f['id']}: {f['title']}](../{f['review_map']})\n" for f in features)
    status+='\nThe [verification register](verification.md) explains evidence types and the historical test result. Planned guide paths are tracked internally, not presented as completed pages.\n'
    register=header('PP-REF-003','Document register')
    register+='Every public page has a stable ID, review date, maturity, and explicit navigation entry. **DRAFT** describes the document; it does not describe product acceptance or owner approval.\n\n'
    register+='| ID | Page | Revision | Maturity |\n| --- | --- | --- | --- |\n'
    for d in docs:
        target='../'+d['path']
        register+=f"| {d['id']} | [{d['title']}]({target}) | {d['revision']} | {d['status']} |\n"
    register+='\nSee [authoring and validation](../contributing/index.md) for the update process.\n'
    import render_review
    views={'docs/reference/feature-status.md':status,'docs/reference/document-register.md':register}
    views.update(render_review.render())
    return views

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    stale=[]
    for name,text in render().items():
        path=ROOT/name
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8')!=text: stale.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            if not path.is_file() or path.read_text(encoding='utf-8')!=text:
                path.write_text(text,encoding='utf-8',newline='\n')
    if stale:
        print('Stale generated pages: '+', '.join(stale),file=sys.stderr);return 1
    return 0

if __name__=='__main__':sys.exit(main())
