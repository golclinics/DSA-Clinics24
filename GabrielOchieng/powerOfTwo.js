// A program that takes an integer as input and returns true if the input is a power of two.

const isPowerOfTwo = (n) => {
  if (n <= 0) {
    return false;
  }
  while (n % 2 === 0) {
    n /= 2;
  }
  return n === 1;
};

// Test cases
console.log(isPowerOfTwo(8)); // Returns: true
console.log(isPowerOfTwo(6)); // Returns: false
