#!/usr/bin/env python3

# Define the ListNode classstNode


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to reverse a singly linked list


def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Helper function to print the linked list


def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Creating the linked list 1 -> 2 -> 3 -> 4 -> 5


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
printLinkedList(head)

# Reversing the linked list
reversed_head = reverseLinkedList(head)

print("Reversed Linked List:")
printLinkedList(reversed_head)
