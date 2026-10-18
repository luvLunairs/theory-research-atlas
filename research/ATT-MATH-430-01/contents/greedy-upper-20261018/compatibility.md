> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Upper-interior compatibility and the defect interaction graph

18 October 2026. Proposed algebraic lemma supporting the upper-interior
greedy proof; contributor checks are not independent verification.

Let k>=1, ceil(f/2)+1<=a<=f-2, f>=5. Put

    Q=2f, d=2a-f-1, b=f-a, m=(3k+1)Q+d.

Equivalently b>=2,d>=1, a=b+d+1, f=2b+d+1. In particular a>=4,
d+2<a, and 2a>f+1. Use cells tQ+[r,s]. Let R comprise

    A_i: cell i, [a,f],                 0<=i<k-1;
    A_(k-1): cell k-1, [a,f+1];
    B_i: cell k+i, [a,2a-1],            0<=i<k;
    C: cell 2k, [a+1,2a-1];
    D_i: cell 2k+1+i, [a+d,2a-1],       0<=i<k.

Define extras E_i in cell k+i with residues [2a,f+a-1], and two
single residues u=2kQ+a and v=2kQ+2a. Set

    H=R union all E_i union {u,v}.

The seed f is already in R. The purpose of H is to permit the true
initial anchors and a finite set of transient defects, instead of
assuming the initial length-f corridor contains the sequence forever.

## Lemma 1: (H+R) mod m is disjoint from R

This ordinary sumset statement even allows equal summands. Therefore
it is sufficient for distinct-summand exclusion as well.

The following tables give the ordinary, unnormalized sum cell and
residue intervals. A denotes all A_i, B all B_i, and D all D_i.
The slightly enlarged upper bound f+1 for all A is harmless except
where the location of that endpoint is explicitly used below.

| Pair | Sum cell range | Sum residue range |
| --- | --- | --- |
| A+A | [0,2k-2] | [2a,2f+2] |
| A+B | [k,3k-2] | [2a,Q+d+1] |
| A+C | [2k,3k-1] | [2a+1,Q+d+1] |
| A+D | [2k+1,4k-1] | [2a+d,Q+d+1] |
| B+B | [2k,4k-2] | [2a,4a-2] |
| B+C | [3k,4k-1] | [2a+1,4a-2] |
| C+C | {4k} | [2a+2,4a-2] |
| B+D | [3k+1,5k-1] | [2a+d,4a-2] |
| C+D | [4k+1,5k] | [2a+d+1,4a-2] |
| D+D | [4k+2,6k] | [2a+2d,4a-2] |

To check the table, sums below m retain their cell and possibly carry
Q from the residue. An uncarried sum is above the selected upper
endpoint in its cell. A carried sum from A+A has residue at most 2;
from A+B,A+C,A+D at most d+1; from B+B,B+C at most 2d. In the last
two cases a carried sum below m lies in a D cell or beyond its final
cell, and 2d<a+d. Thus these carried portions miss R as well.

Sums above m subtract (3k+1)Q+d. After that subtraction, their residue
ranges for the last seven relevant rows are respectively

    A+D: [2a,Q+1],
    B+B: [f+1,Q+d],
    B+C: [f+2,Q+d],
    C+C: [f+3,Q+d],
    B+D: [2a,Q+d],
    C+D: [2a+1,Q+d],
    D+D: [2a+d,Q+d].

The uncarried parts exceed the upper endpoint of every R interval in
the possible cell. For B+B, the reduced uncarried cell is at most k-3,
so the residue f+1 cannot hit the exceptional A_(k-1) endpoint. For
B+C the upper reduced uncarried cell is k-2; for C+C it is k-1.
For A+D it is at most k-2. Carried reduced residues are at most d or
1, below a. A sum in raw cell 3k that crosses m has the same reduced
low-residue description; any part before that crossing and after the
last D cell lies in the empty terminal part of [0,m). No boundary
crossing introduces an additional selected point.

It remains to add the H\R rows.

