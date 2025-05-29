#!/usr/bin/env python3
"""Module to calculate the minor matrix of a given matrix."""


def determinant(matrix):
    """Helper function to calculate the determinant of a square matrix.

    Args:
        matrix (list of lists): The square matrix.

    Returns:
        int or float: The determinant value.
    """
    # Special case: 0x0 matrix
    if matrix == [[]]:
        return 1

    n = len(matrix)

    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if n == 2:
        return (matrix[0][0] * matrix[1][1]
                - matrix[0][1] * matrix[1][0])

    # Recursive case: Use Laplace expansion along the first row
    det = 0
    for col in range(n):
        # Build the submatrix (minor) by removing first row and col-th column
        sub = [row[:col] + row[col + 1:] for row in matrix[1:]]
        # Alternate signs and recurse
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)

    return det


def minor(matrix):
    """Calculates the minor matrix of a given matrix.

    Args:
        matrix (list of lists): The matrix to compute the minor of.

    Returns:
        list of lists: The minor matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    # Validate the input is a list of lists
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    # Ensure matrix is non-empty and square
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    # Special case: 1x1 matrix → Minor is [[1]]
    if n == 1:
        return [[1]]

    minors = []
    # Loop through each element to calculate its minor
    for i in range(n):
        row_minors = []
        for j in range(n):
            # Build submatrix by excluding current row (i) and column (j)
            sub = [
                row[:j] + row[j + 1:]
                for k, row in enumerate(matrix) if k != i
            ]
            # Compute determinant of the submatrix and add it to row
            row_minors.append(determinant(sub))
        # Add the row of minors to the result
        minors.append(row_minors)

    return minors
