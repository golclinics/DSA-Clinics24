function reverseInteger(num) {
    let reversedNum = 0;
    let isNegative = num < 0;
  
    // Convert negative numbers to positive for the reversal process
    num = Math.abs(num);
  
    // Reverse the digits
    while (num > 0) {
      const lastDigit = num % 10;
      reversedNum = reversedNum * 10 + lastDigit;
      num = Math.floor(num / 10);
    }
  
    // Restore the negative sign if the input number was negative
    return isNegative ? -reversedNum : reversedNum;
  }
  
  // Example usage:
  const input = parseInt(-1658, 10);
  console.log(input)
  console.log(`Reversed number: ${reverseInteger(input)}`);