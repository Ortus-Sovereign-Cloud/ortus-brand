#!/usr/bin/env bash
# The design reference: every board the README lists has its picture, the
# canvas file is valid JSON, and the logos are where the apps expect them.
set -euo pipefail
cd "$(dirname "$0")/.."
missing=0
for board in $(grep -o '`[A-Z][A-Za-z]*`' design/README.md | tr -d '`' | sort -u); do
  [ -f "design/screens/$board.png" ] || { echo "check: design/screens/$board.png is missing" >&2; missing=1; }
done
python3 -c 'import json,sys; json.load(open("design/boards/canvas.json"))'
for f in ortus-mark.svg ortus-logo-dark.png ortus-logo-light.png ortus-avatar.svg; do
  [ -f "$f" ] || { echo "check: $f is missing" >&2; missing=1; }
done
[ "$missing" = 0 ]
echo "all checks passed"
