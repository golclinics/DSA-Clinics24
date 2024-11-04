

# Code to write a program that takes an integer as input and returns an integer with reversed digit ordering

def rev_number(number):
    conv_number = str(number)   

    if conv_number[0] == "-":
        reversed_str = "-" + conv_number[:0:-1]
    else:
        reversed_str = conv_number[::-1]

    # Return the reversed string converted to an integer
    return int(reversed_str)

# Test cases
print(rev_number(500))   # Expected output: 5
print(rev_number(-56))   # Expected output: -65
print(rev_number(-90))   # Expected output: -9
print(rev_number(91))    # Expected output: 19






