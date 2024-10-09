# Loop through numbers from 1 to 100 
for i in range(1, 101): 
    # Check if the number is divisible by both 3 and 5 
    if i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz") # Print "FizzBuzz" for multiples of both 3 and 5 
    # Check if the number is divisible by 3 
    elif i % 3 == 0: 
        print("Fizz") # Print "Fizz" for multiples of 3 
    # Check if the number is divisible by 5 
    elif i % 5 == 0: 
        print("Buzz") # Print "Buzz" for multiples of 5 
    else: 
        print(i) # Print the number if it is not divisible by 3 or 5