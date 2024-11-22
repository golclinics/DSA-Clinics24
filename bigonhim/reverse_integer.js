function reverseInteger(num) {
    return parseInt(num.toString().split('').reverse().join('')) * Math.sign(num);
}
const originalNumber = 543;
const reversedNumber = reverseInteger(originalNumber);
console.log(`Original: ${originalNumber}, Reversed: ${reversedNumber}`);

//explanation of the code
//Firstly change the number to a string using the .toString() then split the string to characters using .split('')
//Secondly Reverse the order of the array elements then join back the characters to a string using the .join('')
//Thirdly using the Math.sign() method we keep the original sign of the number