def reverse_integer(n):
    negative = n < 0
    n = abs(n)
    
    reversed_str = str(n)[::-1]
    reversed_int = int(reversed_str)
    
    if negative:
        reversed_int = -reversed_int
        
    return reversed_int

def test_reverse_integer():
    print(reverse_integer(500))   
    print(reverse_integer(-56))   
    print(reverse_integer(-90))   
    print(reverse_integer(91))    
    print(reverse_integer(0))     

test_reverse_integer()