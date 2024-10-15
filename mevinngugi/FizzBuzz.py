"""
Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.
"""
def FizzBuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print (f"{x} % 3 and 5 = FizzBuzz")
        elif x % 3 == 0:
            print (f"{x} % 3 = Fizz")
        elif x % 5 == 0:
            print (f"{x} % 5 = Buzz")
