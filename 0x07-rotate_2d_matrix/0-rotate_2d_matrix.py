#!/usr/bin/python3
"""
The rotate 2d matrix module
"""

def transpose(mat: list) -> None:
    """Transpose a matrix inplace

    Args:
        mat (list): a 2 dimensional matrix
    """
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


def revForClockwiseRotation(mat: list) -> None:
    """rotate the transposed matrix clockwisely

    Args:
        mat (list): transposed 2d matrix
    """
    n = len(mat)
    for row in mat:
        left, right = 0, n - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1


def revForAntiClockwiseRotation(mat: list) -> None:
    """rotat the transpose matrix anticlockwisely

    Args:
        mat (list): transpose 2d matrix
    """
    n = len(mat)
    for i in range(n // 2):
        mat[i], mat[n - i - 1] = mat[n - i - 1], mat[i]


def rotate_2d_matrix(mat: list) -> None:
    transpose(mat)
    revForClockwiseRotation(mat)