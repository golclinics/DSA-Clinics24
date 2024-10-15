def reverse_integer(num):
    # Handle negative numbers
    sign = -1 if num < 0 else 1
    num = abs(num)
    
    # Reverse the digits
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    
    # Apply the original sign and return
    return sign * reversed_num

# Test cases
# test_cases = [500, -56, -90, 91]

# for case in test_cases:
#     result = reverse_integer(case)
#     print(f"Input: {case}, Output: {result}")

# Input from the user
num = int(input("Enter an integer: "))
result = reverse_integer(num)
print(f"Reversed integer: {result}")