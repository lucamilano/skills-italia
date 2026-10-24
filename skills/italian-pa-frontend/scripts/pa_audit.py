#!/usr/bin/env python3
"""Conservative static lint for HTML-like files. NOT an accessibility conformance test."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path

EXT = {'.html', '.htm', '.cshtml', '.jsx', '.tsx'}
SKIP = {'node_modules', '.git', 'bin', 'obj', '.next', 'dist', 'build', 'coverage'}


class EvidenceParser(HTMLParser):
    def __init__(self, filename):
        super().__init__(convert_charrefs=True)
        self.filename = str(filename)
        self.issues = []
        self.ids = set()
        self.inputs = []
        self.labels = set()
        self.wrapping_labels = 0
        self.in_label = 0
        self.html_seen = False
        self.html_lang = False
        self.main_count = 0

    def warn(self, line, rule, message):
        self.issues.append({'file': self.filename, 'line': line,
                            'rule': rule, 'level': 'possible', 'message': message})

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        line = self.getpos()[0]
        if tag == 'html':
            self.html_seen = True
            self.html_lang = bool(attrs.get('lang'))
        if tag == 'main':
            self.main_count += 1
        ident = attrs.get('id')
        if ident:
            if ident in self.ids:
                self.warn(line, 'duplicate-id', f'Identificativo duplicato: {ident}')
            self.ids.add(ident)
        if tag == 'label':
            self.in_label += 1
            if attrs.get('for') or attrs.get('htmlFor'):
                self.labels.add(attrs.get('for') or attrs.get('htmlFor'))
        if tag == 'img' and 'alt' not in attrs and 'aria-hidden' not in attrs:
            self.warn(line, 'img-alt', 'Immagine senza attributo alt (potrebbe essere decorativa).')
        if tag == 'input' and attrs.get('type', 'text') not in ('hidden','submit','button','reset','image'):
            if not any(k in attrs for k in ('aria-label','aria-labelledby')) and not self.in_label:
                self.inputs.append((line, ident))
        if tag == 'a' and attrs.get('target') == '_blank':
            rel = set((attrs.get('rel') or '').lower().split())
            if 'noopener' not in rel:
                self.warn(line, 'blank-rel', 'Link target="_blank" senza rel="noopener"; verificare sicurezza e contesto.')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag == 'label':
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == 'label' and self.in_label:
            self.in_label -= 1

    def result(self):
        if self.html_seen and not self.html_lang:
            self.warn(1, 'html-lang', 'Documento HTML senza lingua esplicita.')
        if self.html_seen and self.main_count == 0:
            self.warn(1, 'main-landmark', 'Documento HTML senza elemento <main>.')
        for line, ident in self.inputs:
            if not ident or ident not in self.labels:
                self.warn(line, 'input-name', 'Input senza label HTML associata rilevabile staticamente; controllare il nome accessibile.')
        return sorted(self.issues, key=lambda i:(i['line'],i['rule']))


def scan_text(content, filename):
    p = EvidenceParser(filename)
    try:
        p.feed(content)
        p.close()
    except (ValueError, AssertionError) as exc:
        p.warn(1, 'parse-error', f'Parsing HTML parziale: {exc}')
    return p.result()


def scan_path(path):
    if path.is_file():
        paths = [path] if path.suffix.lower() in EXT else []
    else:
        paths = sorted(f for f in path.rglob('*') if f.is_file() and
                       f.suffix.lower() in EXT and not (set(f.relative_to(path).parts) & SKIP))
    results = []
    for f in paths:
        try:
            results.extend(scan_text(f.read_text(encoding='utf-8'), f))
        except (UnicodeError, OSError) as exc:
            results.append({'file':str(f),'line':1,'rule':'read-error','level':'possible','message':str(exc)})
    return len(paths), results


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('path', type=Path, help='File or folder to inspect')
    cli.add_argument('--format', choices=['text','json'], default='text')
    args = cli.parse_args()
    if not args.path.exists():
        cli.error(f'Path does not exist: {args.path}')
    count, findings = scan_path(args.path)
    if args.format == 'json':
        print(json.dumps({'files_scanned':count, 'findings':findings,
                          'disclaimer':'Static heuristics only; not a WCAG/AgID compliance certification.'},
                         ensure_ascii=False,indent=2))
    else:
        print(f'Analizzati {count} file; {len(findings)} possibili criticità (euristiche).')
        for f in findings:
            print(f"{f['file']}:{f['line']} [{f['rule']}] {f['message']}")
        print('ATTENZIONE: gli esiti non attestano conformità WCAG/AGID.')
    return 0  # Do not fail CI for heuristic findings in MVP.


if __name__ == '__main__':
    raise SystemExit(main())
