# Publication potential and final scientific decision

Assessment updated: 8 September 2026 after adversarial mathematical audit. These are judgments about the present evidence, not acceptance probabilities or journal policy statements.

## Final checkpoint

**Novelty.** The strongest candidate is now a loading-uniform cap-profile modulus and honest-length classification: at any original-mode rank-one signal, the locations of TT cuts constrained to rank one determine a block decomposition, and the all-degree loading polynomial gives a uniform honest-length scale; the first nonzero degree recovers the fixed-loading exponent. Feasible elementary paths attain this order even with proper singular internal rank constraints. No identical statement was found in the reviewed sources. This does not certify priority. Segre osculating geometry, higher-order delta inference, tensor tangent cones, generic confidence-ball inversion and modulus lower bounds already exist.

**Mathematical contribution.** Complete internal proofs establish the contact-order theorem, its elementary leading constant, a matching-order honest expected-length result, the known-tube sensitivity threshold, a computable attaining interval with unknown-noise extension, and the slack-at-every-cut negative result. A six-binary-mode example has q=3 inside a genuinely singular TT class. A supporting local-Wald calculation explains the approximately 48.65% limiting coverage of a boundary-calibrated 95% interval under iterated local drift. The latter is a specialization of known degeneracy theory, not a separate novelty claim.

**Improvement.** We do not improve existing high-dimensional tensor estimation or efficient regular-inference rates. The defensible comparison is:

    A single cap-one matrix envelope: quadratic functional modulus
       -> all TT caps in the six-mode example: cubic modulus.

    Ambient honest interval at a q>=2 point: order sigma/sqrt(n)
       -> exact structured class: order (sigma/sqrt(n))^q/lambda^(q-1).

    Exact structural class
       -> known eta neighborhood: add min(eta,sigma/sqrt(n)).

These are comparisons across explicitly different parameter restrictions, not superiority under identical information. No sharp minimax confidence constant is established.

**Generality.** The coefficient experiment is not specific to AI. It applies to structured Gaussian regression with fixed loading. Conditional finite-sample coverage permits any full-column-rank design with iid Gaussian homoskedastic errors. Expected-length rates now also hold under quantitative general-design conditions with conditional Gaussian errors. A median of independent OLS groups gives the full rate under iid pairs, Gaussian design and a known conditional variance bound, with unconditional design coverage; a separate broader covariance-bound result has a slower proved upper bound.

**Simulation validation.** The original 186,000 datasets are preserved. Two separately labeled audit studies add 12,000 datasets (6,000 paired loading/energy and 6,000 independent finite-variance), giving 198,000 unique datasets overall. Original settings have 2,000 replications each; finite-variance cohorts have 1,000. The large-n slopes approach -q/2 for q=1,2,3,4; the six-way singular example approaches -1.5. Rank-selected and known-rank plug-in Wald methods can under-cover near the boundary; boundary-degree Wald is accurate at the exact point but fails under drift. Known-tube intervals respond to structural departure. Conservatism, dimension effects and out-of-assumption noise diagnostics are reported. The large-n addendum and later supporting Wald derivation are explicitly disclosed.

**Remaining weakness.** A skeptical reviewer could say the structural theorem is an elegant but short consequence of known product geometry, with a generic statistical wrapper. The main short-length evaluation points remain original-mode rank one. The internal singularity does not itself change the exponent. The energy refinement reduces length substantially at one tested boundary, but ambient and median-localization constants remain large, and no comparison establishes superiority over fully optimized generic minimum-distance inversion. High-dimensional minimax constants and non-rank-one weak-bond geometry remain unresolved. There is no real-data result.

**Go / No-Go: Promising — theory requires further work.** Continue as a focused theory project. Do not submit the present draft to a top journal as if novelty or importance were settled. Independent expert review should scrutinize the classification against osculating-variety and nonregular-inference literature. For a stronger version, prioritize dimension-dependent sharp bounds or a non-rank-one phenomenon that changes the mathematical picture; do not add an LLM experiment as a substitute.

## Venue-specific assessment

| Venue | Current assessment | What is missing |
|---|---|---|
| Annals of Statistics | No-Go for submission in present form | A general and substantial statistical theorem beyond the fixed-dimensional rank-one/product structure calculation: e.g. sharp growing-dimensional honest length, a new class of singular local experiments, or genuinely new non-rank-one transition theory. Independent proof and priority review essential. |
| JASA, Theory and Methods | Promising, not ready | A practically competitive interval, strong comparison against calibrated minimum-distance inversion, and a compelling statistical use case with defensible structure. A cosmetic AI demonstration would not fix the theoretical scope. |
| JRSS-B | Promising, not ready | A broader methodological principle with materially better constants/computation and evidence that the approximation sensitivity changes substantive inference. |
| Biometrika | Plausible focused direction after strengthening | A tightly scoped theorem or counterexample with sharper calibration and concise presentation; the present conservative method and familiar generic ingredients invite an incremental verdict. |
| Bernoulli | Plausible theory target after further work | Clear separation from existing geometric corollaries, possibly general contact/modulus or random-design theory with sharper constants. |
| Statistica Sinica | Plausible with revision and independent validation | A clear inferential methodological contribution, stronger practical calibration and a convincing example; current limited scope must remain explicit. |
| COLT | Weak fit at current scope | A substantial learning-theoretic or statistical-computational result. The inherited norm-hardness observation is insufficient. |
| NeurIPS / ICML theory tracks | Conditional fit | A genuine learning problem with dimension/sample/computation guarantees or a convincing general inference phenomenon. Architecture novelty is not available from this project. |

## Capability and lifecycle audit

The original idea is occupied at the generic level; the revised idea is a targeted generalization with a proved mathematical nucleus. Resource constraints, advisor support, weekly time and research background were not supplied, so no personalized timeline or success probability is invented. The current simulations are CPU-only. More proof work, not a larger benchmark budget, is the critical next resource. The sensible project stage is independent theorem/novelty review followed by one sharply selected theoretical extension.

## Audit verdict versus publication decision

The mathematical audit verdict is **B — rigorous but can be strengthened**: all stated results have complete internally checked proofs. This does not upgrade the publication recommendation to submission-ready. The uniform loading theorem, finite-variance full-rate construction, energy refinement and explicit assumption counterexamples strengthen the project, but generic product geometry, robust mean estimation and modulus lower bounds remain established prior art. See `../audit/final_verdict.md` for precise improvements and source-access limitations.
