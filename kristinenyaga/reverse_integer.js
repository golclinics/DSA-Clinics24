const reverseInteger = (num) => {
  
  const isNegative = num < 0;
  const reversedNumber = parseInt(num.toString().split('').reverse().join(''));
  return isNegative ? -reversedNumber : reversedNumber;

};

console.log(reverseInteger(500));
console.log(reverseInteger(-56));
console.log(reverseInteger(-90));
console.log(reverseInteger(91));