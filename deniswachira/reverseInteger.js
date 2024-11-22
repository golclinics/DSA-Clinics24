// Entry Challenge C1
// Reverse Integer
// Write a program that takes an integer as input and return an integer with reversed digit
// ordering.

function reverseInteger(n) {
    let reversed = 0;
    let num = Math.abs(n);

    while (num > 0) {
        let lastDigit = num % 10;  
        reversed = (reversed * 10) + lastDigit;  
        num = Math.floor(num / 10);  
    }

    return reversed * Math.sign(n);  
}

// Test cases
console.log(reverseInteger(500));  
console.log(reverseInteger(-56));  
console.log(reverseInteger(-90));  
console.log(reverseInteger(91));   
