function powTwo(num) {
  if (num <= 0) {
    return false;
  }
  return (num & (num - 1)) === 0;
}

var number = prompt("Enter a number: ");
number = parseInt(number, 10);

if (powTwo(number)) {
  console.log(`True: ${number} is a power of two`);
  alert(`True: ${number} is a power of two`);
} else {
  console.log(`False: ${number} is not a power of two`);
  alert(`False: ${number} is not a power of two`);
}
