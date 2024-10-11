function isPowerOfTwo(n) {
    if (n <= 0) {
        return false;
    }
    
    // Check if the number is a power of two using bit manipulation
    return (n & (n - 1)) === 0;
}

// Test cases
console.log(isPowerOfTwo(8));  // true
console.log(isPowerOfTwo(6));  // false

//Run in browser or node to test the code