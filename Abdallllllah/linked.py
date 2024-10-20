class Node:
    def __init__(self, data, next=None):
        self.data=data 
        self.next= next
    

    
class linked:
    def __init__(self):
        self.head= None
    
    def insertbeginning(self, data):
        newnode = Node(data)
        newnode.next=self.head
        self.head=newnode

    def atend(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head=newnode
            return
        current = self.head
        while current.next:
            current=current.next
        current.next=newnode
    

    def delete(self, key):
        if self.head.data==key:
            self.head = self.head.next
            return
        current = self.head
        prev=None
        while current:
            if current.data==key:
                prev.next= current.next
                return
            prev= current
            current= current.next
                




    def print(self):
        current = self.head
        while current:
            print(current.data,end="-->")
            current= current.next
    def reverselist(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current=next
        self.head=prev



link = linked()
link.atend("mango")
link.atend("orange")

link.atend("lemon")
link.print()
link.reverselist()
print()
link.print()
        
        