def reverse_int(k):
# Change the value to absolute
    abs_k = str(abs(k))
    # Reverse the digits
    reversed_k = abs_k[::-1]
    reversed_value = int(reversed_k)

    #Check if its Negativve
    if k < 0:
        reversed_value = -reversed_value

    return reversed_value
        
print(reverse_int(500))
print(reverse_int(-56))
print(reverse_int(90))
print(reverse_int(91))