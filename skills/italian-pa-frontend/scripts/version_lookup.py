#!/usr/bin/env python3
"""Query versioned official-documentation rules; not an implementation validator."""
import argparse,json,re,sys
from pathlib import Path
RULES=Path(__file__).resolve().parents[1]/'catalog/version-rules.json'
def parse_version(s):
    if not re.fullmatch(r'2\.\d+(?:\.\d+)?',s):
        raise ValueError('Expected Bootstrap Italia 2.x version, e.g. 2.15.0')
    p=[int(x) for x in s.split('.')]
    return tuple((p+[0])[:3])
def applicable(data,version,component=None):
    current=parse_version(version)
    return [r for r in data['rules'] if (not component or r['component'] in (component,'global')) and parse_version(r['introduced_in'])<=current]
def main(argv=None):
    p=argparse.ArgumentParser(description='Bootstrap Italia 2.x version rule lookup')
    p.add_argument('--version',required=True)
    p.add_argument('--component',choices=['header','navigation','forms','tables','modals','steppers','all'],default='all')
    p.add_argument('--json',action='store_true')
    args=p.parse_args(argv)
    try: data=json.loads(RULES.read_text(encoding='utf8')); out=applicable(data,args.version,None if args.component=='all' else args.component)
    except (ValueError,OSError,json.JSONDecodeError) as exc: p.error(str(exc))
    if args.json: print(json.dumps({'version':args.version,'component':args.component,'rules':out,'warning':'No listed rules does not mean the component has no version differences.'},ensure_ascii=False,indent=2))
    else:
        for r in out: print(f"{r['id']} [{r['component']}, >= {r['introduced_in']}]\n  {r['summary']}\n  CHECK: {r['check']}\n  SOURCE: {r['source']}")
        if not out: print('No catalogued rules for this selection. This is NOT a compatibility guarantee.')
    return 0
if __name__=='__main__': sys.exit(main())
