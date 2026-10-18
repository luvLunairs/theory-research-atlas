> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Adversarial audit of the analytic upper branches

18 October 2026. Local scientific draft for full-text human screening and
manual submission. This is a fresh mathematical reading by a contributor
to the same AI-assisted project, including some of the arguments being
examined. It is not independent scientific verification, a human review,
an approved machine check, or a claim of priority.

## Finding and exact scope

No unresolved logical gap in **eventual periodicity** was identified in
the analytic branches listed below. In particular, the two apparent
diagonal exceptions in the envelope arguments are handled by induction
on actual integers; discarding those exceptions merely because their
residues agree would be invalid. The finite exceptional targets in the
first-plateau proofs also require their stated occurrence restrictions.
Those restrictions were checked, rather than replaced by modular
sum-freeness of the eventual tail.

This finding does not validate the whole proposed theorem. The upper
boundary `a=f-1` for `k>=2`, the rays `a=f+1,f+2` for `k>=2`, and the
exception `k=2,a=f+3` use separate symbolic certificates. Their engines,
certificates and continuation arguments are outside this reading. The
lower branch, midpoint and small-first-seed work are also outside it.
The full theorem therefore remains **inconclusive within this audit's
scope alone**, even though no repair was required for the analytic
arguments actually examined.

The target is the strict greedy sequence with positive seeds `f<g`.
At each integer above `g`, membership means that the integer is not a
sum of two distinct earlier selected integers. The audit is concerned
with the existence of a nonempty periodic tail. Least periods, exact
starts and least gap preperiods were not comprehensively re-audited.
No new parameter enumeration or certificate replay was used here.

The requested readings, with SHA-256 hashes taken from the actual files,
are:

| File, relative to `work/` | SHA-256 |
| --- | --- |
| `greedy-upper-20261018/unified-theorem.md` | `3CB5934F1F09B03A23F0164234AAAF416E65DF0852B41A0E668397B31A04E438` |
| `greedy-upper-20261018/compatibility.md` | `1416B25D62306438E705C30969F580A299D8391AEEACB156A2B6913506D12920` |
| `greedy-upper-20261018/upper1/proof.md` | `3BA64BE838CF746AE7308F72FD3051CAFA50FE759A001E8B7CBEEB15D5D4BC60` |
| `greedy-upper-20261018/upper2/proof.md` | `21BECD61D994FE36CDE9A0FD8FBF82FC98C1E13F970CAF7AEE6359CF042E3FFB` |
| `greedy-lower-20261018/mechanism.md` | `30D4C3F56AEE91272E9C634F62136BDB89559696E9845EE1059E872C8BBB9D1A` |
| `greedy-lower-20261018/even/proof.md` | `A0EEE3F1C2515F49B96DB5CB5BA8A8FBE2CF368238802BD4BEE495E5117964C3` |
| `greedy-lower-20261018/lower/proof.md` | `37869C5D0F046630877277526F7B6ABDDE369A672811EEC017702CB2DBD82487` |
| `greedy-unified-20261018/odd-multiple-proof.md` | `F5C508D9D7562015BB998F3F6FFFBB97EBDDCD086E570421D49F30065B1B6627` |

The following sections give the checked logical chains in continuous
form, including the delicate endpoint calculations. They retain the
notation and credit of the linked arguments; they do not claim new
formulas. All intervals are inclusive integer intervals.

## The common identification argument

For a proposed positive set `T` containing exactly `f,g` at or below `g`,
two properties suffice: no member of `T` is a sum of distinct members of
`T`, and every integer greater than `g` outside `T` is such a sum. The
representing summands are positive and strictly smaller than their sum.
Induction on the candidate integer therefore identifies `T` with the
greedy sequence. This is a direct induction over all integers, not an
inference from a long observed prefix.

The envelope proofs use a slightly different but equally causal
induction. At a candidate `x`, assume confinement, the necessary
protected entries and uniqueness of exceptional entries only for
integers strictly below `x`. A protected entry is selected because the
complete collision classification rules out a representation using
those smaller entries. An omitted entry is excluded by a displayed pair
of positive protected or initial entries. Each member of that pair is
smaller than `x`, even if it belongs to the same numbered block as `x`.
Thus no entire future block is assumed to have been selected.

For disjoint integer intervals, ordinary endpoint sums give the exact
sum interval. For a self-pair of `[l,u]`, distinct sums give
`[2l+1,2u-1]`, provided `l<u`. A pair of nested intervals with a shared
lower endpoint and different upper endpoints loses just the doubled
lower endpoint in the specific overlap used below: all interior
diagonals can be replaced by neighboring integers in the appropriate
order. These facts are used with actual intervals, not just residues.

## Upper interior: compatibility and causal confinement

