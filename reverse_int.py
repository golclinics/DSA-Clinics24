def reverse_integer(num):
    number = str(num) 

    if number[0] == '-' and number[1] == '0':
  		# code checks for 0 as a number in the input
        return -int(number.replace('0', ''))
    elif number[0] == '-':
        # code checks for any negative sign
        return -int(number[:0:-1])
    else:
        # Handle positive numbers
        return int(number[::-1])

s = int(input("Enter your integer: "))
print(reverse_integer(s))
