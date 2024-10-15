def reverseInteger(number):
    if number == 0 or float(number) != number:
        raise ValueError("The number must not be equal to zero or a decimal")
    else:
        number = int(number)
    
    numberString = list(str(abs(number))) # handle negative numbers and remove the negative sign
    reversedNumber = reversed(numberString)

    reversedNumber = int(''.join(reversedNumber)) #  convert the number to a string then integer
    if int(number) < 0:
        return -reversedNumber
    else:
        return reversedNumber
    

try:
    integer = float(input("Please enter a number:  "))

    if integer == 0 or int(integer) != integer:
        raise ValueError("The number must not be equal to zero or a decimal")
    else:
        integer = int(integer)
except Exception as e:
    raise ValueError("The number should be an integer or greater than zero") from e


print(reverseInteger(integer))