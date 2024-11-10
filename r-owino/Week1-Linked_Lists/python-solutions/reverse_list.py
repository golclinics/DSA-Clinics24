#!/usr/bin/env python3
"""
206. Reverse Linked List

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
given: 1 -> 2 -> 3 -> 4 -> 5
reverse: 5 -> 4 -> 3 -> 2 -> 1

Input: head = [1,2]
Output: [2,1]
given: 1 -> 2
reverse: 2 -> 1

Input: head = []
Output: []

"""

from list_definition import ListNode, SinglyListInsert
from typing import Optional

class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """reverses a linked list"""
        # check if the list is empty or only has one element
        if head is None or head.next is None:
            return head
        
        # reverse the list
        temp = head
        prev = None

        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        
        return prev

if __name__ == "__main__":
    insert = SinglyListInsert()
    insert.insert_node(1)
    insert.insert_node(2)
    insert.insert_node(3)
    insert.insert_node(4)

    print("Original list:")
    insert.display()

    sol = Solution()
    insert.head = sol.reverseList(insert.head)

    print("List after reversal:")
    insert.display()
