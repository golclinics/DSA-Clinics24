/*prints the numbers from 1 to 100. For multiples of 3, print Fizz; for
multiples of 5, print Buzz; and for numbers that are multiples of both 3 and 5, print FizzBuzz*/

//iterates between the range 1 to 100
for (let i = 1; i < 101; i++) {
  if (i % 5 === 0 && i % 3 === 0) {
    //checks if the current number is a multiple of 3 and 5
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    //checks if the current number is a multiple of 3
    console.log("Fizz");
  } else if (i % 5 === 0) {
    //checks if the current number is a multiple of 5
    console.log("Buzz");
  } //the current number is printed out if its not a multiple of 3 or 5
  else console.log(i);
}
