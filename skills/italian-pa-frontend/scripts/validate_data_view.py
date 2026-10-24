#!/usr/bin/env python3
"""Validate completeness of an administrative data view brief; no runtime or compliance assertions."""
import argparse
import json
import sys
from pathlib import Path

MODES = {'server', 'client'}
STATES = {'loading', 'empty', 'no-results', 'error', 'ready', 'forbidden'}

def validate(doc):
    errors, warnings = [], []
    if not isinstance(doc, dict): return ['Root must be a JSON object'], []
    if doc.get('view') not in ('administrative-list', 'administrative-dashboard'):
        errors.append('view must be administrative-list or administrative-dashboard')
    if not isinstance(doc.get('title'), str) or not doc['title'].strip(): errors.append('title is required')
    source = doc.get('data_source')
    if not isinstance(source, dict):
        errors.append('data_source must be object'); source = {}
    if source.get('status') not in ('confirmed', 'unresolved', 'mock'):
        errors.append('data_source.status must be confirmed, unresolved, or mock')
    if source.get('status') == 'confirmed' and not source.get('endpoint'):
        errors.append('confirmed data source needs endpoint')
    if source.get('status') != 'confirmed':
        warnings.append('data source not verified: do not claim live data integration')
    cols=doc.get('columns')
    if not isinstance(cols, list) or not cols: errors.append('columns must be nonempty list'); cols=[]
    ids=set()
    for i,c in enumerate(cols):
        if not isinstance(c,dict): errors.append(f'columns[{i}] must be object');continue
        cid=c.get('id');label=c.get('label')
        if not isinstance(cid,str) or not cid.strip() or cid in ids: errors.append(f'columns[{i}] id missing/duplicate')
        else: ids.add(cid)
        if not isinstance(label,str) or not label.strip(): errors.append(f'columns[{i}] label required')
        if not isinstance(c.get('sortable'),bool):errors.append(f'columns[{i}] sortable must be boolean')
    search=doc.get('search')
    if not isinstance(search,dict) or not isinstance(search.get('enabled'),bool):errors.append('search.enabled must be boolean')
    elif search['enabled'] and search.get('scope') not in ('entire_dataset','current_page'):
        errors.append('search.scope required: entire_dataset or current_page')
    filters=doc.get('filters')
    if not isinstance(filters,list): errors.append('filters must be list');filters=[]
    for i,f in enumerate(filters):
        if not isinstance(f,dict) or not all(isinstance(f.get(k),str) and f[k].strip() for k in ('id','label','type')):
            errors.append(f'filters[{i}] id, label and type required')
    sorting=doc.get('sorting')
    if not isinstance(sorting,dict) or not isinstance(sorting.get('enabled'),bool): errors.append('sorting.enabled must be boolean');sorting={}
    if sorting.get('enabled'):
        allowed=sorting.get('allowed_fields')
        if not isinstance(allowed,list) or not allowed or any(x not in ids for x in allowed):
            errors.append('sorting.allowed_fields must refer to columns')
        else:
            for col in cols:
                if isinstance(col,dict) and col.get('id') in allowed and col.get('sortable') is not True:
                    errors.append(f'column {col["id"]} is not marked sortable')
        default=sorting.get('default')
        if not isinstance(default,dict) or default.get('field') not in (allowed if isinstance(allowed,list) else []) or default.get('direction') not in ('asc','desc'):
            errors.append('sorting.default must use allowed field and asc/desc')
    page=doc.get('pagination')
    if not isinstance(page,dict) or page.get('mode') not in MODES or type(page.get('page_size')) is not int or page['page_size'] < 1:
        errors.append('pagination requires mode server/client and positive integer page_size')
    export=doc.get('export')
    if not isinstance(export,dict) or not isinstance(export.get('enabled'),bool):errors.append('export.enabled must be boolean');export={}
    if export.get('enabled'):
        if export.get('scope') not in ('page','selected','filtered_all'):
            errors.append('export.scope must be page, selected or filtered_all')
        if export.get('authorized_backend') is not True:
            warnings.append('export authorization/backend unresolved: do not present as functional')
    actions=doc.get('actions')
    if not isinstance(actions,list):errors.append('actions must be list');actions=[]
    for i,a in enumerate(actions):
        if not isinstance(a,dict) or not isinstance(a.get('id'),str) or not a.get('label') or not a.get('requires_permission'):
            errors.append(f'actions[{i}] requires id, label, requires_permission');continue
        if a.get('backend_enforced') is not True:
            warnings.append(f'actions[{i}] server permission not verified: UI hiding is insufficient')
    states=doc.get('states')
    if not isinstance(states,list) or any(s not in STATES for s in states):errors.append('states must be recognized state list');states=[]
    for state in ('loading','empty','no-results','error','ready'):
        if state not in states: warnings.append(f'missing recommended state: {state}')
    if doc.get('responsive_strategy') not in ('scroll-without-information-loss','alternative-equivalent-view'):
        errors.append('responsive_strategy must preserve information and actions')
    for key in ('accessibility_tests','acceptance_tests'):
        if not isinstance(doc.get(key),list) or not doc[key]: errors.append(f'{key} must be nonempty array')
    return errors,warnings

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('file');parser.add_argument('--json',action='store_true',dest='json_output');args=parser.parse_args()
    try:doc=json.loads(Path(args.file).read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as exc:print(f'ERROR: {exc}',file=sys.stderr);return 2
    errors,warnings=validate(doc)
    if args.json_output: print(json.dumps({'valid':not errors,'errors':errors,'warnings':warnings},ensure_ascii=False,indent=2))
    else:
        for err in errors:print('ERROR:',err)
        for w in warnings:print('WARNING:',w)
        if not errors:print('OK: specification structurally valid; verify backend and actual UI')
    return 1 if errors else 0

if __name__=='__main__':sys.exit(main())
