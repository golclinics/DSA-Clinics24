"""
Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.
"""

for x in range(1,101):
    
     # Check if the number is a multiple of 3
    if x % 3 == 0:
        print("Fizz")

    # Check if the number is a multiple of 5
    elif x % 5 == 0:
        print("Buzz")

    # Check if the number is a multiple of both 3 and 5
    elif x % 3 == 0 and x % 5== 0:
        print("FizzBuzz")

    # Otherwise, just print the number
    else:
        print(x)

    