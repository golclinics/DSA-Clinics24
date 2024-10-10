package main

import "fmt"

// PowerOfTwo checks if input a power of 2
func PowerOfTwo(n int) {
	if n <= 0 {
		fmt.Println(false)
	}
	fmt.Println((n & (n - 1)) == 0)
}

