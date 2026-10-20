# A proof draft for K₃(7,2) ≥ 30

20 October 2026. Research contribution for
[Q-CODE-202, Ternary length-seven covering codes of radius two](https://github.com/luvLunairs/theory-research-atlas/blob/45c0a5184062519b89be6367220855ba7e0bca8f/docs/cards/Q-CODE-202.md).

## Question and outcome

The target is the unrestricted minimum size of a subset of
$\{0,1,2\}^7$ whose radius-two Hamming balls cover the space.
This contribution gives an exact computational exclusion of all covers
with at most 29 words. Together with the credited published 34-word
cover, the resulting interval is

$$
30\le K_3(7,2)\le34.
$$

This is a partial result prepared for scientific assessment. It does
not determine the exact value, assert priority, or carry the repository's
approved “Machine checked” designation.

Read [manuscript.md](manuscript.md) for the continuous mathematical
argument. It defines the necessary scalar and Gram constraints,
explains the finite orbit enumeration and coefficient reconstruction,
states the exact certificate identity, and completes the contradiction.
The known 34-word cover and two general structural lemmas are included.

## Evidence and checks

[reproduction.md](reproduction.md) gives the exact acceptance procedure
and commands. The [exact checker](proof/verify.py) and its accompanying
files provide the complete inputs for the main claim. It requires Python, NumPy, and SciPy,
but no optimization solver, original research directory, or network
connection during verification.

The construction checker separately compares coordinates for every
one of the 2,187 ambient words. The lower-bound checker regenerates all
4,753 used scalar rows, 33 Gram-factor columns, 101 identities,
4,294 orbit bounds, and 4,295 aggregate coefficients.

[CHECK_REPORT.md](CHECK_REPORT.md) records the checks actually performed
on this version. [MANIFEST.json](MANIFEST.json) binds the supplied
payload; [verify_manifest.py](verify_manifest.py) checks it.
The manifest identifies a version, not a mathematical proof.

## Credit and assistance

The upper construction belongs to Östergård and Hämäläinen.
The lower-bound work builds on Gijswijt and Polak, Gijswijt's thesis,
and the cited moment and symmetry methods. Full references are in
the manuscript. [NOTICE.txt](NOTICE.txt) states the reuse terms;
the complete license texts are included under `LICENSES/`.

[ASSISTANCE.md](ASSISTANCE.md) is the single assistance note for this
version. It records substantive AI-assisted derivation, implementation,
writing, and contributor checking, and links the application-recorded
configuration. No human scientific review is inferred from these checks.
The maintainer's configuration recognition, explicit submission instruction,
and reported preliminary human-review pass are recorded with their limits
in the [assistance note](ASSISTANCE.md#maintainer-recognition-review-report-and-authorization).

## Version and scope

This proof draft revises the 19 October 2026 exploratory manuscript,
retained as `K3-7-2-DRAFT-20261019` at local commit
`e43f0b49ddd1234dd8fed8dd7249d1789f0befe4`.
The primary certificate, orbit bounds, construction, and mathematical
checker are byte-preserved from that version. The present revision
expands the proof and narrows the distributed attachments to its needs.

All 1,089 previously retained seven-coordinate word lists and their
checks remain in the earlier construction archive. No new candidate
cover is proposed here. Restricted classifications and unsuccessful
searches are not premises of the proof and are not distributed again.
This revision is prepared for the authorized draft pull request to
`luvLunairs/theory-research-atlas`. Catalogue acceptance and scientific
review remain pending. The submission adds only this 36-file package;
the earlier exploratory archive is not required to reproduce its proof.
