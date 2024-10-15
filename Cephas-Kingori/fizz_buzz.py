"""
Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.
"""

def fizz_buzz(i=1, n=100):
    for i in range(i, n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)

    return

if __name__ == "__main__":
    # print("General case:")
    fizz_buzz()                 # general case

    # print("Custom Range:")
    # fizz_buzz(30,120)         # custom range

    # print("Specific Case:")
    # fizz_buzz(35, 35)         # specific case

    # print("Specific Case:")
    # fizz_buzz(-6, -6)         # negative case