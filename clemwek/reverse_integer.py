# This is a program that takes an integer and returns a reversed integer

def reversed_integer(x):
    def reverse(x):
        x = str(x)
        # reverse the string and convert to integer
        x = x[::-1]
        return int(x)
    # Check if the the integer is negative 
    if x < 0:
        # take the absolute value and convert it to a string
        return -reverse(abs(x))
    else:
        return reverse(x)

# Test the function
print(reversed_integer(123)) # 321
print(reversed_integer(-123)) # -321
print(reversed_integer(500)) # 5
print(reversed_integer(-65)) # -56
print(reversed_integer(-90)) # -9
