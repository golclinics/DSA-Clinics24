/**
 * P - int: Number
 * R - reverse version of the integer
 * E - 56 -> 65, -98 -> -89, 
 * **/

function reverseInteger(integer){
  const str = integer >= 0 
              ? `${integer}`.split("").reverse().join("")
              : `-${`${Math.abs(integer)}`.split("").reverse().join("")}`;

  return Number(str);
}

console.log(reverseInteger(500));
console.log(reverseInteger(-56));
console.log(reverseInteger(-90));
console.log(reverseInteger(91));
