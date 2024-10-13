def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(8))  
print(is_power_of_two(6))  