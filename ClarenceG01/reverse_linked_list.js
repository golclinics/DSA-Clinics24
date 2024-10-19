class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

const reverseLinkedList = (head) => {
  let current = head;
  let prev = null;
  let next;
  while (current !== null) {
    next = current.next;
    current.next = prev;

    prev = current;
    current = next;
  }
  console.log(JSON.stringify(prev));
  return prev;
};
// test case 1->2->3->4->5
const node1 = new Node(1);
const node2 = new Node(2);
const node3 = new Node(3);
const node4 = new Node(4);
const node5 = new Node(5);

node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;

reverseLinkedList(node1);
