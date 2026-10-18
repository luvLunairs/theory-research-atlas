> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Direct proofs for the transition and upper part of the first plateau

18 October 2026. Local scientific draft, requiring full-text human screening
and manual submission. This is AI-assisted research, not independent
verification or an approved machine check.

## Statements and scope

For positive integers f<g, let S(f,g) begin with f,g and append the least
larger integer not expressible as a sum of two **distinct** earlier entries.
Intervals in this note include both endpoints and contain only integers.

The two candidate theorems below address unbounded parameter families:

* **Band theorem:** f>=5 and f<=j<=2f-1, with g=2f+j.
* **Transition theorem:** f>=5 and j=f-1, with g=3f-1.

Both give a complete set description and prove least gap period 2f+2.
They are distinct from the general conjecture, and neither a longer numerical
prefix nor a fitted formula supplies a universal quantifier in the proofs.

The definition and period predictions originate in Daan van Berkel and Wieb
Bosma, *Periodicity conjectures for all 2-sumfree sequences*,
[arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1), Introduction,
Definition 3 and Conjecture 5. The source was opened during this research
session. Exact transient formulas below are derived directly; no agreement
with the source's problematic rendered Definition 8 is asserted. The shared
literature review governs the scope of the novelty search.

For either theorem, it suffices to construct a positive integer set T that
contains exactly f,g at or below g, has no selected element equal to a sum
of two distinct selected elements, and represents every omitted integer
n>g by such a sum. Every positive summand is smaller than n, so induction
identifies T with the greedy sequence. Ordinary interval sums satisfy
[a,b]+[c,d]=[a+c,b+d]; the distinct self-sums of [a,b], when a<b, form
[2a+1,2b-1]. The latter identity follows by using the lower endpoint for
sums at most a+b and the upper endpoint for larger sums.

## Band theorem: f<=j<=2f-1

Fix f>=5 and f<=j<=2f-1. Put m=7f+2j-1. Define actual integer intervals
A_k,B_k,C_k,D_k by shifting row k of this table by km:

| k | A_k-km | B_k-km | C_k-km | D_k-km |
| --- | --- | --- | --- | --- |
| 0 | {f} | [2f+j,3f+j-1] | [4f+j,5f+j-1] | [6f+2j-2,6f+2j-1] |
| k>=1 | [f,f+1] | [2f+j,3f+j-2] | [4f+j+1,5f+j-1] | [6f+2j-2,6f+2j-1] |

Then T, their union over all k>=0, is S(f,2f+j). Its least characteristic
period is m, its least gap period is 2f+2, characteristic periodicity starts
at 4f+j+1, and the least gap preperiod has length f+2.

### Sum exclusion

Let A,B,C,D be the four tail offset intervals. Let R be their union. The
complementary residue intervals in [0,m-1] are

    G0=[0,f-1],                 G1=[f+2,2f+j-1],
    G2=[3f+j-1,4f+j],           G3=[5f+j,6f+2j-3],
    G4=[6f+2j,m-1].

Every selected term has residue in R except for the two actual integers
u=3f+j-1 and v=4f+j. The following exhaustive ordinary-sum table is
disjoint from R modulo m. Including equal summands here only enlarges
sets already proved safe.

| Summand classes | Raw residue-sum interval | Location modulo m |
| --- | --- | --- |
| A+A | [2f,2f+2] | G1 |
| A+B | [3f+j,4f+j-1] | G2 |
| A+C | [5f+j+1,6f+j] | G3 |
| A+D | m+[-1,1] | G4 union G0 |
| B+B | [4f+2j,6f+2j-4] | G3 |
| B+C | m+[2-f,f-2] | G4 union G0 |
| B+D | m+[f+j-1,2f+j-2] | G1 |
| C+C | m+[f+3,3f-1] | G1 |
| C+D | m+[3f+j,4f+j-1] | G2 |
| D+D | m+[5f+2j-3,5f+2j-1] | G3 |
| u+A | [4f+j-1,4f+j] | G2 |
| u+B | [5f+2j-1,6f+2j-3] | G3 |
| u+C | m+[1,f-1] | G0 |
| u+D | m+[2f+j-2,2f+j-1] | G1 |
| v+A | [5f+j,5f+j+1] | G3 |
| v+B | [6f+2j,m-1] | G4 |
| v+C | m+[f+2,2f] | G1 |
| v+D | m+[3f+j-1,3f+j] | G2 |

