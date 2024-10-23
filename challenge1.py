def reverse_integer(num):
    reversed_number = 0
    while num > 0:
        last_digit = num % 10  # Get the last digit
        reversed_number = reversed_number * 10 + last_digit  # Add the digit to the reversed number
        num = num // 10  # Remove the last digit from the original number
    return reversed_number

# Input from the user
num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print(f"Reversed integer: {reversed_num}")
