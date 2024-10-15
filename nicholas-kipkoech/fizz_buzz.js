/**
 * 
 *Write a program that prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
  multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz.
 */

function fizzBuzz(num) {
  for (let i = 1; i < num; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log("Fizz Buzz");
    } else if (i % 5 === 0) {
      console.log("Buzz");
    } else if (i % 3 === 0) {
      console.log("Fizz");
    } else {
      console.log(i);
    }
  }
}

console.log(fizzBuzz(100));
