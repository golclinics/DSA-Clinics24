#include <iostream>
#include <cmath>
using namespace std;

int reverseInteger(int n) {
    int reversed = 0;
    int sign = n < 0 ? -1 : 1;
    n = abs(n);  // Take absolute value to handle negative numbers

    while (n > 0) {
        int digit = n % 10;  // Get the last digit
        reversed = reversed * 10 + digit;  // Append digit to the reversed number
        n /= 10;  // Remove the last digit
    }

    return reversed * sign;  // Apply the original sign
}

int main() {
    int num;

    // Taking input from the user
    cout << "Enter an integer: ";
    cin >> num;

    // Calling the function and printing the result
    cout << "Reversed integer: " << reverseInteger(num) << endl;

    return 0;
}
