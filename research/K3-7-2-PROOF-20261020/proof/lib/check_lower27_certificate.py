#!/usr/bin/env python3
"""Independent exact, standard-library verifier for a fixed-size27 obstruction.

Reconstructs orbit coordinates, covering cuts, fixed-cardinality equalities and
integer quadratic forms of the Gijswijt--Polak q=3 SDP blocks. It imports neither
the numerical builder nor its coefficient cache, and uses no floating arithmetic.
The alpha formula is the q=3 specialization of Gijswijt and Polak's MIT-licensed
CoveringCodesQary.jl, credited in the accompanying audit.

The certificate is a nonnegative integer combination of valid inequalities plus
integer multiples of equalities. A strictly negative box maximum contradicts
the nonnegative combination for every genuine27-word radius2 covering code.
"""
from collections import Counter
from itertools import product
from math import comb, factorial, gcd
from pathlib import Path
import argparse
import hashlib
import json
import time


def require(condition, message):
    if not condition:
        raise ValueError(message)


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def sign(exponent):
    return 1 if exponent % 2 == 0 else -1


def alpha(i, j, t, p, a, k):
    """Exact integer specialization of the cited beta/alpha formulas."""
    beta = sum(
        sign(t-a-u) * choose(u, t-a) * choose(7+a-2*k, 7-k-u)
        * choose(7-k-u, i-a-u) * choose(7-k-u, j-a-u)
        for u in range(8-a)
    )
    factor = sum(sign(a-g) * choose(a, g) * choose(t-a, p-g)
                 for g in range(p+1))
    return beta * 2**(i+j-t) * factor


def distance(x, y):
    return sum(a != b for a, b in zip(x, y))


def orbit(x, y, z):
    return tuple(sorted((distance(x,y), distance(x,z), distance(y,z)))) + (
        sum(len({a,b,c}) == 3 for a,b,c in zip(x,y,z)),
    )


