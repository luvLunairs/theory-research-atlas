> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A direct proof on the upper boundary g=(2k+1)f-1

18 October 2026. Proposed analytic proof, local draft for full-text human
review and manual submission. This replaces the logical need for the
parameter certificate in the preserved [boundary proposal (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).
It does not change that snapshot, assert novelty, or supply independent
verification. Intervals include their integer endpoints.

## Target and statement

Let `f>=4`, `k>=2`, `g=(2k+1)f-1`, and `m=3g=(6k+3)f-3`.
Only sums of two distinct actual earlier entries are forbidden. We
prove the complete membership description below, hence eventual
characteristic period `m`. Least periods and exact preperiods are
unnecessary for this theorem and are not claimed here.

Define

    F_i=[(2k+1+2i)f-1,(2k+2+2i)f-2],       0<=i<=k,
    D=[(4k+4)f-4,(4k+4)f-3],
    E_i={(4k+4+2i)f-3},                    1<=i<k,
    P={f} union all F_i union D union all E_i.

The periodic set is

    R=union_{i=0}^{3k} ((2i+1)f+H_i),

where empty index ranges contribute nothing and

| i | H_i |
| --- | --- |
| 0<=i<=k-2 | {0} |
| k-1 | [0,1] |
| k | [-1,f-3] |
| k+1<=i<=2k-1 | [-1,f-2] |
| 2k | [0,f-3] |
| 2k+1 | [f-4,f-3] |
| 2k+2<=i<=3k | {f-3} |

All these actual integers are positive, disjoint and smaller than
`m`. Our claim is

    S(f,g)=P union union_{n>=1}(nm+R).                    (1)

The table is the same as the preserved proposal, expressed in odd
`f`-cells; the argument also extends its stated domain to `f=4`.
Its negative coordinate `-1` is intentional and will be
handled explicitly in the sum analysis. The source period prediction
is credited to van Berkel and Bosma, [Definition 3(4) and Conjecture 5](https://arxiv.org/html/2609.18522v1).
The new argument uses reflection and complete gap witnesses, with no
finite-prefix continuation theorem or parameter partition.

## A symmetric auxiliary set with exactly two collisions

Put

    u=(2k+2)f-2,       v=(4k+1)f-1,       w=(4k+2)f-2=2g.

These are the only members of `P` not in `R`. Enlarge `R` by the
single point `w` to form `R'=R union {w}`. Its cell table is the
table above with `H_(2k)=[0,f-2]`. Consequently

    H_(3k-i)=f-3-H_i,            m-R'=R'.                 (2)

We prove the following exact statement about ordinary residue sums:
the only pairs from `R'` whose sum modulo `m` lies in `R'` are

    g+g=w,                 w+w=m+g.                      (3)

Write the summands as `(2i+1)f+r` and `(2j+1)f+s`. Before
carrying, their sum is `2(i+j+1)f+(r+s)`, where
`-2<=r+s<=2f-4`. First suppose the actual sum is smaller than `m`.

If `r+s<0`, it lies in the preceding odd cell, with index
`t=i+j` and coordinate `f+r+s`. For `r+s=-1`, this coordinate
is `f-1`, above every selected coordinate. For `r+s=-2`, both
input coordinates are `-1`, so `i,j>=k` and `t>=2k`. At
`t=2k`, both indices must be `k`; the target coordinate is
`f-2`, which is precisely `w`, and both inputs are `g`. At
larger `t` all selected coordinates are at most `f-3`, so there
is no hit.

If `0<=r+s<f`, the sum is in an even cell. The only selected
points in such a cell are the coordinate `-1` points of a
following odd cell. Thus a hit would require `r+s=f-1` and
`k<=t=i+j+1<=2k-1`. Then `i+j<=2k-2`. If one input index
is at most `k-2`, its coordinate is zero and the other is at
most `f-2`, too small. Otherwise both indices must be `k-1`,
and their coordinate sum is at most `2<f-1`. This excludes
all hits in this case, including the noncanonical `-1` entries.

If `r+s>=f`, the carried odd cell has index `t=i+j+1` and
coordinate `r+s-f`. An input index at most `k-2` cannot carry;
an input index `k-1` has coordinate at most one and still
cannot carry, since every other coordinate is at most `f-2`.
Hence both indices are at least `k` and `t>=2k+1`. At
`t=2k+1` both inputs are `k`, so the carried coordinate is
at most `f-6`, below `H_(2k+1)=[f-4,f-3]`. At larger
indices the target, if it exists, is the singleton `f-3`, but
the carried coordinate is at most `f-4`. This excludes the
remaining unwrapped sums.

For a wrapped hit `x+y=m+z`, with `z in R'`, reflection (2)
gives the unwrapped hit `(m-x)+(m-y)=m-z in R'`. Its only
possibility just proved is `m-x=m-y=g`, `m-z=w`. Since
`m=3g`, this means `x=y=w` and `z=g`. The residue-zero
case `x+y=m` does not meet `R'`. This proves (3).

## The other extras do not hit the symmetric set

We next show `(u+R') mod m` misses `R'`. For
`x=(2i+1)f+r`, the raw sum is

    2(k+i+1)f+(f-2+r).

The coordinate lies between `f-3` and `2f-4`. If it does not
carry, a selected target is possible only as the next cell's
coordinate `-1`, requiring `r=1` and
`k<=k+i+1<=2k-1`. This forces `i<=k-2`, where `r=0`, a
contradiction. If it carries and is unwrapped, its odd-cell
index is `k+i+1` and its coordinate is `r-2`. Carrying forces
`i>=k`. At `i=k` the coordinate is at most `f-5`, below
the `D` lower coordinate `f-4`. For `k+1<=i<=2k-1`
it is at most `f-4`, below the selected singleton `f-3`.

For `i=2k`, the sum is already above `m`, and its reduced
value is `r+1 in [1,f-1]`, below the first member `f` of
`R'`. For `i>=2k+1`, reduction gives
`2(i-2k)f+(r+1)`. This is in an even cell with coordinate
at most `f-2`; it cannot hit either an odd nonnegative
coordinate or a following `-1` point, which would require
coordinate `f-1`. These cases prove the claimed exclusion.

Because `u+v=m` and `R'` is symmetric, reflecting a supposed
hit of `v+R'` would give a hit of `u+R'`. Thus
`(v+R') mod m` misses `R'` too.

Now consider the infinite candidate in (1). Its nonexceptional
residues lie in `R`. By (3), no sum from `R+R` hits `R`:
the unwrapped collision targets the removed `w`, and the
wrapped collision requires two inputs equal to that removed
residue. The mixed sums with `w` also cannot hit `R` by
(3), and those with `u,v` are excluded by the preceding
argument. The three distinct exceptional pairs are

    u+v=m,        u+w=m+f-1,        v+w=m+2kf.

Their residues are gaps of `R`. Doubles of actual exceptions
are not permitted: each occurs only once in the candidate.

It remains to exclude exceptional targets themselves, which a
modular argument about `R` would not suffice to do. The value
`u=f+g-1` is below the least possible distinct sum. Below
`v`, all selected terms other than `f` belong to
`F_0,...,F_(k-1)`. Seed-plus-anchor sums end at most at
`v-1`, and two anchor entries sum to at least `2g>v`.
For `w=2g`, seed-plus-earlier-anchor sums still end below
`v`, whereas `f+F_k` starts at `w+1`. Distinct anchor
pair sums start at `2g+1=w+1`; the putative `g+g` is
inadmissible. Thus `u,v,w` are safe. The candidate has no
member equal to a sum of two distinct members.

## Every omitted integer has a distinct representation

For positive blocks write

    B_0=[(2k+1)f-1,(2k+2)f-3],
    B_i=F_i                              (1<=i<=k-1),
    B_k=[(4k+1)f,(4k+2)f-3],
    A_*=[(2k-1)f,(2k-1)f+1],
    X[n]=nm+X.

In block zero, the gaps between the full `F_i` are exactly
`f+F_i`. The gap after `F_k` and before `D` is exactly

    F_0 dotplus F_0=[(4k+2)f-1,(4k+4)f-5].

Here dotplus requires distinct actual entries. For `0<=j<k`,
the disjoint pair `F_0+F_(j+1)` gives

    [(4k+4+2j)f-2,(4k+6+2j)f-4],

covering the gap after `D` and each subsequent high singleton,
with the last interval extending through the block end. These
are all omissions above `g` in the initial block.

The following identities cover every gap of a positive `R`
block. Ranges are offsets relative to `nm`; only their portion
in that block is needed.

| Gap | Distinct representations and offset range |
| --- | --- |
| `[0,f-1]` | `F_1+B_(k-1)[n-1]=nm+[-f+1,f-1]` |
| Between early singleton runs | `F_k+B_i[n-1]=nm+[(2i-1)f+1,(2i+1)f-1]`, `1<=i<=k-1` |
| After `A_*` | `F_k+B_k[n-1]=nm+[(2k-1)f+2,(2k+1)f-2]` |
| Ordinary parts of gaps between `B` runs | `F_i+{nm+f}=nm+[(2k+2+2i)f-1,(2k+3+2i)f-2]`, `0<=i<k` |
| Extra lower point `u[n]` in the first such gap | `v+D[n-1]=nm+[(2k+2)f-2,(2k+2)f-1]` |
| Extra upper point `v[n]` before `B_k[n]` | `F_0+A_*[n]=nm+[4kf-1,(4k+1)f-1]` |
| After `B_k` through the point before `D` | `F_0+B_0[n]=nm+[(4k+2)f-2,(4k+4)f-5]` |
| After `D` and all but the last high singleton | `F_0+B_i[n]=nm+[(4k+2+2i)f-2,(4k+4+2i)f-4]`, `1<=i<k` |
| Final gap after `E_(k-1)` | `v+B_0[n]=nm+[(6k+2)f-2,m-1]` |

For `n>=2` every row involving block `n-1` uses different
actual blocks and is automatically distinct. At `n=1`, use
the full initial `F_i` wherever `B_i[0]` is required. The
early-singleton rows use `F_k` and `F_i` with `i<k`, so
remain disjoint. The after-`A_*` row becomes the restricted
self-sum of `F_k`; its range is exactly the displayed range,
because removing both extreme entries in `B_k` has the same
effect on the endpoint sums as strict self-pairing.

The low-gap row is disjoint unless `k=2,n=1`. In that case
the restricted `F_1` self-sum gives `[-f+2,f-2]`; its lost
lower endpoint is negative, and its lost upper endpoint
`f-1` is supplied by the distinct initial pair
`u+w=m+f-1`. This checks the only exceptional overlap.
All pairs using `v` and `D` are disjoint even initially.
The remaining rows pair an initial term with a positive-block
term and hence are distinct.

The low interval, consecutive early gaps, after-`A_*` gap,
inter-`B` gaps and high gaps exhaust the complement of the
displayed residue table. Every summand is positive, so it is
smaller than the omitted integer it represents. Since the
candidate contains exactly the forced seeds at or below `g`,
sum exclusion and complete coverage identify (1) with the
greedy construction by induction on integers. This proves the
infinite-parameter theorem. No program certificate or observed
repetition is a premise. QED.

## Checks, limits and credit

This proof reuses the preserved candidate formula, the odd-cell
reflection idea from the [odd-multiple proof](../../greedy-unified-20261018/odd-multiple-proof.md),
and interval-sum identities. The new auxiliary point `w`, the
complete two-collision classification and the `k=2` low-gap
repair supply the direct argument on this boundary. It does not
relabel the source period prediction as new research.

The enlarged domain `f>=4` is justified throughout the argument,
not inferred from a table match. At `f=3`, the `D` lower coordinate
`f-4` becomes negative and the bound `2<f-1` in the even-cell
case fails. There is an actual obstruction to extending this membership
formula: at `f=3,k=2`, it would select `52=42+10`, `94=84+10`
and `146=126+20`, although `52+94=146` uses distinct entries.
This refutes that extrapolated formula, not eventual periodicity for
the seed pair `(3,14)`.

The arithmetic was rechecked by summand category, including the
negative coordinate `-1`, the equality `m=3g`, and the smallest
domain `f=4,k=2`. The linked [diagnostic code (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) and
[actual report (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) retain four boundary cases and eight
ray cases, plus the explicit outside-domain obstruction. These are
secondary transcription checks, not proof of the quantifiers.
Earlier sealed artifacts remain intact.

Actual service-supplied identity, version and configuration are
unknown. This is substantive same-team Codex assistance. The
batch's assistance and exact-version report must cover this
proof. Human full-text screening, independent mathematical
assessment and novelty review remain pending. Original prose
and data use CC BY 4.0 under the repository terms.
