#!/usr/bin/env python3
"""Read-only, evidence-based frontend stack hints. No dependency installation."""
import argparse
import json
from pathlib import Path

IGNORE = {'.git', 'node_modules', 'bin', 'obj', '.next', 'dist', 'build', 'vendor', '.venv'}

def inspect(root):
    root = Path(root).resolve()
    signals = []
    def add(label, evidence, certainty='indicative'):
        signals.append({'technology': label, 'evidence': evidence, 'certainty': certainty})
    for package in sorted(root.glob('**/package.json')):
        if len(package.relative_to(root).parts) > 5 or any(p in IGNORE for p in package.parts): continue
        try:
            data = json.loads(package.read_text(encoding='utf-8'))
            deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
        except (OSError, ValueError, TypeError): continue
        for name, label in [('next','Next.js'), ('react','React'), ('@angular/core','Angular'), ('vue','Vue'), ('nuxt','Nuxt'), ('svelte','Svelte'), ('@sveltejs/kit','SvelteKit'), ('bootstrap-italia','Bootstrap Italia'), ('design-react-kit','Design React Kit')]:
            if name in deps: add(label, f'{package.relative_to(root)}: {name} {deps[name]}', 'dependency')
    for csproj in sorted(root.glob('**/*.csproj')):
        if any(p in IGNORE for p in csproj.parts): continue
        try: content = csproj.read_text(encoding='utf-8', errors='replace').lower()
        except OSError: continue
        if 'microsoft.aspnetcore.components.web' in content or 'microsoft.aspnetcore.components.webassembly' in content: add('Blazor', str(csproj.relative_to(root)), 'dependency')
        else: add('ASP.NET project (UI architecture to verify)', str(csproj.relative_to(root)))
    for pattern,label in [('angular.json','Angular'),('vite.config.*','Vite'),('pom.xml','Java/Maven (UI framework to verify)'),('build.gradle*','Java/Gradle (UI framework to verify)'),('composer.json','PHP/Composer (UI framework to verify)')]:
        for f in root.glob(pattern): add(label, str(f.relative_to(root)))
    for pattern,label in [('**/*.razor','Blazor'),('**/*.cshtml','Razor/MVC'),('**/*.vue','Vue'),('**/*.svelte','Svelte')]:
        matched = []
        for f in root.glob(pattern):
            if not any(p in IGNORE for p in f.parts) and len(f.relative_to(root).parts) <= 7:
                matched.append(str(f.relative_to(root)))
                if len(matched)==2: break
        if matched: add(label, ', '.join(matched), 'source')
    return {'root': str(root), 'signals': signals, 'decision': 'review-signals' if signals else 'ask-user-if-code-required', 'note': 'Indizi, non una scelta definitiva. La richiesta esplicita dell’utente ha priorità; non usare questo script per decidere migrazioni.'}

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('project', nargs='?', default='.')
    p.add_argument('--json', action='store_true')
    args=p.parse_args()
    result=inspect(args.project)
    if args.json: print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for s in result['signals']: print(f"- {s['technology']} [{s['certainty']}]: {s['evidence']}")
        if not result['signals']: print('Nessun indizio rilevato. Chiedere la tecnologia solo se serve generare codice.')
        print(result['note'])
