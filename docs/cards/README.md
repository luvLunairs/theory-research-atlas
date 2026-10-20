# Research problems

[Browse](../README.md) · [Results](../results.md) · [Contribute](../../CONTRIBUTING.md)

Each entry brings together a precise task, its sources, prerequisites and ways to check a result. The priorities indicate which tasks may be worth trying; they are not measurements of AI performance. Known results are distinguished from open questions and proposed investigations.

**Looking for new research? Start with [open research candidates](../research-candidates.md).** This complete card directory also retains calibrations and proposals.

[Assessment rubric](../ai-assessment.md) · [Evidence policy](../evidence-policy.md)

| Entry type | Full cards | Broader index |
| --- | --- | --- |
| Literature-origin question | 27 | [View candidates](../candidates.md#literature-open) |
| Curator-proposed task | 2 | [View candidates](../candidates.md#curator-proposed) |
| Known-result calibration | 16 | [View candidates](../candidates.md#known-result-calibration) |

Origin is separate from current status. Reproductions help assess methods; their completion would not constitute a new solution to an open problem. [Research progress](../progress.md) records actual attempts and reviews.

[Priority for a later trial](#priority-trial) · [Preparation needed](#preparation-required) · [Exploratory](#exploratory) · [Not yet assessed](#unassessed) · [Browse by method](#browse-by-method)

<a id="priority-trial"></a>

## Priority for a later trial

<a id="q-code-201"></a>

### [Binary length-12 covering codes of radius three](Q-CODE-201.md)

[Coding theory](../domains/info.md#info-codes) · Literature-origin question

Choose as few length-12 words over a 2-symbol alphabet as possible so that every possible word lies within 3 symbol changes of one chosen word. Any smaller verified cover improves a concrete finite bound.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Hamming distance and covering codes; Finite set covering and bitsets; Exact integer arithmetic; Certificate checking and basic computational reproducibility.

**Verification:** Exact computation, Proof. [How to check a result](Q-CODE-201.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** An explicit finite witness is cheap to inspect and the target is precise, making bounded construction search a reasonable first trial. The search itself may still be difficult.

**Computing requirements and limits:** A direct witness check for 27 codewords uses at most 1,327,104 coordinate comparisons. This is an operation bound, not a measured runtime. A direct binary set-cover formulation has 4,096 variables and 4,096 covering constraints. Proposed initial ceiling: 4 CPU-hours and 8 GiB RAM, stopping sooner on a verified improvement. This is a curator-chosen exploration cap, not an estimate of the resources needed to solve the problem; no run or cost measurement has been made.

**Human review:** Low to moderate for an explicit upper-bound witness. High for unrestricted lower bounds or exact optimality.

</details>

<a id="q-code-202"></a>

### [Ternary length-seven covering codes of radius two](Q-CODE-202.md)

[Coding theory](../domains/info.md#info-codes) · Literature-origin question

Choose as few length-7 words over a 3-symbol alphabet as possible so that every possible word lies within 2 symbol changes of one chosen word. Any smaller verified cover improves a concrete finite bound.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Hamming distance and covering codes; Finite set covering and bitsets; Exact integer arithmetic; Certificate checking and basic computational reproducibility.

**Verification:** Exact computation, Proof. [How to check a result](Q-CODE-202.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** An explicit finite witness is cheap to inspect and the target is precise, making bounded construction search a reasonable first trial. The search itself may still be difficult.

**Computing requirements and limits:** A direct witness check for 33 codewords uses at most 505,197 coordinate comparisons. This is an operation bound, not a measured runtime. A direct binary set-cover formulation has 2,187 variables and 2,187 covering constraints. Proposed initial ceiling: 4 CPU-hours and 8 GiB RAM, stopping sooner on a verified improvement. This is a curator-chosen exploration cap, not an estimate of the resources needed to solve the problem; no run or cost measurement has been made.

**Human review:** Low to moderate for an explicit upper-bound witness. High for unrestricted lower bounds or exact optimality.

</details>

<a id="q-math-002"></a>

### [Audit exact union-closed-family certificates on at most four elements](Q-MATH-002.md)

[Extremal and Ramsey theory](../domains/math.md#math-comb-ext) · Curator-proposed task

Build a small, complete catalog of set families that are closed under union, with a simple witness showing that some element occurs in at least half their sets.

**Status:** Known result in literature; checked 2026-10-13. **Assessment evidence:** Untested forecast.

**Background:** Power sets and finite set families; Closure under union; Binary encodings and integer counting; Basic reproducibility and independent-checker design.

**Verification:** Proof, Exact computation. [How to check a result](Q-MATH-002.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The task has fully bounded enumeration, a local exact witness, and cheap independent verification. Its purpose is to test careful formalization and tooling, not to suggest the general conjecture is easy.

**Computing requirements and limits:** Estimated ordinary CPU and small memory. There are exactly 2^16=65,536 input family masks before filtering; this size justifies a conservative laptop-scale planning assumption but is not a timing measurement.

**Human review:** Low to moderate; independent software and exhaustive-coverage reasoning need careful review.

</details>

<a id="q-math-201"></a>

### [A 150-point no-three-in-line configuration on a 75 by 75 grid](Q-MATH-201.md)

[Geometry](../domains/math.md#math-geom) · Literature-origin question

Place 150 lattice points on a 75 by 75 board so that no straight line contains three. A finite output is easy to check independently, although finding it may be hard.

**Status:** Open after a scoped check; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Integer determinant geometry; SAT or constraint programming; Symmetry and orbit constraints.

**Verification:** Exact computation, Proof. [How to check a result](Q-MATH-201.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Priority applies to the bounded construction experiment: its output is precise and independently checkable. It does not predict that the frontier target will be solved.

**Computing requirements and limits:** Proposed cap: 8 CPU-hours and 16 GiB RAM. The grid has 5,625 positions. A positive witness needs C(150,3)=551,300 exact triple checks. Full impossibility may require much larger resources.

**Human review:** Low for a positive witness; high for a global impossibility proof.

</details>

<a id="q-math-203"></a>

### [The exact ten-point Heilbronn number in the unit square](Q-MATH-203.md)

[Geometry](../domains/math.md#math-geom) · Literature-origin question

Arrange ten points in a unit square so that the smallest of their 120 triangles is as large as possible. A better arrangement has a short exact certificate; proving that no better arrangement exists is much harder.

**Status:** Open after a scoped check; checked 2026-10-17. **Assessment evidence:** Untested forecast.

**Background:** Determinant area formulas; Nonconvex max-min optimization; Rational and real-algebraic arithmetic; Interval certification and the difference between local and global optima.

**Verification:** Exact computation, Proof, Numerical evidence. [How to check a result](Q-MATH-203.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Priority applies to the capped construction search and exact certificate workflow. The twenty-variable formulation and 120-triangle checker make a limited experiment reviewable; the full global optimum remains difficult.

**Computing requirements and limits:** Proposed search cap: 4 CPU-hours, 8 GiB RAM and 100 starts. A candidate has twenty real coordinates and 120 triangle constraints. Exact witness checking is small compared with unrestricted global optimization; no cost or runtime has been measured.

**Human review:** Moderate for an exact lower-bound witness; high for a global proof. Optimization certificates require scrutiny of tolerances and omitted regions.

</details>

<a id="q-math-204"></a>

### [Improve the lower bound for R(4,6) with a 36-vertex graph](Q-MATH-204.md)

[Extremal and Ramsey theory](../domains/math.md#math-comb-ext) · Literature-origin question

Find a graph on 36 vertices in which neither four vertices are all joined nor six vertices are all mutually unjoined. Its complete correctness check involves fewer than two million small subsets.

**Status:** Open after a scoped check; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Ramsey graph definitions; Exact finite graph checking; SAT or constraint optimization; Reproducible graph files.

**Verification:** Exact computation, Proof, Public data. [How to check a result](Q-MATH-204.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The proposed bounded construction trial has reusable attributed seeds and a transparent independent checker. The recommendation concerns reviewability and controlled scope, not an expectation of solving the full problem.

**Computing requirements and limits:** Proposed cap: 8 CPU-hours and 16 GiB RAM for all seeds together. The witness has 630 possible edges; independent brute-force verification examines C(36,4)=58,905 four-sets and C(36,6)=1,947,792 six-sets. Search and global nonexistence can be far more expensive.

**Human review:** Low for a positive witness; high for an unrestricted impossibility proof. Restricted failures need precise scope and provenance.

</details>

<a id="q-formal-001"></a>

### [Reproduce Huang's hypercube degree theorem](Q-FORMAL-001.md)

[Computational complexity](../domains/cs.md#cs-complex) · Known-result calibration

More than half of a Boolean cube forces a vertex with many selected neighbors. A published short proof makes this useful for checking whether a research workflow can preserve a theorem's quantifiers and produce a reviewable proof.

**Status:** Known result in literature; checked 2026-10-13. **Assessment evidence:** Untested forecast.

**Background:** Graphs and hypercubes; Real symmetric matrices; Eigenvalues and principal-submatrix interlacing; Inductive block-matrix construction.

**Verification:** Proof. [How to check a result](Q-FORMAL-001.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Useful first calibration because the target and reference proof are explicit and errors can be localized to linear-algebra lemmas. This predicts auditability, not research discovery or model success.

**Computing requirements and limits:** Symbolic proof first. Optional small matrices grow as 2^n by 2^n; never materialize large cubes merely because no experiment is needed. Formalization cost unknown; no run or time estimate exists.

**Human review:** Moderate; a reviewer needs spectral graph theory or linear algebra. Automated acceptance alone does not validate the source-to-formal-statement translation.

</details>

<a id="q-formal-002"></a>

### [Audit finite-sample split likelihood-ratio coverage in a Bernoulli model](Q-FORMAL-002.md)

[Inference and decision theory](../domains/stat.md#stat-infer) · Known-result calibration

Train a probability estimate on one half of a small coin-flip sample and evaluate it on the other half. Check that the resulting confidence set covers the true probability at the promised rate, without replacing exact evidence by simulation.

**Status:** Known result in literature; checked 2026-10-13. **Assessment evidence:** Untested forecast.

**Background:** Bernoulli and binomial distributions; Conditional expectation; Markov's inequality; Exact rational arithmetic.

**Verification:** Proof, Exact computation. [How to check a result](Q-FORMAL-002.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The proof and exact finite audit provide two complementary checks with limited implementation scope. The relevant capability is disciplined conditioning and exact arithmetic, not confidence asserted by a model.

**Computing requirements and limits:** Small finite enumeration over 121 count pairs at each of nine rational parameter values. Rational bit sizes should be logged; wall time, memory and cost have not been measured.

**Human review:** Moderate; probability review is necessary despite a small program.

</details>

<a id="q-formal-101"></a>

### [Check common quadratic Lyapunov certificates for small matrix polytopes](Q-FORMAL-101.md)

[Control, estimation and systems theory](../domains/eng.md#eng-control) · Known-result calibration

A proposed stability argument can be checked through a few exact matrices. The useful output is a certificate with explicit assumptions, including an explanation of what an unsuccessful check does not establish.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Exact rational arithmetic and positive-definite matrices; Lyapunov functions, linear differential inclusions and uniform decay; The distinction between a sufficient witness and a complete decision procedure.

**Verification:** Proof, Exact computation. [How to check a result](Q-FORMAL-101.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** A finite exact acceptance test separates algebra from theorem application. Priority refers to a possible calibration trial, not demonstrated AI performance.

**Computing requirements and limits:** Exact determinants of matrices of order at most four with bounded rational inputs. Laptop-class execution is an untested planning assumption; larger dimensions and certificate synthesis may be much harder.

**Human review:** Moderate: mechanical algebra checks are short, but a control specialist should approve theorem-to-model alignment.

</details>

<a id="q-formal-103"></a>

### [Check twisted-state spectra on Kuramoto cycle networks](Q-FORMAL-103.md)

[Dynamics on networks and collective behavior](../domains/net.md#net-dynamics) · Known-result calibration

A ring of identical oscillators supports synchronized and twisted phase patterns. A known spectrum provides a compact test of instability, stability up to common rotation, and cases where linearization cannot decide.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Smooth ODE linearization and stability modulo symmetry; Cycle Laplacians and Fourier eigenvectors; Exact trigonometric signs or certified algebraic-number calculations.

**Verification:** Proof, Exact computation. [How to check a result](Q-FORMAL-103.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The known formula and a bounded exact table independently check symbolic reasoning and symmetry handling without relying on trajectories as proof.

**Computing requirements and limits:** Symbolic differentiation and matrices of order at most twenty for the finite table. Exact trigonometric reasoning avoids numerical optimization. The bounds are chosen for inspectability; no runtime, cost or success rate has been measured.

**Human review:** Moderate: short symbolic work is inspectable, but local, orbital and global behavior require dynamics expertise.

</details>

<a id="q-math-001"></a>

### [Reproduce the exact Ramsey number R(3,3)=6](Q-MATH-001.md)

[Extremal and Ramsey theory](../domains/math.md#math-comb-ext) · Known-result calibration

A tiny, established graph-coloring theorem makes a transparent starting benchmark for testing future search-to-certificate workflows.

**Status:** Known result in literature; checked 2026-10-13. **Assessment evidence:** Untested forecast.

**Background:** Complete graphs and edge colorings; Pigeonhole principle; Finite enumeration and independent verification.

**Verification:** Proof, Exact computation. [How to check a result](Q-MATH-001.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** A clear, finite target and short independent checks make this useful for calibrating a workflow before harder research. This is not a prediction of novel discovery.

**Computing requirements and limits:** Estimated ordinary laptop CPU and modest memory for a future run. The full six-vertex space has 32,768 colorings; this is a combinatorial size, not a measured runtime or budget.

**Human review:** Low for mathematical reasoning; moderate only if the implementation hides enumeration or certificate assumptions.

</details>

<a id="q-math-101"></a>

### [Exact finite satisfiability for a small monadic fragment](Q-MATH-101.md)

[Model theory](../domains/logic.md#logic-model) · Known-result calibration

Decide whether a small formula about unary properties can hold in a finite structure, and make every positive or negative answer independently checkable.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** First-order syntax, binding and environments; Induction on formulas; Finite truth tables and exact enumeration.

**Verification:** Proof, Exact computation. [How to check a result](Q-MATH-101.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The type space is small, the semantic reduction is documented, and certificates can be checked independently. The useful challenge is preserving the statement through its encoding, not discovering an unknown theorem.

**Computing requirements and limits:** At k=3 there are 8 predicate types and 255 nonempty subsets. Evaluating a formula also branches over quantified assignments. These are combinatorial sizes, not measured time or memory; exhaustive formula generation is out of scope.

**Human review:** Moderate: the model enumeration is small, but the semantic proof and binder encoding need an experienced reader.

</details>

<a id="q-math-102"></a>

### [Exact mixing certificates for small positive Markov chains](Q-MATH-102.md)

[Markov chains, mixing and interacting systems](../domains/prob.md#prob-mix) · Known-result calibration

Turn a small exact transition matrix into a checkable guarantee on how quickly its probability distributions approach equilibrium.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Finite Markov chains and stationary distributions; Total variation distance; Exact linear algebra and probability couplings.

**Verification:** Proof, Exact computation. [How to check a result](Q-MATH-102.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The proof decomposes into established coupling facts and exact arithmetic checks. Small input dimensions allow independent review while retaining an all-time probabilistic claim.

**Computing requirements and limits:** Rational linear algebra on matrices of order at most 6 and coupling tables of order at most 6 by 6. Rational bit lengths can grow when certifying large T; resource estimates should be recorded for selected inputs before execution.

**Human review:** Moderate: finite arithmetic is straightforward; the passage from one-step certificates to all times needs a probability-trained reviewer.

</details>

<a id="q-math-103"></a>

### [Transfer-matrix calibration for the one-dimensional Ising model](Q-MATH-103.md)

[Rigorous statistical mechanics](../domains/mphy.md#mphy-stat) · Known-result calibration

Recover an exact equilibrium formula for a chain of interacting two-state spins and explain why this idealized model has no singularity in the field at finite temperature.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Finite partition functions; Two-by-two matrix eigenvalues; Real analytic functions and limits; Distinction between a model parameter and a measured physical quantity.

**Verification:** Proof, Exact computation. [How to check a result](Q-MATH-103.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The source provides an exact model and a short route to the answer. It offers independently checkable symbolic steps while exposing common errors in boundary conditions and limits.

**Computing requirements and limits:** Symbolic manipulation of a two-by-two matrix is sufficient for the proof. Optional finite checks contain 2^N spin assignments for each chosen N; no runtime has been measured.

**Human review:** Moderate: the algebra is short, but the parameter conventions and limiting claims need a mathematical-physics reader.

</details>

<a id="q-model-001"></a>

### [Reproduce the CHSH optimum with an exact certificate](Q-MODEL-001.md)

[Quantum theory and foundations](../domains/phys.md#phys-quant) · Known-result calibration

Rebuild a standard limit on quantum correlations in a form another person can check exactly. This calibrates statement translation and certificate checking before unfamiliar Bell problems are considered.

**Status:** Known result in literature; checked 2026-10-13. **Assessment evidence:** Untested forecast.

**Background:** Tensor products, density operators and Hermitian matrices; Positive semidefinite matrices, Gram matrices and weak duality; Exact arithmetic over Q(sqrt(2)) or an equivalent symbolic representation.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-001.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** A fixed operator-proof calibration with an attaining construction is a useful priority trial. If the alternative SDP route is chosen, first resolve the documented source transcription hazards and normalization alignment. No trial results have been recorded.

**Computing requirements and limits:** A few fixed 4 by 4 exact matrices. A standard local symbolic or rational-algebra environment is a plausible resource class; no runtime or monetary estimate has been measured.

**Human review:** Moderate: a linear-algebra reviewer can inspect certificates, but a quantum-information reviewer should confirm statement alignment.

</details>

<a id="q-model-003"></a>

### [Enumerate equilibria of a supplied rational bimatrix game](Q-MODEL-003.md)

[Game and equilibrium theory](../domains/econ.md#econ-game) · Known-result calibration

Find every pair of mixed strategies that are best responses to one another in a small, fully specified mathematical game. The task tests complete case coverage and detection of inputs outside the algorithm scope; it makes no dynamical-stability claim.

**Status:** Known result in literature; checked 2026-10-13. **Assessment evidence:** Untested forecast.

**Background:** Expected payoffs and mixed strategies; Rational linear systems and inequalities; Combinatorics of supports and the precise definition of nondegeneracy.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-003.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** A finite support search and exact certificates permit independent checking. The source's fully specified example makes the trial transferable without inventing new economic claims.

**Computing requirements and limits:** At most 3 by 3 matrices with a declared bit-length bound to be set in the trial. Small support enumeration is a plausible local workload; no time, cost or success measurements exist.

**Human review:** Moderate: arithmetic can be automated, but a game theorist should confirm hypothesis certification and all-equilibria completeness.

</details>

<a id="q-model-101"></a>

### [Reproduce exact Moran fixation probabilities](Q-MODEL-101.md)

[Evolution, population genetics and phylogenetics](../domains/bio.md#bio-evol) · Known-result calibration

Calculate the chance that one mutant eventually replaces a whole idealized population. Exact finite-state calculations make the assumptions and arithmetic inspectable before more complicated evolutionary models are considered.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Finite Markov chains and absorbing-state boundary equations; Rational arithmetic and basic linear algebra; The distinction between a stochastic update rule and a diffusion approximation.

**Verification:** Exact computation, Proof. [How to check a result](Q-MODEL-101.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Small exact systems, explicit update rules and a published formula provide independent checking routes. Priority concerns a future calibration, not an assessed ability to solve open evolutionary questions.

**Computing requirements and limits:** Three systems with 19 unknown interior probabilities and exact rational coefficients. A local exact-arithmetic environment is a plausible resource class; runtime, memory and cost have not been measured.

**Human review:** Low to moderate: arithmetic is finite, but a reviewer must confirm that the stochastic model matches the claimed reproduction.

</details>

<a id="q-model-102"></a>

### [Recover the linear stability threshold of triangular Lagrange points](Q-MODEL-102.md)

[Celestial dynamics](../domains/astro.md#astro-dyn) · Known-result calibration

Reproduce the textbook mass-ratio threshold at which small planar disturbances of the triangular Lagrange equilibria cease to remain bounded in the linearized model. The task deliberately stops before nonlinear or real-system stability.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Linearization of autonomous differential equations and exact determinants; Eigenvalues, diagonalizability and the distinction between linear and nonlinear stability; Rotating-frame Newtonian mechanics.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-102.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The symbolic target is short enough for an independent determinant check, while its interpretation tests a frequent overstatement about stability.

**Computing requirements and limits:** One exact 4-by-4 determinant with an algebraic parameter and quadratic discriminant analysis. A local symbolic environment is a plausible resource class; no runtime or cost has been measured.

**Human review:** Moderate: the determinant is easy to reproduce, while precise stability implications require dynamical-systems knowledge.

</details>

<a id="q-model-103"></a>

### [Verify the Ornstein–Uhlenbeck transition law and equilibrium](Q-MODEL-103.md)

[Statistical and nonequilibrium physics](../domains/phys.md#phys-stat) · Known-result calibration

Check a standard random process that is pulled toward the origin while experiencing noise. Its exact probability distribution offers a controlled way to verify stochastic equations, stationary distributions and equilibrium claims.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Gaussian densities and convolution; Basic Itô integration, deterministic integrating factors and the Itô isometry; Fokker–Planck equations, probability current and weak convergence.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-103.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The closed-form kernel can be checked by both stochastic and differential-equation routes. The main value is whether a generated derivation keeps its conventions and limiting statements consistent.

**Computing requirements and limits:** Symbolic differentiation, Gaussian integration and a few exact identities. A local computer algebra environment is a plausible resource class; no simulation campaign, runtime or cost measurement is required or reported.

**Human review:** Moderate: formulas are explicit, but the probability-space assumptions and weak limit need a reviewer familiar with stochastic processes.

</details>

<a id="preparation-required"></a>

## Preparation needed

<a id="q-code-203"></a>

### [Quaternary length-six covering codes of radius two](Q-CODE-203.md)

[Coding theory](../domains/info.md#info-codes) · Literature-origin question

Choose as few length-6 words over a 4-symbol alphabet as possible so that every possible word lies within 2 symbol changes of one chosen word. Any smaller verified cover improves a concrete finite bound.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Hamming distance and covering codes; Finite set covering and bitsets; Exact integer arithmetic; Certificate checking and basic computational reproducibility.

**Verification:** Exact computation, Proof. [How to check a result](Q-CODE-203.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The recent construction must first be checked and its restrictions understood. A bounded improvement search is then plausible, with a particularly simple independent witness test.

**Computing requirements and limits:** A direct witness check for 47 codewords uses at most 1,155,072 coordinate comparisons. This is an operation bound, not a measured runtime. A direct binary set-cover formulation has 4,096 variables and 4,096 covering constraints. Proposed initial ceiling: 4 CPU-hours and 8 GiB RAM, stopping sooner on a verified improvement. This is a curator-chosen exploration cap, not an estimate of the resources needed to solve the problem; no run or cost measurement has been made.

**Human review:** Low to moderate for an explicit upper-bound witness. High for unrestricted lower bounds or exact optimality.

</details>

<a id="q-formal-003"></a>

### [Build a bounded exact copy-lemma certificate census](Q-FORMAL-003.md)

[Entropy inequalities and information geometry](../domains/info.md#info-entropy) · Curator-proposed task

Create a tiny, explicitly bounded laboratory for checking information inequalities. The output is a collection of exact derivation certificates, including an honest record if every result is already implied by elementary inequalities.

**Status:** Needs further verification; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Entropy and conditional mutual information; Polyhedral cones and rational linear algebra; Linear programming dual certificates; Copy-lemma semantics.

**Verification:** Proof, Exact computation. [How to check a result](Q-FORMAL-003.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The finite specification supports exact checking and automated generation. Usefulness within the stated support and coefficient limits remains unverified; an information theorist should assess these limits and existing coverage before execution.

**Computing requirements and limits:** Six variables produce 63 nonempty entropy coordinates. There are 6 + choose(6,2)*2^4 = 246 elemental Shannon rows; candidate sums grow combinatorially with support. Stream and deduplicate, record exact arithmetic bit growth, and impose a later measured resource cap. No CPU/GPU time or monetary budget is estimated.

**Human review:** High for semantic alignment and novelty; moderate for exact certificates.

</details>

<a id="q-formal-104"></a>

### [Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization](Q-FORMAL-104.md)

[Dynamics on networks and collective behavior](../domains/net.md#net-dynamics) · Literature-origin question

How dense must a network be to make identical phase oscillators synchronize from almost all starting phases? Three quarters of all possible neighbors is sufficient; proving that this universal threshold cannot be lowered remains open.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Kuramoto gradient dynamics, equilibria and stability modulo a continuous symmetry; Circulant matrices, Fourier diagonalization and exact algebraic or certified interval arithmetic; The difference between an equilibrium, a local minimum, a second-order critical point and almost-everywhere convergence.

**Verification:** Proof, Exact computation. [How to check a result](Q-FORMAL-104.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** AI can suggest graph families and derive spectra while exact arithmetic checks stability. Expert review must prevent a marginal linear condition from being mistaken for a nonlinear obstruction.

**Computing requirements and limits:** Suggested pilot cap: 1,000 (graph,q) pairs, n≤32, one CPU-hour and 8 GiB memory, with timeouts marked unresolved. These are proposed limits, not benchmarks. Small circulant spectra support inexpensive numerical filtering, but exact sign certificates and proofs about all graph sizes may be substantially harder.

**Human review:** Medium for a strict finite-dimensional certificate after conventions are fixed; high for marginal equilibria, graph-size limits or a universal threshold proof.

</details>

<a id="q-formal-201"></a>

### [A linear bound for avoiding a specified automaton state](Q-FORMAL-201.md)

[Algorithms and data structures](../domains/cs.md#cs-alg) · Literature-origin question

A resettable finite machine can be driven away from a chosen state. The question is whether fewer than twice as many input symbols as states always suffice. A single small counterexample would be decisive; an unsuccessful sample search would not establish the bound.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Actions of words on subsets of a finite set; Strong connectivity, synchronization and breadth-first search; Distinguishing shortest avoiding words from shortest reset words.

**Verification:** Exact computation, Proof. [How to check a result](Q-FORMAL-201.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Transition-table generation and exact distance checks are well specified, but useful family selection needs an automata specialist and the general conjecture is difficult.

**Computing requirements and limits:** For one n-state instance, exact image-subset exploration uses at most 2^n subsets; at n=14 this is 16,384 possible subsets. Checking one instance is finite, while exhaustive enumeration of all transition tables is much larger. Proposed stop limits are 1,000 instances, 512 MiB memory and four elapsed hours, whichever is reached first. These are proposed ceilings, not measured requirements or performance claims.

**Human review:** Moderate for a single transition table and independently reproduced distance; high for a universal structural theorem.

</details>

<a id="q-formal-203"></a>

### [The sharp triple rendezvous bound for binary synchronizing automata](Q-FORMAL-203.md)

[Algorithms and data structures](../domains/cs.md#cs-alg) · Literature-origin question

How long must a resettable two-letter machine wait before some three starting states can be brought together? A recent construction reaches floor(4n/3); the matching upper bound is still conjectural.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Pair and triple subset automata; Breadth-first search and distance potentials; Permutation cycle types, transformation rank and synchronization tests.

**Verification:** Exact computation, Proof. [How to check a result](Q-FORMAL-203.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** A small certificate graph makes candidate verification attractive, but the recent preprint and its finite-coverage table need review before choosing an untested class. The bounded search is an untested proposal, not a prediction of solving the full conjecture.

**Computing requirements and limits:** For n=13, the graph of nonempty subsets of size at most three has 13+78+286=377 vertices. This bounds the checker graph, not the number of machines to search. Proposed ceilings are 1,000 instances, 512 MiB memory and four elapsed hours. Stop before exceeding any ceiling; no run or timing has been measured.

**Human review:** Low to moderate for one finite certificate; high for exhaustive classification or a universal theorem.

</details>

<a id="q-formal-204"></a>

### [The optimal randomized stretch for two online bins](Q-FORMAL-204.md)

[Randomized, online and distributed algorithms](../domains/cs.md#cs-random) · Literature-origin question

Items arrive one at a time and must immediately be assigned to one of two bins. They could have fit in two unit bins if their future sizes were known. How much extra load is unavoidable when the online algorithm may randomize?

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Competitive analysis with oblivious adversaries; Finite zero-sum games, rational linear programming and dual certificates; Online information constraints and offline feasibility of a packing.

**Verification:** Exact computation, Proof. [How to check a result](Q-FORMAL-204.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Finite games offer exact certificates and a bounded entry point, but a game model that leaks future input information or omits policies yields invalid bounds.

**Computing requirements and limits:** The input pool is capped at 200 sequences of at most eight items. Build the complete online-history representation for that pool only, stopping before 20,000 history states, 1 GiB memory or four elapsed hours. Exact arithmetic can be substantially costlier than floating-point search. These are proposed limits, not measured costs; a small grid is not a guarantee of a small policy space.

**Human review:** High for the reduction from a computational game to the randomized online claim; lower for arithmetic once the game is sound.

</details>

<a id="q-formal-205"></a>

### [A complete graphical criterion for the front-door formula](Q-FORMAL-205.md)

[Causal inference and identifiability](../domains/stat.md#stat-causal) · Literature-origin question

The front-door formula can identify an intervention effect even with hidden confounding, but its familiar sufficient graphical conditions do not describe every graph where the formula works. The task is to find a complete graph-based rule for this specific formula.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Causal DAGs, latent variables and intervention by truncated factorization; Conditional independence, d-separation and identification versus formula validity; Exact marginalization and symbolic rational-function identities.

**Verification:** Exact computation, Proof. [How to check a result](Q-FORMAL-205.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Exact small models and symbolic discrepancies are inspectable, but causal semantics and universal quantifiers need a specialist before any claimed graphical theorem.

**Computing requirements and limits:** With at most five binary nodes, a single full joint table has at most 32 assignments. Symbolic expression growth can still be substantial. Proposed ceilings are 200 graphs, 100 rational parameter assignments per graph, 50,000 expanded polynomial terms per identity, 1 GiB memory and four elapsed hours. Stop at the first ceiling and retain an unresolved label. No runtime or cost has been measured.

**Human review:** Moderate for a small countermodel; high for necessary-and-sufficient graph criteria and cardinality-independent proofs.

</details>

<a id="q-formal-328"></a>

### [Exact capacity of the independent binary deletion channel](Q-FORMAL-328.md)

[Classical information theory](../domains/info.md#info-shannon) · Literature-origin question

When missing bits leave no position markers, even the maximum reliable information rate is unknown. The half-deletion case provides a fixed parameter at which stronger bounds would be useful.

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Information theory and coding theorems; Entropy rates and finite-state processes; Rigorous numerical bounds and exact certificate arithmetic.

**Verification:** Proof, Exact computation. [How to check a result](Q-FORMAL-328.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The published computation supplies concrete methods and checking obligations. Reviewing its assumptions and obtaining complete inputs should precede a new attempt.

**Computing requirements and limits:** No estimate has been measured. Small analytic and certificate checks can be separated from large finite-window enumeration, whose state count grows exponentially. Full source replay requires specialist numerical infrastructure.

**Human review:** High: an information theorist must review the reduction, while numerical evidence needs an independent replay.

</details>

<a id="q-formal-510"></a>

### [Optimal acceleration from predetermined gradient-descent stepsizes](Q-FORMAL-510.md)

[Optimization and operations research](../domains/math.md#math-opt) · Literature-origin question

How much speed can gradient descent gain by changing only its predetermined step lengths? The answer would identify a basic limit of this widely used optimization method.

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Smooth convex optimization and worst-case oracle complexity; Uniform asymptotic estimates and proof certificates for optimization inequalities.

**Verification:** Proof, Exact computation, Numerical evidence. [How to check a result](Q-FORMAL-510.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The problem is explicit and has reusable published arguments. Assessing a specific AI attempt requires a narrower, independently checked target.

**Computing requirements and limits:** Unmeasured. Symbolic work and small numerical diagnostics are possible, but global schedule optimization can be expensive. No hardware, runtime or solution-cost estimate is available.

**Human review:** High for a new general rate theorem; finite algebraic certificates may be easier to audit.

</details>

<a id="q-formal-511"></a>

### [A rank-47 decomposition for 4x4 matrix multiplication in characteristic zero](Q-FORMAL-511.md)

[Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit) · Literature-origin question

Can two 4x4 matrices be multiplied using 47 bilinear products instead of the 48 in current characteristic-zero constructions?

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Bilinear algorithms and tensor rank; Exact rational or algebraic-number arithmetic; Polynomial identity checking.

**Verification:** Exact computation, Proof. [How to check a result](Q-FORMAL-511.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Exact certificates make results easier to inspect than searches. Published computational attempts provide context, but do not imply that a new construction is likely.

**Computing requirements and limits:** A fixed candidate has a finite exact checker; search cost is unconstrained and may be substantial. Coefficient growth can also make checking expensive. No project runtime or budget is measured.

**Human review:** Moderate for a compact exact construction; much higher for an impossibility claim or a complicated coefficient field.

</details>

<a id="q-math-003"></a>

### [Determine the four-color triangle Ramsey number R(3,3,3,3)](Q-MATH-003.md)

[Extremal and Ramsey theory](../domains/math.md#math-comb-ext) · Literature-origin question

How many vertices force a same-colored triangle when every pair is assigned one of four colors? Existing constructive and universal bounds leave a gap.

**Status:** Open after a scoped check; checked 2026-10-13. **Assessment evidence:** Untested forecast.

**Background:** Extremal graph theory and Ramsey bounds; Multicolor edge encodings and symmetry; SAT/constraint programming and certificate checking for computational approaches; Literature on critical colorings and structural upper-bound arguments.

**Verification:** Proof, Exact computation. [How to check a result](Q-MATH-003.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Precise objects and locally verifiable constructions offer a credible role for tool-using AI in literature synthesis, encoding audit, or designing bounded subproblems. The exact unrestricted target requires substantial combinatorial expertise and may exceed available resources.

**Computing requirements and limits:** Unassessed and potentially substantial. The naive space at N vertices is 4^(N*(N-1)/2). Structural restrictions, solver complexity, certificate storage, and checking cost require separate planning. No hardware, runtime, fee, or affordable-solution promise is made.

**Human review:** High for universal upper bounds; low for a supplied finite lower-bound witness after its complete encoding is established.

</details>

<a id="q-math-104"></a>

### [Quadratic generation of matroid toric ideals: the weak White conjecture](Q-MATH-104.md)

[Commutative and homological algebra](../domains/math.md#math-alg-comm) · Literature-origin question

Ask whether every algebraic relation among matroid bases can be built from relations involving just two bases at a time. Recent counterexamples to stronger statements make the exact choice of permitted moves essential.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Matroid axioms, bases and representability; Toric ideals and binomial ideal membership; Fibers of monomial maps; Exact algebraic computation and certificate design.

**Verification:** Proof, Exact computation. [How to check a result](Q-MATH-104.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The statement is exact and supports bounded algebraic investigations, but the unrestricted conjecture is difficult. A useful initial role is auditing variants, small certificates and candidate lemmas under expert supervision.

**Computing requirements and limits:** No general feasible resource bound is asserted. Basis sets, high-degree fibers and ideal-membership calculations can grow rapidly. Any future finite search must first declare rank, ground-set size, fiber degree, representation and stopping limits.

**Human review:** High: both combinatorial and commutative-algebra expertise may be needed, especially for computational nonmembership claims.

</details>

<a id="q-math-202"></a>

### [A triangle-free 40-vertex graph with independence number at most nine](Q-MATH-202.md)

[Extremal and Ramsey theory](../domains/math.md#math-comb-ext) · Literature-origin question

One 40-vertex graph could decide which of two remaining values is R(3,10). Checking such a graph is easier than proving that every graph fails.

**Status:** Open after a scoped check; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Ramsey graphs; Exact clique and independent-set algorithms; SAT certificates; Reproducible seed selection.

**Verification:** Exact computation, Proof, Public data. [How to check a result](Q-MATH-202.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** There is a decisive compact witness, but existing extensive searches make an arbitrary small neighborhood uncertain. Validate the checker and justify seed selection first.

**Computing requirements and limits:** Proposed cap: 8 CPU-hours and 16 GiB RAM, at most 20 seeds. There are 780 possible edges. Triangle checking is small; excluding independent ten-sets needs exact branch-and-bound or a checked SAT certificate. No runtime guarantee is made.

**Human review:** Moderate for a graph with independent code and certificates; very high for universal nonexistence.

</details>

<a id="q-model-201"></a>

### [Complete EFX for four additive goods agents](Q-MODEL-201.md)

[Mechanism design and fair allocation](../domains/econ.md#econ-mech) · Literature-origin question

Can four people always divide indivisible goods so that removing any one item from someone else's share eliminates envy? A finite number of goods still leaves infinitely many possible valuations.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Additive fair division and the distinction between EFX, EFX0, EF1 and partial allocation; Linear real arithmetic, exact certificates and coverage proofs for a finite union of regions; Symmetry reductions that preserve one common labeling of goods across all agents.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-201.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Exact linear constraints let AI propose regions and allocation menus while a separate checker tests each claim. A specialist must first judge whether the chosen region adds anything to known reductions.

**Computing requirements and limits:** First-pilot policy: one region, at most 128 menu allocations, one CPU-hour and 8 GiB memory, then stop with an unresolved region if necessary. These are proposed resource caps, not measured requirements or a promise of completion. The complete allocation space at m=10 has 4^10=1,048,576 assignments; exhaustive region coverage may require much more.

**Human review:** High for a universal regional proof: the certificate checker, encoding and region cover all matter. A small concrete allocation is easy to check but does not prove existence for other values.

</details>

<a id="q-model-202"></a>

### [Complete EFX for more than four common bi-valued chore agents](Q-MODEL-202.md)

[Mechanism design and fair allocation](../domains/econ.md#econ-mech) · Literature-origin question

When every chore is either cheap or expensive for each person, and everyone uses the same two cost levels, can five or more people always obtain exact EFX fairness? The positive four-person result gives a concrete structural starting point.

**Status:** Source reports open; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Additive chore allocation, EFX deletion semantics and common versus personalized values; Finite constraint search and exact integer arithmetic; The item-type decomposition and insertion arguments in the four-agent proof.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-202.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** First check whether the proposed five-agent, eleven-chore, ratio-three pilot is covered by an existing special-case theorem, and select a useful unresolved class. Exact integer checks could then support AI-generated cost patterns and proposed extensions of the four-agent structure.

**Computing requirements and limits:** Suggested first cap: 100 cost-pattern multisets, one CPU-hour and 8 GiB total memory, stopping unresolved instances explicitly. These are proposed limits, not timing estimates. There are 2^55 labeled five-by-eleven cost matrices and 5^11=48,828,125 allocations per fixed matrix; exhaustive global search is not described as cheap.

**Human review:** Individual positive allocations are straightforward; negative instances and structural lemmas require exhaustive coverage and expert review.

</details>

<a id="q-model-204"></a>

### [EFX and Pareto optimality for personalized bi-valued goods](Q-MODEL-204.md)

[Mechanism design and fair allocation](../domains/econ.md#econ-mech) · Literature-origin question

Can indivisible goods always be shared so that envy disappears after removing any one good from another person's bundle, while no reassignment can benefit someone without harming another?

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Additive fair division, EFX and Pareto dominance; Exact finite optimization and certificates of exhaustive coverage.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-204.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The problem is explicit and has reusable published arguments. Assessing a specific AI attempt requires a narrower, independently checked target.

**Computing requirements and limits:** Unmeasured. A fixed n-agent, m-good instance has n^m complete assignments. Exact small-instance checking may be manageable; growth and general Pareto verification can be expensive.

**Human review:** Moderate for a small fully enumerated instance; high for a general theorem or a large exhaustive certificate.

</details>

<a id="q-model-492"></a>

### [Nonlinear stationary axisymmetric tidal response of Kerr black holes](Q-MODEL-492.md)

[Gravitation and spacetime theory](../domains/phys.md#phys-grav) · Literature-origin question

How does a spinning black hole respond beyond first order to a steady surrounding gravitational tide? A complete treatment must connect the spacetime solution with well-defined response coefficients.

**Status:** Open after a scoped check; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** General-relativistic perturbation theory and horizon boundary conditions; Multipole expansions, worldline EFT and symbolic tensor calculation.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-492.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Symbolic tensor manipulation can assist finite-order field equations and matching checks. Choosing an informative sector and interpreting its coefficients require GR and EFT expertise; no AI trial has been run.

**Computing requirements and limits:** A finite-order symbolic calculation may start locally, but expression growth can dominate memory. No runtime or budget has been measured.

**Human review:** High: a specialist must inspect gauge choices, operator identifiability and matching.

</details>

<a id="q-model-493"></a>

### [Three-copy undistillability of the Werner endpoint](Q-MODEL-493.md)

[Quantum information theory](../domains/info.md#info-quant) · Literature-origin question

Can three copies unlock entanglement distillation that a single copy cannot achieve? This finite-copy question probes the limits of entanglement as a communication resource.

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Partial transpose, Schmidt rank, LOCC and matrix inequalities; Tensor indices, unnormalized partial traces and certified arithmetic.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-493.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The explicit algebra permits symbolic checks and candidate generation, but the unresolved nonnormal sector and recent claims require careful preparation.

**Computing requirements and limits:** Unmeasured. At d=4 the coefficient matrix has 64 rows and columns; low-rank parameterization reduces storage but does not make global optimization easy. No runtime or cost is forecast.

**Human review:** High for a general proof; an explicit small witness is more localized but still requires statement alignment.

</details>

<a id="q-formal-102"></a>

### [Verify the equal-block language of a locally constrained tree-adjoining grammar](Q-FORMAL-102.md)

[Formal language and grammar theory](../domains/cog.md#cog-lang) · Known-result calibration

A small formal grammar coordinates three equal blocks of symbols. Making its local restrictions explicit lets readers check strings and derivations without confusing a grammar model with evidence about human language.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Ordered trees, terminal yields and structural induction; Adjoining versus substitution and context-free rewriting; Weak and strong generative capacity; the role of formal grammars in linguistic modeling.

**Verification:** Proof, Exact computation. [How to check a result](Q-FORMAL-102.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Symbolic assistance fits the inductive target and short examples, but a reviewer should first approve transcription of the scanned grammar and its node restrictions.

**Computing requirements and limits:** Small symbolic trees and six derivation records; no parser training. Local execution should suffice for this bounded presentation, but nothing has been timed. General grammar induction or exhaustive unrestricted derivation search would be different tasks.

**Human review:** Moderate: the small trees are inspectable, but local restrictions and their inheritance require formal-language expertise.

</details>

<a id="q-model-002"></a>

### [Certify deficiency-zero hypotheses for small reaction networks](Q-MODEL-002.md)

[Reaction-network and kinetics theory](../domains/chem.md#chem-reaction) · Known-result calibration

Turn a reaction diagram into a checkable explanation of whether a known structural theorem applies. This links chemistry and biology to graph algorithms and exact linear algebra without treating a model as an observed mechanism.

**Status:** Known result in literature; checked 2026-10-13. **Assessment evidence:** Untested forecast.

**Background:** Directed graphs and strongly connected components; Exact rank, conservation laws and stoichiometric subspaces; Mass-action ODEs, complex balance and relative local stability.

**Verification:** Proof, Exact computation. [How to check a result](Q-MODEL-002.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The structural part is well suited to generated code and exact certificates, but a reviewer must first approve representation conventions and the limited theorem conclusion.

**Computing requirements and limits:** Small exact integer matrices and graph traversals under the declared input bounds. Local laptop-class work is an untested planning assumption; larger symbolic equilibrium computations are outside scope.

**Human review:** Moderate for a CRNT specialist; a graph or linear-algebra reviewer can check only the structural layer.

</details>

<a id="q-model-010"></a>

### [Reproduce equilibrium branches in an energy-balance climate model](Q-MODEL-010.md)

[Climate dynamics and reduced models](../domains/earth.md#earth-climate) · Known-result calibration

Reproduce equilibrium branches of a published low-dimensional climate model and put error bounds around its folds. The exercise illustrates why local sensitivity becomes unreliable near a turning point; it does not estimate a threshold for the Earth's climate.

**Status:** Known result in literature; checked 2026-10-14. **Assessment evidence:** Untested forecast.

**Background:** Scalar equilibrium stability and the inverse function theorem; Differentiation of composite smooth functions and physical-unit bookkeeping; Interval arithmetic or another rigorous root-isolation method for transcendental functions.

**Verification:** Proof, Exact computation, Numerical evidence. [How to check a result](Q-MODEL-010.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The finite interval and explicit functions make a rigorous reproduction feasible to specify. A validated transcendental arithmetic environment and resolution of the source's derivative inconsistency are prerequisites for reliable certificates.

**Computing requirements and limits:** One-dimensional interval subdivision and validated evaluation of tanh and exp. A local validated-numerics environment is a plausible starting resource class, but total subdivisions, precision, runtime and cost are unmeasured and must be reported in any future attempt.

**Human review:** High relative to the small model: a reviewer must inspect the completeness of numerical enclosures and the distinction between a source reproduction and a real-world claim.

</details>

<a id="exploratory"></a>

## Exploratory

<a id="q-model-491"></a>

### [Structured resonances and avalanche diagnostics in the quasiperiodic XXZ chain](Q-MODEL-491.md)

[Condensed matter and materials theory](../domains/phys.md#phys-cond) · Literature-origin question

A small thermal region may erase memory in an otherwise localized quantum chain. Two diagnostics disagree about its spread; the source asks how quasiperiodic resonances change the explanation.

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Quantum spin chains and thermalization; Reduced states, entropy and correlations; Perturbation theory and numerical error analysis.

**Verification:** Numerical evidence, Proof. [How to check a result](Q-MODEL-491.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Literature comparison, algebra and reproducible numerical diagnostics offer possible assistance; discovering a correct mechanism is uncertain.

**Computing requirements and limits:** Small-chain calculations may fit a workstation; large phase ensembles and asymptotic scaling can require substantial resources. This is an untested planning estimate, not a runtime or budget measurement.

**Human review:** High: specialists must assess the physical interpretation as well as numerical reproducibility.

</details>

<a id="q-model-494"></a>

### [Thermodynamic pairing order in the stripe regime of the square-lattice Hubbard model](Q-MODEL-494.md)

[Condensed matter and materials theory](../domains/phys.md#phys-cond) · Literature-origin question

Electron stripes and superconducting pairing compete or coexist in the Hubbard model. Pairing on a finite cluster may disappear as both dimensions grow; the source leaves this limit unresolved.

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Fermionic many-body Hamiltonians; Pair correlations and symmetry breaking; Variational Monte Carlo or tensor-network methods; Finite-size scaling and error analysis.

**Verification:** Numerical evidence, Proof. [How to check a result](Q-MODEL-494.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** AI may help compare methods, implement diagnostics and audit uncertainty; full ground-state inference remains demanding.

**Computing requirements and limits:** Substantial GPU/HPC resources may be necessary. Source Table 4 reports roughly 500 H200 GPU-hours for one 144-site training case and 10,000 for a 288-site case; these are author estimates, not project measurements or promised budgets.

**Human review:** High: review requires many-body expertise and access to reproducible numerical evidence.

</details>

<a id="q-model-495"></a>

### [Predictive mixed longitudinal-transverse intermittency exponents](Q-MODEL-495.md)

[Fluid and plasma theory](../domains/phys.md#phys-fluid) · Literature-origin question

Rare intense fluctuations govern turbulent mixing and dissipation. Their longitudinal and transverse statistics need a joint predictive account rather than separate fitted scaling curves.

**Status:** Open after a scoped check; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Incompressible turbulence, structure functions and multifractal modeling; Statistical convergence, Reynolds-number scaling and numerical resolution.

**Verification:** Proof, Numerical evidence. [How to check a result](Q-MODEL-495.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** Symbolic consistency checks and comparison of statistical closures offer bounded tasks. Predicting universal exponents requires more than fitting numerical data; this proposed AI role has not been tested.

**Computing requirements and limits:** Symbolic checks and analysis of selected statistics may be modest; new well-resolved high-Reynolds-number DNS is a major computing task. No costs or runtimes are measured.

**Human review:** High: statistical and fluid-dynamical assumptions require specialist assessment.

</details>

<a id="q-model-496"></a>

### [Efficient passive initialization of a three-dimensional quantum memory](Q-MODEL-496.md)

[Quantum information theory](../domains/info.md#info-quant) · Literature-origin question

A memory is useful only if information can be loaded into its protected state. This asks whether the proposed passive memory can be initialized without preparation taking prohibitively long.

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Stabilizer codes, syndrome sectors and Gibbs states; Local thermal dynamics, mixing estimates and asymptotic error bounds.

**Verification:** Proof, Numerical evidence. [How to check a result](Q-MODEL-496.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** AI may help track the construction's hypotheses and test local lemmas. The missing asymptotic preparation argument is substantial.

**Computing requirements and limits:** Unmeasured. Small instances can test definitions, while exact state-space simulation grows rapidly. Analytical bounds may avoid full simulation; no affordable full-scale run is promised.

**Human review:** High: the protocol must fit the code construction while its error and resource estimates remain uniform in the declared limit.

</details>

<a id="unassessed"></a>

## Not yet assessed

<a id="q-formal-010"></a>

### [Deterministic polynomial-time identity testing for general arithmetic circuits](Q-FORMAL-010.md)

[Circuit and algebraic complexity](../domains/cs.md#cs-complex-circuit) · Literature-origin question

A compact algebraic expression may expand into too many terms to list. Can one always decide, efficiently and without randomness, whether all terms cancel?

**Status:** Source reports open; checked 2026-10-20. **Assessment evidence:** Untested forecast.

**Background:** Arithmetic circuits, formal degree, rational encodings and Turing-machine bit complexity; Derandomization, hitting sets and algebraic complexity; The structural hypotheses of the chosen restricted circuit model.

**Verification:** Proof, Exact computation. [How to check a result](Q-FORMAL-010.md#verification).

<details>
<summary>Review notes and full computing requirements</summary>

**Reason for this priority:** The card records the literature and verification conditions. No task-specific model evaluation or evidence of tractability is available.

**Computing requirements and limits:** Symbolic examples and implementations can support preparation, but no resource estimate is established for discovering or validating a general algorithm. Explicit expansion and exhaustive enumeration can be exponential.

**Human review:** Specialist review is required for the structural argument and the uniform complexity bound.

</details>

<a id="browse-by-method"></a>

## Browse by method

This table covers the detailed problem entries. Other candidates have not received an AI suitability assessment. The methods describe possible approaches, not measured capability.

| Method | Cards |
| --- | --- |
| Algorithms | [Deterministic polynomial-time identity testing for general arithmetic circuits](Q-FORMAL-010.md)<br>[The optimal randomized stretch for two online bins](Q-FORMAL-204.md)<br>[Optimal acceleration from predetermined gradient-descent stepsizes](Q-FORMAL-510.md)<br>[Enumerate equilibria of a supplied rational bimatrix game](Q-MODEL-003.md)<br>[EFX and Pareto optimality for personalized bi-valued goods](Q-MODEL-204.md) |
| Bounds | [Binary length-12 covering codes of radius three](Q-CODE-201.md)<br>[Ternary length-seven covering codes of radius two](Q-CODE-202.md)<br>[Quaternary length-six covering codes of radius two](Q-CODE-203.md)<br>[The optimal randomized stretch for two online bins](Q-FORMAL-204.md)<br>[Exact capacity of the independent binary deletion channel](Q-FORMAL-328.md)<br>[Optimal acceleration from predetermined gradient-descent stepsizes](Q-FORMAL-510.md)<br>[Determine the four-color triangle Ramsey number R(3,3,3,3)](Q-MATH-003.md)<br>[Exact mixing certificates for small positive Markov chains](Q-MATH-102.md)<br>[A triangle-free 40-vertex graph with independence number at most nine](Q-MATH-202.md)<br>[The exact ten-point Heilbronn number in the unit square](Q-MATH-203.md)<br>[Improve the lower bound for R(4,6) with a 36-vertex graph](Q-MATH-204.md)<br>[Thermodynamic pairing order in the stripe regime of the square-lattice Hubbard model](Q-MODEL-494.md)<br>[Efficient passive initialization of a three-dimensional quantum memory](Q-MODEL-496.md) |
| Certificate checking | [Binary length-12 covering codes of radius three](Q-CODE-201.md)<br>[Ternary length-seven covering codes of radius two](Q-CODE-202.md)<br>[Quaternary length-six covering codes of radius two](Q-CODE-203.md)<br>[Build a bounded exact copy-lemma certificate census](Q-FORMAL-003.md)<br>[Check common quadratic Lyapunov certificates for small matrix polytopes](Q-FORMAL-101.md)<br>[Verify the equal-block language of a locally constrained tree-adjoining grammar](Q-FORMAL-102.md)<br>[A linear bound for avoiding a specified automaton state](Q-FORMAL-201.md)<br>[The sharp triple rendezvous bound for binary synchronizing automata](Q-FORMAL-203.md)<br>[The optimal randomized stretch for two online bins](Q-FORMAL-204.md)<br>[Reproduce the exact Ramsey number R(3,3)=6](Q-MATH-001.md)<br>[Audit exact union-closed-family certificates on at most four elements](Q-MATH-002.md)<br>[Determine the four-color triangle Ramsey number R(3,3,3,3)](Q-MATH-003.md)<br>[Exact finite satisfiability for a small monadic fragment](Q-MATH-101.md)<br>[Exact mixing certificates for small positive Markov chains](Q-MATH-102.md)<br>[Quadratic generation of matroid toric ideals: the weak White conjecture](Q-MATH-104.md)<br>[A 150-point no-three-in-line configuration on a 75 by 75 grid](Q-MATH-201.md)<br>[A triangle-free 40-vertex graph with independence number at most nine](Q-MATH-202.md)<br>[Improve the lower bound for R(4,6) with a 36-vertex graph](Q-MATH-204.md)<br>[Reproduce the CHSH optimum with an exact certificate](Q-MODEL-001.md)<br>[Certify deficiency-zero hypotheses for small reaction networks](Q-MODEL-002.md)<br>[Enumerate equilibria of a supplied rational bimatrix game](Q-MODEL-003.md)<br>[Reproduce equilibrium branches in an energy-balance climate model](Q-MODEL-010.md)<br>[Complete EFX for four additive goods agents](Q-MODEL-201.md)<br>[Complete EFX for more than four common bi-valued chore agents](Q-MODEL-202.md) |
| Classification | [Build a bounded exact copy-lemma certificate census](Q-FORMAL-003.md)<br>[Check twisted-state spectra on Kuramoto cycle networks](Q-FORMAL-103.md)<br>[Audit exact union-closed-family certificates on at most four elements](Q-MATH-002.md) |
| Construction | [Binary length-12 covering codes of radius three](Q-CODE-201.md)<br>[Ternary length-seven covering codes of radius two](Q-CODE-202.md)<br>[Quaternary length-six covering codes of radius two](Q-CODE-203.md)<br>[Deterministic polynomial-time identity testing for general arithmetic circuits](Q-FORMAL-010.md)<br>[Verify the equal-block language of a locally constrained tree-adjoining grammar](Q-FORMAL-102.md)<br>[Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization](Q-FORMAL-104.md)<br>[The sharp triple rendezvous bound for binary synchronizing automata](Q-FORMAL-203.md)<br>[A rank-47 decomposition for 4x4 matrix multiplication in characteristic zero](Q-FORMAL-511.md)<br>[Reproduce the exact Ramsey number R(3,3)=6](Q-MATH-001.md)<br>[Audit exact union-closed-family certificates on at most four elements](Q-MATH-002.md)<br>[Determine the four-color triangle Ramsey number R(3,3,3,3)](Q-MATH-003.md)<br>[Exact mixing certificates for small positive Markov chains](Q-MATH-102.md)<br>[Quadratic generation of matroid toric ideals: the weak White conjecture](Q-MATH-104.md)<br>[A 150-point no-three-in-line configuration on a 75 by 75 grid](Q-MATH-201.md)<br>[A triangle-free 40-vertex graph with independence number at most nine](Q-MATH-202.md)<br>[The exact ten-point Heilbronn number in the unit square](Q-MATH-203.md)<br>[Improve the lower bound for R(4,6) with a 36-vertex graph](Q-MATH-204.md)<br>[Complete EFX for more than four common bi-valued chore agents](Q-MODEL-202.md)<br>[EFX and Pareto optimality for personalized bi-valued goods](Q-MODEL-204.md) |
| Counterexample | [A linear bound for avoiding a specified automaton state](Q-FORMAL-201.md)<br>[The sharp triple rendezvous bound for binary synchronizing automata](Q-FORMAL-203.md)<br>[A complete graphical criterion for the front-door formula](Q-FORMAL-205.md)<br>[Quadratic generation of matroid toric ideals: the weak White conjecture](Q-MATH-104.md)<br>[Complete EFX for four additive goods agents](Q-MODEL-201.md)<br>[Complete EFX for more than four common bi-valued chore agents](Q-MODEL-202.md)<br>[EFX and Pareto optimality for personalized bi-valued goods](Q-MODEL-204.md)<br>[Three-copy undistillability of the Werner endpoint](Q-MODEL-493.md) |
| Exact computation | [Audit finite-sample split likelihood-ratio coverage in a Bernoulli model](Q-FORMAL-002.md)<br>[Build a bounded exact copy-lemma certificate census](Q-FORMAL-003.md)<br>[Check common quadratic Lyapunov certificates for small matrix polytopes](Q-FORMAL-101.md)<br>[Check twisted-state spectra on Kuramoto cycle networks](Q-FORMAL-103.md)<br>[Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization](Q-FORMAL-104.md)<br>[The optimal randomized stretch for two online bins](Q-FORMAL-204.md)<br>[Exact capacity of the independent binary deletion channel](Q-FORMAL-328.md)<br>[A rank-47 decomposition for 4x4 matrix multiplication in characteristic zero](Q-FORMAL-511.md)<br>[Reproduce the exact Ramsey number R(3,3)=6](Q-MATH-001.md)<br>[Audit exact union-closed-family certificates on at most four elements](Q-MATH-002.md)<br>[Exact finite satisfiability for a small monadic fragment](Q-MATH-101.md)<br>[Exact mixing certificates for small positive Markov chains](Q-MATH-102.md)<br>[Transfer-matrix calibration for the one-dimensional Ising model](Q-MATH-103.md)<br>[A 150-point no-three-in-line configuration on a 75 by 75 grid](Q-MATH-201.md)<br>[The exact ten-point Heilbronn number in the unit square](Q-MATH-203.md)<br>[Reproduce the CHSH optimum with an exact certificate](Q-MODEL-001.md)<br>[Certify deficiency-zero hypotheses for small reaction networks](Q-MODEL-002.md)<br>[Enumerate equilibria of a supplied rational bimatrix game](Q-MODEL-003.md)<br>[Reproduce exact Moran fixation probabilities](Q-MODEL-101.md)<br>[Recover the linear stability threshold of triangular Lagrange points](Q-MODEL-102.md)<br>[Complete EFX for four additive goods agents](Q-MODEL-201.md)<br>[Complete EFX for more than four common bi-valued chore agents](Q-MODEL-202.md)<br>[EFX and Pareto optimality for personalized bi-valued goods](Q-MODEL-204.md)<br>[Three-copy undistillability of the Werner endpoint](Q-MODEL-493.md) |
| Finite search | [Binary length-12 covering codes of radius three](Q-CODE-201.md)<br>[Ternary length-seven covering codes of radius two](Q-CODE-202.md)<br>[Quaternary length-six covering codes of radius two](Q-CODE-203.md)<br>[Build a bounded exact copy-lemma certificate census](Q-FORMAL-003.md)<br>[Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization](Q-FORMAL-104.md)<br>[A linear bound for avoiding a specified automaton state](Q-FORMAL-201.md)<br>[The sharp triple rendezvous bound for binary synchronizing automata](Q-FORMAL-203.md)<br>[The optimal randomized stretch for two online bins](Q-FORMAL-204.md)<br>[A complete graphical criterion for the front-door formula](Q-FORMAL-205.md)<br>[A rank-47 decomposition for 4x4 matrix multiplication in characteristic zero](Q-FORMAL-511.md)<br>[Reproduce the exact Ramsey number R(3,3)=6](Q-MATH-001.md)<br>[Audit exact union-closed-family certificates on at most four elements](Q-MATH-002.md)<br>[Determine the four-color triangle Ramsey number R(3,3,3,3)](Q-MATH-003.md)<br>[Exact finite satisfiability for a small monadic fragment](Q-MATH-101.md)<br>[Quadratic generation of matroid toric ideals: the weak White conjecture](Q-MATH-104.md)<br>[A 150-point no-three-in-line configuration on a 75 by 75 grid](Q-MATH-201.md)<br>[A triangle-free 40-vertex graph with independence number at most nine](Q-MATH-202.md)<br>[Improve the lower bound for R(4,6) with a 36-vertex graph](Q-MATH-204.md)<br>[Complete EFX for four additive goods agents](Q-MODEL-201.md)<br>[Complete EFX for more than four common bi-valued chore agents](Q-MODEL-202.md)<br>[EFX and Pareto optimality for personalized bi-valued goods](Q-MODEL-204.md) |
| Formalization | [Reproduce Huang's hypercube degree theorem](Q-FORMAL-001.md)<br>[Verify the equal-block language of a locally constrained tree-adjoining grammar](Q-FORMAL-102.md)<br>[Exact finite satisfiability for a small monadic fragment](Q-MATH-101.md) |
| Model analysis | [Check common quadratic Lyapunov certificates for small matrix polytopes](Q-FORMAL-101.md)<br>[Check twisted-state spectra on Kuramoto cycle networks](Q-FORMAL-103.md)<br>[Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization](Q-FORMAL-104.md)<br>[A complete graphical criterion for the front-door formula](Q-FORMAL-205.md)<br>[Transfer-matrix calibration for the one-dimensional Ising model](Q-MATH-103.md)<br>[Certify deficiency-zero hypotheses for small reaction networks](Q-MODEL-002.md)<br>[Reproduce equilibrium branches in an energy-balance climate model](Q-MODEL-010.md)<br>[Reproduce exact Moran fixation probabilities](Q-MODEL-101.md)<br>[Recover the linear stability threshold of triangular Lagrange points](Q-MODEL-102.md)<br>[Verify the Ornstein–Uhlenbeck transition law and equilibrium](Q-MODEL-103.md)<br>[Structured resonances and avalanche diagnostics in the quasiperiodic XXZ chain](Q-MODEL-491.md)<br>[Nonlinear stationary axisymmetric tidal response of Kerr black holes](Q-MODEL-492.md)<br>[Thermodynamic pairing order in the stripe regime of the square-lattice Hubbard model](Q-MODEL-494.md)<br>[Predictive mixed longitudinal-transverse intermittency exponents](Q-MODEL-495.md)<br>[Efficient passive initialization of a three-dimensional quantum memory](Q-MODEL-496.md) |
| Model construction | [Exact finite satisfiability for a small monadic fragment](Q-MATH-101.md) |
| Numerical computation | [Exact capacity of the independent binary deletion channel](Q-FORMAL-328.md)<br>[Optimal acceleration from predetermined gradient-descent stepsizes](Q-FORMAL-510.md)<br>[The exact ten-point Heilbronn number in the unit square](Q-MATH-203.md)<br>[Reproduce equilibrium branches in an energy-balance climate model](Q-MODEL-010.md)<br>[Structured resonances and avalanche diagnostics in the quasiperiodic XXZ chain](Q-MODEL-491.md)<br>[Thermodynamic pairing order in the stripe regime of the square-lattice Hubbard model](Q-MODEL-494.md)<br>[Predictive mixed longitudinal-transverse intermittency exponents](Q-MODEL-495.md)<br>[Efficient passive initialization of a three-dimensional quantum memory](Q-MODEL-496.md) |
| Proof | [Reproduce Huang's hypercube degree theorem](Q-FORMAL-001.md)<br>[Audit finite-sample split likelihood-ratio coverage in a Bernoulli model](Q-FORMAL-002.md)<br>[Deterministic polynomial-time identity testing for general arithmetic circuits](Q-FORMAL-010.md)<br>[Check common quadratic Lyapunov certificates for small matrix polytopes](Q-FORMAL-101.md)<br>[Verify the equal-block language of a locally constrained tree-adjoining grammar](Q-FORMAL-102.md)<br>[Check twisted-state spectra on Kuramoto cycle networks](Q-FORMAL-103.md)<br>[Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization](Q-FORMAL-104.md)<br>[A linear bound for avoiding a specified automaton state](Q-FORMAL-201.md)<br>[The sharp triple rendezvous bound for binary synchronizing automata](Q-FORMAL-203.md)<br>[A complete graphical criterion for the front-door formula](Q-FORMAL-205.md)<br>[Exact capacity of the independent binary deletion channel](Q-FORMAL-328.md)<br>[Optimal acceleration from predetermined gradient-descent stepsizes](Q-FORMAL-510.md)<br>[Reproduce the exact Ramsey number R(3,3)=6](Q-MATH-001.md)<br>[Determine the four-color triangle Ramsey number R(3,3,3,3)](Q-MATH-003.md)<br>[Exact finite satisfiability for a small monadic fragment](Q-MATH-101.md)<br>[Exact mixing certificates for small positive Markov chains](Q-MATH-102.md)<br>[Transfer-matrix calibration for the one-dimensional Ising model](Q-MATH-103.md)<br>[Quadratic generation of matroid toric ideals: the weak White conjecture](Q-MATH-104.md)<br>[Reproduce the CHSH optimum with an exact certificate](Q-MODEL-001.md)<br>[Certify deficiency-zero hypotheses for small reaction networks](Q-MODEL-002.md)<br>[Enumerate equilibria of a supplied rational bimatrix game](Q-MODEL-003.md)<br>[Reproduce exact Moran fixation probabilities](Q-MODEL-101.md)<br>[Recover the linear stability threshold of triangular Lagrange points](Q-MODEL-102.md)<br>[Verify the Ornstein–Uhlenbeck transition law and equilibrium](Q-MODEL-103.md)<br>[Complete EFX for four additive goods agents](Q-MODEL-201.md)<br>[Complete EFX for more than four common bi-valued chore agents](Q-MODEL-202.md)<br>[EFX and Pareto optimality for personalized bi-valued goods](Q-MODEL-204.md)<br>[Nonlinear stationary axisymmetric tidal response of Kerr black holes](Q-MODEL-492.md)<br>[Three-copy undistillability of the Werner endpoint](Q-MODEL-493.md)<br>[Efficient passive initialization of a three-dimensional quantum memory](Q-MODEL-496.md) |
| Symbolic derivation | [Reproduce Huang's hypercube degree theorem](Q-FORMAL-001.md)<br>[Audit finite-sample split likelihood-ratio coverage in a Bernoulli model](Q-FORMAL-002.md)<br>[Build a bounded exact copy-lemma certificate census](Q-FORMAL-003.md)<br>[Deterministic polynomial-time identity testing for general arithmetic circuits](Q-FORMAL-010.md)<br>[Check twisted-state spectra on Kuramoto cycle networks](Q-FORMAL-103.md)<br>[Determine the sharp connectivity threshold for homogeneous Kuramoto synchronization](Q-FORMAL-104.md)<br>[A complete graphical criterion for the front-door formula](Q-FORMAL-205.md)<br>[Optimal acceleration from predetermined gradient-descent stepsizes](Q-FORMAL-510.md)<br>[A rank-47 decomposition for 4x4 matrix multiplication in characteristic zero](Q-FORMAL-511.md)<br>[Transfer-matrix calibration for the one-dimensional Ising model](Q-MATH-103.md)<br>[Quadratic generation of matroid toric ideals: the weak White conjecture](Q-MATH-104.md)<br>[The exact ten-point Heilbronn number in the unit square](Q-MATH-203.md)<br>[Reproduce the CHSH optimum with an exact certificate](Q-MODEL-001.md)<br>[Reproduce equilibrium branches in an energy-balance climate model](Q-MODEL-010.md)<br>[Recover the linear stability threshold of triangular Lagrange points](Q-MODEL-102.md)<br>[Verify the Ornstein–Uhlenbeck transition law and equilibrium](Q-MODEL-103.md)<br>[Structured resonances and avalanche diagnostics in the quasiperiodic XXZ chain](Q-MODEL-491.md)<br>[Nonlinear stationary axisymmetric tidal response of Kerr black holes](Q-MODEL-492.md)<br>[Three-copy undistillability of the Werner endpoint](Q-MODEL-493.md)<br>[Predictive mixed longitudinal-transverse intermittency exponents](Q-MODEL-495.md) |

