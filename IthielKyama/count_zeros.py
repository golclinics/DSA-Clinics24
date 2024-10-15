# Program that takes an integer as input and returns true if the input is a power of two using recursion

def function(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    else:
        return n % 2 == 0 and function(n // 2)


print(function(4))
