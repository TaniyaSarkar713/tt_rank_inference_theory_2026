# Contact Orders and Honest Tensor Inference

**Current theory: 11 September 2026; integrated manuscript: 9 September 2026. Research decision: Promising; further theoretical work and independent review are needed for a strong top-journal submission.** A new proof addendum resolves unequal-bond rate geometry for fully normal product loadings, removes the balanced-gap assumption from the learned-compression bound, and gives a computable interval for an explicit single-cut rank loss. Internal checking is not independent peer review or a novelty certificate.

## Project status — updated 11 September 2026

The [12-page September 11 proof addendum](paper/revision_2026_09_11/addendum.pdf) extends the preserved September 9 manuscript. The new modulus holds at every localization radius and retains each bond's singular value separately. Its rank-deficient extension has an explicit complementary-space admissibility premise. Statistical consequences include matching fixed-dimensional honest expected length over the unbounded rank-capped class and a 23-feature interval that attains a quartic-to-cubic transition in the displayed four-mode family.

The new deterministic-seed checks passed: 210 feasible perturbation witnesses (including strongly imbalanced examples), 300 cross identities, 450 constructed-ball target inclusions, and 900 outcome-wise length bounds, alongside spectrum, boundary-path, and implementation checks. These checks can falsify formulas; they are not a proof substitute or a coverage experiment. No new Monte Carlo cohort was generated. The addendum compiled without LaTeX diagnostics, and its theorem and interval pages were visually checked. The extension and historical artifact validators passed, verifying current proof/check hashes, 80 local links, all 394 manifest entries, and the preserved manuscript and simulation records.

Unknown weak orientations near the noise scale, arbitrary dense or partially normal loadings, exact critical-transition constants, optimal confidence calibration, and efficient general inversion remain open. The [current proof audit](audit/revision_2026_09_11/proof_audit.md) identifies precisely which previous requirements are resolved and which remain. The new theorems are internally derived, with novelty still provisional.

