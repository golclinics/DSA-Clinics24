def is_power_of_two(n):
    # Return False for non-positive numbers
    if n <= 0:
        return False

    # Keep dividing the number by 2
    while n > 1:
        if n % 2 != 0:  # If n is not even, it's not a power of two
            return False
        n //= 2  # Divide n by 2

    return True  # If we reach 1, it is a power of two

# Test cases
print(is_power_of_two(8))   # Output: True
print(is_power_of_two(6))   # Output: False