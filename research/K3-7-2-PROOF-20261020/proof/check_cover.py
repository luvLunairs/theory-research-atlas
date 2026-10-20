#!/usr/bin/env python3
"""Independent exact checker for ternary length-7, radius-2 covering codes.

Input is UTF-8 text, one seven-digit word per nonempty line. Blank lines are
ignored; comments, other characters, duplicate words and empty codes are rejected.
The checker explicitly visits every point and directly counts coordinate
inequalities to every codeword. It imports no search code, precomputed incidence
matrix, numerical library or solver.

Exit status: 0 = radius-2 cover; 1 = valid input but not a cover; 2 = bad input.
Original code is covered by the repository MIT license. AI assistance is disclosed
in the enclosing research draft; this is a claim-specific check, not a formal
verification or an independent human review.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path


def read_code(path: Path) -> tuple[bytes, list[str]]:
    """Validate the complete file before doing any covering computation."""
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    words: list[str] = []
    first_line: dict[str, int] = {}
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        # Do not silently trim a malformed word or accept annotations.
        if len(line) != 7 or any(symbol not in "012" for symbol in line):
            raise ValueError(
                f"line {line_number}: expected exactly seven symbols from 0,1,2"
            )
        if line in first_line:
            raise ValueError(
                f"line {line_number}: duplicate {line!r}; first occurs on line "
                f"{first_line[line]}"
            )
        first_line[line] = line_number
        words.append(line)
    if not words:
        raise ValueError("the code must contain at least one word")
    return raw, words


def check_code(words: list[str]) -> dict:
    """Enumerate all 3**7 points, without sphere generation or search routines."""
    nearest_histogram: Counter[int] = Counter()
    multiplicity_histogram: Counter[int] = Counter()
    uncovered: list[str] = []
    farthest: str | None = None
    covering_radius = -1
    for point_tuple in itertools.product("012", repeat=7):
        point = "".join(point_tuple)
        nearest = 8
        multiplicity = 0
        for center in words:
            distance = sum(a != b for a, b in zip(point, center))
            nearest = min(nearest, distance)
            if distance <= 2:
                multiplicity += 1
        nearest_histogram[nearest] += 1
        multiplicity_histogram[multiplicity] += 1
        if nearest > 2:
            uncovered.append(point)
        if nearest > covering_radius:
            covering_radius = nearest
            farthest = point
    visited = sum(nearest_histogram.values())
    incidences = sum(k * v for k, v in multiplicity_histogram.items())
    # These are internal sanity checks, additional to exhaustive distances.
    if visited != 2187:
        raise AssertionError("not every ambient word was visited")
    if incidences != len(words) * 99:
        raise AssertionError("the radius-2 incidence count is inconsistent")
    return {
        "alphabet": [0, 1, 2],
        "length": 7,
        "target_radius": 2,
        "ambient_words_checked": visited,
        "code_size": len(words),
        "covering_radius": covering_radius,
        "is_radius_2_cover": not uncovered,
        "distance_to_code_histogram": dict(sorted(nearest_histogram.items())),
        "radius_2_coverage_multiplicity_histogram": dict(
            sorted(multiplicity_histogram.items())
        ),
        "radius_2_ball_size": 99,
        "radius_2_total_incidences": incidences,
        "uncovered_count": len(uncovered),
        "uncovered_words": uncovered,
        "farthest_word_example": farthest,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code_file", type=Path)
    parser.add_argument("--json", dest="json_file", type=Path,
                        help="also retain the complete report at this path")
    args = parser.parse_args()
    try:
        if args.json_file and args.json_file.resolve() == args.code_file.resolve():
            raise ValueError("the JSON output must not overwrite the input code")
        raw, words = read_code(args.code_file)
        report = check_code(words)
        report.update({
            "input_file": str(args.code_file.resolve()),
            "input_file_sha256": hashlib.sha256(raw).hexdigest(),
            "normalized_sorted_code_sha256": hashlib.sha256(
                ("\n".join(sorted(words)) + "\n").encode("ascii")
            ).hexdigest(),
            "checker_file_sha256": hashlib.sha256(
                Path(__file__).read_bytes()
            ).hexdigest(),
            "method": "exhaustive coordinate comparisons, Python standard library",
        })
        rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if args.json_file:
            args.json_file.write_text(rendered, encoding="utf-8")
        print(rendered, end="")
        return 0 if report["is_radius_2_cover"] else 1
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))
        return 2  # argparse.error exits; this only documents the exit contract.


if __name__ == "__main__":
    raise SystemExit(main())
