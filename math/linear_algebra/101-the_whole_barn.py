#!/usr/bin/env python3
"""
101-the_whole_barn.py

Function to add two matrices of any dimension.

If the shapes differ, returns None.
"""


def add_matrices(mat1, mat2):
    """
    Adds two matrices element-wise and returns a new matrix.

    Args:
        mat1 (list): First matrix (nested lists of ints/floats).
        mat2 (list): Second matrix (nested lists of ints/floats).

    Returns:
        list or None: New matrix after addition or None if shapes mismatch.
    """
    # Check if both are lists
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        # Base case: mat1 and mat2 are numbers, add them directly
        if isinstance(mat1, (int, float)) and isinstance(mat2, (int, float)):
            return mat1 + mat2
        # Types don't match, shape mismatch
        return None

    # If lengths differ, shapes mismatch
    if len(mat1) != len(mat2):
        return None

    # Recursive addition for each element
    result = []
    for a, b in zip(mat1, mat2):
        summed = add_matrices(a, b)
        if summed is None:  # Shape mismatch detected deeper
            return None
        result.append(summed)

    return result
