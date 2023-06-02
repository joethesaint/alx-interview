#!/usr/bin/python3
"""
Making change 0(n)
"""


def makeChange(coins, total):
    """
    Classic Bottom-Up dynamic program
    """
    temp_val = 0  # temporary value
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_val += total // coin
            total = total % coin

    return temp_val if total == 0 else -1
