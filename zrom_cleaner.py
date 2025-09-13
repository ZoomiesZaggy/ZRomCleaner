#!/usr/bin/env python3
"""Minimal CLI stub for ZRom Cleaner.

This simplified script demonstrates argument parsing and logging behaviour. It
is intended as a placeholder and can be replaced with the full project script
when available.
"""

import argparse
import logging
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Logging helpers

# Python's logging module does not include a TRACE level by default.  Define a
# custom level that sits below ``DEBUG`` so ``-vv`` can enable it.
TRACE_LEVEL_NUM = 5
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")


def _trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE_LEVEL_NUM):
        self._log(TRACE_LEVEL_NUM, message, args, **kwargs)


logging.Logger.trace = _trace  # type: ignore[attr-defined]


def determine_log_level(verbosity: int) -> int:
    """Map ``-v`` occurrences to logging levels.

    ``0`` -> ``logging.INFO``
    ``1`` -> ``logging.DEBUG``
    ``2+`` -> ``TRACE_LEVEL_NUM``
    """

    if verbosity >= 2:
        return TRACE_LEVEL_NUM
    if verbosity == 1:
        return logging.DEBUG
    return logging.INFO


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description="ZRom Cleaner (skeleton)")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help=(
            "Increase log output: none=INFO, -v=DEBUG, -vv=TRACE "
            "(uses a custom TRACE level below DEBUG)."
        ),
    )
    # Real script would define more options here.
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Entry point for the CLI."""

    args = parse_args(argv)

    # Configure logging based on the requested verbosity.
    logging.basicConfig(level=determine_log_level(args.verbose), format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    logger.info(
        "ZRom Cleaner skeleton script is bundled. Replace with your full zrom_cleaner.py if needed."
    )
    logger.info("Run: python zrom_cleaner.py /path/to/roms --regions U E UK J W --apply")
    logger.debug("Debug logging is enabled.")
    logger.trace("Trace level active.")


if __name__ == "__main__":
    main()
