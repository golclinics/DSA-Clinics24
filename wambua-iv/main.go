package main

import "fmt"

func main () {
	fmt.Println("Identify multiple of 3 and 5 with FizzBuzz")
	FizzBuzz(100)
	
	fmt.Println("/-------------------------------------------------/")
	
	//tests for the poweroftwo func
	fmt.Println("Check if number is a power of two")
	PowerOfTwo(8)
	PowerOfTwo(6)
	
	fmt.Println("/-------------------------------------------------/")

	reversed := []int {500, -56, -90, 91}
	
	fmt.Println("Integer Reversal")
	for i := 0; i < len(reversed); i++ {
		reversal, _ := ReverseInteger(reversed[i])
		fmt.Println(reversal)
	}
}