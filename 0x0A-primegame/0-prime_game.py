#!/usr/bin/python3
"""
Module for the prime game contains the isWinner function
The script determines the winner between Maria and Ben and None if there is tie
"""


def isWinner(x: int, nums: list[int]) -> str:
    """determines the winner of the rounds

    Args:
        x (int): number of rounds
        nums (List[int]): an arrray of number

    Returns:
        str: The winner
    """
    def is_prime(x): return False if x in (0, 1) else all(x %
                                                          i != 0 for i in range(2, int(x ** 0.5) + 1))

    def who_won(n): return 1 if sum(
        1 for i in range(n) if is_prime(i)) % 2 == 0 else 0

    count = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = who_won(n)
        if winner == 0:
            count['Maria'] += 1
        else:
            count['Ben'] += 1
    if count['Maria'] > count['Ben']:
        return 'Maria'
    elif count['Maria'] < count['Ben']:
        return 'Ben'
    return None
