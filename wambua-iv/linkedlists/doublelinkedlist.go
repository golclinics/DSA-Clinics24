package linked

import "fmt"

type DNode struct {
	data     int
	next     *DNode
	previous *DNode
}

type DoubleLinkedList struct {
	head *DNode
	tail *DNode
}

func (list *DoubleLinkedList) InsertAtBeginning(data int) {
	newNode := &DNode{
		data:     data,
		next:     nil,
		previous: nil,
	}
	if list.head == nil {
		list.head = newNode
		list.tail = newNode
	} else {
		newNode.previous = list.tail
		list.tail.next = newNode
		list.tail = newNode
	}
}

func (list *DoubleLinkedList) InsertAtEnd(data int) {
	newNode := &DNode{data: data, next: nil, previous: nil}

	if list.head == nil {
		list.head = newNode
		list.tail = newNode
	}

	currentNode := list.head

	for currentNode.next != nil {
		currentNode = currentNode.next
	}

	newNode.previous = currentNode
	currentNode.next = newNode
	list.tail = newNode
}

func (list *DoubleLinkedList) InsertAfterValue(afterValue, data int) {
	currentNode := list.head

	for currentNode != nil {
		if currentNode.data == afterValue {
			newNode := &DNode{data: data, next: currentNode.next, previous: currentNode}
			if currentNode.next != nil {
				currentNode.next.previous = newNode
			}
			currentNode.next = newNode
			break
		}
		currentNode = currentNode.next
	}
}

func (list *DoubleLinkedList) InsertBeforeValue(beforeValue, data int) {

	if list.head == nil {
		return
	}

	if list.head.data == beforeValue {
		newNode := &DNode{data: data, next: list.head, previous: nil}
		list.head = newNode
	}

	currentNode := list.head
	for currentNode != nil {
		if currentNode.data == beforeValue {
			newNode := &DNode{data: data, next: currentNode, previous: currentNode.previous}
			if currentNode.previous != nil {
				currentNode.previous.next = newNode
			}
			currentNode.previous = newNode
			break
		}
		currentNode = currentNode.next
	}

}

func (list *DoubleLinkedList) DeleteBeforeValue(beforeValue int) {
	currentNode := list.head
	
	if currentNode == nil || currentNode.data == beforeValue {
		fmt.Printf("Node with value %d doesn't exist or is at the head \n", beforeValue)
	}
	
	for currentNode.next != nil {
		if currentNode.next.data == beforeValue {
			if currentNode.next.previous != nil && currentNode.next.previous.previous != nil {
				nodeToDelete := currentNode.next.previous
				nodeToDelete.previous.next = currentNode.next
				currentNode.next.previous = nodeToDelete.previous
			} else if currentNode.next.previous != nil {
				list.head = currentNode
				currentNode.previous = nil
			}
			return
		}
		currentNode = currentNode.next
	}
	fmt.Printf("Node with value %d is not found \n", beforeValue)
}

func (list *DoubleLinkedList) DeleteAtEnd() {
	if list.head == nil {
		fmt.Println("Double linked list is empty")
	}
	if list.head.next == nil {
		list.head = nil
	}

	var currentNode *DNode = list.head

	for currentNode.next.next != nil {
		currentNode = currentNode.next
	}
	list.tail = currentNode
	currentNode.next = nil
}

func (list *DoubleLinkedList) PrintOut() {
	currentNode := list.head

	for currentNode != nil {
		fmt.Printf("%d -> ", currentNode.data)
		currentNode = currentNode.next
	}
}

func (list *DoubleLinkedList) Reverse() {
	currentNode := list.tail

	fmt.Println()
	for currentNode != nil {
		fmt.Printf("%d -> ", currentNode.data)
		currentNode = currentNode.previous
	}
	fmt.Println()

}
