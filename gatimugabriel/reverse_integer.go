package gatimugabriel

import "math"

func Reverse(x int) int {
	// sign multiplier; 1 for positive numbers and -1 for negative numbers
	sign := 1
	if x < 0 {
		sign = -1
		x *= sign
	}

	var finalNumber int

	for x > 0 {
		lastDigit := x % 10 //  extract last digit from original number

		// Check for overflow before doing the multiplication
		if finalNumber > math.MaxInt32/10 || finalNumber < math.MinInt32/10 {
			return 0
		}

		finalNumber = (finalNumber * 10) + lastDigit // add the digit to finalNumber
		x = x / 10                                   // pop last digit from original number
	}

	return finalNumber * sign
}
