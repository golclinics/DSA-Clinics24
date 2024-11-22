def is_power_of_two(n):
    """
    Checks if the given integer is a power of two.
    
    Args:
    n (int): The input integer.

    """
    if n <= 0:
        return False
    
    return (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(8))   # Should print: True
print(is_power_of_two(6))   # Should print: False
print(is_power_of_two(64)) # Should print: True
print(is_power_of_two(10)) # Should print: False
print(is_power_of_two(0))  # Should print: False