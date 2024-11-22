// Define the main function for FizzBuzz
function fizzBuzz() {
    // Loop through numbers from 1 to 100
    for (let i = 1; i <= 100; i++) {
        // Initialize a boolean to track if the number is divisible by 3 or 5
        let isFizz = false;
        let isBuzz = false;
        
        // Check if the current number is divisible by 3
        if (i % 3 === 0) {
            isFizz = true; // Set isFizz to true if divisible by 3
        }
        
        // Check if the current number is divisible by 5
        if (i % 5 === 0) {
            isBuzz = true; // Set isBuzz to true if divisible by 5
        }
        
        // If the number is divisible by both 3 and 5, print 'FizzBuzz'
        if (isFizz && isBuzz) {
            console.log("FizzBuzz");
        }
        // If the number is only divisible by 3, print 'Fizz'
        else if (isFizz) {
            console.log("Fizz");
        }
        // If the number is only divisible by 5, print 'Buzz'
        else if (isBuzz) {
            console.log("Buzz");
        }
        // If the number is not divisible by either, print the number itself
        else {
            console.log(i);
        }
    }
}

// Call the fizzBuzz function to execute
fizzBuzz();
