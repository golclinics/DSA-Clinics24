#!/usr/bin/python3

def power_of_2(n):
    if (n <= 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
    return True

if __name__ == "__main__":

    val = int(input('Enter a value\n'))

    if(power_of_2(val)):
        print("{}=> returns true".format(val))
    else:
        print("{}=> returns false".format(val))
