function isPowerOfTwo(n) {
    if (n <= 0) return false;
    return (n & (n - 1)) === 0;
}
//test case
console.log(isPowerOfTwo(8));  // true
console.log(isPowerOfTwo(6));  // false
