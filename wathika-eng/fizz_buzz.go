// Package main will solve the FizzBuzz problem
package main

import "fmt"

func Fizz() {
	// a loop which runs from 0 to 100
	for a := 0; a <= 100; a++ {
		// if a is divisible by both 3 and 5, print fizzbuzz
		if a%3 == 0 && a%5 == 0 {
			fmt.Printf("FizzBuzz\n")
		} else if a%3 == 0 { // if a is divisible by 3 only, print Fizz
			fmt.Printf("Fizz\n")
		} else if a%5 == 0 { // if a is divisible by 5 only, print Buzz
			fmt.Printf("Buzz\n")
		} else { // if not divisible by either 3 or 5, just print the value
			fmt.Printf("%v\n", a)
		}
	}
}

func main() {
	Fizz()
}
