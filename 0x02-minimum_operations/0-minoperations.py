#!/usr/bin/python3
"""
2. Minimum Operations
"""


def minOperations(x):  # x is the number
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file
        Returns:
            Integer: if n is impossible to acheive,
            return 0
    """
    res = 0  # result
    idx = 2  # index
    if x < 2:
        return 0
    while (idx < x + 1):
        # check to see if the problem can be broken into smaller problems
        while x % idx == 0:
            # if yes, then add no of smaller problems to result
            res += idx
            # break into smaller pieces
            x /= idx
        idx += 1
    return res

    # paste_chars = 1  # how many characters are in the file
    # clipboard = 0  # how many H's are copied
    # count_ops = 0  # counts the number of operations

    # while paste_chars < n:
    #     # to check if clipboard is empty and yet to copy anything
    #     if clipboard == 0:
    #         # then copy all
    #         clipboard = paste_chars
    #         # increment the number of operations
    #         count_ops += 1

    #     # to check if the paste_chars is yet to paste anything
    #     if paste_chars == 1:
    #         # paste
    #         paste_chars += clipboard
    #         # increment the number of operations
    #         count_ops += 1
    #         # continue to the next loop
    #         continue

    #     remainder = n - paste_chars  # to get the remaining chars to paste
    #     # check if impossible by checking if clipboard
    #     # has more than needed to reach the number desired
    #     # which also means num of chars in file is equal
    #     # or more than in the clipboard.
    #     # in both situations, it's impossible to achieve n of chars
    #     if remainder < clipboard:
    #         return 0
    #     # if it can't be divided
    #     if remainder % paste_chars != 0:
    #         # paste the current clipboard
    #         paste_chars += clipboard
    #         # increment count_ops
    #         count_ops += 1
    #     else:
    #         # copyall
    #         clipboard = paste_chars
    #         # paste
    #         paste_chars += clipboard
    #         # increment count_ops
    #         count_ops += 2

    #     # if got the desired result
    #     if paste_chars == n:
    #         return count_ops
    #     else:
    #         return 0