For example, B+B starts at or above 5f+j because j>=f; C+C ends at
3f-1<=2f+j-1 for the same reason. The other endpoint containments use
f>=5 and j>=f, together with the displayed formulas. The raw intervals
and their reductions cross at most one multiple of m. Thus any sum with
at least one nonexceptional selected summand cannot hit a selected term
whose residue is in R. The only distinct exceptional pair has sum u+v=m,
which is absent.

It remains to exclude targets u and v. The first satisfies
u=f+(2f+j)-1 and is smaller than the least sum of two distinct selected
members. For v, all smaller selected terms are f and members of B_0.
The sums f+B_0 end at v-1, and distinct B_0+B_0 sums start at
4f+2j+1>v. No other smaller selected terms exist. Hence v is safe too.
This proves the required exclusion.

### Coverage of every omitted integer

Write B_0 and C_0 for the unshifted initial intervals in the theorem.
Below m and above g the three omitted intervals are covered as follows:

| Omitted interval | Available sums |
| --- | --- |
| [3f+j,4f+j-1] | {f}+B_0, exactly |
| [5f+j,6f+2j-3] | {f}+C_0=[5f+j,6f+j-1], together with B_0 restricted+ B_0=[4f+2j+1,6f+2j-3] |
| [6f+2j,m-1] | B_0+C_0=[6f+2j,m+f-1] |

The middle pair of intervals has no missing integer precisely because
4f+2j+1<=6f+j, which is the hypothesis j<=2f-1. The other endpoint
containments follow from j>=f and j>=5.

For tail block k, an offset G means the actual interval km+G. The following
table covers every one of its five omitted intervals:

| Block | Omitted offsets | Available sums |
| --- | --- | --- |
| 1 | G0 | B_0+C_0, carrying into block 1 |
| k>=2 | G0 | B_0+C_(k-1)=(k-1)m+[6f+2j+1,m+f-1], carrying into block k |
| 1 | G1 | C_0 restricted+ C_0=m+[f+2,3f-2], together with B_0+D_0=m+[f+j-1,2f+j-1] |
| k>=2 | G1 | C_0+C_(k-1)=km+[f+2,3f-1], together with B_0+D_(k-1)=km+[f+j-1,2f+j-1] |
| k>=1 | G2 | v+D_(k-1)=km+[3f+j-1,3f+j], together with B_0+A_k=km+[3f+j,4f+j] |
| k>=1 | G3 | C_0+A_k=km+[5f+j,6f+j], together with B_0+B_k=km+[4f+2j,6f+2j-3] |
| k>=1 | G4 | v+B_k=km+[6f+2j,m-1], exactly |

The unions in G1 are contiguous because j<=2f-1. Their endpoints remain
inside G1 because j>=f. The unions in G3 are contiguous since j<=2f-1
implies 4f+2j<=6f+j+1; their lower and upper endpoints are exactly the
gap endpoints. The low-gap crossing intervals start below km and finish
at km+f-1. These statements are integer interval calculations, including
their endpoints. Every pair uses disjoint actual intervals, except the
explicitly restricted self-sums. All representations therefore use distinct
selected members. The recurrence criterion now proves the set description.

### Least periods and transient

The cyclic characteristic word has four one-runs, of lengths 2,f-1,f-1,2.
A nontrivial repetition factor would divide four, and hence be 2 or 4.
Factor 2 would require opposite run lengths equal, in particular 2=f-1;
factor 4 would require all run lengths equal. Both are impossible for f>=5.
Thus m is primitive. The block contains 2f+2 ones, so the least gap period
is 2f+2: a shorter repeated gap block would induce a characteristic period
whose sum is a positive multiple of m but whose number of selected entries
is smaller than the number in a primitive m-block, a contradiction.

