#!/usr/bin/python3

def reverseDigit(num: int) -> int:
    '''Reverses a number. e.g -56 reversed is -65

    Args:
        num (int) - number to reverse the values.
    Return:
        reversed number
    '''
    is_negative = num < 0
    num = abs(num)

    reversed_num = 0
    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num = num // 10
    
    if is_negative:
        reversed_num = -reversed_num
    
    return reversed_num
