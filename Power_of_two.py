# A program that takes an integer as input and returns true if input is a power of two
# It can be solved simply by using python bitwise operators
def is_power_of_two(n):
    return (n > 0) and (n & (n-1)) == 0



    

    