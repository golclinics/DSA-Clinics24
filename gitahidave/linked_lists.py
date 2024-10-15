# Define the structure of a singly linked list node
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to reverse the linked list
def reverse_linked_list(head):
    prev = None  # Initialize previous node as None
    current = head  # Start with the head node

    while current:  # Traverse through the linked list
        next_node = current.next  # Save the next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move prev to the current node
        current = next_node  # Move to the next node

    return prev  # prev will be the new head of the reversed list

# Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original list:")
print_linked_list(head)

# Reversing the linked list
reversed_head = reverse_linked_list(head)

print("Reversed list:")
print_linked_list(reversed_head)
