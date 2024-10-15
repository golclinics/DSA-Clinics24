#include <stdio.h>
#include <stdlib.h>

int reverse_integer(int n);
/**
 * main - Entry point of the function
 * Program that takes an integer as input and return/prints  an integer with reversed digit ordering.
 * Return: Always 0(success)
 */
int main(void)
{
    int n, reversed_num = 0;
    printf("Enter Digit: ");
    scanf("%d", &n);

    if (n < 0)
        reversed_num = reverse_integer(abs(n)) * -1;
    else
        reversed_num = reverse_integer(n);

    printf("The reverse is %d\n", reversed_num);
}

/**
 * reverse_integer - Program that takes an integer as input and return/prints  an integer with reversed digit ordering.
 * @n: The integer to be reversed
 * Return: The reversed integer
 */
int reverse_integer(int n)
{
    int reverse = 0;
    while (n > 0)
    { 
        reverse = reverse * 10 + n % 10;
        n /= 10;
    }
    return (reverse);
}
