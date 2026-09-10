# Assumptions, necessity and weakening opportunities

| Assumption | Where needed | Why / failure if removed | Possible weakening |
|---|---|---|---|
| Fixed tensor order K | All uniform statistical constants | Kth moments and selected dimension grow with K. | Track K explicitly; no growing-K rate is currently claimed. |
| Exact reference ranks and t<βmin | G1 | Inverses in canonical interfaces require full bond rank. | G2 treats a specified rank-loss family; unequal losses remain open. |
| Product loading, absent from signal in every mode | G1, G2, D2 | Forces every core in the target contraction to change. Two normal modes can give only quadratic contact. | Classify partially normal/dense loadings by a tensor multilinear jet; not proved here. |
| iid isotropic Gaussian design | C and D statistical results | Gives independent selected/omitted predictors and exact F calibration. | Known covariance plus a variance-corrected orthogonalization may work, but rank structure need not survive arbitrary whitening. |
| Independent homoscedastic Gaussian errors, unknown σ>0 | Exact F calibration | Orthogonal projection independence and chi-square residual law are used. | Earlier project robust localizers concern a different branch; no automatic transplant. |
| Prespecified coordinate crosses | C4 short-length claim | At the displayed family all signal is included in selected coordinates. Arbitrary rotations can have large omitted variance or weak pivots. | D1–D3 learn subspaces, with a stronger sample requirement. |
| n≥m+max(K,2) | C4, D2 | Ensures Kth inverse-Wishart moments. Coverage itself only needs n>m. | Alternative bounded localizers might weaken moment requirements. |
| Fixed rank caps in statistical growth regime | D3 | Compressed dimension and Tucker core entropy are then bounded. | Explicit formulas are provided, but they are not rank-optimal for growing ranks. |
| Balanced βj∈[b,κb] | D2 only | Converts fallback control in βmin into control with product βj. | Refined rare-event concentration could treat imbalance. |
| Global constrained least-squares pilot | D3 | Basic inequality holds at a global minimizer. | Certified approximate global minimization or a specified initialized algorithm needs its own proof. |
| Norm cap and interior margin | D1–D3 | Bounds bad-training contribution and preserves the lower-bound path. | Remove cap using additional moment/tail control; C4 already has no norm cap. |
| Fresh fixed-count iid Monte Carlo; certified bounds and finite cover | M2 | Ensures conditional Clopper–Pearson coverage and valid transport. | Anytime-valid simulation and branch-and-bound certification are possible extensions. |
| 0<α<1/2 | Two-point lower bounds | Leaves positive mass for simultaneous endpoint coverage. | Upper coverage statements allow 0<α<1. |

No claims are made for dependent observations, contamination, covariance estimation, neural-network training trajectories, unbounded K, or unknown rank caps. Rank may vary within a prespecified capped class; that is the sense in which honesty accommodates rank uncertainty.
