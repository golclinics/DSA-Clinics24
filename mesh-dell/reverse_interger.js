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

function testReverseInterger() {
  console.log(reverseInteger(500) == 5 ? "Test Passed" : "Test Failed");
  console.log(reverseInteger(-56) == -65 ? "Test Passed" : "Test Failed");
  console.log(reverseInteger(-90) == -9 ? "Test Passed" : "Test Failed");
  console.log(reverseInteger(91) == 19 ? "Test Passed" : "Test Failed");
}

testReverseInterger();
