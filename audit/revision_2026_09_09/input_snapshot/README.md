# Contact Orders and the Fragility of Honest Tensor Inference

Audited revision completed 8 September 2026, directly in `tt_rank_inference_theory_2026`. The original project snapshot is preserved in `audit/baseline_2026-09-07/`; earlier sibling projects are unchanged.

**Mathematical verdict: B — rigorous but can be strengthened. Research decision: Promising — further work needed for a strong top-journal case.** All stated results have complete internally checked derivations. This is not independent peer review, formal verification, a novelty certificate, or a submission-ready judgment.

## Start here

- [Research program addressing verdict B](notes/strengthening_program_2026-09-08.md), with separate development proofs for [all-rank-two weak-bond inference](theory/active_rank_two_modulus.md), [growing-dimension compression](theory/growing_dimension_compression.md), and [calibration benchmarks](theory/gaussian_product_benchmark.md). These post-audit notes are not yet incorporated into the manuscript or its numbered inventory; novelty remains provisional. See the [additional prior-art comparisons](literature/strengthening_novelty_addendum.md).
- [Revised manuscript PDF](paper/main.pdf).
- [Audit findings and final verdict](audit/final_verdict.md).
- [All numbered results and statuses](audit/theorem_inventory.md), [assumption audit](audit/assumption_audit.md), and [complete proof checks](audit/proof_audit.md).
- [Dependency graph](audit/dependency_graph.md), [strengthening matrix](audit/theorem_strengthening_matrix.md), [counterexample appendix source](paper/appendix_counterexamples.tex), and [open questions](audit/open_and_resolved.md).
- [Publication assessment](notes/publication_assessment.md), [28-paper novelty matrix](literature/novelty_matrix.md), and [all 18 supplied-paper reviews](literature/local_corpus_review.md).
- [Paired energy/transition findings](simulations/results/audit/analysis.md), [finite-variance findings](simulations/results/robust_audit/analysis.md), and [validation report](audit/validation_report.md).

## Main verified strengthening

At B0=lambda times an original-mode rank-one product, split the TT chain at caps equal to one. Let a_l be the Frobenius norm of the loading's degree-l block component. The local modulus and optimal pointwise expected length under global honesty are determined by

    R_A(t) = (a_0+a_1)t + sum_{l=2}^J a_l t^l/lambda^(l-1),
    L_eta,alpha(B0) ≍ R_A(sigma/sqrt(n)) + ||A|| min(eta,sigma/sqrt(n)).

Unlike the original fixed-loading statement, the constants are uniform in deterministic loadings and signal directions. The fixed-loading q-order formula remains a corollary. The energy certificate is no longer than the original on any dataset. Its common coverage event protects all contrasts, including a selected contrast's random target; the expected-length statement and conditional selective inference require separate care.

Further proved extensions weaken the Gaussian sample threshold, remove the norm cap, permit quantitative general-design conditions, and retain the full contact rate with a median-of-group-OLS localizer under independent observations and a known conditional variance bound. The broader dependent-error covariance-bound branch has only a slower proved upper bound. Twelve counterexamples explain the limits, including a nonshrinking-length obstruction for honesty over every unspecified finite variance bound.

## Reproduce

Use the versions in `requirements.lock.txt`, plus pdflatex/bibtex. Run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/check_theory.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/check_audit_theory.py
OPENBLAS_NUM_THREADS=1 python simulations/code/validate_results.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/run_audit.py
OPENBLAS_NUM_THREADS=1 python simulations/code/analyze_audit.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/run_robust_audit.py
OPENBLAS_NUM_THREADS=1 python simulations/code/analyze_robust_audit.py
python audit/build_companion.py
python simulations/code/build_paper.py
python audit/validate_project.py
```

The two `run_*audit.py` commands regenerate the separately seeded audit experiments; their analyzers also verify hashes and interval endpoints. To regenerate the original 186,000 datasets use `run_study.py`, `run_asymptotic.py`, and `analyze.py`, following `simulations/simulation_design.md`. Original simulation code and execution hashes were preserved.

There are 198,000 unique datasets overall: 186,000 original, 6,000 paired loading/energy, and 6,000 finite-variance. The studies contain 1,632,000 interval records. Within-cohort loading/method comparisons share datasets and are explicitly paired. The original `research_companion.xlsx` preserves the primary results; `audit/audit_companion.xlsx` and the separate CSV files document the audit additions. No LLM or real-data experiment is claimed.

## Organization and limitations

`paper/` contains the manuscript, proofs, bibliography and vector figures; `theory/` contains current statements and proof maps; `audit/` contains the reconstruction, inventories, comparisons, verdict and preserved baseline; `literature/` contains source evidence; `simulations/` contains code and raw results; `notes/` contains research judgments; `build/` contains compilation/QA artifacts.

The audited manuscript still fixes dimensions and evaluates original-mode rank-one coefficients. Separate development notes now establish focused higher-rank and growing-dimension special cases. General higher-rank geometry, optimal dimension thresholds and sharp confidence constants remain unresolved. The audited manuscript's internal singular example does not establish that internal singularity causes the cubic exponent. The finite-variance procedure uses established median amplification and has conservative constants; it is not an adversarial-contamination or unrestricted unknown-variance procedure.
