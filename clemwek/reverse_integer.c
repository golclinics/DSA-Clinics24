#include <stdio.h>

//  This is a program that takes an integer and returns a reversed integer

int reverse_integer(int x) {
    int reversed = 0;
    int remainder = 0;

    while (x != 0) {
        remainder = x % 10;
        reversed = reversed * 10 + remainder;
        x = x / 10;
    }
    return reversed;
}

int main() {
    printf("%d \n", reverse_integer(123));
    printf("%d \n", reverse_integer(500));
    printf("%d \n", reverse_integer(-90));
    printf("%d \n", reverse_integer(-56));
    printf("%d \n", reverse_integer(91));
}