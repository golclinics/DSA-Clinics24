user_input = int(input("Enter a number to check: ")) # request user for number/value

# function to check if value passed is a power of 2

def is_power_of_two(m):
    if m == 1:
        return True 
    elif m < 1:
        return False
    
    while m > 1:
        if m % 2 != 0:
            return False
        m //= 2
    return True

print(is_power_of_two(user_input))