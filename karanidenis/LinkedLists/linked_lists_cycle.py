# Python program to detect loop
# in the linked list using hashset

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function that returns true if there is a loop in linked
# list else returns false.
def detect_loop(head):
    st = set()

    # loop that runs till the head is None
    while head is not None:

        # If this node is already present
        # in hashmap it means there is a cycle
        # (Because you will be encountering the
        # node for the second time).
        if head in st:
            return True

        # If we are seeing the node for
        # the first time, insert it in hash
        st.add(head)
        print(st)

        head = head.next
    return False

# Create a hard-coded linked list:
# 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
# head.next.next.next.next.next.next = Node(20)
print(head.data)

# head.next.next.next.next = head

print(head.data)

if detect_loop(head):
    print("true")
else:
    print("false")
