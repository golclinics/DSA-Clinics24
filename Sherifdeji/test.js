// ```
// Write a program that takes an integer as input and return an integer with reversed digit ordering.

// For example

// For input 500, the program should return 5.
// For input -56, the program should return -65.
// For input -90, the program should return -9.
// For input 91, the program should return 19.

// ```;

// test-reverseDigit.js
const reverseDigit = require("./reverse_integer"); // Adjust the path accordingly

function runTest(description, input, expectedOutput) {
  const result = reverseDigit(input);
  if (result === expectedOutput) {
    console.log(`✅ ${description}`);
  } else {
    console.error(`❌ ${description}`);
    console.error(`   Expected: ${expectedOutput}, but got: ${result}`);
  }
}

// Test cases
runTest("should return 5 for input 500", 500, 5);
runTest("should return -65 for input -56", -56, -65);
runTest("should return -9 for input -90", -90, -9);
runTest("should return 19 for input 91", 91, 19);
