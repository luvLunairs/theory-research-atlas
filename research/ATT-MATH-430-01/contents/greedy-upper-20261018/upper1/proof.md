> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Reverse triangular extinction in the upper-offset interior

18 October 2026. Local scientific draft requiring full-text human review
and manual submission. The source predicts the gap count; the membership
formula and structural argument below are contributor proposals, not a
novelty claim or independent verification. Integer intervals are inclusive.

## Exact target and residue formula

Let k>=1 and f>=5 be integers, and assume

    ceil(f/2)+1 <= a <= f-2.

This nonempty domain automatically has f>=6. Put g=2kf+a and

    m=(6k+1)f+2a-1,          p=k(2f+2-a)+a.

Let S be the strict greedy sequence with seeds f,g: each later selected
integer is the least larger integer not equal to a sum of two distinct
earlier selected integers. Use 2f-cells, writing [i;u,v] for the integer
interval 2fi+[u,v]. Define

    A_i=[i;a,f],                              0<=i<k-1,
    A_(k-1)=[k-1;a,f+1],
    B_i=[k+i;a,2a-1],                         0<=i<k,
    C=[2k;a+1,2a-1],
    D_i=[2k+1+i;3a-f-1,2a-1],                 0<=i<k,
    R=union_i A_i union union_i B_i union C union union_i D_i.

All runs are nonempty, disjoint and lie strictly between 0 and m.
The proposed theorem is

    x in S <=> x mod m in R,                  x >= (6k-3)m.       (1)

The least characteristic period is m and the least gap period is p.
The threshold in (1) is a sufficient bound. No exact least transient,
least gap preperiod, or optimal uniform bound is claimed here.

