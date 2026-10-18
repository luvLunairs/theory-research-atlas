> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A direct proof for the upper plateau

18 October 2026. Local scientific draft, requiring full-text human review
and manual submission. This is an AI-assisted contributor argument, not
independent verification or a priority claim. Service model identity,
version and configuration are unknown. Integer intervals are inclusive.

## Exact scope and source

Let f>=5, k>=2 and 3<=b<f be integers, excluding the single parameter
type (k,b)=(2,3). Put

    h=2k+1,       g=hf+b,       c=2b-1,
    m=3hf+c=(6k+3)f+2b-1.

We prove the complete strict greedy sequence S(f,g), whose successive
candidates avoid sums of two distinct earlier entries. Both seed sizes
and the quotient are unbounded, and the offset b varies throughout the
stated interval. The proposed conclusions are

    least characteristic period m,
    least gap period p=(k+1)(f-1)+3,
    exact characteristic start N=(8k+8)f+4b-1,
    exact gap preperiod K=(k+3)f+k+b+1.                    (1)

The period prediction is Definition 3(5) and Conjecture 5 of Daan van
Berkel and Wieb Bosma, [*Periodicity conjectures for all 2-sumfree
sequences*, arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1).
Our parameterization gives d=g-f=2kf+b. The source predicts a different
value when (k,b)=(2,3), which is explicitly excluded, and a correction
for k=1, which is outside this proof. No new period prediction or exact
agreement with the source's preperiod formulas is claimed. The shared
literature note controls the bounded update search and novelty limits.

The construction is suggested by eight retained finite probes, but the
proof below uses interval identities and ascending induction, with no
finite-parameter extrapolation or finite-block continuation test.

## The complete set

Define the initial full intervals and high entries by

    F_i=[(h+2i)f+b,(h+2i+1)f+b-1],       0<=i<=k,
    D=[(2h+2)f+c-1,(2h+2)f+c],
    E_j={(2h+2+2j)f+c},                 1<=j<=k-1,
    H={f} union all F_i union D union all E_j.

All these sets are disjoint and contained in [0,m-1]. Write

    u=(h+1)f+b-1,
    V=[(h+4)f+c-2,(h+4)f+c],
    W_i=[(h+2i)f+c-1,(h+2i)f+c],       3<=i<=k,
    R=H minus ({u} union V union all W_i).

Thus u is the upper endpoint of F_0; V is a three-point hole in F_2;
and W_i are two-point holes in later F intervals. Empty index ranges
contribute nothing. Each hole lies in its stated F interval, because
3<=b<f. Let v_- and v_+ denote the two endpoints of V. The claim is

    S = H union (m+(R union {v_-,v_+}))
          union union over n>=2 of (nm+R).                (2)

We use X[n]=nm+X for a translated set. In particular the recurring
parts B_i=R intersect F_i satisfy:

* B_0 is F_0 without its upper endpoint, of length f-1.
* B_1=F_1, of length f.
* B_2 is F_2 without V, with component lengths b-3 and f-b.
* For i>=3, B_i is F_i without W_i, with component lengths b-2 and f-b.

The domain restriction has a precise use: B_k retains both endpoints
of F_k. For k>=3 its omitted internal interval has length 2. For k=2,
b>=4 ensures that both components of B_2 are nonempty; its omitted
internal interval has length 3. Since f>=5, adding any full F_i to B_k
fills the same entire sum interval as adding F_i to F_k. The two
component sum intervals overlap or are adjacent. This convolution fact
will cover the long low gaps without assuming that the holes are absent.

## Collision classification inside the envelope

We first classify all ordinary pairs from H modulo m. The only way for
such a pair to hit R is u+u=D's lower endpoint. Consequently actual
distinct pairs cannot hit R as long as u has only its initial occurrence.
This uniqueness will be proved simultaneously with confinement to H.

The following elementary cases establish the classification. They allow
equal residues except where the exceptional u+u is explicitly identified.

**The seed.** The value 2f is below g and differs from f. Each f+F_i
is the gap following F_i. The sums f+D and f+E_j lie in the gaps between
successive high entries, except f+E_(k-1)=m, whose residue is zero.
They never hit R.

**Two F intervals.** If s=i+j, their ordinary sum interval is

    [(2h+2s)f+2b,(2h+2s+2)f+2b-2].                    (3)

Before reduction this lies above the last F interval. At any following
high entry E_j, the sum interval ends one integer too soon. The only
possible D collision is its lower endpoint at the upper end of F_0+F_0,
and attaining that endpoint requires both terms to equal u. The other
D endpoint is one integer larger. After reduction by m, every part of
(3) lies below g. Such a part can contain f only if s lies between k
and k+1; at s=k its upper endpoint is f-1, and at s=k+1 its lower
endpoint is f+1. Thus it does not contain f. A sum crosses m at most
once, since the largest raw endpoint is smaller than 2m.

