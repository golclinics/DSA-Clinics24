#include <stdio.h>
#include <stdlib.h>  

int reverseInteger(int n) {
    int reversed_num = 0;
    int is_negative = n < 0;  // checks if the number is negative

   
    n = abs(n); //converts to absolute value

    // Reverse the digits
    while (n > 0) {
        int last_digit = n % 10;
        reversed_num = reversed_num * 10 + last_digit;
        n /= 10;
    }

    // If the original number was negated, return the negative of reversed number
    return is_negative ? -reversed_num : reversed_num;
}

int main() {
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);

    printf("Reversed integer: %d\n", reverseInteger(n));
    return 0;
}
