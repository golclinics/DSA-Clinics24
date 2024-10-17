function isPowerOfTwo(int) {
  if (int <= 0) return false;

  while (int % 2 === 0) {
    int = int / 2;
  }
  return int === 1;
}

console.log(isPowerOfTwo(8)); // true
console.log(isPowerOfTwo(6)); // false
