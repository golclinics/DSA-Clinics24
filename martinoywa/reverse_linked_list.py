from helpers.linked_list_helpers import *


def reverse_linked_list(head):
    prev, after, current = None, None, head

    while current:
        after = current.next
        current.next = prev
        prev = current
        current = after

    return prev


if __name__ == "__main__":
    # create the LL
    LL = ListNode(1)
    current = LL
    for _ in range(2, 6):
        current.next = ListNode(_)
        current = current.next
    
    print("Before Reverse")
    print_linked_list(LL)
    print()

    print("After Reverse")
    LL_rev = reverse_linked_list(LL)
    print_linked_list(LL_rev)
    print()
    