#!/usr/bin/env python3
"""
This module contains a function that
initializes variables for a Gaussian Mixture Model
"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """
    Initializes variables for a Gaussian Mixture Model

    Args:
        X: numpy.ndarray (n, d) containing the dataset
            - n: number of data points
            - d: number of dimensions for each data point
        k: positive integer - the number of clusters

    Returns:
        pi: numpy.ndarray (k,) containing priors for each cluster,
            initialized to be equal
        m: numpy.ndarray (k, d) containing centroid means for each cluster,
           initialized with K-means
        S: numpy.ndarray (k, d, d) containing covariance matrices for
           each cluster, initialized as identity matrices
        (None, None, None) on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    if not isinstance(k, int) or k <= 0:
        return None, None, None

    n, d = X.shape

    if k > n:
        return None, None, None

    # Initialize priors equally
    pi = np.full((k,), 1 / k)

    # Initialize means using K-means
    m, _ = kmeans(X, k)

    # Initialize covariance matrices as identity matrices
    S = np.tile(np.identity(d), (k, 1, 1))

    return pi, m, S