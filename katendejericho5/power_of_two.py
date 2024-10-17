def is_power_of_two(n):
    # Returns True if n is positive and has only one bit set in its binary representation
    return n > 0 and (n & (n - 1)) == 0

# Get user input
number = int(input("Enter an integer: "))

# Check if the number is a power of two and print the result
if is_power_of_two(number):
    print("true")  # Returns true for powers of two
else:
    print("false")  # Returns false for non-powers of two

print("\n")
print("Running ---Test cases")
# test cases
print(is_power_of_two(1))  # True
print(is_power_of_two(2))  # True
print(is_power_of_two(3))  # False
print(is_power_of_two(4))  # True
print(is_power_of_two(8)) # True
print(is_power_of_two(6)) # False
