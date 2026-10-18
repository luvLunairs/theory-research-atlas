> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# A shorter uniform coverage argument for the S(3,6k) tail

18 October 2026. Same-team AI scientific draft, requiring full-text human
review and manual submission. Actual service model identity, version and
configuration are unknown. This is a simplification of the retained
[direct proof](../../greedy-analytic-20261018/small/f3-zero.md), not a new
periodicity prediction or an independent verification.

Fix k>=5 and m=24k. Use the candidate blocks and notation in that proof:

    A=0:[2k-2,2k+1], B=1:[k,2k-1], C=2:[1,k-2],
    D=3:[0,1], E=3:{4k-1}, F=4:[3k-2,4k-3],
    G=5:[2k+1,3k-1], R=A union B union C union D union E union F union G.

Here r:[a,b] means {6i+r:a<=i<=b}. The initial anchors are
X=0:[k,2k], Y=2:[k,2k-1], v=4:{2k}, and B; block one contains
the full core subset C[1] and the singleton s[1]=m+10, whose offset
is 4:{1}. Every block j>=3 is R[j]=jm+R by definition of the candidate.
The earlier argument must still establish sum exclusion and coverage in
blocks zero through three. This note replaces only the later coverage
part, without strengthening its theorem or adding a computational premise.

For n>=4 the following table covers the literal complement of R in the
target block. Each right-hand interval is a row interval in the left-hand
residue, after subtracting nm. A carry is specified explicitly.

| Omitted residue and rows | Selected factors, carry, and resulting rows |
| --- | --- |
| 0:[0,2k-3] | Y[0]+F[n-1], carry 1: [-1,2k-3] |
| 0:[2k+2,4k-1] | v[0]+C[n], carry 0: [2k+2,3k-1]; C[1]+F[n-1], carry 0: [3k,5k-4] |
| 1:[0,k-1] | Y[0]+G[n-1], carry 1: [-k+2,k-1] |
| 1:[2k,4k-1] | X[0]+B[n], carry 0: [2k,4k-1] |
| 2:{0} | Y[0] row 2k-1 plus A[n-1] row 2k+1, carry 1: {0} |
| 2:[k-1,4k-1] | v[0]+F[n-1], carry 1: [k-1,2k-2]; C[1]+A[n-1], carry 0: [2k-1,3k-1]; s[1]+F[n-1], carry 0: [3k,4k-1] |
| 3:[2,4k-2] | v[0]+G[n-1], carry 1: [2,k]; X[0]+E[n-1], carry 1: [k-1,2k-1]; Y[0]+B[n], carry 0: [2k,4k-2] |
| 4:[0,3k-3] | X[0]+F[n-1], carry 1: [-2,2k-3]; Y[0]+C[n], carry 0: [k+1,3k-3] |
| 4:[4k-2,4k-1] | X[0]+F[n], carry 0: [4k-2,6k-3] |
| 5:[0,2k] | X[0]+G[n-1], carry 1: [-k+1,k-1]; Y[0]+D[n], carry 0: [k,2k] |
| 5:[3k,4k-1] | v[0]+B[n], carry 0: [3k,4k-1] |

For example, C[1]+A[n-1] has target block n, residue 2, and row
interval [1+(2k-2),(k-2)+(2k+1)]=[2k-1,3k-1]. The adjacent
s[1]+F[n-1] interval has residue 4+4=2 modulo six and one extra
row from that residue addition, hence rows
[1+(3k-2)+1,1+(4k-3)+1]=[3k,4k-1]. No block carry occurs
in either interval. Thus the three intervals for the high residue-two
gap tile it with exact adjacency at both joins.

All other rows follow by ordinary endpoint addition, adding
floor((r+s)/6) and subtracting 4k for the indicated block carry.
In residue zero, the two high intervals are adjacent and their last
endpoint 5k-4 is at least 4k-1. In residue three, the first two
overlap and the third is adjacent. In the low residue-four gap,
k+1<=2k-2 for k>=3, so its two intervals overlap or are adjacent.
The high residue-four interval reaches 4k-1 because 6k-3>=4k-1.
The two low residue-five intervals are adjacent. Every remaining
coverage row consists of a single containing interval. Negative rows
and rows beyond 4k-1 are discarded; these overhangs do not remove
any target in the displayed gap.

There are no distinctness exceptions in this table. One factor is in
block zero or one, and the other is in block n or n-1>=3. Thus they
are different actual integers even when their residues or row values
agree. Every factor belongs to its stated candidate block, including
the isolated residue-two witness, whose A endpoint is present because
n-1>=3. The eleven left-hand intervals are exactly the six residue
classes' omissions from R. Positivity of both factors makes them earlier
than their target. This proves every omission in every block n>=4.

The improvement is organizational but mathematically substantive: the
eventual coverage is expressed in eighteen unrestricted cross-block AP
identities, with no transient endpoint repairs and no same-block overlap
rules. The separate finite treatment of blocks zero through three remains
necessary. The full membership and periodicity theorem continues to depend
on the retained exclusion proof and those early-block arguments.

Checks: all eleven target intervals, eighteen factor identities, endpoint
joins and source lifetimes were rederived from the printed candidate.
No new parameter examples or greedy scans were used. The companion audit
records the exact input versions, remaining scope and provenance. Prose
and data follow the repository's CC BY 4.0 terms.
