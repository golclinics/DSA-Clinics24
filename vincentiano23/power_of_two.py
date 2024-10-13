
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(8))  # Expected output: True
print(is_power_of_two(6))  # Expected output: False







