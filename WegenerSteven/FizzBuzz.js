/*challenge 2
Write a program that prints the numbers from 1 to 100. 
For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; 
and for numbers that are multiples of both 3 and 5, print "FizzBuzz".*/

//the program below will print numbers from 1 to 100, following the FizzBuzz rules.
for(n=1; n<=100; n++){
    //prints 'FizzBuzz if the number is a multiple of both 3 and 5.
    if (n % 3 === 0 && n % 5 === 0) {
        console.log("FizzBuzz");
    } 
    //prints 'Fizz' if the number is a multiple of 3.
    else if (n % 3 === 0) {
        console.log("Fizz");
    } 
    //prints 'Buzz if the number is a multiple of 5.
    else if (n % 5 === 0) {
        console.log("Buzz");
    } 
    //returns number that is neither a multiple of 3 nor 5.
    else {
        console.log(n);
    }
}