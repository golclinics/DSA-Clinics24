/*
* Solution for Entry Challenge C1: Reverse Integer
 */

package main

import (
	"fmt"
	"log"
	"strconv"
)

func reverseInt(num int) int {
	isNegative := num < 0
	if isNegative {
		// convert to a positive value
		num = num * -1
	}

	revString := ""
	str := strconv.Itoa(num) // integer to string conversion

	// loop string in reverse order
	for i := len(str) - 1; i >= 0; i-- {
		newStr := string(str[i])
		revString += newStr
	}

	// convert string back to integer
	num, err := strconv.Atoi(revString)
	if err != nil {
		log.Fatal(err)
	}

	if isNegative {
		return num * -1
	}

	return num
}

func main() {
	num := 91
	result := reverseInt(num)

	fmt.Printf("value1: %v, type: %T\n", num, num)
	fmt.Printf("value2: %v, type: %T\n", result, result)
}
