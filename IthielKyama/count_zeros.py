# Program that takes an integer as input and returns true if the input is a power of two using recursion

def function(num):
    if num <= 0:
        return False
    elif num == 1:
        return True
    else:
        return num % 2 == 0 and function(num // 2)


n = int(input("Input integer: "))
print(function(n))
