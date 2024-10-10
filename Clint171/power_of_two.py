# Function to take an integer and return True if it is a power of two, False if it is not.

def power_of_two(n):
    # Logic: If n is 0, it is not a power of two. If n is 1, it is a power of two. If n is even, divide by 2 until n is odd. If n is odd, it is not a power of two.
    if n == 0:
        return False
    while n % 2 == 0:
        n = n / 2
    if n == 1:
        return True
    else:
        return False

# Test cases
print(power_of_two(0)) # False
print(power_of_two(1)) # True
print(power_of_two(2)) # True
print(power_of_two(3)) # False
print(power_of_two(4)) # True
print(power_of_two(5)) # False
print(power_of_two(6)) # False
print(power_of_two(7)) # False
print(power_of_two(8)) # True
print(power_of_two(9)) # False
print(power_of_two(10)) # False