# Canonical complete proofs and audit map

Full, non-sketch proofs are in:

- [Original proof chain, independently revised](../paper/appendix.tex): factorization; loading-uniform signed witnesses; contact constant; slack and singular example; two-point/tube; OLS moments; HOSVD mixing; coverage/length; norm coefficient; local Wald limit.
- [Strengthening proofs](../paper/appendix_strengthening.tex): energy certificate, localization transfer, general design, finite-variance Markov ball, unbounded class, independent-group median OLS and matching worst-noise lower bound.
- [Twelve counterexamples](../paper/appendix_counterexamples.tex): zero signal, invalid caps, nonidentifiability, dependence, wrong pivots, nonuniform loading order, pointwise coverage, inverse moments, expectation failure, bootstrap failure, loading selection, and unknown unrestricted variance bounds.

Each main proof has a roadmap. [Independent proof audit](../audit/proof_audit.md) checks inequalities, quantifiers, constants and possible failure points; [dependency graph](../audit/dependency_graph.md) separates deterministic coverage from expected-length arguments to avoid circular reasoning. [External results audit](../audit/external_results_and_prior_art.md) identifies which external results are actually invoked and which are only prior art.

No unproved assertion is used to bridge these proofs. PROVED means checked internal mathematical derivation, not mechanized proof or independent peer review. Historical proofs and PDFs are preserved under `audit/baseline_2026-09-07/`.
