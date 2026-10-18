> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Odd multiples: a proof uniform in the seed and the quotient

18 October 2026. Proposed scientific result, pending full-text human review
and manual submission. This is an AI-assisted contributor argument, not
independent verification or a novelty claim. Integer intervals are inclusive.

## Statement

For every pair of integers f>=5 and k>=1, set g=(2k+1)f and

    m=(6k+3)f-1=3g-1,       p=(k+1)f+2k.

The proposed theorem gives the complete strict greedy sequence S(f,g),
where each new term avoids sums of two distinct earlier entries. Its
least characteristic period is m, its least gap period is p, characteristic
periodicity begins at N=(4k+1)f+1, and the least gap preperiod is kf+2.
Both f and k are unbounded. In particular the result has no upper bound
on g/f. The k=1 specialization was already covered by the previous local
plateau draft; the present argument addresses all k with the same rules.

The period value is the specialization a=f of Definition 3(4) and
Conjecture 5 in Daan van Berkel and Wieb Bosma,
[*Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1).
It is not a new period prediction. The explicit set and uniform proof
are proposed here; the shared literature note controls novelty limits.

## A single description using f-sized cells

Define intervals H_i for integer indices 0<=i<=3k:

| Index i | H_i |
| --- | --- |
| 0<=i<=k-2 | {0} |
| i=k-1 | [0,1] |
| i=k | [0,f-2] |
| k+1<=i<=2k-1 | [0,f-1] |
| i=2k | [1,f-1] |
| i=2k+1 | [f-2,f-1] |
| 2k+2<=i<=3k | {f-1} |

An empty index range contributes nothing. Put

    R = union over i=0,...,3k of ((2i+1)f + H_i).

Thus only odd f-cells can contain members of R. For the initial block put

    F_i=[(2k+1+2i)f,(2k+2+2i)f-1],       0<=i<=k,
    D=[(4k+4)f-2,(4k+4)f-1],
    E_i={(4k+4+2i)f-1},                    1<=i<=k-1,
    P={f} union F_0 union ... union F_k union D union E_1 ... union E_(k-1).

The claimed full sequence is

    T = P union union over n>=1 of (nm+R).                    (1)

All sets lie in their declared m-blocks and are separated by nonempty
gaps when f>=5. P contains exactly f,g at or below g. Relative to R,
the initial block has just two extra points

    u=(2k+2)f-1,     v=(4k+1)f,

and omits the early cells below g except for f. The set R is symmetric:

    H_(3k-i)=f-1-H_i,       m-R=R.                           (2)

## Exclusion of every distinct sum

First prove (R+R) mod m is disjoint from R, even allowing equal residues.
Write x=(2i+1)f+r and y=(2h+1)f+s with r in H_i and s in H_h.
Their uncarried cell index is even. If x+y<m, a selected odd cell is
possible only when r+s>=f; its index in the H-table is t=i+h+1 and
its within-cell coordinate is r+s-f. A hit would require t<=3k.

If either i or h is at most k-2, its coordinate is 0 and no carry occurs.
If one index is k-1, its coordinate is at most 1. The only possible
carry has coordinate 0 and the other index at least k+1, giving
t>=2k+1, where H_t excludes 0. If both indices are at least k, then
t>=2k+1. Equality forces i=h=k and the carried coordinate is at most
f-4, below H_(2k+1)=[f-2,f-1]. If t>=2k+2, H_t={f-1}, whereas
every carried coordinate is at most f-2. Thus no unwrapped sum hits R.
For x+y>=m, apply (2): (m-x)+(m-y)=2m-(x+y)<=m. A positive wrapped
hit in R would give an unwrapped hit in R by reflection; residue zero
is not selected. Hence the assertion holds in all cases.

Next pair u or v with a residue x=(2i+1)f+r in R. For u, an unwrapped
carry has coordinate r-1. If i=k-1 it is 0 in H_(2k), which excludes 0;
if i=k it is at most f-3 in H_(2k+1); if k+1<=i<=2k-1 it is at
most f-2 in a cell selecting only f-1. Smaller indices do not carry.
When i>=2k the sum wraps and, since r>=1, its reduced f-cell is even.
These cases exclude (u+R) mod m from R.

For v, all unwrapped sums remain in even cells. A wrapped sum with an
odd cell has coordinate r+1 and index t=i-k-1. When k+1<=i<=2k-1,
the target H_t={0}; when i=2k, H_t=[0,1] but r+1>=2; when i=2k+1,
H_t=[0,f-2] but r+1>=f-1. Larger indices have r=f-1, so the extra
carry makes the reduced cell even. The case i=k can only wrap to
residue zero. Thus (v+R) mod m also avoids R.

The only distinct exceptional pair is u+v=m, which is absent. Finally,
exceptional targets themselves are safe: u=f+g-1 is below the least
possible distinct sum f+g. Below v the only selected terms are f and
F_0,...,F_(k-1). Their sums with f end at v-1 and occupy even f-cells;
sums of two terms from the F intervals are at least 2g>v. Therefore
v cannot be a distinct sum either. This proves that T is sum-free for
distinct summands, including every initial exception.

## Coverage of every omitted integer

Ordinary sums of disjoint integer intervals fill the interval between
their endpoint sums. Distinct self-sums of [a,b], a<b, fill
[2a+1,2b-1]. We use only these identities and positive summands.

