# Proof audit, 24 October 2026

## Exact claim

The largest dimension of a linear subspace of M_3(F_3) containing no nonzero nilpotent matrix is five. This refutes the universally quantified finite-field assertion of Wigderson's Conjecture 8 at F=F_3, n=3. It does not establish a maximum over other fields or matrix sizes.

## Mathematical review

1. A nilpotent 3 by 3 matrix has characteristic polynomial t^3. Conversely, trace, second characteristic coefficient and determinant all zero imply X^3=0 by Cayley-Hamilton.
2. The strictly upper triangular subspace has dimension three. A nilpotent-free subspace of dimension at least six is therefore exactly six-dimensional and complementary to it. Projection onto the other six entries is an isomorphism, giving the graph X_C(y) for a unique 3 by 6 coefficient matrix.
3. A search witness is nonzero and supported only on columns already fixed. It therefore applies to every completion. Every open node has all 27 possible next columns. Induction gives complete coverage of all 3^18 coefficient matrices.
4. The independent C implementation tests characteristic-polynomial coefficients, rather than using the original Lean cube expansion. All 3,109,888 nodes close, with no open depth-six leaf. Its recurrence and counts are checked by the executable itself.
5. A second method enumerates all 25,095,280 five-dimensional subspaces of sl_3(F_3) by unique reduced row echelon presentations of their annihilators. Every six-dimensional subspace of M_3(F_3) intersects sl_3(F_3) in dimension at least five. Every enumerated subspace contains a nonzero matrix whose cube is zero.
6. The revised five-parameter construction has a written proof. Trace zero gives a=-(c-d). With p=c-d and z=c+d, the remaining nilpotence equations reduce to -z^2+pe-e^2-b^2=0 and -p+(p+e)b^2=0. The cases b=0 and b^2=1 force the zero matrix or a nonexistent square equal to 2 in F3.
7. The statements about characteristic three are restricted to finite fields where Frobenius is surjective. The earlier sentence claiming Proposition 4.5 over every characteristic-three field was broader than its proof and has been corrected.
8. Elementary finite-field quadratic-form arguments now prove the isotropic-vector fact and the seven-variable zero count in the manuscript, instead of relying only on citations for those deductions.

## Independent exact executions

- All 19,683 matrices over F3: characteristic-coefficient criterion agrees with the direct cube test.
- All 243 construction parameter choices: only the zero matrix is nilpotent; the parameter map is injective.
- All 262,144 F2 coefficient matrices: exactly 128 give nilpotent-free graph spaces.
- All 64 and 15,625 elements in the stated F2 and F5 example spaces: only zero is nilpotent.
- Independent exhaustive search: 3,109,888 nodes, zero open leaves.
- Independent trace-zero enumeration: 25,095,280 subspaces, zero nilpotent-free subspaces.

The supplementary original count over all 678,468,820 six-dimensional subspaces and the complete nilpotent-line histogram were not freshly rerun in this revision. They are not needed for the independently reproduced main proof.

## Novelty and attribution

The conjecture statement was checked directly against arXiv:2609.29177v1, Conjecture 8. The preceding preprint and its code archive are cited. Searches on 24 October 2026 did not identify an independent earlier resolution of this exact pair of parameters. This is a bounded literature search, not an absolute priority certificate or a substitute for refereeing.

The original counterexample and formal development are attributed to Deep Bhattacharjee's project. This audit adds a direct algebraic proof, an independently written C verifier, explicit trust accounting, and scope corrections. It does not claim to have newly discovered the original counterexample.

## Computational and review limits

The exhaustive upper bound is computer-assisted and trusts correct compilation and execution. The archived Lean main theorem uses two native_decide evaluations; it is not a standard-axioms-only kernel proof. The package includes the actual logs, rather than a generic statement that all formal checks are complete. The state of fresh formal re-elaboration is reported separately in FORMAL-STATUS.md.

The engine preserves its formal and human review gates. Journal acceptance and peer review have not been obtained by preparing this package.
