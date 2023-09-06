#!/usr/bin/python3
"""
Module for the prime game
"""


def isPrime(x: int) -> bool:
    """return if a number is a prime number

    Args:
        x (int): the number to be checked

    Returns:
        bool: the result
    """
    if x == 0 or x == 1:
        return False
    ret = True
    for n in range(2, x // 2):
        if x % n == 0:
            ret = False
            break
    return ret


def whoWon(n: int) -> int:
    """check who won for a number

    Args:
        n (int): number

    Returns:
        int: who won
    """
    currentWinner = 1
    for i in range(n):
        if isPrime(i):
            currentWinner = 0 if currentWinner == 1 else 1
    return currentWinner


def isWinner(x: int, nums: list[int]) -> str:
    """determines the winner of the rounds

    Args:
        x (int): number of rounds
        nums (List[int]): an arrray of number

    Returns:
        str: The winner
    """
    count = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = whoWon(n)
        if winner == 0:
            count['Maria'] += 1
        else:
            count['Ben'] += 1
    if count['Maria'] > count['Ben']:
        return 'Maria'
    else:
        return 'Ben'
