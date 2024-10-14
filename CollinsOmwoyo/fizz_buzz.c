#include <stdio.h>

/**
 * main - Prints numbers from 1 to 100 with special cases for multiples of 3 and 5.
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
    for (int i = 1; i <= 100; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
            printf("FizzBuzz");
        else if (i % 3 == 0)
            printf("Fizz");
        else if (i % 5 == 0)
            printf("Buzz");
        else
            printf("%d", i);

        if (i < 100)
            printf(" ");  // Print space between outputs except after the last one.
    }
    printf("\n");
    return 0;
}
