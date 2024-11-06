# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    
# Create a hard-coded linked list:
# 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = ListNode(60)
head.next.next.next.next.next.next = ListNode(70)
head.next.next.next.next.next.next.next = ListNode(80)

head.next.next.next.next.next.next.next = head.next

print(Solution().hasCycle(head)) # False