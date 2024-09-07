class Node:
    def __init__(self, number):
        self.number = number
        self.next=None
    

class Power:
    def __init__(self):
        self.head = None
       
        
    def powerchecker(self, number):
        
        if isinstance(number, int):
            new_node = Node(number)
            
            self.head = new_node
            print(self.head.number)
            if self.head.number == 1:
                print('a power of 2')
                return
            
            current = self.head
            while (current.number / 2) != 1:
                
                
                if isinstance(current.number, int)==True or float(current.number).is_integer():
                    current.number = current.number / 2
                
                    if current.number == 2:
                        
                        print('a power of 2')
                
                else:
                    print('not a power of 2')
                    break
                

            
        else:
            return "not an integer"
if __name__ == "__main__":
    p = Power()
    p.powerchecker(8)