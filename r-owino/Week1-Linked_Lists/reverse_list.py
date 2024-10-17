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

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
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

def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """convert an input list to a linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

sol = Solution()
linked_list = list_to_linked_list([1,2,3,4,5])
print(linked_list_to_list(sol.reverseList(linked_list)))
