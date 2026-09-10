# Internal proof audit, 9 September 2026

This is a step-by-step mathematical audit, supplemented by numerical falsification checks. It is not independent peer review or formal verification. The earlier 17-result manuscript inventory remains a historical inventory; the new revision has its own result identifiers.

## Audit of the input rank-two theorem

| Input claim | Verification | Finding |
|---|---|---|
| Exact ranks and pivot strength | Each prefix is a sum of two orthogonal outer products; its singular values are a,b. Weyl transfers perturbation t to each selected pivot. | Correct for b>0; exact rank is lost at b=0. |
| Exact cross identity T4 | In a rank-capped matrix an invertible maximal pivot supplies a column basis. Repeated application along prefix cuts reconstructs the target. | Correct; established cross interpolation, not a new identity. |
| Energy upper bound T2 | Each target slice has its sole coordinate 2 in a different physical mode. Coordinate sets are disjoint. Apply Frobenius submultiplicativity and AM–GM. | Correct; gives the sharp K^{-K/2} coefficient. |
| Lower path T2 | Expand a product of e1+s e2; all physical masks are orthogonal, squared distance is b²[(1+s²)^K−1]. | Correct and feasible under every cap. |
| Uniform transition T1 | Verify mean-value lower bound for t/b≤1 and a monotone ratio for t/b≥1. Use the ambient upper bound when pivots are not stable. | Correct uniformly in b and a≥b. |
| Single-unfolding comparison | Matrix model has two disjoint off-pivot slices and an attainable row/column rotation. Its modulus is t²/(2b). | Correct comparison to each single-cut relaxation. Does not rule out matrix encodings with extra nonlinear constraints. |
| Coverage T5 | The common Gaussian confidence event includes the truth; positive denominator bounds certify true pivot invertibility. Empty intersections cannot occur on this event. | Correct. Original ambient OLS requires n>p. |
| Moments and lower bound T6–T7 | Kth inverse-Wishart moment needs n−p+1>K. Two-point transport requires α<1/2. | Correct with the explicit α restriction now stated in the new revision. The sharp geometric constant is not a sharp confidence-length constant. |

No counterexample to the mathematical rank-two statements was found. The substantive weaknesses were their scope and interpretation, not an algebraic failure. The preserved input note is not rewritten as though it contained the subsequent extensions.

## General modulus: G1 and G2

1. **Physical normality.** Check the stronger assumption B*×j wjᵀ=0 in every mode. Without it the Kth-order conclusion is false, even at rank one.
2. **Canonical representation.** For a nearby feasible B with t<βmin, Weyl ensures exact ranks. Left-orthonormal interfaces identify Qj's eigenvalues with unfolding singular values. No incoherence, chosen cross, or spectral gap between nonzero singular values is required.
3. **Upper-bound factorization.** Writing Zj=HjQj makes each ||Zj|| exactly a full physical contraction norm. The target factors with one inverse Qj per bond.
4. **Overlap correction.** Full physical contractions overlap. They cannot simply be assigned total squared energy t². The proof retains pairwise contractions and shows their contribution is at most t⁴Σ(βi−t)^{-2}. This is the key additional lemma relative to the selected-entry rank-two proof.
5. **Sharp attainability.** Adjacent rank-one matrices built from weakest eigenvectors of Qj align every inverse factor. Single-core perturbations have total squared energy one. Distinct physical masks make all expansion terms orthogonal.
6. **Uniform remainder.** Bound every size-s mask by K^{-s/2}βmin^{-(s−1)}. The explicit feasible u=t exp(−t²/(2βmin²)) makes the lower asymptotic uniform in dimension, rank and reference for fixed K.
7. **Weak family.** An arbitrary background supported in complementary physical spaces has unfolding singular values orthogonal to the added product. This establishes a complete transition when all weakest bond singular values equal b. It does not classify unequal simultaneous rank losses.

Numerical checks used 36 non-diagonal references with K=3,4,5 and varying rank profiles. They checked prefix spectra, attainable-path coefficients, distances and upper energy inequalities. Such checks supplement the proof; they do not prove a universal inequality.

## Calibrated cross inference: C1–C5

