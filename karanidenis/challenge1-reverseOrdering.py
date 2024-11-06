# Write a program that takes an integer as input and return an integer with reversed digit
# ordering.

# For example

# For input 500, the program should return 5. 
# For input -56, the program should return -65. 
# For input -90, the program should return -9. 
# For input 91, the program should return 19. 


def reverseOrdering(num):
    num_str = str(num)

    if num < 0:
        return int("-" + str(num)[::-1][:-1])
    else:
        return int(str(num)[::-1])
    
    
print(reverseOrdering(500)) # 5
print(reverseOrdering(-56)) # -65
print(reverseOrdering(-90)) # -9
print(reverseOrdering(91)) # 19