function reverseInteger(num) {
  let reversedNum = 0;
  const isNegative = num < 0;
  num = Math.abs(num);

  while (num > 0) {
    let lastDigit = num % 10;
    reversedNum = reversedNum * 10 + lastDigit;
    num = Math.floor(num / 10);
  }

  return isNegative ? -reversedNum : reversedNum;
}
