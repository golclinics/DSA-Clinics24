A linked list is a linear data structure where elements, called *nodes*, are linked together using pointers. Each node contains two parts:

1. **Data**: Stores the actual value or information.
2. **Pointer/Reference**: Stores the address of the next node in the sequence.

Linked lists come in several types:

- **Singly Linked List**: Each node points to the next node in the list, forming a one-way chain.
- **Doubly Linked List**: Each node has two pointers—one to the next node and one to the previous node—allowing traversal in both directions.
- **Circular Linked List**: The last node points back to the first node, forming a loop.

### Key Characteristics:
- **Dynamic Size**: Linked lists can easily grow or shrink in size as elements are added or removed.
- **Efficient Insertions/Deletions**: Adding or removing nodes does not require shifting elements, as in an array. It just requires updating pointers.
- **No Direct Access**: Unlike arrays, linked lists do not allow direct access to elements. You must traverse the list from the head node to access a specific element.

### Common Operations:
- **Insertion**: Can be done at the beginning, end, or a specific position in the list.
- **Deletion**: Can be done for a specific node or position.
- **Traversal**: Accessing each node sequentially to process the data.

Linked lists are commonly used for implementing other data structures like stacks, queues, and for applications where dynamic memory allocation is necessary.