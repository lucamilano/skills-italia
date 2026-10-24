#!/usr/bin/env python3
"""Run the optional browser harness against a synthetic localhost fixture, not a PA portal."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from threading import Thread

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    browser = ROOT / 'skills/italian-pa-frontend/browser-tests'
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT / 'tests/browser-smoke')))
    worker = Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        with tempfile.TemporaryDirectory(prefix='skills italia browser ') as temp:
            config = {
                'baseURL': f'http://127.0.0.1:{server.server_port}', 'pages': ['/'],
                'components': {
                    'menu': {'path': '/', 'trigger': '#menu-open', 'panel': '#menu', 'close': '#menu-close'},
                    'modal': {'path': '/', 'trigger': '#modal-open', 'dialog': '#modal', 'close': '#modal-close'},
                    'form': {'path': '/', 'submit': '#submit', 'error': '#form-error'},
                    'table': {'path': '/', 'table': '#table', 'header': '#table th', 'row': '#table tbody tr'},
                    'wizard': {'path': '/', 'next': '#next', 'previous': '#previous', 'step': '#step'},
                },
            }
            path = Path(temp) / 'fixture.json'
            path.write_text(json.dumps(config), encoding='utf-8')
            env = {**os.environ, 'PA_TEST_CONFIG': str(path), 'PA_ALLOW_REMOTE': '0'}
            print('Synthetic localhost harness checks; these are NOT real-portal or compliance tests.', flush=True)
            return subprocess.run(['node', 'scripts/review.mjs', '--config', str(path), '--iteration', '1'], cwd=browser, env=env, check=False).returncode
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=5)


if __name__ == '__main__':
    raise SystemExit(main())
