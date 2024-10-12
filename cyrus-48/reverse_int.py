# Write a program that takes an integer as input and return an integer with reversed digit
# ordering.

# For example

# For input 500, the program should return 5. 
# For input -56, the program should return -65. 
# For input -90, the program should return -9. 
# For input 91, the program should return 19. 



def reverse_integer(n: int) -> int:
    if  n < 0 :
        reversed_int =  int("-" + str(n)[:0:-1])
        
    else:
        reversed_int  = int(str(n)[::-1])
        
        
    return reversed_int



#  tests

print(reverse_integer(500))
print(reverse_integer(-56))
print(reverse_integer(-90))
print(reverse_integer(91))