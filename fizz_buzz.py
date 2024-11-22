def fizz_buzz(n=100):
    """
    Prints FizzBuzz sequence up to n.
    
    Args:
    n (int): Upper limit of the sequence (default is 100).
    
    Returns:
    None
    """
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Function call
fizz_buzz()