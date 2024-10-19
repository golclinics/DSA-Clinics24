function powerOfTwo(number) {
  if (number <= 0) {
    return false;
  } else {
    while (number % 2 === 0) {
      number /= 2;
    }
    return number === 1;
  }
}
console.log(powerOfTwo(6));
console.log(powerOfTwo(8));
