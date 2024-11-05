class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    # Plan
    # 1. Initialize three pointers: previous(prev), current(curr) and next_node
    # 2. Set prev to None (becomes the new head of the reversed list)
    # 3. Loop through the list while current is not None:
    #       a. Store the next node (current.next) in next_node
    #       b. Reverse by setting current.next to prev
    #       c. Move prev and curr one step forward
    # 4. After the loop, return prev, which is now the new head of the reversed list

    prev =  None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# Test the Function
def print_linked_list(head):
    """Helper function to print the linked list."""
    curr = head
    while curr:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("None")  # End of the list

def main():
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original linked list:")
    print_linked_list(head)

    # Reverse the linked list
    reversed_head = reverse_linked_list(head)

    print("Reversed linked list:")
    print_linked_list(reversed_head)

# Run the main function
if __name__ == "__main__":
    main()