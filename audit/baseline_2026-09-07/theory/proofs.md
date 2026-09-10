# Proof map and audit

The canonical complete mathematical derivations are in [paper/appendix.tex](../paper/appendix.tex), included in the manuscript PDF. Keeping one canonical proof source avoids divergent copies.

1. Product factorization: inductively peel cap-one prefix cuts; internal ranks are preserved by nonzero external products.
2. Contact upper bound: projection off candidate factor lines bounds each angle by t/lambda; degree-s components are bounded by (lambda+t)(t/lambda)^s. For t>=lambda use Cauchy–Schwarz.
3. Contact lower bound: choose a nonzero elementary coefficient in a minimal mask. Each active block follows v+s w, whose internal TT ranks are at most two. The exact distance is lambda sqrt((1+s²)^q-1); the target is lambda c_A s^q.
4. Leading elementary constant: use the positive local product chart and arithmetic–geometric mean under the perturbation energy constraint.
5. Honest lower bound: compute joint KL exactly; Pinsker and the event that an interval contains both targets give the two-point bound. No restriction to regular estimators.
6. Tube: nearest exact-class point exists by compactness. Triangle inequality gives the upper modulus; the ambient loading direction gives the missing lower term.
7. Coverage: one OLS chi-square/F ball, one product-envelope certificate, intersection on the same event. No independence assumption on the pilot is used.
8. Expected length: inverse-Wishart moments are derived from residualized Gaussian columns; HOSVD has a sqrt(J) residual bound. Projector mixing forces lower pilot degrees to vanish at the appropriate powers of pilot error. The bad localization event is bounded by a higher moment instead of being ignored.
9. Complexity: exact three-block coefficient equals an already hard tensor norm. No new hardness theorem is claimed.

## Explicit failure-point audit

- A zero loading has trivial interval and is excluded.
- Zero pilot, large localization radius, empty interval intersection: all have defined fallbacks.
- Internal cap constraints need not hold for the pilot; only the containing product envelope is used for coverage.
- Unknown sigma is estimated from ambient OLS residuals, valid even when the coefficient is outside the exact rank class.
- Fixed geometry is essential for the moment constants and the choice of a nonzero elementary loading coefficient.
- Original-mode rank one is essential for the internal rank-two witness paths.
- The norm cap has an interior margin, so the witness alternatives are feasible.
- q is capped below by one: radial changes are first order, not order zero.
- Uniform honesty is over the parameter class, while the short-length assertion is pointwise at rank-one signals.
- No claims of efficient constants, minimax adaptation to unknown eta, or inference in p>=n are made.
