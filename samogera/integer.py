def reverse_integer(n):
    # Convert integer to string and handle the sign
    sign = -1 if n < 0 else 1
    n = abs(n)
    # Reverse the digits and convert back to integer
    reversed_number = int(str(n)[::-1]) * sign
    return reversed_number
print(reverse_integer(500))   # Output: 5
