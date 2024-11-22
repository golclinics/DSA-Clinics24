def reverse_integer(n):
    # convert integer to string and reverse it
    reversed_str = str(abs(n))[::-1]
    # convert back to integer
    reversed_int = int(reversed_str)

    # restore the negative sign if needed
    if n < 0:
        reversed_int = -reversed_int
    return reversed_int
