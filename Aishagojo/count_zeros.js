 // Write a program that takes an integer as input and return an integer with reversed digit
 // ordering.

const readline = require('readline');


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function reverseInteger(n) {
    let reversed = 0;
    let num = Math.abs(n);

    
    while (num > 0) {
        reversed = reversed * 10 + (num % 10);
        num = Math.floor(num / 10);
    }

    
    return n < 0 ? -reversed : reversed;
}


rl.question("Enter an integer: ", (input) => {
    const num = parseInt(input, 10);
    const result = reverseInteger(num);
    console.log("Reversed integer:", result);
    rl.close(); 
});