The interior domain is `k>=1`, `f>=5`,
`ceil(f/2)+1<=a<=f-2`. Set

    Q=2f, d=2a-f-1, b=f-a, m=(3k+1)Q+d.

Then `b>=2`, `d>=1`, `a=b+d+1`, `f=2b+d+1`, so `a>=4`
and `d+2<a`. The periodic set consists of the following `Q`-cells:

    A_i=iQ+[a,f]                         (0<=i<k-1),
    A_(k-1)=(k-1)Q+[a,f+1],
    B_i=(k+i)Q+[a,2a-1]                 (0<=i<k),
    C=2kQ+[a+1,2a-1],
    D_i=(2k+1+i)Q+[a+d,2a-1]            (0<=i<k).

Let their union be `R`. Enlarge it to `H` by adding
`E_i=(k+i)Q+[2a,f+a-1]` and `u=2kQ+a`, `v=2kQ+2a`.

I recalculated the ten `R+R` and twelve extra-plus-`R` rows in
[compatibility.md](../greedy-upper-20261018/compatibility.md). The
following carry details are necessary for their claimed exclusion.
The doubled exceptional endpoint of `A_(k-1)` carries to a coordinate
at most `2`, below every selected lower coordinate. The other low
carries from `A+B,A+C,A+D` are at most `d+1`. Carries from `B+B,B+C`
below `m` can be as large as `2d`, but land only in `D` cells or the
empty terminal cell, and `2d<a+d`. Thus a low-coordinate argument
without the cell location would have been insufficient in these rows.

After subtraction of `m`, the lower uncarried coordinate for `B+B` is
`f+1`. Its cell index is at most `k-3`, so it cannot hit the exceptional
`f+1` endpoint in `A_(k-1)`. For `B+C` the lower coordinate is `f+2`
and the cell index is at most `k-2`; for `C+C` it is `f+3` in cell
`k-1`. The other wrapped rows start above the upper selected endpoint
in their possible cells. Their residual carries are at most `d`, or
at most `1` for `A+D`. A raw sum in cell `3k` crossing `m` produces
the same reduced low-coordinate case; the portion before crossing
lies after the final `D` run. This also checks the partial terminal
cell rather than treating `m` as a multiple of `Q`.

In `E+A`, a carried coordinate can equal `a` only by using the top of
`E_i` and the exceptional endpoint of `A_(k-1)`. The resulting cell is
`2k+i`: its run starts at `a+1` when `i=0` and at `a+d` otherwise.
The alleged collision is therefore absent even at `d=1`. Below `m`,
the carried part of `E+B` is at most `a+d-1` in a `D` cell. After
wrapping, the `E+B,E+C` portions start above the relevant `A` runs,
and any carry is at most `a-1`. The same bound deals with `E+D`.
The `u` and `v` rows reduce to the stated gaps; the largest delicate
low coordinate from `v+A` is `d+2<a`. These computations prove

    ((H+R) mod m) intersect R = empty.

The complete residual collision list among extras is especially
important. With `s=i+j`, the ordinary sum `E_i+E_j` first carries `Q`
to cell `2k+s+1`, with coordinate interval `[2d+2,2a-2]`. For
`s<=k-1` it can meet only `D_s`, below its upper endpoint, and has
actual block index `q+r` if the two extras are in blocks `q,r`.
For `s>=k`, subtracting `m` gives cell `s-k` and coordinates
`[d+2,f-1]`; its actual block index is `q+r+1`. Both input indices
strictly exceed the target index `s-k`.

The sum `v+E_i` can meet `A_i` only at coordinate `a`, requiring the
top of `E_i`; an initial `v` shifts its block index by one. The sum
`u+u` can meet `A_(k-1)` at coordinate `f+1`. The remaining types
`u+E_i,u+v,v+v` miss `R`. This is exhaustive: the envelope has only
the categories `R,E_i,u,v`, and every pair with an `R` input has
already been excluded. In particular, the `u+u` row may not yet be
discarded, since two different occurrences would be a legal pair.

Before `u`, the true sequence consists of the seed `f` and the full
anchors `F_i=B_i union E_i`. Seed-plus-anchor sums fill the intervening
gaps. The next interval `[u,v]` is also selected: distinct sums of two
anchor entries start at `2g+1=v+1`, and all seed-plus-anchor sums end
at most at `u-1`. The initial coverage after `[u,v]` follows from the
restricted self-sum of `F_0`, the disjoint sums `F_0+F_i` for `i>=1`,
and `F_0+[u,v]`. These intervals reach at least the integer preceding
the next `D` run, or extend through the block end. They may also cover
an unprotected lower portion of a `D` run; no claim that each initial
`D` run is already full is needed. This confines block zero and establishes its protected
`B,C,D` upper entries.

