function reverseInteger(num) {
    // Determine the sign
    const sign = num < 0 ? -1 : 1;
    
    // Convert to positive number and then to string
    let numStr = Math.abs(num).toString();
    
    // Reverse the string
    let reversedStr = numStr.split('').reverse().join('');
    
    // Convert back to number and apply the sign
    return sign * parseInt(reversedStr, 10);
}

// // Test cases
// const testCases = [500, -56, -90, 91];

// testCases.forEach(testCase => {
//     const result = reverseInteger(testCase);
//     console.log(`Input: ${testCase}, Output: ${result}`);
// });

// Input from User
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Enter a number: ', num => {
    const result = reverseInteger(parseInt(num, 10));
    console.log(`Reversed number: ${result}`);
    readline.close();
});