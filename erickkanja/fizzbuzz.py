#initializes the counter
num = 1
#Loops through numbers from 1-100
while num <=100:
    #Prints Fizzbuzz if the number is divisible by both 3 and 5
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    #Prints Fizz if the number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")
    #Prints Buzz if the number is divisible by 3
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    #Increments counter
    num = num + 1