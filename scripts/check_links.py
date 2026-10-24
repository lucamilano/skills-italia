#!/usr/bin/env python3
"""Check local Markdown links/anchors; optionally verify external URL availability."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import sys
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

from install import ROOT, excluded


def links(text):
    # Fenced examples are illustrative commands/templates, not document links.
    text = re.sub(r'^(```|~~~).*?^\1\s*$', '', text, flags=re.M | re.S)
    return re.findall(r'!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', text)


def anchors(path):
    content = path.read_text(encoding='utf-8')
    content = re.sub(r'^(```|~~~).*?^\1\s*$', '', content, flags=re.M | re.S)
    counts, found = {}, set()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', content, re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', heading)
        heading = re.sub(r'<[^>]*>', '', heading).lower()
        slug = ''.join(c for c in heading if c in '-_ ' or unicodedata.category(c)[0] in 'LN').replace(' ', '-')
        count = counts.get(slug, 0)
        found.add(f'{slug}-{count}' if count else slug)
        counts[slug] = count + 1
    found.update(re.findall(r'\bid=["\']([^"\']+)["\']', content))
    return found


def check_local(root=ROOT):
    errors, external = [], set()
    for path in sorted(root.rglob('*.md')):
        if excluded(path.relative_to(root)):
            continue
        content = path.read_text(encoding='utf-8')
        for raw in links(content):
            target = raw.strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme in ('https', 'http'):
                external.add(target.split('#')[0])
                continue
            if parsed.scheme in ('mailto', 'tel'):
                continue
            if parsed.scheme or parsed.netloc:
                errors.append(f'{path.relative_to(root)}: unsupported link {target}')
                continue
            local = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            if not local.is_relative_to(root.resolve()) or not local.exists():
                errors.append(f'{path.relative_to(root)}: missing/escaping link {target}')
            elif parsed.fragment and local.suffix == '.md' and unquote(parsed.fragment) not in anchors(local):
                errors.append(f'{path.relative_to(root)}: missing anchor {target}')
        # Include bare official URLs used throughout the preserved module references.
        for url in re.findall(r'https?://[^\s<>`"\)]+', content):
            external.add(url.rstrip('.,;|').split('#')[0])
    return errors, external


def check_external(url):
    try:
        request = Request(url, headers={'User-Agent': 'SkillsItalia-LinkCheck/0.1 (documentation validation)'})
        with urlopen(request, timeout=20) as response:
            response.read(1024)
            return url, response.status, response.geturl(), None
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        return url, getattr(exc, 'code', None), None, str(exc)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--external', action='store_true')
    args = parser.parse_args()
    errors, urls = check_local()
    for error in errors:
        print('ERROR:', error)
    if args.external:
        with ThreadPoolExecutor(max_workers=6) as pool:
            for url, status, final, error in pool.map(check_external, sorted(urls)):
                print(f'{"FAIL" if error else "OK"} {status or "network"} {url}' + (f' -> {final}' if final and final != url else ''))
                if error:
                    errors.append(f'{url}: {error}')
    print(f'{len(errors)} link errors; {len(urls)} external URLs {"checked" if args.external else "not checked (use --external)"}.')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
