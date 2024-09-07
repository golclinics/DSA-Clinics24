#Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
#multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.
class FizzBuzz:
    def __init__(self):
        self.number = None
        
    def multiples(self):
        for self.number in range(100):
            if self.number % 3 == 0 and self.number % 5 == 0:
                print('FizzBuzz')
            elif self.number % 3 == 0:
                print('Fizz')
            elif self.number % 5 == 0:
                print('Buzz')
            else:
                print(self.number)
if __name__ == '__main__':
    f = FizzBuzz()
    f.multiples()