#!/usr/bin/env python3
# minimal entry calling GUI if no args else CLI
import sys
from pathlib import Path


def _get_version() -> str:
    """Return the application version string."""
    version_path = Path(__file__).with_name("VERSION.txt")
    return version_path.read_text(encoding="utf-8").strip()  # use UTF-8 encoding


def main():
    # placeholder for the full script; users can replace with the latest
    print("ZRom Cleaner skeleton script is bundled. Replace with your full zrom_cleaner.py if needed.")
    print("Run: python zrom_cleaner.py /path/to/roms --regions U E UK J W --apply")


if __name__ == "__main__":
    main()
