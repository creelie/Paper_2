# Nilpotent-free spaces over F3

## Current upload package

[Paper_2 package](Paper_2%20package/README.md) contains the reviewed Hexagon/Overleaf source ZIP, the current PDF, AI provenance, complete Hexagon fields and supporting files for **Linear Algebra and its Applications**. The package records the current proof/check scope and has no margin line numbers. No journal submission or acceptance is claimed. Version: 1.2.0.


**Sole author: Deep Bhattacharjee.** Submission revision 1.1.0, 24 October 2026.

The maximum dimension of a nilpotent-free linear subspace of M3(F3) is **five**. Every subspace of dimension at least six contains a nonzero nilpotent matrix. This disproves the universal finite-field assertion in Wigderson's Conjecture 8 at this particular field and size.

- Manuscript: [Paper_2_Annals.pdf](Paper_2_Annals.pdf)
- Revision DOI: [10.5281/zenodo.23607867](https://doi.org/10.5281/zenodo.23607867)
- Original preprint: [hexagon:2610.00480v1](https://hexagonmath.org/2610.00480v1)
- Original archive: [10.5281/zenodo.23343183](https://doi.org/10.5281/zenodo.23343183)
- Source: [creelie/Paper_2](https://github.com/creelie/Paper_2)

The lower bound has a direct written algebraic proof. The upper bound is an exhaustive computer-assisted proof, with a coverage argument and a complete independent C verifier printed in the manuscript. The Lean development's main theorem trusts two compiled `native_decide` evaluations, in addition to the kernel and its three standard axioms. It is **not** a standard-axioms-only kernel proof. Written arguments added in this revision are not described as newly formalized.

The manuscript uses `aomart`, a self-contained abstract, BibTeX and a vector figure. It is prepared for possible submission to **Annals of Mathematics**. No journal submission or acceptance has occurred. Its special-case scope and computational upper bound may limit its suitability for that journal; acceptance cannot be guaranteed. Linear Algebra and its Applications remains a natural specialist alternative, subject to the author's choice and exclusive-submission rules.

## Reproduce

Python 3 and an ordinary C compiler:

```
python scripts/verify.py
```

This runs the independent exhaustive tree verifier and the exact examples. On Windows the script supports the locally installed Lean-bundled clang when ordinary compiler headers are unavailable. The main verification uses no stochastic choices and no floating-point arithmetic.

Full formal rebuild, with Lean 4.34.1 and the pinned Mathlib dependencies:

```
cd formal
lake build
lake env lean Check.lean > axioms.txt
python audit_axioms.py axioms.txt
```

The audit deliberately permits exactly the two documented native-evaluation axioms. See [VERIFICATION.md](VERIFICATION.md) for the distinction between current executions and preserved prior logs.

Build the manuscript with a TeX distribution containing `aomart`, `aomplain`, TikZ and listings:

```
python scripts/build_manuscript.py
```

The final single ZIP is created only after publication of the Zenodo record and exact PDF checksum confirmation. `scripts/package_submission.py` enforces that order. Build caches, executables, private credentials and nested input ZIPs are excluded.

[SCAN-REPORT.md](SCAN-REPORT.md) records the inventory and screening of C:\FNL_2, including FNL.zip and its nested archives. Screening all titles and abstracts is distinguished from detailed proof auditing of the selected paper.
