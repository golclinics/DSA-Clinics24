#include <stdio.h>
#include <iostream>

using namespace std;

bool isPowerOfTwo(int n) {
    if (n == 1) {
        return true;
    }
    if (n <= 0 || n % 2 != 0) {
        return false;
    }
    return isPowerOfTwo(n / 2);
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    cout << isPowerOfTwo(8);
    cout << isPowerOfTwo(6);

    return 0;
}
