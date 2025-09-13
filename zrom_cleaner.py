#!/usr/bin/env python3
"""Minimal ZRom Cleaner entry point.

This skeleton script ships with the repository so that users can drop in
their own full ``zrom_cleaner.py`` if desired.  For demonstration purposes the
CLI implements a handful of logging options that mirror the behaviour of the
project's real command line interface.
"""

from __future__ import annotations

import argparse
import logging
from typing import Iterable, Optional


# ---------------------------------------------------------------------------
# Logging helpers

TRACE_LEVEL = 5
logging.addLevelName(TRACE_LEVEL, "TRACE")


def _trace(self: logging.Logger, msg: str, *args, **kwargs) -> None:  # pragma: no cover - thin wrapper
    """Add ``Logger.trace`` similar to ``Logger.debug``."""
    if self.isEnabledFor(TRACE_LEVEL):
        self._log(TRACE_LEVEL, msg, args, **kwargs)


logging.Logger.trace = _trace  # type: ignore[attr-defined]


def _parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    """Create an ``ArgumentParser`` and parse ``argv``."""

    parser = argparse.ArgumentParser(
        description=(
            "ZRom Cleaner skeleton script is bundled. Replace with your full "
            "zrom_cleaner.py if needed."
        )
    )
    parser.add_argument("path", nargs="?", help="Path to ROM directory")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase logging verbosity: -v=INFO, -vv=DEBUG, -vvv=TRACE",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Only show errors (sets logging level to ERROR)",
    )
    return parser.parse_args(argv)


def _log_level(args: argparse.Namespace) -> int:
    """Translate ``--verbose``/``--quiet`` flags to a logging level."""

    if args.quiet:
        return logging.ERROR

    # Map 0->WARNING, 1->INFO, 2->DEBUG and 3+->TRACE
    return {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}.get(
        args.verbose, TRACE_LEVEL
    )


def main(argv: Optional[Iterable[str]] = None) -> None:
    """Entry point for the script."""

    args = _parse_args(argv)

    logging.basicConfig(level=_log_level(args), format="%(levelname)s: %(message)s")

    logger = logging.getLogger(__name__)
    logger.trace("Trace logging enabled")
    logger.debug("Debug logging enabled")
    logger.info("Info level logging enabled")
    logger.warning("Warning level logging enabled")
    logger.error("Error level logging enabled")

    print(
        "ZRom Cleaner skeleton script is bundled. Replace with your full zrom_cleaner.py if needed."
    )
    print(
        "Run: python zrom_cleaner.py /path/to/roms --regions U E UK J W --apply"
    )


if __name__ == "__main__":
    main()

