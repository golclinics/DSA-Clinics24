#!/usr/bin/env python3

"""
Reverses the digits of an integer.
"""


def reverse_integer(num: int) -> int:
    """
    Args:
        num (int): The integer to reverse. This can be positive or negative.

    Returns:
        int: The integer formed by reversing the digits of the input.
    """

    is_negative = num < 0

    num = abs(num)

    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10

    if is_negative:
        reversed_num = -reversed_num

    return reversed_num
