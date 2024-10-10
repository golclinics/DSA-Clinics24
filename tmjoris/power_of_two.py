def is_power_of_two(num):
                    #Does a Bitwise AND operation between num and num-1, before 
                    #checking if all the bits are 0, to see if num is a power of 2 
    if num > 0 and (num & (num-1)) == 0: 
        return True
    return False

number = int(input("Enter a number: "))

print(is_power_of_two(number))
