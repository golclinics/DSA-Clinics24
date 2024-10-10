//function to reverse a number
function reverseNum(num) {
  return (
    parseFloat(
        num
        .toString()
        .split("")
        .reverse()
        .join("")
    ) * Math.sign(num)
  );
}
//export function
module.exports = reverseNum;