def reverse_integer(number):
    ''' step 1: convert the "number" to a string to reverse the digits '''
    num_str = str(abs(number))
    reversed_str = num_str[::-1]
    
    '''step 2: convert the reversed string back to an integer'''
    reversed_num = int(reversed_str)
    
    '''step 3: Handle negative numbers i.e 500'''
    if number < 0:
        reversed_num = -reversed_num
    
    return reversed_num


def main():
    '''Testing with cases given'''

    print(reverse_integer(500))   # Output: 5
    print(reverse_integer(34567898765433456700))   # Output: 765433456789876543
    print(reverse_integer(-56))   # Output: -65
    print(reverse_integer(-90))   # Output: -9
    print(reverse_integer(91))    # Output: 19

    



if __name__ == "__main__":
    main()
