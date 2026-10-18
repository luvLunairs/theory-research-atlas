"""Read-only exact checks of the printed fixed f=3 lifetime proof tables.

Same-team AI audit, not independent/formal verification. No greedy prefix is
computed. Intervals with infinity are handled as entire rays. MIT.
"""
from pathlib import Path
import hashlib
import json
import math
import re
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OLD = ROOT / "work/greedy-analytic-20261018"
LIFE = OLD / "even-multiples/boundary-lifetime-tables.md"
ARITH = OLD / "even-multiples/boundary-arithmetic-tables.md"
FINITE = OLD / "finite-small.md"
INF = math.inf


def union(parts):
    out = []
    for a, b in sorted(parts):
        if a > b:
            continue
        if out and a <= out[-1][1] + 1:
            out[-1] = (out[-1][0], max(out[-1][1], b))
        else:
            out.append((a, b))
    return tuple(out)


def parse(text):
    text = text.strip()
    if text == "-":
        return ()
    parts = []
    for token in text.split(" U "):
        if re.fullmatch(r"\d+", token):
            parts.append((int(token), int(token)))
        else:
            hit = re.fullmatch(r"\[(\d+),(\d+|infinity)[\])]", token)
            assert hit, ("bad interval", token)
            parts.append((int(hit[1]), INF if hit[2] == "infinity" else int(hit[2])))
    assert all(a >= 0 and a <= b for a, b in parts)
    normalized = union(parts)
    assert normalized == tuple(parts), ("not disjoint canonical lifetimes", text)
    return normalized


def plus(I, J, carry, strict=False):
    a, b = I
    d, e = J
    return union([(a+d+carry+int(strict), b+e+carry-int(strict))])


