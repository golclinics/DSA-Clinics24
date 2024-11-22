function isPowerOfTwo(n){
  if(n <= 0 ){
    return false   
  }
    //bitwise operation to check if n is power of two using bitwise AND   
  return (n & (n-1)) === 0
}

console.log(isPowerOfTwo(4))    //return true
console.log(isPowerOfTwo(6))    //return false
console.log(isPowerOfTwo(8))    //returns true
