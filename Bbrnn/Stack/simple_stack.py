class Stack:
    def __init__(self) -> None:
        #Initialize the stack
        self.stack = []
        
        
    def is_empty(self):
        #Check if the stack is empty
        return len(self.stack) == 0
    
    #Add an element to the top of the stack
    def push(self,element):
        self.stack.append(element)

    #Remove and print the top element of the stack
    def pop(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            return self.stack.pop()
    
    #Return the top most element
    def peek(self):
        if not self.is_empty():
            #Return the top element without removing it
            return self.stack[-1]
        else:
            return "The stack is empty"

     #Display the stack   
    def display(self):
         print("Stack elements", self.stack)


#Example
if __name__ =="__main__":
    stack =Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("Top element is", stack.peek())
    stack.pop()
    stack.display()


        