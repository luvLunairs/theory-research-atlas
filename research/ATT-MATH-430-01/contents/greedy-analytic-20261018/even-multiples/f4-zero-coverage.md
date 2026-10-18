> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# All-block analytic coverage for S(4,8k), k>=6

18 October 2026. Local scientific draft requiring full-text human review
and manual submission. This is same-team AI-assisted mathematical work,
not independent or formal verification. The statement here is the coverage
half of a global membership proof; the companion contributor handles
exclusion of selected targets. The explicit arithmetic tables, rather than
a program pass, are the premises of the argument.

## Candidate, target and notation

Let `k>=6`, `g=8k` and `m=32k+1`. A progression `r:[a,b]`
means `{8i+r:a<=i<=b}`, with integer row index `i`. Define `P_n`
by the following table of offsets in `[0,m)`, and let

    T=union_(n>=0)(nm+P_n).

| n | r=0 | r=1 | r=2 | r=3 | r=4 | r=5 | r=6 | r=7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `[k,2k]` | `[k,2k-1]` | `[k,2k-1]` | `[k,2k-1]` | `0;4k-1` | `4k-1` | `2k` | `[2k,3k-1]` |
| 1 | `[k,k+1]` | `[k,2k-1]` | `[0,k-1]` | `[0,k-2];4k-1` | `0;4k-1` | `1;[3k-1,4k-2]` | `[3k-2,3k-1];[3k+2,4k-3]` | `[2k+1,3k-1]` |
| 2 | `[2k-2,2k-1]` | `[k,2k-1]` | `[0,k-2]` | `[0,k-2]` | `4k-1` | `[3k-2,4k-3]` | `[3k-2,4k-3]` | `[2k-2,3k-3]` |
| 3 | `[2k-2,2k]` | `[k-2,2k-3]` | `[0,k-2]` | `[0,k-2]` | `[4k-3,4k-1]` | `[3k-2,4k-3]` | `[3k-2,4k-3]` | `[2k-3,3k-4]` |
| 4 | `[2k-2,2k]` | `[k-3,2k-4]` | `[0,k-2]` | `[0,k-4]` | `[4k-4,4k-1]` | `[3k-2,4k-3]` | `[3k-4,4k-5]` | `[2k-3,3k-4]` |
| 5 | `[2k-4,2k]` | `[k-3,2k-4]` | `[0,k-2]` | `[0,k-5]` | `[4k-4,4k-1]` | `[3k-2,4k-3]` | `[3k-5,4k-6]` | `[2k-3,3k-4]` |
| n>=6 | `[2k-5,2k]` | `[k-3,2k-4]` | `[0,k-2]` | `[0,k-5]` | `[4k-4,4k-1]` | `[3k-2,4k-3]` | `[3k-5,4k-6]` | `[2k-3,3k-4]` |

