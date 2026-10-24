# Verification and proof scope

24 October 2026; paper revision 1.1.0.

## Current exact executions

- Independent C verifier: 3,109,888 nodes; all 1,740,852 visited depth-six nodes closed; zero open leaves; full 27-way branching at every open internal node. It tests trace, second characteristic coefficient and determinant, independently of the Lean cube expansion. Output: `verification/current/audit-tree.txt`.
- Python: all 19,683 matrices over F3 satisfy equivalence of the characteristic-coefficient and cube tests; all 243 lower-bound parameter choices checked; all 64 F2 and 15,625 F5 example elements checked; all 262,144 F2 coefficient matrices enumerated, with exactly 128 nilpotent-free graph spaces. Output: `verification/current/examples.json`.
- Formal source identity: every Lean source is byte-for-byte identical to the previously rebuilt and re-elaborated development. A fresh 16-theorem axiom inspection was run against those unchanged compiled modules. Outputs: `formal-source-identity.json`, `lean-axioms.txt`, `axiom-audit.txt` in `verification/current/`.

## Prior full executions retained separately

`provenance/prior-verification/` preserves the preceding same-day NilCore build, complete manuscript-module re-elaboration, 16-theorem axiom audit, independent tree check and trace-zero enumeration. The latter covered all 25,095,280 five-dimensional subspaces of sl3(F3). Those files are prior execution records, not mislabeled as new rebuilds in this formatting revision.

The larger 678,468,820-subspace enumeration and the 1,872-count histogram have not been freshly rerun here. They are supplementary historical reports and are not needed for the reproduced main proof. The manuscript distinguishes these facts.

## Trust and scope

The upper bound uses exhaustive finite computation and trusts correct compilation/execution. Lean's main theorem depends on the standard axioms `propext`, `Classical.choice`, `Quot.sound` plus exactly:

```
NilCore.root_eq._native.native_decide.ax_1_1
NilCore.checkCands_eq._native.native_decide.ax_1_1
```

No `sorryAx` is allowed. The five-dimensional example and several ancillary formal results use only the three standard axioms. The new written algebraic proof of the lower bound, the elementary quadratic-form count, and the independent C implementation are separate written arguments/computations, not newly certified Lean theorems. The original formal files and MIT notice are preserved.

The finite result is unconditional in the usual computer-assisted sense: it assumes no unproved mathematical conjecture. It does not remove the computational trust base, prove other finite fields or sizes, or refute the Gerstenhaber-Serezhkin bound.
