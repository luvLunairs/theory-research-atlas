> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Three fixed first-seed-four cases by global lifetime identities

18 October 2026. Proposed finite arithmetic proofs of infinite sets,
pending full-text human review and manual submission. These arguments
use explicit residue-lifetime identities in the linked appendix. They do
not use a computed prefix, observed repetition, or a continuation checker
as a premise. They are not a new uniform theorem in the second seed.

## Statements and candidate sets

The strict greedy sequences with seeds `(4,24)`, `(4,32)` and `(4,40)`
are ultimately periodic. The following sufficient characteristic periods
and starts follow from the proof:

| Second seed g | Working block size m | Sufficient period | Sufficient start |
| --- | --- | --- | --- |
| 24 | 67 | 67 | 603 |
| 32 | 91 | 91 | 637 |
| 40 | 115 | 23 | 1035 |

No minimum-start or least-period assertion is required. The working
block size is `m=3g-5` in all three cases. For the last case, the
larger block size `115=5*23` makes the transients substantially simpler
than blocks of length 23. The final residue word explicitly splits
into five identical pieces, so period 23 follows as well.

For each case, the selected-lifetime table in the
[complete arithmetic appendix](f4-fixed-tables.md) defines a set
`L_r` of nonnegative integer block indices for each residue `0<=r<m`.
Unlisted residues have empty lifetime. Define the proposed infinite set

    T={nm+r : 0<=r<m and n in L_r}.                       (1)

All lifetimes are intervals, rays, or the one explicitly stated union
`L_40={0} union [9,infinity)` in the `g=40` case. The tables are the
literal definitions of the candidates, so (1) does not depend on a
program evaluating or reconstructing the sequence. The only elements
at or below the second seed are the two prescribed seeds, and all
elements are positive. This follows directly by reading the lifetimes
of the residues at most `g`.

## The elementary strict lifetime operation

For two different residues `a<b`, every pair of their actual entries
is distinct. Write `a+b=r+cm`, where `0<=r<m` and `c` is zero or one.
The exact lifetime of their sums at residue `r` is

    (L_a+L_b)+c.                                         (2)

Interval lifetimes add by `[l,u]+[p,q]=[l+p,u+q]`, allowing an
infinite upper endpoint; disjoint unions distribute over this identity.
Thus (2) is an equality of infinite sets, not merely a list of sample
representations.

When the two residues are equal, different actual integers require
different block indices. For an interval lifetime `[l,u]`, the exact
strict self-sum is

    [l,u] dotplus [l,u]=[2l+1,2u-1],                     (3)

with empty right side for a singleton interval and upper endpoint
infinite for a ray. To see that there is no missing integer, if
`2l+1<=t<=l+u`, use `l+(t-l)`; if `l+u<t<=2u-1`, use
`u+(t-u)`. The two entries are distinct in both cases. For a ray only
the first construction is needed. For a union of disjoint intervals,
apply (3) separately inside each component and use ordinary interval
addition between two different components. Add the carry `c` afterwards.

In particular the only disconnected lifetime in our candidates obeys

    ({0} union [9,infinity)) dotplus
    ({0} union [9,infinity)) = [9,infinity),             (4)

because the cross-component sums already give `[9,infinity)` and the
within-ray strict sums start at 19. The forbidden `0+0` contributes
nothing. All remaining strict sums in the appendix use (3) directly.

These are singleton-residue instances of the parent
[lifetime lemma](../lifetime-lemma.md); the argument has been written
out here to expose the exact distinctness condition.

## Exclusion of every selected integer

Let `H={r:L_r is nonempty}`. The appendix's exclusion table gives,
for every `r in H`, **all** unordered pairs `a<=b` in `H` such that
`a+b` is congruent to `r` modulo `m`. This is a short finite addition
table at each supported residue: a possible partner of `a` is uniquely
`r-a` or `r+m-a`, when it lies in `H` and is at least `a`. The table
includes diagonals even when (3) makes their lifetime empty. Thus no
distinct-residue pair or different-block diagonal is suppressed.

The last column is the union of (2) or (3) over those displayed pairs.
Every such union is disjoint from `L_r`. This proves that no selected
integer is a sum of two distinct selected integers. To illustrate the
arithmetic, the row `g=24,r=10` has exactly the source pairs `34:43`
and `35:42`, both with carry one. They give

    ([0,6]+[0,1])+1 = [1,8],
    ({0}+{0})+1 = {1}.

Their union is `[1,8]`, disjoint from `L_10=[9,infinity)`.
The diagonal in the `g=24,r=48` row is `24:24`, but `L_24={0}`,
so its strict sum is empty. This is why the actual number `24+24`
does not forbid the initially selected 48.

The disconnected case is also explicit. For `g=40,r=80`, the only
sources are `17:63`, `40:40` and `86:109`. They respectively give

    [5,infinity)+[6,infinity) = [11,infinity),
    L_40 dotplus L_40        = [9,infinity),
    [0,infinity)+[7,infinity)+1 = [8,infinity).

