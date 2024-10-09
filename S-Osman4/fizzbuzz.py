def fizzbuzz():
    '''
    Print numbers from 1 to 100.
    For multiples of 3, print Fizz.
    For multiples of 5, print Buzz.
    For multiples of both 3 and 5, print FizzBuzz.
    '''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)