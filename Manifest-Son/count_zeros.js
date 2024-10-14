// Writing a program that takes an integer as input and return an integer with reversed digit ordering.
function reverseInterger(num){
    let reversed = 0;
    let remainder = Math.abs(num);
    // Math.abs() is used to convert negative numbers to positive

    while(remainder > 0){
        reversed = (reversed * 10) + (remainder % 10);
        remainder = Math.floor(remainder / 10);
    } 

    // While loop is used to reverse the number
    return num < 0 ? -reversed : reversed;
}

console.log(reverseInterger(123));
