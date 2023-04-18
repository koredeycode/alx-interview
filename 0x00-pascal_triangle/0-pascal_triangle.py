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
    ret = [[1]]
    if n >= 2:
        ret.append([1, 1])
    for i in range(n - 2):
        tmp = ret[-1]
        add = [1]
        i = 0
        ln = len(tmp) - 1
        while i < ln:
            a = tmp[i]
            b = tmp[i + 1]
            add.append(a + b)
            i += 1
        add.append(1)
        ret.append(add)
    return ret
