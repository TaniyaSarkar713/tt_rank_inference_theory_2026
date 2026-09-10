# Selected-cross simulation findings

There are 95,000 independent Gaussian regression sufficient-statistic realizations, 5,000 per setting, and 380,000 interval records. The ambient embedding has p=2,560,000, while only m=21 selected features enter inference. The full ambient design is not materialized: Wishart/normal/chi-square sampling exactly reproduces the sufficient-statistic law of the specified regression. This demonstrates the prespecified-coordinate theorem, not adaptation to unknown orientations.

At nominal 95% coverage, 5,000 replications give coverage Monte Carlo SE 0.00308 (about 0.31 percentage points). All-success rows have plug-in MCSE zero but a nontrivial Wilson lower limit. Conditional common-ball coverage and dataset-wise length dominance were checked for every stored interval.

|   bond_over_tn | method      |   coverage |   coverage_mcse |   mean_length |   length_mcse |   mean_length_over_scale |
|---------------:|:------------|-----------:|----------------:|--------------:|--------------:|-------------------------:|
|              0 | cross_joint |     1      |      0          |   0.0264849   |   3.36234e-06 |             11.9857      |
|              0 | scalar_t    |     0.9516 |      0.00303504 |   0.00867311  |   1.35898e-06 |              3.925       |
|              2 | cross_joint |     1      |      0          |   0.0264923   |   3.3318e-06  |             95.9125      |
|              2 | scalar_t    |     0.9474 |      0.003157   |   0.00867478  |   1.3543e-06  |             31.406       |
|              8 | cross_joint |     1      |      0          |   0.0263244   |   1.72658e-05 |           6099.48        |
|              8 | scalar_t    |     0.9474 |      0.003157   |   0.00867367  |   1.34569e-06 |           2009.73        |
|             32 | cross_joint |     1      |      0          |   0.000111781 |   5.13394e-07 |           1657.61        |
|             32 | scalar_t    |     0.9498 |      0.00308804 |   0.00867362  |   1.33787e-06 |         128622           |
|            128 | cross_joint |     1      |      0          |   1.06768e-06 |   4.57532e-09 |           1013.29        |
|            128 | scalar_t    |     0.9462 |      0.00319079 |   0.00867427  |   1.38256e-06 |              8.23242e+06 |

## Paired length ratios

|   setting |      n | family          |          b |    ratio |   ratio_mcse |   mean_difference |   difference_mcse |
|----------:|-------:|:----------------|-----------:|---------:|-------------:|------------------:|------------------:|
|         0 |    512 | boundary        | 0          | 1        |  0           |       0           |       0           |
|         1 |    512 | boundary        | 0.0176777  | 1        |  0           |       0           |       0           |
|         2 |    512 | boundary        | 0.0707107  | 0.999825 |  8.84882e-05 |      -2.17931e-05 |       1.10419e-05 |
|         3 |    512 | boundary        | 0.282843   | 0.124193 |  0.000204456 |      -0.00574496  |       2.0679e-05  |
|         4 |    512 | boundary        | 1.13137    | 0.124206 |  0.000202887 |      -4.9819e-05  |       1.42627e-07 |
|         5 |    512 | local_departure | 0.0176777  | 1        |  0           |       0           |       0           |
|         6 |    512 | local_departure | 0.0707107  | 1        |  0           |       0           |       0           |
|         7 |    512 | local_departure | 0.282843   | 0.159402 |  0.000262889 |      -0.00815515  |       2.97623e-05 |
|         8 |   8192 | boundary        | 0          | 1        |  0           |       0           |       0           |
|         9 |   8192 | boundary        | 0.00441942 | 1        |  0           |       0           |       0           |
|        10 |   8192 | boundary        | 0.0176777  | 0.993706 |  0.000634118 |      -0.000166736 |       1.67975e-05 |
|        11 |   8192 | boundary        | 0.0707107  | 0.134361 |  0.000235406 |      -0.000720164 |       2.04372e-06 |
|        12 |   8192 | boundary        | 0.282843   | 0.134352 |  0.000232767 |      -6.87916e-06 |       1.6088e-08  |
|        13 |   8192 | local_departure | 0.00441942 | 1        |  0           |       0           |       0           |
|        14 |   8192 | local_departure | 0.0176777  | 0.999625 |  0.000128977 |      -9.92502e-06 |       3.41677e-06 |
|        15 |   8192 | local_departure | 0.0707107  | 0.17723  |  0.000304286 |      -0.00107797  |       3.49343e-06 |
|        16 |    512 | fixed_bond      | 0.3        | 0.123713 |  0.000201045 |      -0.00455914  |       1.57518e-05 |
|        17 |   8192 | fixed_bond      | 0.3        | 0.134432 |  0.000232817 |      -5.72297e-06 |       1.33492e-08 |
|        18 | 131072 | fixed_bond      | 0.3        | 0.136528 |  0.000239304 |      -1.78165e-08 |       4.15673e-11 |

## Fixed-bond slopes

| method         |    slope |        mcse |
|:---------------|---------:|------------:|
| cross_separate | -2.24299 | 0.000796947 |
| cross_joint    | -2.22522 | 0.00114483  |

The limiting prediction is −2 for K=4 and fixed b. Finite-grid slopes and their Monte Carlo errors do not remove finite-sample bias. Coverage remains conservative for the cross intervals; the numerator optimization certifies shorter intervals but does not solve optimal expected-length calibration. No unknown-orientation pilot or nonzero-target minimum-distance method was tested.
