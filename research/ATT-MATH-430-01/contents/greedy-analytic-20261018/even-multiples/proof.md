> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A direct extinction proof for every even multiple with k>=3

18 October 2026. Proposed scientific result for full-text human review and
manual submission. This is same-team AI-assisted research, not independent
verification, formal verification or a novelty claim. All intervals below
contain integers and include their endpoints.

## Claim and relation to the earlier certificate

Let `f>=5` and `k>=3` be integers. Put

    g=2kf,       m=(6k-1)f-1,       K=max(2,k-2).

For the strict greedy sequence `S(f,g)`, only sums of two distinct earlier
selected integers are forbidden. Define the following subsets of `[0,m)`:

    A_0=[f-1,f],
    A_i=(2i+1)f+[-3,-2],                      2<=i<k,
    B_0=2kf+[1,f-2],
    B_1=(2k+2)f+[0,f-2],
    B_i=(2k+2i)f+[0,f-4],                     2<=i<k,
    D={4kf},
    C_j=(4k+2j)f+[-2,-1],                     1<=j<k.

There is no `A_1`. Let `R` be their union. Then

    x in S(f,g) if and only if x mod m in R,      for all x>=2Km.    (1)

Thus the characteristic sequence is eventually periodic with period
`m`, for unbounded `f` and `k`, including `k=3,4`. The bound `2Km`
is sufficient and is not asserted to be the earliest starting point.
This proof does not need a finite-prefix certificate or any executable
checker's pass flag.

