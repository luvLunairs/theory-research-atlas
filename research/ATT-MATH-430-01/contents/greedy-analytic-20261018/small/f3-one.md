> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A direct proof for S(3,6k+1)

18 October 2026. Local scientific draft for full-text human review and
manual submission. Actual service model identity, version and configuration
are unknown. The argument is same-team AI work, not independent verification.

## Statement and provenance

Let k>=2, g=6k+1 and m=24k+3. In this note every displayed progression
has step six, and [x,y] means the inclusive progression from x to y.
An upper endpoint smaller than its lower endpoint means the empty set.
Put

    A=[18k-6,24k], B=[6k+1,18k+1], C=[2,12k-4],
    D=[3,6k-9], E={24k-1}, R=A union B union C union D union E,
    F=[24k-6,24k], Q=[6k+2,12k+2], Z=[6k+3,12k-3],
    u=12k+6, v=12k+2, w=6k-3.

Define blocks by

    P_0={3,u} union F union B union Q union Z,
    P_1=[18k,24k] union B union C union [3,6k-3] union E,
    P_n=R for n>=2,
    T=union_(n>=0)(nm+P_n).

**Proposition.** T is the strict greedy sequence S(3,6k+1). Consequently
it is m-periodic from 2m. No claim that m is least is required; at k=2
the least characteristic period is smaller.

