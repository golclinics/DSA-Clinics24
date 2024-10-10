package main


import 	"strconv"


func ReverseInteger(num int) (int, error) {
	// Check if number is negative
	negated := num < 0

	// String conversion
	stringed := strconv.Itoa(num)

	// Strip negation sign
	if negated {
		stringed = stringed[1:]
	}

	runes := []rune(stringed)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	reversedString := string(runes)
	reversedInt, err := strconv.Atoi(reversedString)
	if err != nil {
		return 0, err
	}

	// Restore negation sign
	if negated {
		reversedInt = -reversedInt
	}

	return reversedInt, nil
}