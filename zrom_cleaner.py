#!/usr/bin/env python3
# minimal entry calling GUI if no args else CLI
import sys
from pathlib import Path
import argparse


def main(argv=None):
    """Minimal CLI entry point.

    When no path argument is supplied, the user is prompted for one. An
    empty response defaults to the current working directory.
    """
    parser = argparse.ArgumentParser(description="ZRom Cleaner skeleton")
    parser.add_argument("path", nargs="?", help="Directory containing ROMs")
    args = parser.parse_args(argv)

    if args.path is None:
        response = input("Enter ROM directory (leave blank for current directory): ").strip()
        args.path = Path(response) if response else Path.cwd()
    else:
        args.path = Path(args.path)

    # placeholder for the full script; users can replace with the latest
    print(
        "ZRom Cleaner skeleton script is bundled. Replace with your full zrom_cleaner.py if needed."
    )
    print("Run: python zrom_cleaner.py /path/to/roms --regions U E UK J W --apply")
    print(f"Using ROM directory: {args.path}")
if __name__ == "__main__":
    main()
