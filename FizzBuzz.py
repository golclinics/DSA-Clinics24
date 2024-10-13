#!/usr/bin/env python3

# FizzBuzz Program: Prints numbers from 1 to 100 with special rules for multiples of 3 and 5.

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Run the fizzbuzz function
fizzbuzz()

