package main

import "github.com/wambua-iv/DSA-Clinics24/linkedlists"

//import "fmt"

//func main() {
// fmt.Println("Identify multiple of 3 and 5 with FizzBuzz")
// FizzBuzz(100)

// fmt.Println("/-------------------------------------------------/")

// //tests for the poweroftwo func
// fmt.Println("Check if number is a power of two")
// PowerOfTwo(8)
// PowerOfTwo(6)

// fmt.Println("/-------------------------------------------------/")

// reversed := []int{500, -56, -90, 91}

// fmt.Println("Integer Reversal")
// for i := 0; i < len(reversed); i++ {
// 	reversal, _ := ReverseInteger(reversed[i])
// 	fmt.Println(reversal)
// }

//}

func main() {
	var doubly linked.DoubleLinkedList

	doubly.InsertAtBeginning(10)
	doubly.InsertAtBeginning(57)
	doubly.InsertAtEnd(70)
	doubly.InsertAfterValue(57, 60)
	doubly.InsertBeforeValue(60, 65)
	doubly.DeleteAtEnd()
	doubly.PrintOut()
	//doubly.Reverse()
	doubly.DeleteBeforeValue(60)
	doubly.PrintOut()
}
