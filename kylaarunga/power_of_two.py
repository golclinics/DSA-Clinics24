def is_power_of_two(n):
    
    # dealing with Edge cases: Any number less than or equal to 0 cannot be a power of two
    if n <= 0:
        return False

    # A number is a power of two if it has only one bit set to 1 in its binary representation
    # Using the bit manipulation trick: n & (n - 1) == 0
    return (n & (n - 1)) == 0

# Prompt the user for input
try:
    user_input = int(input("Enter an integer: "))  # Ask the user for an integer input
    result = is_power_of_two(user_input)            # Check if the input is a power of two
    print(f"{user_input} => {result}")               # Print the result
except ValueError:
    print("Please enter a valid integer.")           # Handle invalid inputs
