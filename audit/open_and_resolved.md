# Resolved questions and remaining mathematical work

## RESOLVED — complete proof

- All 11 numbered baseline statements are valid under their stated assumptions; several were not sharp in their scope or constants.
- The all-degree loading modulus and expected-length formula are uniform in deterministic A and signal directions. Signed feasible paths remove cancellation concerns.
- The Gaussian sufficient sample condition is n≥p+max(J,2).
- Energy coefficients improve by J^(−l/2); interval length is never larger on any dataset.
- The confidence event supports all contrasts simultaneously, including a selected contrast's random target; it does not condition on selection.
- Quantitative Gram assumptions permit deterministic and non-Gaussian/dependent designs with conditional Gaussian errors.
- A known covariance bound yields finite-variance coverage and an explicit degree-capped upper bound without error independence.
- Under iid observation pairs and a known conditional variance bound, median OLS groups restore the full degree rate; a Gaussian submodel matches the worst-noise expected-length lower bound.
- A global norm cap is unnecessary; the closed unbounded class has attained nearest-point distances.
- The difference between exact-boundary Wald calibration and locally honest inference is verified in its stated iterated regime.

## COUNTEREXAMPLE FOUND

C1 zero signal; C2 enlarging cap-one restrictions; C3 unidentified structured direction; C4 arbitrary dependence; C5 finite variance with Gaussian pivot; C6 loading-uniform rate based on q alone; C7 pointwise-only coverage; C8 full rank without inverse moments; C9 O_P without expectation control; C10 ordinary bootstrap; C11 scalar post-selection intervals; C12 unknown unrestricted conditional variance bounds. Full constructions and proofs are in the manuscript appendix.

## PARTIAL — established pieces but no complete stronger theorem

- Growing dimension: exact full-rank Gaussian coverage and fixed-dimensional geometry are available; dimension factors in upper/lower length do not match.
- Computational calibration: exact local coefficient contains a hard tensor norm; no statistical-computational interval lower bound or sharp efficiently attainable constant is proved.
- General higher-rank geometry: slack-at-every-cut cases are solved; arbitrary partially active TT strata are not classified.

## OPEN PROBLEM / LIKELY PROVABLE — not manuscript theorems

| Priority | Proposed stronger result | Proof strategy | Missing step | Impact × feasibility / publication value |
|---|---|---|---|---|
| 1 | Dimension-dependent honest functional length near TT boundaries | Replace the ambient ball by intrinsic localization; derive matching local alternatives reflecting dimensions | Honest localization across rank strata and matched loading-dependent lower bound | High impact, difficult; most useful for AoS/COLT-level case |
| 2 | Non-original-mode-rank-one evaluation points with active internal constraints | Use existing tangent-cone formulas and construct higher-order feasible arcs | Uniform noncancellation/attainability and local norm control | High impact, difficult; best chance of a genuinely different tensor phenomenon |
| 3 | Sharp constants in the focused three-block experiment | Analyze calibrated minimum-distance inversion and least-favorable directions | Exact expected-length optimum or strong approximation certificate | Medium/high impact, moderate difficulty; useful for Biometrika/JRSS-B |
| 4 | Full contact rate under specified dependent errors | Construct a valid block/localization method under a concrete mixing or martingale model | Uniform high moments and an information lower bound in the same model | Medium impact, moderate/high difficulty; do not say arbitrary dependence |
| 5 | Unknown scale under specified non-Gaussian tail restrictions | Robust scale estimation plus jointly honest localization | Additional identifiable tail/scale class that avoids C12; uniform integration | Medium impact, moderate/high difficulty |
| 6 | Expected-length control for selected loadings | Start from pathwise sum a_l(Ahat)U^{d_l}; impose conditional independence or bounded selection class | Control mixed loading/localization moments at the claimed scale | Medium impact, moderate difficulty; simultaneous coverage alone is solved |
| 7 | Approximate HOSVD computation with certified residual | Replace sqrt(J) by a verified residual factor | Guarantee from the actual numerical solver | Lower scientific impact, likely feasible |

No publication-level claim is based on an unproved candidate rate. The finite-variance full-rate question was solved during this audit for the independent known-bound branch; it is no longer listed as an open iid problem.
