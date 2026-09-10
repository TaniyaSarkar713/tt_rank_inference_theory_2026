# Contact Orders and Honest Tensor Inference

**Current revision: 9 September 2026. Research decision: Promising — further theoretical work is needed for a strong top-journal submission.** The rank-two result survived a detailed internal audit. Its new generalization, calibrated interval, growing-dimension results and full proofs are now assembled in a separate dated manuscript. Internal checking is not independent peer review or a novelty certificate.

## Start here: the new revision

- [Integrated manuscript PDF](paper/revision_2026_09_09/main.pdf), [LaTeX source](paper/revision_2026_09_09/main.tex), and [editable front matter](paper/revision_2026_09_09/frontmatter.md).
- [Step-by-step proof audit and result inventory](audit/revision_2026_09_09/proof_audit.md), [assumption audit](audit/revision_2026_09_09/assumption_audit.md), and [strict publication assessment](audit/revision_2026_09_09/publication_review.md).
- [General sharp TT modulus](theory/general_normal_modulus.md), [selected-cross calibration and growing dimensions](theory/certified_cross_inference.md), [learned-subspace theorem](theory/growing_dimension_general_tt.md), and [minimum-distance certification limits](theory/certified_minimum_distance_calibration.md).
- [Updated novelty comparisons](literature/revision_2026_09_09_novelty.md), [new simulation findings](simulations/results/tt_revision_2026_09_09/analysis.md), and [prespecified design](simulations/tt_revision_design.md).

For a unit product loading annihilating the reference in every physical mode, the new general theorem gives

\[
\omega_A(t;B_*)\sim\frac{t^K}{K^{K/2}\prod_{j=1}^{K-1}\beta_j},
\qquad t/\min_j\beta_j\to0.
\]

The geometric limit is uniform over dimensions and ranks for fixed order K. An explicit rank-two interval uses only 6K−3 selected features and attains the full weak-bond scale even when the ambient dimension exceeds n. Its short-length theorem concerns prespecified directions; a separate learned-subspace theorem requires n1 b²/σ² to exceed a dimension-dependent complexity. Optimal confidence constants and unknown weak-orientation adaptation remain open. Existing MPS geometry, Gaussian sketching and conservative test inversion are credited as prior art.

The new experiment has 95,000 independent datasets, 5,000 per setting, and 380,000 paired interval records. It samples the exact selected-regression sufficient-statistic law in an ambient 40^4 embedding. The 198,000 historical datasets are a separate cohort; their files were preserved.

## Reproduce the new revision

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/tt_revision/check_geometry.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/tt_revision/run.py
MPLCONFIGDIR=/tmp/tt_revision_mpl python simulations/code/tt_revision/analyze.py
python paper/revision_2026_09_09/build_revision.py
python audit/revision_2026_09_09/validate_revision.py
```

Python dependencies are recorded in [the revision requirements](simulations/code/tt_revision/requirements.txt), including mpmath for high-precision checks. The new build uses Pandoc, LuaLaTeX and DejaVu fonts. Proof notes are assembled into the manuscript by `build_revision.py`; edit those notes or `frontmatter.md`, then rebuild. The root manifest covers the deliverable sources and artifacts; compilation changes PDF hashes and requires an intentional manifest refresh.

## Preserved earlier work

The 8 September [manuscript](paper/main.pdf), [17-result audit](audit/theorem_inventory.md), [verdict](audit/final_verdict.md), [28-paper matrix](literature/novelty_matrix.md), and [18 supplied-paper reviews](literature/local_corpus_review.md) remain available. The original baseline is in `audit/baseline_2026-09-07/`. The inputs to the present extension are preserved in `audit/revision_2026_09_09/input_snapshot/` with their original hashes. The earlier strengthening program is [dated 8 September](notes/strengthening_program_2026-09-08.md).

## Historical manuscript: main verified strengthening

At B0=lambda times an original-mode rank-one product, split the TT chain at caps equal to one. Let a_l be the Frobenius norm of the loading's degree-l block component. The local modulus and optimal pointwise expected length under global honesty are determined by

    R_A(t) = (a_0+a_1)t + sum_{l=2}^J a_l t^l/lambda^(l-1),
    L_eta,alpha(B0) ≍ R_A(sigma/sqrt(n)) + ||A|| min(eta,sigma/sqrt(n)).

Unlike the original fixed-loading statement, the constants are uniform in deterministic loadings and signal directions. The fixed-loading q-order formula remains a corollary. The energy certificate is no longer than the original on any dataset. Its common coverage event protects all contrasts, including a selected contrast's random target; the expected-length statement and conditional selective inference require separate care.

Further proved extensions weaken the Gaussian sample threshold, remove the norm cap, permit quantitative general-design conditions, and retain the full contact rate with a median-of-group-OLS localizer under independent observations and a known conditional variance bound. The broader dependent-error covariance-bound branch has only a slower proved upper bound. Twelve counterexamples explain the limits, including a nonshrinking-length obstruction for honesty over every unspecified finite variance bound.

## Reproduce the historical manuscript

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

The historical studies contain 198,000 unique datasets: 186,000 original, 6,000 paired loading/energy, and 6,000 finite-variance. The studies contain 1,632,000 interval records. Within-cohort loading/method comparisons share datasets and are explicitly paired. The original `research_companion.xlsx` preserves the primary results; `audit/audit_companion.xlsx` and the separate CSV files document the audit additions. No LLM or real-data experiment is claimed.

## Historical scope and project organization

`paper/` contains the manuscript, proofs, bibliography and vector figures; `theory/` contains current statements and proof maps; `audit/` contains the reconstruction, inventories, comparisons, verdict and preserved baseline; `literature/` contains source evidence; `simulations/` contains code and raw results; `notes/` contains research judgments; `build/` contains compilation/QA artifacts.

The audited manuscript still fixes dimensions and evaluates original-mode rank-one coefficients. Separate development notes now establish focused higher-rank and growing-dimension special cases. General higher-rank geometry, optimal dimension thresholds and sharp confidence constants remain unresolved. The audited manuscript's internal singular example does not establish that internal singularity causes the cubic exponent. The finite-variance procedure uses established median amplification and has conservative constants; it is not an adversarial-contamination or unrestricted unknown-variance procedure.
