> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A direct proof for two infinite first-seed-two families

18 October 2026. Local scientific draft requiring full-text human review and
manual submission. This is a same-team AI contribution, not independent
verification or a priority claim. Actual service model identity, version and
configuration are unknown.

## Target and provenance

The strict greedy sequence `S(2,g)` starts with `2,g`, and admits a larger
integer if and only if it is not a sum of two distinct earlier members.
This note replaces the certificate dependency for every `g=4k+1` and
`g=4k+2`, `k>=1`, by an explicit all-integer sum argument.

The membership formulas were already retained in
[the first-seed-two draft (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).
The source conjecture and predicted periods are due to Daan van Berkel and
Wieb Bosma, [*Periodicity conjectures for all 2-sumfree sequences*,
Definition 3 and Conjectures 1 and 5](https://arxiv.org/html/2609.18522v1).
Those passages were inspected in the earlier work; the parent owns the
updated source check for this revision. No claim that the two families or
their predictions are new is made. The new contribution here is a unified
direct proof that does not use a parameter checker or finite continuation.

Write `[a,b]_4={a,a+4,...,b}`, with congruent endpoints. An interval is empty
when its lower endpoint exceeds its upper endpoint. Only nonempty input
intervals are used in the sum identities below. Ordinary sums of two such
APs add endpoints. The restricted self-sum of `[a,b]_4`, for `a<b`, is
`[2a+4,2b-4]_4`; a singleton has empty restricted self-sum.

## Unified statement

Let `w>=5` be odd and put

    e = 4 floor(w/4)+2,       g=min(w,e),       m=3w,
    E = [2,2w-4]_4,           O = [w,3w-2]_4,
    X = [e,2w]_4,             u=2w,            R=E union O.

Thus `e=w+1` when `w=1 mod 4`, and `e=w-1` when `w=3 mod 4`.
In particular `6<=e<=2w-4`; the latter equality is possible at `w=5`.
Define

    P_0 = {2} union X union O,
    T = P_0 union union_(n>=1)(nm+R).

**Proposition.** `T=S(2,g)`. Consequently `S(2,g)` is characteristic
`3w`-periodic from `3w` onward. For `w=4k+1` this proves the formula for
`g=4k+1`; for `w=4k+3` it proves the formula for `g=4k+2`.

All displayed sets lie in the specified `m`-blocks. They are positive and
`P_0` contains exactly `2,g` at or below `g`. It therefore suffices to show
that no member of `T` is the sum of two distinct members, and every omitted
integer greater than `g` has such a representation. Positivity then makes
every representing summand smaller than its target, so ordinary induction
on the scanned integer identifies the greedy sequence.

## Exclusion

First, `R+R` is disjoint from `R` modulo `m`, even when equal residues are
allowed. The following table gives all three sum types. A carried part means
subtracting `m`; all sums are smaller than `2m`.

| Type | Raw AP | Reason it misses `R` before and after a carry |
| --- | --- | --- |
| `E+E` | `[4,4w-8]_4` | Before a carry it is `0 mod 4`. After a carry it is `w mod 4` with value at most `w-8`, below `O`. |
| `E+O` | `[w+2,5w-6]_4` | Before a carry it is `w+2 mod 4`, the other odd class. After a carry it is `0 mod 4`. |
| `O+O` | `[2w,6w-4]_4` | Before a carry it is `2 mod 4` but starts above `max E=2w-4`. After a carry it is `w+2 mod 4`. |

The two odd residue classes `w` and `w+2 mod 4` are distinct. There are
no even `0 mod 4` entries in `R`. This proves every asserted exclusion,
including the possibility that a raw interval has no carried part.

Every actual selected integer outside the periodic residue set has to be
the one initial integer `u=2w`: indeed `X\{u}` is a subset of `E`.
Its mixed sums are also safe:

| Type | Raw AP | Reason it misses `R` modulo `m` |
| --- | --- | --- |
| `u+E` | `[2w+2,4w-4]_4` | Uncarried values are `0 mod 4`; carried values are `w mod 4` and at most `w-4`. |
| `u+O` | `[3w,5w-2]_4` | Every value carries, leaving `[0,2w-2]_4`, which is `0 mod 4`. |

The pair `u,u` is not available because `u` occurs only once as an actual
member of the proposed set. Its positive block translates are absent.
It remains to exclude a representation of the initial target `u` itself.
Earlier selected evens are all `2 mod 4`, and earlier selected odds all
`w mod 4`. An even-even sum is `0 mod 4` and an even-odd sum is odd, so
only two odds could represent `u=2w`. The two least distinct odds are
`w,w+4`, whose sum is already `2w+4>u`. Thus `u` is safe too.

These arguments exclude every distinct selected pair hitting `T`. They
do not confuse equal residues in different blocks with equal integers.

## Coverage in the initial block

Consider `g<n<m`. The odd residue class `w mod 4` is entirely selected
in `O`; the even class `2 mod 4` is selected in `X` until its endpoint
`2w`. Its remaining omitted part is covered by the restricted self-sum
of `O`. The other two residue classes are covered as follows:

| Omitted class | Available distinct sums |
| --- | --- |
| `n=0 mod 4` | `2+X=[e+2,2w+2]_4`, and `X dotplus X=[2e+4,4w-4]_4` |
| `n=w+2 mod 4` | `2+O=[w+2,3w]_4` |
| `n=2 mod 4`, `n>2w` | `O dotplus O=[2w+4,6w-8]_4` |

The first omitted multiple of four above `g` is `e+2`. The two intervals
in that row have no missing step because `e<=w+1` implies
`2e+4<=2w+6`. Their final endpoint `4w-4` is at least `m-1` for `w>=5`.
The other odd class starts above `g` at `w+2`; its displayed sum extends
through the end of the block. In the last row `6w-8>=m-1`, again for
`w>=5`. There is no missing `2 mod 4` entry between `g` and `e`, since
`g` is either `e` or `e-1`. All pairs involving the seed `2` use a
different integer because `min X>=6` and `min O>=5`.

## Coverage in every positive block

For any set `Y` of offsets, write `Y[n]=nm+Y`; use `E[n],O[n]` only for
`n>=1`, while the actual initial copies are `X` and `O`. The following
identities cover the complement of `R` in every positive block. Sums
may extend outside the target block; only their intersection with that
block is needed.

**Even class `0 mod 4`.** For every `n>=1`,

    u+O[n-1] = nm+[0,2w-2]_4,
    X+E[n]   = nm+[e+2,4w-4]_4,                         (1)

where `O[0]` denotes the actual initial `O`. The two intervals meet or
are adjacent because `e<=2w-4`, hence `e+2<=2w+2`. The upper endpoint
`4w-4` reaches beyond every required multiple of four below `m`.
For n=1 the first sum has an even and an odd summand; for n>=2
its summands lie in different blocks. The second uses one
initial integer and one integer from block `n`, so both sums are strict.

**Even class `2 mod 4`.** Its omitted part starts at `2w`. For every
`n>=1`,

    O+O[n] = nm+[2w,6w-4]_4.                            (2)

The summands come from different actual blocks. This covers its whole
required part below `m`; all smaller positive offsets in this class are
exactly `E`.

**Odd class `w mod 4`.** Its omitted offsets are those below `w`. For
`n>=2`, use

    u+E[n-1] = nm+[2-w,w-4]_4.                          (3)

For the first positive block use the actual initial interval instead:

    u+(X\{u}) = m+[e-w,w-4]_4.                         (4)

Here `X\{u}=[e,2w-4]_4` is nonempty. If `w=1 mod 4`, its carried
lower endpoint is `1`, the first required positive residue in this class.
If `w=3 mod 4`, that endpoint is `-1`, below its first required residue
`3`. Thus (4) covers exactly as much of the low gap as needed. Its two
summands are distinct since the second is smaller than `u`; the factors
in (3) are in different blocks. Offsets from `w` through the end of this
odd class are selected in `O`.

**Other odd class `w+2 mod 4`.** For `n>=2`, use the different-block sum

    O+O[n-1] = nm+[-w,3w-4]_4.                         (5)

Its upper endpoint is the largest offset of this class below `m`, and
its lower endpoint is negative. In block one replace it by a restricted
self-sum and a seed-plus-tail sum:

    O dotplus O = m+[4-w,3w-8]_4,
    2+O[1]      = m+[w+2,3w]_4.                        (6)

The first starts below the first required nonnegative residue, since
`w>=5`. The rows are contiguous because `w+2<=3w-4`, and the second
reaches the end of the block. Distinctness is explicit in the self-sum;
the seed is different from every member of `O[1]`.

These four classes partition every offset in `[0,m)`. Equations (1)--(6)
cover every omitted integer in every positive block. Together with initial
coverage and exclusion, they prove `T=S(2,g)` and the asserted infinite
periodic tail. No computed prefix, parameter sample, or continuation
certificate is a premise. QED.

## Checks and limits

The proof was rechecked symbolically, including `w=5` where
`X\{u}` is a singleton, both congruence classes of `w`, the special
first positive block, and the strict self-sum endpoints. An optional
diagnostic script reuses only the four earlier cases `w=5,7,13,15`;
its results are corroboration, not the proof above. The actual outcome
and exact-version hashes will be retained in the shared small-family
check report.

This note does not yet replace the certificate proofs for `g=0,3 mod 4`,
the exceptional second seeds `7,8,11,12`, the non-midpoint `f=3` families,
or the remaining `f=4` families. Least periods and exact transients are
not claimed here. The existing computer-assisted results for those cases
remain unchanged, while a complete purely analytic replacement remains
unfinished. Original prose/data use CC BY 4.0 under the repository terms.
