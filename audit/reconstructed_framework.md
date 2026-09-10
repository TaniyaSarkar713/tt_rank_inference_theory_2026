# Reconstructed statistical framework

This is a reconstruction from the experiment, not an assumption that the manuscript's conclusions hold. Audit date: 7 September 2026. The immutable input is in `baseline_2026-09-07/`; hashes are in `baseline_hashes.json`.

## Experiment and identifiability

For K≥2 and positive integers d₁,…,d_K, the coefficient space is the finite-dimensional real Hilbert space H=⊗ₖR^{dₖ}, p=∏ₖdₖ. Vectorization uses the original mode order and preserves the Frobenius inner product. Observe the entire design matrix X∈R^{n×p} and response Y∈Rⁿ. In the primary experiment the rows are independent N_p(0,I) and Y=Xb+ε, ε independent N_n(0,σ²I); b=vec(B). σ>0 is either known or an additional nuisance parameter. No latent random factors are part of the experiment. The uₖ at the evaluation point are deterministic unknown unit vectors.

For two coefficients with the same σ, conditional equality of the Gaussian response laws is equivalent to X(b−b′)=0 almost surely. In the isotropic experiment, E||X(b−b′)||²=n||b−b′||², so the coefficient is identifiable. More generally, identifiability on a structured class Θ requires that no nonzero difference in Θ−Θ belongs to the almost-sure design nullspace. Identification of ψ alone requires aᵀ(b−b′)=0 for every observationally indistinguishable pair. Full-rank finite-sample OLS is a sufficient computational condition, not a necessary condition for structured identification. Counterexample C3 shows that structure does not automatically remove a missing direction.

TT cores have gauge freedom, including insertion of an invertible matrix and its inverse across a bond. The data law, unfolding ranks, ψ, projectors onto block lines, and the modulus depend only on B. None of the results identifies individual cores. Factor signs at a nonzero block product change parameterizations but not P_j or Q_j. At zero the factors cannot be identified, and the higher-order contact conclusion is false (C1).

The half-squared loss is ℓ(B;x,y)=(y−xᵀb)²/2. R(B)=E_{B*}ℓ and R_n(B)=n⁻¹Σℓ satisfy R(B)−R(B*)=||B−B*||²/2. With a general second-moment design Σ, the excess risk is (b−b*)ᵀΣ(b−b*)/2. Under the finite-variance extension this statement requires the conditional mean-zero assumption; infinite-variance loss is not introduced. The risk is descriptive, not the main theorem's evaluation criterion.

## Structured class and estimand

The prefix unfolding B^[k] has dimensions (∏_{i≤k}d_i)×(∏_{i>k}d_i). All caps r̄_k are positive integers, not necessarily attainable maxima; redundant caps do not hurt the statements. Θ₀={B:rank B^[k]≤r̄_k, ||B||≤M}; Θ_η={B:||B||≤M, dist(B,Θ₀)≤η}. η≥0 is a specified deterministic coefficient-distance allowance. It is neither an outlier fraction nor an estimated structural certificate. Every TT rank stratum below the caps is in the coverage class. Positive caps ensure nontrivial elementary directions are feasible.

The strengthened paper also proves the same relevant results for the unbounded closed rank class and its distance tube. Global boundedness was a technical convenience; the nonzero local signal restriction remains.

The target ψ_A(B)=⟨A,B⟩ has a deterministic prespecified loading. The original theorem fixed A. The revised theorem is uniform over deterministic A and permits A=A_n; this expected-length formula does not permit substituting an arbitrary data-selected loading without controlling dependence. The common confidence event does give simultaneous coverage for all loadings, hence coverage for a data-selected loading and its random target. It does not give coverage conditional on the selection event. A=0 is now included in the multiscale theorem, with the exact zero interval and zero modulus; q is defined only for nonzero A.

The evaluation point is B₀=λ⊗uₖ, λ>0 (and λ<M/2 for the bounded-class version). This is a property of the point where length is evaluated, not a restriction that all true coefficients in the honesty class are rank one. Known cap-one cuts induce J blocks with factors v_j. For Π_l the true degree-l block projector, a_l=||Π_l A|| and

R_A(t)=(a₀+a₁)t+Σ_{l=2}^J a_l t^l/λ^{l−1}.

The exact contact order q=max(1,min{l:a_l>0}) is a useful fixed-loading limit, but R_A is the correct uniform quantity near degeneracy.

## Procedures, quantifiers and benchmark

With S=XᵀX invertible, z=S⁻¹XᵀY is unique OLS. A rank-one block HOSVD gives Bhat. It is a deterministic spectral construction; neither a globally optimal TT fit nor a stationary point of a nonconvex algorithm is assumed. Rank-one projection residual ≤√J||z−B₀|| is proved directly. Internally TT-infeasible pilots are allowed because coverage uses the containing block-product class.

A valid simultaneous Euclidean confidence ball supplies e. The graded product certificate bounds every candidate in that ball enlarged by η; it is intersected with the projection of the SAME ball. The Gaussian scalar z/t interval is a simulation baseline, not a permissible replacement for the common ball projection in this proof without recalibrating simultaneous coverage. On an empty intersection the reported interval is {aᵀz}, of length zero. Coverage on the common event guarantees the intersection is not empty there.

For 0<α<1/2, honesty means inf_{B∈Θ_η} P_{B,σ}{ψ_A(B)∈I}≥1−α. For unknown σ this holds jointly for all σ>0. L_{η,α}(B₀;σ) is the infimum of E_{B₀,σ}|I| over these procedures. This is a pointwise expected-length optimum subject to global coverage, not the minimax estimation risk sup_B E||Bhat−B||². The lower bound allows all measurable intervals, including randomized intervals if the randomization is independent and shared across experiments. No estimator regularity is imposed.

Finite-sample coverage is uniform over the stated parameter class and conditional on any admissible fixed design. Expected length is evaluated at the rank-one points; constants are uniform over loading and unit directions after the audit but not over growing dimensions. The revised Gaussian sufficient sample condition is n≥p+max(J,2); n>p alone suffices for the residual pivot. The local condition σ/√n≤cλ is explicit. The theory is a finite-sample inequality with fixed-dimensional constants, not merely an O_P statement.

## Measurability and existence

Rank constraints are closed polynomial zero sets. Bounded Θ₀ is compact; unbounded Θ₀ still attains nearest-point distances because a minimizing sequence is bounded. No measurable nearest-point selector is needed for coverage: for each realized finite B a point exists and the deterministic inequality holds for every such point.

A fully specified measurable leading eigenvector rule is available. Form the orthogonal projector E onto the top eigenspace, choose the smallest coordinate i with ||Ee_i||>0, and take Ee_i/||Ee_i||. Eigenvalues and their eigenspace projectors are Borel functions, so this finite rule is measurable even at ties. Apply it to each unfolding covariance; absorb the sign of the final scalar contraction into the first factor and use a fixed convention at zero. NumPy SVD is used in simulations; almost-sure simple leading singular values under continuous Gaussian OLS make tie choices immaterial to those results. This observation is not used to discard ties in the deterministic coverage theorem.

## Independent finite-variance completion

The median-OLS branch in R17 keeps Gaussian design and iid observation pairs but only assumes zero conditional error mean and a known conditional variance upper bound. Its sample condition is floor(n/g)≥2p+2 with g=2(floor(J/2)+1)−1. It supplies unconditional coverage and a matching worst-noise expected-length scale at B0; this is a different quantifier over noise laws from the fixed-Gaussian-sigma L. C12 shows why the union over every unspecified finite conditional variance bound cannot support shrinking globally honest intervals.
