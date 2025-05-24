#!/usr/bin/env python3
"""
Module to slice a numpy ndarray along specified axes.
"""


def np_slice(matrix, axes={}):
    """
    Slice a numpy.ndarray along specific axes.

    Parameters
    ----------
    matrix : numpy.ndarray
        The input array to slice.
    axes : dict, optional
        A dictionary where the keys are axes (int), and the values are
        tuples representing slice parameters (start, stop, step) for that axis.
        Defaults to {} (no slicing).

    Returns
    -------
    numpy.ndarray
        A new sliced numpy ndarray according to the specified axes.

    Examples
    --------
    >>> import numpy as np
    >>> mat = np.array([[1, 2, 3], [4, 5, 6]])
    >>> np_slice(mat, axes={1: (1, 3)})
    array([[2, 3],
           [5, 6]])
    """
    slices = []
    for i in range(matrix.ndim):
        if i in axes:
            slices.append(slice(*axes[i]))
        else:
            slices.append(slice(None))
    return matrix[tuple(slices)]
