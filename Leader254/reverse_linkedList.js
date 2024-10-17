class GolNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  reverse() {
    if (this.head == null || this.head.next == null) return this;

    let current = this.head;
    let previous = null;
    let next = null;

    while (current) {
      next = current.next;
      current.next = previous;
      previous = current;
      current = next;
    }
    this.head = previous;
    return this;
  }
}

// Manual test
const list = new SinglyLinkedList();
const node1 = new GolNode(1);
const node2 = new GolNode(2);
const node3 = new GolNode(3);
const node4 = new GolNode(4);
const node5 = new GolNode(5);

list.head = node1;
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
list.tail = node1;

let current = list.head;
let values = [];

while (current) {
  values.push(current.value);
  current = current.next;
}
// log the list before the reversal

console.log("List before reversal is", values.join(" -> "));

list.reverse();

current = list.head;
values = [];
while (current) {
  values.push(current.value);
  current = current.next;
}
// print the list after reversing the list

console.log("Reversed List:", values.join(" -> "));
