> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A direct envelope and anchor proof for S(3,6k)

18 October 2026. Local scientific draft; full-text human review and manual
submission required. Actual service model identity/version/configuration
are unknown. No independent or formal verification is claimed.

## Candidate and notation

Let k>=5, g=6k and m=24k. A pair r:I denotes the step-six progression
{6i+r:i in I}; every interval of row indices is inclusive, with step one.
Block n means adding nm, so carrying one block subtracts 4k from the row
index and leaves its residue r unchanged. All endpoints below are integers.

The following table comes from the retained
[first-seed-three formulas (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).
The period prediction is credited there to Daan van Berkel and Wieb Bosma,
[arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1), Definition 3 and
Conjecture 5. The parent source check records the literature screening.
Here a new explicit global argument replaces the old parameter certificate.

| r | P_0 | P_1 | P_2 | R=P_n, n>=3 |
| --- | --- | --- | --- | --- |
| 0 | [k,2k] | [k,k+1] | {2k-1} | [2k-2,2k+1] |
| 1 | [k,2k-1] | same | same | same |
| 2 | [k,2k-1] | [0,k-1],{4k-1} | [0,k-2] | [1,k-2] |
| 3 | {0,4k-1} | same | {0,1,4k-1} | same as P_2 |
| 4 | {2k} | {1,3k-1},[3k+2,4k-2] | [3k-2,4k-3] | same as P_2 |
| 5 | [2k,3k-1] | [2k+1,3k-1] | same as P_1 | same as P_1 |

Let T be the union of nm+P_n. We prove **T=S(3,6k)**; hence m is a
characteristic period from 3m. We make no least-period assertion here.
The argument uses only endpoint addition, strict self-sums, and induction
on the candidate integer. It is independent of a program certificate.

For a row interval [a,b] in residue r, the strict self-sum has row
interval [2a+1+c,2b-1+c] in residue 2r mod 6, where c=floor(2r/6).
For two different residue components, ordinary endpoint addition is exact,
with c=floor((r+s)/6). For equal residues in different blocks the ordinary
sum is also exact. These elementary identities will be used explicitly.

## The envelope and all potential collisions with its core

Write the eventual core as

    A=0:[2k-2,2k+1], B=1:[k,2k-1], C=2:[1,k-2],
    D=3:[0,1], E=3:{4k-1}, F=4:[3k-2,4k-3],
    G=5:[2k+1,3k-1].

Every selected block is contained in the following ten disjoint components
of an envelope H; capitalized X,Y,Z below denote initial anchor subsets:

    x=0:[k,2k+1], b=B, y=2:[0,2k-1], t=2:{4k-1},
    d=D, e=E, s=4:{1}, v=4:{2k},
    f=4:[3k-2,4k-2], z=5:[2k,3k-1],
    X=0:[k,2k], Y=2:[k,2k-1], Z=5:[2k,3k-1].

Here X,Y,Z,v are present in block zero; b and e are present in every
block, as is 3=3:{0}. The names s,t and u=4:{4k-2} denote actual
exceptional components in block one only. The offset 2=2:{0} occurs
in blocks one and two only. The component G is present in every block.

The following is a complete list of intersections of ordinary H-pair
sums with R, after reduction modulo m. A carry of one means subtracting
4k from the row index. An entry such as A:[a,b] records row indices.

| Pair | Intersection with R | Carry |
| --- | --- | --- |
| x+x | A:[2k,2k+1] | 0 |
| x+v | F:[3k,4k-3] | 0 |
| y+y | F:[3k-2,4k-3] | 0 |
| y+s | A:[2k-2,2k+1] | 0 |
| y+v | A:{2k+1} | 0 |
| y+f | A:{2k-2} | 1 |
| t+v | A:{2k} | 1 |
| s+s | C:{3} | 0 |
| v+v | C:{1} | 1 |
| v+z | D:{1} | 1 |

All other unordered pairs among x,b,y,t,d,e,s,v,f,z have empty
intersection with R. This last assertion is a finite endpoint identity,
not an assumed computational result. To check it, for r:[a,b] and
s:[c,d] form

    (r+s mod 6):[a+c+floor((r+s)/6), b+d+floor((r+s)/6)],

subtract 4k when necessary, and intersect the two resulting intervals
with the displayed R interval(s) in that residue. The ten nonempty
results are precisely the table. For example y+f has uncarried row
interval [3k-1,6k-2] in residue 0; its only R intersection after carrying
is the endpoint 2k-2. The pair f+f has carried row interval
[2k-3,4k-3] in residue 2, above C because k>=5; it gives no hit.
This calculation also shows that H+R misses R: in every listed collision
both contributing portions lie outside R.

We now account for all ten collisions using actual lifetimes.

* For x+x to hit A, both rows are k or k+1. These rows occur only in
  blocks zero and one. In block zero, the row-2k pair is the forbidden
  diagonal, and row 2k+1 is absent. In block one neither target row is
  selected. In block two, a strict pair from block one can produce row
  2k+1, which is absent; row 2k again needs the same actual summand twice.
* For x+v, v occurs only initially. The block-zero F targets are absent.
  In block one x has rows k,k+1, giving precisely the absent F rows
  3k,3k+1. Later x rows are too large to hit F.
* For y+y, the initial strict interval is [2k+1,4k-3]; its F targets are
  absent from block zero. An initial y plus a block-one y reaches F
  only at 3k-2, absent from block one. All later combinations are too low.
* For y+s, s is in block one only. Only initial y can hit A, and all
  the resulting A rows are absent from block one.
* For y+v, the hit requires y row 0, present only in blocks one and two;
  the target A row 2k+1 is absent in both those blocks.
* For y+f, the hit requires the two maximal rows 2k-1 and 4k-2. These
  occur in blocks zero and one, respectively. After carrying, the target
  is A row 2k-2 in block two, where it is absent.
* The t+v hit is A row 2k in block two, where it is absent.
* The s+s and v+v hits require the same single actual term twice.
* The v+z hit requires z row 2k, so both inputs are initial. The target
  is D row 1 in block one, where it is absent.

Consequently no selected entry of R can be a distinct sum of T entries.

## Protecting the transient selected entries

Initial entries outside R are subsets of X,Y,v and the first point of Z.
Their protection follows by residue and the first possible sum: the first
strict x+x row is 2k+1, beyond X; the first class-2 row from initial
nonseed pairs is 2k, beyond Y; seed 3 plus B ends at row 2k-1 in class
4, below v, while strict Y+Y starts at 2k+1; seed 3 plus Y likewise
ends at row 2k-1 in class 5, below the first point of Z. All remaining
pair types in these four target classes start above those targets.

The carried portion of P_0 dotplus P_0 in block one is exactly:

| Residue | Row indices |
| --- | --- |
| 0 | [0,k-1] |
| 1 | [0,k-1],{2k} |
| 2 | [2k,3k-1] |
| 3 | [1,2k-1] |
| 4 | {0},[2,2k-2] |
| 5 | [0,2k-2] |

This follows by the same endpoint identity, now using the seven initial
components X,B,Y,{3},E,v,Z and their strict self-sums. It misses all
selected block-one extras: class-0 rows k,k+1; class-2 rows 0,k-1,4k-1;
and class-4 rows 1,4k-2.

Nor can P_0+P_1 without a carry hit those extras. For class 0 rows k,k+1,
the only small seed pairing is 3+D, giving row 1; the next possible
pair Y+s starts at k+2. Other pairs start at 2k or later. Class-2 row 0
is smaller than every possible positive offset sum. For class-2 row k-1,
the smallest remaining possibility X+(2 in block one) starts at k.
For class-2 row 4k-1, the relevant low intervals end at 3k or 4k-2
(the latter from B+B), whereas any use of t, E+G, or v+f starts above
4k-1. For class-4 row 1 the seed pair 3+B already starts at k. For
class-4 row 4k-2, X+s, B+3, Y+y and v+x end at most at 3k+1;
X+f starts at 4k-1, and Z+G starts at 4k+2. All other possibilities
are larger. These comparisons use k>=5. Two block-one entries are too
large to represent a block-one target.

The only block-two extra is class-2 row 0, the actual integer 2m+2.
It is smaller than a sum of two block-one offsets (the least is 2+2),
and smaller than 3 plus any block-two offset. For P_0+P_1 with a carry,
the target uncarried row is 4k in class 2. The preceding class-2 pair
list has low ranges ending at most at 4k-2 and high ranges starting
at least at 5k-1, so it misses this row too. Two block-zero terms sum
to less than 2m. This protects the last extra and proves exclusion.

## Initial coverage

The table below gives all necessary block-zero omissions above g. Each
entry is a row interval in the indicated class. A dot denotes strict
self-sums; every other displayed pair has distinct residue supports.

| r | Available sums and row intervals |
| --- | --- |
| 0 | X dotplus X: [2k+1,4k-1] |
| 1 | X+B: [2k,4k-1] |
| 2 | X+Y: [2k,4k-1] |
| 3 | X+3: [k,2k]; B+Y: [2k,4k-2] |
| 4 | B+3: [k,2k-1]; Y dotplus Y: [2k+1,4k-3]; X+v: [3k,4k] |
| 5 | Y+3: [k,2k-1]; B+v: [3k,4k-1] |

Comparing with P_0 proves the required coverage; in class 4 the selected
row 2k separates the first interval from the second, and in class 5 the
selected Z separates the two intervals.

## Coverage outside the envelope in every positive block

Write U[j] for the actual copy jm+U. The results below are row indices
after subtracting nm. In this section n>=1. The symbols C_j,F_j,A_j
mean the actual entire residue-2, residue-4, residue-0 column of P_j
only when explicitly subscripted; ordinary C,F,A retain their R meaning.

| Target r and interval outside H | Selected pairs giving coverage |
| --- | --- |
| 0: [0,k-1] | B[0]+G[n-1] gives [-k+2,k-1] |
| 0: [2k+2,4k-1], n=1 | X[0]+x[1] gives [2k,3k+1]; B[0]+G[1] gives [3k+2,5k-1] |
| same, n=2 | v[0]+C_2[2] gives [2k+1,3k-1]; X[0]+A_2[2] gives [3k-1,4k-1] |
| same, n>=3 | v[0]+C[n] gives [2k+2,3k-1]; C[1]+F[n-1] gives [3k,5k-4] |
| 1: [0,k-1] | Y[0]+G[n-1] gives [-k+2,k-1] |
| 1: [2k,4k-1] | X[0]+B[n] gives [2k,4k-1] |
| 2: [2k,4k-2] | B[0]+B[n] gives [2k,4k-2] |
| 3: [2,4k-2] | v[0]+G[n-1] gives [2,k]; X[0]+E[n-1] gives [k-1,2k-1]; Y[0]+B[n] gives [2k,4k-2] |
| 4: [2,2k-1], n=1 | Z[0] dotplus G[0] gives [2,2k-2]; 3[0]+B[1] gives [k,2k-1] |
| same, n>=2 | Z[0]+G[n-1] gives [2,2k-1] |
| 4: [2k+1,3k-3] | Y[0]+C[n] gives [k+1,3k-3] |
| 5: [0,2k-1] | X[0]+G[n-1] gives [-k+1,k-1]; Y[0]+3[n] gives [k,2k-1] |
| 5: [3k,4k-1] | v[0]+B[n] gives [3k,4k-1] |

Here x[1] denotes its actually selected interval [k,k+1]. The C_2
row in the second special case includes row 0. For n=1 the expression
Y+C[n] uses the smaller core C, which is already present in P_1;
all other unqualified core symbols used in this table are also selected.
Every claimed interval follows from endpoint addition and the indicated
block carry. Different-block B copies in the class-2 row are distinct.
For n=1, Z and G overlap in the initial block; distinctness removes the
upper endpoint double, which the additional seed-plus-B interval repairs.
For n>=2 those two progressions lie in different blocks.

Two isolated class-4 rows outside H are covered as follows. To obtain
row 0, use X row 2k plus v at n=1; X row k+1 plus F_1 row 3k-1
at n=2; and X row k+2 plus F[n-1] row 3k-2 for n>=3. In each
case the two input rows add to 4k, hence carry to block n. To obtain
row 4k-1, use X row k plus F_1 row 3k-1 at n=1; for n>=2 use
X row k+1 plus F[n] row 3k-2. This completes the complement of H.

## Coverage of missing points inside H

Only the rows listed here are missing inside H above g. We give explicit
selected summands for all of them. Results are again target row indices.

**Class 0.** In block zero the missing row 2k+1 is already covered by
X dotplus X. In block one, Y[0]+s[1] gives [k+2,2k+1]. In block two,
Y[0]+u[1], with a carry, gives [k-1,2k-2]; t[1]+v[0], with a carry,
gives 2k; the two distinct x[1] rows k,k+1 sum to 2k+1. These cover
everything except the selected row 2k-1. For n>=3, Y[0]+F[n-1], with
a carry, gives [-1,2k-3], covering the missing [k,2k-3].

**Class 2.** In block one, X[0]+(2 in block one) gives [k,2k], covering
the missing [k,2k-1]. In block two, X[0]+t[1], with a carry, gives
[k-1,2k-1]. For n>=3, v[0]+F[n-1], with a carry, gives
[k-1,2k-2]; the row 2k-1 is obtained from (2 in block one) plus
A[n-1] row 2k-1. The latter exists already in block two. Row 0 in
block three is s[1]+u[1], with a carry; for n>=4 it is the sum of
Y[0] row 2k-1 and A[n-1] row 2k+1, with a carry. Finally, the
missing high row 4k-1 for every n>=2 is s[1] plus F[n-1] row 4k-3.
That F endpoint is already present in block one because k>=5.

**Class 3.** The only missing relevant H row is row 1 in block one;
it is v[0]+Z[0] at the two rows 2k,2k, with a carry. The inputs have
different residues, so this is a permitted pair.

**Class 4.** In block zero all missing f rows are covered by the initial
table. In block one, Y[0]+y[1], using y[1]=2:[0,k-1], gives
[k,3k-2], covering v's missing
row 2k and the missing f row 3k-2. The other missing f rows 3k,3k+1
are x[1]+v[0]. For n>=2, the missing s row 1 is obtained by a carry
from X row k+2 plus F_1 row 3k-1 at n=2, and from X row k+3 plus
F[n-1] row 3k-2 for n>=3. The missing v row 2k lies in Y[0]+C[n],
whose rows are [k+1,3k-3]. The missing f endpoint 4k-2 is X row k
plus F[n] row 3k-2.

**Class 5.** Only row 2k is missing. In block one it is B[0] row 2k-1
plus s[1] row 1. For n>=2 it is Y[0] row 2k-1 plus D[n] row 1.

Class 1 has no missing H points. Every specified summand is selected
in its declared block. Same-residue factors use different blocks except
for the different entries in x[1] and the pair s[1],u[1]. The latter
have row indices 1 and 3k-1 in residue 4 and differ for k>=5.
All other pairs have different residues or explicitly different actual
entries. Every summand is positive.

This proves that every omitted integer above g is a sum of two distinct
T entries, while the exclusion argument proved no selected entry is such
a sum. T has precisely the two forced seeds at or below g. Chronological
induction therefore identifies T with S(3,6k), proving the proposition.

## Status and checks

During rechecking, the C+F upper endpoint was corrected from 5k-5 to
5k-4. A finite identity check and same-team reading also caught the
initial Z+G overlap: its strict sum ends at 2k-2, not 2k-1. The explicit
3[0]+B[1] witness now covers that omitted endpoint. Neither correction
changes the proposed sequence. These failed intermediate identities are
retained here rather than represented as successful checks.

The tables are written arithmetic identities, with every interval and
boundary witness exposed for human checking. The derivation aid
derive-zero.py examined only the envelope's ten collision types at two
bounded parameter choices; it does not establish any universal claim.
The universal argument above is endpoint algebra for k>=5. A separate
diagnostic is retained as corroboration, not as a premise. Source novelty,
human review, formal verification, and least-period conclusions are not
claimed by this note.