In block 0 above g, the gaps between F_i and F_(i+1), 0<=i<k,
are exactly f+F_i. After F_k, the gap

    [(4k+2)f,(4k+4)f-3]

is covered by f+F_k and distinct F_0+F_0. After D and the succeeding
singletons E_i, each gap is covered by F_0+F_(i+1), for 0<=i<=k-1:

    F_0+F_(i+1)=[(4k+4+2i)f,(4k+6+2i)f-2].                (3)

The last such interval continues past m-1 and covers the final high
gap. These are precisely all omitted integers of block 0 above g.

For subsequent blocks use notation B_i for the tail version of F_i:

    B_0=[(2k+1)f,(2k+2)f-2],
    B_i=F_i for 1<=i<=k-1,
    B_k=[(4k+1)f+1,(4k+2)f-1].

Write X[n]=nm+X for a tail run X. In block 0, use the corresponding
F_i rather than B_i. Let A_*=[(2k-1)f,(2k-1)f+1] and e=m-f;
e is in D if k=1, and is E_(k-1) otherwise. In every block n>=1,
the following list covers the complement of R, with offsets relative to nm.

* **Low gap [0,f-1].** F_0+B_k[n-1] carries into block n and ends
  at nm+f-1. For n=1, F_0+F_k does the same. When k=1 the first
  selected run is [f,f+1]; when k>1 it is {f}; the low gap is unchanged.
* **Gaps between the early singleton cells.** For 1<=i<=k-1,
  F_k+B_i[n-1] equals
  nm+[(2i-1)f+1,(2i+1)f-1]. The block-0 version is F_k+F_i.
  The indices i<k ensure distinct intervals even when n=1.
* **Gap after A_*.** It is [(2k-1)f+2,(2k+1)f-1]. For n>=2,
  F_k+B_k[n-1] fills it exactly. For n=1 the distinct self-sum
  F_k+F_k covers through the penultimate endpoint; F_0+e supplies
  the remainder, since F_0+e=m+[2kf,(2k+1)f-1]. These intervals
  overlap or are adjacent.
* **Gaps between the long B runs.** F_i+{nm+f}, 0<=i<=k-1,
  covers [(2k+2+2i)f,(2k+3+2i)f-1]. The missing lower endpoint
  u in the first gap is supplied by v+D[n-1], which covers
  [(2k+2)f-1,(2k+2)f]. The missing last endpoint v before B_k
  is supplied by F_0+A_*[n]=nm+[4kf,(4k+1)f]. For k=1 these
  two endpoints belong to the same gap; the displayed intervals
  still overlap and cover it.
* **After B_k through the high end.** F_0+B_0[n] covers
  [(4k+2)f,(4k+4)f-3]. For 1<=i<=k-1, F_0+B_i[n] covers
  [(4k+2+2i)f,(4k+4+2i)f-2], leaving exactly D and the E
  singletons between consecutive intervals. The remaining first
  integer (6k+2)f of the last high gap is covered by v+B_0[n].
  F_0+B_k[n] covers from (6k+2)f+1 through m+f-1, completing
  the high gap and the next low gap.

All pairs use disjoint actual intervals or explicitly restricted self-sums.
In particular the early seed in the long-gap row is the selected translate
nm+f, while F_i is an initial interval; no unavailable translate of an
exception is assumed. Crossing sums use only their portion in the stated
block. Each gap in the H-table is accounted for, for every n and every k.

Every omitted integer above g is therefore a sum of two distinct members
of T. Both are positive and smaller than their sum. Together with sum
exclusion and the forced seeds, induction proves (1) is exactly S(f,g).

## Least periods and exact transient

The cyclic run-length word of R is

    1^(k-1), 2, f-1, f^(k-1), f-1, 2, 1^(k-1).

Here exponents denote repetitions of run lengths, not powers. Since f>=5,
lengths 1,2,f-1,f are distinct. Exactly one length-2 run is followed by
a length-(f-1) run; the other is followed by a singleton if k>=2 and
by the other length-2 run if k=1. This unique circular marker prevents
any proper repetition, so m is primitive. Summing the run lengths gives
p=(k+1)f+2k. A shorter gap period would yield a characteristic period
containing fewer than p selected points, contradicting primitivity.

The last discrepancy between P and the periodic extension is v=(4k+1)f,
present initially but absent at every positive m-translate. Hence the exact
characteristic start is v+1, even when another eventual period is allowed:
every eventual period is a multiple of primitive m. Before v+1 there are
the seed f, k full F intervals and v itself, totaling kf+2 entries.
The incoming gap to v+1 is 1; its translate in the tail is f+2 for k>=2
and f+3 for k=1. Every later gap agrees with the tail. Thus the least gap
preperiod is kf+2, with d_0=g-f.

## Status and limitations

Small examples suggested the formula. No finite upper limit on k occurs
in the proof: the f-cell carry argument and indexed covering identities
quantify over all allowed indices. Diagnostics are secondary checks.
The general seed pair, offsets away from a=f, and the midpoint extinction
problem are not settled by this theorem. This draft must receive full-text
human screening, independent mathematical assessment and priority checking.
Actual service model identity/version/configuration are unknown and covered
by the shared assistance note. Original text/data use CC BY 4.0, code MIT.
