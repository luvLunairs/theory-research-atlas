"""Check the delivered proof package's exact inventory using the stdlib."""
from pathlib import Path, PurePosixPath
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def main():
    manifest_path = ROOT / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    excluded = set(manifest["excluded_files"])
    records = manifest["files"]
    expected = {}
    for record in records:
        name = record["path"]
        parts = PurePosixPath(name)
        if parts.is_absolute() or ".." in parts.parts or "\\" in name:
            raise ValueError("Unsafe manifest path")
        if name in expected:
            raise ValueError("Duplicate manifest entry")
        expected[name] = record
    actual = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.relative_to(ROOT).as_posix() not in excluded
    }
    if actual != set(expected):
        raise ValueError(
            f"File inventory differs: missing={sorted(set(expected) - actual)}, "
            f"extra={sorted(actual - set(expected))}"
        )
    for name, record in expected.items():
        data = (ROOT / name).read_bytes()
        if len(data) != record["bytes"]:
            raise ValueError(f"Byte count differs: {name}")
        if hashlib.sha256(data).hexdigest() != record["sha256"]:
            raise ValueError(f"Digest differs: {name}")
    print(json.dumps({
        "pass": True,
        "payload_files": len(records),
        "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
    }, indent=2))


if __name__ == "__main__":
    main()
