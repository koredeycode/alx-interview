#!/usr/bin/python3
"""
the 0-nqueen module containing the solution
"""
import sys

solutions = []


def print_board(board, n):
    """
    print a chess board
    """
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" | ")
        print()
    print("=" * (n + 3))


def is_safe(row, col, board, n):
    """
    check if a position on the board is safe for the queen to stay
    """
    x = row
    y = col

    while x >= 0:
        if board[x][y]:
            return False
        x -= 1

    x = row
    y = col

    while y < n and x >= 0:
        if board[x][y]:
            return False
        y += 1
        x -= 1

    x = row
    y = col
    while y >= 0 and x >= 0:
        if board[x][y]:
            return False
        x -= 1
        y -= 1
    return True


def findPositions(board, n):
    """
    find the position of the queens from a valid board
    """
    ret = []
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                ret.append([i, j])
    return ret


def solveNQueens(row, board, n):
    """
    recursive function that solve the nqueen function
    """
    if row == n:
        solutions.append(findPositions(board, n))
        return
    for col in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = 1
            solveNQueens(row + 1, board, n)
            board[row][col] = 0


def main(args) -> None:
    """
    the program's main function
    """
    if len(args) != 2:
        print("Usage: nqueens N")
        return
    num: str = args[1]
    if not num.isnumeric():
        print("N must be a number")
        return
    num = int(num)
    if num < 4:
        print("N must be at least 4")
        return
    n = num
    board = [[0 for i in range(n)] for j in range(n)]
    solveNQueens(0, board, n)
    [print(sol) for sol in solutions]


if __name__ == "__main__":
    main(sys.argv)