**One F interval and D.** These sums wrap once. Their reduced interval is

    [(2i+2)f+b-1,(2i+3)f+b-1].                         (4)

For i<k this is below g and above f. For i=k it starts at u and ends
one integer before F_1, meeting H only at u. Since u is removed from R,
there is no R collision.

**One F interval and an E entry.** The reduced interval is

    [2(i+j+1)f+b,(2(i+j+1)+1)f+b-1].                   (5)

It is either below g and above f or exactly a gap between F intervals.
It therefore avoids every F interval and the seed; it is also below
the high D/E region. Again exactly one m is subtracted.

**Two high entries.** These sums also wrap exactly once. The possibilities
are

    D+D:       (h+4)f+[c-2,c],
    D+E_j:     (h+4+2j)f+[c-1,c],
    E_i+E_j:   (h+4+2i+2j)f+{c}.                       (6)

When their F index is at most k these are precisely V, W_(j+2), or
an upper point of W_(i+j+2), respectively. All were removed from R.
Larger indices lie beyond the last F run. They cannot hit D or E:
their f-coefficient is odd, while those high entries have even
f-coefficients, and the remaining coordinate difference has absolute
value at most 2, less than f. They also cannot hit the small seed.
This proves the promised classification, including its sole exception.

In particular (H+R) mod m avoids R. The stronger unqualified claim
that H+H avoids R would be false because of u+u; the strict distinctness
condition and the uniqueness argument below are essential.

## The initial block and the protected recurring entries

Before the end of F_k, the sequence consists exactly of f and all F_i.
Indeed f+F_i fills each intervening gap, and the smallest sum involving
two F entries is at least 2g, larger than the end of F_k. Thus these
full intervals are available as fixed initial anchors.

Between F_k and D, addition of f to F_k covers through
(2h+1)f+b-1. Distinct self-sums of F_0 fill

    [2hf+2b+1,(2h+2)f+2b-3].                           (7)

These intervals overlap or are adjacent because b<=f-1, and their
union reaches exactly the point before D. In particular 2g is covered
by f+F_k, although the formal pair g+g is unavailable. After D and
after each E_j, use F_0+F_(j+1), with j=0,...,k-1. Their ranges are

    [(2h+2+2j)f+2b,(2h+4+2j)f+2b-2],                (8)

the gaps between the high entries; the last extends beyond m-1.
The factors are disjoint initial intervals. The collision classification
protects D and every E_j, since the only potential R collision u+u
uses the same actual initial entry twice. Induction on the candidate
integer now proves that block zero is exactly H.

For subsequent blocks we use simultaneous ascending induction on the
actual candidate integer. The assertions are that every selected residue
lies in H, u has only its initial occurrence, and every R entry is
selected. The collision classification protects an R candidate whenever
the assertions hold for smaller integers. Every later u[n], n>=1,
is excluded by

    min(F_k)+min(D[n-1])=nm+u.                          (9)

These are distinct actual entries: for n=1 the initial F_k and D are
disjoint, and for n>=2 they lie in different blocks. They are positive
and smaller than their sum. Thus the only exceptional R collision can
never become a valid distinct pair.

It remains to exclude candidates outside H without assuming the entire
future block. The next section gives representations using initial
anchors and protected R entries. A protected summand in the current
block is smaller than its represented target, since its partner is
positive; this justifies ordinary ascending induction and avoids any
circular assumption that the whole block has already been selected.

## Complete coverage outside H in every later block

All ranges below are offsets relative to nm, for n>=1. Use only the
part of a sum interval lying in the stated block.

**Low region.** For i=0,...,k, use F_i+B_k[n-1]. For n>=2 the
convolution fact established above gives exactly

    I_i=[(2i-1)f+1,(2i+1)f-1].                         (10)

Use also F_i+D[n-1], 0<=i<=k-1, giving

    J_i=[(2i+2)f+b-1,(2i+3)f+b-1].                    (11)

The interval I_0 covers [0,f-1]. The intervals I_1,...,I_k cover
from f+1 to (2k+1)f-1 except the points 3f,5f,...,(2k-1)f.
Each such point belongs to a J_i, and J_(k-1) also covers from
(2k+1)f through g-1. Thus precisely the low region outside the
selected seed residue f is covered.

For n=1 use the full initial F_k in place of B_k[0]. When i<k the
factors are disjoint. At i=k the distinct self-sum loses the two
endpoints of I_k, giving

    [(2k-1)f+2,(2k+1)f-2].

The missing first point is in J_(k-2), and the missing last point
is in J_(k-1), using b>=3 and b<f. Every F_i/D pair is disjoint.
This handles the entire first-block distinctness boundary explicitly.

**Between F intervals.** The selected translate nm+f plus the fixed
F_i covers exactly the gap after F_i and before F_(i+1), for i<k.
It also covers the first part of the gap after F_k. The rest of that
gap is covered by F_0+B_0[n], whose range is

    [2hf+2b,(2h+2)f+2b-3].                            (12)

