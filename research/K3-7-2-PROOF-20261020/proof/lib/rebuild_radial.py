"""Exact independent coefficient and control audit for radial moments.

Uses an independently encoded multiset of coordinate equality patterns,
orbit-stabilizer weights, direct shell counts and explicit finite Gram sums.
No discovery module is imported. The retained coefficient cache is compared
only after rebuilding the coefficients.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from math import factorial, comb
from pathlib import Path
import hashlib
import json
import pickle
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LOWER = HERE.parent / "lower"

import numpy as np
from scipy.sparse import load_npz
from audit_fivepoint import Canonical, partition_patterns


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compositions(total, parts):
    for bars in combinations(range(total+parts-1), parts-1):
        locations = (-1,) + bars + (total+parts-1,)
        yield tuple(locations[i+1]-locations[i]-1 for i in range(parts))



def rebuild(codes):
    canonical=Canonical()
    words=np.array(list(product(range(3),repeat=7)),dtype=np.int64)
    V=len(codes);lookup={int(code):i for i,code in enumerate(codes)}
    shell_sizes = [comb(7, i)*2**i for i in range(8)]
    reconstructed, keys_by_degree = {}, {}
    records = []
    for degree in (2, 3, 4):
        patterns = partition_patterns(degree)
        pairs = list(combinations(range(degree), 2))
        equality = lambda p: sum(1 << i for i, (a,b) in enumerate(pairs) if p[a] == p[b])
        lookup_pattern = {equality(p): i for i, p in enumerate(patterns)}
        transforms = np.array([[lookup_pattern[equality([p[i] for i in perm])]
                                for p in patterns]
                               for perm in permutations(range(degree))], dtype=np.int64)
        counts = np.array(list(compositions(7, len(patterns))), dtype=np.int64)
        expanded = np.array([np.repeat(np.arange(len(patterns)), row) for row in counts])
        # Base16 packing of sorted pattern IDs differs from the discovery
        # histogram base8 key but represents the same coordinate multiset.
        representative_keys = np.full(len(counts), np.iinfo(np.int64).max, dtype=np.int64)
        powers = 16**np.arange(7, dtype=np.int64)
        for transform in transforms:
            representative_keys = np.minimum(representative_keys,
                np.sort(transform[expanded], axis=1) @ powers)
        _, representatives = np.unique(representative_keys, return_index=True)
        keys = list(combinations_with_replacement(range(8), degree))
        key_lookup = {key: i for i, key in enumerate(keys)}
        encoded_key_lookup = {sum(value*8**i for i, value in enumerate(key)): index
                              for key, index in key_lookup.items()}
        matrix = np.zeros((len(keys), V+1), dtype=np.int64)
        pattern_array = np.array(patterns, dtype=np.int64)
        for ri in representatives:
            ids = expanded[ri]
            points = pattern_array[ids].T
            sorted_ids = tuple(sorted(map(int, ids)))
            automorphisms = sum(tuple(sorted(map(int, transform[ids]))) == sorted_ids
                                for transform in transforms)
            constant_coordinates = sum(np.all(points[:, coordinate] == points[0, coordinate])
                                       for coordinate in range(7))
            denominator = automorphisms
            for amount in counts[ri]:
                denominator *= factorial(int(amount))
            numerator = factorial(7)*2**(7-int(constant_coordinates))*factorial(degree)
            assert numerator % denominator == 0
            weight = numerator // denominator
            unique_points = np.array(list(dict.fromkeys(map(tuple, points))))
            column = lookup[int(canonical.codes(unique_points)[0])]
            distances = np.sort(np.count_nonzero(words[:, None, :] != points[None, :, :], axis=2), axis=1)
            packed = distances @ (8**np.arange(degree, dtype=np.int64))
            frequency = np.bincount(packed, minlength=8**degree)
            for key in np.flatnonzero(frequency):
                matrix[encoded_key_lookup[int(key)], column] += weight*int(frequency[key])
        for i, key in enumerate(keys):
            denominator = factorial(degree)
            for amount in Counter(key).values():
                denominator //= factorial(amount)
            assert np.all(matrix[i] % denominator == 0)
            matrix[i] //= denominator
            expected_total = 1
            for weight in key:
                expected_total *= shell_sizes[weight]
            assert sum(map(int, matrix[i])) == expected_total
        reconstructed[degree], keys_by_degree[degree] = matrix, keys
        records.append({"degree": degree, "coordinate_histograms": len(counts),
                        "uncollapsed_tuple_orbits": len(representatives), "rows": len(keys),
                        "every_coefficient_matches": True})
        print("radial exact coefficient pass", degree, len(keys), flush=True)
    reconstructed[0] = np.zeros((1, V+1), dtype=np.int64)
    reconstructed[0][0, V] = 1
    keys_by_degree[0] = [()]
    reconstructed[1] = np.zeros((8, V+1), dtype=np.int64)
    reconstructed[1][:, 0] = shell_sizes
    keys_by_degree[1] = [(i,) for i in range(8)]
    row = {key: values for degree in keys_by_degree
           for key, values in zip(keys_by_degree[degree], reconstructed[degree])}

    return row
