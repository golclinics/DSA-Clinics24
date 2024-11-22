"""
Write a program that takes an integer as input and returns true if the input is a power of two.
"""

def is_a_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1

# Example test case
test_number = int(input("Enter a number: "))
result = is_a_power_of_two(test_number)
print(result)