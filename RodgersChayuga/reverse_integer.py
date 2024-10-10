# Reverse Integer

# Write a program that takes an integer as input and return an integer with reversed digit
# ordering.

# For example

# For input 500, the program should return 5. 
# For input -56, the program should return -65. 
# For input -90, the program should return -9. 
# For input 91, the program should return 19. 

def reverseInteger(num):
    # We handle the negative and positive sign.
    sign = -1 if num < 0 else 1

    # We update the value of 'num' with a positive number if it was negative, and maintain it if it was positive
    num = abs(num)

    reversed_num = 0 # this variable will store the reversed number
    while num > 0:
        digit = num % 10 # store the remainder of num divided by 10
        reversed_num = (reversed_num * 10) + digit # 
        num //= 10 # Get the result of num divided by 10

    return sign * reversed_num # returning back the sign eg (-1 * 345)

print(reverseInteger(-234)) # -432
print(reverseInteger(74)) # 47
print(reverseInteger(200)) # 2
