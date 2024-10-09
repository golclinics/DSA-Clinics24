def fizzBuzz():
    '''from 1 to including 100 hence 101'''
    for num in range(1, 101):
        '''using conditional statement to filter out logic'''
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print (num)
        

def main():
    '''Testing with cases given'''
    print(fizzBuzz())



if __name__ == "__main__":
    main()
            
