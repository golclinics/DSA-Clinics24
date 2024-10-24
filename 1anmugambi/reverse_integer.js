function reverseInteger(Int) {

    //Check and return if 0-9 is the same integer
    if(Int>=0 && Int<=9) {
        return Int;
    }

    //Keep the original sign (1 for positive, -1 for negative)
    const sign = Int < 0 ? -1 : 1;
    Int = Math.abs(Int);

    let reverseInteger = 0;
    while(Int!=0){
        reverseInteger = reverseInteger * 10 + (Int % 10); // Adds the last digit
        Int = Math.floor(Int/10); // Removes the last digit
    }

    return reverseInteger * sign;
}

console.log(reverseInteger(500));
console.log(reverseInteger(-56));