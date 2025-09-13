#!/usr/bin/env python3
"""Minimal CLI entry point for the ZRom Cleaner skeleton script."""

import argparse
import logging
import sys
from pathlib import Path


def _build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the skeleton script."""

    parser = argparse.ArgumentParser(description="ZRom Cleaner skeleton script")
    parser.add_argument("path", nargs="?", default=".", help="ROM folder")
    parser.add_argument(
        "--log-file",
        type=Path,
        help="write log output to this file in addition to the console",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    handlers = [logging.StreamHandler()]
    if args.log_file:
        handlers.append(logging.FileHandler(args.log_file))

    logging.basicConfig(level=logging.INFO, handlers=handlers, format="%(message)s")

    logging.info(
        "ZRom Cleaner skeleton script is bundled. Replace with your full zrom_cleaner.py if needed."
    )
    logging.info(
        "Run: python zrom_cleaner.py /path/to/roms --regions U E UK J W --apply"
    )


if __name__ == "__main__":
    main()

