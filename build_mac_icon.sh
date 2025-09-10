#!/usr/bin/env bash
set -euo pipefail
python3 -m pip install --upgrade pip pyinstaller
pyinstaller --onefile --windowed --name ZRomCleaner zrom_cleaner.py
