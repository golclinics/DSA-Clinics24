
//Write a program that takes an integer as input and return an integer with reversed digit
//ordering.

//Code
function reverseInteger(n) {
    let negative = n < 0;
    n = Math.abs(n);
    let reversed = 0;

    while (n > 0) {
        let lastDigit = n % 10;
        reversed = reversed * 10 + lastDigit;
        n = Math.floor(n / 10);
    }

    return negative ? -reversed : reversed;
}

//Test
console.log(reverseInteger(600));    
console.log(reverseInteger(-66));     
console.log(reverseInteger(-80));    
console.log(reverseInteger(92));      
console.log(reverseInteger(0));   


//Run using node Reverse_Interger.js
