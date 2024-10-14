# Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
# multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.

num = int(input("Enter a number: "))
if num % 3==0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 ==0:
    print("Buzz")

else:
    print(num)