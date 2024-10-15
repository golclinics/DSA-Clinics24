#!/usr/bin/python3

def power_of_two(n):
    """
        program that takes an integer as input
        returns true if the input is a power of two else false.
    """
    return False if n <= 0 else (n & (n - 1) ) == 0


if __name__ == "__main__":
    print(power_of_two(int(input("Enter Number: "))))
    