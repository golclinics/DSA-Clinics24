function isPowerOfTwo(n){
    // Check if the number is greater than 0 and if n & (n - 1) equals 0
    return n > 0 && (n & (n - 1)) === 0;
}

module.exports = isPowerOfTwo;
