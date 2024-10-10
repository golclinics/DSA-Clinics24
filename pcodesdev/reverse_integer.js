
function reverseDigits(num) { 
    // Check if num is null or undefined
    if (num === null || num === undefined) {
        throw new Error('num cannot be null or undefined');
    }

    // Convert the number into a string
    const numString = num.toString();

    // Split the string into an array of characters
    const numArray = numString.split('');

    // Reverse the array
    const reversedNumArray = numArray.reverse();

    // Join the array of characters back into a string
    const reversedNumString = reversedNumArray.join('');

    // Parse the reversed string back into a number
    const reversedNum = parseInt(reversedNumString);

    // Multiply the reversed number by the sign of the original number 
    // to get the complete reversed number
    const result = reversedNum * Math.sign(num);

    return result;
}

// Test the function
const num = 1234
console.log(reverseDigits(num))
const num2 = -1234
console.log(reverseDigits(num2))