def powerOfTwo(x):
    """
    i need to returns True if the given integer x is a power of two, False otherwise.
    """
    if x <= 0:
        return False
    
    ''' checking for even and repeatedly dividing by 2 '''
    while x % 2 == 0:
        x //= 2 

    return x == 1    


def main():
    '''Testing with cases given'''

    print(powerOfTwo(8))  # True
    print(powerOfTwo(6))  # False
    print(powerOfTwo(16)) # True
    print(powerOfTwo(12)) # False
    print(powerOfTwo(0))  # False
    print(powerOfTwo(-3)) # False




if __name__ == "__main__":
    main()
