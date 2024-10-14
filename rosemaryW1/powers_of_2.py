# The function checks if a number is a power of two.
# Logic: A number is a power of two if it has exactly one '1' bit in its binary representation.
# This is checked using the expression (n & (n - 1)) == 0. This expression works because:
# For powers of two, the binary representation has exactly one bit set to '1' (e.g., 1 -> 0001, 2 -> 0010, 4 -> 0100).
# The operation (n & (n - 1)) removes the lowest set bit. If the result is 0, then there was exactly one bit set.
# For numbers that are not powers of two, the result will not be zero.
# Edge cases considered: Zero and negative numbers are not powers of two.


def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Test cases - You can modify these numbers to test different cases
def run_tests():
    test_cases = [1, 2, 3, 4, 5, 8, 16, 18, 32, 0, -1]
    
    print("Testing powers of two:")
    for num in test_cases:
        result = is_power_of_two(num)
        print(f"Input: {num} -> Output: {result}")

# Run the tests
if __name__ == "__main__":
    run_tests()
    

# Expected outcome
# Testing powers of two:
# Input: 1 -> Output: True
# Input: 2 -> Output: True
# Input: 3 -> Output: False
# Input: 4 -> Output: True
# Input: 5 -> Output: False
# Input: 8 -> Output: True
# Input: 16 -> Output: True
# Input: 18 -> Output: False
# Input: 32 -> Output: True
# Input: 0 -> Output: False
# Input: -1 -> Output: False