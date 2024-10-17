class node:
    def __init__(self,data=None):
        self.data = data
        self.next=None

    
class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def reverse(self):
        prev_node = None
        curr_node = self.head.next
        next_node = None

        while (curr_node != None) :  #We arent at the end of the LL yet
            next_node = curr_node.next   #Save the next node to avoid loss of nodes
            curr_node.next = prev_node   #Reverse the pointer
            prev_node = curr_node
            curr_node = next_node

        
        self.head.next =  prev_node

my_list = linked_list()

my_list.append(1)

my_list.append(2)

my_list.append(3)

my_list.append(4)

my_list.display()

my_list.reverse()

my_list.display()