For a=ceil(f/2)+1+j, Definition 3(4) and Conjecture 5 of Daan van Berkel
and Wieb Bosma, [*Periodicity conjectures for all 2-sumfree sequences*,
v1](https://arxiv.org/html/2609.18522v1), predict this value p. Their
correction at a=f-1 for k>1 is outside the present interior domain.
The initial inspection included the full Definition 3 branch and its
corrections. The shared literature note records later-result searches
and unresolved historical screening limits.

The proof extends the invariant-envelope and finite-extinction method
from the [earlier lower-offset argument (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).
The target template and the direction of its dependence between run
indices are different. In particular no exact interval recurrence for
the transient is assumed. At k=1 the residue formula agrees with the
earlier [plateau theorem (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material);
the new target here is the unbounded-quotient extension.

## The compatibility lemma and the larger envelope

Define the initial anchor intervals and two exceptional integers

    F_i=[k+i;a,f+a-1],                        0<=i<k,
    u=4kf+a,                  v=4kf+2a,
    E_i=[k+i;2a,f+a-1],                       0<=i<k,
    H=R union union_i E_i union {u,v}.

Thus F_i=B_i union E_i, and all these extra strips are nonempty.
We use the following explicit modular compatibility statement:

    ((H+R) mod m) intersect R is empty.                       (2)

The parent contributor supplies its separate [cell-carry proof](../compatibility.md).
Equation (2) includes ordinary sums with equal residues; it is
strong enough to control different actual entries in different blocks.
The remainder of this document proves confinement, reachability and
minimality from this specific lemma, not from a numerical tail guess.

Only two extra-strip collision types can meet R. For x in E_i and y
in E_j, writing s=i+j, their raw sum, after one carry of length 2f, is

    [2k+s+1;4a-2f,2a-2].

If s<=k-1, it lies below m and can meet only D_s, strictly below that
run's upper endpoint. For s>=k, it wraps once modulo m and becomes

    [s-k;2a-f+1,f-1],

which can meet only A_(s-k), strictly below its upper endpoint.
Both assertions use 2a>=f+2 and a<=f-2. Some points in these enlarged
intervals are gaps, which does not affect the necessary conditions.

The integer u plus E_i misses R: after subtracting m its coordinates
in cell i-1 range from f+a+1 to 2f, a gap including the zero carry;
for i=0 the relevant values lie in the final gap or at zero. The
integer v plus E_i has reduced coordinates [2a-f+1,a] in cell i,
so it can hit only the lower point a of A_i. This happens only when
the E_i summand is its top endpoint f+a-1. Finally

    u+v-m=(2k-1)f+a+1

is in the gap after A_(k-1). The doubles u+u and v+v are inadmissible
when u,v each occur only once; that fact is proved simultaneously below.

Consequently the protected entries of R are every A upper endpoint
(including both f and f+1 in A_(k-1)), every B_i, all of C, and every
D_i upper endpoint. None can be excluded by an admissible pair from H
provided u,v have only their initial occurrences.

## Actual initial anchors and confinement

Before u, the actual sequence consists of {f} and all F_i. Adding f
to each F_i covers its following gap. No sum of two F entries occurs
below 2g+1=v+1, so these intervals and the next interval

    G=[2k;a,2a]=[u,v]

are all selected. Adding f to F_(k-1) ends at u-1; adding f to G starts
above v because f>a. This proves the asserted initial anchors directly.

After G and below m, all points outside H are covered by these sums:

    F_0 distinct-plus F_0
        =[2k;2a+1,2f+2a-3],
    F_0+F_i
        =[2k+i;2a,2f+2a-2],                 1<=i<k,
    F_0+G
        =[3k;2a,f+3a-1].

The first covers the gap after G through the next D run's lower
endpoint minus one. The second covers the gap after D_(i-1), and the
last covers the gap after D_(k-1) through the block end. Endpoint
coverage uses f-a>=2. F_0 and F_i are disjoint for i>=1, and F_0 and G
are disjoint. The protected D upper endpoints cannot be excluded by
the collision classification. Ascending induction on integers now
proves confinement to H throughout block zero and the presence of all
B_i, C and D upper endpoints there. No lower A entries below g are
asserted to be selected.

For later blocks, write X[n]=nm+X. Assuming confinement and the stated
protected entries at all smaller integers, the collision classification
forces each next protected entry to be selected. All integers outside H,
and all later copies of u,v, are excluded by the following witnesses.
Intervals in the right column are offsets relative to nm.

| Gap or exceptional target | Actual witnesses | Covered offsets |
| --- | --- | --- |
| Before A_0, k>=2 | F_(k-1)+B_1[n-1] | [-f+1,a-1] |
| Before A_0, k=1 | F_0+C[n-1] | [-f+2,a-1] |
| After A_i, 0<=i<=k-3 | F_(k-1)+B_(i+2)[n-1] | [(2i+1)f+1,(2i+2)f+a-1] |
| After A_(k-2), k>=2 | u+B_(k-1)[n-1], F_(k-1)+C[n-1] | [(2k-3)f+1,(2k-3)f+a], [(2k-3)f+2,(2k-2)f+a-1] |
| After A_(k-1) | u+C[n-1], F_(k-1)+{D_0 upper}[n-1] | [(2k-1)f+2,(2k-1)f+a], [(2k-1)f+a,2kf+a-1] |
| After F_i | F_i+{f}[n] | [2(k+i)f+f+a,2(k+i+1)f+a-1] |
| u[n] | {F_0 upper}+{A_(k-1) upper}[n] | {4kf+a} |
| v[n] and the gap after C | F_0+B_0[n] | [4kf+2a,(4k+1)f+3a-2] |
| After D_i, k>=2 | F_i+B_1[n] | [(4k+2i+2)f+2a,(4k+2i+3)f+3a-2] |
| After D_0, k=1 | u+B_0[n], F_0+C[n] | [6f+2a,6f+3a-1], [6f+2a+1,7f+3a-2] |

An absent index range contributes no row. The last gap intervals can
extend beyond m; only the portion in the current block is needed. The
row after F_(k-1) reaches u[n]-1, and the next singleton witness covers
u[n]. The interval for v[n] starts at its exact offset; equivalently its
first witness is the seed g plus the protected lower endpoint of B_0[n].
Each summand is positive and hence smaller than its represented target,
so witnesses in block n are already available when needed.

For n>=2 the early-row factors are in different blocks. For n=1 the
required B,C,D entries are present by the block-zero argument. Every
pair remains distinct except potentially F_(k-1)+B_j[0] with j=k-1.
The intervals share their lower endpoint but have different upper
endpoints. Their distinct sums omit only the first sum. For the low-gap
row at k=2, this lost offset is -f+1, outside the current block. For
k>=3 it occurs in the row after A_(k-3), at offset (2k-5)f+1, and is
covered by the disjoint pair

    u+B_(k-2)[0]=m+[(2k-5)f+1,(2k-5)f+a].

All other initial F/B pairs are disjoint; u is outside each B_i and
outside C, while the F/C and F/D factors are disjoint. Two integer
intervals of length at least two can lose only a shared extreme sum
when equal summands are disallowed: an interior representation (x,x)
can be replaced by (x-1,x+1) in one order. Thus no interior gap is hidden
in the overlapping case. Our intervals meet that length condition.

This closes the simultaneous ascending induction. Every actual selected
integer has residue in H, the protected entries occur in every positive
block, and u,v occur only at their initial values.

## Reverse triangular extinction

Let E_i[n] denote the arbitrary subset of upper-strip E_i actually
selected in block n, translated back by nm. No assumption that it is
an interval is made. From compatibility and the collision calculation,
a missing A_l point in a positive block can only be caused by

* E_i[q]+E_j[r] with i+j=k+l and q+r=n-1, or
* v+E_l[n-1], which can remove only A_l's lower point a and requires
  the top extra f+a-1 to be selected.

For l=k-1 the first case is impossible. Therefore A_(k-1)[n] with its
lower endpoint omitted is full for every n>=1. Its sum with F_0 covers
every extra E_(k-1)[n] except possibly its lowest point 2a. The top
extra f+a-1 is strictly above 2a because a<=f-2. Hence from block 2
the second obstruction also disappears; A_(k-1) is full and its sum
with F_0 excludes the entire E_(k-1) strip. This is the base case.

Induct downwards on l. We prove

    A_l[n] is full and E_l[n] is empty for n>=T_l,
    T_l=3(k-l)-1.                                        (3)

For i+j=k+l, both i and j exceed l. By the induction hypothesis,
nonempty E_i[q],E_j[r] require q<=T_i-1 and r<=T_j-1. Consequently

    n-1=q+r <= T_i+T_j-2 = 3(k-l)-4.

There is thus no such obstruction for n>=3(k-l)-2=T_l-1. In those
blocks A_l with only its lower endpoint omitted is full. The interval
F_0+(A_l minus its lower point)[n] begins at extra coordinate 2a+1
and extends past f+a-1, leaving at most coordinate 2a selected in E_l.
Since that is not the top extra, v can no longer obstruct A_l's lower
endpoint in the next block. A_l is full from T_l, and F_0+A_l[n]
then covers the entire extra strip. This proves (3).

A missing D_l point can only arise from E_i[q]+E_j[r] with i+j=l,
q+r=n. If both extra sets are nonempty, (3) gives

    n <= (T_i-1)+(T_j-1) = 6k-3l-4.

Therefore D_l is full for n>=6k-3l-3. By block 6k-3 every D is full,
all A runs are full, every E strip has vanished, B and C are protected,
and repeated u,v never occur. Together with the separate cell-carry proof
of (2), this proves (1). The proof does not infer convergence from samples.

## Least periods

Write b=f-a. Then b>=2 and a>=b+2. The circular list of one-run lengths
in R consists of

    k-1 copies of b+1; one b+2; k copies of a;
    one a-1; k copies of b+1.

All separating zero runs are nonempty. If a>=b+4, C is the unique run
of length a-1. If a=b+3, the two runs of length b+2 are A_(k-1) and
C; only the former is preceded by a run of length b+1, also when k=1.
If a=b+2, the k+1 long runs (A_(k-1) followed by all B runs) form one
contiguous segment in this circular run list; all other runs have the
shorter length b+1. There is a unique short-to-long transition.
In every case a nontrivial circular repetition would repeat a unique
marker, which is impossible. Thus the least characteristic period is m.

Counting entries gives

    k(b+1)+1 + ka + (a-1) + k(b+1)
      = k(2f+2-a)+a = p.

Any shorter eventual gap period would induce a positive characteristic
translation whose cycle contains fewer than p entries. That contradicts
primitivity of the m-word, proving the least gap period p.

## Evidence, unfinished work and provenance

The initial three discovery cases were (f,k,a)=(12,3,7), (13,3,9), and
(13,4,10). They suggested the 3k+1-run template and the two exceptional
initial endpoints. Their prefixes and measured computation are retained
in [explore.py (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) and [exploration.json (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).
Their observed stabilizations are
finite observations, not the universal proof. The initial endpoint-width
approach was replaced by an arbitrary-subset extinction argument; no
unproved exact width recurrence is asserted.

The separate [diagnostics (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) recheck those three cases and
the deliberate boundaries (6,1,4), (6,2,4), (7,2,5), (8,1,6). They test
the modular compatibility, protected core, confinement, intermediate
extinction bounds, sufficient tail onset and primitive word against a
literal distinct-sum scan. These are finite contributor consistency
checks, not the justification of the universal quantifiers. Actual
results, measured process CPU and exact proof/code hashes are retained
in [diagnostic-results.json (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).

The checks use standard-library Python. Model compute, uninstrumented
session CPU and actual peak memory are unknown.

The region a=f-1 is excluded deliberately: there the lowest and highest
extra coordinates coincide, so reducing a strip to {2a} no longer removes
its top endpoint. That is a precise failure of this extinction argument,
consistent with the source's different period correction. It is not a
counterexample to periodicity.

The compatibility lemma (2) is part of this proof's human-review scope.
No exact preperiod formula or result for arbitrary offsets is claimed.
The source's period conjecture
and the inherited method are credited above. Parent and upper-offset Codex
contributors supplied the new formula and argument collaboratively.
Actual service model identities, versions, configurations and settings
are unknown. Human screening and manual submission remain required.
Original prose/data CC BY 4.0; code MIT. No review approval is assigned.
