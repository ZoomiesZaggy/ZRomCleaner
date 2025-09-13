#!/usr/bin/env python3
"""ZRom Cleaner – minimal CLI with exclude + prompt support.

Scans a directory tree and prints discovered files, with support for
--exclude globs. Excludes are matched against paths *relative to the scan
root* and can be provided multiple times or as comma-separated lists.

Examples:
  python zrom_cleaner.py demo/roms -x cache/ -x "*.nfo,*.txt" -vv
"""

from __future__ import annotations

import argparse
import fnmatch
import logging
import os
from pathlib import Path
from typing import Iterable, List

# ---------------------------------------------------------------------------
# Logging helpers (INFO / DEBUG / TRACE)

TRACE_LEVEL_NUM = 5
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")


def _trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE_LEVEL_NUM):
        self._log(TRACE_LEVEL_NUM, message, args, **kwargs)


logging.Logger.trace = _trace  # type: ignore[attr-defined]


def determine_log_level(verbosity: int) -> int:
    """0 -> INFO, 1 -> DEBUG, 2+ -> TRACE."""
    if verbosity >= 2:
        return TRACE_LEVEL_NUM
    if verbosity == 1:
        return logging.DEBUG
    return logging.INFO


# ---------------------------------------------------------------------------
# Exclude handling

def _normalize_patterns(patterns: Iterable[str]) -> list[str]:
    """
    Normalize glob patterns so they behave as users expect:
      - use POSIX separators,
      - strip trailing slashes,
      - prefix with '**/' so patterns match anywhere under root,
      - if the user targeted a directory (had trailing '/'), also add '/**'.
    """
    norm: list[str] = []
    for p in patterns or []:
        p = p.strip()
        if not p:
            continue
        is_dir = p.endswith(("/", "\\"))
        p = p.replace("\\", "/").rstrip("/")
        if not p:
            continue
        p_anywhere = p if p.startswith("**/") else f"**/{p}"
        norm.append(p_anywhere)
        if is_dir and not p_anywhere.endswith("/**"):
            norm.append(p_anywhere + "/**")

    # de-dupe, keep order
    seen: set[str] = set()
    out: list[str] = []
    for pat in norm:
        if pat not in seen:
            seen.add(pat)
            out.append(pat)
    return out


def _should_exclude(item: Path, root: Path, patterns: Iterable[str]) -> bool:
    """Return True if *item* should be excluded according to *patterns*."""
    pats = _normalize_patterns(patterns)
    if not pats:
        return False

    # Compare using path relative to root so globs behave as expected.
    rel = item.resolve().relative_to(root.resolve())
    rel_posix = rel.as_posix()

    # Windows: do case-insensitive matching to feel natural.
    hay = rel_posix.lower() if os.name == "nt" else rel_posix

    for pat in pats:
        target = pat.lower() if os.name == "nt" else pat
        if fnmatch.fnmatch(hay, target):
            return True
    return False


def _scan(root: Path, excludes: Iterable[str]) -> List[Path]:
    """
    Return all files under *root*, skipping anything that matches *excludes*.
    We prune excluded directories during traversal for speed.
    """
    results: List[Path] = []
    root = root.resolve()
    pats = _normalize_patterns(excludes)

    for dirpath, dirnames, filenames in os.walk(root, topdown=True):
        dpath = Path(dirpath)

        # Prune directories in-place so we don't descend into excluded trees.
        keep_dirs: list[str] = []
        for d in dirnames:
            p = dpath / d
            if not _should_exclude(p, root, pats):
                keep_dirs.append(d)
        dirnames[:] = keep_dirs

        # Files
        for f in filenames:
            p = dpath / f
            if _should_exclude(p, root, pats):
                continue
            results.append(p)

    return results


# ---------------------------------------------------------------------------
# CLI

def _split_excludes(values: list[str] | None) -> list[str]:
    """Split repeatable/comma-separated -x/--exclude values into a flat list."""
    pats: list[str] = []
    for v in values or []:
        pats.extend([p.strip() for p in v.split(",") if p.strip()])
    return pats


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """
    Parse args but *tolerate unknown flags* so README examples like
    '--regions ... --apply' don't fail in this skeleton.
    """
    parser = argparse.ArgumentParser(description="ZRom Cleaner (minimal CLI)")
    parser.add_argument(
        "path",
        nargs="?",
        help="Path to scan (default: prompt; blank = current directory)",
    )
    parser.add_argument(
        "-x", "--exclude",
        action="append",
        default=[],
        metavar="GLOB[,GLOB...]",
        help="Exclude paths by glob (repeatable). Examples: -x cache/ -x '*.nfo,*.txt'",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="Increase log verbosity: none=INFO, -v=DEBUG, -vv=TRACE",
    )
    args, unknown = parser.parse_known_args(argv)
    # keep unknowns for logging only; the real app would parse them
    setattr(args, "_unknown", unknown)
    return args


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    logging.basicConfig(
        level=determine_log_level(args.verbose),
        format="%(levelname)s: %(message)s",
    )
    log = logging.getLogger("zrom_cleaner")

    # Interactive prompt when no path supplied
    if args.path is None:
        try:
            response = input("Enter ROM directory (leave blank for current directory): ").strip()
        except EOFError:
            response = ""
        root = Path(response) if response else Path.cwd()
    else:
        root = Path(args.path)

    root = root.resolve()
    excludes = _split_excludes(args.exclude)

    if getattr(args, "_unknown", None):
        log.debug("Ignoring unknown args (skeleton): %s", " ".join(args._unknown))

    log.info("Scanning: %s", root)
    if excludes:
        log.debug("Excludes: %s", excludes)

    for path in _scan(root, excludes):
        print(path)


if __name__ == "__main__":
    main()
