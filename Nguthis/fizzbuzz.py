"""Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz."""
for digit in range(1,101):
    
    if  digit%3==0 and digit%5==0:
        print("FizzBuzz")
    elif digit%5==0:
        print("Buzz")
    elif digit%3==0:
        print("Fizz")
    else :
        print(digit)
