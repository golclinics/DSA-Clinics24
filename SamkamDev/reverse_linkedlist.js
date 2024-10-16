class Node {
  constructor(data) {
    this.data = data;
    this.tail = null;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  insertEnd(data) {
    const newNode = new Node(data);
    //Position of the head , check if the exist other elements
    if (this.head == null) {
      //if not have the created node pointing to the head
      this.head = newNode;
    } else {
      //if there exist other elements we loop until where the next value  of the node points to null , we start at the head of the list
      let current = this.head;
      while (current.next != null) {
        //if not null we move to the next node in each iteration
        current = current.next;
      }
      //1->2->3-4-5-->Null
      //when we reach to the last node which next points to null , we point next to created node
      current.next = newNode;
    }
    this.length++;
  }

  reverse() {
    //p<-c->n
    let prev = null;
    let current = this.head;
    let next = null;

    //the tail to the current head
    this.tail = this.head;

    while (current != null) {
      next = current.next;
      current.next = prev;
      prev = current;
      current = next;
    }
    //the head to the new tail
    this.head = prev;
  }

  printList() {
    let current = this.head;
    let result = "";
    while (current !== null) {
      result += current.data + " -> ";
      current = current.next;
    }
    result += "null";
    console.log(result);
  }
}

const list = new LinkedList();
list.insertEnd(1);
list.insertEnd(2);
list.insertEnd(3);
list.insertEnd(4);
list.insertEnd(5);

console.log("Original list:");
list.printList();

list.reverse();

console.log("Reversed list:");
list.printList();