| Pair | Sum cell range | Sum residue range |
| --- | --- | --- |
| E+A | [k,3k-2] | [3a,Q+a] |
| E+B | [2k,4k-2] | [3a,f+3a-2] |
| E+C | [3k,4k-1] | [3a+1,f+3a-2] |
| E+D | [3k+1,5k-1] | [3a+d,f+3a-2] |
| u+A | [2k,3k-1] | [2a,f+a+1] |
| u+B | [3k,4k-1] | [2a,3a-1] |
| u+C | {4k} | [2a+1,3a-1] |
| u+D | [4k+1,5k] | [2a+d,3a-1] |
| v+A | [2k,3k-1] | [3a,Q+d+2] |
| v+B | [3k,4k-1] | [3a,4a-1] |
| v+C | {4k} | [3a+1,4a-1] |
| v+D | [4k+1,5k] | [3a+d,4a-1] |

For E+A, the only carried residue not strictly below a can equal a.
It requires the upper endpoint f+1 of A_(k-1) and the upper endpoint
f+a-1 of E_i. Their carry lands in cell 2k+i. At i=0 the C interval
starts at a+1; at i>0 the D interval starts at a+d. Neither includes a.
The other uncarried residues here exceed 2a-1.

For E+B, a carried sum below m is at most a+d-1 and lies in a D
cell. For E+C, a carried portion below m can only lie in the empty
terminal cell 3k+1 before m. Above m, E+B and E+C have uncarried lower bounds f+a+1 and
f+a+2 in A cells, and carried upper bound a-1. For E+D, subtraction
of m gives [3a,Q+a-1], missing the relevant A/B cells before carry
and having residue at most a-1 afterwards.

For u+A no carry occurs and every sum exceeds 2a-1. For u+B, the
reduced range is [f+1,f+a] in A cells of index at most k-2; u+C
gives [f+2,f+a] in A_(k-1); u+D gives [2a,f+a] in B cells. Before
reduction their high residues likewise miss R. For v+A the carried
residue is at most d+2<a. For v+B, v+C and v+D the reduced ranges
start respectively at f+a+1, f+a+2 and 3a; the possible carried
residue is at most d+1<a. This proves all remaining exclusions.

## Lemma 2: complete defect-to-R interactions

Modulo m, the only ways two members of H\R can sum into R are:

| Pair | Possible target | Target residue portion |
| --- | --- | --- |
| E_i+E_j, i+j<=k-1 | D_(i+j) | [a+d,2a-2] |
| E_i+E_j, i+j>=k | A_(i+j-k) | [a,f-1] |
| v+E_i | A_i | {a}, using the top of E_i |
| u+u | A_(k-1) | {f+1} |

There are no other hits: u+E_i, u+v and v+v all avoid R.
The last row permits the same residue twice; for actual integers it
requires two different occurrences of u. It must not be silently
discarded until uniqueness of the actual u occurrence is proved.

Indeed E_i+E_j has raw cell 2k+i+j and residue [4a,2f+2a-2].
It always carries Q. If i+j<=k-1, the resulting cell is 2k+1+i+j
with residue [2d+2,2a-2]. If i+j>=k, subtracting m gives cell
i+j-k with residue [d+2,f-1]. Intersections with R give the first
two rows. The latter cell index is at most k-2, and both contributing
indices are strictly larger than it. This is the reverse triangular
dependence used in the extinction proof.

For v+E_i, after reduction and carry the cell is i and the residue
range [d+2,a]; only its endpoint a meets R. It is attained only at
the top of E_i. For u+u the reduced cell/residue is k-1,f+1.
For u+E_i the reduced high range is [f+a+1,Q], whose only carried
point is 0. Finally u+v reduces to cell k-1 and residue f+a+1;
v+v carries to cell k with residue d+2. Both are outside R.

If actual defects are written qm+E_i, the first row carries block
index q+r, the second q+r+1. An initial v plus a block-q E_i hits
block q+1. The u+u row also carries one block after adding its two
block indices. This specifies the temporal shifts, not only residues.

Empty index ranges contribute nothing, including at k=1. The same
inequalities apply there: a negative upper bound for a reduced cell
means that the purported wrapped case cannot occur, not a new cell.

These lemmas do not by themselves prove that the greedy sequence is
confined to H, that u occurs only once, or that extras disappear. Those
are separate obligations in [the upper-interior proof](upper1/proof.md).
The modular computations and the earlier lower-offset defect method
inspired the new reversed ordering. Source period predictions remain
credited to [van Berkel and Bosma](https://arxiv.org/html/2609.18522v1).
