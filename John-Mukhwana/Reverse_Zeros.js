
function reverseInteger(num) {
    let numStr = Math.abs(num).toString();
    let reversedStr = numStr.split('').reverse().join('');
    // Convert the reversed string back to an integer
    let reversedNum = parseInt(reversedStr);
    // If the original number was negative, make the reversed number negative as well
    return num < 0 ? -reversedNum : reversedNum;
}

// Export the reverseInteger function for use in other files
module.exports = reverseInteger;

// If this file is being run directly from the command line
if (require.main === module) {
     // Import the readline module to read input from the command line
    const readline = require('readline');
        
    // Create an interface for reading input from the command line
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
// Prompt the user to enter an integer
    rl.question("Enter an integer: ", (answer) => {
         // Parse the input as an integer
        const input = parseInt(answer);
        //Reverse the integer using the reverseInteger function
        const reversed = reverseInteger(input);
        console.log(`Reversed integer: ${reversed}`);
        // Close the readline interface
        rl.close();
    });
}