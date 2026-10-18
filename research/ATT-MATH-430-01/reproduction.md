# Reproducing the retained arithmetic checks

Use Python 3.10 or later, with only its standard library. The retained helper
runs used Python 3.12.14. Run without `-O`, `-OO` or `PYTHONOPTIMIZE`: their
mathematical assertions must remain active. No installation, network access,
paid service, discovery search or expanded greedy enumeration is needed.

From the repository root:

```powershell
python -B research/ATT-MATH-430-01/replay.py --verify-manifest
```

Substitute your installed Python executable if necessary. The script resolves
all artifacts relative to its own location, so the working directory need
not be the repository root when an absolute script path is supplied.

The final check validates the complete package file list, byte counts and
SHA-256 digests against `manifest.json`; every selected original/publication
digest in `source-map.json`; Python and JSON syntax; and thirteen original
source bindings in the three retained reports. Original hashes identify the
examined working copies. Publication hashes identify the relocated copies,
whose disclosed banners, links and attribution may differ. Matching a hash
does not authenticate the origin or truth of its contents.

The replay imports only the three retained helpers and calls their checking
functions. It never calls their report-writing `main` functions. It redirects
the small-seed helper's file locations to the selected publication tables and
compares complete stable mathematical outcomes with the original reports:

| Check | Expected scope |
| --- | --- |
| Framework probes | 484 mixed interval cases, 16,056 cylinder cases, 280 rectangle cases and the retained explicit failed extensions |
| Small-seed printed arithmetic | Three fixed first-seed-three lifetime proofs and the two displayed first-seed-two finite-case tables, with every retained outcome field |
| First-seed-four printed arithmetic | 353 selected-target pair entries, 208 gap witnesses, 103 original gaps/172 identities, 208 envelope/core and 2,942 transient collision checks, and the compressed 13-gap/22-identity lemma |

Successful execution prints `PASS` for the mapped files, retained arithmetic
and final manifest. The final line explicitly identifies this as a same-team
contributor check. It is not independent or formal verification, a proof of
the whole manuscript, a novelty determination, or human-review approval.
The manuscript and its mathematical appendices remain the candidate argument.

The default command, without flags, is also read-only. When a publication
replay report exists, it compares the stable outcomes, source bindings, map
digest and replay-program digest with that report. Runtime identity and
timings are observations of each run and are not required to be identical.

For a deliberate new publication version, a maintainer may use:

```powershell
python -B research/ATT-MATH-430-01/replay.py --write-report
```

This writes only `reproducibility-results.json`, after the checks succeed.
It does not rewrite the three original result files, source mapping, proofs
or manifest. Record the new report's digest in the publication manifest,
then run `--verify-manifest`. These two flags are mutually exclusive. A changed
source map or replay program requires a new report; an old result must not
be silently applied to a different version. No helper writers or old
snapshot-wide audit commands are needed.

Original replay code is MIT-licensed; this explanatory text follows the
repository's CC BY 4.0 terms. Scientific inputs, AI tool roles and publication
status are recorded in the package's shared provenance and attribution notes.
