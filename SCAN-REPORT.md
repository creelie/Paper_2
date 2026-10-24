# FNL_2 inventory and candidate screening

24 October 2026. This report separates archive integrity/inventory, source screening and detailed mathematical verification. It does not certify all papers or promise Annals acceptance.

## Coverage

- C:\FNL_2\FNL.zip: 156 entries; every entry CRC-tested successfully. The inventory and outer SHA256 are in `provenance/FNL-inventory.json` and `outer-archive-check.json`.
- Its nested `FNL/CLAUDE PAPERS.zip`: 786 entries in 41 paper collections. Inventory: `provenance/claude-papers-inventory.json`.
- All five larger nested archives and the fifty unique journal-source ZIP variants also passed independent CRC checks (`provenance/nested-archive-checks.json`).
- Fifty unique journal-source ZIP variants were extracted for screening, containing 118 TeX sources. All 41 collections were screened at title/abstract level, with theorem/dependency inspection of the shortlisted papers. `candidate-screen.json` records source-archive SHA256 values and extracted titles/abstracts.
- The three newer audit packages in FNL.zip were inspected: nilpotent-free F3, SYM null projection, and the Poisson-brane compatibility audit. Paper_2 uses the newer F3 revision, not the older nested source.
- The eight-paper scoped-revision archive and the separate Grundy strong-product package were inventoried. Grundy is already Paper_1.
- Source archives are unchanged. Original metadata in the collection index is historical input, not a verification of publication, acceptance, priority or correctness.

## Selection and changed literature finding

Paper_2 is the nilpotent-free M3(F3) result. Its exact finite theorem, written reduction, direct five-dimensional construction, exhaustive verifier and formal trust disclosure form a coherent complete result. A prior full re-elaboration and independent trace-zero enumeration are preserved; new finite checks and an axiom inspection are recorded separately. The specialist LAA venue in the prior package was not evidence of journal acceptance. Annals is the requested target, whose editorial significance threshold remains uncertain.

