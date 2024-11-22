def reverse_integer(number: int):
    '''This functin takes in an integer and reverses it'''
    reversed_num = str(abs(number))[::-1]
    reversed_int = int(reversed_num)
    if number < 0:
        return reversed_int*-1
    else:
        return reversed_int
    
print(reverse_integer(-90))