# Reproduce the exact lower bound and the 34-word cover

## Inputs and environment

The precise claim is Theorem 1 of [manuscript.md](manuscript.md):
there is no unrestricted radius-two cover of $\{0,1,2\}^7$ with
at most 29 words, while the supplied 34-word set is a cover.

The tested environment is Python 3.12.14, NumPy 2.5.4, and
SciPy 1.18.1 on Windows. Python itself is not installed by
[proof/requirements.txt](proof/requirements.txt). A separate virtual
environment is suitable. No paid solver or service is required.
Dependency installation may require network access; verification does
not.

The primary inputs are `proof/certificate.json`,
`proof/orbit-box.json`, the two JSON files under `proof/data/`,
and `proof/known34.txt`. Their exact bytes and all checker sources
are bound by [MANIFEST.json](MANIFEST.json).
The historical paths inside certificate metadata and
[proof/source-map.json](proof/source-map.json) record provenance;
the verifier does not open those paths.

## Commands

From this package's root, first check the delivered files:

```text
python -B verify_manifest.py
```

Then run:

```text
cd proof
python -m pip install -r requirements.txt
python -B verify.py --output verification.json
python -B test_negative_controls.py
```

Run normal Python, without `-O`, `-OO`, or `PYTHONOPTIMIZE`.
The verifier explicitly rejects optimized execution because assertions
must remain active. `-B` only suppresses bytecode files.

The positive replay must exit successfully and report `"pass": true`
in `verification.json`. It must reproduce the exact strict upper bound

```text
-5058649380435826018685689638659
/1276058875953519237987654777869130792960
```

The negative controls must exit successfully, report `"pass": true`
in `negative-controls.json`, and show rejection of all four corruptions:
an invalid alphabet symbol, a word that is too short, a word that is
too long, and one altered integer Gram-factor entry.

The negative-control program bypasses only the initial checksum of
the altered certificate, in memory. It requires the reconstructed
coefficient comparison to reject the mutation. Its temporary copy is
removed on exit, and the original certificate is checked unchanged.

Rerunning writes fresh verification reports and timings. These outputs
will differ from the delivered snapshot's manifest; verify that snapshot
before replay, and use a separate copy if its original reports must
remain unchanged. The mathematical input files are not overwritten.

## What the lower-bound checker reconstructs

The raw scalar and Gram interpretations are proved in Sections 3–4
of the manuscript. Its Sections 5–6 and Appendix A specify the finite
enumeration, exact normalization, and input labels.

| Source | Role |
| --- | --- |
| `proof/verify.py` | Input validation, complete support accounting, exact aggregation, orbit bounds, final contradiction, and separate cover check |
| `proof/lib/check_shell28_certificate.py` | Complete moments through degree four, rooted orbit representatives, literal covering rows, and shell matrices |
| `proof/lib/audit_fivepoint.py` | Equality-pattern canonicalization and exact stabilizer counts |
| `proof/lib/rebuild_scalar_products.py` | Literal cover/Boolean products and exact four-slot ball recurrence |
| `proof/lib/audit_full29_root_scalars.py` | Conditional-square rows and conditional integer cubics |
| `proof/lib/rebuild_radial.py` | Radial moment products for integer shell-count matrices |
| `proof/lib/audit_fourier_pair.py` | Ordered center-pair matrix coefficients |
| `proof/lib/rebuild_fourier_quadratic.py` | Integer reconstruction of Fourier quadratic matrices |

Some source filenames and unused declarations preserve earlier
development history. They do not change the target to 27 or 28.
The accepted target is checked explicitly as `size == 29`.
The retained legacy `check_lower27_certificate.py` is identified in
the source lineage but is not executed by the current proof replay.
No solver snapshot, pickle, NPZ matrix, earlier pass report, or
external work folder is read by `verify.py`.

All 4,753 nonzero scalar weights are checked nonnegative.
The Gram multipliers are supplied as integer factors, giving positive
semidefiniteness algebraically. The checker regenerates the raw matrix
coefficients, contracts the factors, and reconstructs all 4,295
aggregate coefficients. Every bound is recalculated from orbit
cardinalities. Final arithmetic uses Python integers and `Fraction`.
Bounded integer arrays and sparse operations use NumPy and SciPy;
the mathematical counts and their safety bounds are described in
Appendix A.

## Independent upper-bound replay

The upper bound alone uses only the Python standard library:

```text
python -B check_cover.py known34.txt
```

Expected results are 34 distinct centers, 2,187 ambient words tested,
zero uncovered words, and covering radius 2. The histogram of the
distance to the nearest center is
`{"0": 34, "1": 467, "2": 1686}`.
The combined `verify.py` run calls this separate direct-distance checker
as well.

The command-line cover report may print the local input path chosen
by the person running it. The retained combined report does not expose
a host-specific path.

## Trust and limits

This is an exact computational proof with explicit finite inputs.
The acceptance calculation is independent of the optimization programs
used in discovery. Correctness of the mathematical specifications,
ordinary software execution, and hardware remain in its trust basis.
It is not a formal proof-assistant certificate.

The delivered reports are contributor-run evidence. They neither assert
independent human scientific review nor confer the project's approved
“Machine checked” status. Novelty and the exact value of $K_3(7,2)$
remain separate questions.
