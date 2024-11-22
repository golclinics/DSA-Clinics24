const powerOfTwo = (num) => {
    if (num === 1) return true; 
    if (num === 0 || num % 2 !== 0) return false; 
    return powerOfTwo(num / 2); 
  };

  //testing
  let ans=powerOfTwo(98);
  let ans2=powerOfTwo(8);
  let ans3=powerOfTwo(0);
  let ans4=powerOfTwo(16);

  console.log(ans);
  console.log(ans2);
  console.log(ans3);
  console.log(ans4);

  //in this problem we are trying to find if a number is divisible by two by recurrsively dividing it by two and checking it againt the basecase one which is 2^0
  // which will return true 
  //or if it is equal to zero since zero is not a power of two or simply not divisible by two which will return false