"""
Given the linked list 1 -> 2 -> 3 -> 4 -> 5,
reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e


def reverseList(head: Node) -> Node:
    if head is None:
        return

    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


print(reverseList(a))
