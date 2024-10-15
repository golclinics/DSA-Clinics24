# Loop running from 1 to 100
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0: # If the number is divisible by both 3 and 5 (num % 3 == 0 and num % 5 == 0), it prints FizzBuzz
        print("FizzBuzz")
    elif num % 3 == 0: # If the number is divisible by only 3 (num % 3 == 0), it will print Fizz.
        print("Fizz")
    elif num % 5 == 0: # If the number is divisible by only 5 (num % 5 == 0), it will print Buzz.
        print("Buzz")
    else: # Otherwise, it prints the number itself
        print(num)
