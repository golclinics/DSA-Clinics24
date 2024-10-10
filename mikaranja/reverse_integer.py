def reverse_number(x):
    # Reverse the digits of the number
    reversed_num = int(str(x)[::-1])
    return reversed_num

# Input from the user
x = int(input("Enter the number: "))

# Get the reversed number
rev = reverse_number(x)

# Output the reversed number
print("Reversed number:", rev)