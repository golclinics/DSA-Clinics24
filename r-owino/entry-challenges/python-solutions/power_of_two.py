#!/usr/bin/env python3
"""Checks if an integer is a power of 2"""

def powerOfTwo(n: int) -> bool:
    """
    Checks if an input integer is a power of 2

    Parameters
    ----------
    n: int
        the number to check if a power of 2
    
    Returns
    -------
    bool
        True if n is a power of 2, False otherwise
    """
    x = 1
    while x < n:
        x *= 2
    return x == n

print(powerOfTwo(64))
