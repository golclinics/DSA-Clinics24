#include <stdio.h>
char *power_of_two(int n);
/**
 * main - Entry point of the function
 * Return: Always 0(success)
 */
int main(void)
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    (power_of_two(n) == "True") ? printf("True\n") : printf("False\n");
    return (0);
}

/**
 * power_of_two - Program that takes an integer as input
 * @n: Integer
 * Return: true if the input is a power of two else false. 
 */

char *power_of_two(int n)
{
    while (n % 2 == 0)
    {
        n = n / 2;
        if (n == 1)
            return ("True");
    }
}