#!/usr/bin/env python3
"""Minimal command line entry point for ZRom Cleaner."""

import argparse
from pathlib import Path
from typing import Optional


def _validate_path(path_str: str) -> Path:
    """Validate that ``path_str`` points to an existing directory.

    Args:
        path_str: String representation of the path provided by the user.

    Returns:
        A resolved :class:`~pathlib.Path` instance.

    Raises:
        FileNotFoundError: If the path does not exist.
        NotADirectoryError: If the path exists but is not a directory.
    """

    path = Path(path_str).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {path}")
    return path


def _parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description="ZRom Cleaner skeleton script")
    parser.add_argument("path", nargs="?", help="Directory containing ROMs to clean")
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> None:
    """Entry point used by the command line interface."""

    args = _parse_args(argv)
    path_str = args.path
    if path_str is None:
        # Prompt the user for a directory if no path argument was supplied.
        path_str = input("Enter ROM directory [current directory]: ").strip()
        if path_str == "":
            path_str = "."

    path = _validate_path(path_str)

    # placeholder for the full script; users can replace with the latest
    print(
        "ZRom Cleaner skeleton script is bundled. Replace with your full zrom_cleaner.py if needed."
    )
    print("Run: python zrom_cleaner.py /path/to/roms --regions U E UK J W --apply")
    print(f"Validated path: {path}")


if __name__ == "__main__":
    main()
