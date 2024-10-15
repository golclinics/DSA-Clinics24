// Define the ListNode class
class ListNode {
    constructor(value = 0, next = null) {
        this.value = value;
        this.next = next;
    }
}

// Function to reverse the linked list
function reverseLinkedList(head) {
    let prev = null;
    let current = head;
    let next = null;

    while (current !== null) {
        // Save the next node
        next = current.next;
        // Reverse the current node's pointer
        current.next = prev;
        // Move the pointers one step forward
        prev = current;
        current = next;
    }

    // Return the new head of the reversed linked list
    return prev;
}

// Creating the linked list 1 -> 2 -> 3 -> 4 -> 5
let head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);
head.next.next.next.next = new ListNode(5);


// Reversing the linked list
let reversedHead = reverseLinkedList(head);

// Printing the reversed linked list
let current = reversedHead;
while (current !== null) {
    console.log(current.value);
    current = current.next;
}