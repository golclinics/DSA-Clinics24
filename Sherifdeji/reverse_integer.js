function reverseDigit(num) {
  if (num < 0) {
    let split = num.toString().split("");
    const partToReverse = split.slice(1);

    const joinPartToReverse = partToReverse.reverse().join("");

    split.splice(1, partToReverse.length, ...joinPartToReverse);

    let r = split.join("");
    return parseInt(r);
  } else {
    const split = num.toString().split("").reverse().join("");
    return parseInt(split);
  }
}

module.exports = reverseDigit;
