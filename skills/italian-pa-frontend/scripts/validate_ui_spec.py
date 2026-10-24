#!/usr/bin/env python3
"""Validate completeness of UI composition brief, NOT WCAG/design compliance."""
import json
import sys
from pathlib import Path

REQUIRED_STATES = {"loading", "empty", "error"}

def check(doc):
    issues=[]
    for field in ("screen","purpose","technology","layout","states","components","validation"):
        if field not in doc: issues.append("missing field: " + field)
    t=doc.get('technology',{})
    if not isinstance(t,dict) or not all(t.get(k) for k in ('source','name','design_system_version')):
        issues.append('technology requires source, name and design_system_version (can say unverified)')
    layout=doc.get('layout',{})
    if not isinstance(layout,dict) or not layout.get('content_order') or not layout.get('viewports'):
        issues.append('layout requires content_order and viewports')
    states=doc.get('states',[])
    if not isinstance(states,list) or not REQUIRED_STATES.issubset(set(states)):
        issues.append('states must include loading, empty, error')
    if not isinstance(doc.get('components',[]),list): issues.append('components must be a list')
    validation=doc.get('validation',{})
    if not isinstance(validation,dict) or not all(isinstance(validation.get(k),bool) for k in ('keyboard','zoom_reflow','contrast','manual_review')):
        issues.append('validation flags must be booleans for keyboard, zoom_reflow, contrast, manual_review')
    return issues

if __name__=='__main__':
    try: doc=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    except (IndexError,OSError,ValueError) as exc:
        print('ERROR:',exc);sys.exit(2)
    problems=check(doc)
    if problems:
        for issue in problems: print('ERROR:',issue)
        sys.exit(1)
    print('OK: UI brief structure valid; design/accessibility NOT verified.')
