def is_power_of_two(n):
    # Check if n is a positive integer
    if n <= 0 or not isinstance(n, int):
        return False
    
    # Use bitwise AND operation to check if n is a power of two
    return (n & (n - 1)) == 0

# Test cases
test_cases = [8, 6, 1, 16, 3, 32, 0, -4]

for num in test_cases:
    result = is_power_of_two(num)
    print(f"{num} => returns {result}")