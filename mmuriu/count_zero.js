// Function to reverse the digits of the input number
function reverseDigits() {
    const input = document.getElementById("numberInput").value; // Get the input value
    const number = parseInt(input); // Parse the input to an integer

    // Check if the input is a valid number
    if (isNaN(number)) {
        document.getElementById("result").textContent = "Please enter a valid number."; // Error message for invalid input
    } else {
        const isNegative = number < 0; // Check if the number is negative
        const reversedStr = Math.abs(number).toString().split('').reverse().join(''); // Reverse the digits
        const reversedNumber = isNegative ? -parseInt(reversedStr) : parseInt(reversedStr); // Preserve the sign
        document.getElementById("result").textContent = `Reversed: ${reversedNumber}`; // Display the result
    }
}

// Add event listener to the button
document.getElementById("submitButton").addEventListener("click", reverseDigits);
