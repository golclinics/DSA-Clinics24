const reversed = (num) => {
  let reversedNum = 0;

  while (num > 0) {
    const lastDigit = num % 10;
    reversedNum = reversedNum * 10 + lastDigit;
    num = Math.floor(num / 10);
  }

  return reversedNum;
};

console.log(reversed(0));
console.log(reversed(500));
console.log(reversed(123456));
