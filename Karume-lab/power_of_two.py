def is_power_of_two(num: int) -> bool:
    """
    Summary:
        Determines whether a given integer is a power of two.
    Parameters:
        num : int
            The number to check if it's a power of two.
    Returns:
        bool
            Returns True if the number is a power of two, False otherwise.
    """
    if num == 0:
        return False
    while num != 1:
        if num % 2 != 0:
            return False
        num //= 2

    return True
