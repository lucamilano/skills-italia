#!/usr/bin/env python3
"""Check structural completeness of a workflow brief; not a compliance audit."""
import argparse, json, sys
from pathlib import Path

def validate(data):
    errors=[]
    if not isinstance(data,dict): return ['Root must be an object']
    if data.get('workflow') not in ('administrative-wizard','administrative-form'):
        errors.append('workflow must be administrative-wizard or administrative-form')
    steps=data.get('steps')
    if not isinstance(steps,list) or not steps: errors.append('steps must be a nonempty list'); steps=[]
    ids=set(); fields=set()
    for n,step in enumerate(steps):
        if not isinstance(step,dict): errors.append(f'steps[{n}] must be object'); continue
        sid=step.get('id')
        if not isinstance(sid,str) or not sid.strip() or sid in ids: errors.append(f'steps[{n}].id missing/duplicate')
        else: ids.add(sid)
        if not isinstance(step.get('title'),str) or not step['title'].strip():errors.append(f'steps[{n}].title missing')
        if not isinstance(step.get('fields'),list):errors.append(f'steps[{n}].fields must be array');continue
        for m,field in enumerate(step['fields']):
            if not isinstance(field,dict):errors.append(f'field {n}.{m} must be object');continue
            fid=field.get('id')
            if not isinstance(fid,str) or not fid.strip() or fid in fields:errors.append(f'field {n}.{m} id missing/duplicate')
            else:fields.add(fid)
            if not isinstance(field.get('label'),str) or not field['label'].strip():errors.append(f'field {n}.{m} label missing')
            if not isinstance(field.get('required'),bool):errors.append(f'field {n}.{m} required must be boolean')
    features=data.get('features')
    if not isinstance(features,dict):errors.append('features must be object');features={}
    backend=data.get('backend')
    if not isinstance(backend,dict):errors.append('backend must be object');backend={}
    for key in ('draft','attachments'):
        if not isinstance(features.get(key),bool):errors.append(f'features.{key} must be boolean')
    # A workflow can be planned without endpoints, but missing services are clearly reported.
    warnings=[]
    for flag,endpoint in [('draft','draft_endpoint'),('attachments','upload_endpoint')]:
        if features.get(flag) and not backend.get(endpoint): warnings.append(f'{flag}: backend capability unresolved; do not claim functionality')
    if not backend.get('submit_endpoint'): warnings.append('submit endpoint unknown: cannot claim successful final submission')
    if not isinstance(data.get('acceptance_tests'),list):errors.append('acceptance_tests must be array')
    return errors,warnings

def main():
    p=argparse.ArgumentParser();p.add_argument('file');p.add_argument('--json',action='store_true',dest='as_json');args=p.parse_args()
    try:data=json.loads(Path(args.file).read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as e:print(f'ERROR: {e}',file=sys.stderr);return 2
    result=validate(data)
    if isinstance(result,list): errors,warnings=result,[]
    else:errors,warnings=result
    if args.as_json:print(json.dumps({'valid':not errors,'errors':errors,'warnings':warnings},ensure_ascii=False,indent=2))
    else:
        for e in errors:print('ERROR:',e)
        for w in warnings:print('WARNING:',w)
        if not errors:print('OK: structure valid; feature and backend verification remain required')
    return 1 if errors else 0
if __name__=='__main__':sys.exit(main())
