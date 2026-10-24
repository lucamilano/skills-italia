#!/usr/bin/env python3
"""Find lightweight UI reuse clues; never infer correctness from file names alone."""
import argparse
import json
import os
from pathlib import Path

SKIP={'node_modules','.git','.next','dist','build','bin','obj','coverage','.venv','vendor','__pycache__','.cache'}
EXCLUDE_SUFFIX={'.lock','.map','.min.js'}
EXTS={'.tsx','.jsx','.vue','.svelte','.razor','.cshtml','.html','.css','.scss','.ts','.js'}
GROUPS={
    'tables':['table','datatable','grid','elenco','listing'],
    'filters':['filter','search','ricerca','filtro'],
    'navigation':['header','navbar','sidebar','navigation','breadcrumb'],
    'feedback':['alert','toast','error','loader','spinner'],
    'forms':['form','field','input','wizard'],
    'tokens':['token','variables','theme','palette'],
    'pagination':['pagination','paging','paginator'],
}

def discover(root,limit=3000):
    root=Path(root).resolve()
    if not root.is_dir():raise ValueError('repository path must be existing directory')
    results={key:[] for key in GROUPS}; scanned=0; truncated=False
    for base,dirs,files in os.walk(root):
        dirs[:]=sorted(d for d in dirs if d not in SKIP and not d.startswith('.'))
        for name in sorted(files):
            path=Path(base)/name
            if path.suffix.lower() not in EXTS or any(name.endswith(s) for s in EXCLUDE_SUFFIX):continue
            scanned+=1
            if scanned>limit:truncated=True;break
            label=path.relative_to(root).as_posix()
            lower=name.lower()
            for key,words in GROUPS.items():
                if any(word in lower for word in words):results[key].append(label)
        if truncated:break
    return {'root':str(root),'scanned_files':min(scanned,limit),'truncated':truncated,
            'hints':results,'disclaimer':'Filename-only hints; inspect code and accessibility manually.'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('repository');parser.add_argument('--json',action='store_true',dest='json_output');parser.add_argument('--limit',type=int,default=3000);args=parser.parse_args()
    try:report=discover(args.repository,max(1,args.limit))
    except ValueError as exc:parser.error(str(exc))
    if args.json_output:print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        for name,paths in report['hints'].items():
            if paths:print(f'{name}: '+', '.join(paths[:12]))
        print(report['disclaimer'])
    return 0
if __name__=='__main__':raise SystemExit(main())
