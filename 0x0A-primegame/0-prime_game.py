#!/usr/bin/python3
"""
the prime_game module
"""


def is_prime(x):
    """Check if a number is prime."""
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner of a prime game session with `x` rounds."""
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_num = max(nums)
    primes = [is_prime(i) for i in range(max_num + 1)]

    for n in nums[:x]:
        prime_count = sum(primes[:n])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
