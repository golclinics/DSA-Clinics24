def fizz_buzz():
    """
    This function implements the FizzBuzz logic for numbers from 1 to 100.

    The rules are as follows:
    - For multiples of 3, it returns 'Fizz'.
    - For multiples of 5, it returns 'Buzz'.
    - For multiples of both 3 and 5, it returns 'FizzBuzz'.
    - For all other numbers, it returns the number itself as a string.
    """

    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
