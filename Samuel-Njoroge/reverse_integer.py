def reverse_digits(number):
    # Convert the number to a string
    num_str = str(abs(number))
    
    # Reverse the string
    reversed_str = num_str[::-1]
    
    # Convert back to an integer
    reversed_num = int(reversed_str)
    
    # Preserve the original sign
    return reversed_num if number >= 0 else -reversed_num

# Test the function
input_num = int(input("Enter an integer: "))
result = reverse_digits(input_num)
print(f"The number with reversed digits is: {result}")