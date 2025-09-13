@echo off
if not exist assets\zrom.ico (
    echo Error: assets\zrom.ico not found.
    exit /b 1
)

if not exist zrom_cleaner.py (
    echo Error: zrom_cleaner.py not found in project root.
    exit /b 1
)

python -m pip install --upgrade pip pyinstaller
pyinstaller --onefile --windowed --name ZRomCleaner --icon assets\zrom.ico zrom_cleaner.py
