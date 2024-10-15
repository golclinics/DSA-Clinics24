def power_of_two(n):
    """
    This module takes an integer as input and returns true if the input is a power of two
    """
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

if __name__ == "__main__":
    #Test Cases
    test_cases = [8, 6, 0, -4, 16, 32, 3, 64]
    for case in test_cases:
        print(f"{case} => {power_of_two(case)}")