Their union is `[8,infinity)`, exactly after `L_80=[0,7]`.
Conversely, the sole source for residue 40 is `75:80`, with carry one:
`{0}+[0,7]+1=[1,8]`. This is disjoint from its initial seed occurrence
and its later ray `[9,infinity)`. It explains the disappearance and
return of that seed residue without assuming future choices.

All other exclusion rows are the same interval operations with their
numbers displayed. There are respectively 42, 106 and 205 listed pairs
in the three complete supported-target tables. This finite arithmetic
burden is explicit; a claim that a program passed is not substituted
for the identities. The tables and operations together constitute the
written exclusion argument and can be checked without running code.

## Coverage of every omitted candidate

For each supported residue, the same exact sum-lifetime column also
covers every omitted block index whose actual integer exceeds `g`.
When `r>g`, this means every omitted `n>=0`; when `r<=g`, it means
every omitted `n>=1`. There is no obligation to represent the forced
omissions below the second seed.

The appendix's final table for each case addresses **every** residue
outside `H`. A row lists one or two source pairs and the exact sum
lifetime supplied by each pair. Their union includes `[0,infinity)`
for `r>g`, or `[1,infinity)` for `r<=g`. Every source lifetime is
specified in the selected table. For example, at `g=32,r=66`,

    32:34 supplies {0}+[0,5]=[0,5],
    10:56 supplies [6,infinity)+[0,infinity)=[6,infinity).

The adjacent intervals cover every nonnegative block. At
`g=40,r=44`, the initial seed residue and its later return require
the two witnesses

    4:40 supplies [0,4] union [9,infinity),
    3:41 supplies [3,infinity),

whose union is again all nonnegative blocks. For the low residue zero
in the same case, `41:74` has carry one and supplies
`[0,infinity)+{0}+1=[1,infinity)`, exactly the required range.

The last tables contain respectively 50, 71 and 87 source pairs.
They never use an equal-residue pair; distinctness is therefore
automatic, even if the two block indices coincide. All selected-target
diagonals were handled separately by (3). Thus exclusion and coverage
have accounted for every actual integer above the second seed.

Since every summand is positive, a representation of an integer uses
smaller integers. Induction on the scanned integer now identifies the
candidate (1) with the strict greedy sequence. This argument works
directly for all nonnegative block indices; no finite-prefix extension
criterion is involved.

## The periodic tails

For `g=24`, every finite lifetime ends before block 9 and every ray
has begun by block 9. For `g=32`, the corresponding block is 7.
For `g=40`, it is 9. Consequently the sets (1) have a fixed residue
word from `9*67=603`, `7*91=637`, and `9*115=1035`, respectively.

In the last case the eventual residue set is exactly

    union_(j=0)^4 (23j+{2,3,10,17,18}).                  (5)

Equation (5) follows by listing the residues with ray lifetimes in its
table. It makes period 23, rather than merely 115, valid after 1035.
This establishes all the stated eventual-periodicity conclusions. QED.

## Evidence, actual limitations and provenance

The preserved [first-seed-four finite record (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material)
suggested the periods 67, 91 and 23 and earlier sufficient starts.
Those earlier computations and continuation certificates are not used
as proof premises here. Bounded arithmetic with exactly these three
seeds suggested the lifetime tables. Changing the working modulus from
23 to 115 in the last case compressed its apparently irregular
42-block transient into the stated interval lifetimes. No additional
seed census was performed.

The [discovery helper (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) and
[retained discovery output (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) preserve that
exploration; its primitive-modulus description for `g=40` was lengthy
and was not suitable for the present written proof. The separate
[literal-model helper (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) rechecks the displayed
interval identities and formats the appendix. The
[actual report (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) binds its code and output.
The first execution of that helper had a Python tuple-closing syntax
error; it stopped before checking identities, and was corrected.
No failed mathematical identity was suppressed.

This is a complete proposed finite arithmetic argument for three fixed
seed pairs. It does not provide a new uniform formula in `g`, and the
353 supported-target pair identities plus 208 gap witnesses remain a
substantial explicit reading obligation. The tables were prepared with
AI and bounded arithmetic, so full human screening must include them,
the main argument and supporting material. A reader who has not checked
the table arithmetic cannot replace that obligation with the program's
success message. Independent mathematical review, formal verification,
least-period and optimal-transient claims, and historical novelty remain
outside this proof's completed checks.

The underlying problem and period predictions are due to Daan van
Berkel and Wieb Bosma,
[*Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1),
Definition 3 and Conjecture 5. The parent supplied the fixed-boundary
target, and the current worker supplied the modulus compression,
literal lifetimes and arithmetic presentation. These are substantive
same-team AI contributions. Actual service-supplied model identity,
version and configuration are unknown. No human screening, independent
verification, approval, publication or submission is claimed. Original
prose/data use CC BY 4.0 and code MIT under the repository terms.
