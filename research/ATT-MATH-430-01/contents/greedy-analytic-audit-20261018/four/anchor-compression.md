> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# One anchor lemma for the later first-seed-four blocks

18 October 2026. Proposed analytic simplification, local draft for full-text
human review and manual submission. This is substantive same-team AI work,
not independent or formal verification. It replaces the five separate
coverage sections for blocks three onward, not the exclusion proof or the
three initial coverage sections. No executable result is a premise.

The exact sum rule is [Framework Lemma 2](../framework.md#2-block-coordinates-and-distinct-actual-integers).
The global identification step is Framework Theorem 3. The source candidate
and earlier witnesses remain in the immutable
[coverage note](../../greedy-analytic-20261018/even-multiples/f4-zero-coverage.md)
and [complete table](../../greedy-analytic-20261018/even-multiples/f4-coverage-tables.md).
The underlying sequence and period conjecture are due to Daan van Berkel
and Wieb Bosma, as credited there. This note makes no novelty judgment.

## A rectangular parameter domain

Fix integers

    k>=6,       2<=a<=5,       2<=b<=3,       2<=d<=5.       (1)

The three parameters in (1) vary independently. Put `m=32k+1`.
As before, `r:[u,v]` denotes the offset AP `{8j+r:u<=j<=v}`;
all endpoints are inclusive. A component followed by `[q]` is translated
by `qm`. The following five fixed components are in block zero:

    I_0=0:[k,2k],       I_1=1:[k,2k-1],
    I_2=2:[k,2k-1],     I_3=3:[k,2k-1],
    X=6:{2k}.                                                (2)

Suppose the candidate's current block `n>=3` is exactly the union of

    A=0:[2k-a,2k],       B=1:[k-b,2k-b-1],
    C=2:[0,k-2],         D=3:[0,k-d],
    E=4:[4k-b-1,4k-1],   F=5:[3k-2,4k-3],
    G=6:[3k-d,4k-d-1],   J=7:[2k-3,3k-4].                    (3)

In block `n-1`, assume the candidate contains these four components:

    F^-=5:[3k-2,4k-3],
    G^-=6:[3k-a,4k-a-1],
    E^-=4:[4k-d+1,4k-1],
    J^-=7:[2k-b,3k-b-1].                                    (4)

There is no hypothesis that the entire preceding block has the same
shape as (3), and no assumption that an actual greedy sequence has already
stabilized. These are literal containment conditions on the proposed set.

**Anchor lemma.** Under (1)--(4), every integer in block `n` outside
(3) is a sum of two different positive candidate entries, provided the
initial components (2) and preceding components (4) belong to that
candidate.

## Thirteen gap identities

In the table, a factor from (2) is always initial, a factor named
`A[n]`, etc. is current, and a factor with superscript `-` is in block
`n-1`. The result is expressed in row coordinates of the target residue
after subtracting `nm`. A preceding-block factor uses one carry; a
current-block factor uses zero carries. Thus both summands are actual
members of distinct blocks, including at the boundary `n=3`.

| Omitted class and complete row interval | Selected sums and resulting row intervals |
| --- | --- |
| `0:[0,2k-a-1]` | `I_3+G^-[n-1] -> [1-a,2k-a-1]` |
| `0:[2k+1,4k]` | `X+C[n] -> [2k+1,3k-1]`; `I_1+J[n] -> [3k-2,5k-4]` |
| `1:[0,k-b-1]` | `I_3+J^-[n-1] -> [1-k-b,k-b-1]` |
| `1:[2k-b,4k-1]` | `I_0+B[n] -> [2k-b,4k-b-1]`; `I_2+J[n] -> [3k-2,5k-4]` |
| `2:[k-1,4k-1]` | `X+F^-[n-1] -> [k-1,2k-2]`; `I_1+B[n] -> [2k-b,4k-b-2]`; `I_3+J[n] -> [3k-2,5k-4]` |
| `3:[k-d+1,4k-1]` | `I_0+E^-[n-1] -> [k-d+1,2k-1]`; `I_2+B[n] -> [2k-b,4k-b-2]`; `I_3+A[n] -> [3k-a,4k-1]` |
| `4:[0,4k-b-2]` | `I_0+F^-[n-1] -> [-2,2k-3]`; `I_3+B[n] -> [2k-b,4k-b-2]` |
| `5:[0,3k-3]` | `I_1+F^-[n-1] -> [-2,2k-4]`; `I_3+C[n] -> [k,3k-3]` |
| `5:[4k-2,4k-1]` | `I_0+F[n] -> [4k-2,6k-3]` |
| `6:[0,3k-d-1]` | `I_2+F^-[n-1] -> [-2,2k-4]`; `I_3+D[n] -> [k,3k-d-1]` |
| `6:[4k-d,4k-1]` | `I_0+G[n] -> [4k-d,6k-d-1]` |
| `7:[0,2k-4]` | `I_3+F^-[n-1] -> [-2,2k-4]` |
| `7:[3k-3,4k-1]` | `I_0+J[n] -> [3k-3,5k-4]` |

Every identity follows from the single calculation

    t=(r+s-c) mod 8,
    rows=[u+v-4kc+floor((r+s-c)/8),
          U+V-4kc+floor((r+s-c)/8)],                       (5)

for input rows `[u,U]`, `[v,V]` and carry `c`. In particular the
carry changes the AP residue by minus one; it is not just a row shift.
All 22 resulting intervals are displayed, so the table is directly
checkable by integer addition. For example, `I_0+E^-` has residue
`0+4-1=3` and rows

    [k+(4k-d+1)-4k, 2k+(4k-1)-4k]
      =[k-d+1,2k-1].

This covers the beginning of the class-three gap in every later block,
including block six. That block therefore needs no separate two-transient-
block witness in this version.

Here are all possible endpoint-joining conditions, to make the universal
quantifiers explicit. After intervals already meet at their written
endpoints, the remaining comparisons reduce to

    a>=1, b>=2, k>=3, k>=4, k>=b-1,
    k+a>=b+1, 2k>=d.                                     (6)

For instance the class-three second-to-third junction needs
`3k-a<=4k-b-1`, equivalent to `k+a>=b+1`; the class-four junction
needs `2k-b<=2k-2`, equivalent to `b>=2`. The class-five and
class-six low-gap junctions need `k<=2k-3`. The class-zero upper
mask ends at row `4k`, not `4k-1`, and `5k-4>=4k` supplies that
last point. Every inequality in (6) follows from the independent box
(1). All listed input intervals are nonempty and canonical there;
in particular `k-d>=1`, so the proof never silently applies a two-term
self-sum formula to an empty or singleton interval.

Subtracting (3) from the canonical offset masks `[0,4k]` for residue
zero and `[0,4k-1]` for the other residues gives exactly the thirteen
left-hand intervals. There are no other omissions. All witnesses use
block zero and block `n` or `n-1>=2`, hence two different actual integers.
They are positive, so each is smaller than its sum. This proves the
anchor lemma. QED.

## Application to the literal S(4,8k) candidate

For the unchanged candidate `P_0,...,P_5,R`, the current block has
exactly (3) with

| Current block n | a | b | d |
| --- | --- | --- | --- |
| 3 | 2 | 2 | 2 |
| 4 | 2 | 3 | 4 |
| 5 | 4 | 3 | 5 |
| n>=6 | 5 | 3 | 5 |

Every row belongs to the independent domain (1). The interface (4) is
checked directly from the candidate, as follows:

| n | Previous G lower/upper | Previous E lower/upper | Previous J lower/upper |
| --- | --- | --- | --- |
| 3 | `[3k-2,4k-3]` | `{4k-1}` | `[2k-2,3k-3]` |
| 4 | `[3k-2,4k-3]` | `[4k-3,4k-1]` | `[2k-3,3k-4]` |
| 5 | `[3k-4,4k-5]` | `[4k-4,4k-1]` | `[2k-3,3k-4]` |
| n>=6 | `[3k-5,4k-6]` | `[4k-4,4k-1]` | `[2k-3,3k-4]` |

The previous `F` column is `[3k-2,4k-3]` in every case. The
singleton previous `E` at `n=3` is used with an initial component
in a different block, so its ordinary interval sum has no forbidden
diagonal. Conditions (2) are initial selected columns by definition.
Thus the lemma supplies coverage in **every block n>=3**.

Retain only the original coverage table's three early sections, blocks
zero, one and two (lines 7--58 of the audited snapshot). They contain
38 omitted intervals and include all three strict self-pairs. Their
explicit endpoints and distinctness are unchanged. Together with the
13 rows above, there are now 51 gap rows to read instead of 103.
The [separate exclusion proof](../../greedy-analytic-20261018/small/f4-zero-exclusion.md)
still supplies the other half of the global greedy identification.
Consequently the same membership candidate and sufficient tail start
`6m` follow; no least-period or optimal-start claim is added.

## Audit scope and limits

This simplification was obtained by rederiving the written sums and
grouping repeated endpoint relations. It is not inferred from extra
greedy examples. Its proof uses the rectangular inequalities (1),
the literal candidate/interface rows, and the 22 explicit sum identities.
The original table and its derivation code are unchanged and remain
available to inspect the discarded duplication.

The earlier formula cannot simply be extended to `k=5`: then `m=161`
and its recurring row would contain offsets 40 and 80. The different
proposed tail entries `1006=6m+40` and `1167=7m+40` sum to
`2173=13m+80`, also proposed selected. This disproves that unchanged
formula at `k=5`; it does not contradict periodicity of `S(4,40)`,
which has its separate fixed-lifetime proof. The anchor lemma concerns
coverage only and cannot repair an exclusion failure.

The linked [audit record](audit.md) states actual checks and file hashes.
The parent's shared assistance note governs this version: actual model
identity/version/configuration are unknown, and full-text human review
and manual submission remain required. Prose/data use CC BY 4.0 under
the contribution terms.