For positive blocks, the witnesses in
[upper1/proof.md](../greedy-upper-20261018/upper1/proof.md) cover every
gap between the `A` runs, between anchors, after `C`, and after the
`D` runs. Recalculation gives exact gap endpoints in each row. The
last `F` gap ends at `u[n]-1`, and

    max(F_0)+max(A_(k-1)[n]) = u[n]

excludes the next `u`. The two summands are in different blocks.
The `v[n]` witness starts at exactly `v[n]`, using the seed `g` and
the protected lower endpoint of `B_0[n]`. Consequently the uniqueness
of both exceptional entries is an assertion obtained from earlier
actual entries, not an assumption about the completed block.

The one overlap needing special treatment is
`F_(k-1)+B_(k-1)[0]` when proving a gap in block one. These intervals
share their lower endpoint. Their lengths are `f` and `a`, with
`a>=4` and `f-a>=2`; removing equal summands deletes only their
lowest sum. At `k=2` its offset is `-f+1`, outside block one. At
`k>=3` it is `(2k-5)f+1`, and the disjoint pair

    u+B_(k-2)[0] = m+[(2k-5)f+1,(2k-5)f+a]

repairs it. At `k=1` none of these indices exists, and the separate
`F_0+C[0]`, `u+C[0]`, and final-gap rows are disjoint actual pairs.
Thus the chronological induction closes also at the smallest quotient.

## Upper interior: extinction follows from a triangular dependence

It remains to show that confinement is a periodicity argument rather
than merely a bounded-residue argument. Let `E_i[n]` be the actual,
possibly noninterval subset of extra strip `i` in block `n`.

A missing point of `A_l[n]`, for `n>=1`, requires either
`E_i[q]+E_j[r]` with `i+j=k+l` and `q+r=n-1`, or the initial `v`
plus the top of `E_l[n-1]`. The `u+u` possibility is now impossible
because uniqueness of `u` has been proved. For `l=k-1` there is no
extra pair with `i+j=2k-1`. Thus `A_(k-1)[n]` without its lower
endpoint is always full. Adding fixed `F_0` excludes every extra
coordinate at least `2a+1`; the top `f+a-1` lies strictly above
`2a`, because `f-a>=2`. In the following block the `v` obstruction
has disappeared too. Hence `A_(k-1)` is full and its extra strip
empty for all `n>=2`.

Induct down on `l`, setting `T_l=3(k-l)-1`. For a potential pair
with `i+j=k+l`, both indices exceed `l`, so prior induction gives

    q+r <= (T_i-1)+(T_j-1) = 3(k-l)-4.

Because the target index is `n=q+r+1`, these pair obstructions are
absent for `n>=3(k-l)-2=T_l-1`. In those blocks only the lower
endpoint of `A_l` can be missing. The same anchor addition removes
the top of `E_l`, and the next block has full `A_l`; adding `F_0`
then excludes all of `E_l`. This proves extinction from `T_l`.

A missing point of `D_l[n]` requires an extra pair with `i+j=l`
and, importantly, `q+r=n`, with no extra block carry. Its latest
possible block is

    n <= T_i+T_j-2 = 6k-3l-4.

Therefore each `D_l` is full from `6k-3l-3`. By block `6k-3`
every run of `R` is full and every extra has disappeared. The
displayed nonempty periodic word really is the greedy tail. The
strict inequality removing the extra top fails at `a=f-1`; the
proof and the combined decomposition correctly exclude that line.

## High plateau: the exceptional diagonal is harmless only causally

Here `f>=5`, `k>=2`, `3<=b<f`, with `(k,b)!=(2,3)`. Use the
notation of [upper2/proof.md](../greedy-upper-20261018/upper2/proof.md):

    h=2k+1, c=2b-1, m=3hf+c,
    F_i=[(h+2i)f+b,(h+2i+1)f+b-1]        (0<=i<=k),
    D=[(2h+2)f+c-1,(2h+2)f+c],
    E_j={(2h+2+2j)f+c}                  (1<=j<=k-1),
    H={f} union all F_i union D union all E_j.

The tail `R` removes `u=max F_0`, the three-point interval
`V=(h+4)f+[c-2,c]`, and the two-point intervals
`W_i=(h+2i)f+[c-1,c]`, `3<=i<=k`. These holes fit inside their
stated intervals. For `B_i=R intersect F_i`, both endpoints of
`F_k` remain in `B_k` in this domain. If `k=2` this uses `b>=4`;
if `k>=3` it follows from `b>=3` and `b<f`. The holes have length
at most three, so addition of a length-`f` interval bridges each
hole. Explicitly, if a hole has length `t<=3`, the two resulting
sum intervals are adjacent or overlapping because `f>=t+1`.
It follows that `F_i+B_k=F_i+F_k` as ordinary intervals.

The pair classification was checked by category. Seed-plus-`F` sums
occupy following gaps; seed-plus-high-entry sums occupy high gaps
or residue zero. For `s=i+j`, the raw `F_i+F_j` interval is

    [(2h+2s)f+2b,(2h+2s+2)f+2b-2].

