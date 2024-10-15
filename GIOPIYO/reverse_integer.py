# Write a program that takes an integer as input and return an integer with reversed digit ordering.
def reverse_number(n):
    if n < 0:
        reversed_str = str(abs(n))[::-1]
        reversed_number = -int(reversed_str)
    else:
        reversed_str = str(n)[::-1]
        reversed_number = int(reversed_str)
    
    return reversed_number


print(reverse_number(1009)) 

