for x in range(1,101): #Loop for printing the numbers from 1 to 100
    if(x%3==0 and x%5==0): # checking for the divsiblilty of both 3 and 5 if the condtion is not met it proceeds with the loop
        print(f"{x} FizzBuzz") # returns fizzbuzz if both numbers are divisble by 3 and 5
    elif(x%3==0): # checking for the divsiblilty  3 , if the condtion is not met it proceeds with the loop
        print(f"{x} Fizz") # returns if fizz numbers are divisble by 5
    elif(x%5==0): # checking for the divsiblilty  5 if the condtion is not met it proceeds with the loop
        print(f"{x} Buzz") # returns buzz if the numbers are divisble by 5
    else:
        print(x) # all the remaining numbers that do not meet the conditions are printed out