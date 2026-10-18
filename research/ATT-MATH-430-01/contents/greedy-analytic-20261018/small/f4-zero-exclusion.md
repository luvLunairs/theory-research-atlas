> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Direct exclusion for the first-seed-four zero-offset family

18 October 2026. Local scientific draft for full-text human review and
manual submission. Actual service model identity/version/configuration
are unknown. Same-team AI mathematical work; no independent verification
or formal approval is claimed.

## Scope, table and arithmetic

Fix k>=6, g=8k, m=32k+1. Let P_0,...,P_5,R be exactly the first table
of the retained [first-seed-four formulas (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material),
and define P_n=R for n>=6, T=union_(n>=0)(nm+P_n). This note proves
that **no selected member of T is a sum of two distinct members of T**.
The complementary global coverage proof is in
[the coverage note](../even-multiples/f4-zero-coverage.md). Together with
the two forced seeds, those two facts identify the candidate by induction.
Neither argument uses a finite-prefix certificate as a premise.

The candidate's period prediction is credited to Daan van Berkel and
Wieb Bosma, [arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1),
Definition 3; the retained and current parent source checks state the
screening limits. The membership table is inherited local research.
The envelope and lifetime proof here is new same-team contributor work.

Notation r:[a,b] means {8i+r:a<=i<=b}, with inclusive row indices.
Every R row is listed below. A carry c=0 or 1 in adding two offsets
from residues r,s produces residue and row interval

    residue = (r+s-c) mod 8,
    rows = [a+d+floor((r+s-c)/8)-4kc,
            b+e+floor((r+s-c)/8)-4kc]                 (1)

for inputs r:[a,b],s:[d,e]. A target block index is the sum of the
input block indices plus c. An interval is intersected with the target
residue's valid offsets before using it; c must be the actual carry.
This matters because m is 1 modulo 8. Distinct self-sums remove the two
extreme endpoint doubles for one actual AP; inputs in different blocks
may have equal row offsets and are still distinct actual integers.

## An envelope and all collisions with the recurring core

The eight recurring components are

    A=0:[2k-5,2k], B=1:[k-3,2k-4], C=2:[0,k-2],
    D=3:[0,k-5], E=4:[4k-4,4k-1], F=5:[3k-2,4k-3],
    G=6:[3k-5,4k-6], J=7:[2k-3,3k-4].

Every selected block lies in the following disjoint thirteen-component
envelope H:

    a=0:[k,2k], b=1:[k-3,2k-1], c=2:[0,2k-1],
    d=3:[0,k-2], e=3:[k,2k-1], t=3:{4k-1},
    s=4:{0}, u=4:[4k-4,4k-1], v=5:{1},
    w=5:[3k-2,4k-1], x=6:{2k},
    y=6:[3k-5,4k-3], z=7:[2k-3,3k-1].

The following table lists every nonempty intersection of an ordinary
H-pair sum modulo m with R. There are only sixteen, among the 91
unordered pairs including self-pairs. All intervals in the second column
are row indices in the named core component.

| Pair | Intersection with R | Carry |
| --- | --- | --- |
| a+a | A:{2k} | 0 |
| a+x | G:[3k,4k-6] | 0 |
| b+e | E:[4k-4,4k-2] | 0 |
| c+c | E:[4k-4,4k-2] | 0 |
| c+e | F:[3k-2,4k-3] | 0 |
| c+v | J:[2k-3,2k] | 0 |
| d+e | G:[3k-5,3k-3] | 0 |
| e+e | G:[3k-5,4k-6] | 0 |
| e+s | J:[2k-3,2k-1] | 0 |
| e+v | A:[max(k+2,2k-5),2k] | 0 |
| e+w | J:[2k-3,2k-2] | 1 |
| e+y | A:[2k-5,2k-3] | 1 |
| e+z | B:[k-3,k-1] | 1 |
| t+x | A:{2k} | 1 |
| v+v | C:{3} | 0 |
| x+x | D:{1} | 1 |

This is an explicit interval identity from (1), not an empirical list.
To check completeness, substitute each of the thirteen H intervals in
(1) and intersect with the eight displayed R intervals. For example
e+y has carried class 0 and rows [-4,2k-3], meeting A in exactly
[2k-5,2k-3]; e+w has carried class 7 and rows [-2,2k-2]. Every pair
not in the table has empty intersection. All comparisons use k>=6.
At k=6 the a+x intersection is a singleton. The maximum in e+v is
necessary at k=6. In every nonempty row both contributing portions lie
outside R; thus the same endpoint calculation also gives (H+R) mod m
disjoint from R.

Here is the lifetime check of every listed possible collision. These
statements refer to the literal P_n table, not an induction assumption.

* **a+a.** Row 2k requires two rows k. They occur only in blocks zero
  and one. A same-block pair repeats an actual summand; the different-block
  pair targets block one, where A row 2k is absent.
* **a+x.** x occurs only initially. Initial G targets are absent. In block
  one, a has rows k,k+1, so the only possible targets are 3k,3k+1;
  both are absent from P_1's class 6. Later a rows are at least 2k-5,
  making their sum with x at least 4k-5, beyond G. More specifically
  blocks two through four have a lower endpoint 2k-2, and block five
  has 2k-4, also beyond the collision range.
* **b+e.** e is initial only. The b intervals in blocks zero through two
  end at 2k-1; any E hits are among 4k-4,4k-3,4k-2, absent in those
  blocks. In block three b ends at 2k-3, allowing only 4k-4, absent
  from P_3. Later b ends at 2k-4 and cannot hit E.
* **c+c.** Only two initial c intervals can reach E. Their strict self-sum
  ends at 4k-3, and its E hits are absent initially. Every pair involving
  a later c interval ends at most at 3k-2, below E.
* **c+e.** Again e is initial. Initial F targets are absent. The block-one
  c interval ends at k-1 and can hit only F row 3k-2, absent from P_1.
  Later c ends at k-2 and gives no hit.
* **c+v.** v occurs only in block one. Only initial c can hit J, producing
  rows at most 2k in block one; J there starts at 2k+1.
* **d+e.** d is absent initially. In blocks one through three d ends at
  k-2; all possible G rows are at most 3k-3, below their class-6 lower
  endpoint 3k-2. In block four only 3k-5 can be hit, while that column
  starts at 3k-4. Later d ends at k-5, too low to hit G.
* **e+e.** Both inputs are initial. Every possible G target is absent
  initially, where the only class-6 entry is x, below G.
* **e+s.** s occurs only in blocks zero and one. The J targets end at
  2k-1 and are absent in both blocks.
* **e+v.** Targets lie in block one and start at k+2. That block's a
  interval ends at k+1, so none is selected.
* **e+w.** The initial w is row 4k-1; its J hits lie in block one at
  rows 2k-3,2k-2, both absent. Block-one w ends at 4k-2 and can hit
  only row 2k-3 in block two, whose class 7 starts at 2k-2. Later w
  ends at 4k-3 and cannot hit J.
* **e+y.** y first occurs in block one. In blocks one through three it
  ends at 4k-3, so the targets in blocks two through four have rows
  2k-5 through 2k-3, all absent there. In block four y ends at 4k-5,
  allowing only row 2k-5 in block five, where a starts at 2k-4. Later
  y ends at 4k-6 and cannot hit A.
* **e+z.** In blocks zero and one z ends at 3k-1; the B targets in
  blocks one and two have rows k-3 through k-1, all absent. Block-two
  z ends at 3k-3, allowing only row k-3 in block three, whose class 1
  starts at k-2. Later z ends at 3k-4 and cannot hit B.
* **t+x.** t occurs only in block one and x only initially. The target
  is A row 2k in block two, where that row is absent.
* **v+v, x+x.** Each component is a single actual term; its repeated
  self-pair is forbidden.

No selected core entry can therefore be a distinct sum of T entries.

## Protecting every transient selected entry

The portions of H outside R and their selected lifetimes are as follows.
An interval is intersected with the indicated actual block column; this
handles k=6 without replacing a shorter interval by a longer one.

| Target component outside R | Selected occurrences |
| --- | --- |
| a_L=0:[k,2k-6] | block 0; intersection with [k,k+1] in block 1 |
| b_H=1:[2k-3,2k-1] | blocks 0,1,2; only row 2k-3 in block 3 |
| c_H=2:[k-1,2k-1] | intersection with [k,2k-1] in block 0; row k-1 in block 1 |
| d_H=3:[k-4,k-2] | blocks 1,2,3; only row k-4 in block 4 |
| e=3:[k,2k-1] | block 0 only |
| t=3:{4k-1} | block 1 only |
| s=4:{0} | blocks 0,1 |
| v=5:{1} | block 1 only |
| w_H=5:[4k-2,4k-1] | row 4k-1 in block 0; row 4k-2 in block 1 |
| x=6:{2k} | block 0 only |
| y_H=6:[4k-5,4k-3] | intersection with P_1 in block 1; all three rows in blocks 2,3; only row 4k-5 in block 4 |
| z_H=7:[3k-3,3k-1] | blocks 0,1; only row 3k-3 in block 2 |

For clarity the finite interval exclusions used below can be checked
against this complete conservative list of potentially relevant H pairs.
All other H pairs miss the indicated target rows by (1). Some listed
pairs have empty intersection for some k; keeping them does no harm.

| Target | Possible pairs; superscript * means one carry |
| --- | --- |
| a_L | d+v, e+v, (e+y)* |
| b_H | a+b, c+z, (t+z)*, (u+x)*, (u+y)*, (w+w)* |
| c_H | a+c, b+b, d+z, (a+t)*, (u+z)*, (w+x)*, (w+y)* |
| d_H | (a+u)*, b+c, (b+t)*, (w+z)*, (x+y)*, (y+y)* |
| t | a+e, v+y |
| s | (a+w)*, (b+u)*, c+c, (c+t)*, (x+z)*, (y+z)* |
| v | (a+y)*, (b+w)*, c+d, (c+u)*, (d+t)*, (z+z)* |
| w_H | a+w, b+u, c+e, c+t, (t+t)*, x+z, y+z |
| y_H | a+x, a+y, b+w, c+u, e+e, (t+u)*, z+z |
| z_H | a+z, b+x, b+y, c+w, (t+w)*, (u+u)* |

The omitted targets e and x occur only initially and are protected with
all other initial entries in the next paragraph. Boundary-only possibilities
such as (y+y)* for d_H and b+y for z_H are intentionally retained.

**Block zero.** Apart from seed 4, the four low progressions in residues
0,1,2,3 start at row k and end at row 2k or 2k-1. Two terms other than the first seed 4
cannot hit these low progressions, except through the double of the
second seed 8k; that pair repeats an actual summand and is forbidden. Adding seed 4 changes these residues to 4,5,6,7 and cannot
hit those low progressions; adding it to any initial high component is
already too large. The initial w_H point has row 4k-1 in class 5:
c+e ends at 4k-2, b+s ends at 2k-1, and all other class-5 pairs start
above it. The initial x has row 2k in class 6: seed-plus-c ends at
2k-1 and the first distinct e+e row is 2k+1. The initial z interval
starts at 2k in class 7: seed-plus-e ends at 2k-1, while a+z and b+x
start at 3k, beyond its upper endpoint 3k-1. All remaining pairs in
these target residues start higher. Thus every initial selected entry
is protected.

**a_L.** Only block one remains, with rows at most k+1. The pair d+v
cannot occur before block two, (e+y)* cannot occur before block two,
and e+v begins at row k+2. None represents the selected rows.

**b_H.** For a+b in target blocks at most three, b starts at k until
block two; in block three its lower endpoint k-2 gives a sum at least
2k-2, above that block's only relevant row 2k-3. For c+z, z initially
starts at 2k or 2k+1, giving rows at least 2k+1 once a later c is used;
the first smaller possibility uses z in block two and c in block one,
targeting block three at row at least 2k-1, again too high. Initial c
has row at least k and gives still larger sums. For (t+z)*, the earliest
targets are block two with row at least 2k and block three with row at
least 2k+1. For (u+x)*, u in blocks zero through two is row 4k-1,
giving target row 2k; lower u first occurs too late. For (u+y)* before
block four, u is row 4k-1 and y starts at 3k-2, giving row at least
3k-2, too high. Finally (w+w)* either uses the initial high w, giving
large rows, or first uses two block-one w intervals: its target block
is three and even its ordinary lower row 2k-1 exceeds 2k-3.

**c_H.** Its only later selected occurrence is row k-1 in block one.
For a+c the smallest possible later c row is 0, but initial a starts
at k. The pairs b+b and d+z have lower rows at least 2k and 2k+1.
The carried pairs (u+z)* and (w+x)*, with both inputs initial, have
lower row 2k. The pairs (a+t)* and (w+y)* cannot occur before block
two. This exhausts the target.

**d_H.** For (a+u)*, using u from blocks zero through two yields rows
at least k-1, above the targets through block three. The first smaller
u, in block three, can target block four starting at k-3, still above
its selected row k-4. For b+c, b initially starts at k; the first lower
b is in block three and must pair with a later c to give a small row,
targeting block four at row at least k-2. For (b+t)* the earliest b
values give rows at least k-1; lower b arrives after this extra expires.
For (w+z)* the smallest possible row in blocks two and three is at
least k-1. In block four the smallest is k-2, from w in block one
and z in block two, still above k-4. For (x+y)*, y in blocks one
through three starts at 3k-2, giving row at least k-1 in target blocks
two through four. Finally, (y+y)* can first target block three; through
target block four both input y intervals start at 3k-2, giving row at
least 2k-3, beyond every selected d_H row. This also covers k=6,7,
where the much wider static envelope admits this pair type.

**t.** Its only occurrence is in block one at row 4k-1. The pair a+e
would have to use block-one a, whose upper row k+1 gives a sum at
most 3k. The pair v+y starts in block two. Neither hits t.

**s.** Its later occurrence is row 0 in block one. A carried pair would
need two initial inputs. For (a+w)* and (b+u)* their row is at least
k-1; for (x+z)* it is at least 1. Initial t and y are absent, excluding
the other carried types. A noncarried c+c sum in block one is at least
k, since one input must be initial. None gives row 0.

**v.** It occurs at row 1 in block one. Initial y,d,t are absent, so
the corresponding carried pair types cannot occur. Initial (b+w)* and
(c+u)* give rows at least k-1. The only potential small carried pair
is initial z+z: distinctness changes its minimum target row from the
forbidden endpoint double 1 to 2. A noncarried c+d pair requires an
initial c and therefore has row at least k. This protects v.

**w_H.** The remaining selected target is row 4k-2 in block one.
For a+w the smallest row is 4k-1; b+u starts still higher. For c+e,
the block-one c ends at k-1, giving a sum at most 3k-2. For c+t,
initial c already makes the sum larger than the target. The pair
(t+t)* starts in block three. For x+z the smallest block-one row is
4k+2; y+z starts at least at 5k-1. All miss the selected row.

**y_H.** The pair a+x uses block-one a only potentially at k=6: its
upper row 3k+1 then equals 4k-5. That row is precisely a hole in P_1's
class-6 column, whose intervals are [3k-2,3k-1] and [3k+2,4k-3].
For k>=7 it is below y_H. In blocks two through four a gives rows
above y_H; later y_H has no selected occurrence.
For a+y through block three the lower row is at least 4k-2; in block
four the first smaller y gives row 4k-4, above its only selected extra
row 4k-5. The pair b+w is at least 4k-2 through block three; in block
four it is still at least 4k-3. For c+u, early u is row 4k-1; the
first smaller u can only target block four at row at least 4k-3.
The pair e+e has only initial targets. For (t+u)* in blocks two through
four, u is still row 4k-1, giving row 4k-2. Finally, z+z has lower
rows at least 4k+2,4k-1,4k-2 in target blocks one,two,three,
respectively. In block four its lower row is at least 4k-3, above
4k-5. Strictness can only increase these safe lower bounds.

**z_H.** In block one a+z and b+x start at least at 3k; in block two
a+z starts at least at 3k-2 and b+x at 3k, above the only selected
extra row 3k-3. The pair b+y starts at least at 4k-2 in these blocks.
For c+w, the smallest block-one row exceeds 3k-1; in block two its
smallest possible row is 3k-1, again above 3k-3. The carried pair
(t+w)* cannot target block one; in block two it gives row 4k-2.
For (u+u)* in these blocks both u inputs have row 4k-1, likewise
giving 4k-2. These bounds protect every later z_H occurrence.

This exhausts the twelve transient portions of H outside R and every
potential pair type. Together with the recurring-core argument, it proves
T intersect (T dotplus T) is empty for every k>=6.

## Checks and limits

The proof uses explicit residue arithmetic and actual block lifetimes;
no observed prefix is extrapolated. The bounded derivation helper
derive-four-zero.py was used to organize the interval intersections,
including the k=6,7 boundary-only pair types. It is not a premise of
the universal argument. Direct same-team checks and any finite diagnostics
are recorded separately. Coverage is a separate substantive obligation,
discharged only when its linked direct proof has also been checked.
