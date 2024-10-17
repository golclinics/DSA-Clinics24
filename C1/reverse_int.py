def reverse(n):
    """
    This function takes an integer n as input and returns the integer with its digits reversed.
    :param n: Integer input, positive or negative
    :return: Integer with reversed digits
    """

    is_negative = n < 0
    reversed_str = str(abs(n))[::-1]
    reversed_int = int(reversed_str)
    return -reversed_int if is_negative else reversed_int
