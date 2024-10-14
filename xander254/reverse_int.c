#include <stdio.h>

/**
  * reverse integer - A function that reverses the integer it input
  * @a: the integer to be reversed
  * Return: reversed integer
  */
int reverse_integer(int a)
{
        int revarr = 0;
        
        while (a != 0)
        {
            revarr = revarr *10 + (a % 10);
            a = a / 10;
        }   
        return (revarr);
}
int main()
{
    int num = 0;

    /*input*/
    printf("Enter an integer\n");
    scanf("%d", &num);


    /*reversed*/
    int result = reverse_integer(num);
    printf("The reversed value is: %d\n", result);

    return 0;
}
