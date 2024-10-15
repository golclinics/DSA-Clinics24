#include <stdio.h>

const char* isPowerOfTwo(int n) {
    if (n < 1) {
        return "false";
    }
    if (n & (n - 1)) {
        return "false";
    }
    return "true";
}

int main() {
    printf("%s\n", isPowerOfTwo(8));
    printf("%s\n", isPowerOfTwo(4));
    printf("%s\n", isPowerOfTwo(14));
    return 0;

}