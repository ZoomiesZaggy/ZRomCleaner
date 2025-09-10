#!/usr/bin/env bash
set -euo pipefail
REL=release
OUT="$REL/ZRomCleaner_mac"
ZIP="$REL/ZRomCleaner_mac.zip"
mkdir -p "$REL"
rm -rf "$OUT"
mkdir -p "$OUT/assets"
cp dist/ZRomCleaner "$OUT/ZRomCleaner" || true
cp README.md VERSION.txt "$OUT/"
cp assets/zrom_icon_*.png "$OUT/assets/" 2>/dev/null || true
cd "$REL"
zip -r "ZRomCleaner_mac.zip" "ZRomCleaner_mac"
echo done
