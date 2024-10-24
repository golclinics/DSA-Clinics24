def reverse_integer(n):
    reversed_string = str(n)[::-1] # Convert the integer to a string and reverse the string

    if n < 0:
        reversed_int = -int(reversed_string[:-1]) # Remove the negative sign from the reversed string, then re-add it
    else:
        reversed_int = int(reversed_string)

    return reversed_int

print(reverse_integer(120))
print(reverse_integer(-123)) 