# Empirical findings

186,000 independent datasets; 93 settings; 705 method/functional summary rows.

## Rate checks

| profile           |   q |   p |   theory |   primary_slope |   late_slope |   late_slope_mcse |
|:------------------|----:|----:|---------:|----------------:|-------------:|------------------:|
| four_slack        |   1 |  16 |     -0.5 |       -0.547814 |    -0.502685 |       9.44466e-06 |
| four_two_blocks   |   2 |  16 |     -1   |       -1.07116  |    -1.00306  |       0.00202182  |
| three_product     |   3 |   8 |     -1.5 |       -1.56318  |    -1.50383  |       0.00404533  |
| four_three_blocks |   3 |  16 |     -1.5 |       -1.6052   |    -1.49981  |       0.00295814  |
| six_singular      |   3 |  64 |     -1.5 |       -1.77594  |    -1.51069  |       0.00162883  |
| four_product      |   4 |  16 |     -2   |       -2.13646  |    -2.00989  |       0.00377104  |

The large-n slopes use a transparent post-primary addendum. Their Monte Carlo errors account for simulation means, not asymptotic approximation bias.

## Pointwise versus local coverage

|   c | method                |   coverage |   coverage_mcse |   coverage_lo |   coverage_hi |   mean_length |
|----:|:----------------------|-----------:|----------------:|--------------:|--------------:|--------------:|
|   0 | graded                |     1      |      0          |      0.998083 |      1        |   1.72019e-05 |
|   0 | degree_wald           |     0.9535 |      0.00470838 |      0.94337  |      0.961891 |   1.57478e-08 |
|   0 | known_rank_wald       |     1      |      0          |      0.998083 |      1        |   6.92702e-11 |
|   0 | selected_rank_wald_k2 |     1      |      0          |      0.998083 |      1        |   1.66293e-08 |
|   1 | graded                |     1      |      0          |      0.998083 |      1        |   1.95103e-05 |
|   1 | degree_wald           |     0.5205 |      0.0111709  |      0.498587 |      0.542334 |   3.568e-08   |
|   1 | known_rank_wald       |     0.9225 |      0.00597887 |      0.909955 |      0.933425 |   1.0704e-07  |
|   1 | selected_rank_wald_k2 |     0.3655 |      0.0107682  |      0.344671 |      0.386845 |   5.10192e-08 |
|   2 | graded                |     1      |      0          |      0.998083 |      1        |   2.376e-05   |
|   2 | degree_wald           |     0.475  |      0.0111664  |      0.453183 |      0.496913 |   9.66209e-08 |
|   2 | known_rank_wald       |     0.849  |      0.00800622 |      0.83264  |      0.864022 |   2.89863e-07 |
|   2 | selected_rank_wald_k2 |     0.5525 |      0.0111185  |      0.530628 |      0.574171 |   2.02602e-07 |
|   4 | graded                |     1      |      0          |      0.998083 |      1        |   3.6014e-05  |
|   4 | degree_wald           |     0.482  |      0.0111731  |      0.460157 |      0.503912 |   3.60987e-07 |
|   4 | known_rank_wald       |     0.9255 |      0.00587153 |      0.913158 |      0.93621  |   1.08296e-06 |
|   4 | selected_rank_wald_k2 |     0.9155 |      0.00621931 |      0.9025   |      0.926907 |   1.0696e-06  |
|   8 | graded                |     1      |      0          |      0.998083 |      1        |   6.70542e-05 |
|   8 | degree_wald           |     0.488  |      0.0111771  |      0.466137 |      0.509909 |   1.40521e-06 |
|   8 | known_rank_wald       |     0.939  |      0.00535159 |      0.927646 |      0.948671 |   4.21564e-06 |
|   8 | selected_rank_wald_k2 |     0.939  |      0.00535159 |      0.927646 |      0.948671 |   4.21564e-06 |

## Structural departure

| eta_kind   |         eta | method      |   coverage |   coverage_mcse |   mean_length |
|:-----------|------------:|:------------|-----------:|----------------:|--------------:|
| fast       | 9.59075e-09 | graded      |     1      |      0          |   1.73494e-05 |
| fast       | 9.59075e-09 | ambient     |     0.939  |      0.00535159 |   0.0173975   |
| fast       | 9.59075e-09 | tube_graded |     1      |      0          |   1.73686e-05 |
| 100fast    | 9.59075e-07 | graded      |     1      |      0          |   1.72892e-05 |
| 100fast    | 9.59075e-07 | ambient     |     0.9505 |      0.00485024 |   0.0173941   |
| 100fast    | 9.59075e-07 | tube_graded |     1      |      0          |   1.92085e-05 |
| 10000fast  | 9.59075e-05 | graded      |     0      |      0          |   1.72503e-05 |
| 10000fast  | 9.59075e-05 | ambient     |     0.9585 |      0.00445969 |   0.017395    |
| 10000fast  | 9.59075e-05 | tube_graded |     1      |      0          |   0.000209184 |
| quadratic  | 6.51042e-06 | graded      |     0.847  |      0.00804957 |   1.72173e-05 |
| quadratic  | 6.51042e-06 | ambient     |     0.951  |      0.00482696 |   0.01739     |
| quadratic  | 6.51042e-06 | tube_graded |     1      |      0          |   3.02462e-05 |
| ambient    | 0.00441942  | graded      |     0      |      0          |   1.80868e-05 |
| ambient    | 0.00441942  | ambient     |     0.9605 |      0.00435544 |   0.0173989   |
| ambient    | 0.00441942  | tube_graded |     1      |      0          |   0.0088628   |

## Limits

All graded intervals covered in the main exactly specified contact experiments. At 2000/2000, the Wilson interval is approximately [0.9981,1]; this documents conservatism and does not prove population coverage one. The narrow degree-calibrated intervals are pointwise benchmarks with poor local coverage. Neither their short width nor the conservative method’s coverage proves efficient constants. Stress diagnostics outside Gaussian homoskedastic errors do not establish robustness.
