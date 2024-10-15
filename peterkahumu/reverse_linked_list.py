class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = Node(data)

    def printList(self):
        current = self.head
        if not current:
            print("The list is empty")
        else:
            while current:
                print(current.data, end=(" "))
                current = current.next
        
    def reverse(self):
        previous = None
        current = self.head

        if not current:
            print("The list is empty")
        else:
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            self.head = previous

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.reverse()
linked_list.printList()
