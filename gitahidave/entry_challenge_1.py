def reverse_integer(x):
    # Ensuring the number is a negative
    sign = -1 if x < 0 else 1
    
    # Reversing the digits by converting the number to a string
    reversed_str = str(abs(x))[::-1]
    
    # Converting the reversed string back to an integer
    reversed_num = int(reversed_str)
    
    # Restoring the sign of the number
    return sign * reversed_num

# Prompting the user for input
num = int(input("Enter an integer: "))
print("Reversed integer:", reverse_integer(num))
