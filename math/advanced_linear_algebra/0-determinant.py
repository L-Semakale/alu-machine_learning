#!/usr/bin/env python3
"""Module to calculate the determinant of a matrix."""


def determinant(matrix):
    """Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): The matrix to calculate the determinant of.

    Returns:
        int or float: The determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square.
    """
    # Validate that it's a list of lists
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a list of lists")

    # Check for 0x0 matrix (special case: [[]])
    if matrix == [[]]:
        return 1

    n = len(matrix)

    # Matrix must be square
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for n > 2
    det = 0
    for col in range(n):
        # Create submatrix (minor)
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(submatrix)

    return det
