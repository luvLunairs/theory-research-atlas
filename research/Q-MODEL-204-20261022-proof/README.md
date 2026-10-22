# Complete proofs of partial results for Q-MODEL-204

This contribution contains a continuous mathematical manuscript for the current partial results on complete EFX and global integral Pareto optimality for personalized bivalued goods. **It does not settle unrestricted existence.**

- [Complete proof manuscript](PROOF.md): exact integer compensation, robust cores, balanced EFX completion, arbitrary-ratio residual-capacity theorem, sharp welfare bound, finite-pool obstructions, and the exact three-agent Nash-selector obstruction.
- [Primary-source audit](SOURCES.md).
- [One consolidated assistance and final check report](ASSISTANCE_AND_CHECKS.md), including [model/configuration evidence](execution-metadata.json) and [maintainer recognition and upload authorization](MAINTAINER_RECOGNITION.md).
- [Scientific evidence archive](evidence.zip), [latest replay report](replay-report.json), [independent AI audit](INDEPENDENT_AUDIT.md), and [exact file manifest](manifest.json).

The mathematical proof is self-contained. The archive preserves earlier proof inputs, Python checkers, exact certificates and outputs. Python 3.10 or newer and NumPy are needed to repeat the retained computations; the recorded run used Python 3.12.14 and NumPy 2.3.5.

From the repository root:

```powershell
python research/Q-MODEL-204-20261022-proof/verify_package.py
python research/Q-MODEL-204-20261022-proof/reproduce.py --jobs 2
```

The replay creates fresh files under `work/`, verifies all nine scientific outputs exactly apart from timing fields, and leaves this package unchanged. Package integrity and repository consistency checks do not confer the project's **Machine checked** label or human scientific approval.

This is a research-progress contribution under the project's [contribution guide](../../CONTRIBUTING.md). The stable target is [Q-MODEL-204](../../docs/candidates/Q-MODEL-204.md). The ordinary research-update route does not require modifying structured source records or changing the target's unresolved status. Submission does not imply acceptance or authorization to merge.
