// Declaration of an empty array
const results = [];

// loop through 1 to 100
for (let i = 1; i <= 100; i++) {
     // Check if there is a number that is multiple of both 3 and 5 and return FizzBuzz
    if (i % 5 === 0 && i % 3 === 0) {
        results.push("FizzBuzz");
    }
    // Check if there is a number that is multiple of 3 and return Fizz
    else if (i % 3 === 0) {
        results.push("Fizz");
    }
    // Check if there is a number that is multiple of 5 and return Buzz
    else if (i % 5 === 0) {
        results.push("Buzz");
    }
    // Return the number if it is not a multple of 3 and 5 
    else {
        results.push(i);
    }
}

console.log(results);