Call the last row `R`. This is the same candidate as the
[retained first-seed-four table (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material),
not an extrapolation from a new parameter scan. Its source prediction and
original attribution to van Berkel and Bosma, [arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1),
remain as recorded in that bundle. All prior files are unchanged.

**Coverage lemma.** Every integer `x>g` outside `T` is a sum of two
distinct positive members of `T`, for every `k>=6`.

Write `P_q(r:I)` for the actual progression `qm+{8i+r:i in I}`.
This is used only when `I` is visibly a selected interval in row `q`
of the table. Its dependence on `k` is understood. In particular an
entry written `P_(n-1)` refers to the actual preceding block, not a
subtraction from a progression name.

## The exact sum formula and distinctness

Take progressions `P_q(r:[a,b])` and `P_p(s:[d,e])`, and choose
`c in {0,1}` with `q+p+c=n`. Put

    t=(r+s-c) mod 8,       h=floor((r+s-c)/8).

Their sum, in target-block coordinates, is exactly

    nm + {8j+t : a+d-4kc+h <= j <= b+e-4kc+h}.          (1)

This is an integer identity obtained by subtracting `c(32k+1)`.
The one-block carry changes the residue by **minus one**; ignoring
that change would give an incorrect proof. Parts of the sum outside
the target block are harmless because only its intersection with the
specified omitted interval is needed.

Formula (1) uses distinct actual summands whenever the two block indices
are different, or their residue classes are different, or their row
intervals are disjoint. Every non-self pair below has one of these
properties. The only same-component pairs are explicitly written
`dotplus`; for them replace `[a+d,b+e]` by
`[2a+1,2b-1]` before applying the carry. These are exactly the sums
of two distinct rows of an interval. Every interval used in a self-pair
has at least two rows at `k=6` and for all larger `k`.

## Exhaustive omitted intervals and their witnesses

The [complete coverage tables](f4-coverage-tables.md) list every
omitted interval above `g` for `n=0,...,6`, followed by a uniform
table for every `n>=7`. Each line gives the target residue and its
whole omitted row interval, then explicitly selected factors, the
carry `c`, and the resulting interval from (1). There are 103 gap
rows and 172 pair contributions. They cover all `k>=6`, rather
than a list of numerical parameter values.

The row-coordinate mask is `[0,4k]` in residue zero and
`[0,4k-1]` in every other residue: the extra last zero-residue row
is the offset `m-1=32k`. This endpoint is included throughout.
In block zero, restrict the mask to rows at least `k+1` in residue
zero and at least `k` in other residues, so that exactly the
candidates above `g=8k` are treated. Subtracting the selected
intervals in the displayed candidate gives exactly the left columns
of the coverage tables. No omitted component is hidden by an
envelope approximation.

For each row, the listed resulting intervals start at or before the
omitted interval, meet or overlap consecutively, and finish at or beyond
its last endpoint. These are explicit affine endpoint inequalities.
They can be checked for all `k>=6` by writing `k=6+t`, `t>=0`:
each relevant endpoint difference is a displayed affine function with
nonnegative constant and nonnegative coefficient. This is a universal
integer inequality argument, not a sample at `k=6`.

For example, the final block-zero residue-six gap is covered by
`[2k+1,4k-3]` and `[3k,4k]`. They meet or overlap because
`3k<=4k-2`, and the second reaches the required `4k-1`.
The first interval is the strict self-sum of the initial residue-three
progression, so its two prohibited endpoint doubles have not been
silently restored. In block one the residue-five gap beginning at row
two uses the strict self-sum of the initial residue-seven progression,
whose carried rows are `[2,2k-2]`; the cross-block interval
`[k,3k-2]` covers the remainder, including the missing upper diagonal.

The last transient block contains a useful boundary identity. In block
six, the residue-three gap `[k-4,4k-1]` is covered by

    P_2(5:[3k-2,4k-3]) + P_3(7:[2k-3,3k-4])
        -> [k-4,3k-6]       with one carry,
    P_0(3:[k,2k-1]) + P_6(0:[2k-5,2k])
        -> [3k-5,4k-1]     with no carry.

These two intervals are adjacent, and all factors lie in different
blocks. This explicitly handles the last change of the lower
residue-zero endpoint; it is not inferred from earlier block behavior.

## Why the coverage persists forever

The table for `n>=7` uses only a fixed block-zero anchor and a
progression from `P_n=R` or `P_(n-1)=R`. Thus all its factor
lifetimes are already guaranteed by the **definition** of `T` for
every such `n`. The sum identities depend on the block index only
through the additive shift `nm`. For instance the entire low
residue-zero gap has the single identity

    P_0(3:[k,2k-1]) + P_(n-1)(6:[3k-5,4k-6])
      = nm + 0:[-4,2k-6],

whose relevant part contains `0:[0,2k-6]`. The high residue-zero
gap uses the two intervals `[2k+1,3k-1]` and `[3k-2,5k-4]`,
and `5k-4>=4k` for `k>=6`. All seven other residue classes
have the explicit analogous rows in the table. This is the repeated
anchor mechanism that supplies every later omission.

All selected factors in these tables are positive integers. Hence a
factor representing `x` is smaller than `x`. The coverage lemma is
therefore established for every integer `x>g` outside the candidate.
Together with a separate complete exclusion proof and the obvious
forced-seed initialization, the global greedy identification criterion
gives `T=S(4,8k)`, with the displayed periodic row from block six.
This note supplies the coverage obligation; it does not claim exclusion
on the basis of its own tables. QED.

## Checks, assistance and limits

The helper [f4_coverage_derive.py (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) searched among
symbolic AP sum identities from the retained candidate. It kept only
coverage chains whose endpoint inequalities hold for all `k=6+t`,
`t>=0`, then printed every chosen factor and interval. The written
identities above and in the table are sufficient for the proof without
executing that helper. No new greedy scan, enlarged enumeration,
finite-prefix continuation or parameter-checker pass is a premise.
The [retained output (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) records the literal
witness objects, final hashes and actual process time.

This worker read every written coverage row and rechecked the carry
formula, source progression lifetimes, strict self-sums, target masks
and endpoint joins, including `k=6`. The complementary exclusion
analysis and selected-transient protection are assigned to another
same-team contributor, and must be combined before asserting membership.
No independent review, human screening, formal verification or novelty
claim follows from these contributor checks. Actual service model
identity, version and configuration are unknown; manual submission
remains required. Original prose/data use CC BY 4.0 and code uses MIT
under the repository terms.
