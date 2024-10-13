def reverseInteger(number):
    if number == 0 or int(number) != number:
        raise ValueError("The number must not be equal to zero or a decimal")
    
    numberString = list(str(abs(number))) # handle negative numbers and remove the negative sign
    reversedNumber = reversed(numberString)

    reversedNumber = int(''.join(reversedNumber)) #  convert the number to a string then integer
    if int(number) < 0:
        return -reversedNumber
    else:
        return reversedNumber
    

integer = int(input("Please enter a number:  "))
print(reverseInteger(integer))