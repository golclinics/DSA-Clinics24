// From the Tuesday class, I have the following code to reverse a singly linked list
class GoLNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function reverseLinkedList(head) {
  let prev = null;
  let current = head;
  let next = null;

  while (current !== null) {
    next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }

  return prev;
}

function createLinkedList(arr) {
  if (arr.length === 0) return null;
  
  const head = new GoLNode(arr[0]);
  let current = head;
  
  for (let i = 1; i < arr.length; i++) {
    current.next = new GoLNode(arr[i]);
    current = current.next;
  }
  
  return head;
}

function linkedListToArray(head) {
  const result = [];
  let current = head;
  
  while (current !== null) {
    result.push(current.value);
    current = current.next;
  }
  
  return result;
}


function reverse() {
  console.log("Creating a linked list: [1, 2, 3, 4, 5]");
  const originalList = createLinkedList([1, 2, 3, 4, 5]);
  console.log("Original list:", linkedListToArray(originalList));

  console.log("\nReversing the linked list...");
  const reversedList = reverseLinkedList(originalList);
  console.log("Reversed list:", linkedListToArray(reversedList));

}

reverse();

module.exports = { reverseLinkedList, createLinkedList, linkedListToArray };