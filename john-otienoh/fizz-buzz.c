#include <stdio.h>
/**
 * main - Entry point of the function
 * Program that prints the numbers from 1 to 100. 
 * For multiples of 3, print Fizz; 
 * For multiples of 5, print Buzz; 
 * For numbers that are multiples of both 3 and 5, print FizzBuzz.
 * Return: Always 0(success)
 */
int main(void)
{
    int i;

    for (i = 1; i <= 100; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
            printf(" Fizzbuzz");
        else if (i % 3 == 0)
            printf(" Fizz");
        else if (i % 5 == 0)
            printf(" Buzz");
        else
            printf(" %d", i);
    }
    printf("\n");
    return (0);
} 