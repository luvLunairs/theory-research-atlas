> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# A self-contained lower-offset extinction lemma

18 October 2026. Local scientific draft for full-text human review and
manual submission. This appendix reorganizes the already retained lower
proof into one chronological argument. It is same-team AI contribution
checking, not independent verification, formal verification or approval.

## Statement and notation

For integers `k>=1`, `a>=2` and `f>=2a`, let `S` be the strict
greedy sequence initialized by `f,g`, where

    g=2kf+a,                 m=(6k-1)f+2a-1.

After the two forced seeds, a candidate is selected precisely when it
is not the sum of two distinct earlier selected integers. In particular,
unselected integers below `g` need not have such representations.
Every interval below contains integers and includes its endpoints.
Define subsets of `[0,m)` by

    A_i=2if+[f-a+1,f],                         0<=i<k,
    B_0=2kf+[a+1,f],
    B_i=2(k+i)f+[a,f],                        1<=i<k,
    C_0=4kf+[a,2a],
    C_i=2(2k+i)f+[a,2a-1],                   1<=i<k,
    R=union_i(A_i union B_i union C_i).

Then

    x in S if and only if x mod m in R,       for every x>=4km.   (1)

This proves eventual characteristic periodicity with period `m`.
No least period or exact preperiod assertion is needed for this lemma.
The domain includes `f=4,a=2`; every inequality below uses only
`a>=2` and `f>=2a`. The separately retained
[first-seed-four specialization (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material)
was also reread and has the same collision indices and extinction bounds.

The proof combines the [earlier template (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material),
[anchor argument (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material),
[envelope argument (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material), and
[extinction argument (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material).
Their exact examined versions are recorded in the accompanying
[audit (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material). Van Berkel and Bosma's
[Definition 3(2), Conjecture 5](https://arxiv.org/html/2609.18522v1)
motivates the period prediction; their conjecture is not used as a premise.

Write `X[n]=nm+X` for a translated set and put

    F_i=2(k+i)f+[a,f+a-1],
    D_i=(2k+2i+1)f+[1,a-1],                  0<=i<k,
    H=R union {g} union union_i D_i.

Here `H=R union union_i F_i`, `f in R`, and the displayed union into
`R`, `{g}` and the strips `D_i` is disjoint. The runs of `R` and these
strips lie in `[0,m)`. We shall prove that all selected residues lie
in `H`, that `g` occurs only initially, and that only lower parts of
the `A,C` runs can be missing. The selected subsets of the strips
need not be intervals.

## 1. Modular compatibility

The following stronger exclusion permits equal residues:

    ((H+R) mod m) intersect R is empty.                    (2)

It therefore also applies to distinct actual integers from different
blocks with the same residue. Here is a complete carry check.

Use cells of length `2f` and write

    m=2f(3k-1)+D,                 D=f+2a-1.

Every selected coordinate of `R` lies in `[a,f]`; an `A` coordinate
is at least `f-a+1>=a+1`. In the six `R+R` cases, the raw coordinate
is in `(0,2f]`. A coordinate above `f` is unselected, and coordinate
`2f` carries to an unselected zero. Each summand is below `m`, so
there is at most one subtraction of `m`.

* `A+A` has coordinate `[2f-2a+2,2f]`, above `f` or at the zero
  carry. Its largest actual sum is `(4k-2)f<m`.
* `A+B` has coordinate `[f+1,2f]` and largest actual sum
  `(6k-2)f<m`, so the same argument applies.
* For `B_i+B_j`, an unwrapped sum can meet only a `C` cell. In
  cell `2k` it uses `B_0+B_0` and starts at `2a+2`, above `C_0`.
  In later `C` cells it starts at least at `2a`, above their upper
  coordinate `2a-1`. If it wraps, subtract `D` from the raw
  coordinate `r`. Without a borrow the new cell is
  `i+j-k+1<=k-1` and its coordinate is at most `f-2a+1`, below
  the relevant `A` run. With a borrow the coordinate is
  `r+f-2a+1>=f+1`. Only nonnegative reduced cells can arise in
  a sum that actually wraps.
* `A+C` has raw coordinate `[f+1,f+2a]`, giving exclusion before
  a wrap. After a wrap, the nonborrowed coordinate is at most `1`;
  the borrowed coordinate is at least `2f-2a+2>f`.
* Every `B+C` sum exceeds `m`. Its coordinate is in
  `[2a,f+2a]`. A borrow leaves at least `f+1`; without a borrow
  the coordinate is `0` or `1`.
* Every `C+C` sum exceeds `m`. Its coordinate is in `[2a,4a]`.
  A borrow leaves at least `f+1`; without a borrow it is at most
  `2a-f+1<=1`.

Thus `R+R` avoids `R` modulo `m`. Because `f in R`, it remains
only to check `F_i+R`.

* `F_i+A_j` has coordinate `[f+1,2f+a-1]`. Its possible `2f`
  carry leaves at most `a-1`; without that carry it exceeds `f`.
  Its maximum `(6k-2)f+a-1` is below `m`.
* For `F_i+B_j`, the only possible unwrapped target is a `C`
  cell. Cell `2k` requires `i=j=0` and its coordinate starts
  at `2a+1`; every later `C` cell has minimum sum coordinate
  `2a`. Both are above the corresponding `C` maximum. A `2f`
  carry leaves at most `a-1`. After an `m` wrap without a borrow,
  the cell is `i+j-k+1<=k-1` and the coordinate is at most
  `f-a`, below `A`; a borrow leaves at least `f+1`.
* Every `F_i+C_j` sum wraps. A borrowed coordinate exceeds `f`.
  A nonborrowed coordinate is at most `a`. Equality `a` requires
  the upper endpoints of `F_i` and `C_0`. Its cell is `i+1<=k`:
  `A` excludes coordinate `a`, and `B_0` begins at `a+1`.

This proves (2), including `k=1` and `f=2a`.

## 2. Actual initial anchors

Up to the end of `F_(k-1)`, the selected terms are exactly `f` and
the intervals `F_0,...,F_(k-1)`. The seed sum `f+F_i` is precisely
the gap after `F_i`, and every sum of two nonseed terms is at least
`2g`, which exceeds the last endpoint `(4k-1)f+a-1` of these
intervals. Ascending induction from the second seed proves the claim.

The following seed gap ends at `4kf+a-1`. The interval `C_0`
is then selected: its last point is `4kf+2a=2g`, whereas the
smallest distinct sum of nonseed entries is `2g+1`. Moreover
`f+C_0` starts after `C_0`, since `f>a`. Consequently all
`F_i` and all of `C_0` are actual initial entries, not hypothetical
tail entries.

## 3. Which extra pairs can hit the proposed tail?

For `x=(2k+2i+1)f+d in D_i` and
`y=(2k+2j+1)f+e in D_j`, with `1<=d,e<=a-1`, their raw sum is

    2f(2k+i+j+1)+(d+e),              2<=d+e<=2a-2.         (3)

If `i+j<=k-2`, it lies below `m` and can hit `R` only in
`C_(i+j+1)`, strictly below its upper endpoint `2a-1`. If
`i+j>=k-1`, it exceeds `m`; after one subtraction its canonical
form is

    2f(i+j-k+1)+(f+d+e-2a+1).                            (4)

Its coordinate is between `f-2a+3>=3` and `f-1`, and its cell
index is in `[0,k-1]`. Thus it can hit only a lower part of
`A_(i+j-k+1)`. In particular no such sum hits any `B_i`, any
`A_i` upper endpoint, any `C_i` upper endpoint, or any point of
`C_0`.

Furthermore

    g+D_i=(4k+2i+1)f+[a+1,2a-1].                         (5)

For `i<k-1`, the coefficient of `f` is odd, so its canonical
`2f`-cell coordinate is `f+[a+1,2a-1]`, strictly between `f`
and `2f`; it misses `R`. For `i=k-1`, (5) lies in
`[m-a+2,m]`, the final unselected gap or residue zero. The formal
pair `g+g` will be unavailable because the chronological induction
below proves that the seed `g` has no selected translate.

## 4. Chronological envelope and protected entries

We prove simultaneously, in increasing order of the scanned integer:

1. Every selected integer has residue in `H`.
2. The only selected occurrence of residue `g` is the initial seed.
3. In every positive block all `A` upper endpoints, every `B_i`,
   all of `C_0`, and all `C_i` upper endpoints are selected.
4. In block zero every `B_i`, `C_0`, and every `C_i` upper
   endpoint is selected. Initially skipped `A` entries below `g`
   are not claimed to be selected.

By (2), a pair hitting `R` must use two non-`R` residues. By
(3)--(5), such a pair of previously admitted terms cannot hit any
of the listed protected entries. The only remaining formal case is
`g+g`; under the inductive assertion of uniqueness it is not a
pair of distinct actual integers. Thus any protected candidate must
be selected when the scan reaches it.

For the initial block, Section 2 supplies the entries through `C_0`.
Every point outside `H` after `C_0` and below `m` is covered by

    F_0 distinct-plus F_0
      =[4kf+2a+1,(4k+2)f+2a-3],
    F_0+F_i
      =[(4k+2i)f+2a,(4k+2i+2)f+2a-2],     1<=i<k.      (6)

The first interval starts just after `C_0` and reaches the next
`C` run's lower endpoint minus one. Each later interval covers the
gap after its `C_i`; the last reaches the end of the block. For
`k=1` the first interval alone reaches that end. The endpoint
comparisons use `a>=2`. The second line uses disjoint initial
intervals, and the first is the exact restricted sumset of an
integer interval. Thus the induction gives assertions 1, 2 and 4
through block zero.

For block `n>=1`, the following actual sums cover all gaps of `H`
and also every repeated `g`. Endpoints in the last column are
relative to `nm`.

| Location | Sums | Offset interval |
| --- | --- | --- |
| Before `A_0` | `F_(k-1)+B_0[n-1]` | `[-f+2,f-a]` |
| After `A_i`, `0<=i<=k-2` | `F_(k-1)+B_(i+1)[n-1]` | `[(2i+1)f+1,(2i+3)f-a]` |
| After `A_(k-1)`, including `g[n]` | `F_(k-1)+C_0[n-1]` | `[(2k-1)f+1,2kf+a]` |
| After `F_i`, `0<=i<k` | `F_i+{nm+f}` | `[(2k+2i+1)f+a,(2k+2i+2)f+a-1]` |
| After `C_0` | `F_0+B_0[n]` | `[4kf+2a+1,(4k+2)f+a-1]` |
| After `C_i`, `1<=i<k` | `F_(i-1)+B_1[n]` | `[(4k+2i)f+2a,(4k+2i+2)f+a-1]` |

The last row is absent for `k=1`; the preceding row then covers
the final gap. For `k>=2` the last row extends past the block end.
All sums using a current-block protected entry use an entry smaller
than the target, because the other summand is positive. Hence the
table does not assume that the rest of the current block has already
been constructed. The row ending at `g[n]` forbids each repeated
`g` using previously established entries, closing its uniqueness
assertion within this same induction.

For `n>=2`, each pair consists of an initial `F` entry and a
positive-block entry, so it is distinct. For `n=1`, the needed
initial `B,C` entries exist by assertion 4. Initial `F/C` pairs
are disjoint; `F_(k-1)` and `B_j[0]` are disjoint when
`j<k-1`. Two overlaps remain:

* When `k=1`, the first row uses `F_0+B_0[0]`. Their lower
  coordinates are `a,a+1`, and their upper coordinates are
  `f+a-1,f`, respectively. Neither extreme is shared, so no
  sum is lost when equal actual summands are forbidden.
* When `k>=2`, the last gap between `A` runs uses
  `F_(k-1)+B_(k-1)[0]`. Only its first sum is lost, because
  the lower endpoint is shared and the upper endpoints differ.
  Its missing offset is `(2k-3)f+1`. The disjoint pair
  `F_(k-2)+C_0[0]` gives
  `[(2k-3)f+1,(2k-2)f+a]`, which repairs that point.

Here we used a simple interval fact: two integer intervals, each of
length at least two, lose no interior sum upon forbidding a diagonal
pair. For an interior sum `2x`, a representation `(x,x)` can be
replaced by `(x-1,x+1)` in one order unless both intervals start
at `x` or both end at `x`; these exceptional possibilities are
exactly shared extreme sums. All intervals above satisfy the length
condition, including `f=2a` and `a=2`.

This proves all four assertions. It is a forward induction on
integers, not a hypothesis that an entire periodic block is already
present.

## 5. Finite extinction of arbitrary selected strips

Let `E_i[n]=(S intersect (nm+D_i))-nm`, for `n>=0`. These are
arbitrary subsets. By the envelope and (2)--(5), any missing `R`
entry above `g` must be excluded by two actual strip entries.
Equations (3)--(4) give the following necessary conditions:

* A missing point of `C_l[n]`, `l>=1`, requires nonempty
  `E_i[q],E_j[r]` with `i+j=l-1` and `q+r=n`.
* A missing point of `A_l[n]`, **`n>=1`**, requires nonempty
  `E_i[q],E_j[r]` with `i+j=k+l-1` and `q+r=n-1`.

These are one-way implications. Enlarging possible pair sums to
include equal terms cannot invalidate the exclusion of every possible
obstruction. No implication is applied to preseed holes.

We claim

    E_i[n] is empty whenever n>=2i+2.                     (7)

For `i=0,n>=2`, the selected intervals `C_0[0]` and `C_0[n-1]`
lie in different blocks. Their sum, relative to `nm`, is

    (2k+1)f+[1,2a+1],

which covers `D_0`. Thus every candidate in that strip is forbidden.

Suppose (7) holds for every `i<l`. If `C_l[n]` had a missing
point, its necessary obstruction would have `i+j=l-1` and

    q<=2i+1,   r<=2j+1,   n=q+r<=2(i+j)+2=2l.

Therefore `C_l[n]` is full for `n>=2l+1`. For `n>=2l+2`,
use the initial `C_0[0]` and this full `C_l[n-1]`. Their sum,
relative to `nm`, is

    (2k+2l+1)f+[1,2a],

covering `D_l`. The two factors are in different blocks and all
their elements are positive, so every target has distinct smaller
summands. This proves (7) by induction on `l`.

All extra strips are therefore empty from block `2k`, and all
`C` runs are full from block `2k-1`. A missing `A_l[n]` in a
positive block would require

    n-1=q+r<=2i+1+2j+1=2k+2l.

Hence `A_l[n]` is full for `n>=2k+2l+2`, whose largest value
is `4k`. From block `4k` onward the protected `B` runs remain,
the `A,C` runs are full, the strips are empty, repeated `g` is
excluded, and the envelope excludes everything else. This proves
(1) for all later integers, not merely for a checked finite prefix.

## Scope, checks and assistance

This appendix supplies the chronological and distinctness details
needed to use the lower-offset argument as one analytic component
of an eventual-periodicity proof. It neither extends the argument
above `a=f/2` nor relies on numerical stabilization, a finite-state
claim, exact transient interval shapes, or the source preperiod formula.

It was prepared by the same Codex contributor who participated in the
earlier lower-offset work, then reread against the sealed files and
the interval identities in the audit. No new enumeration or program
execution was used for the mathematical claim. Actual service-supplied
model identity, version and configuration remain unknown; the parent
audit's assistance record applies. The same-team relationship and the
need for full-text human review and manual submission remain unchanged.
Prose and mathematical data are offered under the repository's
CC BY 4.0 terms.
