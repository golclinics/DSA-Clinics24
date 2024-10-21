package linked

import "fmt"

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head *Node
}

//insertion into linked list

func (list *LinkedList) insertAtEnd(data int) {
	//creating a new node
	newNode := &Node{data: data, next: nil}

	if list.head == nil {
		//if the head node is nil the new node becomes the head
		list.head = newNode
	}

	//if the haed is not empty iterate to find the last node by followung the
	// next node until it reaches a nil value
	currentNode := list.head
	for currentNode.next != nil {
		currentNode = currentNode.next
	}

	currentNode.next = newNode
}

//insert at the start of the linked list

func (list *LinkedList) InsertAtBeginning(data int) {
	if list.head == nil {
		//if the head node is nil the new node becomes the head
		newNode := &Node{data: data, next: nil}
		list.head = newNode
	}
	//if list is not empty => create new node with provided data
	// update and sets the next pointer to the head
	newNode := &Node{data: data, next: list.head}
	list.head = newNode
}

//insert after Node Value
//insert a new node after first occurence of provided value

func (list *LinkedList) InsertAfterValue(afterValue, data int) {
	//create new node with the provide data
	newNode := &Node{data: data, next: nil}

	currentNode := list.head

	for currentNode != nil {
		if currentNode.data == afterValue {
			//connecting the new node by updating the next pointers
			newNode.next = currentNode.next
			currentNode.next = newNode
		}

		fmt.Printf("Cannot insert node after value %d doesn't exist", afterValue)
	}
}

//insert before a value

func (list *LinkedList) insertBeforeValue(beforeValue, data int) {
	if list.head == nil {
		//no node to be returned
		return
	}

	// if the current node value matches the beforeValue
	// create a new node and set next pointer to the current head insertBeforeValue
	if list.head.data == beforeValue {
		newNode := &Node{data: data, next: list.head}
		list.head = newNode
	}

	//iterate through the node to find value equal to the before insertBeforeValue
	// create new node and point the next value to the current value next
	currentValue := list.head
	for currentValue.next != nil {
		if currentValue.next.data == beforeValue {
			newNode := &Node{data: data, next: currentValue.next}
			currentValue.next = newNode
		}
		currentValue = currentValue.next
	}
	fmt.Printf("Cannot find insert node, before value %d doesn't exist", beforeValue)
}

//delete values from the beginning

func (list *LinkedList) DeleteAtBeginning() {
	if list.head != nil {
		list.head = list.head.next
		fmt.Println("Head of current node has been delated")
	}
}

// delete value at the end
func (list *LinkedList) DeleteAtEnd() {
	if list.head == nil {
		fmt.Println("Linked list is empty")
	}

	if list.head.next == nil {
		list.head = nil
		fmt.Println("Last node of the list has been deleted")
	}

	var current *Node = list.head
	for current.next.next != nil {
		current = current.next
	}
	current.next = nil
	fmt.Println("last node of the linked list has been deleted")
}

func (list *LinkedList) DeleteAfterValue(afterValue int) {
	if list.head == nil {
		fmt.Println("Linked list is enpty")
	}

	var currentNode *Node = list.head

	for currentNode != nil && currentNode.data != afterValue {
		currentNode = currentNode.next
	}

	if currentNode == nil {
		fmt.Printf("node with value %d doesn't exist", afterValue)
	}

	if currentNode.next == nil {
		fmt.Printf("node with value %d is the last node", afterValue)
	}

	var toBeDeleted *Node = currentNode.next
	fmt.Printf("Node with value %d, after the node %d has been deleted", toBeDeleted.data, afterValue)
	currentNode.next = currentNode.next.next
}

// Delete before a value
func (list *LinkedList) DeleteBeforeValue(beforeValue int) {
	currentNode := list.head
	var previousNode *Node

	if currentNode == nil || currentNode.next == nil {
		fmt.Printf("Node with value %d doesn't exist", beforeValue)
	}

	for currentNode.next != nil {
		if currentNode.next.data == beforeValue {
			if previousNode == nil {
				fmt.Printf("Node before value %d will be deleted", beforeValue)
				list.head = currentNode.next
			} else {
				var toBeDeleted *Node = currentNode
				fmt.Printf("Node before value %d with value %d has been deleted", beforeValue, toBeDeleted.data)
				previousNode.next = currentNode.next
			}
		}
		previousNode = currentNode
		currentNode = currentNode.next
	}
	fmt.Printf("Node before value %d not found", beforeValue)
}

func (list *LinkedList) CountNodes() (count int) {
	currentNode := list.head
	for currentNode != nil {
		currentNode = currentNode.next
		count++
	}
	return
}

//search for a node

func (list *LinkedList) SearchNodeAt(index int) *Node {
	count := 0
	currentNode := list.head

	for currentNode != nil {
		count++
		currentNode = currentNode.next
	}

	if index <= 0 || index > count {
		return nil
	}
	currentNode = list.head
	for count = 1; count < index; count++ {
		currentNode = currentNode.next
	}
	return currentNode
}

func (list *LinkedList) Reverse() {
	currentNode := list.head
	var previousNode *Node

	for currentNode != nil {
		nextNode := currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	}
	fmt.Println()
	for previousNode != nil {
		fmt.Printf("%d -> ", previousNode.data)
		previousNode = previousNode.next
	}
}

//print out node

func (list *LinkedList) PrintOut() {
	currentNode := list.head
	for currentNode != nil {
		fmt.Printf("%d -> ", currentNode.data)
		currentNode = currentNode.next
	}

}
