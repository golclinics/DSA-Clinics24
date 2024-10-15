#!/usr/bin/python3

def reverse_integer(num):
    """
    Function that takes an integer as input and return/prints  an integer with reversed digit ordering.
    """
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num // 10
    return reverse

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    t = "The reverse is "
    print(f"{t}{reverse_integer(abs(n)) * -1}") if n < 0 else print(f"{t}{reverse_integer(n)}")
