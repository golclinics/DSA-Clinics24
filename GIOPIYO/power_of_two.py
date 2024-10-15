# Write a program that takes an integer as input and returns true if the input is a power of two.

def power_2(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

number = int(input("Enter any integer: ")) 
result = power_2(number) 
print(result) 