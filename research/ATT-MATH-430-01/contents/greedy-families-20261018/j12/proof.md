> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# An explicit description of two infinite families

18 October 2026. Local scientific draft; human review and manual submission
required. This argument is AI-assisted original work within this research
attempt, not a claim of established novelty or independent verification.

## Target and source

For positive integers `f < g`, let `S(f,g)` start with `f,g`. Each subsequent
term is the least larger integer which is not the sum of two distinct earlier
terms. This is the strict greedy definition in Daan van Berkel and Wieb Bosma,
[*Periodicity conjectures for all 2-sumfree sequences*,
arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1), Introduction.
Their Definition 3(2) and Conjecture 5 predict gap period `f+j+1` in the
parameter region considered here, subject to their explicit small-parameter
corrections. Their `f=4,g=9` correction matters below.

The target is an analytic description for `g=2f+j`, for `j=1,2`, valid for
infinitely many `f`, rather than an enlarged computation. The argument does
not require the source's finite-block periodicity theorem. Literature and
priority assessment belong to the batch's source review and remain separate
from the proposed mathematical proof.

## Proposed theorem

Intervals below contain all integers between their endpoints, inclusive.
Let `j` be 1 or 2 and `f >= j+2`. Put

```
m = 5f+2j-1,
A = [f-1, f],
D = [2f+j, 3f+j-1],
B = [2f+j+1, 3f+j-2],
C = [4f+j, 4f+2j],
P = {f} union D union C,
R = A union B union C.
```

Then

```
S(f,2f+j) = P union the union of (k*m + R) over all integers k >= 1.   (1)
```

Except for `(f,j)=(4,1)`, the least eventual characteristic period is `m`
and the least eventual gap period is `f+j+1`. At `(f,j)=(4,1)`, these least
periods are respectively 7 and 2. In all these cases, the characteristic
sequence is periodic from integer `3f+j` onward, and the minimal preperiod
length of the successive-gap sequence is `f+1`.

## Proof of the membership description

Call the right-hand side of (1) `T`. It starts with `f,2f+j`. To identify it
with the greedy sequence, it suffices to show:

1. No member of `T` is the sum of two distinct members of `T`.
2. Every integer `n>2f+j` outside `T` is the sum of two distinct members
   of `T`.

All members are positive. Hence any summands representing `n` are smaller
than `n`, so these two statements establish the greedy recurrence by induction.

The complement of `R` in `[0,m-1]` consists of the four intervals

```
G0 = [0, f-2],
G1 = [f+1, 2f+j],
G2 = [3f+j-1, 4f+j-1],
G3 = [4f+2j+1, m-1].
```

All are nonempty for the stated parameter ranges. All of `A,B,C,D` lie in
`[0,m-1]`, and `B` is the interior of `D`.

### Excluding sums from the candidate set

Every member of `T` has residue in `A union D union C` modulo `m`. The two
endpoints of `D` occur only once each in `T`, as the actual integers in `P`;
they do not occur in `R`. Consequently, a sum of two distinct members whose
residues both lie in `D` cannot have raw residue sum equal to twice either
endpoint. It lies in `[4f+2j+1,6f+2j-3]`. Here a raw residue sum is the sum
of the two representatives in `[0,m-1]`, before reduction modulo `m`.

The following exhaustive table bounds the raw residue sums of every possible
pair. Ordinary sums are used where permitting an equal pair only enlarges a
safe interval.

| Residue classes | Raw residue sum interval | Location modulo `m` |
| --- | --- | --- |
| `A,A` | `[2f-2,2f]` | `G1` |
| `A,D` | `[3f+j-1,4f+j-1]` | `G2` |
| `A,C` | `m+[-j,1]` | `G3 union G0` |
| `D,D`, distinct actual terms | `[4f+2j+1,6f+2j-3]` | `G3 union G0` |
| `D,C` | `m+[f+1,2f+j]` | `G1` |
| `C,C` | `m+[3f+1,3f+2j+1]` | `G2` |

The lower containment in the last row uses `j<=2`; its upper containment
uses `f>=j+2`. The `A,A` row uses `f>=3`, and the wraparound part of `A,C`
uses `f>=j+2`. All other endpoint comparisons follow immediately from the
displayed definitions. Thus no sum of distinct members has residue in `R`.
This excludes every candidate member at least `m`.

It remains to exclude sums equal to members of `P`. Members of `P` are below
`m`, whereas every tail member exceeds `m`. The interval `D` ends at
`3f+j-1`, immediately before the smallest sum `f+(2f+j)=3f+j` of distinct
members. For `C`, the sums `f+D` stop at `4f+j-1`, immediately before `C`,
and distinct sums from `D+D` start at `4f+2j+1`, immediately after `C`.
All sums involving `C` and another member are larger than the top of `C`:
the smallest is `f+(4f+j)=5f+j>4f+2j`, since `f>j`. These observations also
exclude sums equal to `f` or any member of `D`. This proves statement 1.

