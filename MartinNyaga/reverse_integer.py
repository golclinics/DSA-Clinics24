def reverse_integer(n):
    # Using string slicing

    if n < 0:           # check if n is a negative number
        return -int(str(n)[1:][::-1])
    else:
        return (str(n)[::-1])

num = int(input("Enter an integer: ")) # inputs the integer

print(reverse_integer(num)) # prints the result