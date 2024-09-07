#Write a program that takes an integer as input and return an integer with reversed digit
#ordering.
#
#For example
#
#For input 500, the program should return 5. 
#For input -56, the program should return -65. 
#For input -90, the program should return -9. 
#For input 91, the program should return 19. 
class Reverse:
    def __init__(self, number):
        self.number=number

    def reverse(self):
        if self.number>0:
            self.number = str(self.number)
            output=''
            y=len(self.number)-1
            for i in range(len(self.number)):
                output+=self.number[y]
                y -= 1
            print(int(output))
        else:
            self.number = str(self.number)
            output=self.number[0]
            y=len(self.number)-1
            for i in range(len(self.number)-1):
                output+=self.number[y]
                y -= 1
            print(int(output))

            
if __name__ == '__main__':
    r = Reverse(-65)
    r.reverse()