> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Analytic domain extensions that remove small-seed certificates

18 October 2026. Local contributor proof, pending human review and manual
submission. These are extensions of the explicitly linked earlier local
analytic arguments, not extrapolations from their diagnostic runs. Only
eventual periodicity and the indicated membership conclusions are used.
Least periods and exact transients are deliberately outside this note.

## 1. Odd multiples for every f>=3

The complete membership statement and proof in
[odd-multiple-proof.md](../greedy-unified-20261018/odd-multiple-proof.md)
remain valid for every integer f>=3 and k>=1, with

    g=(2k+1)f,       m=(6k+3)f-1.

Use its exact P,R,H_i,F_i,D,E_i,u,v and B_i definitions. In particular
R is supported on odd f-cells, with within-cell intervals

    {0} (i<=k-2), [0,1] (i=k-1), [0,f-2] (i=k),
    [0,f-1] (k+1<=i<=2k-1), [1,f-1] (i=2k),
    [f-2,f-1] (i=2k+1), {f-1} (i>=2k+2).

The exact greedy set is P in block zero and R in every positive
m-block. Here is a check of every place where a smaller f could
alter that proof.

* These runs are nonempty, disjoint and separated for f>=3. The
  reflection H_(3k-i)=f-1-H_i still holds, including k=1.
* In an unwrapped R+R sum, a carry with an index k-1 has coordinate
  zero at a target index at least 2k+1, which excludes zero because
  f-2>=1. When both indices are k, the carry coordinate is at most
  f-4, strictly below f-2. If f=3 this upper bound is negative,
  meaning no carry is possible, not that a negative coordinate is
  selected. At larger indices the carried coordinate is at most f-2,
  whereas the target is {f-1}. These are all unwrapped collision
  cases, and reflection excludes wrapped ones.
* The u+R exclusions need respectively 0<1, f-3<f-2, and f-2<f-1.
  Its wrapped values lie in even cells because the relevant r>=1.
  The v+R exclusions need r+1>=2>1 and r+1>=f-1>f-2; if r=f-1,
  a further f-cell carry makes the cell even. Each inequality holds
  at f=3. The sole exceptional pair is u+v=m. Initial u and v
  remain respectively below f+g and below every two-anchor sum.
* All ordinary interval sums and the restricted F_0/F_k self-sums
  in the gap proof remain nondegenerate. The first high gap is
  covered by f+F_k and F_0 dotplus F_0; their endpoints overlap
  because f>=2. The exceptional block-one gap after A_* is filled
  by F_k dotplus F_k and F_0+e. Their overlap is again guaranteed
  by f>=2. Every other covering range is an exact indexed sum;
  its endpoints do not use f>=5.
* The missing B endpoints are still covered by v+D[n-1] and
  F_0+A_*[n], with distinct actual factors. At k=1 the two repairs
  lie in the same gap and overlap as in the original proof. The
  final high gap starts with v+B_0[n], and F_0+B_k[n] completes
  it; B_0 and B_k each have f-1>=2 entries.

Thus the exclusion and complete gap coverage in that proof hold
unchanged for f>=3. Positivity and the seed guards identify the
candidate with the greedy sequence. This proves the extended statement.
It covers all S(3,6k+3) and S(4,8k+4), including k=1. The old
primitive-period argument uses distinct run lengths and is not imported:
for example at f=3,k=1 the sufficient period 26 is not least.

## 2. The high plateau at f=4,b=3,k>=3

Use the H,R,F_i,D,E_i,u,V,W_i definitions of the
[high-plateau proof](../greedy-upper-20261018/upper2/proof.md), and the
chronological argument in [Proposition U2](../greedy-proof-audit-20261018/upper-audit.md).
Their eventual-periodicity conclusion extends to f=4,b=3,k>=3:

    g=8k+7,       m=24k+17,
    every block n>=2 is exactly R.

The reason the previous f>=5 restriction can be relaxed in this
particular domain is explicit. B_2 has component lengths 0 and 1;
it is a singleton, but no gap-coverage step uses it as the full
anchor. The last run B_k, because k>=3, has two surviving endpoint
components of length 1 separated by a two-point hole. Adding any
full F interval of length 4 fills the same entire sum interval as
adding the full F_k: the two resulting intervals overlap. B_0 has
length 3 and B_1 is the full length-4 interval.

The six envelope collision calculations continue to hold: their
only high-cell parity comparison uses an absolute residual discrepancy
at most 2, strictly less than f=4. The two possible F+F crossings
adjacent to the seed end at f-1 and start at f+1. Their sole collision
with R is still u+u, at the lower endpoint of D. The chronological
induction excludes every repeated u by min(F_k)+min(D[n-1]),
simultaneously protecting R and confining the sequence to H.

