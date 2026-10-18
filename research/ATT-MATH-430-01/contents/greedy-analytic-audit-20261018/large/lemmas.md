> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Two reductions for the analytic large-seed arguments

18 October 2026. Same-team mathematical consolidation, local draft for
full-text human review and manual submission. These reductions retain the
family-specific collision and coverage obligations. They are not a
certificate, independent review, or claim of historical originality.
The shared parent assistance note records the unknown service identity,
version and configuration. Original prose/data use CC BY 4.0.

## 1. One-sided reflection and a single deleted diagonal

Let m be a positive integer and let V be a subset of {1,...,m-1} satisfying
m-V=V. Call x+y=z an unwrapped hit if x,y,z belong to V; equal x,y are
allowed in this definition.

**Reflection lemma.** Every wrapped hit x+y=m+z with x,y,z in V
corresponds bijectively to the unwrapped hit

    (m-x)+(m-y)=m-z.                                      (1)

Consequently either of the following hypotheses is sufficient for an
ordinary sum-free recurring residue set:

1. V has no unwrapped hit. Then ((V+V) mod m) intersects V trivially.
2. There is a positive g with m=3g, w=2g in V, and the only unwrapped
   hit is g+g=w. Put R=V minus {w}. Then ((R+R) mod m) intersects R
   trivially, and (({w}+R) mod m) also misses R.

Moreover, for any integer u, the condition that (u+V) mod m misses V
is equivalent to the same condition for (m-u)+V.

**Proof.** In a wrapped hit, m<x+y<2m, so the two positive reflected
summands in (1) have sum m-z in V, smaller than m. Reflection is its
own inverse. A sum equal to m has residue zero, outside V. This proves
the first assertion and case 1.

In case 2 the only possible wrapped hit is the reflection of g+g=w,
namely w+w=m+g. Deleting w from the recurring set removes the target
of the first hit and both inputs of the second. A pair consisting of
w and a member of R is neither of the two listed pairs, proving the
mixed assertion as well. Finally a modular relation u+x=z, with
x,z in V, reflects to (m-u)+(m-x)=m-z modulo m. Reflection preserves
V, proving the last equivalence. QED.

This is a reduction of collision analysis, not yet a greedy-sequence
theorem. If an actual w occurs once outside the recurring set, its
formal double is inadmissible, but all distinct exceptional cross-pairs
and all exceptional targets must still be checked. Every omitted
integer above the second seed must still have a distinct positive
representation. The positivity and seed conditions cannot be omitted.

### Two applications with different diagonal data

For the [odd-multiple argument](../../greedy-unified-20261018/odd-multiple-proof.md),
use V=R, m=(6k+3)f-1 and the odd-cell table in its lines 29-43.
The cell argument at lines 68-80 proves that no unwrapped hit exists.
Case 1 therefore supplies every wrapped exclusion. The argument at
lines 85-90 excludes u+R; since v=m-u, the final assertion replaces
the separate wrapped/unwrapped v+R classification at lines 92-97.
The explicit coverage and initial-exception checks remain necessary.
The membership domain is f>=3,k>=1 by the separately checked
[small-domain extension](../../greedy-analytic-20261018/small-domain-extensions.md),
lines 9-62. No least-period conclusion is imported at f=3 or 4.

For the [upper-boundary argument](../../greedy-analytic-20261018/upper/boundary.md),
use its V=R', m=3g, g=(2k+1)f-1 and w=2g, for f>=4,k>=2.
Lines 70-101 establish precisely the one unwrapped hit g+g=w,
including the negative cell coordinate -1. Case 2 proves the regular
and w-mixed exclusions at once. Its u+R' calculation and v=m-u
then handle the other two exceptional residues. The three distinct
exceptional cross-pairs, the safety of the initial exceptional targets,
and all gap witnesses are still provided by lines 144-228 of that proof.

The reduction exposes the actual difference between these families:
the odd-multiple table is symmetric and has no diagonal hit; the
boundary table becomes symmetric only after inserting the one point w,
and has exactly one unwrapped diagonal hit. A claim that all symmetric
residue sets are sum-free would be false and is not used.

## 2. Even multiples as a cutoff recurrence plus one cleanup step

This section replaces the separate induction arithmetic in Sections 4
and 5 of the [direct even-multiple proof](../../greedy-analytic-20261018/even-multiples/proof.md).
It does not replace that proof's envelope, collision classification,
or chronological seed initialization. Fix f>=5,k>=3 and put

    m=(6k-1)f-1,    D={4kf},
    C_l=(4k+2l)f+[-2,-1]      (1<=l<k),
    beta_i=(2k+2i+1)f-1       (0<=i<k).

Use X[n]=nm+X. The already established chronological facts are:

* The sequence lies in the displayed envelope H; H+R modulo m misses R.
* The seed g=2kf and beta_0 occur only initially. Every D[n] and every
  upper C endpoint is selected, and C_1[n] is full for every n>=0.
* A missing lower C_l[n] requires selected beta_i[q], beta_j[r] with
  i+j=l-1 and n=q+r. This is a necessary condition, allowing a formal
  diagonal only as an enlargement of possible obstructions.
* D[0]+min C_l[n-1]=nm+beta_l for n>=1. Its factors are disjoint
  even initially, so a full C_l from t removes beta_l from t+1.

These are exactly the local premises needed for the acyclic cutoff
rule in the parent framework. Their causal proof is essential: merely
deleting the formal pairs g+g and beta_0+beta_0 from a modular table
would not establish uniqueness of their actual occurrences.

**Cutoff claim.** Let B_i be a block from which beta_i is absent.
Valid choices are B_0=B_1=1 and B_i=i for 2<=i<k. Every C_l is full
from block l-1.

**Proof.** The protected C_1 and its anchor identity give B_1=1.
If i+j=l-1, a pair of beta occurrences must have

    q+r <= B_i+B_j-2.                                   (2)

Proceed in increasing l from l=2. When one index is zero, the proposed bounds
give q+r<=l-2; when both are positive they give q+r<=l-3.
Thus every C_l is full for n>=l-1. Its anchor identity gives B_l=l,
closing the induction. Equivalently the core threshold is the single
max-plus recurrence, for 2<=l<k,

    F_l=max_{i+j=l-1}(B_i+B_j-1)=l-1,
    B_l=F_l+1=l,

with the protected l=1 case supplied separately. QED.

For 2<=i<k the different-block identity

    C_1[0]+C_(i-1)[n-1]
        =nm+(2k+2i+1)f+[-3,-1]                          (3)

is available when n>=max(2,i-1). It deletes all three endpoint
depths delta_i,gamma_i,beta_i simultaneously. The explicit n>=2
guard is needed when i=2: two copies of the same initial two-point
interval would have only their strict middle sum and would not fill
all three depths. Different blocks make all endpoint pairs legitimate.

Set K=max(2,k-2). The preceding cutoffs imply that every exceptional
strip has disappeared from block K; the seed g and the first two beta
types also have no positive-block occurrences. All C runs are full
by K. A remaining missing A entry could only be a wrapped pair of
endpoint extras, hence would have n=q+r+1 with q,r<=K-1. It is
therefore impossible for n>=2K. The protected B,D runs, full C runs,
full A runs and confinement yield the same nonempty recurring set R
from 2Km.

This formulation consolidates three beta subcases into one dependency
cutoff recurrence and separates the only genuine diagonal issue in
the cleanup. It preserves the sufficient bound and does not assert
the older exact transient table or a minimal period.
