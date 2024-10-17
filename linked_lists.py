class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next  
            prev = current         
            current = next_node 
        
        self.head = prev 