The project has its own [private GitHub repository](https://github.com/TaniyaSarkar713/tt_rank_inference_theory_2026), a [beginner mathematical summary of the earlier foundation](summary.md), and a [local reference collection and reading guide](references/README.md). The collection contains eight papers and one supplementary PDF, with source links, versions, and file hashes.

The closest statistical comparison in the inspected collection is Ke, Song, Zhao and Wang, *Efficient Inference for Low-rank Regression via Covariance-Weighted Projection*. Its first-order variance condition separates it from this project's fully normal targets. Wouters et al. is the main higher-order MPS geometry comparison. The [reading guide](references/README.md) explains the overlap and differences and points to the relevant results in each downloaded version.

The [September 11 literature comparison](literature/unequal_bond_comparison_2026_09_11.md) records a bounded follow-up search and distinguishes inspected results from abstract-only comparisons. A specialist theorem-level novelty review remains outstanding.

**Standing repository rule:** update this README's project status and file organization in every commit, and verify those updates before each push. The persistent instructions are in [AGENTS.md](AGENTS.md).

## Start here: the September 11 extension

- [Proof addendum PDF](paper/revision_2026_09_11/addendum.pdf), [assembled Markdown](paper/revision_2026_09_11/addendum.md), and [LaTeX source](paper/revision_2026_09_11/addendum.tex).
- [Unequal-bond modulus and partial rank loss, U1–U4](theory/unequal_bond_modulus.md), and [honest inference and the 23-feature interval, V1–V3](theory/unequal_bond_inference.md).
- [Proof audit and remaining requirements](audit/revision_2026_09_11/proof_audit.md), [numerical check results](audit/revision_2026_09_11/checks.json), and [scoped literature comparison](literature/unequal_bond_comparison_2026_09_11.md).
- [Interval implementation](simulations/code/unequal_bonds/methods.py) and [reproducible check script](simulations/code/unequal_bonds/check_theory.py).

For a unit product loading absent from the reference in every physical mode, the new general rate is

\[
\omega_A(t;B_*)\asymp_K t\prod_{j=1}^{K-1}\min\{1,t/\beta_j\},\qquad t>0.
\]

Here \(\beta_j\) is the smallest singular value at the capped rank of the jth prefix unfolding. Each bond stronger than the noise scale contributes another small factor; a weaker bond stops contributing that factor. For exact-rank references the constants depend only on tensor order. At rank-deficient references a zero gap contributes one, provided the exact capped ranks are attainable in the physical space perpendicular to the loading.

In the new four-mode example, the gaps are \((b,1,1)\). For small t the modulus changes from \(t^4/b\) to \(t^3\) as b falls below t. Substituting \(t=\sigma/\sqrt n\) gives the corresponding honest-length rates. The 23-feature interval attains both rates for prespecified coordinate directions: coverage requires n > 23 and the expected-length theorem requires n ≥ 27. This does not establish adaptation to unknown weak directions.

## September 9 integrated manuscript

- [Integrated manuscript PDF](paper/revision_2026_09_09/main.pdf), [LaTeX source](paper/revision_2026_09_09/main.tex), and [editable front matter](paper/revision_2026_09_09/frontmatter.md).
- [Step-by-step proof audit and result inventory](audit/revision_2026_09_09/proof_audit.md), [assumption audit](audit/revision_2026_09_09/assumption_audit.md), and [strict publication assessment](audit/revision_2026_09_09/publication_review.md).
- [General sharp TT modulus](theory/general_normal_modulus.md), [selected-cross calibration and growing dimensions](theory/certified_cross_inference.md), [learned-subspace theorem](theory/growing_dimension_general_tt.md), and [minimum-distance certification limits](theory/certified_minimum_distance_calibration.md).
- [Updated novelty comparisons](literature/revision_2026_09_09_novelty.md), [new simulation findings](simulations/results/tt_revision_2026_09_09/analysis.md), and [prespecified design](simulations/tt_revision_design.md).

For a unit product loading annihilating the reference in every physical mode, the September 9 sharp theorem gives

\[
\omega_A(t;B_*)\sim\frac{t^K}{K^{K/2}\prod_{j=1}^{K-1}\beta_j},
\qquad t/\min_j\beta_j\to0.
\]

The geometric limit is uniform over dimensions and ranks for fixed order K. An explicit rank-two interval uses only 6K−3 selected features and attains the full weak-bond scale even when the ambient dimension exceeds n. Its short-length theorem concerns prespecified directions; a separate learned-subspace theorem requires n1 b²/σ² to exceed a dimension-dependent complexity. Optimal confidence constants and unknown weak-orientation adaptation remain open. Existing MPS geometry, Gaussian sketching and conservative test inversion are credited as prior art.

The September 9 experiment has 95,000 independent datasets, 5,000 per setting, and 380,000 paired interval records. It samples the exact selected-regression sufficient-statistic law in an ambient 40^4 embedding. The 198,000 historical datasets are a separate cohort; both cohorts' files were preserved.

## File organization — reviewed 11 September 2026

The organization below was reviewed for this commit and includes all September 11 additions.

| File or directory | Contents and current role |
|---|---|
| [README.md](README.md) | Current project status, navigation, reproduction commands, and repository-update rule. |
| [summary.md](summary.md) | Preserved beginner explanation of the earlier foundation; the September 11 unequal-bond extension is described above and in its addendum. |
| [AGENTS.md](AGENTS.md) | Persistent instructions for README maintenance and artifact integrity. |
| [references/](references/) | Eight closest and supporting papers, the Ke et al. supplement, a reading guide, BibTeX entries, and download provenance with hashes. |
| [paper/revision_2026_09_11/](paper/revision_2026_09_11/) | New 12-page proof addendum, assembled Markdown/LaTeX, build script, and compilation output. |
| [paper/revision_2026_09_09/](paper/revision_2026_09_09/) | Preserved integrated manuscript, complete proof supplement, bibliography, and build sources; read with the September 11 addendum. |
| [paper/](paper/) | Preserved earlier manuscript, appendices, bibliography, and vector figures. |
| [theory/](theory/) | Theorem statements and proofs, including the new `unequal_bond_modulus.md` and `unequal_bond_inference.md`; earlier notes retain their dated scope. |
| [simulations/code/unequal_bonds/](simulations/code/unequal_bonds/) | New 23-feature interval implementation and deterministic-seed algebraic checks; no coverage simulation cohort. |
| [simulations/code/tt_revision/](simulations/code/tt_revision/) | September 9 selected-coordinate interval implementation, geometry checks, and simulation scripts. |
| [simulations/results/tt_revision_2026_09_09/](simulations/results/tt_revision_2026_09_09/) | Saved results for the 95,000-dataset revision cohort and its validation reports. |
| [simulations/](simulations/) | Prespecified designs, all current and historical code, raw results, and figures. |
| [audit/revision_2026_09_11/](audit/revision_2026_09_11/) | Current proof ledger, unresolved requirements, numerical checks with theory/code source hashes, and extension artifact validator. |
| [audit/](audit/) | Internal proof and assumption audits, publication assessments, validators, and frozen earlier snapshots. |
| [literature/](literature/) | Literature reviews and dated novelty comparisons, including the new unequal-bond comparison; downloaded PDFs are in `references/`. |
| [notes/](notes/) | Research planning and assessments of the paper's direction. |
| [real_data/README.md](real_data/README.md) | Application status and a proposed follow-up protocol; no completed real-data study. |
| [build/](build/) | Preserved compilation and document-quality artifacts. |
| [research_companion.xlsx](research_companion.xlsx) and [audit/audit_companion.xlsx](audit/audit_companion.xlsx) | Historical study summaries and audit additions. |
| [MANIFEST.sha256](MANIFEST.sha256) | Integrity hashes for the research deliverables and subsequent documentation/reference additions. |
| [requirements.lock.txt](requirements.lock.txt) and [revision requirements](simulations/code/tt_revision/requirements.txt) | Historical and current Python dependency records. |

## Reproduce the September 11 extension

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/unequal_bonds/check_theory.py
python paper/revision_2026_09_11/build_addendum.py
```

The check script uses NumPy and SciPy from the recorded environment and saves source hashes with its results. The addendum build uses Pandoc, LuaLaTeX, and DejaVu fonts. Edit the two new theory notes, rerun the checks, and rebuild to keep the proof text and reported checks synchronized. No original results are regenerated by these commands.

After reviewing changes, refresh the root manifest while preserving all existing entries, then run `python audit/revision_2026_09_11/validate_extension.py`. It checks proof/check freshness, navigation, and the build, and also runs the required `python audit/revision_2026_09_09/validate_revision.py`. Do not use that older validator's `--refresh-manifest` option to replace the expanded inventory: it can omit later additions. Recompiling a PDF changes its hash.

## Reproduce the September 9 revision

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

## Historical scope

The audited manuscript still fixes dimensions and evaluates original-mode rank-one coefficients. Separate development notes now establish focused higher-rank and growing-dimension special cases. General higher-rank geometry, optimal dimension thresholds and sharp confidence constants remain unresolved. The audited manuscript's internal singular example does not establish that internal singularity causes the cubic exponent. The finite-variance procedure uses established median amplification and has conservative constants; it is not an adversarial-contamination or unrestricted unknown-variance procedure.