def primitive(row):
    divisor = 0
    for coefficient in row:
        divisor = gcd(divisor, abs(coefficient))
    return [coefficient // max(divisor, 1) for coefficient in row]


def reconstruct():
    ambient = list(product(range(3), repeat=7))
    zero = (0,)*7
    errors = [w for w in ambient if distance(w, zero) <= 2]
    require(len(errors) == 99, "wrong radius2 ball size")
    compositions = []
    for b in range(8):
      for c in range(8-b):
       for d in range(8-b-c):
        for e in range(8-b-c-d):
            a = 7-b-c-d-e
            i, j, h = c+d+e, b+d+e, b+c+e
            key = tuple(sorted((i,j,h))) + (e,)
            x = (0,)*(a+b) + (1,)*(c+d+e)
            y = (0,)*a + (1,)*b + (0,)*c + (1,)*d + (2,)*e
            require(orbit(zero,x,y) == key, "orbit classification mismatch")
            compositions.append(((a,b,c,d,e), i,j,h,key,x,y))
    keys = sorted({c[4] for c in compositions})
    lookup = {key:i for i,key in enumerate(keys)}
    width = len(keys)+1
    pair = [lookup[(0,i,i,0)] for i in range(8)]
    constant = width-1
    def new():
        return [0]*width
    def add(row, index, value=1):
        row[index] += value
    cover = []
    cuts = []
    for counts,i,j,h,key,x,y in compositions:
        local = new()
        for error in errors:
            add(local, lookup[orbit(error,x,y)])
        add(local, pair[h], -1)
        cover.append(local)
        t, p0, px = new(), new(), new()
        for z in ambient:
            if distance(y,z) <= 2:
                add(t, lookup[orbit(zero,x,z)])
                add(p0, pair[distance(zero,z)])
                add(px, pair[distance(x,z)])
        # Expand the four Boolean products times the covering inequality.
        first = t.copy(); add(first,pair[i],-1)
        second = [a-b for a,b in zip(p0,t)]
        add(second,pair[0],-1); add(second,pair[i])
        third = [a-b for a,b in zip(px,t)]
        add(third,pair[0],-1); add(third,pair[i])
        fourth = [a-b-c for a,b,c in zip(t,p0,px)]
        add(fourth,pair[0],101); add(fourth,pair[i],-1); add(fourth,constant,-1)
        fifth, sixth, seventh = new(),new(),new()
        add(fifth,pair[i]); add(fifth,lookup[key],-1)
        add(sixth,pair[h]); add(sixth,lookup[key],-1)
        add(seventh,lookup[key]); add(seventh,pair[i],-1)
        add(seventh,pair[h],-1); add(seventh,pair[0])
        cuts.extend((first,second,third,fourth,fifth,sixth,seventh))
    equalities = []
    for i in range(8):
        row = [0]*(width-1)
        x = (1,)*i + (0,)*(7-i)
        for z in ambient:
            row[lookup[orbit(zero,x,z)]] += 1
        row[pair[i]] -= 27
        equalities.append(row)
    row = [0]*(width-1); row[pair[0]] = 1
    equalities.append(row)
    rhs = [0]*8+[1]
    block_names = [(a,k,kind) for a in range(8) for k in range(a,8)
                   if k <= 7+a-k for kind in ("triple","complement","cover")]

    def quadratic(block_index, vector):
        require(0 <= block_index < len(block_names), "invalid block index")
        a,k,kind = block_names[block_index]
        indices = list(range(k,8+a-k))
        border = int(k == 0 and kind != "triple")
        require(len(vector) == len(indices)+border, "wrong quadratic vector length")
        require(all(type(v) is int for v in vector), "noninteger quadratic vector")
        position = {i:r+border for r,i in enumerate(indices)}
        result = new()
        for ci,(counts,i,j,h,key,x,y) in enumerate(compositions):
            if i not in position or j not in position:
                continue
            _,_,_,p,e = counts
            coefficient = vector[position[i]] * vector[position[j]] * alpha(i,j,p+e,p,a,k)
            if kind == "triple":
                add(result,lookup[key],coefficient)
            elif kind == "complement":
                add(result,pair[h],coefficient); add(result,lookup[key],-coefficient)
            else:
                result = [v+coefficient*u for v,u in zip(result,cover[ci])]
        if border:
            for i in indices:
                coefficient = 2*vector[0]*vector[position[i]]*comb(7,i)*2**i
                if kind == "complement":
                    add(result,pair[0],coefficient); add(result,pair[i],-coefficient)
                else:
                    x = (1,)*i + (0,)*(7-i)
                    for error in errors:
                        add(result,pair[distance(x,error)],coefficient)
                    add(result,pair[0],-coefficient)
            square = vector[0]**2
            add(result,constant,square if kind == "complement" else -square)
            add(result,pair[0],-square if kind == "complement" else 99*square)
        return result
    return keys,cuts,equalities,rhs,quadratic,block_names


def check(path):
    started = time.monotonic()
    certificate_bytes = path.read_bytes()
    certificate = json.loads(certificate_bytes)
    keys,cuts,equalities,rhs,quadratic,block_names = reconstruct()
    require(certificate["size"] == 27, "certificate has wrong cardinality")
    require(certificate["variable_keys"] == [list(k) for k in keys], "wrong orbit coordinates")
    require(certificate["variable_bounds"] == [0,1], "wrong moment box")
    require(certificate["equalities"] == equalities, "fixed-cardinality equalities differ")
    require(certificate["rhs"] == rhs, "equality right sides differ")
    rows = certificate["rows"]
    provenance = certificate["row_provenance"]
    weights = certificate["row_weight_numerators"]
    powers = certificate["row_scale_bits"]
    require(len(rows) == len(provenance) == len(weights) == len(powers), "row length mismatch")
    require(all(type(w) is int and w >= 0 for w in weights), "inequality weights must be nonnegative integers")
    require(all(type(p) is int and p >= 0 for p in powers), "invalid dyadic row scales")
    used = Counter()
    verified_rows = []
    for index,(row,origin,weight) in enumerate(zip(rows,provenance,weights)):
        require(len(row) == len(keys)+1 and all(type(v) is int for v in row), "invalid integer row")
        if not weight:
            continue  # Algebraically unused rows need no validity assumption.
        kind = origin["kind"]
        if kind == "linear":
            ci = origin["index"]
            require(type(ci) is int and 0 <= ci < len(cuts), "invalid linear row reference")
            expected = cuts[ci].copy()
        elif kind == "quadratic":
            expected = quadratic(origin["block"],origin["vector"])
        else:
            raise ValueError("unknown row provenance")
        expected[-1] *= 81  # z=81*y; multiply the entire inequality by81.
        require(row == primitive(expected), f"reconstructed row mismatch at index{index}")
        used[kind] += 1
        verified_rows.append(index)
    equality_weights = certificate["equality_weight_numerators"]
    equality_powers = certificate["equality_scale_bits"]
    require(len(equality_weights) == len(equalities) == len(equality_powers), "equality length mismatch")
    require(all(type(v) is int for v in equality_weights), "noninteger equality weight")
    require(all(type(v) is int and v >= 0 for v in equality_powers), "invalid equality scale")
    common = certificate["combined_common_scale_bits"]
    denominator_bits = certificate["weight_denominator_bits"]
    require(type(common) is int and common >= max(powers+equality_powers), "invalid common scale")
    require(type(denominator_bits) is int and denominator_bits >= 0, "invalid denominator")
    combined = [0]*(len(keys)+1)
    for row,power,weight in zip(rows,powers,weights):
        factor = weight * 2**(common-power)
        combined = [a+factor*b for a,b in zip(combined,row)]
    for row,right,power,weight in zip(equalities,rhs,equality_powers,equality_weights):
        factor = weight * 2**(common-power)
        for i,coefficient in enumerate(row):
            combined[i] += factor*coefficient
        combined[-1] -= factor*right
    require(combined == certificate["combined_integer_coefficients"], "combined coefficients differ")
    upper = combined[-1] + sum(max(0,c) for c in combined[:-1])
    require(upper == certificate["strict_upper_bound_integer"], "box maximum differs")
    require(upper < 0, "certificate does not yield a strict contradiction")
    return {
        "certificate_sha256":hashlib.sha256(certificate_bytes).hexdigest(),
        "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic":"Python exact integers only; no floating-point arithmetic or solver",
        "variables":len(keys),"reconstructed_linear_rows":len(cuts),"reconstructed_block_names":len(block_names),
        "used_inequalities":dict(used),"verified_used_row_indices":verified_rows,
        "exact_fixed_cardinality_equalities":len(equalities),
        "all_inequality_weights_nonnegative":True,
        "strict_upper_bound_numerator":upper,
        "strict_upper_bound_denominator_power_of_two":common+denominator_bits,
        "conclusion":"The certificate excludes a radius2 covering code of exactly27 ternary words of length7.",
        "extension":"A smaller cover could be enlarged to size27, so the same obstruction implies K_3(7,2)>=28.",
        "limits":"PSD validity can be justified by the cited block theorem or by the separate exact ambient-space Gram check ../check_gram_embedding.py. This checker reconstructs the integer block formulas; it is not a formal proof-assistant development or novelty review.",
        "elapsed_seconds":time.monotonic()-started,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate",type=Path)
    parser.add_argument("--json",dest="output",type=Path,required=True)
    args = parser.parse_args()
    report = check(args.certificate)
    args.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
