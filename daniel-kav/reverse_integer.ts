//  Entry Challenge C1
//  Reverse Integer
//  Write a program that takes an integer as input and return an integer with reversed digit
//  ordering.

function reverseInteger(n: number): number {
    // Check if the number is negative
    const isNegative = n < 0;

    // Work with the absolute value of the number
    n = Math.abs(n);

    // Reverse the digits by converting to a string and reversing it
    const reversedStr = n.toString().split('').reverse().join('');

    // Convert the reversed string back to a number
    let reversedInt = parseInt(reversedStr);

    // If the original number was negative, apply the negative sign
    if (isNegative) {
        reversedInt = -reversedInt;
    }

    return reversedInt;
}

// Test cases
console.log(reverseInteger(500));   // Output: 5
console.log(reverseInteger(-56));   // Output: -65
console.log(reverseInteger(-9099));   // Output: -9
console.log(reverseInteger(911));    // Output: 19
