> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A direct lifetime proof for the other two first-seed-two families

18 October 2026. Local same-team AI scientific draft; full-text human review
and manual submission are required. Actual service model identity, version
and configuration are unknown. No independent verification is claimed.

## Statement and relation to the retained formulas

The following unifies `S(2,4k+3)` for `k>=3` and `S(2,4k)` for `k>=4`.
Its formulas come from the retained
[first-seed-two tables (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material),
whose conjectural source and attribution are recorded there and in
[the companion direct proof](f2-two-classes.md). The argument below replaces
the old parameter certificates for these two families. It uses explicit
sum intervals and exceptional lifetimes, not finite-prefix computation.

Let `h>=4`, let `a` be either `7` or `9`, and put

    m=12h+a-12,       g=min(4h,4h+a-8),
    A=[a,4h+a-4]_4,  B=[4h+4,8h]_4,  C=[8h+a-6,m-2]_4,
    R={2} union A union B union C,
    X=[4h,8h]_4,     Y=[4h+a-8,8h+a-12]_4,
    J=[4h+a-12,4h+a]_4,       D=[4h+a-12,4h+a-4]_4.

Here `[u,v]_4` is an inclusive AP of step four. All displayed intervals are
nonempty for `h>=4`. Define the actual block offsets by

    P_0={2} union X union Y union C,
    P_1={2} union J union B union C,
    P_2={2} union [a+4,4h+a-4]_4 union B union C,
    P_n=R for every n>=3,
    T=union_(n>=0)(nm+P_n).

**Proposition.** `T=S(2,g)`. In particular it is `m`-periodic from `3m`.
For `a=7`, set `k=h-1`: then `g=4k+3` and `m=12k+7`.
For `a=9`, set `k=h`: then `g=4k` and `m=12k-3`.

Every offset lies in `[0,m)`, the actual entries are positive, and the only
entries at or below `g` are the forced seeds `2,g`. To prove the proposition
we establish the global exclusion-and-coverage identity for `T`. All sums
then use smaller positive integers, which proves greedy identification by
induction. No continuation lemma is needed.

The four residue classes modulo four are `0`, `2`, `a`, and `a+2`.
The first two are even; the latter two are different odd classes. Notice
that `m=a mod 4` and `C` is in class `a+2`. This notation works for both
values of `a` without changing any argument.

## Ordinary sums of the periodic core

The following complete table proves `(R+R) mod m` misses `R`, even allowing
equal residues. Raw sums are less than `2m`. The singleton `2` is denoted `s`.

| Pair | Raw AP | Exclusion reason |
| --- | --- | --- |
| `s+s` | `{4}` | Class `0`, below `B`. |
| `s+A` | `[a+2,4h+a-2]_4` | Class `a+2`, below `C`. |
| `s+B` | `[4h+6,8h+2]_4` | Class `2`, above the singleton `2`. |
| `s+C` | `[8h+a-4,m]_4` | Class `a`, above `A`; its final value carries to `0`. |
| `A+A` | `[2a,8h+2a-8]_4` | Class `2`, above `2`, and below `m`. |
| `A+B` | `[4h+a+4,12h+a-4]_4` | Uncarried class `a` is above `A`; the carried part has class `0` and value at most `8`. |
| `A+C` | `[8h+2a-6,16h+2a-18]_4` | Uncarried class `0` is above `B`; carried class `a+2` is at most `4h+a-6`, below `C`. |
| `B+B` | `[8h+8,16h]_4` | Uncarried class `0` is above `B`; carried class `a+2` is at most `4h+12-a`, below `C`. |
| `B+C` | `[12h+a-2,20h+a-14]_4` | It carries to `[10,8h-2]_4`, class `2`, missing `2`. |
| `C+C` | `[16h+2a-12,24h+2a-28]_4` | It carries to `[4h+a,m-4]_4`, class `a`, above `A`. |

For example, `A+A` remains below `m` because
`m-(8h+2a-8)=4h-a-4>=3`. Every other containment follows directly from
`h>=4` and `a in {7,9}`. Carried pieces are obtained by subtracting one
`m`; empty carried or uncarried pieces are simply absent.

## The exceptional lifetimes and their collisions

Put

    v=4h,       z=4h+a,       I=[z,8h+a-12]_4.

The selected entries outside `R` modulo `m` are exactly: `v` in block zero;
all of `I` in block zero; and the first residue `z` once more in block one.
Thus `v` has lifetime `{0}`, `z` has lifetime `{0,1}`, and `I\{z}` has
lifetime `{0}`. The only extra in the first positive block is `m+z`.
The residue sets `I`, `A`, `B`, `C`, `{s}` and `{v}` are pairwise
disjoint. The distinguished residue `z=min I` belongs to `I`; its
occurrence in block one is treated separately, not as a disjoint component.

All mixed sums with `R` miss `R` modulo `m`:

| Pair | Raw AP | Relevant bound after any carry |
| --- | --- | --- |
| `I+s` | `[4h+a+2,8h+a-10]_4` | Class `a+2`, below `C` by at least four. |
| `I+A` | `[4h+2a,12h+2a-16]_4` | Uncarried class `2` misses `2`; carried class `a` is at most `a-4`. |
| `I+B` | `[8h+a+4,16h+a-12]_4` | Uncarried class `a` is above `A`; carried class `0` is at most `4h`, below `B`. |
| `I+C` | `[12h+2a-6,20h+2a-26]_4` | Carried class `a+2` is at most `8h+a-14`, below `C`. |
| `v+s` | `{4h+2}` | Class `2`, different from `2`. |
| `v+A` | `[4h+a,8h+a-4]_4` | Uncarried class `a`, above `A`. |
| `v+B` | `[8h+4,12h]_4` | Uncarried class `0` is above `B`; carried class `a+2` is at most `12-a`, below `C`. |
| `v+C` | `[12h+a-6,16h+a-14]_4` | It carries to `[6,4h-2]_4`, class `2`, missing `2`. |
| `v+I` | `[8h+a,m]_4` | Class `a` above `A`, with only the final point carrying to `0`. |

The pair `v,v` is disallowed, since there is only one actual occurrence of
`v`. The exceptional `I` pairs require more care; their carried residue
class is `a`, so these are exactly what delay the low part of `A`.

The distinct block-zero self-sum of `I` has carried offsets

    [a+16-4h,4h+a-16]_4.

Its intersection with `A` is exactly `[a,4h+a-16]_4`, since `h>=4`.
These are precisely the missing `A` entries in block one. The cross sum
of `I` in block zero with the actual integer `m+z` has, after carrying
once more, offsets

    [a+12-4h,a]_4

in block two. Its intersection with `A` is exactly `{a}`, precisely the
missing `A` entry in block two. Uncarried parts of these sums have class
`2`, with values larger than the seed residue. There is no distinct
block-one self-pair, because its extra part is the singleton `m+z`.
Thus no exceptional-exceptional pair hits any selected core entry.

It remains to exclude representations of the exceptional targets themselves.
For the initial `v`, the only possibly smaller nonseed entry is the first
point of `Y` when `a=7`, namely `4h-1`; adding the seed gives `4h+1>v`.
For any initial target in `I`, a representation in its odd class could only
use an initial `X` entry plus an initial `Y` entry, or the seed plus `C`.
The former sum starts at `8h+a-8>max I`, and the latter starts still
later at `8h+a-4`. All other parity classes miss it. Hence `v` and `I`
are safe at their initial occurrences.

For the remaining target `m+z=16h+2a-12`, both summands must lie in blocks
zero and one. With one summand in each block, their offsets must add to
`z`. The only relevant class pairs are `s+C`, `Y+B`, and `X+J`.
Their minimum sums are respectively `8h+a-4`, `8h+a-4`, and
`8h+a-12`, all larger than `z=4h+a` for `h>=4`.
If both summands lie in block zero, the actual target is `2 mod 4`.
The possible classes are `s+X`, `Y+Y`, and `C+C`.
The first two have maxima at most `8h+2` and `16h+2a-24`, respectively,
both below the target. The least *distinct* `C` pair is
`16h+2a-8`, four above it. The equality with two copies of `min C`
is forbidden by strict distinctness. This excludes the last exceptional
target and completes global sum exclusion.

## Initial-block coverage

Above `g` and below `m`, the selected initial progressions are `X`, `Y`,
and `C`, together with the smaller seed. All omitted values are covered
by the following four residue-class rows:

| Class | Required omitted part | Distinct covering sums |
| --- | --- | --- |
| `0` | Above `max X=8h` | `X dotplus X=[8h+4,16h-4]_4` |
| `a` | Above `max Y=8h+a-12` | `X+Y=[8h+a-8,16h+a-12]_4` |
| `a+2` | Before `min C=8h+a-6` | `s+Y=[4h+a-6,8h+a-10]_4` |
| `2` | All values of this class above `g` | `s+X=[4h+2,8h+2]_4`, followed by `Y dotplus Y=[8h+2a-12,16h+2a-28]_4` |

There is no omitted value of class `0` or `a` between `g` and the starts
of `X` and `Y`, since those starts are consecutive. The other odd class
starts above `g` at `4h+a-6`. In the last row the second interval starts
at `8h+2` if `a=7`, or at `8h+6` if `a=9`; in either case the union has
no missing step. Every covering upper endpoint reaches the end of its
required part. Each non-self pair uses disjoint actual progressions.

## Coverage of every positive block

Write `Z[n]=nm+Z` when that offset set is actually present in block `n`.
The sets `{2},B,C,D` are present in every positive block; `B,C` are also
present initially. The additional initial sets are `X,Y`, and the first
positive `A` run is `J[1]`. The following identities suffice for all omitted
offsets. As usual, only the intersection of a displayed sum interval with
the target block is needed.

**Class `0`.** For every `n>=1`,

    Y+B[n-1] = nm+[-4h+8,4h]_4,
    X+B[n]   = nm+[8h+4,16h]_4.                        (1)

The first covers all class-zero offsets below `B`; the second covers all
such offsets above `B`. In the first identity `B[0]` denotes the subset
of the actual initial `X`. At n=1 its summands have different parity;
at n>=2 they lie in different blocks. They are therefore always distinct.
The second uses different blocks.

**Class `2`.** For every `n>=1`,

    X+C[n-1] = nm+[6,8h-2]_4,
    Y+D[n]   = nm+[8h+2a-20,12h+2a-16]_4.             (2)

The second starts at `8h-6` or `8h-2`, and ends at `m+3` or `m+5`.
Thus the union covers every class-two offset except the selected `2`.
At n=1 the first pair has different parity; at n>=2 its summands lie
in different blocks. The second pair lies in different
actual blocks.

**Class `a+2`.** The only selected run in this class is `C`. For the
low omitted portion use

    X dotplus X = m+[16-a-4h,4h+8-a]_4                 (n=1),
    X+B[n-1]    = nm+[16-a-4h,4h+12-a]_4              (n>=2),
    Y+{nm+2}    = nm+[4h+a-6,8h+a-10]_4              (n>=1). (3)

The first two lower endpoints are negative for `h>=4`. In block one,
the gap between the first interval's end and the last interval's start is
`2a-14`, which equals `0` or `4`; there is no missing step. In later
blocks they overlap or touch. The last endpoint is exactly `min C-4`.
The only same-block overlap in these rows is already handled by the strict
self-sum in block one.

**Class `a`, low portion and transient omissions.** The following cover
exactly as far as each block needs before its selected `A` run:

    Y dotplus Y = m+[a-4h,4h+a-16]_4                  (n=1),
    Y+J[1]      = 2m+[a-8-4h,a]_4                    (n=2),
    Y+D[n-1]    = nm+[a-8-4h,a-4]_4                  (n>=3). (4)

All lower endpoints are negative. Their upper endpoints are respectively
four below `min J`, four below the start `a+4` of the block-two run, and
four below `min A`. Every positive-block cross pair is distinct.

**Class `a`, high portion.** For `n>=2`,

    C+C[n-1] = nm+[4h+a,m-4]_4.                       (5)

This covers everything in that class above `A`. In block one the first
such point `z=4h+a` is selected instead. All higher omitted points are
covered by

    C dotplus C = m+[4h+a+4,m-8]_4,
    s+C[1]      = m+[8h+a-4,m]_4.                    (6)

The two intervals have no missing step because `8h+a-4<=m-4` for `h>=4`.
Their union reaches the last required offset `m-4`. The singleton seed is
different from the positive-block `C` summand.

Equations (1)--(6), with the selected runs, exhaust all four residue classes
in every positive block. They establish coverage by distinct members of
`T` at every omitted integer above `g`. The exclusion already proved shows
that `T` is precisely the strict greedy set. The final row is `R` from
block three onward, proving the proposition. QED.

## Checks, corrections and limits

The argument was rechecked at `h=4`, both values of `a`, all three exceptional
blocks, and all strict self-sum endpoints. In deriving the unified notation,
an initial scratch transcription incorrectly enlarged the `a=7` initial
`Y` upper endpoint and `X` endpoint by four. It produced a false potential
collision at `h=4`, namely `31+32=63`; the original table does not select
`31`. The corrected endpoints above are `Y=[4h-1,8h-5]_4` and
`X=[4h,8h]_4` in that case. This was a transcription error in the new
attempt, not a failure of the sealed formula. The retained new diagnostic
will compare these exact formulas and witnesses using only the earlier
cases `h=4,5`, `a=7,9`.

The proof makes no least-period or exact-transient claim. The second seeds
`7,8,11,12` remain outside these two infinite families and need separate
direct arguments to remove their certificate dependence. Original prose/data
follow the repository's CC BY 4.0 terms. Full human scientific review remains
pending, and no approval is assigned.
