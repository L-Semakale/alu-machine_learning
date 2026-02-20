#!/usr/bin/env python3
"""
This module contains a function that
tests for the optimum number of clusters by variance
"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    Tests for the optimum number of clusters by variance

    Args:
        X: numpy.ndarray (n, d) containing the dataset
            - n: number of data points
            - d: number of dimensions for each data point
        kmin: positive integer - the minimum number of clusters
        kmax: positive integer - the maximum number of clusters
        iterations: positive integer - max number of iterations

    Returns:
        results: list containing the outputs of K-means for each cluster size
        d_vars: list containing the difference in variance from the
                smallest cluster size for each cluster size
        (None, None) on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(kmin, int) or kmin <= 0:
        return None, None
    if kmax is not None and (not isinstance(kmax, int) or kmax <= 0):
        return None, None
    if kmax is not None and kmin >= kmax:
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None

    # Set kmax to n if not provided
    if kmax is None:
        kmax = X.shape[0]

    # Must analyze at least 2 different cluster sizes
    if kmax - kmin < 1:
        return None, None

    results = []
    variances = []

    for k in range(kmin, kmax + 1):
        C, clss = kmeans(X, k, iterations)
        results.append((C, clss))
        var = variance(X, C)
        variances.append(var)

    # Calculate differences from the first (smallest k) variance
    first_var = variances[0]
    d_vars = [first_var - v for v in variances]

    return results, d_vars