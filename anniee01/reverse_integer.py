"""Reverse Integer
Write a program that takes an integer as input and return an integer with reversed digit
ordering.

For example

For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
"""

def reverse_integer(n):
    """This function takes an integer as input and returns reversed digit"""
    str_n = str(abs(n))
    reversed_n = int(str_n[::-1])

    if n < 0:
        return -reversed_n
    else:
        return reversed_n

