> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# An analytic proof for the two rays above odd multiples

18 October 2026. Local scientific draft requiring full-text human review
and manual submission. This argument replaces the program-certificate
dependency for the [preserved ray proposal (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material),
and enlarges its first-seed domain. It is same-team AI-assisted research,
not independent verification, approval or a novelty claim.

## Statement and scope

For every integer `f>=3`, `k>=2` and `b in {1,2}`, put

    h=2k+1,       c=2b-1,
    g=hf+b,      m=3hf+c.

The strict greedy sequence with seeds `f,g` is `m`-periodic in
every block with index `n>=3`. The residue set is explicitly
described below. This proves eventual periodicity for the two
unbounded quotient families. No least-period or exact-transient
assertion is needed.

The source predicts the gap counts in [Definition 3(4) and Conjecture 5
of van Berkel and Bosma](https://arxiv.org/html/2609.18522v1).
The initial formula was already preserved for `f>=5`. The proof here
also covers `f=3,4`, by checking the inequalities used in the argument;
the extension is not inferred from a finite table match.

All intervals are inclusive integer intervals. Define

    F_i=[(h+2i)f+b,(h+2i+1)f+b-1],       0<=i<=k,
    D=[(2h+2)f+c-1,(2h+2)f+c],
    E_j={(2h+2+2j)f+c},                 1<=j<k,
    A_l={(2l+1)f+b},                    1<=l<k,
    u=max F_0=(h+1)f+b-1.

For `2<=i<=k`, let the bottom strip of `F_i` be

    X_i=(h+2i)f+[b,2b-1].

It has exactly `b` entries. Set

    B_0=F_0 minus {u},       B_1=F_1,
    B_i=F_i minus X_i       (2<=i<=k),
    R={f} union all A_l union all B_i union D union all E_j,
    H=R union {u} union all X_i.

Since `f>b`, every `B_i` is nonempty. The runs, strips and
singletons lie in `[0,m)` as stated and are disjoint; in particular
all `A_l` lie strictly between `f` and `g`. Coordinates such as
`2b` or `c` are not assumed smaller than `f`. That point matters
at `f=3,b=2` and is handled by the coefficient comparisons below.

## Complete envelope collisions

The only ways an ordinary pair of envelope residues can meet `R`
are:

1. `u+u=min D`.
2. A pair from `X_i,X_j` can meet `A_l` only if
   `i+j=k+l+1`. Writing their coordinates within the bottom
   strips as `b+e,b+e'`, it must satisfy `e+e'=b-1`.
   Its raw sum is `m+A_l`.

Here the second line has `i,j>=l+1>=2`. Thus both inputs are
extras, not protected tail entries. We now prove that these are
all the collisions, including the small-first-seed boundaries.

First omit the `A_l` and consider

    H_0={f} union all F_i union D union all E_j.

Seed-plus-`F_i` sums lie exactly in the following gaps. Seed-plus-
high-entry sums lie in high gaps, with `f+E_(k-1)=m`.
The value `2f` is below `g` and differs from the seed and every
`A_l`.

For `s=i+j`, ordinary `F_i+F_j` sums form

    [(2h+2s)f+2b,(2h+2s+2)f+2b-2].                   (2)

They are above the last `F` run. They miss each high singleton
by one at the relevant endpoint. Their only `D` intersection
is the lower endpoint of `D`, attained at the upper endpoint
of `F_0+F_0`, so both entries must equal `u`. After subtracting
`m`, any remaining portion is below `g`, in

    [(2s-h)f+1,(2s-h+2)f-1].                          (3)

The seed residue `f` is missed: at `s=k` this interval ends
at `f-1`, and at `s=k+1` it starts at `f+1`.
For an `A_l` hit, the only possible index sum is
`s=k+l+1`. Comparing its actual offset `b` with the summand
offsets in (2) gives exactly `e+e'=b-1`. Consequently the
summands are both in the corresponding bottom strips. This
derives both the residue target and its one-block carry.

The reduced `F_i+D` interval is

    [(2i+2)f+b-1,(2i+3)f+b-1].                       (4)

For `i<k` it lies below `g`; it stops one integer before any
next `A_l` and starts after the preceding one. For `i=k` it
meets the envelope only at the removed `u`. Likewise

    (F_i+E_j)-m=[2(i+j+1)f+b,(2(i+j+1)+1)f+b-1]      (5)

is either a low gap or a gap between full `F` runs. Its upper
endpoint is one below a possible low `A` entry or the next
full `F` lower endpoint. These inequalities need only `f>b`.

The remaining high-high sums wrap exactly once and have forms

    (D+D)-m       =(h+4)f+[2b-3,2b-1],
    (D+E_j)-m     =(h+4+2j)f+[2b-2,2b-1],
    (E_i+E_j)-m   =(h+4+2i+2j)f+2b-1.                (6)

Where they reach a full `F` run, their intersection is contained
in its removed bottom strip. Indeed the target run has index at
least two and starts at coordinate `b`, while every coordinate
in (6) is at most `2b-1`. A coordinate below `b` is in the
preceding gap, since `f>b`. If their run index is larger than
`k`, they lie beyond all `F` runs and cannot hit `D` or `E`:
the `f`-coefficients are odd instead of even, and their coordinate
difference from a high entry has absolute value at most two,
strictly less than `f>=3`. This is an unnormalized comparison;
it remains valid when `c=f` at `f=3,b=2`.

It remains to check pairs involving a low singleton `A_l`.
The seed plus `A_l` is a low even-cell point below `g` and
cannot be another `A` point. A pair `A_l+A_t` has even
coefficient and coordinate `2b`. It misses high even-cell
entries, whose coordinates are `2b-2` or `2b-1`; changing
an even coefficient costs at least `2f`. It misses an adjacent
odd `F` or `A` cell too: the next cell's lowest possible
coordinate in this representation is at least `f+b>2b`,
and the preceding `F` cell ends at coordinate `b-1<2b`.
All these sums are below `m`.

The sum `A_l+F_j` has even coefficient
`2(k+l+j+1)` and coordinates `[2b,f+2b-1]`. In the next
odd `F` cell its index would be `t=l+j+1>=2`, whose
protected part starts at coordinate `2b`; in the present
even-cell coordinates that start is `f+2b`, one above the
sum interval's endpoint. The preceding `F` cell ends at
coordinate `b-1`, below the sum interval. More distant
odd cells cannot meet it because `f>b`. High `D/E` entries
at the same even coefficient have coordinates at most
`2b-1`, below the sum interval; the next even coefficient
already lies above it. Thus these sums may remove bottom
strip entries but cannot hit `R`. Their actual maximum is
below the last high singleton, so they do not wrap.

For `A_l+D`, the raw coefficient is `4k+2l+5` and the
coordinates are `[3b-2,3b-1]`. Below `m` this lies above
the full `F` region and above `D`. Relative to any `E`,
its coordinate difference is `b-1` or `b`, smaller than
`f`, whereas its coefficient has opposite parity. Thus it
misses every high entry. Wrapping occurs only at `l=k-1`
and gives `[b-1,b]`, below the seed `f`.

For `A_l+E_j`, the raw coefficient is `4k+2l+2j+5`
and coordinate `3b-1`. Before wrapping it misses the high
entries by the same parity comparison, with coordinate
difference `b<f` from an `E`; it is already above `D`.
After wrapping it is

    2(l+j-k+1)f+b.

If this is nonnegative, it is below `g`, is not the seed,
and its even coefficient prevents equality with a low
`A` singleton. There is no second wrap. This completes
all pair categories and proves the collision classification.

## Initial anchors and the protected core

Every `F_i` in block zero is selected. Before the end of `F_k`,
seed-plus-anchor sums cover all intervening gaps, while the
least two-anchor sum is already larger than `max F_k`.
The initial block has no low `A_l`, since they are below the
second seed `g`.

The gap after `F_k` and before `D` is covered by the union of

    f+F_k=[2hf+b,(2h+1)f+b-1],
    F_0 dotplus F_0=[2hf+2b+1,(2h+2)f+2b-3].          (7)

The intervals overlap or are adjacent because `b+1<=f`.
In particular the unavailable diagonal `g+g` leaves no gap:
the seed-plus-anchor interval covers `2g`. After `D` and
each high singleton, the disjoint anchor sums

    F_0+F_(j+1)
      =[(2h+2+2j)f+2b,(2h+4+2j)f+2b-2],  0<=j<k,  (8)

cover the respective gaps, extending through the block end.
The only possible collision with `D` or `E` is the repeated
initial `u+u`, which is inadmissible. Therefore block zero
is exactly `H_0`.

Let the protected core be

    P=R minus union_l A_l={f} union all B_i union D union all E_j.

We prove simultaneously, by induction on the actual integer,
that all selected residues lie in `H`, every positive-block
entry of `P` is selected, and `u` has only its initial occurrence.
Suppose these assertions hold at smaller integers. A candidate
with residue in `P` could be represented only by the collision
class `u+u`; the other classified collisions target `A` entries.
The induction hypothesis permits only the one initial actual
`u`, so a distinct pair is impossible. Thus the core candidate
is selected. A later `u[n]` is excluded by

    min F_k + min(D[n-1]) = nm+u,                       (9)

where `X[n]=nm+X`. At `n=1` the factors are disjoint initial
runs; later they are in different blocks. The `D` summand is
protected and positive, hence earlier than its represented
target. This proves uniqueness causally rather than assuming
it in order to protect a completed block.

## Complete coverage outside the envelope

We now give the witnesses completing that same chronological
induction. All ranges are offsets relative to `nm`, with `n>=1`.

For `n>=2`, the following low sums are available:

    F_0+B_k[n-1]: [-f+b+1,f-1],
    F_k+B_1[n-1]: [f+1,3f-1],
    F_k+B_i[n-1]: [(2i-1)f+b+1,(2i+1)f-1],  2<=i<=k,
    F_i+D[n-1]: [(2i+2)f+b-1,(2i+3)f+b-1],  0<=i<k. (10)

The first covers `[0,f-1]` because `f>b`. The second
covers the integers immediately after the seed residue.
Between two subsequent long intervals, the last row ends at
`A_l-1` and the next long interval begins at `A_l+1`.
They therefore cover precisely the low gaps while leaving
the envelope singleton `A_l`. The last `D` sum also covers
the range from `(2k+1)f` through `g-1`. These intervals
overlap where necessary since `b-1<f`.

For `n=1` use the full initial `F_i` in place of `B_i[0]`.
Every such pair is disjoint except the case `F_k+F_k`.
Its strict sum interval is

    [(2k-1)f+2,(2k+1)f-2]

in block-one offsets. The lost last endpoint `(2k+1)f-1`
is covered by `F_(k-1)+D`. The lost first endpoint
`(2k-1)f+1` is covered by `F_(k-2)+D` when `b=2`;
when `b=1` it is exactly the permitted envelope singleton
`A_(k-1)`, so it need not be covered to prove confinement.
All other low ranges in (10) are enlarged by using full
initial intervals and remain sufficient. The `F+D` factors
are disjoint even at `k=2`.

Between full `F` runs use the protected translate `nm+f`
and the fixed initial `F_i`. After the last full `F` run,
combine that seed-plus-anchor sum with

    F_0+B_0[n]
      =nm+[2hf+2b,(2h+2)f+2b-3].                     (11)

Their union ends exactly before `D` and has no hole because
`f>b`. The high gaps are supplied by `F_j+B_1[n]`,
`0<=j<k`, giving exactly (8) in the current block. They
are distinct because the factors lie in different blocks.

This is the full complement of `H`: low gaps, gaps between
the full anchors, the gap before `D`, and all high gaps.
Every witness uses fixed initial entries or protected core
entries of the preceding or current block. As positive
summands, they precede their target. The actual-integer
induction therefore establishes confinement, core protection
and uniqueness of `u` for all time. It leaves the low `A`
entries and bottom strips undecided when appropriate.

## The remaining defects disappear in two stages

For `i>=3`, the identity `D+E_(i-2)[n-1]` has coordinates
`[2b-2,2b-1]` in `F_i[n]`. For `b=1` it covers the
single bottom entry; for `b=2` it covers both. Thus

    X_i[n] is empty for every i>=3 and n>=1.             (12)

For `n>=2`, the different-block sum `D+D[n-1]` has
coordinates `[2b-3,2b-1]` in `F_2[n]`, covering its
entire bottom strip. Hence `X_2[n]` is empty for `n>=2`.
In block one, that strip has at most one selected entry:
it has size one when `b=1`; when `b=2`, the distinct sum
of the two initial `D` entries removes its lower point,
leaving at most its upper point. We do not assume the
remaining point is selected.

Consider a missing `A_l[n]` in a positive block. By the
complete collision classification, its only possible
representation consists of entries in `X_i[q],X_j[r]`
with

    i+j=k+l+1,             q+r=n-1.                    (13)

For `n>=4`, (12) and extinction of `X_2` after block one
make this impossible: both block indices would be at most
one, so their sum could not exceed two. At `n=3`, both
must equal one and both strips must be `X_2`. But
`X_2[1]` has at most one actual selected entry, so this
would repeat a summand. Thus every `A_l[n]` is selected
for all `n>=3`.

At those blocks the protected core is full, all low singletons
are full, every bottom strip is empty, and the later copies
of `u` are absent. Confinement consequently leaves exactly
the nonempty residue set `R`. This proves the stated
infinite-parameter periodicity theorem. QED.

## Boundary behavior, checks and provenance

The proof deliberately establishes a sufficient block-three tail,
not the complete transient table. In particular it does not assume
the exceptional early behavior at `(k,b)=(2,1)`: whether the one
possible point in `X_2[1]` survives is immaterial. If desired,
the preserved exact table can be analyzed separately; it is not
a premise of the theorem proved here.

The first-seed extension rests on `f>b` and `2<f`, rather than
on a canonical-coordinate assumption such as `2b<f`. Thus
`f=3,b=2` is included even though some displayed coordinates
cross an `f`-cell boundary. The high-high exclusion at `f=2`
would lose the strict bound `2<f`; this argument makes no
claim there. This identifies a precise remaining limitation.

The parent supplied the request to remove the certificates and
suggested checking the small-first-seed domain. This worker
derived the enlarged envelope, complete collision classification,
protected-core induction and two-stage extinction. The earlier
[analytic high-plateau proof](../../greedy-upper-20261018/upper2/proof.md)
supplied the anchor and high-gap identities; the new low-gap
witnesses use `F_k+B_i`, because `F_i+B_k` would incorrectly
leave low integers uncovered after `B_k` loses its bottom strip.
That unsuccessful witness choice is retained here as a limitation
of the naive extension, not as a failure of periodicity.

The [targeted diagnostic code (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) and [actual report (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material)
retain eight ray cases, including both `f=3` rays at `k=2,3`,
with literal greedy prefixes and complete envelope-collision checks.
The interval and collision arguments above prove the unbounded
quantifiers. Service-supplied model identity, version and settings
are unknown. This substantive same-team AI work remains subject
to full-text human screening and manual submission. No independent
review, publication or approval is claimed. Prose/data use CC BY 4.0
and any original supporting code uses MIT under repository terms.
