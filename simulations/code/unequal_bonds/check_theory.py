"""Falsification checks for U1--U4 and V3; not a coverage simulation study."""
import hashlib
import json
from pathlib import Path
import platform
import sys

import numpy as np
import scipy

from methods import coordinate_maps, fit_interval, intervals

ROOT = Path(__file__).resolve().parents[3]


def contract(cores):
    tensor = cores[0]
    for core in cores[1:]:
        tensor = np.tensordot(tensor, core, axes=(-1, 0))
    return tensor.squeeze(axis=(0, -1))


def canonicalize(cores):
    cores = [x.copy() for x in cores]
    for j in range(len(cores) - 1):
        left, physical, right = cores[j].shape
        q, factor = np.linalg.qr(cores[j].reshape(left * physical, right), mode="reduced")
        cores[j] = q.reshape(left, physical, right)
        cores[j + 1] = np.tensordot(factor, cores[j + 1], axes=(1, 0))
    return cores


def spectral_data(cores):
    betas, vectors, inverses = [], [], []
    for j in range(len(cores) - 1):
        right = cores[j + 1]
        for core in cores[j + 2:]:
            right = np.tensordot(right, core, axes=(-1, 0))
        right = right.reshape(right.shape[0], -1)
        u, s, _ = np.linalg.svd(right, full_matrices=False)
        betas.append(s[-1])
        vectors.append(u[:, -1])
        inverses.append((u / s) @ u.T)
    return np.array(betas), vectors, inverses


def scale(t, betas):
    factors = [1.0 if beta == 0 else min(1.0, t / beta) for beta in betas]
    return t * np.prod(factors)


def grouped_upper(t, betas):
    strong = np.asarray(betas)[np.asarray(betas) >= 2 * t]
    order = len(strong) + 1
    if order == 1:
        return t
    overlap = sum((order - 1 - i) / (beta - t) ** 2 for i, beta in enumerate(strong))
    value = order ** (-order / 2) * (t * t + t ** 4 * overlap) ** (order / 2)
    return min(t, value / np.prod(strong - t))


def weak_family(epsilon):
    tensor = np.zeros((3, 3, 3, 3))
    tensor[0, 0, 0, 0] = tensor[0, 1, 1, 1] = 1
    tensor[1, 0, 0, 0] = epsilon
    return tensor


def weak_gap(epsilon):
    return epsilon * np.sqrt(2 / (2 + epsilon ** 2 + np.sqrt(4 + epsilon ** 4)))


def dense_tt(tensor, profile):
    """Exact-rank TT-SVD for the small dense validation examples."""
    cores = []
    remainder = tensor
    left = 1
    for j, physical in enumerate(tensor.shape[:-1]):
        u, s, vh = np.linalg.svd(remainder.reshape(left * physical, -1), full_matrices=False)
        right = profile[j]
        cores.append(u[:, :right].reshape(left, physical, right))
        remainder = s[:right, None] * vh[:right]
        left = right
    cores.append(remainder.reshape(left, tensor.shape[-1], 1))
    return cores


def ranks(tensor, tol=1e-10):
    return [int(np.linalg.matrix_rank(tensor.reshape(int(np.prod(tensor.shape[:j])), -1), tol=tol))
            for j in range(1, tensor.ndim)]


