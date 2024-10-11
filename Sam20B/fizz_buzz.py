def number_list():
    for num in range(1, 101): # Loop from 1 to 100
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz") # Print "FizzBuzz" for multiples of both 3 and 5
        elif num % 3 == 0:
            print("Fizz") # Print "Fizz" for multiples of 3
        elif num % 5 == 0:
            print("Buzz") # Print "Buzz" for multiples of 5
        else:
            print(num) # Print the number for any other condition

number_list() # calls the function