def pairlife(r, s, L, m, forbid_diagonal=True):
    out = []
    for i, I in enumerate(L[r]):
        for j, J in enumerate(L[s]):
            if r == s and j < i:
                continue
            out.extend(plus(I, J, (r+s)//m, forbid_diagonal and r == s and i == j))
    return union(out)


def rows(section):
    for line in section.splitlines():
        if line.startswith("| "):
            cells = [x.strip() for x in line.strip("|").split("|")]
            if cells[0].startswith("---"):
                continue
            yield cells


def sections(text):
    result = {}
    chunks = re.split(r"^## f=3, g=(\d+), m=(\d+)\s*$", text, flags=re.M)
    for i in range(1, len(chunks), 3):
        result[int(chunks[i])] = (int(chunks[i+1]), chunks[i+2])
    return result


def covers(intervals, I):
    return any(a <= I[0] and I[1] <= b for a, b in intervals)


def factor(text):
    dagger = text.endswith(" dagger")
    if dagger:
        text = text[:-7]
    match = re.fullmatch(r"\((\d+); (.*)\)", text)
    assert match, text
    value = parse(match[2])
    assert len(value) == 1
    return int(match[1]), value[0], dagger


def fixed_case(g, m, life_text, arith):
    L, stated_Q = {}, {}
    for cells in rows(life_text):
        if not cells[0][0].isdigit():
            continue
        for r in map(int, cells[0].split(",")):
            assert r not in L
            L[r], stated_Q[r] = parse(cells[1]), parse(cells[2])
    assert set(L) == set(range(m))
    H = {r for r in L if L[r]}
    R = {r for r in H if L[r][-1][1] == INF}
    E = H-R
    assert 0 not in H or not covers(L[0], (0, 0))
    assert {r for r in H if r <= g and covers(L[r], (0, 0))} == {3, g}
    actual_Q = {r: [] for r in range(m)}
    pairs = {}
    for r in sorted(H):
        for s in sorted(H):
            if r > s:
                continue
            q = pairlife(r, s, L, m)
            if q:
                pairs[r, s] = q
                actual_Q[(r+s)%m].extend(q)
    actual_Q = {r: union(q) for r, q in actual_Q.items()}
    assert actual_Q == stated_Q, (g, "printed Q differs from full strict sum")
    for r in range(m):
        assert not any(max(a,c) <= min(b,d) for a,b in L[r] for c,d in actual_Q[r])
        b = max(0, (g-r)//m+1)
        clipped = union([(max(a,b), z) for a,z in L[r]+actual_Q[r]])
        assert clipped == ((b,INF),), (g,r,"incomplete global coverage")

    sub = re.split(r"^### (.*)$", arith, flags=re.M)
    headings = {sub[i].strip():sub[i+1] for i in range(1,len(sub),2)}
    matrix = headings["Envelope-plus-core upper containment"]
    core = {int(i):(int(a),int(b)) for i,a,b in re.findall(r"R(\d+)=\[(\d+),(\d+)\]", matrix)}
    gaps = {int(i):(int(a),int(b)) for i,a,b in re.findall(r"G(\d+)=\[(\d+),(\d+)\]", matrix)}
    assert set(core) == set(range(len(core)))
    assert {x for a,b in core.values() for x in range(a,b+1)} == R
    assert {x for a,b in gaps.values() for x in range(a,b+1)} == set(range(m))-R
    seen_H, matrix_cells = set(), 0
    for cells in rows(matrix):
        match = re.fullmatch(r"\[(\d+),(\d+)\]", cells[0])
        if not match:
            continue
        a,b = map(int,match.groups())
        assert not seen_H.intersection(range(a,b+1))
        seen_H.update(range(a,b+1))
        assert len(cells) == len(core)+1
        for i, cell in enumerate(cells[1:]):
            d,e = core[i]
            names = cell.split("/")
            assert all(re.fullmatch(r"G\d+", name) for name in names)
            allowed = {x for name in names for x in range(gaps[int(name[1:])][0],gaps[int(name[1:])][1]+1)}
            assert {(x%m) for x in range(a+d,b+e+1)} <= allowed, (g,cells[0],i,cell)
            matrix_cells += 1
    assert seen_H == H

    core_hits = headings["All nonempty exceptional pairs hitting the core"]
    match = re.search(r"Exceptional residues E: ([\d,]+)\.",core_hits)
    assert match and set(map(int,match[1].split(","))) == E
    shown_hits = {}
    for cells in rows(core_hits):
        if not cells[0].isdigit():
            continue
        r,s = map(int,re.fullmatch(r"\((\d+),(\d+)\)",cells[1]).groups())
        assert (r,s) not in shown_hits
        assert (r+s)%m == int(cells[0])
        shown_hits[r,s] = parse(cells[2])
    needed_hits = {(r,s):v for (r,s),v in pairs.items() if r in E and s in E and (r+s)%m in R}
    assert shown_hits == needed_hits

    exceptions = headings["Every contributor to an exceptional target"]
    seen_E, exception_pairs = set(), 0
    for cells in rows(exceptions):
        if not cells[0].isdigit():
            continue
        t = int(cells[0]); assert t not in seen_E; seen_E.add(t)
        shown = {}
        for item in cells[1].split("; "):
            match = re.fullmatch(r"\((\d+),(\d+)\): (.*)",item)
            assert match,item
            key = int(match[1]),int(match[2])
            assert key not in shown
            shown[key] = parse(match[3])
        assert shown == {p:q for p,q in pairs.items() if sum(p)%m == t}
        assert parse(cells[2]) == actual_Q[t]
        exception_pairs += len(shown)
    assert seen_E == E

    witnesses = headings["Ray witnesses for residues never selected"]
    seen_never, all_witnesses, repairs = set(), {}, set()
    ray_count = finite_count = 0
    for cells in rows(witnesses):
        if not cells[0][0].isdigit() and not re.fullmatch(r"\(\d+,\d+\)",cells[0]):
            continue
        r,I,d1 = factor(cells[1]); s,J,d2 = factor(cells[2])
        assert not d1
        assert I in L[r] and J in L[s], (g,"unavailable lifetime",cells)
        strict = r == s and I == J
        assert d2 == strict
        if r == s and I != J:
            assert I[1] < J[0] or J[1] < I[0]
        target, carry = (r+s)%m,(r+s)//m
        obtained = plus(I,J,carry,strict)
        if cells[0].isdigit():
            t = int(cells[0]); assert t not in seen_never; seen_never.add(t)
            assert t == target and int(cells[3]) == carry
            assert parse(cells[4]) == obtained and obtained[-1][1] == INF
            all_witnesses[t] = list(obtained); ray_count += 1
        else:
            t,n = map(int,re.fullmatch(r"\((\d+),(\d+)\)",cells[0]).groups())
            assert (t,n) not in repairs; repairs.add((t,n))
            assert t == target and covers(obtained,(n,n))
            assert parse(cells[3]) == obtained
            all_witnesses[t].extend(obtained); finite_count += 1
    assert seen_never == set(range(m))-H
    for t, covered in all_witnesses.items():
        b=max(0,(g-t)//m+1)
        assert covers(union(covered),(b,INF))

    # Deliberately drop distinctness to expose the exact false obstruction.
    false_hits=[]
    for r in sorted(H):
        ordinary = pairlife(r,r,L,m,False)
        t=2*r%m
        for a,b in ordinary:
            for c,d in L[t]:
                if max(a,c)<=min(b,d):
                    false_hits.append({"summand_residue":r,"target_residue":t,"first_false_target_block":max(a,c)})
    return {"g":g,"m":m,"residues":m,"selected_residues":len(H),
            "matrix_cells":matrix_cells,"nonempty_pair_lifetimes":len(pairs),
            "exceptional_pairs_to_core":len(shown_hits),"pairs_to_exceptional_targets":exception_pairs,
            "ray_witnesses":ray_count,"early_repairs":finite_count,
            "failed_refutation_using_forbidden_diagonals":false_hits,"status":"passed"}


def finite_small():
    text = FINITE.read_text(encoding="utf-8")
    definitions = text.split("| g | m | P | R | X=P minus R |")[1].split("Both are positive")[0]
    cases = {}
    for cells in rows(definitions):
        if not cells[0].isdigit():
            continue
        g,m = map(int,cells[:2])
        P,R,X = [set(map(int,cell.strip("{}").split(","))) for cell in cells[2:]]
        assert X == P-R and {x for x in P if x<=g} == {2,g}
        cases[m] = (g,P,R,X)
    assert set(cases) == {31,33}
    triangle = text.split("| r, m=31 | Resulting residues |")[1].split("The mixed sums")[0]
    counts = {m: {"triangular_rows":0,"mixed_rows":0,"initial_witnesses":0,"all_block_witnesses":0} for m in cases}
    for cells in rows(triangle):
        if not cells[0].isdigit():
            continue
        for i,m in enumerate((31,33)):
            r=int(cells[2*i]); shown=list(map(int,cells[2*i+1].split(","))); R=cases[m][2]
            assert shown == sorted((r+s)%m for s in R if s>=r)
            assert not set(shown)&R
            counts[m]["triangular_rows"] += 1
    mixed = text.split("| m | Exceptional integer x |")[1].split("It remains to check")[0]
    for cells in rows(mixed):
        if not cells[0].isdigit():
            continue
        m,x=map(int,cells[:2]); R=cases[m][2]
        assert x in cases[m][3]
        shown=list(map(int,cells[2].split(",")))
        assert shown == sorted((x+r)%m for r in R) and not set(shown)&R
        counts[m]["mixed_rows"] += 1
    initial = text.split("| g=11 | g=12 |")[1].split("For positive blocks")[0]
    seen = {m:set() for m in cases}
    for cells in rows(initial):
        if not cells[0][0].isdigit() and cells[0] != "—":
            continue
        for i,m in enumerate((31,33)):
            if cells[i] == "—":
                continue
            hit=re.fullmatch(r"(\d+)=(\d+)\+(\d+)",cells[i]); assert hit
            t,a,b=map(int,hit.groups()); P=cases[m][1]
            assert a in P and b in P and a!=b and a+b==t
            assert t not in seen[m]; seen[m].add(t)
            counts[m]["initial_witnesses"] += 1
    for m,(g,P,R,X) in cases.items():
        assert seen[m] == set(range(g+1,m))-P
        tail=text.split(f"| r, m={m} | (a,b,c), all n>=2 |")[1]
        tail=tail.split("| r, m=33 |")[0] if m==31 else tail.split("The tables exhaust")[0]
        seen_tail=set()
        for cells in rows(tail):
            if not cells[0].isdigit():
                continue
            r=int(cells[0]); hit=re.fullmatch(r"\((\d+),(\d+),([01])\)",cells[1]); assert hit
            a,b,c=map(int,hit.groups())
            assert a in P and b in R and a+b==c*m+r
            # For every n>=2, n-c>=1, so these are distinct actual blocks.
            assert 2-c>=1
            a1,b1=map(int,re.fullmatch(r"(\d+)\+(\d+)",cells[2]).groups())
            allowed=P|{m+x for x in R}
            assert a1 in allowed and b1 in allowed and a1!=b1 and a1+b1==m+r
            assert r not in seen_tail; seen_tail.add(r)
            counts[m]["all_block_witnesses"] += 1
        assert seen_tail == set(range(m))-R
        assert counts[m]["triangular_rows"] == len(R) and counts[m]["mixed_rows"] == len(X)
    return [{"g":cases[m][0],"m":m,**counts[m],"status":"passed"} for m in sorted(cases)]


def main():
    started=time.process_time()
    ls=sections(LIFE.read_text(encoding="utf-8")); ars=sections(ARITH.read_text(encoding="utf-8"))
    assert set(ls)==set(ars)=={12,18,24}
    cases=[fixed_case(g,m,body,ars[g][1]) for g,(m,body) in sorted(ls.items())]
    finite = finite_small()
    report={"status":"passed","method":"exact interval/ray arithmetic parsed from final printed Markdown, no greedy generation",
            "cases":cases,"finite_first_seed_two":finite,"process_cpu_seconds":time.process_time()-started,
            "input_sha256":{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in (LIFE,ARITH,FINITE)},
            "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "limits":"Same-team audit only; not independent or formal verification; parser/code remain part of the trust boundary."}
    (HERE/"printed-results.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
