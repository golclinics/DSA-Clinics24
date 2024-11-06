# Reverse a Linked List
# Implement a function to reverse a singly linked list.

# Given the linked list 1 -> 2 -> 3 -> 4 -> 5,
# reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def reverse(self):
        curr = self.head
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        print("Reversed Linked List: ", end=" ")
        
    # def __str__(self):
    #     current_node = self.head
    #     while(current_node):
    #         print(current_node.data, end=" -> ")
    #         current_node = current_node.next
    #     return ""
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            return new_node
        
        current = self.head
        while current.next is not None:
            current = current.next
            
        current.next = new_node
        

    # print method for linkedlist
    def printl(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            
linked_list = LinkedList()
linked_list.insertAtBegin(2)
linked_list.insertAtBegin(5)
linked_list.insertAtBegin(1)
linked_list.printl()
print("\n")
linked_list.reverse()
linked_list.printl()

print("\n")
linked_list.insertAtEnd(4)
linked_list.printl()
# print(linked_list)
