//Using in built method split , revers and join
const ReverseNumber = (num) => {
  //convert to str and reverse

  let reversedStr = Math.abs(num).toString().split("").reverse().join("");

  //convert to integer
  let reversedNo = parseInt(reversedStr);

  //check if the original number was negative if yes use ternary operator to compare

  return num < 0 ? -reversedNo : reversedNo;
};

console.log(ReverseNumber(500));
console.log(ReverseNumber(-56));
console.log(ReverseNumber(-90));
console.log(ReverseNumber(91));

//Remove the need of using in built methods

const ReverseNumber2 = (num) => {
  let reversedNo = 0;
  let isNegative = false;

  if (num < 0) {
    isNegative = true;
    //Handle negative numbers
    num = Math.abs(num);
  }

  while (num > 0) {
    reversedNo = reversedNo * 10 + (num % 10);
    num = Math.floor(num / 10);
  }

  return isNegative ? -reversedNo : reversedNo;
};

console.log(ReverseNumber2(500));
console.log(ReverseNumber2(-56));
console.log(ReverseNumber2(-90));
console.log(ReverseNumber2(91));
