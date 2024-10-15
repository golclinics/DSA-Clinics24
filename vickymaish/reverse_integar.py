import math

class Solution:
    def reverse(self, x: int) -> int:
        # declare min and max values for 32-bit integers
        MIN = -2147483648  # corrected the min value to -2147483648
        MAX = 2147483647   # corrected the max value to 2147483647
        # initialize result with zero
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if (res > MAX // 10 or
                (res == MAX // 10 and digit >= MAX % 10)):
                return 0
        
            if (res < MIN // 10 or
                (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit
        return res

# Testing the code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_value = 123
    print(f"Reversed {test_value}: {solution.reverse(test_value)}")  # Expected output: 321
    
    test_value = -500
    print(f"Reversed {test_value}: {solution.reverse(test_value)}")  # Expected output: -321
    
    test_value = 1534236469
    print(f"Reversed {test_value}: {solution.reverse(test_value)}")  # Expected output: 0 (overflow)