The formulas for k>=3 are transcribed from the retained
[first-seed-three table (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).
The period prediction and underlying sequence problem belong to Daan
van Berkel and Wieb Bosma, [arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1),
Definition 3 and Conjecture 5; the retained source note and the parent
source check record inspected passages and screening limitations.
The present argument replaces that family's parameter certificate by
explicit global sum identities. The proof below also works at k=2.
It uses the elementary chronological identification principle in the
[lifetime lemma](../lifetime-lemma.md): positive summands of a target
integer are smaller than that target.

All block offsets lie in [0,m), and T contains precisely 3,g at or below
g. We prove that T and its distinct-summand sumset are complementary
above g. This identifies T with the greedy sequence by induction.

## Excluding all selected entries

First, (R+R) modulo m is disjoint from R, even allowing equal residues.
Here are all fifteen ordinary sum intervals before carrying. The last
column explains their avoidance of R. A carried value has m subtracted;
raw residue classes are taken modulo six.

| Pair | Ordinary sum interval | Exclusion |
| --- | --- | --- |
| A+A | [36k-12,48k] | raw class 0 is above A; carried class 3 is above D |
| A+B | [24k-5,42k+1] | raw class 1 is above B; carried class 4 is absent |
| A+C | [18k-4,36k-4] | raw class 2 is above C; carried class 5 is below E |
| A+D | [18k-3,30k-9] | raw class 3 is above D; carried class 0 is below A |
| A+E | [42k-7,48k-1] | carried class 2 is above C |
| B+B | [12k+2,36k+2] | raw class 2 is above C; carried class 5 is below E |
| B+C | [6k+3,30k-3] | raw class 3 is above D; carried class 0 is below A |
| B+D | [6k+4,24k-8] | class 4 is absent |
| B+E | [30k,42k] | carried class 3 is above D |
| C+C | [4,24k-8] | class 4 is absent |
| C+D | [5,18k-13] | class 5 is below E |
| C+E | [24k+1,36k-5] | raw class 1 is above B; carried class 4 is absent |
| D+D | [6,12k-18] | class 0 is below A |
| D+E | [24k+2,30k-10] | raw class 2 is above C; carried class 5 is below E |
| E+E | {48k-2} | carried class 1 is above B |

For example the smallest carried A+A value is at least 12k-15,
which is greater than 6k-9 for k>=2. Every other comparison follows
directly from the displayed endpoints. Intervals that cross m are split
there; a row need not actually have both raw and carried portions.

Every offset of T outside R belongs to u,v,Z in block zero, or w in block
one. At k=2, u already belongs to A; allowing it again among these
components only duplicates a harmless case. The offset w is absent from
Z. Each component is harmless when added to R.
For completeness the following table gives every raw mixed interval.
Splitting at m shows no intersection with R: raw classes 0,1,2,3,5
lie respectively outside A,B,C,D,E, and raw class 4 is absent; the same
statement holds after subtracting m and changing the class by three.

| Extra | +A | +B | +C | +D | +E |
| --- | --- | --- | --- | --- | --- |
| u | [30k,36k+6] | [18k+7,30k+7] | [12k+8,24k+2] | [12k+9,18k-3] | {36k+5} |
| v | [30k-4,36k+2] | [18k+3,30k+3] | [12k+4,24k-2] | [12k+5,18k-7] | {36k+1} |
| Z | [24k-3,36k-3] | [12k+4,30k-2] | [6k+5,24k-7] | [6k+6,18k-12] | [30k+2,36k-4] |
| w | [24k-9,30k-3] | [12k-2,24k-2] | [6k-1,18k-7] | [6k,12k-12] | {30k-4} |

Among extra-extra pairs the only hits on R are:

* v+max(Z)=24k-1 in block zero, where E is absent;
* the portion [max(12k+12,18k-6),24k-12] of the strict self-sum
  Z dotplus Z=[12k+12,24k-12], where block zero has no selected entries;
* the endpoint 18k-6 of Z+w=[12k,18k-6], in block one,
  where P_1 lacks precisely that A endpoint.

Indeed u+v=m+5; u+Z=[18k+9,m]; u+w=18k+3; v+w=18k-1.
None gives another R hit, even after carrying. The actual w has block
index one, so its sums with initial extras have that additional m.
There are no permitted u+u,v+v,w+w pairs because each extra is a
single actual term. These statements exhaust the extra-extra pairs.
The maximum in the second bullet matters at k=2: this intersection is
{36}, whereas u=30 is selected and also belongs to A. For k>=3 the
lower endpoint is 18k-6.

It remains to protect the selected extras themselves. In block zero,
u has class 0 and is smaller than the first distinct Z+Z sum 12k+12;
3+Z ends at 12k. Other class-0 pairs available below u do not exist.
The extra v has class 2 and is smaller than the first distinct B+B
sum 12k+8. A target in Z has class 3 and is smaller than the first
B+Q sum 12k+3; all other possible class-3 pairs are larger. The
remaining initial entries are already protected by the preceding tables.

The extra w in block one is the actual number m+w=30k. A sum of two
block-zero entries of class 0 is either from Z+Z or 3+Z, both below
30k, or involves u,F, whose possible sums are above 30k; diagonal
u+u is unavailable. There are no other class-0 pairs in P_0. A
block-zero plus block-one representation would need offset sum w;
the only initial entry smaller than w is 3, but w-3=6k-6 is absent
from P_1. Two block-one entries are too large. Thus this extra is
also protected. We have proved T intersect (T dotplus T) is empty.

## Covering every omission in block zero

The following sums cover the omitted candidates above g, separately
in all six residue classes. Every row is an exact AP sum identity.
Self-sums marked with a dot use unequal summands; all other pairs
have different residue classes or disjoint supports.

| Class | Covering sums |
| --- | --- |
| 0 | 3+Z=[6k+6,12k]; Z dotplus Z=[12k+12,24k-12] |
| 1 | u+B=[18k+7,30k+7] |
| 2 | B dotplus B=[12k+8,36k-4] |
| 3 | B+Q=[12k+3,30k+3] |
| 4 | 3+B=[6k+4,18k+4]; B+Z=[12k+4,30k-2] |
| 5 | 3+Q=[6k+5,12k+5]; Q+Z=[12k+5,24k-1] |

The class-0 hole between the first two rows is u, which is selected;
the final two class-0 points form F. The selected B,Q,Z fill the other
initial stretches in their respective classes. The two intervals in
each remaining class overlap or meet at consecutive step-six points.

## Covering every positive block

Write X[n]=nm+X when the indicated set is selected in block n.
B,F are selected in every block; Q,Z,u are selected in block zero;
C and E are selected in every positive block. Let D_n be the actual
class-3 progression in block n: D_1=[3,6k-3] and D_n=D for n>=2.
All expressions below are listed as offsets after subtracting nm.
The table holds for every n>=1 except where a restriction is shown.

| Target class | Pair of selected sets | Resulting offsets |
| --- | --- | --- |
| 0 | Q[0]+B[n-1] | [-12k,6k] |
| 0 | Z[0]+F[n-1] | [6k-6,12k-6] |
| 0 | Z[0]+D_n[n] | [6k+6,18k-6] if n=1; [6k+6,18k-12] otherwise |
| 1 | Z[0]+B[n-1] | [-12k+1,6k-5] |
| 1 | u[0]+B[n] | [18k+7,30k+7] |
| 2 | B[0]+B[n] | [12k+2,36k+2] |
| 3 | B[0]+C[n] | [6k+3,30k-3] |
| 3 | E[1]+B[n-2], n>=2 | [6k-3,18k-3] |
| 4 | u[0]+B[n-1] | [-6k+4,6k+4] |
| 4 | F[0]+B[n-1] | [6k-8,18k-2] |
| 4 | Z[0]+B[n] | [12k+4,30k-2] |
| 5 | B[0] dotplus B[0], n=1 | [5-12k,12k-7] |
| 5 | B[0]+B[n-1], n>=2 | [-12k-1,12k-1] |
| 5 | Z[0]+C[n] | [6k+5,24k-7] |

Some intervals cross neighboring blocks; only their intersections with
[0,m) are needed. These formulas are obtained by adding the displayed
endpoints and subtracting m precisely when the block indices add to
n-1. Unequal summands are automatic except for the explicitly restricted
self-sum in the class-5 row. In the class-2 row the two B sets have
different block indices, so their extreme doubles are correctly retained.

These intervals cover exactly the following required omissions (extra
covered points outside the target block can be discarded):

* class 0: [0,18k-6] at n=1, and [0,18k-12] at n>=2;
* class 1: [1,6k-5] and [18k+7,24k+1];
* class 2: [12k+2,24k+2];
* class 3: [6k+3,24k-3] at n=1, and [6k-3,24k-3] at n>=2;
* class 4: [4,24k-2];
* class 5: [5,24k-7].

For the potentially shortest joins, 6k+6<=12k and
6k+5<=12k-1 hold at k>=2, so no step-six point is missed. These
omission lists are the literal complements of P_n in [0,m). Together
with exclusion and the block-zero calculation, they prove the global
greedy identity and the proposition. No finite-prefix certificate or
computer-generated identity is a premise of this proof.

## Checks and limits

The written identities were rechecked algebraically, including k=2 where
D is a singleton, the sole block-one extra, and the distinct B self-sum.
A diagnostic caught a transcription error in the last table: subtracting
m from the lower endpoint 12k+8 gives 5-12k, not 8-12k. The corrected
endpoint has the required residue class 5; the coverage conclusion is
unchanged. The failed equality is retained in the attempt record.
A same-team read caught a further k=2 classification issue: u then lies
in A, and the Z self-sum intersection starts at 36 rather than 30. The
maximum and explicit overlap note above repair that explanation without
changing the candidate sequence or any coverage witness.
A companion finite diagnostic is retained separately; such checks do not
establish the universal statement or provide independent verification.
This note asserts a sufficient characteristic period and threshold only.
Source novelty, a least-period claim, formal proof checking and human
scientific review remain outside its completed checks.
