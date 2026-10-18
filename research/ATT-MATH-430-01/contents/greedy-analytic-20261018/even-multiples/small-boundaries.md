> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Direct lifetime arithmetic for S(3,12), S(3,18) and S(3,24)

18 October 2026. Local proposed proof for full-text human review and manual
submission. The arithmetic tables were expanded with a same-team AI-authored
helper. This is not independent verification, formal verification, or a
claim of historical priority. The proof obligations and their finite
arithmetic ingredients are written below; no executable pass flag or
finite-prefix continuation statement is a premise.

## Statement and exact candidate

For the strict greedy rule, only sums of two **different actual integers**
are forbidden. The following three sequences are eventually periodic:

| Seeds | Characteristic period | Sufficient start |
| --- | --- | --- |
| `3,12` | `16` | `80=5m` |
| `3,18` | `122` | `244=2m` |
| `3,24` | `96` | `480=5m` |

These are valid periods and sufficient starts; least periods and exact
preperiods are not asserted here. The earlier candidate data are retained
in the [small-first-seed-three bundle (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material).
Their earlier computer-assisted continuation proofs are not used here.
Van Berkel and Bosma's [original sequence definition and predictions](https://arxiv.org/html/2609.18522v1)
and the earlier contributors retain their credit. Current literature and
priority assessment remain with the parent contribution's source review.

For one of the three moduli, a residue `r` has *lifetime* `L_r`, a set
of nonnegative block indices. Define the proposed infinite set directly by

    T = {nm+r : 0<=r<m, n in L_r}.                         (1)

The complete values of `L_r` are the middle column of the
[lifetime table](boundary-lifetime-tables.md). A grouped row assigns the
same lifetime to each listed residue. Every residue occurs in exactly one
row. A singleton such as `1` means `{1}`, `[a,b]` is inclusive, and
`[a,infinity)` is an infinite ray. An empty lifetime is written `-`.
The table is the definition of `T`, not a statement that an observed
prefix has already identified it.

All entries of `T` are positive. The only entries at or below `g` are
`3,g`: this can be read from the rows with lifetime containing zero.
Let `R` be the residues with infinite lifetimes, `H` those with any
nonempty lifetime, and `E=H\R` the finite exceptional residues.
The lifetime tables show that every `R` lifetime has stabilized and every
`E` lifetime has ended by the sufficient start in the statement. It remains
to identify these proposed sets with the greedy sequences for all integers.

## Exact arithmetic used in every table

For residues `r,s`, put `c=floor((r+s)/m)` and `t=r+s-cm`.
If `r!=s`, then all actual summands are distinct, and lifetime intervals
`I=[a,b]` in `L_r`, `J=[d,e]` in `L_s` contribute exactly

    [a+d+c,b+e+c]                                         (2)

to the lifetime of represented target residue `t`. An infinite upper
endpoint remains infinite. If `r=s` but the intervals `I,J` are different
components of its lifetime, they are disjoint block-index sets, so (2)
still gives distinct actual summands. Finally one component `I=[a,b]`
paired with itself contributes exactly

    [2a+1+c,2b-1+c],                                     (3)

with the usual empty-interval convention. For a ray this is
`[2a+1+c,infinity)`. Formula (3) follows from the block-index sums
`q+u` with `a<=q<u<=b`; these fill exactly `[2a+1,2b-1]`.
A singleton lifetime contributes nothing to its own strict self-sum.
These formulas are the singleton-residue specialization of the
[lifetime addition lemma](../lifetime-lemma.md).

Let `Q_r` denote the union of all contributions (2), (3) producing residue
`r`. The third column of the lifetime table gives its value. The following
sections derive the required upper bounds and coverings using the
[complete arithmetic ingredients](boundary-arithmetic-tables.md). In
particular the third column is not left as an unexplained equality claim.

## Upper containment: no sum hits a selected integer

For each case, the first arithmetic table lists every consecutive interval
of `H`, every consecutive interval of `R`, and every complementary gap
`G_i` of `R` in `[0,m)`. Its cell for `[a,b]` and `[d,e]`
asserts the explicit endpoint inclusion

    ([a+d,b+e] mod m) is contained in the listed gap(s).   (4)

There is at most one carry because all residues are less than `m`.
The matrix includes **every** envelope/core interval pair; it permits
equal residues, which only enlarges these safe upper bounds. Each cell
is checked by adding its two displayed endpoints and, when needed,
subtracting the displayed modulus. Thus

    ((H+R) mod m) intersect R is empty.                   (5)

For example at `m=122`, `[18,20]+[102,103]=[120,123]`
reduces into `G14=[120,121]` and `G0=[0,1]`. At `m=96`,
`[52,54]+[42,43]=[94,97]` similarly reduces into
`G16=[94,95]` and `G0=[0,2]`. No inference about lifetime
or actual distinctness is needed for these enlarged bounds.

By (5), a selected core entry can be represented only by two exceptional
entries. The second arithmetic table lists **all nonempty exceptional
pairs whose reduced target lies in R**, together with their exact target
lifetimes from (2), (3). Their unions are:

| g | Core target residue r | Represented lifetime Q_r |
| --- | --- | --- |
| `12` | `2` | `{2}` |
| `12` | `12` | `{2,4}` |
| `18` | `46` | `{0,1}` |
| `18` | `52,68,102,118` | `{0}` each |
| `24` | `9` | `{1}` |
| `24` | `20` | `[2,4]` |
| `24` | `36` | `[1,2]` |
| `24` | `42` | `{1}` |
| `24` | `48` | `[1,3]` |
| `24` | `54` | `[0,2]` |
| `24` | `70` | `{0}` |
| `24` | `76,82` | `[0,1]` each |

Every other core residue has empty represented lifetime. These are exactly
the omissions from the displayed core lifetimes above the forced seeds.
In particular they are disjoint from the selected lifetimes `L_r`.

Two details illustrate the importance of actual distinctness. At `g=18`,
all seven exceptional residues occur only in block zero, so none of their
formal doubles contributes. The pairs `(20,26)` and `(82,86)` reach
residue `46` in blocks zero and one, respectively, after which that core
residue is always selected. At `g=24`, residue `24` has lifetime
`[0,1]`; its strict self-pair gives target residue `48` only in block
one, using the distinct actual terms `24` and `120`. Its formal
same-block doubles are not used.

A representation of a selected exceptional entry itself need not be
controlled by (5). The third arithmetic table therefore treats each
exceptional target separately. For every such target it lists every
nonempty unordered residue-pair contribution, their lifetime unions, and
the resulting `Q_r`. Each row uses the full selected lifetimes, including
every finite component of a core lifetime. Comparing it with `L_r` in
the lifetime table gives `Q_r intersect L_r=empty`. For example at
`g=24`, the only pairs producing exceptional residue `2` are
`(10,88)`, with target lifetime `{3}`, and `(44,54)`, with
target lifetime `[4,infinity)`. Thus its selected lifetime `[1,2]`
is safe. For residue `64`, the three contributions have union
`[0,1] union [4,infinity)`, excluding its selected lifetime `[2,3]`.

The core and exceptional cases exhaust every selected residue. This proves
that no selected actual integer is a sum of two distinct members of `T`.

## Lower containment: every omission has an all-block witness

For a residue `r`, the first block relevant to the greedy decisions is

    b_r=max(0,floor((g-r)/m)+1).                          (6)

Thus the required omitted lifetime is `[b_r,infinity)\L_r`.
For core residues, the exceptional-pair table above supplies exactly the
finite omitted lifetime. For exceptional residues, the complete pair-
contribution table supplies its entire omitted lifetime, including its
infinite part. These claims follow by ordinary unions of the explicitly
listed intervals; they do not require extending a computed prefix.

It remains to cover residues outside `H`. For **each** such residue,
the fourth arithmetic table supplies two selected lifetime components,
their carry, and an infinite covered target lifetime. Formula (2) proves
each ray witness, or (3) when marked `dagger`. Any block from `b_r`
before that ray starts is explicitly listed in the following finite-
witness table, again with both actual lifetime components and their sum.
This is an exhaustive partition of the required block indices for each
never-selected residue.

There are only eleven early repairs over the three cases: one for `g=12`,
one for `g=18`, and nine for `g=24`. For example the `g=18`
ray for residue `76` starts in block one, while its required block-zero
entry is `36+40=76`. For `g=24`, the missing block-one entry
at residue `4` is `48+52=100=96+4`. The same case's two early
entries at residue `72` are supplied by `24+48=72` and
`(96+20)+52=96+72`; its ray begins in block two. All displayed
factors are distinct, including those sharing a residue but using disjoint
lifetime components. The dagger rows explicitly impose different blocks.

Consequently every omitted integer greater than `g` is represented by a
distinct pair from `T`. Combined with upper containment, this establishes
the exact global identity

    x in T iff x not in T dotplus T,     for every x>g.    (7)

All summands are positive and therefore smaller than their represented
target. Induction on `x`, starting with the exactly specified seeds,
identifies `T` with the strict greedy sequence. Its lifetime rays then
give the three stated periodic tails. QED.

## Evidence, limitations and retained failed approach

The complete written proof consists of this note and its two linked
arithmetic tables. The helper [boundary_lifetimes.py (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material)
expanded the finite interval/ray products and selected explicit coverage
witnesses. Its [actual output (historical reference; not a proof premise)](../../../lineage.md#omitted-historical-material) retains every
unmerged contribution, rather than only a final Boolean outcome. It reads
the three existing candidate tables; it performs no new greedy sequence
scan or enlarged parameter search. Those prior tables suggest the candidate
lifetimes, but correctness of their earlier continuation computations is
not assumed in (1)--(7).

The first implementation attempt used an incorrect relative input root and
stopped with `FileNotFoundError` before scientific calculation. The path
was corrected; no mathematical outcome was inferred from that failed run.
The helper's exact arithmetic was checked against the displayed definitions,
including strict same-residue sums, singleton lifetimes and carries. The
worker read the written tables, checked the exceptional interactions and
coverage repairs, and rechecked their relation to the chronological greedy
criterion. The matrices and witness lists expose the finite arithmetic
for further full-text checking. Their generation is disclosed; they are
not described as an independent computation or a proof assistant result.

This is a direct arithmetic closure of three fixed exceptional seed pairs,
not a new parameter family and not a claim that their periods were unknown.
The unbounded variable in the argument is the block index, handled exactly
by interval and ray addition. The parent separately supplies the uniform
families. The combined proof remains a local scientific draft, with human
review and manual submission required. Service-supplied model identity,
version and configuration are unknown. Prose/data use CC BY 4.0 and code
uses MIT under the repository terms.
