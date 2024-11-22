def reverse_integer(n):
    # Check if the number is negative
    is_negative = n < 0
    # Convert the number to a string and reverse it
    reversed_str = str(abs(n))[::-1]
    # Convert the reversed string back to an integer
    reversed_int = int(reversed_str)
    # If the number was negative, make the result negative
    if is_negative:
        reversed_int = -reversed_int
    return reversed_int

# Example usage
if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    print("Reversed integer:", reverse_integer(num))