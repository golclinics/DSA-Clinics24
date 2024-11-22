# Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

# Examples:

# 8=> returns true 
# 6=> returns false

def is_power_of_two(num):
    if num <= 0: # Checking for negatives and zero
        return False # it returns 'False'
    
    while num > 1: # Loop as log as num is greater than 1
        if num % 2 != 0: # If 'num' module 2 is not equal to '0', then this is not power of 2
            return False
        num = num // 2 # divide the input num by 2 at each iteration and get it's floor value, and update 'num' 

    return True # Otherwise return True if at each iteration we found 0 when we divide num by 2


# Test cases
print(is_power_of_two(8))  # Output: True
print(is_power_of_two(6))  # Output: False
print(is_power_of_two(16))  # Output: True