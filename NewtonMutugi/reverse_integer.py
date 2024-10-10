def reverse_integer(num: int) -> int:
    """
    Takes an integer as input and
    returns an integer with reversed digit ordering.
    """
    sign = -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1])
    return sign * reversed_num

if __name__ == "__main__":
    # Test for positive integer
    print(reverse_integer(234))
    # Test for negative integer
    print(reverse_integer(-234))
