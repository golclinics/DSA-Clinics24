class ListNode {
    constructor(value = 0, next = null) {
        this.value = value;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    // Add node to the end of list
    append(value) {
        if (!this.head) {
            this.head = new ListNode(value);
            return;
        }
        let current = this.head;
        while (current.next) {
            current = current.next;
        }
        current.next = new ListNode(value);
    }

    // Reverse linked list
    reverse() {
        let prev = null;
        let curr = this.head;
        while (curr) {
            let next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        this.head = prev;
    }


    print() {
        let current = this.head;
        let output = [];
        while (current) {
            output.push(current.value);
            current = current.next;
        }
        console.log(output.join(' -> '));
    }
}

// Example
const list = new LinkedList();
list.append(1);
list.append(2);
list.append(3);
list.append(4);
list.append(5);

console.log("Input:");
list.print();

list.reverse();

console.log("Output:");
list.print();