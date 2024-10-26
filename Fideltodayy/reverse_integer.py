def reverse_integer(n):
    """
    Reverses the digits of an integer.

    Parameters:
    n (int): The integer to be reversed.

    Returns:
    int: The reversed integer.
    """
    # Step 1: Handle the sign
    sign = -1 if n < 0 else 1
    abs_number = abs(n)

    # Step 2: Convert to string and reverse
    reversed_str = str(abs_number)[::-1]

    # Step 3: Convert back to integer (this removes leading zeros)
    reversed_number = int(reversed_str)

    # Step 4: Reapply the sign
    return sign * reversed_number

# Example usage:
if __name__ == "__main__":
    # Test cases
    test_inputs = [500, -56, -90, 91, 0, 0000]
    for num in test_inputs:
        reversed_num = reverse_integer(num)
        print(f"Input: {num} → Output: {reversed_num}")
