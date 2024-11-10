#!/usr/bin/env python3
"""
24. Swap Nodes in Pairs

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
given: 1 -> 2 -> 3 -> 4
swap: 2 -> 1 -> 4 -> 3

Input: head = [1,2,3]
Output: [2,1,3]
given: 1 -> 2 -> 3
swap: 2 -> 1 -> 3
"""

from list_definition import ListNode, SinglyListInsert
from typing import Optional

class Solution:
    def __init__(self):
        self.head = None

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        # check that the nodes to be swapped are not null
        while curr.next and curr.next.next:
            # identify nodes to swap
            first = curr.next
            second = first.next

            # actual swap
            first.next = second.next
            second.next = first
            curr.next = second

            # next pair swap
            curr = first
        
        return dummy.next

if __name__ == "__main__":
    insert = SinglyListInsert()
    insert.insert_node(1)
    insert.insert_node(2)
    insert.insert_node(3)
    insert.insert_node(4)
    insert.insert_node(6)

    # display the inserted list
    print("Original list:")
    insert.display()

    # swap pairs
    sol = Solution()
    insert.head = sol.swapPairs(insert.head)
    
    # display list after swapping
    print("After swapping:")
    insert.display()