It lies above the last `F` interval. It misses each high singleton
by one at the relevant endpoint, and its only possible `D` hit is
the lower endpoint of `D`, attained as `u+u`. After subtracting
`m`, any portion is below `g`; the two successive cases `s=k` and
`s=k+1` end at `f-1` and start at `f+1`, respectively, so the seed
residue is not hit. No second modulus subtraction is possible.

The reduced `F_i+D` interval is
`[(2i+2)f+b-1,(2i+3)f+b-1]`. It is below `g` for `i<k` and
meets `H` only at `u` when `i=k`. The `F_i+E_j` intervals occupy
the gaps between the `F` runs. The three high-high types reduce to

    D+D:     (h+4)f+[c-2,c],
    D+E_j:   (h+4+2j)f+[c-1,c],
    E_i+E_j: (h+4+2i+2j)f+c.

When these indices are at most `k`, they are precisely deleted holes.
For larger indices, they cannot collide with `D` or any `E`: their
`f`-coefficients are odd whereas those of the high entries are even,
and the remaining coordinate discrepancy has absolute value at most
two, strictly less than `f`. This argument is still valid when
`c>f`; it compares the same unnormalized coordinates instead of
assuming `0<=c<f`. These cases are exhaustive. The sole ordinary
`H+H` collision into `R` is indeed `u+u`.

The initial anchors are selected because the least two-anchor sum
exceeds `max F_k`. Seed-plus-anchor sums cover the intervening gaps.
After `F_k`, the seed-plus-`F_k` interval and the distinct self-sum
of `F_0` overlap or are adjacent exactly as needed when `b<=f-1`.
This includes `2g`, without using the forbidden pair `g+g`. After
`D` and the high singletons, disjoint `F_0+F_(j+1)` intervals cover
the gaps. The sole `R` collision is an unavailable initial diagonal,
so block zero is exactly `H`.

For all positive blocks, the identity

    min(F_k)+min(D[n-1]) = nm+u

excludes the next occurrence of `u`. At `n=1` the factors are in
disjoint initial runs; later they are in different blocks. Each is
smaller than the represented target. Under chronological induction
this simultaneously proves uniqueness of `u` and protects every
`R` entry. In particular, if two different occurrences of residue
`u` were proposed as a representation of a protected candidate, both
would be earlier actual integers, contradicting the established
uniqueness assertion. The argument does not discard equal residues
in different blocks by fiat.

The low-gap sums `F_i+B_k[n-1]` give

    I_i=[(2i-1)f+1,(2i+1)f-1],          0<=i<=k,

and `F_i+D[n-1]` give

    J_i=[(2i+2)f+b-1,(2i+3)f+b-1],      0<=i<=k-1.

Their union covers `[0,g-1]` except the selected seed residue `f`:
the `I_i` miss just the odd multiples `3f,5f,...,(2k-1)f`, which
are supplied by the `J_i`; the last `J_i` reaches `g-1`. At block
one the full initial `F_k` is used. The self-sum at `i=k` loses
the endpoints `(2k-1)f+1` and `(2k+1)f-1`. They belong to
`J_(k-2)` and `J_(k-1)`, respectively, with `b>=3` and `b<f`.
These are genuine distinct repairs even at the smallest allowed `k`.

Between `F` runs, the selected translate of `f` supplies the gaps.
After `F_k`, the additional interval `F_0+B_0[n]` reaches exactly
the point before `D`. The high gaps are supplied by `F_j+B_1[n]`,
where `B_1` is full. All these current-block summands precede the
target because their initial partners are positive. This completes
confinement and protection without presupposing a completed block.

Finally, `D+E_(i-2)[n-1]` excludes every `W_i[n]` for `n>=1`,
using distinct factors even in block zero. For `n>=2`, the two
different-block copies `D+D[n-1]` exclude all three points of `V[n]`.
In block one the two distinct initial `D` points represent only the
middle of `V`. Its endpoints have only the two forbidden diagonal
representations: the exhaustive classification excludes the other
categories and high-high pairs involving an `E` have larger index.
Thus the complete set is `H` in block zero, `R` plus those two
endpoints in block one, and exactly `R` thereafter. Eventual
periodicity is proved directly. The excluded `(k,b)=(2,3)` type
cannot be reinstated, since the low-gap convolution then loses an
endpoint of `F_k`.

## Inherited first-plateau arguments

The first-plateau decomposition covers `g=2f+j` with `f>=5` and
`ceil(f/2)+1<=j<=2f`. For the current upper theorem, only its
transition and band are indispensable inherited dependencies; the
interior also has the fresh argument above. I nevertheless reread
the wedge proof as requested. The endpoint `j=2f` corresponds to
`k=2,a=0` in the unique quotient notation, so it is not an upper
offset dependency here; its separate endpoint proof was not audited.

