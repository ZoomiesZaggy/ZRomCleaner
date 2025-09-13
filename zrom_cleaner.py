#!/usr/bin/env python3
"""Minimal CLI placeholder for ZRom Cleaner.

This skeleton script provides a small command line interface that accepts the
same flags as the full application.  The options currently only print the
parsed values so that command line examples in the documentation are valid.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def _build_parser() -> argparse.ArgumentParser:
    """Create an argument parser with placeholder options.

    Returns
    -------
    argparse.ArgumentParser
        Parser preloaded with arguments understood by the full application.
    """

    parser = argparse.ArgumentParser(description="ZRom Cleaner placeholder CLI")
    parser.add_argument(
        "path",
        nargs="?",
        default=Path.cwd(),
        type=Path,
        help="Path to the ROM directory (defaults to current working directory)",
    )
    parser.add_argument(
        "--regions",
        nargs="+",
        default=["U", "E", "J"],
        help="Region priority codes in order of preference",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply file operations (no-op in placeholder)",
    )
    parser.add_argument(
        "--report",
        metavar="FILE",
        help="Write a placeholder report to FILE",
    )
    parser.add_argument(
        "--keep-original-pair",
        action="store_true",
        help="Keep the original and best revision pair (placeholder)",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    """Entry point for the placeholder CLI."""

    parser = _build_parser()
    args = parser.parse_args(argv)

    print("ZRom Cleaner skeleton script is bundled.")
    print("Replace with your full zrom_cleaner.py if needed.")
    print(f"Path: {args.path}")
    print(f"Regions: {' '.join(args.regions)}")
    print(f"Apply operations: {args.apply}")
    if args.report:
        print(f"Report will be written to: {args.report} (placeholder)")
    if args.keep_original_pair:
        print("Original + best revision pairing enabled (placeholder)")


if __name__ == "__main__":  # pragma: no cover - direct execution
    main()

