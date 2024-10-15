

def isPowerOfTwo(num):

    '''
    Power of Two
    Write a program that takes an integer as input and returns true if the input is a power of two.

    Examples:

    8=> returns true 
    6=> returns false
    '''

    if num <= 0 or not isinstance(num, int):
        return False
    
    return (num & (num - 1)) == 0

print(isPowerOfTwo(8))

print(isPowerOfTwo(6))

print(isPowerOfTwo(16))