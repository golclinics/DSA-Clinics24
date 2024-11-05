#!/usr/bin/env python3

def fizzbuzz(start, end):
    # Plan:
    # 1. Loop through each number from start to end (inclusive).
    # 2. For each number, check:
    #    - If it is divisible by 3 and 5, print "FizzBuzz".
    #    - If it is divisible by 3, print "Fizz".
    #    - If it is divisible by 5, print "Buzz".
    #    - Otherwise, print the number itself.

    for number in range(start, end + 1):  # Loop from start to end (inclusive)
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")  # Divisible by both 3 and 5
        elif number % 3 == 0:
            print("Fizz")  # Divisible by 3
        elif number % 5 == 0:
            print("Buzz")  # Divisible by 5
        else:
            print(number)  # Print the number itself

def main():
    # Set the range for FizzBuzz
    start = 1  # Starting number
    end = 100  # Ending number

    print(f"FizzBuzz from {start} to {end}:")
    fizzbuzz(start, end)  # Call the fizzbuzz function with the specified range

# Run the main function
if __name__ == "__main__":
    main()
