/*
Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.

Examples:

8=> returns true 
6=> returns false

*/

const isPowerOfTwo = (n: number): boolean => {
  /* A number is a power of two if it is greater than 0 and if bitwise AND of the number and (number - 1) equals 0 */
  return n > 0 && (n & (n - 1)) === 0
}

console.log(isPowerOfTwo(8)) // Output: true
console.log(isPowerOfTwo(6)) // Output: false

//to run => cd DennisRono && ts-node power_of_two.ts