The Wormald paper initially ranked highly because of its all-regular-tournament determinant identity and exact cyclic limit. A fresh primary-source check found Alexander Divoux and Shouda Wang, *The maximum number of Hamiltonian cycles in tournaments*, [arXiv:2610.23755v1](https://arxiv.org/html/2610.23755v1), submitted 16 October 2026. Its main theorem states the asymptotic constant cosh(1)/cos(1), and Sections 6-7 use the same determinant ratio det(I-K)/det(I-iK). This overlaps the draft's claimed result and makes its description of the broader extremal conjecture as open outdated. The new preprint has not been independently refereed by this project. Its existence is sufficient to require an explicit priority/novelty analysis and a revised introduction before promoting the supplied draft. It is not published here as a new closure.

The exact question source for Paper_2 was checked directly: Yuval Wigderson, [*Duality for matrix space questions*, arXiv:2609.29177v1, Conjecture 8](https://arxiv.org/html/2609.29177v1). Searches for an earlier independent resolution of the exact M3(F3) nilpotent-free dimension problem did not identify one. This bounded search is not a priority guarantee. The user's own preceding preprint and archive are explicitly credited.

## Collection-by-collection screening

"Detailed audit outstanding" means the collection was screened but its full proof has not been verified in this pass. These entries are not certified conjecture closures.

| No. | Collection | Screening disposition |
| --- | --- | --- |
| 01 | 01 PolyaVinogradovLogLog | External uniform 7/8 zero-free premise remains unproved in the supplied paper; not selected as an unconditional closure. |
| 02 | 02 SYMSeveralTimes | Axiom-dependent SYM obstruction; specialist physics scope, not an all-model construction. |
| 03 | 03 KnotTables | Finite knot-table result; full conjecture not closed. |
| 04 | 04 BraneGasUV | UV/physical construction compatibility needs further audit. |
| 05 | 05 HodgeDenseLoci | Hodge F2 and F3-prime remain open. |
| 06 | 06 LehmerTotient | Prime-factor lower bound for Lehmer candidates; full Lehmer conjecture remains open. |
| 07 | 07 DworkGenerations | String construction/GSC vacuum remains unconstructed. |
| 08 | 08 ReflexiveDescent | Uniform seed bound established; exact value remains between 22 and 348. |
| 09 | 09 YangMillsForestGauge | Fixed-spacing/strong-coupling statement; continuum Yang-Mills not established. |
| 10 | 10 BLLM | Engine/model documentation, not a mathematical closure. |
| 11 | 11 MirrorClauseGSC | Mirror/standard-embedding obstruction; not a nine-condition GSC vacuum. |
| 12 | 12 BookRamsey58 | Exact finite book-Ramsey case; proof/novelty not fully re-audited here. |
| 13 | 13 GhostsBraneGases | Spectral Poisson-model result; specialist physics candidate. |
| 14 | 14 Sl2WeightSystemAtMinus3Over32 | General sl2 invariant formula; title/abstract screened, detailed proof audit outstanding. |
| 15 | 15 GolombWelchRadiusThree | Golomb-Welch finite lattice cases; full conjecture remains open. |
| 16 | 16 Kourovka2071b | Finite graph counterexample; detailed proof audit outstanding. |
| 17 | 17 OddAntiholeConjecture | Odd-antihole subclass theorem; detailed proof/novelty audit outstanding. |
| 18 | 18 GurvichNaumovaConjecture | All-parameter partition recursion; detailed proof/novelty audit outstanding. |
| 19 | 19 WelchSumFree | Finite-field Welch sum-free construction; detailed proof/novelty audit outstanding. |
| 20 | 20 ShankarLatticePathsCatalan | Catalan equality classification; delicate induction not fully audited here. |
| 21 | 21 SimpsonCircularAbelianSquares | Binary circular Abelian-square bound/classification; detailed proof/novelty audit outstanding. |
| 22 | 22 TauMaximalGraphs | Matroid-exchange statement; comparison with known matroid results needed. |
| 23 | 23 AndreanovKallusD5 | Potential overlap with known Andreanov-Kallus result requires resolution. |
| 24 | 24 Erdos1183UnionClosedFamilies | Erdos 1183 claims held for a separate proof audit. |
| 25 | 25 ErdosStrausExceptionalSet | Erdos-Straus exceptional-set bound; full conjecture remains open. |
| 26 | 26 ErdosStrausSieveConstant | Sieve-constant refinement, not full Erdos-Straus closure. |
| 27 | 27 ErdosSzekeresHighDim | Finite integer-point configurations; detailed proof/novelty audit outstanding. |
| 28 | 28 GraffitiDominationCounterexamples | Counterexample families for Graffiti conjectures; detailed proof/novelty audit outstanding. |
| 29 | 29 GrundyStrongProduct | Already selected and released as Paper_1; not duplicated. |
| 30 | 30 H1MaximalSublatticesSD | Finite semidistributive-lattice counterexample; detailed proof/novelty audit outstanding. |
| 31 | 31 KimberlingConjecture | Kimberling/OEIS exact limit; detailed proof/novelty audit outstanding. |
| 32 | 32 LiuFanoIndexConjecture | Specific Fano-index counterexample with classification input; not an all-dimensional classification. |
| 33 | 33 MaximalSublatticesConvexGeometries | Finite convex-geometry counterexamples; detailed proof/novelty audit outstanding. |
| 34 | 34 MorleyPSecting | Tetrahedron counterexample family; detailed proof/novelty audit outstanding. |
| 35 | 35 Musin24CellTwoTranslates | Restricted D4 packing case; full conjecture not established. |
| 36 | 36 SpectralAlgebrasCayley | Spectral Cayley-graph statement; detailed proof/novelty audit outstanding. |
| 37 | 37 StarFormingBipartite | Star-forming families/complexity results; detailed proof/novelty audit outstanding. |
| 38 | 38 UnionClosedLimit | Entropy-method limit and finite SAT checks; full union-closed conjecture remains open. |
| 39 | 39 WOWII66ForestNumber | Forest-number counterexample family; detailed proof/novelty audit outstanding. |
| 40 | 40 WigdersonConj8F3 | SELECTED Paper_2: exact maximum five in M3(F3); detailed earlier audit and current independent reruns, with computational trust disclosed. |
| 41 | 41 WormaldTournaments | NOT selected: new primary arXiv 2610.23755v1 overlaps determinant ratio and cyclic limit; outdated open-status claims need revision. |
