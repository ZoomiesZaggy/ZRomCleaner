#!/usr/bin/env python3
"""Minimal entry calling GUI if no args else CLI.

This skeleton focuses on demonstrating command line parsing. The real
project uses a far more feature rich script. Replace this file with the
latest ``zrom_cleaner.py`` if you need the full application.
"""

import argparse
import configparser
import json
import sys
from pathlib import Path
from typing import Any, Dict, List


def _build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser.

    A ``--config`` option is available to load defaults from a JSON or INI
    file. Values provided explicitly on the command line override those
    found in the configuration file.
    """

    parser = argparse.ArgumentParser(description="ZRom Cleaner CLI")
    parser.add_argument("path", nargs="?", help="ROM directory", default=None)
    parser.add_argument(
        "--regions",
        nargs="+",
        help="Region priority, e.g. U E UK J W",
    )
    parser.add_argument("--report", help="Write CSV report to file")
    parser.add_argument(
        "--keep-original-pair",
        action="store_true",
        help="Keep original paired with best revision",
    )
    parser.add_argument("--apply", action="store_true", help="Apply changes")
    parser.add_argument(
        "--config", help="Path to JSON or INI config file providing defaults"
    )
    return parser


def _load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration values from *config_path*.

    Supports either JSON or INI files. Values are returned as a dictionary
    keyed by the parser's destination names.
    """

    data: Dict[str, Any] = {}
    path = Path(config_path)
    if not path.exists():
        return data

    try:
        if path.suffix.lower() == ".json":
            data = json.loads(path.read_text())
        else:
            parser = configparser.ConfigParser()
            parser.read(path)
            section = parser.sections()[0] if parser.sections() else parser.default_section
            data = dict(parser[section])
    except Exception:
        # If the config fails to load we simply ignore it and fall back to
        # command line defaults.
        return {}

    # Normalise known options
    if "regions" in data and isinstance(data["regions"], str):
        # Split on whitespace to form a list of region codes
        data["regions"] = data["regions"].split()

    for flag in ["keep_original_pair", "apply"]:
        if flag in data:
            value = str(data[flag]).lower()
            data[flag] = value in {"1", "true", "yes", "on"}

    return data


def _parse_args(argv: List[str]) -> argparse.Namespace:
    """Parse command line arguments, merging config file values."""

    parser = _build_parser()
    # First parse just to discover --config
    preliminary, _ = parser.parse_known_args(argv)

    config: Dict[str, Any] = {}
    if preliminary.config:
        config = _load_config(preliminary.config)
        if config:
            # Only apply config keys that match known parser destinations
            valid = {action.dest for action in parser._actions}
            parser.set_defaults(**{k: v for k, v in config.items() if k in valid})

    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    # placeholder for the full script; users can replace with the latest
    args = _parse_args(argv or sys.argv[1:])
    print(
        "ZRom Cleaner skeleton script is bundled. Replace with your full"
        " zrom_cleaner.py if needed."
    )
    print("Parsed arguments:")
    for key, value in vars(args).items():
        print(f"  {key}: {value}")
    print("Run: python zrom_cleaner.py /path/to/roms --regions U E UK J W --apply")


if __name__ == "__main__":
    main()
