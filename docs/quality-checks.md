# Source notes and unresolved checks

These notes describe limitations in the literature used by the atlas. Consult each source or problem record for its inspection date and scope; a collection update does not mean that every source was rechecked. Specific concerns about a claimed proof remain separate from a complete proof review or a conclusion about the original problem.

The [pending checks](pending-checks.md) give the missing information for each candidate. The wider index includes historical questions, broad source-defined research directions and targets whose current status has not been established. Their presence is an invitation to examine the evidence, not a claim that every item remains open.

The [dated literature checks](literature-checks.md) distinguish statement verification from examination of later work. Each links the inspected passages and preserves limitations. Their counts measure editorial coverage, not independent mathematical verification or a complete census of current open problems.

## Read a problem

The [binary covering-code card](cards/Q-CODE-201.md#at-a-glance) illustrates where to find the relevant material:

| Section | Look for |
| --- | --- |
| [At a glance](cards/Q-CODE-201.md#at-a-glance) | Origin, status, review state and evidence for the trial label |
| [Problem](cards/Q-CODE-201.md#problem) | Definitions, quantifiers, assumptions and success criteria |
| [Verification](cards/Q-CODE-201.md#verification) | Whether the check establishes the intended claim; coverage proves an upper bound, not optimality |
| [Evidence](cards/Q-CODE-201.md#evidence) | Supporting passages, later results and corrections |
| [Assessment](cards/Q-CODE-201.md#assessment) | Methods, resources, expertise and uncertainty; forecasts versus measurements |
| [Research records](cards/Q-CODE-201.md#audit-trail) | Authorship, attempts, review scope and revisions |

## Problem-specific notes

Consult the relevant example when planning a check; these are not requirements for every submission.

| Topic | Evidence | What still needs attention |
| --- | --- | --- |
| Modular linear equations | [Q-FORMAL-500](candidates/Q-FORMAL-500.md#literature-checks) links the prime-power FPT theorem and official FOCS 2026 acceptance | The modulus-4 classification has a sourced resolution. Reproducing the algorithm or improving its bounds would be a separate task. |
| Ulam sequence density | [Q-MATH-428](candidates/Q-MATH-428.md#literature-checks) records a concern in Proposition 3.6 of Agama's version 12 | The chain 1,2,...,N has average regulator 1, contrary to the claimed uniform growth for arbitrary chains. This observation does not settle the density problem; the alternative argument and wider literature still need review. |
| Random polynomial irreducibility | [Q-MATH-425](candidates/Q-MATH-425.md#literature-checks) links Kogler's manuscript and public Lean formalization | A fixed-revision build, axiom audit and independent comparison with the original conjecture remain necessary. Repository reports are not project measurements. |
| Parallel approval voting | [Q-MODEL-445](candidates/Q-MODEL-445.md#literature-checks) specifies the winning-committee task, parallel model and MES completion convention | Hardness applies to defined rules and asymptotic guarantees, not to every practical use of parallel computing. |
| Auditory cortical models | [Q-CROSS-445](candidates/Q-CROSS-445.md#literature-checks) includes Kell et al.'s published auditory model and author-provided parameters | Predictive progress does not settle the broad explanatory direction. Weights, stimuli and neural measurements require separate access and rights checks. |
| Markovian PDE representations | [Rocha and Willems (2006)](https://homes.esat.kuleuven.be/~sistawww/smc/jwillems/Articles/JournalArticles/2006.1.pdf), section 3, disprove the original weak-Markovian converse | [Q-CROSS-401](candidates/Q-CROSS-401.md) retains the historical conjecture and its sourced disproof. Strong-Markovian variants must not silently replace it. |
| Regular feedback implementation | [Vinjamoor and Belur (2010)](https://www.ee.iitb.ac.in/~belur/pdfs/j10laa.pdf), Theorem 4.2 and concluding discussion | Full interconnection is solved in the cited setting; necessary and sufficient conditions for partial interconnection are left for further work. [Q-CROSS-403](candidates/Q-CROSS-403.md) concerns partial interconnection. |
| Hydrological prediction under change | [Santos et al. (2025)](https://hess.copernicus.org/articles/29/683/2025/) study robustness across 352 catchments | The model comparison provides partial empirical evidence. It neither solves all prediction-under-change questions nor proves universal impossibility. |
| Cortical topography | [Qian et al. (2026)](https://www.nature.com/articles/s41467-026-70065-3) provide a model with local lateral connectivity | Predictive sufficiency does not identify the unique biological mechanism. Backpropagation remains part of training, and data access must be checked separately. |
| [Four-color triangle Ramsey number](cards/Q-MATH-003.md#evidence) | [Radziszowski's survey](https://www.cs.rit.edu/~spr/ElJC/sur.pdf), revision 18, section 6.1.1, gives bounds of 51–62 | Check the original lower-bound construction and corrected witness before using them. Multiplicity results do not determine the exact Ramsey number. Openness needs dated evidence; construction checks and universal bounds have different costs. |
| [Union-closed families](cards/Q-MATH-002.md#at-a-glance) | [Bruhn and Schaudt](https://arxiv.org/pdf/1309.3297), Theorem 17, includes the small-ground-set case | The curator-designed four-element task is a certificate benchmark for a known property; mathematical novelty is not claimed. |
| [Copy-lemma inequalities](cards/Q-FORMAL-003.md#assessment) | [Csirmaz's survey](https://arxiv.org/html/2509.12439v1), Definition 24, Lemma 27 and Claims 31–32, gives both the construction and relevant obstructions | Singleton conditioning yields no non-Shannon consequence. Two-variable conditioning avoids that particular obstruction, but the usefulness of the bounded search remains unverified. Justify finite-search constraints and compare prior work. |
| Five-variable information inequalities | [Csirmaz and Csirmaz](https://arxiv.org/abs/2512.23316) report systematic prior work | Any proposed inequality needs comparison with existing results and exact certificates before a novelty claim. |
| Split likelihood-ratio inference | [Universal Inference](https://arxiv.org/html/1912.11436v4), Theorem 1, supplies the finite-sample guarantee | The independent split and endpoint conventions matter. Checking a finite parameter grid does not establish the all-parameter result. |
| [Bimatrix equilibria](cards/Q-MODEL-003.md#verification) | [von Stengel's survey](https://arxiv.org/html/2102.04580), Definition 2, Algorithm 4 and equation (3), specifies nondegeneracy and support enumeration | Preserve nondegeneracy. Validity of each equilibrium and completeness of the list are separate obligations. Neither establishes dynamical stability. |
| [Deficiency-zero reaction networks](cards/Q-MODEL-002.md#problem) | [Anderson, Craciun and Kurtz](https://arxiv.org/html/0803.3042), Definition 2.4 and Theorem 3.1, gives the relevant hypotheses and conclusion | Preserve mass-action, positive-class and relative local-stability qualifications; do not infer global convergence or empirical adequacy. |
| [CHSH bound](cards/Q-MODEL-001.md#verification) | [Wehner's exposition](https://arxiv.org/pdf/quant-ph/0510076) contains apparent transcription or normalization discrepancies | Reconcile the alternative SDP presentation with its dual and justify the reduction to an exact certificate. The operator-proof route remains available, with mixed-state assumptions explicit. |
| Two-copy Werner-state problem | [Fraser et al.](https://arxiv.org/abs/2607.24309), Section 3, and two further 2026 preprints claim a negative resolution | The theorem parameters were compared in [Q-MODEL-006](candidates/Q-MODEL-006.md#literature-checks). Complete proofs, independent validation and acceptance remain unconfirmed; agreement among claims is insufficient. |
| Navier–Stokes | [Clay's announcement of 11 September 2026](https://www.claymath.org/news/navier-stokes-announcement/) describes an apparent resolution under evaluation | An older unqualified open-problem label is insufficient. The announcement does not substitute for reviewing the proof. |
| [Weak White conjecture](cards/Q-MATH-104.md#evidence) | [Larson's 2026 preprint](https://arxiv.org/html/2607.02208v1), Conjecture 1.1(3), separates arbitrary quadratic generators from symmetric exchanges | The reported counterexample to symmetric-exchange generation and the separate quadratic-Gröbner obstruction do not settle the weak version. Recent proofs and computational artifacts still need independent review. |
| Kuramoto connectivity threshold | [McRae's 2026 revision](https://arxiv.org/html/2503.18801v2), section 3.4.3, retains the conjectured sharp value of 3/4 | Spurious second-order critical points are not necessarily stable equilibria. The target is nonlinear almost-everywhere synchronization, not only a Jacobian test. |
| [Moran fixation](cards/Q-MODEL-101.md#verification) | The card describes residual certificates for the finite-state model | Retain absorbing boundaries and establish uniqueness. An exact residual does not establish biological adequacy. |
| [Common Lyapunov certificate](cards/Q-FORMAL-101.md#verification) | The card specifies exact certificate acceptance for conditional decay | Rejecting one certificate does not establish instability. |
| [Locally constrained grammar](cards/Q-FORMAL-102.md#problem) | [Vijay-Shankar and Joshi](https://aclanthology.org/P85-1011/), Example 2.5, uses local adjoining restrictions | The scanned elementary trees and restrictions need a checked transcription. The nonempty language and the empty-word convention are separate obligations; sample derivations do not prove both inclusions. |
| Triangular Lagrange points | [Fitzpatrick's treatment](https://farside.ph.utexas.edu/teaching/celestial/Celestial/node86.html), equations (9.87)-(9.88), supplies the linearized threshold | The card excludes the critical parameter and makes no nonlinear stability claim. Purely imaginary eigenvalues require attention to multiplicity and Jordan structure. |
| [Energy-balance climate model](cards/Q-MODEL-010.md#verification) | [Ashwin and von der Heydt](https://link.springer.com/article/10.1007/s10955-019-02425-x), equations (19)-(21), Table 1 and following curvature expression | Recompute derivatives from the declared functions, resolve source discrepancies, preserve the smooth tanh tails and certify root completeness. Sensitivity is undefined at folds. A formal fold is not a measured climate tipping point. |
| [Finite covering codes](cards/Q-CODE-201.md#verification) | [Gijswijt and Polak](https://arxiv.org/html/2504.01932v2), Tables 1–3, and [Maharaj](https://arxiv.org/html/2610.03760v1), Corollary 10 and Proposition 12 | The newer quaternary upper bounds supersede the earlier table. An explicit cover can be checked exactly but may be expensive to find; restricted-search failure is not an unrestricted lower bound. The lower-bound certificates and recent constructions have not been independently audited here. |
| No-three-in-line configurations | [Flammenkamp's current table](https://wwwhomes.uni-bielefeld.de/achim/no3in/table.html) and [dated construction notes](https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html) | Older unsolved grid sizes are unreliable guides after the 2025–2026 constructions. A missing construction is not a proof of nonexistence; symmetry-restricted exhaustion does not settle the unrestricted question. |
| Four-agent fair division of goods | [Alkassar, Fouz and Mehlhorn](https://arxiv.org/html/2608.08590v1), Definition 1 and Theorem 1 | The preprint reports complete EFX0 allocations for at most nine goods. Preserve the treatment of zero-valued goods. A ten-good starting scope needs its own novelty check and is not presented as a separately established open conjecture. |
| Bi-valued chores | [He and Tao](https://arxiv.org/html/2606.08872v1), Section 6 | Keep the common two-value assumption distinct from personalized values, and existence distinct from Pareto efficiency. Counterexamples for unrestricted costs do not settle the bi-valued case. |
| Automaton state avoidance | [The original conjecture](https://arxiv.org/pdf/1607.04025), Section 3, Conjecture 5, and [the 2026 survey](https://arxiv.org/pdf/2608.24245), Section 2.2 | Retain strong connectivity from the original statement. Synchronization alone does not make a sink state avoidable; the survey's shorter wording omits an essential qualification. |
| Front-door completeness | [Wu and Robeva](https://arxiv.org/html/2604.15288v1), Section 2.1.1 and Section 6 | Preserve strict observational positivity. A complete identification algorithm for some functional does not automatically characterize validity of this particular front-door formula. |
| Heilbronn configurations | [Sudermann-Merx](https://arxiv.org/html/2603.11107v1), Appendix A, and [Monji, Modir and Kocuk](https://arxiv.org/html/2512.14505v1), Table 5 | Exact coordinates establish a lower bound only after checking every triangle. Solver objectives, recomputed areas, unproved boundary restrictions and unrestricted global upper bounds must remain separate. |

## Review coverage and placement

Use [pending checks](pending-checks.md) and [dated literature checks](literature-checks.md) to find a bounded review task. Prioritize possible resolutions, counterexamples, changed hypotheses and unsettled recent claims. Compare exact statements; a source's open label is dated evidence, not a guarantee of current openness.

| Candidate | Focus for an initial review |
| --- | --- |
| [Star-graph diversity time](candidates.md#q-model-301) | The [source conjecture](https://arxiv.org/html/2503.09841v2) uses n leaves and N=n+1 total vertices, counts every update including null updates, and depends on birth-death order. |
| [Partition numbers dividing factorials](candidates.md#q-math-304) | Counterexample search versus proof for all integers above 39. |
| [Deterministic factor-2 tournament approximation](candidates.md#q-formal-330) | The [paper](https://arxiv.org/html/2609.16723v1) guarantees 2+epsilon for each fixed positive epsilon; the exact factor-2 target remains distinct. |
| [Linear sample compression](candidates.md#q-formal-317) | Preserve stored examples and side-information bits. The [proof claim](https://arxiv.org/abs/2603.23561) is withdrawn, with an error identified in its second lemma; its title and older abstract do not establish a solution. |
| [Finite-energy-density localization](candidates.md#q-model-310) | Fixed low-energy intervals versus nonzero energy density. |
| [Rational Hodge conjecture](candidates.md#q-land-303) | Rational coefficients, projectivity and construction versus numerical evidence. |

Broad directions need explicit assumptions and success criteria before solution review. Brief profiles contain less detail than cards. For [Millennium and Hilbert problems](landmark-problems.md), distinguish historical negative answers, independence from stated axioms, partial progress and unreviewed proof claims. Solved entries are context, not open candidates.

Use the [subject map](README.md) and [coverage matrix](coverage.md) for placement, and the [difficulty view](difficulty.md) for target scope. Compare equivalent formulations to avoid duplicates; a general source directory does not establish a particular claim. Suggest additions with a source, scope and placement rationale.

## Classification and access limits

Historical collections require particular care. The 2002 MTNS control questions, older probability notes and individual TOPP geometry entries can provide precise statements while leaving decades of subsequent work to review. A recently accessed website does not make its older status assessment current. The mathematical physics workshop list and the voting-theory chapter likewise support only the questions and qualifications present in the inspected text.

The hydrology and sensory-cortex collections contain research directions rather than uniformly specified conjectures. Their candidate records identify missing model choices, observables and success criteria. Theoretical analysis can proceed without a new experiment in some cases, but identifying the mechanism operating in nature may require observational or experimental evidence. These records do not promise inexpensive computation or easy empirical verification.

Recent candidate checks also distinguish the following cases:

- The [Kourovka Notebook](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/10/21tkt-1.pdf) uses separate markers for accepted resolutions and proposed AI solutions awaiting confirmation. Placement outside its solved-problem archive alone does not establish open status.
- The original [Hilbert Problem 18](https://www.gutenberg.org/cache/epub/71655/pg71655-images.html) includes general congruent solids as well as spheres. Resolution of the familiar sphere-packing component does not settle the entire broad formulation.

The [historical collections](landmark-problems.md) include all seven Millennium and 23 Hilbert entries. Clay's current status list and official problem descriptions provide the Millennium baseline. Hilbert's original lecture supplies the scopes; a recent institutional overview provides historical orientation. Broad or interpretation-dependent Hilbert entries still need specialist primary-source histories before becoming full research cards. The algebraic thirteenth problem is distinguished from continuous superposition, and rational Hodge classes from the disproved integral variant.

Some current resolution claims have not completed independent scrutiny. A claim register or repository listing establishes that a claim exists; it does not establish its theorem. In particular, a reported 2026 uniform bound in Hilbert's sixteenth problem does not supply an exact maximum or classify curve arrangements. Its linked proof has not been inspected here. Such limitations remain visible rather than being compressed into a single solved/open label.

The MSC2020 introduction, top-level classification list and selected logic, Markov-process and lattice-model entries were inspected. An exhaustive code-level crosswalk remains unverified. ACM coverage uses a partial ACM-hosted curriculum mapping and an ETH-hosted mirror; correspondence with the complete official classification requires further checking.

Some bibliography entries are author pages, institutional records or abstracts. Their notes identify exactly what was reviewed. A book portal is not a review of the book, and an abstract cannot establish the correctness of a proof. Publication years remain unspecified where reliable dating is unavailable.

The [source directory](sources.md) records authors, links, dates, exact locations and limitations. Each problem card provides its own status evidence and unresolved questions. These distinctions matter because a source may be reliable for a definition while offering only historical evidence about whether a problem is still open.

## Rechecking a claim

Return to the cited version and exact theorem or problem number. Check later versions, corrections and relevant follow-up work. Record any changed assumptions, competing claims or limits on what was reviewed. Keep the review date attached to the claim it supports.

The atlas summarizes and links to third-party work; it does not redistribute a full source archive. Preserve authorship and rights when adding quotations, copies or archived material.

[Source directory](sources.md) · [Evidence standards](evidence-policy.md) · [Review guide](review-guide.md)
