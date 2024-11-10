""" contains the list definition for a singly linked list """

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyListInsert:
    def __init__(self):
        self.head = None
    
    def insert_node(self, val):
        """inserts a new node at the tail"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def display(self):
        """displays the linked list"""
        nodes = []
        current = self.head
        while current:
            nodes.append(current.val)
            current = current.next
        print(" -> ".join(map(str, nodes)))
