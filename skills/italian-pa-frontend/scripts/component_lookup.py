#!/usr/bin/env python3
"""Consultazione offline del catalogo componenti (Python standard library)."""
import argparse
import json
import sys
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / 'catalog' / 'components.json'

def load_catalog():
    return json.loads(CATALOG.read_text(encoding='utf-8'))

def main(argv=None):
    parser = argparse.ArgumentParser(description='Italian PA Frontend component catalog')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list', help='Lista componenti disponibili')
    show = sub.add_parser('show', help='Dettagli componente e link')
    show.add_argument('component_id')
    args = parser.parse_args(argv)
    data = load_catalog()
    items = data['components']
    if args.command == 'list':
        for item in items:
            print(f"{item['id']}: {item['name']} [{item['status']}]")
        return 0
    match = next((item for item in items if item['id'] == args.component_id), None)
    if match is None:
        print('Componente non trovato: '+args.component_id, file=sys.stderr)
        return 2
    print(json.dumps(match, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