The initial block differs from the eventual residue extension exactly at
f+1, u and v. The last mismatch is v=4f+j; it is selected initially but
absent at all its positive m-translates. Hence characteristic periodicity
starts exactly at v+1=4f+j+1, even when other candidate periods are allowed,
because every eventual period is a multiple of primitive m. Before v+1
there are f+2 selected entries: f, the f entries of B_0, and v. The incoming
gap from v to v+1 is 1, while its periodic counterpart is f+3. All later
gaps repeat. The least gap preperiod is therefore f+2.

## Transition theorem: j=f-1

Fix f>=5, j=f-1 and m=9f-3. Define the following intervals and shifts:

| k | A_k-km | B_k-km | C_k-km | D_k-km |
| --- | --- | --- | --- | --- |
| 0 | {f} | [3f-1,4f-2] | [5f-1,6f-2] | [8f-4,8f-3] |
| 1 | [f,f+1] | [3f-1,4f-3] | [5f,6f-3] | [8f-4,8f-3] |
| k>=2 | [f-1,f+1] | [3f-1,4f-3] | [5f,6f-3] | [8f-4,8f-3] |

Their union is S(f,3f-1). Its least characteristic period is m, its least
gap period is 2f+2, characteristic periodicity starts at 10f-3, and the
least gap preperiod has length 2f+3.

### Sum exclusion

Let A,B,C,D be the final offset intervals, and R their union. The residue
gaps are

    G0=[0,f-2],           G1=[f+2,3f-2],
    G2=[4f-2,5f-1],       G3=[6f-2,8f-5],
    G4=[8f-2,m-1].

The only selected integers with residues outside R are u=4f-2, v=5f-1,
w=6f-2. All ordinary-sum intervals below are disjoint from R modulo m:

| Classes | Raw interval | Location modulo m |
| --- | --- | --- |
| A+A | [2f-2,2f+2] | G1 |
| A+B | [4f-2,5f-2] | G2 |
| A+C | [6f-1,7f-2] | G3 |
| A+D | m+[-2,1] | G4 union G0 |
| B+B | [6f-2,8f-6] | G3 |
| B+C | m+[2-f,f-3] | G4 union G0 |
| B+D | m+[2f-2,3f-3] | G1 |
| C+C | m+[f+3,3f-3] | G1 |
| C+D | m+[4f-1,5f-3] | G2 |
| D+D | m+[7f-5,7f-3] | G3 |
| u+A | [5f-3,5f-1] | G2 |
| u+B | [7f-3,8f-5] | G3 |
| u+C | m+[1,f-2] | G0 |
| u+D | m+[3f-3,3f-2] | G1 |
| v+A | [6f-2,6f] | G3 |
| v+B | [8f-2,m-1] | G4 |
| v+C | m+[f+2,2f-1] | G1 |
| v+D | m+[4f-2,4f-1] | G2 |
| w+A | [7f-3,7f-1] | G3 |
| w+B | m+[0,f-2] | G0 |
| w+C | m+[2f+1,3f-2] | G1 |
| w+D | m+[5f-3,5f-2] | G2 |

All containments follow from f>=5. For instance A+A lies in G1 because
2f-2>=f+2 and 2f+2<=3f-2 already hold for f>=4; the other comparisons
are no stronger. The three distinct exceptional sums are

    u+v=m,  u+w=m+f-1,  v+w=m+2f.

They are absent: the first is offset zero of block 1; the second precedes
A_1 by one; and the third lies in its G1 gap.

For exceptional targets, u is smaller than the first possible distinct
sum f+(3f-1)=4f-1. For v, the earlier selected integers are f and B_0;
the sums f+B_0 end at v-1 and distinct B_0+B_0 sums begin at 6f-1>v.
For w, the residue table leaves only B+B at its lower endpoint, and v+A
at its lower endpoint. The former would be (3f-1)+(3f-1), a disallowed
repeat. The latter needs residue f-1 in A, whose first selected occurrence
is in block 2 and is too large. Thus exceptional targets are safe too.

### Coverage

Below m and above g, the omitted intervals are

| Omitted interval | Available sums |
| --- | --- |
| [4f-1,5f-2] | {f}+B_0, exactly |
| [6f-1,8f-5] | B_0 restricted+ B_0, exactly |
| [8f-2,m-1] | B_0+C_0=[8f-2,m+f-1] |

In block 1, the low gap is [0,f-1]; the other gaps equal G1 through G4.
In blocks k>=2, all five gaps equal G0 through G4. They are covered by:

