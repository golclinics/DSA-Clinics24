// ```
// Power of Two
// Write a program that takes an integer as input and returns true if the input is a power of two.

// Examples:

// 8=> returns true 
// 6=> returns false

// ```;

const powerOfTwo = (num) => {
  if (num === 1) return true;
  if (num % 2 !== 0) return false;
  return powerOfTwo(num / 2);
};

console.log(powerOfTwo(8)); // true
console.log(powerOfTwo(6)); // false

// FizzBuzz
function fizzBuzz(){
  for(let i= 1; i<= 100; i++){
    if(i % 3 === 1 && i % 5 === 0){
      console.log("FizzBuzz")
    }else if(i % 3 == 0){
      console.log("Fizz")
    } else if(i % 5 == 0){
      console.log("Buzz")
    }

  }
}

fizzBuzz();