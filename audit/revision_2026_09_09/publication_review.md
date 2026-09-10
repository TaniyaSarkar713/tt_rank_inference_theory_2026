# Publication review and decision checkpoint

**Decision: Promising — theory requires further work for a strong top-journal submission.** The rank-two result survives the internal audit, and its new generalization materially strengthens the project. The appropriate claim is a focused theorem about sharp TT normal moduli and honest weak-bond inference. Generic rank uncertainty, TT geometry, sketching and conservative calibration are not defensible standalone novelty claims.

## What changed mathematically

- Diagonal rank-two geometry → arbitrary admissible TT ranks and non-diagonal references under explicit physical normality, with sharp denominator ∏βj.
- Fixed-dimensional ambient OLS → an explicit m=6K−3 selected-feature procedure, honest over the full rank-capped class, attaining the complete weak-component transition at prespecified reference directions with arbitrary ambient dimensions.
- Separate numerator errors → exact optimization of their joint quadratic budget, preserving coverage and shortening intervals on every dataset.
- Prespecified directions → a separate learned-subspace theorem with W-dependent training sample complexity and an explicit failure term. This does not cover unidentified weak directions at the n^{-1/2} boundary.

These are improvements over the project's earlier theorems. They are not claims of improving every guarantee in the external literature. The contribution relative to regular tensor inference is a different, degenerate regime and its geometry, rather than a smaller variance in the same regime.

## Referee-style severity assessment

**CRITICAL for broader claims, resolved by restricting the manuscript:** higher-order MPS geometry and conservative Monte Carlo inversion are established; exact F coverage is not exact nominal coverage at every parameter; the modulus constant is not the confidence-length constant; a selected-coordinate guarantee is not automatic orientation adaptation. These broader claims have been excluded.

**MAJOR, unresolved:** physical normality is restrictive; the method is very conservative; the best growing-dimension boundary result uses prespecified coordinates; the learned pilot and confidence inversion are existence constructions; unknown weak orientations and unequal rank losses are not characterized. Novelty has no independent specialist endorsement. Simulations at zero targets cannot establish worst-case coverage sharpness. Their fixed-b slopes still show finite-sample bias.

**MINOR/editorial:** consolidate the expanded proof supplement into the target journal's format after scope is fixed; replace development identifiers G/C/D with final theorem numbering; improve notation by keeping dimension dj distinct from contraction-energy symbols; add an explicit computational-complexity section if a learned-subspace algorithm is developed. Existing historical artifacts retain their dates and scope.

## Venue assessment

| Venue | Current assessment | What is missing |
|---|---|---|
| Annals of Statistics | Not ready. G1 is a credible core result, but the statistical theory is still specialized. | A substantial general theorem on partial normality, unequal weak bonds, or unknown-orientation adaptation with matching lower/upper bounds; specialist novelty review of the MPS connection. An LLM example would not fill this gap. |
| JASA Theory and Methods | Possible direction; current constants and scope are a concern. | A broadly useful computable interval, stronger calibration/length comparisons, and a convincing statistical use case beyond a prespecified coordinate example. |
| JRSS-B | Possible after strengthening methodology. | Feasible inference with learned structure, interpretable tuning and competitive coverage/length across meaningful alternatives. |
| Biometrika | Potentially a focused paper around G1, the matrix comparison and a sharp statistical consequence. | A tighter central inference theorem or informative near-optimal calibration; a shorter, cohesive presentation and verified distinctness from MPS expansions. |
| Bernoulli | Plausible theoretical target after refinement. | A broader probabilistic/statistical consequence and resolution of at least one substantive generality gap. |
| Statistica Sinica | Plausible focused target, subject to novelty review. | Direct positioning against the new covariance-weighted inference paper, complete computational exposition and stronger nonzero-target experiments. |
| COLT / ML theory venues | Current core is more statistical geometry than learning theory. | A learning/inference tradeoff with matching complexity bounds or a provably efficient procedure; a tensorized-model application alone is insufficient. |

These are research judgments, not acceptance predictions or claims about current editorial policies.

## Final checkpoint

**Novelty.** The most defensible candidate is the sharp normal-loading TT modulus and the boundary transition under compatible rank constraints. G1 extends the previous product-background example; C4 establishes attainability without ambient OLS. No exact matching prior theorem was found in the checked sources. This remains provisional.

**Mathematical contribution.** Complete internal derivations establish G1/G2, C1–C5, D1–D3 and M1/M2. Only G1/G2 and the focused statistical consequences are proposed as substantive contributions; several other results are standard tools or useful specializations.

**Improvement.** The previous project required n>p for the rank-two interval. The new theorem needs n≥6K−3+max(K,2), with constants independent of p at the aligned family. The original numerator ∏(cj+e) is replaced by the maximum over Σδj²≤e², and interval length never increases.

**Generality.** The model is Gaussian structured regression, independent of LLMs. A tensor adapter could motivate a linearization, but no theorem for actual LLM training or deployment is claimed.

**Simulation validation.** 95,000 new independent datasets verify the implemented length dominance, conservative coverage, and strong-bond length decay. They do not test learned subspaces, sharp minimum-distance calibration or worst-case size. Monte Carlo uncertainty is reported.

**Remaining weakness.** A skeptical reviewer can still ask whether special normal loadings make the phenomenon too narrow, whether the sharp constant was implicit in existing MPS constructions, and whether the conservative interval has practical inferential value. The current evidence does not justify an Annals-ready verdict.

## Next proof-driven step

Define a family of unknown supporting orientations with a fixed target loading. Construct many feasible weak-component alternatives that share a reference distribution closely enough for a mixture lower bound, while separating the target enough to constrain one globally honest interval. A packing that changes nuisance parameters without changing the target proves estimation difficulty but not a confidence-length lower bound. First determine whether this construction forces a dimension-dependent loss; if it fails, search for an orientation-free test that attains the selected-direction scale. Keep this branch separate from attempts to optimize the existing conservative confidence set.
