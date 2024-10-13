def reverse_integer(x):
    
    negative = x < 0
    x = abs(x)

    reversed_integer = int(str(x)[::-1])

    if negative:
        return -reversed_integer
    return reversed_integer

# testing on the cli
num = int(input("Enter an integer: "))
print("The Reversed Integer:", reverse_integer(num))
