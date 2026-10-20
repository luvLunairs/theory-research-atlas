"""Independent exact audit of the restricted fifth-moment model.

The model's pickle and NPZ files are comparison targets, not coefficient
sources. Equality-bit patterns implement orbit canonicalization independently;
integer coefficients and exact rational controls are reconstructed below.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import hashlib
import json
import pickle
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TARGET = HERE.parent / "fivepoint"

import numpy as np


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def partition_patterns(k):
    out = []
    def visit(prefix):
        if len(prefix) == k:
            out.append(tuple(prefix))
            return
        for symbol in range(min(2, max(prefix) + 1) + 1):
            visit(prefix + [symbol])
    visit([0])
    return out


class Canonical:
    def __init__(self):
        self.patterns = {k: partition_patterns(k) for k in (4, 5)}
        self.pairs = {k: list(combinations(range(k), 2)) for k in (4, 5)}
        self.lookup = {}
        self.transforms = {}
        for k in (4, 5):
            patterns = self.patterns[k]
            pairs = self.pairs[k]
            equality = lambda p: sum(1 << i for i, (a, b) in enumerate(pairs)
                                     if p[a] == p[b])
            lookup = np.full(1 << len(pairs), -1, dtype=np.int64)
            for i, pattern in enumerate(patterns):
                lookup[equality(pattern)] = i
            self.lookup[k] = lookup
            self.transforms[k] = np.array([
                [lookup[equality([p[i] for i in perm])] for p in patterns]
                for perm in permutations(range(k))], dtype=np.int64)
        assert len(self.patterns[4]) == 14 and len(self.patterns[5]) == 41

    def ids(self, points):
        k = points.shape[1]
        equality = np.zeros((len(points), 7), dtype=np.int64)
        for i, (a, b) in enumerate(self.pairs[k]):
            equality += (points[:, a, :] == points[:, b, :]) * (1 << i)
        ids = self.lookup[k][equality]
        assert np.min(ids) >= 0
        return ids

    def codes(self, points):
        points = np.asarray(points, dtype=np.int64)
        if points.ndim == 2:
            points = points[None, :, :]
        k = points.shape[1]
        if k == 1:
            return np.zeros(len(points), dtype=np.int64)
        if k <= 3:
            if k == 2:
                points = np.concatenate([points, points[:, :1, :]], axis=1)
            distances = np.sort(np.stack([
                np.count_nonzero(points[:, a] != points[:, b], axis=1)
                for a, b in combinations(range(3), 2)], axis=1), axis=1)
            different = np.count_nonzero((points[:, 0] != points[:, 1]) &
                                        (points[:, 0] != points[:, 2]) &
                                        (points[:, 1] != points[:, 2]), axis=1)
            return (((distances[:, 0] * 8 + distances[:, 1]) * 8 +
                     distances[:, 2]) * 8 + different)
        ids = self.ids(points)
        answer = np.full(len(points), np.iinfo(np.int64).max, dtype=np.int64)
        if k == 4:
            powers = 8 ** np.arange(14, dtype=np.int64)
            for transformation in self.transforms[4]:
                answer = np.minimum(answer, powers[transformation[ids]].sum(axis=1))
            return answer + (1 << 50)
        for transformation in self.transforms[5]:
            answer = np.minimum(answer, np.sort(transformation[ids], axis=1) @
                                (64 ** np.arange(7, dtype=np.int64)))
        assert np.max(answer) < (1 << 42)
        return answer + (1 << 60)

    def orbit_size(self, points):
        """Orbit-stabilizer, counting ambient isometries fixing the set."""
        points = np.asarray(points)
        k = len(points)
        if k == 1:
            return 2187
        if k == 2:
            d = int(np.count_nonzero(points[0] != points[1]))
            return 2187 * factorial(7) // factorial(d) // factorial(7-d) * 2**d // 2
        # Handle k=3 using the same equality-partition construction directly.
        pairs = list(combinations(range(k), 2))
        signatures = lambda array: tuple(sorted(
            sum(1 << i for i, (a, b) in enumerate(pairs) if array[a, c] == array[b, c])
            for c in range(7)))
        signature = signatures(points)
        counts = Counter(signature)
        row_symmetries = sum(signatures(points[list(p)]) == signature
                             for p in permutations(range(k)))
        all_equal = (1 << len(pairs)) - 1
        stabilizer = row_symmetries * 2**counts[all_equal]
        for amount in counts.values():
            stabilizer *= factorial(amount)
        group_size = factorial(7) * 6**7
        assert group_size % stabilizer == 0
        return group_size // stabilizer

