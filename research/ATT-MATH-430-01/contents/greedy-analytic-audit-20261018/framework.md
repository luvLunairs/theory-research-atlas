> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../assistance-and-checks.md).

# Strict sums, lifetime identities and finite extinction

18 October 2026. Mathematical consolidation for the candidate proof.
This supplies reusable proofs of the repeated steps; its applications
still require the explicit family-specific interval identities. All
intervals contain integers. Empty intervals and empty index ranges
contribute nothing. No program result is a premise.

The earlier [lifetime calculus](../greedy-analytic-20261018/lifetime-lemma.md),
[lower lemma](../greedy-proof-audit-20261018/lower-lemma.md),
[midpoint lemma](../greedy-proof-audit-20261018/midpoint-lemma.md), and
[upper chronological arguments](../greedy-proof-audit-20261018/upper-audit.md)
are the immediate local sources of these reformulations. The conventions
and precise two-seed conjecture used here follow Daan van Berkel and
Wieb Bosma, [arXiv:2609.18522v1](https://arxiv.org/html/2609.18522v1).
Their [companion paper, Section 2](https://arxiv.org/html/2609.16843v1#S2),
records Queneau's earlier non-additive formulation; that historical
original remains uninspected here.
No historical originality claim is made. The shared assistance note
discloses substantive same-team AI work.

## 1. The exact diagonal-deletion lemma

For sets A,B of integers put

    A dotplus B = {a+b : a in A, b in B, a != b}.

This is symmetric even when A and B overlap. Different labels do not
make two actual integers different.

**Lemma 1.** Let I=[a,b] and J=[c,d] be nonempty intervals, possibly
unbounded above. For a fixed integer t, the possible first summands in
an ordinary representation t=x+y, x in I, y in J, form exactly

    K_t = [max(a,t-d), min(b,t-c)].                         (1)

Consequently t is lost on passing from I+J to I dotplus J exactly
when K_t is the singleton {t/2}. If both intervals contain at least
two integers, the only possible losses are 2a when a=c and 2b when
b=d is finite. If I={a}, then I dotplus J=(a+J) minus {2a};
the same statement holds with the factors interchanged.

**Proof.** Solving c<=t-x<=d together with a<=x<=b gives (1).
Every feasible x except x=t/2 gives different summands, so a sum can
be lost only in the stated singleton case. Suppose both intervals
contain at least two integers and K_t={z}, t=2z. Its lower endpoint
equals z only if z=a or z=d; its upper endpoint equals z only if
z=b or z=c. The combinations a=b and c=d are excluded. The other
two combinations give the common lower endpoints a=c=z or the common
finite upper endpoints b=d=z. Conversely those common extreme sums
have only the repeated-endpoint representation. The singleton formula
is immediate. QED.

In particular,

    [a,b] dotplus [a,b] = [2a+1,2b-1]                     (2)

when a<b; it is empty for a=b. The ray version is [2a+1,infinity).
The lemma includes nested overlapping intervals, which need not lose
both endpoints. It also explains why an unrestricted claim that only
extreme sums are lost is false when one factor is a singleton:
{2} dotplus [1,3]={3,5}, with the interior sum 4 removed.

## 2. Block coordinates and distinct actual integers

Fix a positive modulus m and use canonical residues 0<=r<m. The map
(q,r) -> qm+r is injective for q>=0. Thus two actual entries differ
if their block indices differ or their residues differ. These are
sufficient alternatives, not conditions that must both hold.

For sets A of block indices and I of residues write

    C(A,I)={qm+r:q in A,r in I}.

**Lemma 2.** The strict sum of any two such cylinders is the image,
under (n,s)->nm+s, of

    ((A dotplus B) x (I+J)) union ((A+B) x (I dotplus J)). (3)

The statement is valid for overlapping A,B and I,J. The image is
taken before carrying s into [0,m); duplicate images are simply united.

**Proof.** An unequal actual pair has unequal block indices or unequal
canonical residues. In the first case its coordinate sum belongs to
the first product, in the second to the second product. Conversely,
either product supplies different actual integers. The block-index and
residue choices are independent inside a cylinder. QED.

For a nonempty single rectangle with l<=u and 0<=a<=b<m,
A=[l,u], I=[a,b], (3) reduces to the image of

    [2l,2u] x [2a+1,2b-1],
    [2l+1,2u-1] x {2a,2b}.                               (4)

If either input interval is empty, the sum is empty and (4) is not
applied. Empty output rows are discarded, and the obvious infinite-endpoint
convention applies. The two extreme doubles are available one block later than
the interior sums on a ray. Formula (3), rather than an ordinary product
sum, is the general rule when components overlap or become singletons.

There is a useful version for arithmetic progressions. Write m=dL+e,
where 0<=e<d. An offset component r:[a,b] denotes
{di+r:a<=i<=b}, with all its actual offsets in [0,m). Adding components
in blocks q,p and choosing carry c in {0,1} gives target block n=q+p+c,
residue class t and row interval

    t=(r+s-ce) mod d,
    [a+u-cL+floor((r+s-ce)/d),
     b+v-cL+floor((r+s-ce)/d)].                           (5)

Intersect with the target block mask. If the two actual progressions
are disjoint, this is the ordinary interval sum. If they are in the
same block and class, apply Lemma 1 to their row intervals. In particular
m=32k+1,d=8 gives the minus-one residue shift in the first-seed-four
tables. Formula (5) follows directly by subtracting cm; it is not a
heuristic carry rule.

## 3. A global greedy identification theorem

For each residue r choose a set L_r of nonnegative block indices and
let T={qm+r:q in L_r,0<=r<m}. Require T to be positive and to contain
exactly the forced seeds f,g at or below g. Define the scanned-block set

    D_r={q>=0:qm+r>g}.

It is a ray starting at max(0,floor((g-r)/m)+1). For each r define
the exact possible sum lifetime

    Q_r = union over 0<=a<=b<m, (a+b) mod m=r of
          (L_a + L_b + floor((a+b)/m))             if a<b,
          (L_a dotplus L_a + floor(2a/m))           if a=b.  (6)

**Theorem 3.** Under the positivity and seed conditions, T=S(f,g)
if and only if, for every r,

    Q_r intersect D_r = D_r minus L_r.                    (7)

If each L_r is eventually either a full ray or empty, this identity
proves eventual m-periodicity.

**Proof.** Canonical residues are unique. Different residues in (6)
always represent different actual integers; equal residues require
different block indices. Hence (6) is exactly the lifetime of T dotplus T.
Equation (7) is equivalent to the exclusion and coverage of every
integer x>g. Starting just after the forced seeds, induct on x.
Every positive summand of x is strictly smaller than x. Once the
candidate and the actual greedy sequence agree below x, (7) makes
the same decision at x. The seed guard gives the base case. The
converse follows from the same positivity observation applied to the
actual greedy sequence. Eventual ray/empty lifetimes give a fixed
characteristic word beyond their finitely many starting points. QED.

For nonempty lifetime intervals [l,u] and [v,w], all cross-component sums are
[l+v,u+w]. On a self-component use [2l+1,2u-1]. Decompose a union
of intervals into disjoint components first. This evaluates (6) by
finite interval arithmetic for all block indices, including infinity;
it does not prove an infinite claim from a finite prefix.

The long fixed-case tables can consequently be read in four steps:
verify all L_r and the seed guard; compute all source-pair intervals;
unite them to obtain Q_r; check (7). Extra ray witnesses are an alternative
way of proving the coverage inclusion. Rechecking a software transcription
is useful but is not one of these mathematical premises.

## 4. Lifting finite anchor identities to every later block

**Lemma 4.** Suppose T is a proposed positive set with a fixed residue
row R for all blocks n>=N. A coverage identity valid in every block
n>=N+1 may use a fixed initial component and a component of R in
block n or n-1. If its carry and offset sum interval are fixed, and
these intervals cover each omitted residue interval, it covers every
later omission. The factors are different actual entries whenever the
initial component is in block zero and N>=1. Any earlier coincident-block
case must instead use Lemma 1 or disjointness explicitly.

**Proof.** The factors belong to the candidate for all the asserted
block indices by its definition. Subtracting nm from their sum leaves
exactly the stated offset identity, independent of n. Canonical blocks
are disjoint, so the factors are different. Positivity makes each
factor earlier than its represented target. Thus the coverage holds
for every n in the stated ray. QED.

This is an identity about the proposed set, so it does not assume the
greedy sequence has already stabilized. Theorem 3 then identifies that
set. For a dynamically constructed envelope, current-block factors
must instead be protected at smaller actual integers in the following
simultaneous induction.

**Chronological rule.** Suppose the asserted invariants below an integer
x are confinement to an envelope H, the presence of a protected part P,
and uniqueness of specified initial exceptional entries. To propagate
them, (i) classify every H-pair that can hit P and exclude its actual
lifetimes; (ii) represent each later exceptional copy and each point
outside H using distinct positive initial or protected entries. Every
such factor is below x. The invariants therefore propagate by induction
on x, even if a factor is in the same block. A cyclic implication between
whole unprocessed blocks is not a substitute for this argument.

## 5. A common acyclic extinction bound

Let E_i[n] be the actual selected entries of exceptional strip i in
block n. They may be arbitrary subsets. Order the finitely many strip
types so that every external dependency of type i uses earlier types.
Let C_i[n] be the core portion that controls removal of E_i.

Assume the preceding chronological argument has established confinement,
the protected entries and the following local rules.

* For n>=s_i, where s_i is a specified initial threshold, a missing entry of C_i[n]
  can only be caused by E_j[q]+E_l[r], where j,l are earlier types
  and n=q+r+c for a listed carry c. Optionally one distinguished
  point h_i of C_i may also be obstructed by a distinguished endpoint
  of E_i[n-1]. No other feedback is allowed.
* In the case without feedback, fullness of C_i in every block n>=t
  forces E_i empty in every block n>=max(t+1,tau_i), by an explicit
  sum with a fixed initial anchor. The number tau_i handles any
  coincident-block distinctness exception.
* In the feedback case, fullness of C_i minus h_i from t removes
  the obstructing endpoint of E_i from t by an explicit anchor sum;
  fullness of C_i removes all of E_i in that same block. These anchor
  implications hold at all blocks n>=s_i. The obstructing endpoint
  must differ from any exceptional point the first sum might leave.

**Lemma 5.** Suppose every earlier strip j is empty for n>=B_j.
Set

    F_i=max(s_i, max over listed (j,l,c) of (B_j+B_l+c-1)), (8)

where an empty inner maximum is omitted. Then a valid extinction bound
for type i is max(F_i+1,tau_i) without feedback, and F_i+1 with
feedback. Thus all strips disappear in finite time by induction in
the dependency order.

**Proof.** A nonempty pair of earlier strips requires q<=B_j-1 and
r<=B_l-1; its target is therefore at most B_j+B_l+c-2. No external
obstruction exists from block F_i. Without feedback the controlling
core is full there, and the assumed anchor identity removes E_i by
the stated bound. With feedback, C_i minus h_i is full from F_i,
so the obstructing endpoint is absent from those blocks. At every
block n>=F_i+1 the feedback from n-1 is consequently impossible.
The full C_i then removes the whole strip. This proves the induction.
The conclusion needs neither interval-shaped exceptional subsets nor
finite-memory dynamics. QED.

### Lower offsets

Use the sets and proved collision/anchor identities of the
[lower-offset lemma](../greedy-proof-audit-20261018/lower-lemma.md).
For i=0 the core C_0 is protected from block zero; its two copies
remove E_0 from block two, where their blocks are different. Thus
B_0=2. For i>=1, dependencies are j+l=i-1, c=0, and both types
are earlier. An initial C_0 plus C_i[n-1] removes E_i[n]. Formula
(8) gives F_i=2i+1 and B_i=2i+2. The last possible lower A_i
deficit has j+l=k+i-1, c=1, hence ends before block 2k+2i+2.
Taking the largest index gives the existing sufficient tail bound 4k.
The conditions a>=2,f>=2a ensure all anchor intervals used here
have the required lengths, including their smallest values.

### Upper interior

Use the sets and established classification in
[upper-interior compatibility](../greedy-upper-20261018/compatibility.md)
and [the chronological proof U1](../greedy-proof-audit-20261018/upper-audit.md#proposition-u1-confinement-followed-by-finite-extinction).
Order indices k-1,k-2,...,0. External dependencies of A_i have
j+l=k+i,c=1, so both j,l>i. The only feedback is the initial v
plus the top point of E_i[n-1], obstructing the lower endpoint
of A_i. The sum of F_0 with A_i minus that endpoint leaves at
most the lowest extra coordinate 2a. The top coordinate is f+a-1,
strictly larger because a<=f-2. Thus the feedback rule applies.
The top type has F=1,B=2. Substitution in (8) gives
B_i=3(k-i)-1. A D_i deficit has j+l=i,c=0 and hence is gone
from 6k-3i-3; the uniform tail bound is 6k-3.

At a=f-1 the two distinguished extra coordinates coincide, so the
feedback hypothesis fails. The lemma does not extend that proof to
this boundary. The separate boundary theorem is essential.

## 6. Causal supersolutions for the midpoint

**Lemma 6.** Suppose nonnegative endpoint sequences satisfy
U_n=A_n(L), L_n=B_n(U). Each operator is nondecreasing in its inputs
and uses only indices strictly smaller than n. Let V be a proposed
upper bound, put W_n=B_n(V), and assume A_n(W)<=V_n for every n,
with the initial values also bounded. Then U<=V and L<=W.

**Proof.** Strong induction on n gives the bound on every input to
the two operators. Therefore L_n<=B_n(V)=W_n and
U_n<=A_n(W)<=V_n. Both statements use only earlier bounds, so
there is no circular fixed-point argument. In particular if V and W
have finite support, so do U and L. QED.

The [midpoint appendix](../greedy-proof-audit-20261018/midpoint-lemma.md)
first proves its exact causal recurrence with diagonal corrections,
then supplies and proves the two finite supersolutions. Lemma 6 is
the comparison step. The unbounded range h>=3 and the Boolean boundary
h=2 have different support formulas; neither is inferred from a
finite computation or equality with the actual endpoint sequences.

## 7. Limits of the simplification

These lemmas replace repeated strictness, chronology and extinction
explanations. They do not replace the family-specific collision and
coverage identities, and they do not imply that every finite envelope
stabilizes. For example, {3*2^n+1:n>=0} is supported in the single
residue class 1 modulo 3 and has no sum of two of its members in
that class, but its gaps are unbounded, so it is not ultimately periodic.
It fails the global coverage condition and is not offered as a greedy
counterexample. This rejects an overly broad finite-envelope shortcut.

Singleton deletion and the feedback boundary above are concrete checks
against tempting stronger simplifications. The midpoint proof still
requires its finitely supported supersolution, since its dependency
structure is not the acyclic strip structure of Lemma 5. The final
proof must retain that distinct substantive argument.
