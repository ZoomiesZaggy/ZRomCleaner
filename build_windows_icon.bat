@echo off
rem Verify required files exist before building
if not exist assets\zrom.ico (
    echo Error: icon file assets\zrom.ico not found.
    exit /b 1
)
rem Ensure main script is present
if not exist zrom_cleaner.py (
    echo Error: zrom_cleaner.py not found.
    exit /b 1
)
python -m pip install --upgrade pip pyinstaller
pyinstaller --onefile --windowed --name ZRomCleaner --icon assets\zrom.ico zrom_cleaner.py
