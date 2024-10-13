#include <iostream>
using namespace std;

int reverseInteger(int n) {
    int reversed = 0;
    int sign = n < 0 ? -1 : 1;
    n = abs(n);
    
    while (n > 0) {
        int digit = n % 10;
        reversed = reversed * 10 + digit;
        n /= 10;
    }
    
    return reversed * sign;
}

int main() {
    int num;
    cout << "Enter an integer: ";
    cin >> num;
    
    int reversedNum = reverseInteger(num);
    cout << "Reversed integer: " << reversedNum << endl;
    
    return 0;
}
