import { createInterface } from 'readline';

const rl = createInterface({
    input: process.stdin,
    output: process.stdout
  });
const reverseInteger = () => {
    rl.question('Please enter a number: ', (input) => {
        const number = Number(input);
        
        if (isNaN(number)) {
          console.log('Invalid input. Please enter a valid number.');
        } else {
        const stringifiedInput = number.toFixed(0)

    
    const inputLength = stringifiedInput.length

    const reversedString = []
    let reversedNumber = Number
    let counter = inputLength


    if(inputLength == 1) {
         

    } else {
        while(counter > 0) {
          reversedString.push(stringifiedInput[counter-1])
          if(reversedString[0] == "0") {
            reversedString.shift()
        }
          counter -= 1
        }
           
    }

    const reversedStringLength = reversedString.length

    if(reversedString[reversedStringLength-1] == "-") {
        negativeSign = reversedString.pop()
        reversedString.unshift(negativeSign)
    }
    reversedNumber = Number(reversedString.join(''))
    
    console.log(reversedNumber)
    return reversedNumber

    }
    rl.close();
});
    
}
reverseInteger()