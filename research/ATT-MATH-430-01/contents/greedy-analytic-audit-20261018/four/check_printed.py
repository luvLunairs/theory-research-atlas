"""Read-only audit of literal Markdown arithmetic; imports no earlier checker.

Run from any directory. Writes only this folder's printed-results.json.
This is same-team contributor checking, not independent/formal verification.
"""
from pathlib import Path
from itertools import combinations_with_replacement, product
import hashlib
import json
import platform
import re
import time

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[1]
OLD = WORK / "greedy-analytic-20261018"
INPUTS = [
    OLD / "upper/f4-fixed.md", OLD / "upper/f4-fixed-tables.md",
    OLD / "small/f4-zero-exclusion.md",
    OLD / "even-multiples/f4-zero-coverage.md",
    OLD / "even-multiples/f4-coverage-tables.md",
    HERE / "anchor-compression.md",
]


def norm(parts):
    out = []
    for lo, hi in sorted(parts, key=lambda p: p[0]):
        if hi is not None and lo > hi:
            continue
        if out and (out[-1][1] is None or lo <= out[-1][1] + 1):
            prev = out.pop()
            out.append((prev[0], None if prev[1] is None or hi is None else max(prev[1], hi)))
        else:
            out.append((lo, hi))
    return out


def parse_life(s):
    s = s.strip()
    if s == "empty":
        return []
    parts = []
    for t in s.split(" union "):
        if t.startswith("["):
            lo, hi = t[1:-1].split(",")
            parts.append((int(lo), None if hi == "infinity" else int(hi)))
        else:
            parts.append((int(t), int(t)))
    return norm(parts)


def life_sum(a, b, same, carry):
    out = []
    for i, (lo, hi) in enumerate(a):
        for j, (ll, hh) in enumerate(b):
            if same and j < i:
                continue
            if same and i == j:
                out.append((2 * lo + 1 + carry, None if hi is None else 2 * hi - 1 + carry))
            else:
                out.append((lo + ll + carry, None if hi is None or hh is None else hi + hh + carry))
    return norm(out)


def complement(life, start):
    out, pos = [], start
    for lo, hi in life:
        if hi is not None and hi < pos:
            continue
        if lo > pos:
            out.append((pos, lo - 1))
        if hi is None:
            return out
        pos = max(pos, hi + 1)
    out.append((pos, None))
    return out


def clipped(life, start):
    return norm((max(lo, start), hi) for lo, hi in life)


