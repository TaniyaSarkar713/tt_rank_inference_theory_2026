"""Small algebraic/numerical checks; not Monte Carlo coverage validation."""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.stats import chi2, norm


def tensor_from_cores(cores):
    value = cores[0]
    for core in cores[1:]:
        value = np.tensordot(value, core, axes=(-1, 0))
    return value.squeeze(axis=(0, -1))


def cross_parts(B):
    K = B.ndim
    pivots = [np.array([[B[(u,) * k + (v,) * (K-k)]
                          for v in range(2)] for u in range(2)])
              for k in range(1, K)]
    slices = [np.array([[B[(2,) + (v,) * (K-1)] for v in range(2)]])]
    for k in range(1, K-1):
        slices.append(np.array([[B[(u,) * k + (2,) + (v,) * (K-k-1)]
                                  for v in range(2)] for u in range(2)]))
    slices.append(np.array([[B[(u,) * (K-1) + (2,)]] for u in range(2)]))
    return pivots, slices


def cross_interval(z, e):
    pivots, slices = cross_parts(z)
    lower = [np.linalg.svd(S, compute_uv=False)[-1] - e for S in pivots]
    center = float(z[(2,) * z.ndim])
    left, right = center-e, center+e
    if min(lower) > 0:
        H = np.prod([np.linalg.norm(C)+e for C in slices])/np.prod(lower)
        left, right = max(left, -H), min(right, H)
        if left > right:
            return center, center
    return float(left), float(right)


def run():
    rng = np.random.default_rng(20260908)
    alpha = .05
    z = norm.ppf(1-alpha)
    radius = np.sqrt(chi2.ppf(1-alpha, 3))
    lower = 2/(3*np.sqrt(3))*((z**3+3*z)*norm.cdf(z)+(z*z+2)*norm.pdf(z))
    integral = 2/np.sqrt(3)*quad(lambda x:x*x*norm.cdf(z-x), 0, np.inf)[0]
    assert abs(lower-integral) < 1e-10
    mean_chi = 2*np.sqrt(2/np.pi)
    upper = 2/(3*np.sqrt(3))*(4*mean_chi+9*radius+3*radius**2*mean_chi+radius**3)
    checks, max_cross_error, witness_errors = 0, 0., []
    for K in (3, 4, 5):
        a, b = 2., .7
        B0 = np.zeros((3,)*K)
        B0[(0,)*K], B0[(1,)*K] = a, b
        cores = [np.zeros((1,3,2))]
        cores[0][0,0,0], cores[0][0,1,1] = a, b
        for _ in range(K-2):
            core = np.zeros((2,3,2))
            core[0,0,0], core[1,1,1] = 1., 1.
            cores.append(core)
        last = np.zeros((2,3,1))
        last[0,0,0], last[1,1,0] = 1., 1.
        cores.append(last)
        assert np.allclose(tensor_from_cores(cores), B0)
        for _ in range(100):
            B = tensor_from_cores([C+.005*rng.normal(size=C.shape) for C in cores])
            t = np.linalg.norm(B-B0)
            assert t < b/2
            for k in range(1, K):
                assert np.linalg.matrix_rank(B.reshape(3**k, -1), tol=1e-10) == 2
            pivots, slices = cross_parts(B)
            value = slices[0]
            for S, C in zip(pivots, slices[1:]):
                value = value @ np.linalg.solve(S, C)
            error = abs(value.item()-B[(2,)*K])
            max_cross_error = max(max_cross_error, error)
            assert error < 1e-11
            assert sum(np.linalg.norm(C)**2 for C in slices) <= t*t+1e-12
            bound = t**K/(K**(K/2)*(b-t)**(K-1))
            assert abs(B[(2,)*K]) <= bound+1e-12
            disturbance = rng.normal(size=B.shape)
            disturbance *= .01/np.linalg.norm(disturbance)
            lo, hi = cross_interval(B+disturbance, .01000001)
            assert lo-1e-12 <= B[(2,)*K] <= hi+1e-12
            checks += 1
        # Stable evaluation of the exact feasible lower path at t/b=1e-4.
        ratio = 1e-4
        s2 = np.expm1(np.log1p(ratio**2)/K)
        normalized = s2**(K/2)/ratio**K
        sharp = K**(-K/2)
        witness_errors.append(abs(normalized/sharp-1))
        assert abs(normalized/sharp-1) < 1e-7
        for ratio in (.001, .1, 1., 10.):
            s = np.sqrt(np.expm1(np.log1p(ratio**2)/K))
            v = np.array([0.,1.,s])
            B = b*v
            for _ in range(K-1):
                B = np.multiply.outer(B, v)
            B[(0,)*K] += a
            assert np.isclose(np.linalg.norm(B-B0), b*ratio, rtol=1e-9)
        # Matrix weak-component path has the second-order sharp coefficient.
        s2_matrix = np.expm1(np.log1p(1e-8)/2)
        assert abs((s2_matrix/1e-8)/.5-1) < 1e-7
    # Check compression target and variance identities with imperfect anchors.
    dims = (4,5,6)
    w, v, h, U = [], [], [], []
    for d in dims:
        wj = np.eye(d)[:, -1]
        vj = rng.normal(size=d); vj[-1] = 0.; vj /= np.linalg.norm(vj)
        hj = vj+.2*rng.normal(size=d); hj[-1] = 0.; hj /= np.linalg.norm(hj)
        w.append(wj); v.append(vj); h.append(hj); U.append(np.column_stack((hj,wj)))
    def kron_all(seq):
        value = seq[0]
        for other in seq[1:]:
            value = np.kron(value, other)
        return value
    projection_basis = kron_all(U)
    A, B = kron_all(w), 3*kron_all(v)
    projected_B = projection_basis @ (projection_basis.T @ B)
    corr2 = np.prod([np.dot(vj,hj)**2 for vj,hj in zip(v,h)])
    assert np.allclose(projection_basis.T @ projection_basis, np.eye(8))
    assert np.allclose(projection_basis @ (projection_basis.T @ A), A)
    assert np.isclose(np.linalg.norm(B-projected_B)**2, 9*(1-corr2))
    result = dict(seed=20260908, random_TT_checks=checks,
                  max_cross_identity_absolute_error=max_cross_error,
                  max_sharp_witness_relative_error=max(witness_errors),
                  cubic_NP_lower=lower, cubic_lower_quadrature=integral,
                  cubic_projection_upper=upper, compression_identities=True,
                  interpretation="Algebraic checks, not proof or coverage Monte Carlo validation.")
    dest = Path(__file__).resolve().parents[1]/'notes'/'strengthening_checks.json'
    dest.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
