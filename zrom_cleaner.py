#!/usr/bin/env python3
"""Minimal ZRom Cleaner CLI.

This skeleton script provides a tiny subset of the real project so that
documentation examples can run in tests.  It exposes a small command line
interface that scans a directory tree and prints discovered files.  The actual
project contains a much richer implementation.

The goal of this repository task is to demonstrate adding an ``--exclude``
argument which accepts glob patterns to ignore during the scan.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable, List


def _build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI.

    Only a very small subset of the real application's arguments are
    implemented here.  ``--exclude`` accepts one or more glob patterns and can
    be provided multiple times to build up the list of patterns.
    """

    parser = argparse.ArgumentParser(description="Toy ZRom Cleaner CLI")
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to scan for ROM files (default: current directory)",
    )
    parser.add_argument(
        "--exclude",
        action="extend",
        nargs="+",
        default=[],
        metavar="GLOB",
        help=(
            "Glob patterns to ignore while scanning. "
            "May be provided multiple times."
        ),
    )
    return parser


def _should_exclude(path: Path, patterns: Iterable[str]) -> bool:
    """Return ``True`` if *path* matches any of *patterns*.

    ``Path.match`` is used for glob style matching.
    """

    for pattern in patterns:
        if path.match(pattern):
            return True
    return False


def _scan(root: Path, excludes: Iterable[str]) -> List[Path]:
    """Return a list of files under *root* ignoring ``excludes``."""

    results: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        dirnames[:] = [
            d for d in dirnames if not _should_exclude(current / d, excludes)
        ]
        for name in filenames:
            path = current / name
            if _should_exclude(path, excludes):
                continue
            results.append(path)
    return results


def main() -> None:
    """CLI entry point."""

    parser = _build_parser()
    args = parser.parse_args()

    excludes = args.exclude

    root = Path(args.path).resolve()
    for path in _scan(root, excludes):
        print(path)


if __name__ == "__main__":
    main()
