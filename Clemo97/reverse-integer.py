def reverse_integer(num):
    # Convert the number to a string and handle the sign
    sign = -1 if num < 0 else 1
    num_str = str(abs(num))
    
    # Reverse the string and convert it back to an integer
    reversed_num = int(num_str[::-1])
    
    # Apply the sign and return the result
    return sign * reversed_num

# Test the function
test_cases = [500, -56, -90, 91]
for case in test_cases:
    result = reverse_integer(case)
    print(f"Input: {case}, Output: {result}")