def audit_fixed(text):
    cases, mode, cur = [], None, None
    for line_number, line in enumerate(text.splitlines(), 1):
        h = re.fullmatch(r"## Seeds 4,(\d+); modulus (\d+)", line)
        if h:
            cur = {"g": int(h[1]), "m": int(h[2]), "life": {}, "exclusion": [], "coverage": []}
            cases.append(cur)
        elif line == "### Selected lifetimes":
            mode = "life"
        elif line == "### Complete pair exclusion at supported residues":
            mode = "exclusion"
        elif line == "### Coverage at the other residues":
            mode = "coverage"
        elif re.match(r"\| \d", line):
            cells = [x.strip() for x in line.strip("|").split("|")]
            if mode == "life":
                for r in map(int, cells[0].split(",")):
                    assert r not in cur["life"], (line_number, "duplicate selected residue")
                    cur["life"][r] = parse_life(cells[1])
            else:
                cur[mode].append((line_number, cells))
    reports = []
    for case in cases:
        g, m, life = case["g"], case["m"], case["life"]
        assert all(0 <= r < m for r in life)
        assert [r for r in sorted(life) if r <= g and life[r][0][0] == 0] == [4, g]
        all_pairs = {r: [] for r in life}
        for a, b in combinations_with_replacement(sorted(life), 2):
            r = (a + b) % m
            if r in life:
                all_pairs[r].append((a, b))
        seen, pair_count, witness_count = set(), 0, 0
        for line_number, (target, sources, stated) in case["exclusion"]:
            r = int(target)
            assert r not in seen
            seen.add(r)
            pairs = [] if sources == "none" else [tuple(map(int, p.split(":"))) for p in sources.split(", ")]
            assert pairs == all_pairs[r], (line_number, "source list is not exhaustive", pairs, all_pairs[r])
            actual = norm(p for a, b in pairs for p in life_sum(life[a], life[b], a == b, (a + b) // m))
            assert actual == parse_life(stated), (line_number, "wrong exact sum lifetime", actual, stated)
            assert clipped(actual, int(r <= g)) == complement(life[r], int(r <= g)), (line_number, "wrong complement")
            pair_count += len(pairs)
        assert seen == set(life)
        missing = set(range(m)) - seen
        for line_number, (target, sources) in case["coverage"]:
            r = int(target)
            assert r in missing, (line_number, "coverage residue missing or duplicated")
            missing.remove(r)
            supplied = []
            for item in sources.split("; "):
                a, b, stated = item.split(":", 2)
                a, b = int(a), int(b)
                assert a != b and (a + b) % m == r
                actual = life_sum(life[a], life[b], False, (a + b) // m)
                assert actual == parse_life(stated), (line_number, "wrong witness lifetime", actual, stated)
                supplied += actual
                witness_count += 1
            assert clipped(norm(supplied), int(r <= g)) == [(int(r <= g), None)], (line_number, "coverage gap")
        assert not missing
        reports.append({"g": g, "m": m, "supported_residues": len(life), "exclusion_pairs": pair_count,
                        "coverage_witnesses": witness_count, "all_integer_lifetimes": "exact identities matched"})
    return reports


# Affine expressions are pairs (coefficient of k, constant). No evaluation or
# numerical parameter sampling is used by the following coverage check.
def affine(s):
    s = s.strip()
    assert re.fullmatch(r"[+-]?(?:\d*k|\d+)(?:[+-]\d+)?", s), s
    if "k" not in s:
        return 0, int(s)
    a, b = s.split("k")
    return (1 if a in ("", "+") else -1 if a == "-" else int(a)), (int(b) if b else 0)


def add(x, y): return x[0] + y[0], x[1] + y[1]
def neg(x): return -x[0], -x[1]
def sub(x, y): return add(x, neg(y))
def plus(x, c): return add(x, (0, c))
def le(x, y):
    a, b = sub(y, x)
    return a >= 0 and 6 * a + b >= 0


def interval(s):
    s = s.strip().strip("`")
    if s.startswith("["):
        a, b = map(affine, s[1:-1].split(","))
    else:
        a = b = affine(s)
    assert le(a, b), s
    return a, b


def parse_blocks(text):
    blocks = {}
    for line in text.splitlines():
        if not re.match(r"\| (?:[0-5]|n>=6) \|", line):
            continue
        cells = [x.strip() for x in line.strip("|").split("|")]
        n = 6 if cells[0] == "n>=6" else int(cells[0])
        blocks[n] = {r: [interval(x) for x in cell.strip("`").split(";")] for r, cell in enumerate(cells[1:])}
    assert set(blocks) == set(range(7))
    return blocks


def actual_gaps(blocks, n, r):
    pos = (1, int(r == 0)) if n == 0 else (0, 0)
    end = (4, 0 if r == 0 else -1)
    out = []
    for lo, hi in blocks[min(n, 6)][r]:
        if le(plus(hi, 1), pos):
            continue
        if le(plus(pos, 1), lo):
            out.append((pos, plus(lo, -1)))
        else:
            assert le(lo, pos), (n, r, "unresolved endpoint order")
        pos = plus(hi, 1)
    if le(pos, end):
        out.append((pos, end))
    else:
        assert le(plus(end, 1), pos)
    return out


def audit_coverage(note, table):
    blocks = parse_blocks(note)
    factor = r"P_(\d+|n|\(n-1\))\(([0-7]):(\[[^\]]+\]|[^)]+)\)"
    pat = re.compile(factor + r" (\+|dotplus) " + factor + r" \(carry ([01])\): (.+)")
    n, seen, row_count, pair_count, strict_count = None, {}, 0, 0, 0
    for ln, line in enumerate(table.splitlines(), 1):
        h = re.fullmatch(r"## Block n=(\d)", line)
        if h:
            n = int(h[1])
        elif line == "## All n>=7":
            n = 7  # symbolic n in block-position comparisons; actual rows are R.
        elif re.match(r"\| [0-7]:", line):
            left, right = [x.strip() for x in line.strip("|").split("|")]
            r, gap = left.split(":")
            r, gap = int(r), interval(gap)
            seen.setdefault((n, r), []).append(gap)
            row_count += 1
            upto = None
            for item in right.split("; "):
                h = pat.fullmatch(item)
                assert h, (ln, "cannot parse printed witness", item)
                qtxt, rr, ii, op, ptxt, ss, jj, cc, kk = h.groups()
                def block_index(t):
                    return n if t == "n" else n - 1 if t == "(n-1)" else int(t)
                q, p, rr, ss, c = block_index(qtxt), block_index(ptxt), int(rr), int(ss), int(cc)
                assert q + p + c == n, (ln, "wrong actual block indices")
                if n == 7:
                    assert qtxt == "0" and ptxt in ("n", "(n-1)"), (ln, "nonuniform stable witness")
                I, J, stated = interval(ii), interval(jj), interval(kk)
                for b, residue, seg in ((q, rr, I), (p, ss, J)):
                    assert any(le(lo, seg[0]) and le(seg[1], hi) for lo, hi in blocks[min(b, 6)][residue]), (ln, "factor not selected")
                strict = op == "dotplus"
                if strict:
                    assert q == p and rr == ss and I == J and le(plus(I[0], 1), I[1]), (ln, "invalid strict self-sum")
                    strict_count += 1
                else:
                    assert q != p or rr != ss or le(plus(I[1], 1), J[0]) or le(plus(J[1], 1), I[0]), (ln, "actual factors may coincide")
                assert (rr + ss - c) % 8 == r, (ln, "wrong carried residue")
                shift = (-4 * c, (rr + ss - c) // 8)
                lo, hi = add(add(I[0], J[0]), shift), add(add(I[1], J[1]), shift)
                if strict:
                    lo, hi = plus(lo, 1), plus(hi, -1)
                assert (lo, hi) == stated, (ln, "wrong printed affine sum", (lo, hi), stated)
                if upto is None:
                    assert le(lo, gap[0]), (ln, "uncovered lower endpoint")
                else:
                    assert le(lo, plus(upto, 1)), (ln, "uncovered join")
                    assert le(upto, hi), (ln, "unordered coverage endpoints")
                upto = hi
                pair_count += 1
            assert le(gap[1], upto), (ln, "uncovered upper endpoint")
    for n in range(8):
        for r in range(8):
            assert seen.get((n, r), []) == actual_gaps(blocks, n, r), (n, r, "omitted interval transcription")
    return {"gap_rows": row_count, "pair_identities": pair_count, "strict_self_pairs": strict_count,
            "parameter_domain": "every integer k>=6 by affine coefficient inequalities", "block_domain": "n=0..6 and every n>=7"}


def possible_domain(inequalities, minimum=6):
    """Exact integer solution of a conjunction x(k)<=y(k), k>=minimum."""
    low, high = minimum, None
    for x, y in inequalities:
        a, b = sub(y, x)
        if a == 0:
            if b < 0:
                return None
        elif a > 0:
            low = max(low, -(b // a))  # ceil(-b/a), with exact integer division
        else:
            cap = b // (-a)
            high = cap if high is None else min(high, cap)
        if high is not None and low > high:
            return None
    return low, high


def audit_uniform_exclusion(note, exclusion):
    blocks = parse_blocks(note)
    fragment = exclusion.split("envelope H:", 1)[1].split("The following table", 1)[0]
    found = re.findall(r"\b([a-z])=([0-7]):(\[[^\]]+\]|\{[^}]+\})", fragment)
    assert len(found) == 13
    H = [(name, int(r), interval(seg[1:-1] if seg.startswith("{") else seg)) for name, r, seg in found]
    R = [(r, seg) for r, parts in blocks[6].items() for seg in parts]
    for n in range(7):
        for r, parts in blocks[n].items():
            for lo, hi in parts:
                assert le((0, 0), lo) and le(hi, (4, 0 if r == 0 else -1))
                assert any(s == r and le(I[0], lo) and le(hi, I[1]) for _, s, I in H), (n, r, "outside H")
    def sum_interval(r, I, s, J, c, strict):
        h = (-4 * c, (r + s - c) // 8)
        return (plus(add(add(I[0], J[0]), h), int(strict)),
                plus(add(add(I[1], J[1]), h), -int(strict)))
    collisions, checks = [], 0
    # Any pair with a selected input in a block >=6 has a target in a
    # block >=6, so ordinary H+R exclusion discharges every such pair.
    for name, r, I in H:
        for s, J in R:
            for c in (0, 1):
                target = (r + s - c) % 8
                lo, hi = sum_interval(r, I, s, J, c, False)
                for a, b in blocks[6][target]:
                    checks += 1
                    domain = possible_domain([(lo, hi), (lo, b), (a, hi)])
                    if domain:
                        collisions.append(("H+R", name, r, s, c, domain))
    assert not collisions, collisions
    finite_parts = [(q, r, I) for q in range(6) for r, parts in blocks[q].items() for I in parts]
    finite_checks = 0
    for i, (q, r, I) in enumerate(finite_parts):
        for j in range(i, len(finite_parts)):
            p, s, J = finite_parts[j]
            for c in (0, 1):
                target, n = (r + s - c) % 8, q + p + c
                lo, hi = sum_interval(r, I, s, J, c, i == j)
                for a, b in blocks[min(n, 6)][target]:
                    finite_checks += 1
                    domain = possible_domain([(lo, hi), (lo, b), (a, hi)])
                    if domain:
                        collisions.append(("two transient inputs", q, r, I, p, s, J, c, domain))
    assert not collisions, collisions
    # A deliberately attempted, mathematically false relaxation of the
    # literal recurring row. This is a refutation of that formula only.
    k, m = 5, 161
    terms = [6 * m + 40, 7 * m + 40, 13 * m + 80]
    def in_tail(x):
        n, offset = divmod(x, m)
        row, r = divmod(offset, 8)
        return n >= 6 and any(a[0] * k + a[1] <= row <= b[0] * k + b[1] for a, b in blocks[6][r])
    assert terms[0] != terms[1] and sum(terms[:2]) == terms[2] and all(map(in_tail, terms))
    return {"domain": "all integers k>=6, exact solutions of affine collision inequalities",
            "H_plus_R_intersections_tested": checks, "transient_input_intersections_tested": finite_checks,
            "possible_selected_collisions": collisions,
            "failed_extension_k5": {"m": m, "distinct_inputs": terms[:2], "selected_sum": terms[2]}}


def audit_compression(text):
    variables = "kabd"
    def poly(s):
        terms = re.findall(r"[+-]?(?:\d*[kabd]|\d+)", s)
        assert "".join(terms) == s, s
        out = [0] * 5
        for term in terms:
            if term[-1] in variables:
                c = term[:-1]
                out[variables.index(term[-1])] += 1 if c in ("", "+") else -1 if c == "-" else int(c)
            else:
                out[4] += int(term)
        return tuple(out)
    def addp(*parts): return tuple(map(sum, zip(*parts)))
    def inc(x, c): return addp(x, (0, 0, 0, 0, c))
    def lep(x, y):
        p = tuple(b - a for a, b in zip(x, y))
        if p[0] < 0:
            return False
        return 6 * p[0] + sum(c * (lo if c >= 0 else hi) for c, (lo, hi) in zip(p[1:4], ((2, 5), (2, 3), (2, 5)))) + p[4] >= 0
    def parse_int(s):
        if s.startswith("["):
            a, b = map(poly, s[1:-1].split(","))
        else:
            a = b = poly(s.strip("{}"))
        assert lep(a, b)
        return a, b
    fragment = text.split("## Thirteen gap identities", 1)[0]
    raw = re.findall(r"\b(I_[0-3]|X|[A-J](?:\^-)?)=([0-7]):(\[[^\]]+\]|\{[^}]+\})", fragment)
    source = {name: (int(r), parse_int(seg)) for name, r, seg in raw}
    assert len(source) == 17
    rows, identities, gaps = 0, 0, {}
    for ln, line in enumerate(text.splitlines(), 1):
        if not re.match(r"\| `[0-7]:", line):
            continue
        left, right = [x.strip() for x in line.strip("|").split("|")]
        rr, interval_text = left.strip("`").split(":")
        rr, gap = int(rr), parse_int(interval_text)
        gaps.setdefault(rr, []).append(gap)
        upto = None
        for item in right.split("; "):
            item = item.strip("`")
            factors, result = item.split(" -> ")
            first, second = factors.split("+")
            assert first in ("I_0", "I_1", "I_2", "I_3", "X")
            c = int(second.endswith("[n-1]"))
            assert c or second.endswith("[n]")
            second = second.split("[")[0]
            r, I = source[first]
            s, J = source[second]
            assert (r + s - c) % 8 == rr
            shift = (-4 * c, 0, 0, 0, (r + s - c) // 8)
            lo, hi = addp(I[0], J[0], shift), addp(I[1], J[1], shift)
            assert (lo, hi) == parse_int(result), (ln, "incorrect compressed identity")
            assert lep(lo, gap[0] if upto is None else inc(upto, 1)), (ln, "uncovered compressed join")
            if upto is not None:
                assert lep(upto, hi), (ln, "unordered compressed endpoints")
            upto = hi
            identities += 1
        assert lep(gap[1], upto)
        rows += 1
    for name in "ABCDEFGJ":
        r, (lo, hi) = source[name]
        end = poly("4k" if r == 0 else "4k-1")
        expected = []
        if lo != poly("0"):
            assert lep(poly("1"), lo)
            expected.append((poly("0"), inc(lo, -1)))
        if hi != end:
            assert lep(inc(hi, 1), end)
            expected.append((inc(hi, 1), end))
        assert gaps[r] == expected, (r, "compressed mask omission")
    assert rows == 13 and identities == 22
    return {"gap_rows": rows, "pair_identities": identities,
            "domain": "k>=6, independent 2<=a<=5, 2<=b<=3, 2<=d<=5; exact linear inequalities",
            "scope": "literal sum identities and gap joins; candidate interfaces checked in written proof"}


def main():
    cpu, wall = time.process_time(), time.perf_counter()
    texts = {p.name: p.read_text(encoding="utf-8") for p in INPUTS}
    report = {
        "fixed": audit_fixed(texts["f4-fixed-tables.md"]),
        "uniform_coverage": audit_coverage(texts["f4-zero-coverage.md"], texts["f4-coverage-tables.md"]),
        "uniform_exclusion": audit_uniform_exclusion(texts["f4-zero-coverage.md"], texts["f4-zero-exclusion.md"]),
        "compressed_anchor": audit_compression(texts["anchor-compression.md"]),
        "old_code_imported_or_executed": False,
        "new_greedy_scan": False,
        "independent_verification": False,
        "formal_verification": False,
        "python": platform.python_version(),
        "hashes": {str(p.relative_to(WORK)): hashlib.sha256(p.read_bytes()).hexdigest() for p in INPUTS},
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cpu_seconds": time.process_time() - cpu,
        "wall_seconds": time.perf_counter() - wall,
    }
    (HERE / "printed-results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
