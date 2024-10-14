#include <stdio.h>

/**
  * fizzbuzz - a program that prints the numbers from 1 to 100. 
  * For multiples of 3, print Fizz; for
  * multiples of 5, print Buzz; and for numbers that are multiples of  * both 3 and 5, print FizzBuzz
  * return: 0
  */
int main(void)
{
    int i = 0;

    for (i = 1; i <= 100; i++)
    {
        if ((i % 3 == 0) && (i % 5 == 0))
        {
            printf("FizzBuzz");
        }
        else if ((i % 3) == 0)
        {
            printf("Fizz");
        }
        else if ((i % 5) == 0)
        {
            printf("Buzz");
        }
        else
        {
            printf("%d", i);
            if (i == 100)
            {
                printf("\n");
            }
        }
        printf(" ");
    }
    return (0);
}
