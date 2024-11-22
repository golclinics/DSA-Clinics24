/**
 * Reverses the digits of an integer.
 * @param {number} num - The integer to be reversed.
 * @returns {number} - The reversed integer, or 0 if the result is out of 32-bit signed integer range.
 */
const reverseInteger = (num) => {
    // Convert the number to a string, split into characters, reverse, and join back into a string
    const reversedStr = num.toString().split('').reverse().join('');
    
    // Convert the reversed string back to an integer and apply the original sign
    const reversedInt = parseInt(reversedStr) * Math.sign(num);
    
    // Define the 32-bit signed integer range
    const INT32_MIN = -0x80000000; // -2147483648
    const INT32_MAX = 0x7fffffff;  // 2147483647
    
    // Check if the reversed integer is within the 32-bit signed integer range
    if (reversedInt < INT32_MIN || reversedInt > INT32_MAX) {
        return 0;
    }
    
    return reversedInt;
};

// Test cases
console.log(reverseInteger(500));
console.log(reverseInteger(-56));
console.log(reverseInteger(-90));
console.log(reverseInteger(91));