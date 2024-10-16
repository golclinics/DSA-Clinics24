class Node:
    """Represents a node in the linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None # Initialize an empty linked list
    
    def append(self, value):
        """Adds a new node to the end of the linked list."""
        new_node = Node(value)
        if self.head is None: # If the list is empty the new node becomes the head
            self.head = new_node
        else: # If the list isn't empty, traverse to the end of the list and add the new node at the tail
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def display(self, message=""):
        print(message, end="") # Print the message inputed and stay on the same line
        current = self.head
        while current:
            if current.next is None:
                print(current.value, end="") # If it is the last node don't print the arrow
            else:
                print(current.value, end=" -> ")
            current = current.next
        print() # New line after printing the list
        
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next # Store the next node in memory
            current.next = prev # Reverse the pointer
            prev = current # Move prev to current
            current = next_node # Move to the next node
        self.head = prev # Update the last node as the head
        
# Create the linked list
li = LinkedList()

li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)

#Display the original list
li.display("Linkedn List: ") #Linked List: 1 -> 2 -> 3 -> 4 -> 5

li.reverse() # Reverse the list

# Display the reversed list
li.display("Reversed Linked List: ") # Reversed Linked List: 5 -> 4 -> 3 -> 2 -> 1