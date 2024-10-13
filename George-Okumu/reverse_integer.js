// Write a program that takes an integer as input and return an integer with reversed digit
// ordering.

// For example

// For input 500, the program should return 5. 
// For input -56, the program should return -65. 
// For input -90, the program should return -9. 
// For input 91, the program should return 19. 

function reverse_integer(integer){
    if(!Number.isInteger(integer)) throw new Error('Value must be an integer');
    
    const check_if_int_negative = integer < 0;

    let result = Math.abs(integer).toString().split('').reverse().join('')

    return check_if_int_negative ? -result : result;
}

console.log(reverse_integer(-9010));
console.log(reverse_integer(-9));
