# FizzBuzz
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
# multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.


def fizzBuzz(num):
    if num <= 0:
        return False
    
    result = [] #Creating an empty array to hold the result
    for i in range(1, num + 1): # Loop over all the numbers from 1 inclusive to num inclusive (num + 1)
        if (i % 3 == 0) and (i % 5 == 0):
            result.append("FizzBuzz") #append/push the result to the result string
        elif i % 3 == 0:
            result.append("Fizz") #append/push the result to the result string
        elif i % 5 == 0:
            result.append("Buzz") #append/push the result to the result string
        else:
            result.append(str(i)) #append/push the converted number to the result string

    return result


# Testing:
print(fizzBuzz(15))  #['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
print(fizzBuzz(10))  #['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
print(fizzBuzz(10))  #False