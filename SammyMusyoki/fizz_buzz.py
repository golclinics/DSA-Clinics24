"""
    Entry Challenge C2
    
    Write a program that prints the numbers from 1 to 100. For multiples of 3, print 'fizz';
    for mulitples of 5, print 'Buzz'; for multiples of both 3 and 5 print 'FizzBuzz'
"""

def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
            
fizzbuzz()