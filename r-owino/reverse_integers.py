#!/usr/bin/env python3
"""Takes an integer input and returns its reverse"""

def reverse(x: int) -> int:
    """
    Reverses an integer

    Parameters
    ----------
    x: int
        the integer to reverse

    Returns
    -------
    int
        the reversed integer
    """
    try:
        if not isinstance(x, int):
            raise TypeError("Input must be an integer")

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            remainder = x % 10
            res = res * 10 + remainder
            x //= 10

        res *= sign

        return res

    except Exception as e:
        print(f"Error occurred: {e}")

print(reverse(45.6))
