function reverseInteger(num) {
    // convert the number to a string, reverse the characters, and convert it back to a number
    const reversedNum = parseInt(num.toString().split('').reverse().join(''));
    // if the number is negative, make the reversed number negative
    return num < 0 ? -reversedNum : reversedNum;
}

// test cases
console.log(reverseInteger(500)); // return 5 
console.log(reverseInteger(-56)); // returns -65
console.log(reverseInteger(-90)); // returns -9
console.log(reverseInteger(91)); // returns 19