def main():
    rng = np.random.default_rng(2026091101)
    witnesses = perturbations = references = 0
    max_distance_ratio = 0.0
    max_target_relative_error = 0.0
    sharp_ratios = []
    for dims, profile in [((3, 4, 3), (1, 2, 2, 1)),
                          ((4, 4, 4, 4), (1, 2, 3, 2, 1)),
                          ((4, 4, 4, 4, 4), (1, 2, 3, 3, 2, 1))]:
        order = len(dims)
        for _ in range(10):
            cores = [rng.normal(size=(profile[j], dims[j], profile[j + 1])) for j in range(order)]
            for core in cores:
                core[:, -1, :] = 0
            cores = canonicalize(cores)
            cores[-1] /= np.linalg.norm(contract(cores))
            reference = contract(cores)
            betas, vectors, inverse = spectral_data(cores)
            reference_target = tuple(d - 1 for d in dims)
            z = [vectors[0][None, :]]
            z += [np.outer(vectors[j - 1], vectors[j]) for j in range(1, order - 1)]
            z += [vectors[-1][:, None]]
            directions = [z[j] @ inverse[j] for j in range(order - 1)] + [z[-1]]
            h = np.sqrt(np.expm1(np.log(2) / order))
            for t in [betas.min() * 1e-4, betas.min() * 0.1, betas.min(),
                      betas.max() * 0.3, betas.max() * 2, 10.0]:
                x = h * np.r_[np.minimum(t, betas), t]
                changed = [core.copy() for core in cores]
                for j in range(order):
                    changed[j][:, -1, :] = x[j] * directions[j]
                candidate = contract(changed)
                distance = np.linalg.norm(candidate - reference)
                expected = h ** order * scale(t, betas)
                relative_error = abs(candidate[reference_target] / expected - 1)
                assert distance <= t * (1 + 2e-9)
                assert relative_error < 2e-8, relative_error
                max_distance_ratio = max(max_distance_ratio, distance / t)
                max_target_relative_error = max(max_target_relative_error, relative_error)
                witnesses += 1
            # Independently use equal allocations for the established sharp limit.
            t = betas.min() * 1e-3
            u = t * np.exp(-t * t / (2 * betas.min() ** 2))
            changed = [core.copy() for core in cores]
            for j in range(order):
                changed[j][:, -1, :] = u * directions[j] / np.sqrt(order)
            candidate = contract(changed)
            assert np.linalg.norm(candidate - reference) <= t * (1 + 1e-9)
            sharp = order ** (-order / 2) * t ** order / np.prod(betas)
            sharp_ratios.append(float(candidate[reference_target] / sharp))
            assert abs(sharp_ratios[-1] - 1) < 1e-5
            # Candidates change every physical slice, not just the attaining path.
            for amplitude in np.logspace(-5, 0, 8):
                candidate = contract([core + amplitude * rng.normal(size=core.shape) for core in cores])
                distance = np.linalg.norm(candidate - reference)
                bound = grouped_upper(distance, betas)
                assert abs(candidate[reference_target]) <= bound * (1 + 1e-9) + 1e-14
                constant = 2 ** (order - 1) * max(
                    ((1 + j * (j - 1) / 2) / j) ** (j / 2) for j in range(1, order + 1))
                assert bound <= constant * scale(distance, betas) * (1 + 1e-10)
                perturbations += 1
            references += 1

    singular_checks = 0
    for epsilon in [0, 1e-5, 1e-3, 0.05, 0.5, 1]:
        reference = weak_family(epsilon)
        expected = [weak_gap(epsilon), 1, 1]
        for j in range(1, 4):
            actual = np.linalg.svd(reference.reshape(3 ** j, -1), compute_uv=False)[1]
            assert np.isclose(actual, expected[j - 1], rtol=1e-9, atol=1e-14)
        assert ranks(reference) == ([1, 2, 2] if epsilon == 0 else [2, 2, 2])
        singular_checks += 1

    imbalanced_witnesses = 0
    for epsilon in [1e-6, 1e-4, 1e-2, 0.1, 1]:
        cores = dense_tt(weak_family(epsilon), [2, 2, 2])
        for core in cores:
            core[:, -1, :] = 0  # Remove possible SVD roundoff in an exactly zero slice.
        cores = canonicalize(cores)
        reference = contract(cores)
        assert np.allclose(reference, weak_family(epsilon), rtol=1e-9, atol=1e-14)
        betas, vectors, inverse = spectral_data(cores)
        z = [vectors[0][None, :], np.outer(vectors[0], vectors[1]),
             np.outer(vectors[1], vectors[2]), vectors[2][:, None]]
        directions = [z[j] @ inverse[j] for j in range(3)] + [z[-1]]
        h = np.sqrt(np.expm1(np.log(2) / 4))
        for t in [epsilon * 1e-3, epsilon, np.sqrt(epsilon), 0.1, 1, 10]:
            x = h * np.r_[np.minimum(t, betas), t]
            changed = [core.copy() for core in cores]
            for j in range(4):
                changed[j][:, -1, :] = x[j] * directions[j]
            candidate = contract(changed)
            assert np.linalg.norm(candidate - reference) <= t * (1 + 2e-8)
            assert np.isclose(candidate[2, 2, 2, 2], h ** 4 * scale(t, betas), rtol=2e-8, atol=0)
            imbalanced_witnesses += 1

    boundary_records = []
    e0, e1, e2 = np.eye(3)
    for t in [1e-3, 1e-2, 0.1, 1, 10]:
        u = np.sqrt(np.expm1(np.log1p(t * t) / 3))
        first_block = np.outer(e0, e1) + u * np.outer(e2, e2)
        candidate = np.einsum('i,j,k,l->ijkl', e0, e0, e0, e0)
        candidate += np.einsum('ij,k,l->ijkl', first_block, e1 + u * e2, e1 + u * e2)
        assert max(ranks(candidate)) <= 2
        assert np.isclose(np.linalg.norm(candidate - weak_family(0)), t, rtol=1e-10)
        assert np.isclose(candidate[2, 2, 2, 2], u ** 3, rtol=1e-12)
        ratio = candidate[2, 2, 2, 2] / (t ** 3 / 3 ** 1.5)
        if t == 1e-3:
            assert abs(ratio - 1) < 1e-6
        boundary_records.append({"radius": t, "target": float(u ** 3), "cubic_ratio": float(ratio)})

    coords, pivots, full, grouped, target = coordinate_maps()
    assert len(coords) == 23
    for slices in [full, grouped]:
        assert len(set(np.concatenate(slices))) == sum(len(x) for x in slices)
    identity_checks = inclusion_checks = 0
    for _ in range(150):
        candidate = contract([rng.normal(size=(1, 3, 2)), rng.normal(size=(2, 3, 2)),
                              rng.normal(size=(2, 3, 2)), rng.normal(size=(2, 3, 1))])
        candidate /= np.linalg.norm(candidate)
        theta = np.array([candidate[index] for index in coords])
        for slices, needed in [(full, [0, 1, 2]), (grouped, [1, 2])]:
            product_value = theta[slices[0]].reshape(1, 2)
            for position, pivot in enumerate(needed):
                product_value = product_value @ np.linalg.inv(theta[pivots[pivot]].reshape(2, 2))
                next_slice = theta[slices[position + 1]]
                product_value = product_value @ next_slice.reshape(2, -1)
            assert np.isclose(product_value.item(), theta[target], rtol=2e-6, atol=2e-9)
            identity_checks += 1
        radius = 10 ** rng.uniform(-5, 0)
        delta = rng.normal(size=23)
        delta *= radius * rng.uniform(0, 1) / np.linalg.norm(delta)
        answers, _ = intervals((theta + delta)[None, :], radius)
        for lo, hi in answers.values():
            assert lo[0] - 1e-10 <= theta[target] <= hi[0] + 1e-10
            inclusion_checks += 1

    outcome_checks = 0
    certified_group_only = 0
    for epsilon in [0, 1e-5, 1e-3, 0.1, 1]:
        reference = weak_family(epsilon)
        theta = np.array([reference[index] for index in coords])
        assert sum(reference[index] ** 2 for index in np.ndindex(reference.shape) if index not in set(coords)) == 0
        b = weak_gap(epsilon)
        for magnitude in np.logspace(-6, 1, 15):
            delta = magnitude * rng.normal(size=(12, 23))
            radius = magnitude * rng.uniform(0.1, 3, size=12)
            answers, diagnostics = intervals(theta[None, :] + delta, radius)
            distance = np.linalg.norm(delta, axis=1) + radius
            lo, hi = answers['adaptive_cross']
            length = hi - lo
            bound = np.minimum(2 * distance, 8 * distance ** 3)
            if b > 0:
                bound = np.minimum(bound, 16 * distance ** 4 / b)
            assert np.all(length <= bound * (1 + 1e-9) + 1e-14)
            for name in ['full_cross', 'grouped_cross']:
                other_lo, other_hi = answers[name]
                assert np.all(length <= other_hi - other_lo + 1e-14)
            certified_group_only += int(np.sum(diagnostics['grouped_certified'] & ~diagnostics['full_certified']))
            outcome_checks += len(radius)
    assert certified_group_only > 0

    design = rng.normal(size=(70, 23))
    theta = np.array([weak_family(0.02)[index] for index in coords])
    response = design @ theta + rng.normal(size=70) * 0.2
    fit = fit_interval(design, response)
    assert np.allclose(fit['center'], np.linalg.lstsq(design, response, rcond=None)[0])
    assert fit['radius'] > 0

    source_names = ['theory/unequal_bond_modulus.md', 'theory/unequal_bond_inference.md',
                    'simulations/code/unequal_bonds/methods.py',
                    'simulations/code/unequal_bonds/check_theory.py']
    result = {
        'seed': 2026091101, 'date': '2026-09-11', 'python': platform.python_version(),
        'numpy': np.__version__, 'scipy': scipy.__version__,
        'random_normal_references': references, 'capped_witness_checks': witnesses,
        'general_perturbation_upper_checks': perturbations,
        'maximum_witness_distance_over_radius': float(max_distance_ratio),
        'maximum_witness_target_relative_error': float(max_target_relative_error),
        'sharp_limit_ratio_range': [min(sharp_ratios), max(sharp_ratios)],
        'unequal_family_spectrum_checks': singular_checks, 'boundary_witnesses': boundary_records,
        'strongly_imbalanced_witness_checks': imbalanced_witnesses,
        'selected_coordinate_count': len(coords), 'cross_identity_checks': identity_checks,
        'constructed_ball_inclusion_checks': inclusion_checks,
        'outcome_length_bound_checks': outcome_checks, 'group_only_certified_cases': certified_group_only,
        'regression_wrapper_checked': True,
        'source_sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in source_names},
        'all_checks_passed': True,
        'scope': 'Numerical falsification checks only; no empirical coverage study or formal machine-arithmetic verification.'
    }
    destination = ROOT / 'audit/revision_2026_09_11/checks.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items() if key not in ['source_sha256', 'boundary_witnesses']}, indent=2))


if __name__ == '__main__':
    main()
