def pow_of_two(input: int) -> bool:
    """
    Program that takes an integer as input and
    returns true if the input is a power of two.
    """
    return True if input % 2 == 0 else False
    # Bitwise implementation
    # return input > 0 and (input & (input - 1)) == 0


if __name__ == "__main__":
    # Test case false
    print(pow_of_two(3))
    # Test case true
    print(pow_of_two(4))
