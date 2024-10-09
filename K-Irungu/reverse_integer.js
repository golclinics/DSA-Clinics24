// Reverse Integer

// Write a program that takes an integer as input and return an integer 
// with a reversed digit ordering.

// For example:

// For input 500, the program should return 5. 
// For input -56, the program should return -65. 
// For input -90, the program should return -9. 
// For input 91, the program should return 19. 


function reverseInteger(num) {
    // Check if number is negative
    const isNegative = num < 0;
    // Convert the number to a string, remove the negative sign if present, and reverse it
    const reversedStr = Math.abs(num).toString().split('').reverse().join('');
    // Convert the reversed string back to an integer
    let reversedInt = parseInt(reversedStr);
    
    // If the original number was negative, return the negative reversed integer
    return isNegative ? -reversedInt : reversedInt;
}

// Test cases
console.log(reverseInteger(500));  // Output: 5
console.log(reverseInteger(-56));   // Output: -65
console.log(reverseInteger(-90));   // Output: -9
console.log(reverseInteger(91));    // Output: 19