### Covering every omitted integer

For an integer interval `I=[u,v]` of length at least 2, its sums of distinct
members are exactly `[2u+1,2v-1]`. If a target sum `n` in this range satisfies
`n<=u+v`, use the pair `(u,n-u)`; otherwise use `(n-v,v)`. The bounds ensure
that both entries lie in `I` and are distinct. These representations prove
the elementary interval identity.
In particular, write `D restricted+ D` for such distinct sums; then

```
f+D                  = [3f+j, 4f+j-1],
D restricted+ D      = [4f+2j+1, 6f+2j-3],
D+C                  = m+G1,
D+A                  = G2,
D+B                  = [4f+2j+1, m+f-2].                         (2)
```

Below `m`, every omitted integer greater than `2f+j` belongs to either
`[3f+j,4f+j-1]` or `[4f+2j+1,m-1]`. The first two rows of (2) cover these
using distinct members of `P`.

In the first tail block, the omitted integers in `m+G0` are covered by
`D restricted+ D`, and those in `m+G1` by `D+C`. The omitted integers in
`m+G2` are covered by `D+(m+A)`, and those in `m+G3` by `D+(m+B)`.
These pairs are distinct: the first row imposes distinctness, `D` and `C`
are disjoint, and each of the last two pairs contains one term in `P` and
one term above `m`.

For every integer `k>=2`, the following covers all four gaps of block `k`:

| Omitted integers | Available representing sums |
| --- | --- |
| `k*m+G0` | `D+((k-1)*m+B)` |
| `k*m+G1` | `D+((k-1)*m+C)` |
| `k*m+G2` | `D+(k*m+A)` |
| `k*m+G3` | `D+(k*m+B)` |

In each row, (2) proves interval coverage, and one summand lies in `P`
while the other lies above `m`, ensuring distinctness. This proves
statement 2 and therefore (1).

## Least periods and preperiod

In one circular characteristic block of length `m`, the three nonempty
runs of ones have lengths `2,f-2,j+1`. The three runs of zeros separating
them have lengths `f+j,f+1,2f-3`. All three runs of each type are nonempty.

If this circular binary word were a repetition of a shorter word, the
number of repetitions would divide its three runs of ones. Thus the only
possible nontrivial repetition count is 3, and this would require all
three one-run lengths, and all three zero-run lengths, to be equal. For
`j=2` the first and third one-run lengths differ. For `j=1`, all one-run
lengths coincide only at `f=4`, and there the zero-run lengths are all 5.
That exceptional word is three copies of a word with two adjacent ones
and five zeros, of primitive length 7. Otherwise the word is primitive.

An eventually `m`-periodic sequence has least eventual characteristic
period dividing `m`: translation invariance on the circular word, or the
gcd of any two eventual periods, establishes this. Thus the preceding
run argument establishes the claimed least characteristic periods.

A primitive characteristic period containing `p` ones induces a repeated
block of `p` successive gaps. A shorter eventual gap period containing
`q<p` gaps would have positive total length `t`; shifting by `t` would then
be a characteristic period. Since the least characteristic period divides
`t`, an interval of length `t` contains at least `p` selected integers,
contradicting the `q` gaps in that interval. Consequently the least gap
period is `p`, which is `2+(f-2)+(j+1)=f+j+1` outside the exception and
2 in the exception.

The initial set `P` and the periodic residue pattern `R` differ exactly at
`f-1`, `2f+j`, and `3f+j-1`. Therefore the characteristic sequence agrees
with the periodic extension from `3f+j` onward, and disagrees immediately
before that. In the exceptional primitive-period-7 case, the same
statement follows from the period-7 extension of the same residue set.
There cannot be a different earlier periodic tail: any such tail would
have to agree everywhere with the already fixed infinite periodic tail.
Exactly `f+1` selected integers lie before `3f+j`, namely `f` and `D`.
The minimal successive-gap preperiod is consequently `f+1`, using the
convention of the source's Introduction.

## Checks, limits and attribution

The proof is parameter-symbolic: no finite parameter sweep is used to
justify its universal quantifiers. `check_j12.py` is a small independent
implementation path within this same AI-assisted attempt; it compares
the proposed set with the greedy recurrence at boundary and illustrative
parameters and checks the displayed interval identities. Those checks
are diagnostics, not a substitute for the argument or independent review.

The origin of the target and prediction is van Berkel and Bosma's cited
preprint. The explicit membership formula, residue-table proof and
run-count minimality argument were produced in this AI-assisted attempt.
No named human is represented as having reviewed them. The batch-level
assistance note must include this delegated contribution and its unknown
service model identifier/configuration, as applicable. Full-text human
screening, independent mathematical review and novelty assessment remain
pending. Original prose follows the repository's CC BY 4.0 terms; original
code follows MIT.
