# Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

# Examples:

# 8=> returns true 
# 6=> returns false

def powerOfTwo(num):
    # return num > 0 and (num & (num - 1)) == 0   
    if num > 0:
        while num % 2 == 0:
            num = num / 2
        if num == 1:
            return True
        else:
            return False
    else:
        return False


print(powerOfTwo(8)) # True
print(powerOfTwo(6)) # False
print(powerOfTwo(0)) # False
print(powerOfTwo(-8)) # False

