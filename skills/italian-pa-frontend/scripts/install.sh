#!/usr/bin/env bash
set -euo pipefail
installer_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if command -v python3 >/dev/null 2>&1 && python3 -c 'import sys; sys.exit(sys.version_info < (3,10))' >/dev/null 2>&1; then
  exec python3 "$installer_dir/install.py" "$@"
elif command -v python >/dev/null 2>&1 && python -c 'import sys; sys.exit(sys.version_info < (3,10))' >/dev/null 2>&1; then
  exec python "$installer_dir/install.py" "$@"
else
  echo 'Python 3.10+ is required. Install it before running this local installer.' >&2
  exit 1
fi