1. Count distinct entries, not entries with multiplicity: 2K pivots, 4K−4 target slices, one estimand, giving m=6K−3.
2. Gaussian omitted coordinates become independent noise only after conditioning on the selected design. Its variance is σ²+||B outside F||². Conditioning on the full design would invalidate this argument.
3. The normal and residual chi-square projections yield an exact F ellipsoid. Conversion to a Euclidean ball preserves coverage and introduces conservatism.
4. The numerator optimization has a strictly concave logarithm, positive coordinates, an active quadratic constraint, and a unique scalar multiplier. Its monotone root bracket gives an upper certificate in exact arithmetic.
5. Numerator and denominator error budgets are not fully coupled. The new interval is provably no longer than the separate-bound baseline, but is not the exact confidence-region image.
6. At the aligned weak-component family the omitted signal is zero. Inverse-Wishart moments yield an ambient-dimension-free rate with fixed m. On failed-pivot outcomes, ambient length is controlled by the same Kth moment; there is no unaccounted rare-event term.
7. The lower bound uses full-data KL and an alternative satisfying every TT cap. Thus allowing an adversary to use all p features does not weaken the lower bound.
8. General cross patterns inherit coverage. Their denominators involve chosen pivot singular values, which must not be substituted for unfolding singular values in a minimax lower bound.

The implementation was checked against 80-digit roots in 30 cases; maximum relative numerator discrepancy was 6.09×10^{-14}. Floating-point padding is not a directed-rounding proof. All 95,000 stored datasets obeyed interval-length dominance and truth inclusion whenever the common ball covered.

## Learned compression: D1–D3

1. Training and inference are independent. Include the loading direction in every learned mode subspace, preserving the target exactly.
2. Product projection cannot increase prefix ranks; omitted Gaussian signal changes the variance. No unsupported low-TT-rank assertion about an arbitrary coordinate vector is used.
3. Closed rank constraints and the norm cap make inversion compact. Semialgebraic projection/selection identifies measurable endpoints and a measurable global pilot. This is existence, not an efficient optimization theorem.
4. Small projection error preserves the nonzero bond singular values by Weyl. Commutation with the loading projections preserves physical normality.
5. Balanced weakest bond singular values are explicitly required in the expected-length upper bound. They control the failed-localization contribution by the desired product denominator. The geometric theorem itself does not need balance.
6. The pilot difference lies in a Tucker envelope with mode ranks min(dj,2 r_{j−1}rj). Net construction, K+1 telescoping errors, chi-square tails, conditional Gaussian noise and the least-squares inequality are all displayed. The constant 18 follows from dividing 8 by 4/9.
7. The training failure term 2Mδ remains visible. A matching local lower bound needs an interior norm-cap margin.
8. The sufficient training condition n1 b²/σ² ≳ W+x excludes the unidentified weak-direction regime when W grows. No necessity of that condition has been established.

## Minimum-distance calibration: M1–M2

For the zero-product null, the distance statistic is min Zj²; taking all but one null coordinate to infinity proves the exact worst-case chi-square calibration. Boundary rejection α^K explains overcoverage for this statistic. This does not calibrate a nonzero target.

The general finite-computation certificate separates four errors: mean-region failure, finite covering in total variation, Monte Carlo binomial bounds, and optimization bounds. The observed distance needs a lower bound while simulated distances need upper bounds. A local optimizer gives the wrong bound for the observed distance. Conditional Monte Carlo counts are fixed and iid; adaptive stopping is not covered. Continuum inversion remains a separate computational requirement. The generic principle is prior art.

## Result inventory and dependency order

| Identifier | Status | Role |
|---|---|---|
| G1 | PROVED | Sharp physically normal modulus for general TT ranks |
| G2 | PROVED | General-background weak-component transition |
| C1 | PROVED | Selected-coordinate Gaussian regression identity |
| C2 | PROVED | Unknown-variance finite-sample coverage |
| C3 | PROVED | Optimized numerator and length dominance |
| C4 | PROVED | Matching weak-bond length scale with arbitrary ambient dimensions |
| C5 | PROVED | Fixed higher-rank cross extension, upper bound only |
| D1 | PROVED | Honest inference after learned mode compression |
| D2 | PROVED | Conditional rate plus explicit training-failure term |
| D3 | PROVED | Global-pilot existence bound with explicit dimension dependence |
| M1 | PROVED | Exact zero-product worst-case calibration |
| M2 | PROVED | Conditional finite-computation certificate |
| Efficient unknown-orientation weak-boundary procedure | PARTIAL | Current pilot condition excludes the target regime |
| Nonzero-target minimum-distance interval algorithm | PARTIAL | Certificate exists; optimization and inversion are not implemented |
| Optimal expected-length constants | CONJECTURED/OPEN | No candidate sharp constant is promoted to a theorem |

Dependency order: physical-mask/interface lemmas → G1 → G2 and D2; exact cross identity → C1/C2 → C3 → C4; compact inversion → D1, covering bound → D3, together with G1 → D2. Gaussian two-point transport supplies the statistical lower bounds. M1/M2 are separate calibration results and are not prerequisites for C4.
