

function isPowerOfTwo(n) {
    if (n <= 0) return false;
  
    while (n > 1) {
      if (n % 2 !== 0) {
        return false;
      }
      n = n / 2;
    }
  
    return true;
  }
  
  // Code examples 
  console.log(isPowerOfTwo(8)); // returns true
  console.log(isPowerOfTwo(6)); // returns false
  console.log(isPowerOfTwo(16)); // returns true
  console.log(isPowerOfTwo(0)); // returns false
  console.log(isPowerOfTwo(-1)); // returns false


  // Summary
  // The function isPowerOfTwo(n) takes in a number n and returns true if the number is a power of 2, and false otherwise. 
  // The function first checks if the number is less than or equal to 0, and if it is, it returns false.
  //  It then enters a while loop that continues as long as the number is greater than 1.
  //  In each iteration, the function checks if the number is divisible by 2. If it is not, the function returns false. 
  // If the number is divisible by 2, the function divides the number by 2 and continues to the next iteration. 
  // If the function completes the while loop without returning false, it returns true.
  