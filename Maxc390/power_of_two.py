def check_power(number):
    if number <= 0:
        return "Number is less than or equal to zero, not a power of 2"
    
    # Check if the number is odd (and greater than 1)
    if number % 2 == 1:
        return "Number is odd, not a power of 2"
    
    # Continuously divide the number by 2 if it's even
    while number > 1:
        if number % 2 != 0:
            return "Not a power of 2"
        number //= 2  # Integer division by 2
    
    return "It is a power of 2"

# Test cases
print(check_power(6))  # Expected: Not a power of 2
print(check_power(8))  # Expected: It is a power of 2
print(check_power(0))  # Expected: Number is less than or equal to zero, not a power of 2
print(check_power(1))  # Expected: It is a power of 2
