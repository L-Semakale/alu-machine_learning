#!/usr/bin/env python3
"""
Module that contains a function to concatenate two matrices
along a specified axis.
"""


def shape(mat):
    """Return the shape of a nested list (matrix)."""
    if not isinstance(mat, list):
        return ()
    if len(mat) == 0:
        return (0,)
    return (len(mat),) + shape(mat[0])


def check_shapes_compatible(shape1, shape2, axis):
    """Check if two shapes are compatible for concatenation along
    axis."""
    if len(shape1) != len(shape2):
        return False
    for i in range(len(shape1)):
        if i == axis:
            continue
        if shape1[i] != shape2[i]:
            return False
    return True


def concat_axis(mat1, mat2, axis):
    """Concatenate two matrices along the given axis recursively."""
    if axis == 0:
        # Concatenate top level lists
        return mat1 + mat2
    else:
        # axis > 0, recurse into sublists
        if len(mat1) != len(mat2):
            # shapes don't match along other dimensions, fail
            return None
        result = []
        for i in range(len(mat1)):
            concatenated = concat_axis(mat1[i], mat2[i], axis - 1)
            if concatenated is None:
                return None
            result.append(concatenated)
        return result


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenate two matrices along a specific axis.
    Return new matrix or None if shapes incompatible.
    """
    shape1 = shape(mat1)
    shape2 = shape(mat2)

    if not check_shapes_compatible(shape1, shape2, axis):
        return None
    return concat_axis(mat1, mat2, axis)
