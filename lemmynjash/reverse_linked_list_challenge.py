# #Linked List Challenge

# Reverse a Linked List
# Implement a function to reverse a singly linked list.

# Examples:

# Given the linked list 1 -> 2 -> 3 -> 4 -> 5,
# reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1

class TheNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = TheNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, theValue):
        new_node = TheNode(theValue)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail=temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
            temp = self.head
            while temp is not None:
                print(temp.value, end=" -> " if temp.next else "\n")
                temp = temp.next

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.reverse()
my_linked_list.print_list()