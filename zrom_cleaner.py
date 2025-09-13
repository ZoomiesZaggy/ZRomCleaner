#!/usr/bin/env python3
"""Minimal ZRom Cleaner CLI skeleton with logging controls."""

import argparse
import logging
from pathlib import Path
from typing import Sequence


TRACE_LEVEL = 5
logging.addLevelName(TRACE_LEVEL, "TRACE")


def _build_parser(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments and determine the log level."""

    parser = argparse.ArgumentParser(description="ZRom Cleaner")
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="ROM directory to clean",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity; can be supplied multiple times",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only display errors",
    )

    args = parser.parse_args(argv)

    if args.quiet:
        args.log_level = logging.ERROR
    else:
        verbosity_map = {
            0: logging.WARNING,
            1: logging.INFO,
            2: logging.DEBUG,
        }
        args.log_level = (
            TRACE_LEVEL if args.verbose >= 3 else verbosity_map.get(args.verbose, logging.WARNING)
        )
    return args


def main(argv: Sequence[str] | None = None) -> None:
    args = _build_parser(argv)
    logging.basicConfig(level=args.log_level)

    logging.debug("Running in debug mode")
    logging.log(TRACE_LEVEL, "Running in trace mode")
    print(
        "ZRom Cleaner skeleton script is bundled. Replace with your full zrom_cleaner.py if needed."
    )
    print("Run: python zrom_cleaner.py /path/to/roms --regions U E UK J W --apply")


if __name__ == "__main__":
    main()

