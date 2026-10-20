# A proof draft for K₃(7,2) ≥ 30

20 October 2026. Contribution to [Q-CODE-202](../../docs/cards/Q-CODE-202.md).

The [manuscript](manuscript.md) gives an exact computational exclusion of
unrestricted ternary length-seven radius-two covers with at most 29 words.
Together with the published 34-word construction, it yields

$$
30\le K_3(7,2)\le34.
$$

The draft includes the complete argument, the 34 codewords, and two general
structural lemmas. The exact value and independent scientific assessment
remain open; the contribution has no approved “Machine checked” designation.

[Reproduction instructions](reproduction.md) describe the solver-free
[exact checker](proof/verify.py), certificate, and retained verification
reports. A separate coordinate-comparison checker verifies all 2,187
ambient words. Verification needs Python, NumPy and SciPy, without network
access. [CHECK_REPORT.md](CHECK_REPORT.md) summarizes the actual checks;
[MANIFEST.json](MANIFEST.json) and [verify_manifest.py](verify_manifest.py)
identify and check the distributed files.

The construction is credited to Östergård and Hämäläinen. The lower-bound
work builds on Gijswijt and Polak, Gijswijt's thesis, and the moment and
symmetry methods cited in the manuscript. [NOTICE.txt](NOTICE.txt) and
the accompanying license texts retain the reuse terms.
[ASSISTANCE.md](ASSISTANCE.md) records AI contributions, configuration
evidence and the limits of the reported preliminary human review.
