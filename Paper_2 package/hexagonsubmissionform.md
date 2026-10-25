# Hexagon submission fields

Submit a replacement version of 2610.00480v1; do not create a duplicate work.
The new version identifier is assigned by Hexagon after submission and is not
asserted in advance. Existing record: https://hexagonmath.org/2610.00480v1

## Title

Nilpotent-free spaces of 3 by 3 matrices over the field with three elements

## Abstract - copy the complete block

We prove that the largest dimension of a linear subspace of the $3\times3$ matrices over the field with three elements whose only nilpotent element is zero is five. Thus the proposed existence, over every finite field, of a nilpotent-free space of dimension $n^2-\binom n2$ fails at $n=3$. An explicit five-dimensional example has a direct algebraic proof. For the upper bound, a complement to the strictly upper triangular matrices is the graph of a $3\times6$ coefficient matrix. A search tree covers all $3^{18}$ such matrices using $3{,}109{,}888$ nodes. We give the coverage proof and a complete independent C verifier. The accompanying Lean development formalizes the reduction and search soundness, with two compiled evaluations explicitly included in its trust base. We also describe the nilpotent cone in characteristic three as a quadric in a seven-dimensional quotient and give examples over the fields with two and five elements.

The block uses explicit TeX commands rather than macros defined only in main.tex.

## Subjects, tags and MSC2020

Primary subject: math.RA
Cross-list subjects: math.NT
Tags: nilpotent matrices, matrix spaces, finite fields, computer-assisted proof, nilpotent-free subspaces
MSC2020 primary code: 15A30
MSC2020 additional codes: 15B33, 11T99
arXiv identifier: leave blank. No arXiv identifier is asserted.

## Contributors - preserve this order

Contributor 1: Deep Bhattacharjee
Affiliation: Formerly, Electro-Gravitational Space Propulsion Laboratory (EGSPL), Bhubaneswar, Odisha 751030, India
ORCID: 0000-0003-0466-750X

The affiliations are former affiliations, not assertions of current employment.

## Authorship and understanding selections

Text: A mix of human-written and AI-generated.
Human understanding: All parts of this contribution have been checked and understood by a human.
The user explicitly supplied both declarations for all six papers on 25 October 2026.

## Provenance statement - copy this paragraph

Claude through Claude Code assisted original searches, computations, Lean development and drafting. OpenAI Codex assisted the direct algebraic five-dimensional construction proof, the quadratic-form argument in characteristic three, an independent characteristic-coefficient verifier, proof auditing, scope corrections, references and typesetting. The submitting author declares that all parts have been
checked and understood by a human and takes responsibility for the content.
The Lean development formalises the reduction and search soundness. Two compiled evaluations remain explicit parts of its trust base. This must not be described as an audit using only the three standard axioms.

## Tools used

- Anthropic Claude / Claude Code
- OpenAI Codex
- Lean 4 / Mathlib
- Python
- C and C++
- LaTeX / pdfLaTeX

Use the corresponding system/tool entry if available and Other for an unlisted
tool. Do not invent a model version for an entry that is not documented.

## Formalisation links

https://github.com/creelie/Paper_2/tree/v1.1.0/formal

Scope: The Lean development formalises the reduction and search soundness. Two compiled evaluations remain explicit parts of its trust base. This must not be described as an audit using only the three standard axioms.
If the portal rejects a host/path, leave it for manual review rather than
uploading Lean material in the article source ZIP.

## Files and licence

Required source ZIP: Nilpotent-free_spaces_of_3_by_3_matrices_over_the_field_with_three_elementstex.zip
Reference PDF: Nilpotent-free_spaces_of_3_by_3_matrices_over_the_field_with_three_elements.pdf
AI provenance upload: AI_PROVENANCE.md (outside the source ZIP).
Licence selection: CC BY 4.0, matching the existing Hexagon manuscript record.
The manuscript source ZIP contains the article, bibliography and required
figures only. It excludes Lean developments, executables, journal correspondence,
other manuscripts and private model traces. Standard TeX Live classes/packages
are build dependencies rather than relicensed files in this ZIP.

## Review before submitting

Use pdfLaTeX, main document main.tex. The extracted ZIP was rebuilt locally and
its full extracted text and page count matched the supplied PDF. Confirm the
rendered title, abstract, byline, references and final portal preview. This
packet does not press the portal's Process or Submit button on the author's behalf.


Confirmed package archive: https://doi.org/10.5281/zenodo.23629623 .
Release: https://github.com/creelie/Paper_2/releases/tag/v1.2.0 .
The DOI receipt was added after the archived release; see ARCHIVE-DOI.md.
