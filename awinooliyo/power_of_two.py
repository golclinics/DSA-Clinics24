def is_power_of_two(n: int) -> bool:
    """
    Determines if the given integer is a power of two.
    A number is a power of two if there exists an integer k such that n = 2^k.
    Args:
    n (int): The integer to check.
    Returns:
    bool: True if the number is a power of two, False otherwise.
    """
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
