/* 
Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.
*/

const fizzBuzz = () => {
    // loop from 1 to 100
    for (let i = 1; i <= 100; i++) {
        // check if number is a multiple of 3 and 5 eg 75
        // if so print FizzBuzz
        if (i % 3 === 0 && i % 5 === 0) {
            console.log("FizzBuzz");
        // check if number is a multiple of 3
        // if so print Fizz
        } else if (i % 3 === 0) {
            console.log("Fizz");
        // check if number is a multiple of 5
        // if so print Buzz
        } else if (i % 5 === 0) {
            console.log("Buzz");
        // otherwise just print the number
        } else {
            console.log(i);
        }
    }
};

fizzBuzz();