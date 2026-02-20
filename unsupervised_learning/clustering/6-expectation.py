#!/usr/bin/env python3
"""
This module contains a function that calculates
the expectation step in the EM algorithm for a GMM
"""
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """
    Calculates the expectation step in the EM algorithm for a GMM

    Args:
        X: numpy.ndarray (n, d) containing the dataset
            - n: number of data points
            - d: number of dimensions for each data point
        pi: numpy.ndarray (k,) containing the priors for each cluster
        m: numpy.ndarray (k, d) containing centroid means for each cluster
        S: numpy.ndarray (k, d, d) containing covariance matrices
           for each cluster

    Returns:
        g: numpy.ndarray (k, n) containing the posterior probabilities
           for each data point in each cluster
        l: the total log likelihood
        (None, None) on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(pi, np.ndarray) or len(pi.shape) != 1:
        return None, None
    if not isinstance(m, np.ndarray) or len(m.shape) != 2:
        return None, None
    if not isinstance(S, np.ndarray) or len(S.shape) != 3:
        return None, None

    n, d = X.shape
    k = pi.shape[0]

    if m.shape != (k, d):
        return None, None
    if S.shape != (k, d, d):
        return None, None
    if not np.isclose(np.sum(pi), 1):
        return None, None

    # Calculate weighted likelihoods: pi[i] * P(X | cluster i)
    likelihoods = np.zeros((k, n))
    
    for i in range(k):
        P = pdf(X, m[i], S[i])
        if P is None:
            return None, None
        likelihoods[i] = pi[i] * P

    # Marginal likelihood P(X)
    marginal = np.sum(likelihoods, axis=0)

    # Posterior probabilities (responsibilities)
    g = likelihoods / marginal

    # Total log likelihood
    l = np.sum(np.log(marginal))

    return g, l