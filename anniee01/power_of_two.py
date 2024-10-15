"""Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.

Examples:

8=> returns true
6=> returns false
"""

def is_power_of_two(n):
    """Write a program that takes an integer as input and returns true if the input is a power of two.
        Examples:
        8=> returns true
        6=> returns false"""

    if n <= 0:
        return False
    return (n & (n - 1)) == 0
