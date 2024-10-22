def reverse_integer(number):
    reversed_number = int(str(abs(number))[
                          ::-1]) if number > 0 else int(str(abs(number * -1))[::-1]) * -1

    return reversed_number


# Testing the function with given examples
print(reverse_integer(500))
print(reverse_integer(-56))
print(reverse_integer(-90))
print(reverse_integer(91))
