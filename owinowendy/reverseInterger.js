
function reverseInteger(num) {
    let str = num.toString();
    let isNegative = num < 0;
    let reversedStr = str.split('').reverse().join('');
    let reversedNum = parseInt(reversedStr);
    return isNegative ? -reversedNum : reversedNum;
}

console.log(reverseInteger(178234));   
console.log(reverseInteger(-78678));   
