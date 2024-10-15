function isPowerOfTwo(n) {
    if (n <= 0) {
        return false;
    }
    return (n & (n - 1)) === 0;
}
// examples
console.log(isPowerOfTwo(8));  
console.log(isPowerOfTwo(6)); 
console.log(isPowerOfTwo(10)); 
console.log(isPowerOfTwo(5)); 
console.log(isPowerOfTwo(7)); 
