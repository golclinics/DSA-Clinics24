# Write a program that takes an integer as input and return an integer with reversed digit ordering.
# For input 500, the program should return 5. 
# For input -56, the program should return -65. 
# For input -90, the program should return -9. 
# For input 91, the program should return 19. 


def reverse_num(num):
    #Ensure it's a valid number
    try:
        number=int(num)
        #check if number is a multiple of 10, and reduce the zeros e.g 500->5 , 90->9
        while number % 10==0:
            number=number//10
        #check if it is a negative number
        negative_flag=False
        if number<1:
            negative_flag=True
        #convert number to string
        number=str(number)
        number=number[::-1]
        if negative_flag is True:
            number=number.replace(number[-1],"")
            number="-"+number
        number=int(number)
        return number
    except ValueError:
            print("Please enter a valid integer")


print(reverse_num(500)) #Prints 5
print(reverse_num(-56)) #Prints -65
print(reverse_num(-90)) #Prints -9
print(reverse_num(91))  #Prints 19