| Block | Gap offsets | Available sums |
| --- | --- | --- |
| 1 | [0,f-1] | B_0+C_0, carrying into block 1 |
| 1 | G1 | C_0 restricted+ C_0=m+[f+2,3f-2], exactly |
| 1 | G2 | v+D_0=m+[4f-2,4f-1], together with B_0+A_1=m+[4f-1,5f-1] |
| k>=2 | G0 | B_0+C_(k-1)=(k-1)m+[8f-1,m+f-2], carrying into block k |
| k>=2 | G1 | C_0+C_(k-1)=km+[f+2,3f-2], exactly |
| k>=2 | G2 | B_0+A_k=km+[4f-2,5f-1], exactly |
| k>=1 | G3 | B_0+B_k=km+[6f-2,8f-5], exactly |
| k>=1 | G4 | v+B_k=km+[8f-2,m-1], exactly |

The only nontrivial union overlaps at 4f-1. The crossing intervals have
the displayed nonnegative carried endpoints. Distinctness follows from
disjoint actual intervals except where explicitly imposed in the self-sums.
All positive representing summands precede their target. This completes
the greedy recurrence proof.

### Least periods and transient

The tail one-runs have lengths 3,f-1,f-2,2. A factor 2 repetition would
require both 3=f-2 and f-1=2, which cannot hold simultaneously; a factor 4
would require 3=2. Thus m is primitive. Its 2f+2 ones give least gap period
2f+2 by the characteristic/gap argument used above.

The last mismatch from the m-periodic extension is the missing offset f-1
in block 1, namely m+f-1=10f-4. All larger decisions repeat; its positive
m-translates are present. Hence the exact characteristic start is 10f-3.
Block 0 contributes 1+f+f+2=2f+3 selected entries before that start. The
incoming gap is 2f, while the incoming gap at its translate by m is 1:
that translate is the second member of the full tail A run. Thus the last
nonperiodic incoming gap is located precisely here, and the least gap
preperiod has length 2f+3.

## The precise upper-edge obstruction at j=2f

The band formula cannot simply be continued to j=2f. Here g=4f. Its initial
set would list f, [4f,5f-1], [6f,7f-1], followed only much later by the last
run. But 8f must be selected. The earlier forbidden sums are covered by

    f+[4f,5f-1]=[5f,6f-1],
    f+[6f,7f-1]=[7f,8f-1],
    [4f,5f-1] restricted+ [4f,5f-1]=[8f+1,10f-3].

No other pair of earlier selected terms has sum 8f: two entries from the
first long run could do so only as 4f+4f, which is disallowed, and all pairs
involving two entries from or beyond the second long run are larger.
The same interval checks establish exactly the stated prefix below 8f.
Therefore 8f is the first discrepancy from the proposed continuation of
the band's initial block, and an extra run or singleton is necessary.
This is an obstruction to that formula, not to periodicity. The parent's
separate endpoint argument treats j=2f.

## Checks, limits and provenance

The parameter proofs above use exact interval arithmetic, finite exceptional
terms and induction. Small examples discovered the formulas; they are not
used to prove unbounded quantifiers. The first diagnostic exploration focused
on f=2j-3 and found a four-run pattern. The parent generalized that pattern
to its adjacent two-parameter region, so the discovery scripts and output
remain retained rather than being relabeled as a separate theorem here.

The parent's `band_check.py` and shared interval algebra provide a second
checking path within this same AI-assisted attempt. Their symbolic domain
checks are distinct from numerical diagnostics, but neither constitutes
independent scientific verification or an approved machine check. The
present formulas and proofs were derived by a Codex subagent whose actual
service model identifier, version and reasoning/compute configuration were
unavailable and remain unknown. Earlier local sequence proofs, van Berkel
and Bosma's prediction, and same-team formula messages informed this work.

No unresolved mathematical step was identified in these two arguments as
written. Their correctness, novelty and significance still require review;
the universal conjecture and parameters outside the stated scope are not
resolved by these claims. The batch's single assistance note and exact-version
check report must include this proof, its computations and dependencies.
Original prose/data follow the repository's CC BY 4.0 terms and original
code follows MIT. No human screening, publication or approval is claimed.