Its right endpoint is immediately before D, and its left endpoint
overlaps the seed-plus-F_k range because b<f. These pairs have
different actual summands.

**High gaps.** For j=0,...,k-1 use F_j+B_1[n]. Since B_1 is full,
these give exactly (8). They cover the gap after D and after every
E_j, extending through the final high gap. The factors lie in
different blocks and are distinct.

This accounts for every point outside H. Together with (9) and the
protected-entry argument, the simultaneous induction proves confinement,
the uniqueness of u, and the presence of every R entry in all blocks.

## Exact elimination of the remaining extras

For every W_i[n], 3<=i<=k and n>=1, the sum D+E_(i-2)[n-1]
fills that two-point interval, by (6). Its factors are distinct even
in the initial block. Thus all such later extras are forbidden.

For V[n], D+D[n-1] fills the entire three-point interval when n>=2,
because the blocks differ. At n=1 the distinct self-sum of the two
initial D entries gives only the middle point of V. Its endpoints
v_- and v_+ correspond exactly to doubling one initial D entry.

Those two endpoints in block 1 have no other representation. The
collision calculations show that no seed/F or F/F or F/high pair
can reach them. Among high/high pairs, only D+D has F index 2;
every pair involving an E has larger index. To reach m+V the two
D summands must both be in block zero, since their unshifted sum
already lies in m+V. Each endpoint therefore has only its inadmissible
diagonal representation. They are selected. This proves precisely (2).

## Least periods and exact transient

In R the full run B_1 is the unique one-run of length f. Every other
one-run has length at most f-1: the split F runs have the lengths
listed above, D has length 2, and the seed/E entries are singletons.
All adjacent runs have nonempty zero gaps. A proper cyclic repetition
would repeat the unique length-f marker, which is impossible. Thus m
is the least characteristic period.

The initial set H contains (k+1)f+k+2 entries. Removing the one point u,
the three V points and 2(k-2) W points leaves

    |R|=(k+1)f-k+2=(k+1)(f-1)+3.

A shorter gap period would induce a characteristic translation with
fewer than |R| selected entries; every such translation must be a
positive multiple of primitive m. Therefore the least gap period is p.

The last deviation from the periodic extension of R is the extra
point m+v_+. Its next integer is the selected point

    N=m+v_++1=(8k+8)f+4b-1.

Every later point agrees with the periodic extension. Earlier starts
with a different eventual period are impossible, since every eventual
period is a multiple of primitive m and every positive m-translate of
this last extra point is absent. Thus N is the exact characteristic start.

Block zero contributes (k+1)f+k+2 selected entries before N. In block
1, the entries before N are the seed residue, B_0, B_1, the first
component of B_2 and the two extra endpoints of V. Their count is

    1+(f-1)+f+(b-3)+2=2f+b-1.

The total is K=(k+3)f+k+b+1. The actual incoming gap to N is 1.
The periodic incoming gap is 4 if b>=4; if b=3, the first component
of B_2 is empty and that incoming gap is f+4. Hence this gap really
is a final mismatch, and all later gaps repeat. This proves all of (1).

## Failure boundary, checks and limits

At k=2,b=3, B_k loses its lower endpoint and the low-gap convolution
used in (10) is invalid. The observed later extra residue 3f+3 is not
silently discarded. This parameter type is excluded, consistently with
the distinct period correction in the source. It is a failure of this
particular table, not a counterexample to periodicity.

The initial unqualified H+H exclusion idea also failed: u+u reaches
the lower endpoint of D. The corrected proof retains this exception
and proves uniqueness of u by (9). No assumption of modular sum-freeness
of the whole envelope is used.

The finite discovery record is [exploration.json (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material),
generated by [explore.py (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material). [diagnostics.py (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material)
checks eight specified triples, separately exercising k=2, b=3, and
b=f-1 within the theorem's domain, and also retains the exact first
failure of the excluded table at f=8,k=2,b=3. Its assertions also check
the unique envelope collision u+u, the last characteristic discrepancy,
and the incoming-gap phase. Actual outcomes, timings and exact version
hashes are in [diagnostics.json (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material). Numerical tests check the
transcription and stated boundaries; the universal result rests on
the direct proof, not on those tests. The budget is 300 measured process
CPU seconds, standard-library Python, no installations or paid runs.
Unmeasured model compute, session CPU and peak memory are unknown.

The source and prior local interval/envelope methods are credited above
and in the shared contribution note. The parent and delegated Codex
contributors supplied this continuation and same-team checking; no
human screening, independent verification, or approval is asserted.
The excluded quotient boundary, offsets b=1,2, small seeds f<=4, and
arbitrary seeds are not settled by this draft. Original prose/data use
CC BY 4.0 and code uses MIT under the repository terms.
