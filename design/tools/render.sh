#!/bin/bash
# Renders one design board to a PNG, as the design canvas shows it.
# usage: tools/render.sh <BoardName> [height]   (run from design/)
# Writes screens/<BoardName>.png and prints the board's title and size.
set -euo pipefail
cd "$(dirname "$0")/.."
B=$(ls -d "$HOME"/.cache/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell 2>/dev/null | tail -1)
[ -x "$B" ] || { echo "install a browser first: npx playwright install chromium-headless-shell" >&2; exit 1; }
n=$1
case $n in Mobile*) w=390; h=844;; *) w=1440; h=900;; esac
"$B" --no-sandbox --hide-scrollbars --disable-gpu --virtual-time-budget=4000 --window-size=$w,${2:-$h} \
  --screenshot="$PWD/screens/$n.png" "file://$PWD/boards/$n.dc.html" >/dev/null 2>&1
echo "screens/$n.png ($w x ${2:-$h})"
