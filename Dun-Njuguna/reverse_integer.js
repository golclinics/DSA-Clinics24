function reverseInteger(num) {
    let reversedString = Math.abs(num).toString().split('').reverse().join('');
    let reversedNumber = parseInt(reversedString);
    return num < 0 ? -reversedNumber : reversedNumber;
}


function runTests() {
    console.assert(reverseInteger(500) === 5, 'Test Case 1 Failed');
    console.assert(reverseInteger(-56) === -65, 'Test Case 2 Failed');
    console.assert(reverseInteger(-90) === -9, 'Test Case 3 Failed');
    console.assert(reverseInteger(91) === 19, 'Test Case 4 Failed');
    console.assert(reverseInteger(0) === 0, 'Test Case 5 Failed');
    console.assert(reverseInteger(123) === 321, 'Test Case 6 Failed');
    console.assert(reverseInteger(-123) === -321, 'Test Case 7 Failed');
    
    console.log("All test cases passed!");
}

runTests();
