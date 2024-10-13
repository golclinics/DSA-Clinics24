// Write a program that takes an integer as input and return an integer with reversed digit
// ordering.

// For example

// For input 500, the program should return 5. 
// For input -56, the program should return -65. 
// For input -90, the program should return -9. 
// For input 91, the program should return 19. 

function reverse_integer(integer){
    if(!Number.isInteger(integer)) throw new Error('Value must be an integer');
    
    let reverse_int = null;

    for(let i = Math.abs(integer); i !==0 ; i = Math.floor(i / 10)){
        let digit = i % 10;
        reverse_int = reverse_int * 10 + digit;
    }

    return integer < 0 ? -reverse_int : reverse_int;
}

console.log(reverse_integer(-90000));
console.log(reverse_integer(90000));

