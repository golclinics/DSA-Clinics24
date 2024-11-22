for i in range(1,101):
    output ="" # an empty string for each number
    
    if i % 3 == 0 :
       output += "Fizz" # if the number is divisible by 3 then append the string with fizz
    
    if i % 5 == 0:
        output+= "Buzz" # if the number is divisible by 5 then append string with buzz
    
    if output =="":
        print(i)  # if there was no string added, print the number 
    else:
        print(output)   # print the resulting string which will be in this case FizzBuzz  
            