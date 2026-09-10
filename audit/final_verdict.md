# Final mathematical audit and decision

Completed 8 September 2026. Scope: the existing `tt_rank_inference_theory_2026` manuscript, all its numbered results and essential technical claims, and the strengthened results developed during this audit. The untouched input is preserved under `baseline_2026-09-07/` with hashes.

**Verdict B — RIGOROUS BUT CAN BE STRENGTHENED.** The checked manuscript has complete internal proofs of its stated claims. No counterexample to a baseline numbered theorem was found under its actual assumptions. The audit established stronger statements rather than preserving avoidable assumptions. This is an internal mathematical judgment, not formal verification, independent peer review, or certification that the contribution is new enough for a particular journal.

## What changed mathematically

The strongest result is now the loading-uniform modulus and honest-length theorem. With a_l=||Π_l A||,

    R_A(t) = (a_0+a_1)t + sum_{l=2}^J a_l t^l/lambda^(l-1),
    omega_A(t;B0) ≍ R_A(t),
    L_eta,alpha(B0) ≍ R_A(sigma/sqrt(n)) + ||A|| min(eta,sigma/sqrt(n)).

The constants are independent of deterministic A and the unit signal directions with dimensions/caps fixed. Signed TT-feasible paths isolate every loading degree. For A_epsilon=(E1111+epsilon E1000)/sqrt(1+epsilon²), the rate is (epsilon*t_n+t_n³/lambda²)/sqrt(1+epsilon²), exposing the transition at epsilon≈t_n²/lambda². The previous integer q alone could not express this transition uniformly.

Other proved improvements are:

- Smaller Gaussian sufficient sample condition: n≥p+max(J,2), replacing n≥2p+2J+8.
- Energy coefficients sqrt(C(J,l))/J^(l/2), producing intervals no longer than the original on every dataset, with the same coverage guarantee.
- Simultaneous contrast coverage on one event, including measurable selected contrasts and their random targets; no conditional-on-selection or arbitrary random-loading length claim.
- A general confidence-ball/moment transfer theorem; quantitative non-Gaussian and dependent-design extensions with Gaussian conditional errors.
- Finite-variance coverage under a known conditional covariance bound, with an explicit slower upper bound under the broader dependent-error model.
- Full higher-order rate under iid observation pairs and a known conditional variance bound, using coordinate medians of independent OLS groups. The optimal expected-length scale matches after taking the worst admissible noise law at B0.
- Removal of the global norm cap.

Twelve counterexamples document why other relaxations fail. In particular C12 constructs regression alternatives arbitrarily close in total variation while changing the coefficient, with finite but unbounded-over-the-class conditional variance. It proves that uniform honesty over all such unknown bounds prevents shrinking intervals. This is a directly proved specialization of a classical nonparametric impossibility mechanism, not a new general impossibility principle.

## Strongest, weakest, and next theorem

**Strongest:** R1+R3, supported by R17: the explicit loading-uniform TT modulus, matching honest-length scale and its independent finite-variance extension. The constrained feasible-path computation is the candidate new ingredient. Generic higher-order inference, robust mean estimation and modulus lower bounds already exist.

**Weakest supporting proposition:** R5, the injective-norm identity and inherited hardness observation. Its calculation is correct, but it does not establish a computational-statistical inference gap. It remains clearly labeled supporting material and is excluded from the core contribution list. The Wald proposition is also supporting prior-art specialization.

**Most valuable strengthening:** sharp dimension-dependent honest length or a non-rank-one TT phenomenon with active internal constraints. A further generic localization lemma or a cosmetic LLM application would add less scientific value. The current results remain at original-mode rank-one evaluation points, and the internal singularity does not itself generate the higher contact order.

## Empirical checks

The original 186,000 datasets and 1,410,000 interval records were preserved. A separately labeled paired loading/energy study adds 6,000 datasets and 210,000 records; a finite-variance study adds 6,000 datasets and 12,000 records. Total unique datasets are 198,000, with 1,632,000 interval records across the original and audit studies. Loadings, methods and cap-profile comparisons reuse datasets where specified; these are not counted as independent replications.

At the tested cubic point n=8192, the energy/original mean-length ratio is 0.23626 (paired MCSE 0.00041). Both methods cover 2,000/2,000, whose Wilson interval is [0.9981,1]; this is not proof of perfect population coverage. The new interval is still about 389 times the bare rate scale there. Under finite-variance t2.5 errors, the median-localized procedure has finite-grid slopes −1.598 and −2.133 for q=3 and q=4. They remain steeper than the limiting −1.5 and −2, so the study is not described as exact asymptotic confirmation. Its 1,000/1,000 coverages also indicate conservatism.

## Novelty and publication checkpoint

No matching complete capped-TT loading-uniform modulus and honest-length statement was found in the reviewed sources. This is bounded negative evidence, not a priority certificate. The refreshed matrix contains 28 comparisons; the original review of all 18 supplied PDFs remains available. The robust-mean additions explicitly acknowledge stronger existing localization theory. Bahadur–Savage bibliographic details were verified, but its original full text was unavailable in this pass; no theorem is imported from it.

**Research recommendation: Promising — theory requires further work for a strong top-journal case.** This is compatible with verdict B: the missing work concerns breadth, sharpness, practical calibration and defensible novelty, rather than an unresolved step in a stated central proof. Annals of Statistics submission is not recommended in the present form. Biometrika/Bernoulli or other focused theory outlets may be plausible after external expert assessment and sharper positioning. The venue-by-venue assessment is in `notes/publication_assessment.md`.

## Deliverable map

- Reconstructed model and identifiability: `reconstructed_framework.md`.
- All 17 numbered results, status and sharpness: `theorem_inventory.md/.csv`.
- Essential inline statements: `essential_claim_inventory.md/.csv`.
- Complete stepwise proofs: the three manuscript appendix sources; independent checks in `proof_audit.md`.
- Proof graph and external assumptions: `dependency_graph.md`, `external_results_and_prior_art.md`.
- Assumption audit and relaxation: `assumption_audit.md/.csv`, `assumption_relaxation_matrix.md/.csv`.
- Strengthening and comparisons: `theorem_strengthening_matrix.md/.csv`, `theoretical_comparison.md`.
- Counterexamples: `paper/appendix_counterexamples.tex` and the compiled manuscript.
- Per-result referee attack, efficiency/bootstrap/computation/contamination limits: `referee_attack.md`.
- Resolved, partial and open work: `open_and_resolved.md`.
- New simulation metadata, raw outputs, MC uncertainty and figures: `simulations/results/audit/` and `simulations/results/robust_audit/`.
- Reproducibility and rendered-manuscript checks: `validation_report.md` and `validation.json`.
