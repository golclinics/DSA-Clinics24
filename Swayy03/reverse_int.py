def reverse_integer(n):
    # Convert the integer to a string and reverse it
    if n < 0:
        reversed_str = '-' + str(n)[:0:-1]  # Skip the negative sign and reverse the rest
    else:
        reversed_str = str(n)[::-1]  # Reverse the string for positive numbers

    # Convert the reversed string back to an integer
    reversed_int = int(reversed_str)

    return reversed_int

print(reverse_integer(500))  # Output: 5
print(reverse_integer(-56))  # Output: -65
print(reverse_integer(-90))  # Output: -9
print(reverse_integer(91))   # Output: 19