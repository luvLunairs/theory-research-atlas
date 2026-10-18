> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# A direct proof for the plateau corner g=5f+3

18 October 2026. Local analytic candidate proof, pending full-text human
review. The candidate table was developed in the earlier local
[plateau-boundary contribution (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material).
The proof below replaces its two parameter-certificate leaves by explicit
identities for every f>=4, extending the earlier domain by one first seed.
It does not invoke that checker, its pass flag,
or numerical continuation. Credit and AI assistance are recorded in the
shared note. Original text/data use CC BY 4.0.

## Theorem

Let f>=4 be an integer, g=5f+3 and m=15f+5. Define

    F={f},             U={3f+3},
    B=[5f+3,6f+1],     C=[7f+3,8f+2],
    D=[9f+6,10f+2],    E=[12f+4,12f+5],    Z={14f+5},
    v=6f+2,           x_j=9f+3+j  (j=0,1,2),
    H=F union B union C union D union E union Z,
    R=H union U.

For a residue set Y write Y[n]=nm+Y. The strict greedy sequence
initialized by f,g is exactly

    T = union_(n>=0) H[n]
        union union_(n>=4) U[n]
        union {v[0],x_1[0],x_0[0],x_0[1],x_2[0],x_2[1]}. (4)

Here a singleton notation such as v[n] means nm+v. In particular
the sequence is m-periodic from block 4. No assertion of least period
or optimal preperiod is needed.

All intervals contain integers; an interval with reversed endpoints is
empty. All displayed parts are disjoint and contained in [0,m-1] for f>=4.
The set T has exactly f,g at or below g. We prove exclusion and coverage
for every integer above g, then apply the identification lemma.

## 1. Modular compatibility of the permanent residues

The gaps of R in [0,m-1] are exactly

    G0=[0,f-1],        G1=[f+1,3f+2],
    G2=[3f+4,5f+2],   G3=[6f+2,7f+2],
    G4=[8f+3,9f+5],   G5=[10f+3,12f+3],
    G6=[12f+6,14f+4], G7=[14f+6,15f+4].                (5)

The following table lists every ordinary pair sum of the seven parts
of R, reduced modulo m. A union of two intervals denotes the two sides
of a carry. Every row is contained in the indicated gaps; this follows
by comparing the displayed linear endpoints using f>=4. At f=4,
the first interval in the B,D row is empty, exactly as required.

| Pair | Reduced ordinary sum | Gap |
|---|---|---|
| F,F | {2f} | G1 |
| F,U | {4f+3} | G2 |
| F,B | [6f+3,7f+1] | G3 |
| F,C | [8f+3,9f+2] | G4 |
| F,D | [10f+6,11f+2] | G5 |
| F,E | [13f+4,13f+5] | G6 |
| F,Z | {0} | G0 |
| U,U | {6f+6} | G3 |
| U,B | [8f+6,9f+4] | G4 |
| U,C | [10f+6,11f+5] | G5 |
| U,D | [12f+9,13f+5] | G6 |
| U,E | [2,3] | G0 |
| U,Z | {2f+3} | G1 |
| B,B | [10f+6,12f+2] | G5 |
| B,C | [12f+6,14f+3] | G6 |
| B,D | [14f+9,15f+4] union [0,f-2] | G7,G0 |
| B,E | [2f+2,3f+1] | G1 |
| B,Z | [4f+3,5f+1] | G2 |
| C,C | [14f+6,15f+4] union [0,f-1] | G7,G0 |
| C,D | [f+4,3f-1] | G1 |
| C,E | [4f+2,5f+2] | G2 |
| C,Z | [6f+3,7f+2] | G3 |
| D,D | [3f+7,5f-1] | G2 |
| D,E | [6f+5,7f+2] | G3 |
| D,Z | [8f+6,9f+2] | G4 |
| E,E | [9f+3,9f+5] | G4 |
| E,Z | [11f+4,11f+5] | G5 |
| Z,Z | {13f+5} | G6 |

Thus even ordinary sums of R residues avoid R. This stronger statement
allows repeated residues in different blocks without confusing them
with a forbidden equal-actual-integer pair.

## 2. Exceptional residues and the delayed singleton

Put X={v,x_0,x_1,x_2}. All ordinary X+R sums avoid R as well.
For v, the seven reduced sums with F,U,B,C,D,E,Z are respectively

    {7f+2}, {9f+5}, [11f+5,12f+3], [13f+5,14f+4],
    [3,f-1], [3f+1,3f+2], {5f+2}.                    (6)

For x_j, 0<=j<=2, the corresponding sums are

    {10f+3+j}, {12f+6+j},
    ([14f+6+j,15f+4+j] mod m),
    [f+1+j,2f+j], [3f+4+j,4f+j],
    [6f+2+j,6f+3+j], {8f+3+j}.                       (7)

The third expression is contained in G7 union G0; every other
expression is visibly in one of (5). All possible representations
of an R entry must therefore use two exceptional residues.

Their sums are especially simple:

    2v=12f+4,   v+x_j=m+j,
    x_i+x_j=m+(3f+1+i+j).                            (8)

The first value belongs to E, but v occurs only once, so this double
is inadmissible. Among the last values only i+j=2 belongs to R: it
equals m+u, where u=3f+3. The possible pairs are x_0,x_2 and the
double x_1,x_1. The double is inadmissible because x_1 occurs once.
The distinct pair x_0,x_2 has lifetimes {0,1} and {0,1}, so its
block sums are exactly {0,1,2}. Including the carry, it forbids
exactly U[1],U[2],U[3], and no later U entry. U[0] is below g.
This proves that no selected R entry in (4) has a representation.

It remains to check the selected X entries. In block zero each lies
below 2g. A pair not using f has sum at least 2g+1. The possible
seed sums before these entries are F+B, F+{v}, and F+C; their
ranges end at 7f+2 and 9f+2, missing v,x_0,x_1,x_2. Every further
seed sum is at least 10f+3>9f+5. Thus every X[0] entry is unrepresented.

For x_0[1],x_2[1], the R+R table leaves only E+E and U+B as
possible sources. U+B is unavailable, since U first occurs in
block 4. E[0]+E[0] gives only its strict interior point x_1[1];
its two endpoints would repeat the same actual E integer. In (6),
(7), only v+U can hit either target, namely x_2, and again U is
unavailable. Formula (8) gives no X+X representation of either
target. Hence the two selected block-one exceptional entries are
also unrepresented. This completes exclusion.

## 3. Coverage by actual distinct sums

We now give representations for every omitted integer above g.
Each sum uses entries of (4). Intervals of target values are filled
by sliding the summand inside its indicated interval; all cross
parts are disjoint, so the actual summands are distinct.

For n>=1 the gap coverage is as follows. All ranges in the middle
column are offsets in block n. A bracketed index on a set denotes
its block. The fixed entries x_j[0],v[0] may be used arbitrarily
late, which is essential to this coverage proof.

| Gap | Covering ranges | Representations |
|---|---|---|
| G0, n=1 | {0}, {1}, {2}, [3,f-1] | F[0]+Z[0]; v[0]+x_1[0]; v[0]+x_2[0]; v[0]+D[0] |
| G0, n>=2 | [0,f-1] | carried part of C[0]+C[n-1] |
| G1 | [f+1,2f+2], [2f+2,3f+1], [3f+1,3f+2] | union_(j=0)^2 x_j[0]+C[n-1]; B[0]+E[n-1]; v[0]+E[n-1] |
| G2 | [3f+4,4f+2], [4f+2,5f+2] | union_(j=0)^2 x_j[0]+D[n-1]; C[0]+E[n-1] |
| G3 | [6f+2,6f+3], [6f+3,7f+1], {7f+2} | x_0[0]+E[n-1]; F[0]+B[n]; v[0]+F[n] |
| G4 | [8f+3,9f+2], remaining points as below | F[0]+C[n]; E sums as below |
| G5 | [10f+3,10f+5], [10f+6,12f+3] | union_(j=0)^2 x_j[0]+F[n]; F[0]+D[n], B sums and v[0]+B[n] as below |
| G6 | [12f+6,14f+3], [13f+5,14f+4] | B[0]+C[n]; v[0]+C[n] |
| G7 | [14f+6,15f+4] | x_0[0]+B[n] |

Every carried sum in this table has the target block stated: its
two source blocks sum to n-1 and its residue sum crosses m once.
The uncarried sums use source blocks 0,n. All intervals in each row
overlap or touch, as f>=4. In particular the three x_j+D intervals
have length f-3>=1, so they overlap or are adjacent, and their
union is [3f+4,4f+2].

For G4 in block 1, the only omitted extra point is x_1[1], represented
by the two distinct members of E[0]. The endpoints x_0[1],x_2[1]
are selected. For n>=2, the two different blocks E[0],E[n-1]
supply the entire carried interval [9f+3,9f+5]. For G5, the
strict B[0] self-sum fills [10f+7,12f+1] when n=0; when n>=1,
B[0]+B[n] fills the larger [10f+6,12f+2]. In both cases add
F[0]+D[n]=[10f+6,11f+2] in block n and
v[0]+B[n]=[11f+5,12f+3]. These three intervals cover
[10f+6,12f+3]: the middle B interval bridges the apparent gap.

In block zero, only G3 through G7 have any integers above g.
In G3 omit its first point v, which is selected; its remainder is
F[0]+B[0] together with v[0]+F[0]. In G4 use F[0]+C[0],
since all three x_j[0] are selected. The G5, G6 and G7 rows
apply verbatim using the strict B self-sum just explained.

Finally the missing U[1],U[2],U[3] are represented respectively by

    x_0[0]+x_2[0], x_0[0]+x_2[1], x_0[1]+x_2[1].

All omitted integers above g have now been covered, and all selected
integers have been excluded from the distinct sumset. Positivity makes
every representing summand earlier than its target. Induction on the
actual integer therefore proves T=S(f,5f+3). Formula (4) is literally
m-periodic from block 4, proving the theorem. QED.

## Mechanism and scope

The new singleton has a delayed start because two exceptional residues
each survive for two blocks. Their cross-sum lives for three blocks,
and the carry shifts those blocks to 1,2,3. This explains its activation
at block 4 without computing an 11m prefix. The other endpoint delays
come from strict interval self-sums. The proof is the displayed algebra
and chronological identification, not the old certificate. Historical
novelty, least periods, exact starts and independent review are separate.
