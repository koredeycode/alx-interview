#!/usr/bin/python3
"""
the island perimeter module
"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    calculate the perimeter of an island
    """
    perimeter = 0
    grid_len = len(grid)
    for i in range(grid_len):
        row_len = len(grid[i])
        for j in range(row_len):
            if grid[i][j] != 1:
                continue
            # check up
            if i == 0 or grid[i - 1][j] == 0:
                perimeter += 1
            # check down
            if i + 1 == grid_len or grid[i + 1][j] == 0:
                perimeter += 1
            # check left
            if j == 0 or grid[i][j - 1] == 0:
                perimeter += 1
            # check right
            if j + 1 == row_len or grid[i][j + 1] == 0:
                perimeter += 1
    return perimeter
