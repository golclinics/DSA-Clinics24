function isPowerOfTwo(n) {
    if (n <= 0) {
        return false;
    }
    
    return (n & (n - 1)) === 0;
}


//const input = parseInt(prompt("Enter an integer: "), 10);
console.log(isPowerOfTwo(16));
