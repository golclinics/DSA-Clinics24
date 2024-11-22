#Entry Challenge C2
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
# multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.


""" My solution algorithm
step1:iterating numbers through range 1-101
step2:checking if the number is divisible by 3
step3: if number is divisible by 3 check if is divisible by 5 and if true prints "fizzbuz" if false print "Buzz"
step4: check if number is divisible by 5 and if True prints Fizz
step5: if step2 ,step3,step4 are false print the number
"""

for number in range(1,101):
    if number%3 == 0:
        if number%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)