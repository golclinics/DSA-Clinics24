def reverse_integer(n):
    #  Plan
    # 1. Check if number is negative. If negative, work with its absolute value
    # 2. Convert the absolute value of the number to a string
    # 3. If the original number was negative, make the result negative
    # 4. Return the reversed integer

    num = n < 0
    num_abs = abs(n)

    string = str(num_abs)[::-1]
    integer = int(string)

    if num:
        integer = -integer
    return integer

# Test the Function


def test_reverse_integer():
    # Simple test cases
    print("Test cases:")
    print("Input: 1234, Output:", reverse_integer(1234))  
    print("Input: -567, Output:", reverse_integer(-567))   
    print("Input: 0, Output:", reverse_integer(0))         
    print("Input: 1000, Output:", reverse_integer(1000))   
    print("Input: 10, Output:", reverse_integer(10))       
    print("Input: 7, Output:", reverse_integer(7))         
    print("Input: -100, Output:", reverse_integer(-100))   
    print("Input: 2147483647, Output:", reverse_integer(2147483647))  
    print("Input: -2147483648, Output:", reverse_integer(-2147483648))  

def main():
    test_reverse_integer()  
    
# Run the main function
if __name__ == "__main__":
    main()