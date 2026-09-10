**This project studies how low-rank tensor structure can make statistical estimates unusually precise—and when that advantage disappears.** It combines mathematical proofs, confidence-interval algorithms, and simulation experiments.

This explanation focuses on the current September 9, 2026 revision.

A **tensor** is a multidimensional array. A vector has one index, a matrix has two, and a four-way tensor has entries

$$
B_{i_1,i_2,i_3,i_4}.
$$

For example, a $40\times40\times40\times40$ tensor contains $40^4=2{,}560{,}000$ numbers. The project assumes these numbers have a simpler underlying structure.

A **tensor train**, abbreviated TT, represents each entry through a chain of small matrix products:

$$
B_{i_1,i_2,i_3,i_4}=G_1(i_1)G_2(i_2)G_3(i_3)G_4(i_4).
$$

The matrix sizes fit together as

$$
(1\times r_1)(r_1\times r_2)(r_2\times r_3)(r_3\times1),
$$

so the final result is one number. Small intermediate dimensions allow a compact representation. This is the standard TT construction described in [Oseledets’s foundational paper](https://users.math.msu.edu/users/iwenmark/Teaching/CMSE890/TENSOR_oseledets2011.pdf).

There is an equivalent description that matters especially here: reshape the tensor into a matrix at each cut,

$$
i_1\mid i_2i_3i_4,\qquad
i_1i_2\mid i_3i_4,\qquad
i_1i_2i_3\mid i_4,
$$

and require the corresponding matrix ranks to be small. Matrix rank counts the number of independent column directions. The project imposes **all these rank constraints together**.

The statistical model is ordinary linear regression with tensor-shaped predictors:

$$
Y_i=\langle X_i,B\rangle+\varepsilon_i,
\qquad
\langle X_i,B\rangle
=\sum_{i_1,\ldots,i_K}
(X_i)_{i_1,\ldots,i_K}B_{i_1,\ldots,i_K}.
$$

Here \(X_i\) is observed, \(Y_i\) is the observed response, and \(B\) is the unknown coefficient tensor. In the current main results, predictor entries are independent standard Gaussian variables, and the errors are independent Gaussian variables with unknown standard deviation \(\sigma\).

The goal is to estimate **one chosen number**
\[
\psi_A(B)=\langle A,B\rangle.
\]
The known tensor \(A\), called a *loading*, specifies what we care about. It might select one entry of \(B\), or form a weighted combination of entries.

A confidence interval must be **honest**: its coverage guarantee must hold for every tensor allowed by the stated rank caps. For a 95% interval \(I_n\), this means
\[
\inf_{\substack{B\in\Theta_r\\ \sigma>0}}
P_{B,\sigma}\{\psi_A(B)\in I_n\}\ge0.95,
\]
where \(\Theta_r\) denotes the allowed tensor class.

In repeated experiments, the procedure must cover the true answer at least 95% of the time at every allowed parameter. The actual ranks can be lower than the caps. Consequently, uncertainty about rank must be respected.

**The central mathematical idea is to measure how much the target can change when the tensor changes slightly.** The project calls this the *local modulus*:

$$
\omega_A(t;B_* ) = \sup_{B\in\Theta_r, \|B-B_{\star}\|_F\le t}
|\psi_A(B)-\psi_A(B_*)|.
$$

The Frobenius norm \(\|\cdot\|_F\) is the square root of the sum of squared entries.

Read this formula as:

> Among all allowed tensors within distance \(t\) of \(B_*\), how far can the answer move?

Usually, the answer moves by an amount proportional to \(t\). But tensor constraints can force it to move only by an amount proportional to \(t^2,t^3,\) or \(t^4\). This exponent is the project’s **contact order**.

The four-way example makes this concrete. Let \(e_0,e_1,e_2\) be three perpendicular coordinate directions, and consider
\[
B_b=a\,e_0^{\otimes4}+b\,e_1^{\otimes4},
\qquad a\ge b>0.
\]
The notation \(e_j^{\otimes4}\) means multiplying four copies of the vector to form a product tensor. Thus \(B_b\) has two nonzero entries: \(a\) at \((0,0,0,0)\) and \(b\) at \((1,1,1,1)\).

Every TT rank is two. Our target is the unused entry
\[
\psi(B)=B_{2,2,2,2}.
\]
Its value at \(B_b\) is zero, but the statistical procedure does not get to assume that nearby tensors also have zero target.

To create a nonzero target while keeping ranks at most two, perturb the weaker component:
\[
B(s)=a\,e_0^{\otimes4}
+b(e_1+s e_2)^{\otimes4}.
\]
The target becomes
\[
\psi(B(s))=bs^4.
\]
Why the fourth power? To reach entry \((2,2,2,2)\), we must select the \(s e_2\) contribution in **all four factors**.

Meanwhile,
\[
\|B(s)-B_b\|_F^2
=b^2\big[(1+s^2)^4-1\big]
\approx4b^2s^2.
\]
Therefore, a tensor perturbation of size \(t\) corresponds approximately to \(s=t/(2b)\), giving
\[
\psi(B(s))\approx\frac{t^4}{16b^3}.
\]

This calculation supplies one feasible path. The project also proves that no allowed nearby tensor can produce a larger leading-order change:
\[
\boxed{\omega_A(t;B_b)\sim\frac{t^4}{16b^3}
\quad\text{when }t/b\to0.}
\]
Here \(\sim\) means the ratio of the two quantities approaches one. The derivation appears in the [rank-two geometry note](theory/active_rank_two_modulus.md).

**The surprising change happens when \(b\) disappears.** At \(b=0\), the reference has rank one, but the allowed class still permits rank two. We can then add
\[
B'=a e_0^{\otimes4}+t e_2^{\otimes4}.
\]
This changes the tensor by distance \(t\) and changes the target by exactly \(t\). Hence
\[
\omega_A(t;B_0)=t.
\]

Losing the weak component opens an additional feasible direction. The target changes from fourth-order sensitivity to first-order sensitivity.

For comparing nearby coefficients in this regression model, the natural statistical scale is \(t_n=\sigma/\sqrt n\). The project proves matching lower and upper bounds for the best expected length of an honest interval at this example:

| Strength of the weak component | Best possible expected-length order, for four modes |
|---|---|
| \(b\) is much larger than \(\sigma/\sqrt n\) | \(\displaystyle \frac{\sigma^4}{b^3n^2}\) |
| \(b\) is comparable to or smaller than \(\sigma/\sqrt n\) | \(\displaystyle \frac{\sigma}{\sqrt n}\) |

These are rates up to constant factors. The \(n^{-2}\) rate concerns this particular, locally insensitive target at these reference tensors. It does not mean the entire tensor can be estimated that quickly.

The combined TT constraints matter: keeping only one matrix-unfolding rank constraint gives quadratic behavior, approximately \(t^2/(2b)\), instead of quartic behavior.

The latest revision extends the geometric result beyond this example. For a \(K\)-way reference whose exact ranks equal the caps, it proves
\[
\omega_A(t;B_*)
\sim
\frac{t^K}
{K^{K/2}\beta_1\cdots\beta_{K-1}}.
\]
Each \(\beta_j\) is the smallest nonzero singular value at a TT cut, measuring the strength of its weakest retained direction.

There is a substantial condition: \(A=w_1\otimes\cdots\otimes w_K\), and the signal must vanish when contracted against \(w_j\) in **each individual mode**. This is stronger than merely having \(\psi_A(B_*)=0\). The [general theorem and proof](theory/general_normal_modulus.md) state that restriction explicitly.

**The implemented method turns this geometry into confidence intervals.** Its main steps are:

1. Fit a regression using a carefully chosen collection of tensor coordinates.
2. Construct a simultaneous confidence region for those coefficients.
3. Use exact TT identities to bound the target throughout that region.
4. Apply the sharper bound when the required matrix inverses can be certified; otherwise use the ordinary bound.

For four modes, it uses only \(6K-3=21\) selected predictors. Under the Gaussian design, omitted predictors contribute additional independent noise, whose variance is estimated in the reduced regression. This makes inference possible even when the ambient tensor has millions of entries.

The improved implementation also shares one error budget across the relevant slices, producing intervals no longer than its earlier version. These calculations are in [methods.py](simulations/code/tt_revision/methods.py).

The repository’s parts support different stages of this argument:

| Location | Purpose |
|---|---|
| `theory/` | Statements and mathematical proofs |
| `paper/revision_2026_09_09/` | Current integrated manuscript |
| `simulations/code/tt_revision/` | Interval algorithms and numerical experiments |
| `simulations/results/` | Saved results and analyses |
| `audit/` and `literature/` | Assumption checks, limitations, and comparisons with earlier research |

The [latest simulation analysis](simulations/results/tt_revision_2026_09_09/analysis.md) reports 95,000 independent simulated datasets. It supports the implemented interval improvement and shows substantial conservatism: coverage often exceeds the nominal 95%. The structured intervals are not always shorter than ordinary intervals.

The remaining research questions concern broader target directions, learning unknown signal orientations, and reducing conservative interval lengths. The strongest computable length guarantee currently uses prespecified coordinates; learning those directions is a separate, harder problem. The project contains internally checked proofs and simulations, with real-data applications and independent peer review still outstanding.
