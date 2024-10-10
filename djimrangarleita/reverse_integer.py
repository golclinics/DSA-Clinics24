"""
Entry Challenge C1
Reverse Integer
Write a program that takes an integer as input and return an
integer with reversed digit ordering.

For example

For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
"""


def reverse_integer(num: int) -> int:
    """Reverse an integer given as input

    Args:
        num (int): Input, integer to reverse

    Returns:
        int: Reversed value of num
    """
    reversed_acc, sign = 0, 1
    if num < 0:
        num = abs(num)
        sign = -1

    while num > 0:
        reversed_acc *= 10
        reversed_acc += (num % 10)
        num //= 10

    return reversed_acc * sign