The residue set is the same as the final row in the earlier
[even-multiple table (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material)
and its [quotient-boundary extension (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).
Those files proved a more detailed transient table by universal exact
certificates. The present argument establishes reachability of their
tail directly, without reproving their exact transient formulas.
Van Berkel and Bosma's [Definition 3(2), Conjecture 5](https://arxiv.org/html/2609.18522v1)
predicts the period; that prediction is credited and is not a premise.
The conceptual model is the earlier
[lower-offset extinction lemma](../../greedy-proof-audit-20261018/lower-lemma.md),
but the extra types and two special protected points below are different.

Write `X[n]=nm+X`. Define actual initial anchors

    F_i=(2k+2i)f+[0,f-1],                     0<=i<k,

and possible extra residues

    beta_i=(2k+2i+1)f-1,                     0<=i<k,
    gamma_i=(2k+2i+1)f-2,
    delta_i=(2k+2i+1)f-3,                    2<=i<k.

Let `H=R union union_i F_i`. This is the disjoint union of `R`,
the seed residue `{g}`, all `beta_i`, and the `gamma_i,delta_i`
with `i>=2`. Every such residue is in `[0,m)`. Our proof first
confines the actual sequence to `H`, then eliminates every extra.

## 1. Compatibility of the envelope with the tail

We claim the ordinary modular sumset satisfies

    ((H+R) mod m) intersect R is empty.                    (2)

Equal residues are allowed here, so this statement also controls distinct
actual entries in different blocks. We give all type checks rather than
appeal to the earlier certificate.

Use an integer expression `Lf+e`; subtracting `m` changes it to
`(L-6k+1)f+(e+1)`. All elements of `H` are below `m`, so at
most one subtraction is required. Write an `A_i` offset as `a_i`,
so `a_0 in [-1,0]` and `a_i in [-3,-2]` for `i>=2`; write
a `B_i` offset as `b_i`, and a `C_j` offset as `c_j in [-2,-1]`.

### Ten pairs of regular types

* **A+A:** The sum is `2(i+j+1)f+e`, `-6<=e<=0`, below
  `m` and below every `C,D` target. A `B` coordinate is
  nonnegative, but equality zero here can only come from `A_0+A_0`,
  far before `B`. An adjacent odd `A` cell would require
  `e<=-f-2<=-7`, except possibly `A_0`; the latter can only be
  approached when `i=j=0`, whose actual offset is in `[-2,0]`.
  No target is hit.
* **A+B:** This is `(2(k+i+j)+1)f+e`, with `-3<=e<=f-2`,
  below `m` and beyond `A`. Its preceding `B_(i+j)` can only
  be approached with negative `e`. If `e<=-2`, the `A` index
  is at least two, so the target `B` index is at least two and
  its upper offset is `f-4`; the sum has offset at least `f-3`
  there. If `e=-1`, every `B` upper bound is smaller than
  `f-1`. A next-even-cell `C` collision could only have
  `e=f-2`, which requires `A_0` and `B_0` or `B_1`; that
  cell is before every `C` because `k>=3`. Other `C,D`
  collisions are excluded by their offset bounds.
* **A+D:** The sum is `(4k+2i+1)f+a_i`. At `i=0` it is
  already above the final `B` upper endpoint; later indices are
  larger. Its offset cannot reach either neighboring even `C`
  cell when `f>=5`. It is below `m`.
* **A+C:** Write `s=i+j`. Before wrapping this is
  `(4k+2s+1)f+e`, `-5<=e<=-1`. It is beyond `B,D`, and
  an adjacent `C` coordinate would require `e<=-f-1<=-6`
  or `e>=f-2>=3`. After wrapping it is
  `2(s-k+1)f+(e+1)`, with offset in `[-4,0]` and cell index
  at most `k-1`. The next odd `A` run starts at offset at
  least `f-3>=2`; the preceding odd run ends at most `-f-2`,
  except `A_0`, whose upper bound in that position is `-f`.
  None can be reached. The possible exact sum `m` has residue zero.
* **B+B:** The raw sum is `(4k+2s)f+(b_i+b_j)`. Before a
  wrap its coordinate lies in `[0,2f-4]`. At cell `2k`,
  `B_0+B_0` starts at two, missing `D`; negative `C` offsets
  in that or the next cell cannot be reached. After a wrap the
  form is `(2(s-k)+1)f+e`, `1<=e<=2f-3`. This misses the
  current nonpositive `A` offsets. The only possible next-`A`
  collision is at offset `2f-3`, requiring both `B` indices
  at most one. Then `s<=2` and the possible next `A` index
  `s-k+1<=0`, where no offset `-3` exists. The wrapped sum
  is below `B`.
* **B+D:** Every sum wraps to `(2i+1)f+(b_i+1)`, with
  offset in `[1,f-1]`. It lies above the odd `A` offsets
  and below any nonnegative offset in the next even cell.
* **B+C:** Every sum wraps to `(2(i+j)+1)f+e`, where
  `-1<=e=b_i+c_j+1<=f-2`. It misses `A_0` because
  `j>=1`, misses `A_1` because that run is absent, and misses
  later `A` offsets `-3,-2`. It is above any preceding `B`
  upper endpoint and below the next `B` lower endpoint. A next
  `C` collision would require `e=f-2`, forcing `i<=1`;
  the next even cell then has index `i+j+1<=k+1<2k`, before
  `D,C`.
* **D+D:** The residue is `(2k+1)f+1`, above `B_0` and
  before `B_1`.
* **D+C:** The residue is `(2k+2j+1)f+(c_j+1)`. In the
  preceding `B_j` cell its offset is `f-1` or `f`, above
  every upper endpoint. Neighboring `C` cells cannot be reached.
* **C+C:** With `s=i+j>=2`, the residue is
  `(2k+2s+1)f+e`, `-3<=e<=-1`. The only possible `B`
  target is `B_s`, whose upper offset is `f-4`, below the
  smallest resulting offset `f-3`. Adjacent even `C` cells
  are too far away. There is only one wrap.

These ten cases prove `R+R` avoidance.

### Extras paired with regular types

For `g+R`, the forms are particularly short. The sum with `A_i`
lands above `B_i`, since its coordinate is `f+a_i` and exceeds
that run's upper bound. The sum with `B_i` misses the nonpositive
`C` offsets; at `i=0` it is strictly above `D`. The sums
`g+D` and `g+C_j` reduce to `f+1` and
`(2j+1)f+(c_j+1)`, respectively; these miss `A`, since `j=1`
is absent and later `A` offsets end at `-2`.

An endpoint extra has form

    e_i^(d)=(2k+2i+1)f-d,

where `d=1` is allowed for every `i`, and `d=2,3` only for
`i>=2`. Its sums with the four regular types are as follows.

* With `A_j`, the unwrapped form is
  `2(k+i+j+1)f+(a_j-d)`, with offset in `[-6,-1]`.
  It is beyond `A`, below `m`, and too high to hit the preceding
  `B` cell, whose upper offset relative to this cell is at most
  `-f-2<=-7`. A `C` offset `-2` or `-1` requires `j=0`,
  but then the possible `C` index is `i-k+1<=0`, so no `C`
  run exists there. `D` requires offset zero, which is impossible.
* With `B_j`, an unwrapped sum lies beyond `B` in an odd
  cell with offset `b_j-d in [-3,f-3]`, too far from `C,D`.
  A wrapped sum is `2(i+j-k+1)f+(b_j-d+1)`, with offset
  in `[-2,f-2]`. The only possible next-odd-`A` offsets are
  `f-3,f-2`; attaining either requires `j<=1`. But the
  target `A` index `i+j-k+1<=j<=1` has neither of these
  offsets. Other neighboring `A` positions are out of range.
* With `D`, the residue is `2(i+1)f+(1-d)`, with offset
  in `[-2,0]`. Odd `A` cells are out of range. The only
  possible `B` cell is `B_0`, at `i=k-1`, which excludes
  its offset zero.
* With `C_j`, the residue is `2(i+j+1)f+(c_j-d+1)`, with
  offset in `[-4,-1]` and cell index at most `2k-1`.
  Thus it is before `D,C`, below the same-cell `B` run and
  above the preceding `B` upper endpoint. Adjacent `A` offsets
  cannot be reached because `f>=5`.

This proves (2) for every permitted parameter, including `f=5,k=3`.

## 2. Extra-extra collision classes

The formal pair `g+g` hits `D`. For any endpoint extra,
`g+e_i^(d)=(4k+2i+1)f-d` is in an odd gap before a wrap;
at `i=k-1` its residue is `1-d`, at zero or in the final gap.
Thus it never hits `R`.

For two endpoint extras with indices `i,j`, depths `d,e`, and
`s=i+j`, their sum is

    (4k+2s+2)f-(d+e),                 2<=d+e<=6.           (3)

If `s<=k-2`, this is below `m`; it can hit `R` only at the
lower endpoint of `C_(s+1)`, and only when `d=e=1`.
It is beyond `B,D`, and no other neighboring `C` run is close
enough. If `s>=k-1`, subtracting `m` gives

    (2(s-k+1)+1)f+1-d-e.                                  (4)

This subtraction is valid even at the smallest boundary: its smallest
value is `f+1-6>=0`; equality, possible at `f=5`, is merely
residue zero. The only possible regular targets are `A` entries.
In particular `A_0` can be hit only at its lower endpoint, with
`d=e=1`; later `A` upper/lower endpoints require `d+e=3/4`.
The upper endpoint `f` of `A_0` is never hit.

It follows that every `B_i`, every upper endpoint of `C_j`, and
`f` in every positive block are protected, provided earlier selected
residues lie in `H`. The singleton `D` is also protected if `g`
has only its initial occurrence. The lower endpoint of `C_1` is
protected if `beta_0` has only its initial occurrence: its only
formal extra-pair obstruction is `beta_0+beta_0`, which is then
an inadmissible equal pair. These two uniqueness assertions will be
proved within the same chronological induction, not assumed.

## 3. Initial anchors and chronological confinement

Before `4kf`, the actual sequence is exactly `f` and all `F_i`.
Their successive gaps are the seed translates `f+F_i`. Two nonseed
terms cannot sum below `4kf`, and the only formal representation at
`4kf` is the forbidden double `g+g`. Therefore `D={4kf}` is
selected. The strict self-sum

    F_0 dotplus F_0=[4kf+1,(4k+2)f-3]                     (5)

covers the next gap. Its next two integers constitute `C_1`.
They are protected by the collision classification: `g` and `beta_0`
so far have only their initial copies. This argument can equivalently
be made as the initial part of the following ascending induction.

We prove simultaneously:

1. Every selected integer has residue in `H`.
2. Residues `g` and `beta_0` occur only at their initial values.
3. In every positive block, `f`, every `B_i`, `D`, every
   upper endpoint of `C_j`, and both endpoints of `C_1` occur.
   The corresponding protected `B,D,C` entries occur also in block zero:
   every `B_i`, `D`, each upper `C` endpoint, and both endpoints
   of `C_1`. No other lower `C` endpoint is asserted initially.

The collision calculation proves protection under assertions 1 and 2
for earlier integers. Initially the anchors above supply the entries
through `C_1`. For each `1<=j<k`, the initial disjoint sum

    F_0+F_j=[(4k+2j)f,(4k+2j+2)f-2]                     (6)

covers the gap after `C_j`, and the last extends through the end
of block zero. It may also exclude a lower endpoint of a later `C`
run, which is permitted by the envelope. It never excludes a protected
upper endpoint. Together with (5), this proves the assertions through
block zero by induction over the scanned integer. All omitted `A`
points before the second seed are outside the greedy decision range.

For block `n>=1`, use the following actual sums to cover the complement
of `H`. The displayed intervals are offsets relative to `nm`.

| Region | Sums | Offset interval |
| --- | --- | --- |
| Before `A_0` | `F_(k-2)+B_1[n-1]` | `[-f+1,f-2]` |
| First part after `A_0` | `F_(k-1)+B_1[n-1]` | `[f+1,3f-2]` |
| Bridge across the absent `A_1` | `F_0+C_1[n-1]` | `[3f-1,4f-1]` |
| Last part before `A_2` | `F_(k-1)+B_2[n-1]` | `[3f+1,5f-4]` |
| After `A_i`, `2<=i<=k-2`, first part | `F_(i-1)+C_1[n-1]` | `[(2i+1)f-1,(2i+2)f-1]` |
| After `A_i`, `2<=i<=k-2`, second part | `F_(k-1)+B_(i+1)[n-1]` | `[(2i+1)f+1,(2i+3)f-4]` |
| After the last `A`, first part | `F_(k-2)+C_1[n-1]` | `[(2k-1)f-1,2kf-1]` |
| After the last `A`, through repeated `g` | `F_(k-1)+D[n-1]` | `[(2k-1)f+1,2kf]` |
| After `F_i`, `0<=i<k` | `F_i+{nm+f}` | `[(2k+2i+1)f,(2k+2i+2)f-1]` |
| After `D` | `F_0+B_0[n]` | `[4kf+1,(4k+2)f-3]` |
| After `C_j`, `1<=j<k` | `F_(j-1)+B_1[n]` | `[(4k+2j)f,(4k+2j+2)f-3]` |

The first three rows after `A_0` together cover its entire gap
`[f+1,5f-4]`, including the absent `A_1` cell. The two rows
after each later `A` overlap and fill its gap. The last two `A`
rows also overlap. The rows after `F` and `C` reach the next
run or the block end. Empty index ranges contribute no rows.

The row ending at `2kf` excludes every repeated `g`. In addition,
every repeated `beta_0` is excluded by the lower endpoint of
`C_1[n-1]` plus `F_(k-1)`; the resulting interval is

    nm+[(2k+1)f-1,(2k+2)f-2].                            (7)

Thus the two uniqueness assertions needed for protection are established
at their own scan times. Every summand in the table and (7) is positive
and therefore smaller than its target. The same-block `B` or `f`
entry used in a witness has already been selected before that target;
an entire not-yet-constructed block is never assumed.

Distinctness is automatic when `n>=2`: one factor is an initial `F`
entry and the other belongs to a positive block. At `n=1`, all
`F/C` and `F/D` factors are disjoint. The initial `F/B` overlaps
are handled explicitly:

* If `k=3`, the low row `F_(k-2)+B_1[0]` shares a lower
  endpoint. The only lost sum has offset `-f+1<0`, outside the
  low gap being covered. Its upper endpoints differ.
* A row `F_(k-1)+B_j[0]` can overlap only when `j=k-1`.
  It loses exactly its shared lower-endpoint double. For `k=3`
  this is offset `3f+1`, already in the bridge
  `F_0+C_1[0]`. For `k>=4` it is
  `(2k-3)f+1`, already in `F_(k-3)+C_1[0]`, the first
  row of the same `A` gap.

These intervals each have length at least two; even the shortest
`B_j`, for `j>=2,f=5`, has two entries. Two overlapping integer
intervals of length at least two lose no interior sum under the
distinctness rule: replace a diagonal `(x,x)` by `(x-1,x+1)`
in a feasible order. An order fails only when both intervals start
at `x` or both end at `x`, describing shared extreme sums. In the
two cases above only the lower extreme is shared. Hence the repairs
exhaust all losses. This completes the chronological induction.

## 4. First extinction: beta extras and lower C endpoints

From the envelope and (2), a missing point of `R` above `g` must
be excluded by two actual extra entries. The seed `g` paired with
an endpoint extra misses `R`, and `g+g` is forbidden by uniqueness.
Equations (3)--(4) show that a missing lower endpoint of `C_l[n]`
requires two selected beta extras with

    i+j=l-1,          q+r=n,                              (8)

where their actual values lie in blocks `q,r`. Upper `C` endpoints
are protected. Condition (8) is necessary only; we do not assert its
converse and may harmlessly enlarge possible obstructions by allowing
formal equal pairs.

The induction already proved `beta_0` occurs only in block zero.
Also every later `beta_1` is excluded by

    D[0]+{lower endpoint of C_1[n-1]}=nm+beta_1,   n>=1.

These are distinct actual entries, even when `n=1`, because initial
`D` and `C_1` are disjoint. Hence beta indices zero and one have
no positive-block occurrences.

We prove for `1<=i<k` that `beta_i` is absent in all blocks
`n>=i`, and that `C_l[n]` is full for `n>=l-1` whenever
`1<=l<k`. The `l=1` statement was already protected in every
block. Suppose the beta bounds hold for all indices below `l`,
where `l>=2`. If (8) involves index zero, that term is in block
zero and the other index is `l-1`, so the other block index is
at most `l-2`. If both indices are positive, their block indices
sum to at most

    (i-1)+(j-1)=l-3.

Thus (8) cannot hold when `n>=l-1`, and `C_l[n]` is full
there. For `n>=l`, the distinct pair

    D[0]+{lower endpoint of C_l[n-1]}=nm+beta_l

then excludes `beta_l`. This closes the induction. No exact
description of the other transient entries is used.

## 5. All remaining extras vanish, then every A run fills

For `i>=2` and `n>=max(2,i-1)`, the full intervals `C_1[0]`
and `C_(i-1)[n-1]` lie in different blocks, and their sum is

    nm+(2k+2i+1)f+[-3,-1].                               (9)

The second interval is full because its block index `n-1` is at
least `(i-1)-1`; for `i=2`, `C_1` was full throughout.
Equation (9) therefore excludes all three extras
`delta_i,gamma_i,beta_i`. The factors are distinct actual integers
even when `i=2`, since their blocks differ. Together with uniqueness
of `g,beta_0,beta_1`, this proves that **every extra residue is
absent in all blocks `n>=K=max(2,k-2)`**. All `C` runs are also
full by this point.

Consider an `A` entry in a block `n>=2K`. It is above the second
seed. If it were missing, its obstruction would have to be a pair of
endpoint extras of the wrapped type (4), in blocks `q,r` with

    q+r+1=n.

But every extra is absent from block `K`, so `q,r<=K-1` and
`n<=2K-1`, a contradiction. Thus every `A` entry is selected
from block `2K`. The `B,D` core is protected throughout, every
`C` run is now full, and the envelope excludes all other entries.
This proves (1) for every later integer.

## What this replaces, and what it does not claim

This argument proves eventual reachability of the same regular residue
set for all `f>=5,k>=3`, including the quotient boundaries, by a
chronological envelope and two finite extinction stages. It replaces the
certificate dependency for eventual periodicity on this family. It does
not prove the older exact five-block transient table, its least preperiod,
or source preperiod formulas. The sufficient bound is deliberately weaker
for some `k`, which permits one uniform analytic mechanism.

The attempt initially considered rechecking the entire table by written
pair-sum identities. The simpler route is that `H+R` is safe, only
beta-beta pairs can damage high runs, and completed high runs eliminate
all three extra depths. Treating every extra type as having the same
dependency would obscure this triangular order. Assuming ordinary
sum-freeness of all of `H` would also be false: `g+g=D` and
`beta_0+beta_0` is the lower endpoint of `C_1`. Their actual
uniqueness, not deletion of formal diagonal cases from modular algebra,
is the repair.

The old files remain unchanged. The accompanying check record identifies
the exact version and any diagnostic outcomes. Actual service-supplied
model identity, version and configuration are unknown. Full-text human
review and manual submission are required; no human or machine approval
is assigned. Prose/data use CC BY 4.0 and code uses MIT under the
repository's contribution terms.
