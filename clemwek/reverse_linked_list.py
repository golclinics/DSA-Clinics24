class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    current = head
    prev = None
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_linked_list(node):
    while node:
        print(node.value)
        node = node.next
        
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print("Original Linked List")
    print_linked_list(head)
    
    head = reverse_linked_list(head)
    
    print("Reversed Linked List")
    print_linked_list(head)
