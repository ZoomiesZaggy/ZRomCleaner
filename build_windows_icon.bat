@echo off
python -m pip install --upgrade pip pyinstaller
pyinstaller --onefile --windowed --name ZRomCleaner --icon assets\zrom.ico zrom_cleaner.py