For the wedge `j+2<=f<=2j-2`, the tail runs are

    A=[j,f+1], B=[2f+j,2f+2j-1],
    C=[4f+j+1,4f+2j-1],
    D=[5f+3j-1,6f+2j-1],  M=7f+2j-1.

The exceptional actual entries are the interval
`I=[2f+2j,3f+j-1]`, `u=4f+j`, `v=4f+2j` and
`z=M+2f+2j`. The ten tail-pair and twelve exception-plus-tail
interval rows in [even/proof.md (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material)
were recomputed. Their gap containments use both sides of the wedge:
`A+A` starts above `A` because `2j>=f+2`; the crossing `v+B`
portion remains below `A` because `2j-f<=j-2`. Negative offsets
in crossing rows are high-gap portions, not nonexistent intervals.

All seven distinct exceptional-pair categories were checked as actual
sums. In particular `I+v` ends at offset `j` in block one, whose
`A` run begins at `j+1`; `u+z` is in the high gap of block one;
and `v+z=2M+(2j-f+1)` lies below `A_2` since
`3<=2j-f+1<=j-1`. The target `z` is not settled merely by tail
sum exclusion. Its two possible residue representations require
either the coordinate `j` in `A` or the lower endpoint of `D`.
Neither first occurs before block two, and either actual sum is
therefore too large to equal `z`. The earlier exceptional targets
`I,u,v` are safe by their initial positions and the least distinct
self-sum of the first full anchor.

Coverage also closes at both wedge edges. For the gap after `A`, the
`C_0` self-sum in block one, and `C_0+C_(n-1)` later, cover offsets
`[f+2,f+2j]`. The companion `B_0+D_(n-1)` interval ends at
`2f+j-1` and starts at `f+j-1`, `2j+1`, or `2j` according to
the block. Each start is at least `f+2` and at most `f+2j+1`.
Thus the intervals are contiguous. The other four gaps are covered
by the displayed anchor sums; their low-boundary carry ends at
`j` for block one and `j-1` later. Only the explicitly restricted
self-sums share a run; all other factors lie in disjoint actual
intervals. The common identification argument proves the full
membership table, hence a periodic tail from block two.

For the band `f<=j<=2f-1`, set `m=7f+2j-1`. The tail runs are

    [f,f+1], [2f+j,3f+j-2],
    [4f+j+1,5f+j-1], [6f+2j-2,6f+2j-1].

There are only two exceptional actual entries, `u=3f+j-1` and
`v=4f+j`, with `u+v=m`. The ten tail-pair and eight mixed-pair
rows in [lower/proof.md](../greedy-lower-20261018/lower/proof.md)
are safe modulo `m`. For example, `B+B` begins in the third gap
because `j>=f`, while the reduced `C+C` upper endpoint `3f-1`
stays in the first long gap for the same reason. Initial `u` is
below the least distinct sum and initial `v` lies beyond the end of
seed-plus-`B_0` but below every distinct `B_0` self-sum.

The critical initial coverage is the union of `f+C_0` and the
distinct self-sums of `B_0`. There is no hole exactly when
`4f+2j+1<=6f+j`, or `j<=2f-1`. The first later long gap uses
the distinct `C_0` self-sum, ending at `3f-2`, together with
`B_0+D_0`, beginning at `f+j-1`; these intervals still touch at
the upper boundary `j=2f-1`. Subsequent blocks use disjoint copies,
so the first upper endpoint is instead `3f-1`. The remaining gap
unions were recomputed as displayed. Consequently the exact band
table has its fixed tail already in block one. Continuing this
unchanged table to `j=2f` would leave `8f` uncovered, so the upper
edge is a mathematical restriction, not an arbitrary cutoff.

At the transition `j=f-1`, the eventual four runs modulo `m=9f-3`
are

    [f-1,f+1], [3f-1,4f-3],
    [5f,6f-3], [8f-4,8f-3].

The initial exceptional entries are `u=4f-2`, `v=5f-1` and
`w=6f-2`; the first positive block omits only the lower endpoint
`f-1` of `A`. The ten tail-pair and twelve mixed-pair rows again
miss the tail, now using `f>=5`. Of the three distinct exceptional
sums, `u+v=m`, `u+w=m+f-1`, and `v+w=m+2f`, the middle sum
is safe precisely because that first `A` lower endpoint is absent.
For the exceptional target `w`, the only possible residue hits are
the lower endpoint of `B+B`, requiring a repeated `3f-1`, or
`v+A` using residue `f-1`, whose first occurrence is in block two.
Neither is a valid earlier distinct representation.

The block-one low gap is `[0,f-1]`, as opposed to `[0,f-2]` in
later blocks. The displayed `B_0+C_0` carry fills exactly this
larger required portion. The block-one `C_0` self-sum fills
`[f+2,3f-2]` without losing any claimed endpoint; the `v+D_0`
and `B_0+A_1` union overlaps at `4f-1` and fills the next gap.
The later disjoint-copy rows give the smaller low gap and all
remaining gaps exactly. This establishes the transition table and
its periodicity from block two. No phase or least-preperiod claim
is needed for this conclusion.

## Odd multiples: reflection is valid and the coverage is causal

For `f>=5`, `k>=1`, `g=(2k+1)f`, the proof at
[odd-multiple-proof.md](../greedy-unified-20261018/odd-multiple-proof.md)
uses `m=(6k+3)f-1` and odd `f`-cells
`(2i+1)f+H_i`, `0<=i<=3k`. The coordinate intervals, in order,
are singleton `0` for `i<=k-2`, then `[0,1]`, `[0,f-2]`, full
`[0,f-1]` for `k+1<=i<=2k-1`, then `[1,f-1]`, `[f-2,f-1]`,
and singleton `f-1` thereafter. Empty ranges vanish at `k=1`.
They satisfy `H_(3k-i)=f-1-H_i`, hence `m-R=R`.

For an unwrapped `R+R` sum, only a coordinate carry can reach an
odd cell. If an input index is at most `k-2`, its coordinate is zero,
so no carry occurs. If one input index is `k-1`, a carry has
coordinate zero and lands at index at least `2k+1`, which excludes
zero. If both input indices are at least `k`, the target index is
at least `2k+1`. At equality both inputs are `k`, so the carried
coordinate is at most `f-4`, below `[f-2,f-1]`; at larger indices
it is at most `f-2`, below the selected singleton `f-1`.

For a wrapped putative hit `x+y-m=r in R`, reflection gives
`(m-x)+(m-y)=m-r in R`, an unwrapped sum of two members of `R`.
This is precisely the case already excluded. If `x+y=m`, the
residue is zero and is absent. This justifies the reflection step
without assuming that the original summands were in the same block.

The initial extras are `u=(2k+2)f-1` and `v=(4k+1)f`.
The mixed carry cases in the proof were checked. For `u+R`, the
uncarried cell is even and a carry has coordinate `r-1`; the few
possible odd target cells have lower coordinates `1`, `f-2`, or
`f-1` exceeding that coordinate. Once the sum wraps, its reduced
cell is even. For `v+R`, unwrapped sums are even-cell sums; a
wrapped odd cell has coordinate `r+1`, too large for the successive
target coordinate sets `{0}`, `[0,1]`, or `[0,f-2]`. A carry from
`r=f-1` again makes the target cell even. The sole distinct
extra pair is `u+v=m`, which is absent. Initial `u` is below the
least distinct sum, while initial `v` is beyond all available
seed-plus-anchor sums and below all two-anchor sums. Thus the
proposed full set has no forbidden sum.

The covering identities address every gap, including `k=1` where
some groups disappear. In particular, the gap after the short run
`A_*=[(2k-1)f,(2k-1)f+1]` is supplied by `F_k+B_k[n-1]` in
later blocks. In block one, the restricted `F_k` self-sum stops
one integer earlier; `F_0+e`, with `e=m-f` an actual initial high
entry, supplies `[2kf,(2k+1)f-1]` and repairs that endpoint.
The exceptional later offsets `u` and `v` in the long gaps are
covered respectively by `v+D[n-1]` and `F_0+A_*[n]`. The first uses
the actual initial `v`, and the second uses the proposed tail run
`A_*`; neither assumes that a later translate of `v` is selected.
At `k=1` they lie in the same gap and the intervals still cover it.

At the high end, the only point not reached immediately by the
listed anchor-plus-tail intervals is `(6k+2)f`; it is represented
by `v+B_0[n]`. The next interval `F_0+B_k[n]` starts one integer
later and extends into the next low gap. All factors are disjoint
actual intervals except the stated restricted self-sum. Positivity
therefore proves the proposed set equals the greedy sequence.
Its entire positive-block tail is `R`, so eventual periodicity
follows without an experimental continuation claim.

## Citation-ready chronological induction for the two envelope proofs

The propositions in this section isolate the infinite induction from
the finite interval calculations above. They use those explicit
collision and coverage identities as proved lemmas; they do not use
diagnostics or a finite-block continuation theorem. This is a
replacement presentation of the identification step, without changing
either residue formula.

### Proposition U1: confinement followed by finite extinction

For the upper-interior parameters and sets defined above, the actual
strict greedy sequence has characteristic set `R` in every block
`n>=6k-3`.

**Proof.** Let

    P = {iQ+f : 0<=i<k} union {(k-1)Q+f+1}
        union all B_i union C union {max D_i : 0<=i<k}.

This is the protected part of `R`; in particular it includes the
residue `f`. We first prove three simultaneous assertions for every
actual integer `x>=m`: each selected integer below `x` has residue
in `H`; each point of `nm+P` below `x`, for `n>=1`, is selected;
and every selected integer below `x` congruent to `u` or `v` modulo
`m` equals the respective initial integer `u` or `v`.

The initial-block computation already proved confinement below `m`,
the presence of the fixed anchors `F_i`, the initial entries `u,v`,
and all of `B_i,C,max D_i` in block zero. These are exactly the
initial entries needed by the later coverage identities. No missing
early `A` entry is included in the base assertion about `P`.

Suppose the three assertions hold strictly below `x=nm+r`, where
`n>=1` and `0<=r<m`. If `r in P`, an admissible representation
of `x` must use two smaller selected integers, hence two residues
in `H`. The compatibility lemma excludes a representation having
an input residue in `R`. For two extra strips, the only target
portions in `R` are below the protected upper endpoints of `A`
and `D`. An initial `v` plus an extra strip can hit only an `A`
lower endpoint, which is not in `P` because `a<=f-2`. The only
remaining protected-residue collision is the `u+u` class. By the
induction hypothesis the only earlier selected occurrence of that
residue is the one actual integer `u`, so two distinct earlier
summands in that class do not exist. The other exceptional-pair
types miss `R`. Thus `x` is selected.

If `r=u`, the fixed `max F_0` and the point
`nm+max A_(k-1)` sum to `x`. The latter has protected residue and
is smaller than `x`; both summands are therefore already selected.
They are distinct because one is initial and the other is in a
positive block. If `r=v`, the fixed seed `g` and `nm+min B_0`
give the same conclusion. Thus neither exceptional residue has a
second occurrence.

If `r outside H`, choose a representation in the explicit coverage
table of the upper-interior proof. Every summand is either a fixed
initial anchor/exception or a protected entry of the current or
preceding block. In the latter case it is a positive summand of
`x`, so it is strictly smaller than `x`. If that block is zero,
the required `B,C,D` endpoint is in the established initial set;
otherwise the induction hypothesis applies. The sole possible
initial overlap was the shared lower endpoint of
`F_(k-1),B_(k-1)[0]`. Its missing sum lies outside the block when
`k=2`, or is supplied by `u+B_(k-2)[0]` when `k>=3`. Thus the
chosen representation is always a distinct actual pair, and `x`
is excluded. Finally, if `r in H` is not among these cases, either
greedy decision preserves all three assertions. This exhausts the
candidate integer and proves the simultaneous induction.

Now write `E_i[n]` for the actual selected part of extra strip `i`
in block `n`. The collision classification and uniqueness just
proved imply that an absent `A_l[n]` entry, `n>=1`, can only be
caused by an extra-strip pair with `i+j=k+l`, `q+r=n-1`, or by
the initial `v` and the top entry of `E_l[n-1]`. The former case
has both indices greater than `l`. For `l=k-1` it is impossible.
Hence that `A` run without its lower endpoint is full in every
positive block. Its sum with `F_0` excludes the top of its extra
strip; because `f+a-1>2a`, this conclusion holds even if the
lowest extra survives. The next block has full `A_(k-1)`, and
its sum with `F_0` then excludes the entire strip. Thus the claim
holds for `l=k-1` from block `T_(k-1)=2`.

Descending induction gives the same conclusion for every `l` from
`T_l=3(k-l)-1`: if the higher-index strips are empty from their
respective `T_i`, an extra pair can obstruct only a block with
`n-1<=T_i+T_j-2=3(k-l)-4`. At block `T_l-1` and thereafter
only the lower `A_l` endpoint could still be missing. Adding
`F_0` removes the top extra, and one block later the lower endpoint
is also present. This proves the induction on `l`.

Finally an absent `D_l[n]` entry can only come from two extras
with `i+j=l` and `q+r=n`. Their latest possible target block is
`T_i+T_j-2=6k-3l-4`. All `D_l` are consequently full by block
`6k-3`; all `A,B,C` are full, all strips are empty, and later
`u,v` are absent there. Confinement leaves exactly `R`, which
is nonempty. This proves the proposition. QED.

### Proposition U2: a fixed tail without exact transient assumptions

For the high-plateau parameters and sets defined above, the actual
strict greedy sequence has characteristic set `R` in every block
`n>=2`.

**Proof.** The initial interval computation proves that block zero
is exactly `H`, in particular that every initial anchor and every
initial entry of `R` is available. For `x>=m`, induct on the actual
integer `x` with these simultaneous assertions below `x`: selected
residues are in `H`; every point with residue in `R` in a positive
block is selected; and no second occurrence of residue `u` is
selected.

If `x` has residue in `R`, any representation by earlier selected
integers would be a collision of two envelope residues into `R`.
The exhaustive algebraic classification leaves only `u+u`.
The induction hypothesis supplies only one earlier actual occurrence
of that residue, so it cannot form a distinct pair. Therefore `x`
is selected. If `x=nm+u`, the identity

    min F_k + min(D[n-1]) = x

uses earlier selected entries. The initial `F_k` is always available;
`D[n-1]` is in the initial set when `n=1`, and is protected in a
positive block otherwise. Both summands are positive and less than
`x`. They are distinct in the first case because the runs are
disjoint, and in the other cases because the blocks differ.
Thus `x` is excluded.

If the residue of `x` is outside `H`, the low, middle and high
coverage identities produce a pair from initial anchors and `R`
entries in the preceding or current block. Such an `R` entry is
again smaller than `x` and already selected. The ordinary low-gap
convolution holds because `B_k` has both endpoints of `F_k` and
its hole is shorter than the fixed anchor length. In block one the
full `F_k` is used. The self-sum at the last low interval loses
only its two extreme values, each repaired by the stated `F+D`
sum. Every resulting pair consists of distinct actual integers.
Hence `x` is excluded. A greedy decision at any other residue in
`H` cannot violate the three assertions. This proves them for
every candidate, with no assumption about an entire unprocessed
block.

Only the holes `W_i` and `V` remain as possible additional selected
residues. For every `n>=1`, `D+E_(i-2)[n-1]` fills `W_i[n]`
with distinct protected entries. For every `n>=2`,
`D+D[n-1]` fills `V[n]`; its summands lie in different blocks
and are distinct. Both identities use only smaller positive
summands. Thus for `n>=2` the protected `R` entries are all
selected, all extras are excluded, and confinement forbids any
other residue. The nonempty word is exactly `R`. This proves
eventual periodicity without deciding which endpoints of `V[1]`
are selected, and without using a least-transient claim. QED.

## Integration, remaining obligations and provenance

For `g>=2f`, the representation `g=2kf+a`, `k>=1`, `0<=a<2f`
is unique. Within the upper offsets, the analytic interior ends at
`f-2`; the successive lines `f-1,f,f+1,f+2` are separate cases;
and the high plateau begins at `f+3`. The first-quotient transition
and band apply exactly where claimed. At `f=5` the interior is
empty, but these explicit boundary and plateau categories still
partition the upper offsets. The plateau substitution `b=a-f`
changes `(6k+3)f+2b-1` to `(6k+1)f+2a-1`; the odd-multiple
case has the same expression at `a=f`. Thus the analytic
membership results use the modulus claimed by the integration
document. This partition check does not prove the certificate-only
rows whose existence is listed there.

The original source by Daan van Berkel and Wieb Bosma,
[*Periodicity conjectures for all 2-sumfree sequences*, v1](https://arxiv.org/html/2609.18522v1),
was reopened for Definition 3 and Theorems 12 and 14. Its low-gap
and diagonal results have the assumptions used by the integration
document. This audit does not claim to re-prove those source
theorems or establish novelty; the new source-derived prose here
is a limited statement-alignment check. The membership proposals
and interval calculations above are credited to the parent and
delegated contributors in their preserved files. Prior same-team
checks are not counted as independent evidence for this rereading.

No failed step was concealed by a larger finite test. The known
failure boundaries `a=f-1` in the interior extinction argument,
`(k,b)=(2,3)` in the high-plateau convolution, and `j=2f` in the
band table remain excluded from those particular arguments. The
combined theorem relies on different proofs there. This audit
finds those restrictions logically necessary and correctly retained.

Resource use consisted of text reads, source retrieval and hashing.
No numerical experiment, subprocess research computation, package
installation or certificate-writing command was run. Model compute,
uninstrumented process CPU and peak memory are unknown. The allocated
research-computation ceiling was 300 process CPU seconds and expected
memory below 1 GiB; no empirical peak-memory claim is made.

Actual service-supplied model identity, version and configuration were
unavailable and remain unknown. The parent and this Codex worker
supplied the mathematical assessment and audit prose. This must be
covered by the batch's single assistance note and final-version check
report. Human full-text screening and manual submission remain pending;
no approval state is assigned. Original prose follows CC BY 4.0 under
the repository terms. The sealed files were not edited.

Checked: the eight SHA-bound files above, their exact target ranges,
all stated sum categories in the analytic arguments, the actual
distinctness repairs, block shifts, exceptional targets and induction
dependencies. Action: save this new local audit for human handoff.
Results: no unresolved gap in the audited eventual-periodicity
arguments; no source-file correction required. Limits: certificate-only
branches, other first-seed ranges, comprehensive optimal-period and
preperiod checking, independent scientific review and novelty assessment
are outside this audit. Outcome: local review draft; the total theorem
cannot be certified from this scoped finding alone.
