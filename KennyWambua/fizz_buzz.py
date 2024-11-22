"""

    A python program that prints the numbers from 1 to 100. For multiples of 3, print Fizz;
    For multiples of 5, print Buzz; and for numbers that are multiples of 3 and 5 , print FizzBuzz.

"""

def fizz_buzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
           print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

if __name__ == "__main__":
    fizz_buzz()