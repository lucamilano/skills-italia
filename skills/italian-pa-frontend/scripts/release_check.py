#!/usr/bin/env python3
"""Local pre-release checks. Never claims browser/runtime certification."""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    ("skill structure", [sys.executable, "scripts/validate_skill.py"]),
    ("Python unit tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]),
    ("Node unit tests", ["node", "--test", "browser-tests/scripts/config.test.mjs", "browser-tests/scripts/visual-review.test.mjs"]),
]

def main():
    for label, command in COMMANDS:
        print(f"\n=== {label} ===", flush=True)
        try:
            result = subprocess.run(command, cwd=ROOT, check=False)
        except FileNotFoundError:
            print(f"FAILED: executable missing for {label}: {command[0]}", file=sys.stderr)
            return 1
        if result.returncode:
            print(f"FAILED: {label} (exit {result.returncode})", file=sys.stderr)
            return result.returncode
    print("\nPASS: static validation, Python and Node unit tests. Browser E2E NOT executed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
