#!/usr/bin/python3

def fizz_buzz():
    """
        Program that prints the numbers from 1 to 100. 
        For multiples of 3, print Fizz; 
        For multiples of 5, print Buzz; 
        For numbers that are multiples of both 3 and 5, print FizzBuzz
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{i} ", end="")
    print("\n")

if __name__ == "__main__":
    fizz_buzz()
