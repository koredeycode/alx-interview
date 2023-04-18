#!/usr/bin/python3
"""This module contain the pascal_triangle function"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle
    of n.

    Args:
        n (int): An integer representing the number of rows in the Pascal's
        triangle to generate.

    Returns:
        list: A list of lists of integers representing the Pascal's
        triangle of n.

    Raises:
        None.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    result = pascal_triangle(n - 1)
    last = result[-1]
    new = [1] + [last[i] + last[i + 1] for i in range(len(last) - 1)] + [1]
    result.append(new)
    return result
