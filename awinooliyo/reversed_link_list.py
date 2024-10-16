class ListNode:
    """
    Class representing a single node in a singly linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : ListNode or None
        The reference to the next node in the linked list.
    """
    def __init__(self, value=0, next=None):
        """
        Initialize a new node in the linked list.

        Parameters:
        -----------
        value : int, optional
            The value to be stored in the node (default is 0).
        next : ListNode or None, optional
            The reference to the next node (default is None).
        """
        self.value = value
        self.next = next


def reverse_linked_list(head):
    """
    Reverse a singly linked list.

    Parameters:
    -----------
    head : ListNode
        The head of the singly linked list to be reversed.

    Returns:
    --------
    ListNode
        The new head of the reversed linked list.

    Example:
    --------
    Given the linked list 1 -> 2 -> 3 -> 4 -> 5, the function will return
    the reversed linked list 5 -> 4 -> 3 -> 2 -> 1.
    """
    # Initializing previous node as None
    prev = None
    # Start with the current node as the head of the list
    current = head
    # Traverse the list and reverse the pointers
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def print_linked_list(head):
    """
    Print the linked list in a human-readable format.

    Parameters:
    -----------
    head : ListNode
        The head of the singly linked list to be printed.

    Example:
    --------
    For the linked list 1 -> 2 -> 3 -> 4 -> 5, the output will be:
    1 -> 2 -> 3 -> 4 -> 5
    """
    current = head
    while current is not None:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# Example Usage:
# Creating the linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original Linked List:")
print_linked_list(head)

# Reversing the linked list
reversed_head = reverse_linked_list(head)

print("Reversed Linked List:")
print_linked_list(reversed_head)
