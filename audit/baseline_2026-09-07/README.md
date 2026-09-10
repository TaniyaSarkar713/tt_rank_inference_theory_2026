# Contact Orders and the Fragility of Honest Tensor Inference

A new, self-contained research project for the tt_rank_inference idea, developed7 September 2026. The earlier `jasa_tt_rank_inference` folder is preserved. This project is a skeptical reformulation, not a claim that the old framing was already novel.

**Decision: Promising — theory requires further work.** A complete 22-page draft with proofs is provided; it is not represented as submission ready or independently verified. The leading candidate contribution is a cap-profile classification of honest inference rates at rank-one TT coefficients, including internally singular classes. Generic higher-order inference and modulus methods are explicitly credited to prior work.

## Start here

- [Manuscript PDF](paper/main.pdf), with complete proofs in the appendix.
- [Publication assessment and final scientific checkpoint](notes/publication_assessment.md).
- [Literature review](literature/literature_review.md) and [25-paper novelty matrix](literature/novelty_matrix.md).
- [Theorem status ledger](theory/theorem_statements.md) and [assumption audit](theory/assumptions.md).
- [Simulation findings](simulations/results/analysis.md), [design and disclosed addendum](simulations/simulation_design.md), and [companion workbook](research_companion.xlsx).
- [All18 supplied-paper reviews](literature/local_corpus_review.md).

## Main established calculation

For B0=lambda times an original-mode rank-one product, split the chain at TT caps equal to one. Let q=max(1,minimum nonzero block degree of the fixed loading A). In fixed geometry, optimal pointwise expected length under global honesty over a known eta structural tube is comparable to

    (sigma/sqrt(n))^q / lambda^(q-1) + min(eta,sigma/sqrt(n)).

The project includes explicit witness paths, the elementary leading modulus constant q^(-q/2), a two-point lower bound, a computable graded interval, and finite-sample conditional coverage with known or unknown noise variance. Constants depend on dimension/loading. The theorem does not cover p>=n or general non-rank-one evaluation points. PROVED means a full internal derivation, not peer-review or novelty certification; PARTIAL and CONJECTURED results are kept out of theorem claims.

## Reproduce

Python 3.13, NumPy 2.3.5, SciPy 1.16.3, Pandas, Matplotlib, OpenPyXL, and a LaTeX installation with pdflatex/bibtex were used. Exact package versions are recorded in requirements.lock.txt. Run from this project directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/check_theory.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/run_study.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python simulations/code/run_asymptotic.py
OPENBLAS_NUM_THREADS=1 python simulations/code/analyze.py
OPENBLAS_NUM_THREADS=1 python simulations/code/validate_results.py
python simulations/code/build_paper.py
```

The main study uses162,000 datasets; the separately stored large-n addendum uses 24,000. Each of 93 settings has2,000 replications. There are 1,410,000 compressed replicate interval records and 705 summary rows. The Bartlett sampler exactly reproduces Gaussian-regression sufficient statistics; it does not approximate large n by a sequence model. Non-Gaussian stress settings generate raw observations. All raw interval records, seeds, settings, source hashes, summaries and figure data are included. Smoke outputs are development checks and are not pooled with the study.

The workbook includes all plotted summaries, slope calculations, setting definitions, raw-file locations and source comparisons. Compressed replicate tables remain the canonical row-level data. Generated LaTeX files and caches stay under build/.

## Organization

`paper/`: LaTeX, bibliography, figures, compiled manuscript. `theory/`: assumptions, statements, proof map and open questions. `literature/`: critical survey, novelty matrix, source records and local-corpus review. `simulations/`: locked design, modular code, complete outputs. `real_data/`: application protocol and explicit no-experiment status. `notes/`: decisions, logic, provenance and review. `build/`: compilation/QA artifacts.

## Scientific limitations

The present exponent classification may be viewed as an application of established product geometry. The six-mode example is genuinely singular internally, but that singularity does not generate the cubic exponent. The intervals have large conservative constants. Neither a general weak-bond theory nor a growing-dimensional minimax result has been proved. No real-data or LLM demonstration is claimed. Read the final checkpoint before choosing a journal or investing in a large application study.
