// Reverse a Linked List
// Implement a function to reverse a singly linked list.

// Examples:

// Given the linked list 1 -> 2 -> 3 -> 4 -> 5,
// reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1

// 1. Creating a linked list
class Node {
    constructor(data, next = null){
        this.data = data,
        this.next = next
    }
}

// Maintaining the head sextion
class LinkedList {
    constructor() {
        this.head = null
    }
}

const list = new LinkedList()

LinkedList.prototype.insertAtBeginning = function(data){
    let newNode = new Node(data)
    newNode.next = this.head
    this.head = newNode
    return this.head
}

list.insertAtBeginning(1)
list.insertAtBeginning(2)
list.insertAtBeginning(3)
list.insertAtBeginning(4)
list.insertAtBeginning(5)

let current = list.head

let numbers_container = []

while (current) {
    // for(let i = 0)
    current.data = current.data + ' -> ' 
    numbers_container += current.data
    // console.log((current.data + ' ->'))
    current = current.next
}

console.log(`reversed list: ${numbers_container}`)



// const reverse_linked_list = (list) => {
//     list_string = list.string() + 
//     console.log(list_string)
// }

// console.log(reverse_linked_list({1 -> 2 -> 3 -> 4 -> 5}))