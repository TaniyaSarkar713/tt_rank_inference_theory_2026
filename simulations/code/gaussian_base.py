"""Gaussian calibration with a certified tensor-envelope remainder.

Vectorization is NumPy C order. All dimensions and blocks preserve mode order.
"""
import numpy as np
from scipy.linalg import null_space
from scipy.stats import chi2, t


def outer(vectors):
    out = np.array(1.0)
    for v in vectors:
        out = np.multiply.outer(out, v)
    return out


def block_dimensions(dims, caps):
    blocks, size = [], dims[0]
    for k, cap in enumerate(caps):
        if cap == 1:
            blocks.append(size)
            size = dims[k+1]
        else:
            size *= dims[k+1]
    return tuple(blocks + [size])


def rank_one_hosvd(tensor, block_dims):
    arr = tensor.reshape(block_dims)
    vectors = []
    for j in range(len(block_dims)):
        unfold = np.moveaxis(arr, j, 0).reshape(block_dims[j], -1)
        vectors.append(np.linalg.svd(unfold, full_matrices=False)[0][:, 0])
    direction = outer(vectors)
    coefficient = float(np.sum(arr * direction))
    return (coefficient * direction).ravel(), vectors, coefficient


def tangent_basis(vectors):
    columns = [outer(vectors).ravel()]
    for j, v in enumerate(vectors):
        for u in null_space(v.reshape(1, -1)).T:
            changed = list(vectors)
            changed[j] = u
            columns.append(outer(changed).ravel())
    return np.column_stack(columns)


def tangent_score(a, basis, covariance):
    return basis @ np.linalg.solve(basis.T @ covariance @ basis, basis.T @ a)


def localization_radius(ols, pilot, gram, sigma, gamma):
    p = ols.size
    bound = sigma * np.sqrt(chi2.ppf(1-gamma, p) / np.linalg.eigvalsh(gram)[0])
    return float(np.linalg.norm(ols-pilot) + bound)


def curvature_remainder(a, score, covariance, radius, pilot_norm, blocks):
    if blocks == 1:
        return 0.0
    if pilot_norm <= 1e-14:
        return np.inf
    return float(np.linalg.norm(a-covariance@score) * radius**2 / (np.sqrt(2)*pilot_norm))


def score_interval(a, pilot, score, covariance, gram, xty, yty, m, alpha, remainder=0.0):
    """Inputs gram=X'X, xty=X'Y, yty=Y'Y on independent calibration data."""
    q = float(score @ covariance @ score)
    center_pilot = float(a @ pilot)
    if q <= 0.0:
        return center_pilot, float(remainder)
    zr = float(score @ (xty-gram@pilot) / np.sqrt(q))
    zz = float(score @ gram @ score / q)
    rr = float(yty - 2*pilot@xty + pilot@gram@pilot)
    slope = zr / zz
    variance = max(0.0, (rr-zr*zr/zz) / (m-1))
    center = center_pilot + np.sqrt(q)*slope
    half = t.ppf(1-alpha/2, m-1)*np.sqrt(q*variance/zz) + remainder
    return float(center), float(half)


def certified_score(a, pilot, vectors, covariance, radius, sigma, m, alpha, gamma):
    U = tangent_basis(vectors)
    w = tangent_score(a, U, covariance)
    R = curvature_remainder(a, w, covariance, radius, np.linalg.norm(pilot), len(vectors))
    ambient = np.linalg.solve(covariance, a)
    envelope_sd = np.sqrt(sigma*sigma + np.linalg.eigvalsh(covariance)[-1]*radius*radius)
    critical = t.ppf(1-(alpha-gamma)/2, m-1)
    proxy_tangent = critical*envelope_sd*np.sqrt(max(0,w@covariance@w)/m)+R
    proxy_ambient = critical*envelope_sd*np.sqrt(ambient@covariance@ambient/m)
    if proxy_tangent < proxy_ambient:
        return w, R, True
    return ambient, 0.0, False


def inversion_outer_interval(a, ols, gram, sigma, alpha, block_dims):
    """Computable outer bound to inversion of an OLS confidence ball.

    This does not claim to solve nonconvex endpoint optimization exactly.
    Its coverage is simultaneous for all loadings on the localization event.
    """
    pilot, vectors, _ = rank_one_hosvd(ols, block_dims)
    rho = localization_radius(ols, pilot, gram, sigma, alpha)
    U = tangent_basis(vectors)
    pa = U @ (U.T @ a)
    ambient = np.linalg.norm(a)*rho
    if np.linalg.norm(pilot) <= 1e-14:
        half = ambient
    else:
        remainder = np.linalg.norm(a-pa)*rho*rho/(np.sqrt(2)*np.linalg.norm(pilot))
        half = min(ambient, np.linalg.norm(pa)*rho+remainder)
    return float(a@pilot), float(half)


def gaussian_sufficient_statistics(rng, n, beta, covariance, sigma):
    """Exact Gaussian-design sufficient-statistic sampler, using Bartlett's law.

    Requires n>=p. It is distributionally identical to forming X'X, X'Y,
    Y'Y from n independent N(0,covariance) rows and Gaussian errors.
    """
    p = beta.size
    if n < p:
        raise ValueError('The Bartlett sampler requires n >= p.')
    bartlett = np.tril(rng.normal(size=(p,p)), -1)
    np.fill_diagonal(bartlett, np.sqrt(rng.chisquare(n-np.arange(p))))
    L = np.linalg.cholesky(covariance) @ bartlett
    gram = L @ L.T
    z = rng.normal(size=p)
    g = sigma * L @ z
    noise_ss = sigma*sigma * (z@z + (rng.chisquare(n-p) if n>p else 0.0))
    xty = gram@beta + g
    yty = beta@gram@beta + 2*beta@g + noise_ss
    ols = beta + sigma*np.linalg.solve(L.T,z)
    return gram, xty, float(yty), ols


def order_projections(a, vectors):
    """Orthogonal tensor components with exactly ell perpendicular factors."""
    J=len(vectors)
    parts=[np.zeros_like(a,dtype=float) for _ in range(J+1)]
    lines=[np.outer(v,v) for v in vectors]
    for mask in range(1<<J):
        matrix=np.ones((1,1))
        for j,Q in enumerate(lines):
            matrix=np.kron(matrix,np.eye(Q.shape[0])-Q if mask & (1<<j) else Q)
        parts[mask.bit_count()]+=matrix@a
    return parts


def graded_inversion_interval(a, ols, gram, sigma, alpha, block_dims=(2,4,2)):
    """Honest outer inversion retaining second- and third-order components."""
    if len(block_dims)!=3:
        raise ValueError('This implementation uses exactly three tensor blocks.')
    pilot,vectors,_=rank_one_hosvd(ols,block_dims)
    rho=localization_radius(ols,pilot,gram,sigma,alpha)
    shat=np.linalg.norm(pilot)
    ambient=np.linalg.norm(a)*rho
    if shat<=0 or rho>=shat/2:
        half=ambient
    else:
        parts=order_projections(a,vectors)
        graded=(np.linalg.norm(parts[0]+parts[1])*rho+
                np.sqrt(3)*np.linalg.norm(parts[2])*rho*rho/(shat-rho)+
                np.linalg.norm(parts[3])*rho**3/(shat-rho)**2)
        half=min(ambient,graded)
    return float(a@pilot),float(half)
