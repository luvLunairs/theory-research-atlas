> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# A block-lifetime calculus and finite-defect criterion

18 October 2026. Contributor proof, pending full-text human review. This
reorganizes the exact restricted rectangle identity and chronological
identification argument in the [preceding common lemmas](../greedy-proof-audit-20261018/core-lemmas.md).
It is not a new claim of historical priority. The shared assistance note
records substantive AI assistance and the manual-only submission route.

All intervals below are intervals of integers. Empty inputs give empty
sumsets. Let m>0 and let I be a nonempty interval in [0,m-1]. For a set
of nonnegative block indices A, define the cylinder

    C(A,I) = {am+x : a in A, x in I}.

Its *lifetime* is A. Distinct residues in one block, and equal residues
in different blocks, are distinct actual integers. Both possibilities
must be retained.

## 1. Exact lifetime addition

If I and J are disjoint residue intervals, then

    C(A,I) + C(B,J) = {tm+x : t in A+B, x in I+J}.       (1)

Every pair on the left has distinct actual summands. This follows by
choosing the two block indices and the two residues independently.
The right side is a union before carrying: if x>=m, replace (t,x)
by (t+1,x-m). No endpoint ordering across parameters is assumed.

For one interval I=[a,b] and an interval lifetime A=[l,u], the strict
self-sum is the image of

    [2l,2u] x [2a+1,2b-1],
    [2l+1,2u-1] x {2a,2b},                             (2)

under (t,x) -> tm+x. The same identity holds with u=infinity,
interpreting an unbounded upper endpoint as infinity.

Proof. Unequal residues have exactly the sums [2a+1,2b-1]; the
block-index sum is unrestricted. Equal residues require distinct
block indices, whose sums are exactly [2l+1,2u-1]. Interior residue
sums were already obtained in the first row, leaving the two extreme
doubles. Conversely each displayed value has its indicated distinct
representation. The formula includes singleton intervals and singleton
lifetimes after empty rows have been discarded. QED.

In particular a ray lifetime [h,infinity) has its two endpoint doubles
delayed by one block: the interior sum interval is available from
block 2h, but its extreme doubles only from block 2h+1. This is the
source of several short exceptional transients. Unions of finitely many
lifetime intervals are handled by (1), (2) and ordinary union. For
overlapping representations, first use disjoint actual components.

## 2. Identification with the greedy sequence

Let T be a proposed positive set with precisely f,g at or below g.
Suppose, for every n>g,

    n belongs to T exactly when n is not in T dotplus T. (3)

Then T is the strict greedy sequence. Indeed, every positive summand
of n is smaller than n. Induction on n therefore identifies the
candidate set and the actual earlier choices, and (3) makes the
same decision as the greedy rule. This is a global identity, not
a repeated-prefix observation.

## 3. Finite exceptional residues

Here is a useful form of the mechanism; its hypotheses are substantive
mathematical obligations, not automatically true for a candidate table.
Let R be a set of residues, X a disjoint finite set of exceptional
residues, and let T be a positive set supported on R union X, with
exactly f,g at or below g. Suppose:

1. (R+R) mod m and (X+R) mod m are disjoint from R.
2. Every X residue has an explicitly bounded lifetime in T. The strict
   sums of pairs from those lifetimes are determined by (1), (2).
3. Those exceptional-exceptional sums do not hit the selected R entries,
   and the selected X entries themselves have no distinct representation.
4. Explicit sums of selected entries cover every omitted integer above g.

Then T is the greedy sequence by (3). If, in addition, every R residue
has a final ray lifetime and every X lifetime is finite, T is ultimately
m-periodic. No program certificate or finite continuation theorem is
needed once these four identities and the lifetimes are written out.

For a dynamic version, conditions 1 and 4 confine the sequence to an
envelope and protect its periodic core by chronological induction.
It remains to prove that exceptional lifetimes are bounded, often using
a triangular dependence on strip indices. The bound cannot be inferred
merely from finite residue support or from bounded endpoint values.

The [plateau-corner proof](plateau-corner.md) gives a complete application:
only one eventual residue is hit by a legitimate exceptional pair, and
its last forbidden occurrence follows from [0,1]+[0,1]=[0,2]. Other
branches require their own identities; this criterion alone does not
remove their certificate dependencies.
