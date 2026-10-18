"""Read-only replay of the selected published research artifacts. MIT.

This contributor check is not independent or formal verification. It imports
only the three retained helpers, never their result-writing main functions.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path, PurePosixPath
import platform
import re
import sys
import time


ROOT = Path(__file__).resolve().parent
CURRENT = "work/greedy-analytic-audit-20261018/"
OLD = "work/greedy-analytic-20261018/"
REPORT_NAME = "reproducibility-results.json"
sys.dont_write_bytecode = True


class CheckError(ValueError):
    """A checked package condition failed."""


def require(condition, message):
    if not condition:
        raise CheckError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    def invalid_constant(value):
        raise CheckError(f"Non-JSON numeric constant in {path.name}: {value}")
    return json.loads(path.read_text(encoding="utf-8"), parse_constant=invalid_constant)


def relative_name(value):
    require(isinstance(value, str) and bool(value), "An artifact path is missing")
    require("\\" not in value and ":" not in value, f"Nonportable artifact path: {value}")
    path = PurePosixPath(value)
    require(not path.is_absolute() and all(p not in (".", "..", "") for p in value.split("/")),
            f"Artifact path is not a normalized relative path: {value}")
    return value


def package_path(name):
    name = relative_name(name)
    path = ROOT / name
    require(path.resolve().is_relative_to(ROOT), f"Artifact escapes the package: {name}")
    return path


def digest(value, label):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None,
            f"Invalid SHA-256 for {label}")
    return value


def package_files():
    result = {}
    for path in sorted(ROOT.rglob("*")):
        require(not path.is_symlink(), f"Unexpected symbolic link: {path.relative_to(ROOT)}")
        if path.is_file() and path != ROOT / "manifest.json":
            name = path.relative_to(ROOT).as_posix()
            result[name] = {"sha256": sha(path), "bytes": path.stat().st_size}
    return result


def verify_manifest(actual):
    manifest = read_json(ROOT / "manifest.json")
    expected = manifest.get("files")
    require(isinstance(expected, dict), "Manifest has no files dictionary")
    for name, record in expected.items():
        package_path(name)
        require(isinstance(record, dict), f"Invalid manifest record: {name}")
        digest(record.get("sha256"), name)
        require(type(record.get("bytes")) is int and record["bytes"] >= 0,
                f"Invalid manifest byte count: {name}")
    require(set(expected) == set(actual),
            "Manifest file-list mismatch; missing=" + repr(sorted(set(expected) - set(actual)))
            + "; unexpected=" + repr(sorted(set(actual) - set(expected))))
    for name, record in actual.items():
        require(record == {key: expected[name][key] for key in ("sha256", "bytes")},
                f"Manifest size/hash mismatch: {name}")


def source_mapping():
    document = read_json(ROOT / "source-map.json")
    entries = document.get("files")
    require(isinstance(entries, list) and bool(entries), "Source map has no file entries")
    require(isinstance(document.get("omitted_links"), list), "Source map has no omitted-links list")
    mapped, destinations = {}, set()
    for entry in entries:
        require(isinstance(entry, dict), "Invalid source-map entry")
        source = relative_name(entry.get("source"))
        require(source.startswith("work/"), f"Unexpected original-source identifier: {source}")
        destination = relative_name(entry.get("destination"))
        require(destination.startswith("contents/"), f"Unexpected publication destination: {destination}")
        require(source not in mapped and destination not in destinations,
                f"Duplicate source or destination: {source}")
        digest(entry.get("source_sha256"), source)
        digest(entry.get("published_sha256"), destination)
        require(isinstance(entry.get("changes"), list), f"Missing changes list: {source}")
        path = package_path(destination)
        require(path.is_file(), f"Missing mapped artifact: {destination}")
        require(sha(path) == entry["published_sha256"], f"Published hash mismatch: {destination}")
        mapped[source] = entry
        destinations.add(destination)
    actual_contents = {p.relative_to(ROOT).as_posix() for p in (ROOT / "contents").rglob("*") if p.is_file()}
    require(actual_contents == destinations, "Source map does not cover exactly the contents/ file set")
    return mapped


def syntax_checks(actual):
    counts = {"python": 0, "json": 0}
    for name in actual:
        path = package_path(name)
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="utf-8"), filename=name)
            counts["python"] += 1
        elif path.suffix == ".json":
            read_json(path)
            counts["json"] += 1
    return counts


def import_helper(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"Cannot import helper: {path.name}")
    helper = importlib.util.module_from_spec(spec)
    sys.modules[name] = helper
    spec.loader.exec_module(helper)
    return helper


def replay(mapped):
    bindings = {}

    def path(source):
        require(source in mapped, f"Required source is not mapped: {source}")
        return package_path(mapped[source]["destination"])

    def binding(source, expected):
        expected = digest(expected, source)
        require(source in mapped, f"Unmapped retained hash binding: {source}")
        entry = mapped[source]
        require(entry["source_sha256"] == expected, f"Original hash binding mismatch: {source}")
        bindings[source] = {key: entry[key] for key in
                            ("destination", "source_sha256", "published_sha256")}

    # Code and retained outcome reports must remain byte-identical. Markdown
    # may have disclosed publication changes; both digests are kept distinct.
    preserved = ("framework_checks.py", "framework-checks.json",
                 "small/printed_audit.py", "small/printed-results.json",
                 "four/check_printed.py", "four/printed-results.json")
    for name in preserved:
        source = CURRENT + name
        path(source)
        require(mapped[source]["source_sha256"] == mapped[source]["published_sha256"],
                f"Retained helper or report has changed: {source}")

    framework = read_json(path(CURRENT + "framework-checks.json"))
    require(set(framework["hashes"]) == {"framework.md", "framework_checks.py"},
            "Unexpected framework binding set")
    for name, expected in framework["hashes"].items():
        binding(CURRENT + name, expected)
    helper = import_helper("published_framework_checks", path(CURRENT + "framework_checks.py"))
    framework_actual = helper.check()
    require(framework_actual == framework["results"] and framework["outcome"] == "pass",
            "Framework mathematical outcomes differ")
    require(framework["independent_verification"] is False and framework["formal_verification"] is False,
            "Unexpected framework verification status")

    small = read_json(path(CURRENT + "small/printed-results.json"))
    small_inputs = {OLD + "even-multiples/boundary-lifetime-tables.md",
                    OLD + "even-multiples/boundary-arithmetic-tables.md", OLD + "finite-small.md"}
    require(set(small["input_sha256"]) == small_inputs, "Unexpected small-table binding set")
    for source, expected in small["input_sha256"].items():
        binding(source, expected)
    binding(CURRENT + "small/printed_audit.py", small["checker_sha256"])
    helper = import_helper("published_small_checks", path(CURRENT + "small/printed_audit.py"))
    helper.LIFE = path(OLD + "even-multiples/boundary-lifetime-tables.md")
    helper.ARITH = path(OLD + "even-multiples/boundary-arithmetic-tables.md")
    helper.FINITE = path(OLD + "finite-small.md")
    lifetime = helper.sections(helper.LIFE.read_text(encoding="utf-8"))
    arithmetic = helper.sections(helper.ARITH.read_text(encoding="utf-8"))
    require(set(lifetime) == set(arithmetic) == {12, 18, 24}, "Unexpected fixed small-seed cases")
    small_actual = {
        "cases": [helper.fixed_case(g, modulus, body, arithmetic[g][1])
                  for g, (modulus, body) in sorted(lifetime.items())],
        "finite_first_seed_two": helper.finite_small(),
    }
    require(all(value == small[key] for key, value in small_actual.items()) and small["status"] == "passed",
            "Small-table mathematical outcomes differ")

    four = read_json(path(CURRENT + "four/printed-results.json"))
    four_inputs = {
        OLD + "upper/f4-fixed.md", OLD + "upper/f4-fixed-tables.md",
        OLD + "small/f4-zero-exclusion.md", OLD + "even-multiples/f4-zero-coverage.md",
        OLD + "even-multiples/f4-coverage-tables.md", CURRENT + "four/anchor-compression.md",
    }
    normalized = {"work/" + name.replace("\\", "/"): expected for name, expected in four["hashes"].items()}
    require(set(normalized) == four_inputs and len(normalized) == len(four["hashes"]),
            "Unexpected four-table binding set")
    for source, expected in normalized.items():
        binding(source, expected)
    binding(CURRENT + "four/check_printed.py", four["code_sha256"])
    helper = import_helper("published_four_checks", path(CURRENT + "four/check_printed.py"))
    helper.WORK = ROOT / "contents"
    helper.OLD = ROOT / "contents/greedy-analytic-20261018"
    helper.INPUTS = [path(source) for source in sorted(four_inputs)]
    text = {p.name: p.read_text(encoding="utf-8") for p in helper.INPUTS}
    four_actual = {
        "fixed": helper.audit_fixed(text["f4-fixed-tables.md"]),
        "uniform_coverage": helper.audit_coverage(text["f4-zero-coverage.md"], text["f4-coverage-tables.md"]),
        "uniform_exclusion": helper.audit_uniform_exclusion(text["f4-zero-coverage.md"], text["f4-zero-exclusion.md"]),
        "compressed_anchor": helper.audit_compression(text["anchor-compression.md"]),
    }
    require(all(value == four[key] for key, value in four_actual.items()), "Four-table mathematical outcomes differ")
    for flag in ("old_code_imported_or_executed", "new_greedy_scan", "independent_verification", "formal_verification"):
        require(four[flag] is False, f"Unexpected retained four-table flag: {flag}")
    require(len(bindings) == 13, "Unexpected evidence binding count")
    return {"framework": framework_actual, "small": small_actual, "four": four_actual}, dict(sorted(bindings.items()))


def stable_report(report):
    return {key: value for key, value in report.items() if key not in ("runtime", "measurements")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--verify-manifest", action="store_true", help="Verify the exact final file set, hashes and retained replay")
    modes.add_argument("--write-report", action="store_true", help="Write only reproducibility-results.json after all checks pass")
    args = parser.parse_args()
    require(sys.version_info >= (3, 10), "Python 3.10 or later is required")
    require(sys.flags.optimize == 0 and __debug__, "Assertions are required; do not use -O, -OO or PYTHONOPTIMIZE")
    cpu, wall = time.process_time(), time.perf_counter()
    before = package_files()
    if args.verify_manifest:
        verify_manifest(before)
        require(REPORT_NAME in before, "Manifest verification requires a retained reproducibility report")
    syntax = syntax_checks(before)
    mapped = source_mapping()
    outcomes, bindings = replay(mapped)
    report = {
        "version": "2026-10-18-portable-analytic-replay-v1", "status": "passed",
        "results": outcomes, "source_bindings": bindings,
        "source_map_sha256": sha(ROOT / "source-map.json"), "replay_sha256": sha(Path(__file__)),
        "independent_verification": False, "formal_verification": False, "new_greedy_scan": False,
        "limits": "Same-team contributor replay of retained arithmetic and finite framework probes. Does not establish the whole proof, novelty, scientific acceptance, source authenticity, or human review.",
        "runtime": {"python": platform.python_version(), "implementation": platform.python_implementation(), "optimization": sys.flags.optimize},
        "measurements": {"process_cpu_seconds": time.process_time() - cpu, "wall_seconds": time.perf_counter() - wall},
    }
    report_path = ROOT / REPORT_NAME
    if not args.write_report and report_path.exists():
        require(stable_report(report) == stable_report(read_json(report_path)),
                "Retained publication replay, source mapping or checker version differs")
    require(package_files() == before, "Replay unexpectedly changed the package file set or bytes")
    if args.write_report:
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {len(mapped)} mapped files and 13 original-source evidence bindings; {syntax['python']} Python and {syntax['json']} JSON syntax checks.")
    print("PASS: retained framework, small-seed and first-seed-four arithmetic outcomes reproduced.")
    if args.verify_manifest:
        print(f"PASS: exact manifest file set, sizes and SHA-256 hashes for {len(before)} files.")
    if args.write_report:
        print(f"WROTE: {REPORT_NAME}; include its new digest in the publication manifest.")
    else:
        print("Read-only: package files and retained reports were unchanged.")
    print("Same-team contributor check; no independent, formal, scientific or human-review approval.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (CheckError, AssertionError, OSError, ValueError, KeyError, TypeError) as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr)
        raise SystemExit(1)