For gap coverage, the initial interval joining uses only b<=f-1,
which is equality here. In positive blocks the full last-run convolution
just proved gives I_i=[(2i-1)f+1,(2i+1)f-1]. The J_i intervals
in the original proof fill the odd-cell gaps and the two lost endpoint
doubles in the first block, using precisely b>=3 and b<f; both hold.
The F gaps use the protected seed and B_0, and the high gaps use
the full B_1. No use is made of a second point in B_2.

Finally D+E_(i-2)[n-1] removes each W_i from block 1, and
D[0]+D[n-1] removes all of V for n>=2, using distinct blocks.
All other entries are already determined by the chronological induction.
This proves the claimed fixed tail. It does not need the stronger
assertion that both V endpoints survive in block 1.

The excluded k=2 case is exactly S(4,23); it is covered instead by
the new [plateau-corner theorem](plateau-corner.md), valid for f>=4.
Extending that corner table to f=3 is false: its eventual U residue
would be 12 and its C interval [24,26], so two distinct late translates
of U would sum to a selected C translate. This is a counterexample
to the proposed extension, not to ultimate periodicity.

## The first quotient band and its two boundaries

The complete [band and transition proof](../greedy-lower-20261018/lower/proof.md)
and [endpoint proof](../greedy-lower-20261018/endpoint-proof.md) also
have weaker hypotheses for membership than their stated f>=5 domains.
Only their membership and sufficient-period conclusions are used here.
The following relaxations require no program certificate:

| Formula | New domain | Sufficient period |
| --- | --- | --- |
| Band, g=2f+j | f>=3, f<=j<=2f-1; also (f,j)=(2,3) | 7f+2j-1 |
| Transition, g=3f-1 | f>=4 | 9f-3 |
| Endpoint, g=4f | f>=4 | 11f-1 |

Here is a check of the boundary conditions in the complete arguments.
In the band proof, all 18 ordinary regular and exceptional sum intervals
still avoid R: A+A needs 2f+2<=2f+j-1, hence j>=3;
A+C needs 6f+j<=6f+2j-3, again j>=3; B+D starts
in its gap provided f+j-1>=f+2; and D+D starts in its
gap provided 5f+2j-3>=5f+j. These are the same condition.
The remaining containments need only f>=2, j>=f and j>=3.
The distinct exceptional pair is still u+v=m, and the original
size exclusions of the targets u,v are unchanged.

The initial omitted middle interval is filled because
4f+2j+1<=6f+j, exactly j<=2f-1. In a positive block
the G1 and G3 bridges use this same upper bound or its weaker
versions. All other gap endpoints are exact identities. Initial B,C
have length f>=2, so their restricted self-sums are nonempty.
Tail B,C may be singletons at (f,j)=(2,3), but the proof uses
them only with disjoint actual intervals. The low-gap crossing interval
starts at or below the target block boundary: equality occurs at f=2,
j=3. Thus the old phrase "starts below" is replaced by "starts at
or below" for this extension. The full initial and positive-block
coverage argument remains valid. In particular it proves S(2,7),
S(3,9), S(3,10), S(3,11), and S(4,12),...,S(4,15).

For the transition at f=4, the tight new comparison is
A+A=[6,10]=G1. Every one of the 22 displayed regular/exceptional
rows remains in its indicated gap; C has length two. The three
distinct exceptional sums still hit gaps or the omitted block-one
A endpoint. Every initial and positive-block coverage identity is
unchanged, and each required self-sum uses an initial interval of
length four. This proves the transition membership formula at f=4,
and in particular settles S(4,11).

For the endpoint at f=4, all 15 regular-pair intervals and all
15 exceptional/regular intervals still lie in their indicated gaps.
The tightest formerly strict separation is the lower endpoint of
E+E after carrying: 9f-3=8f+1, exactly the first point of G4.
All three exceptional cross pairs remain absent; the delayed A
endpoint is still absent in block one. B has two entries, C three,
and E two, so every coverage sum and strict initial self-sum has
the stated extent. The G1 missing endpoint is still repaired by
u+D_0. Thus the endpoint formula proves S(4,16).

The endpoint extension to f=3 is false: the same carried E+E
lower endpoint becomes 9f-3=8f, the selected D residue.
Two distinct late copies of min E then give a selected D translate.
This obstruction explains why S(3,12) is not covered by that formula.
None of these relaxations imports a least-period argument: at small
seeds a displayed sufficient period can be a multiple of the least one.

## Scope of the reductions

Together with the new upper boundary/ray proofs and the separately
checked offset-one relaxation, these arguments remove most of the
small-seed certificate branches. They do not settle the changed-shape
families S(3,6k), S(3,6k+1), or S(4,8k), and do not by themselves
handle all finite exceptions. Those obligations are discharged by the
separate direct proofs and fixed-lifetime arguments linked in the final
[coverage map (historical reference; not a proof premise)](../../lineage.md#omitted-historical-material).
