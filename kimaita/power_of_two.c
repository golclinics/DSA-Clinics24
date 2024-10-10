/**
 * power_of_two - checks whether an integer is a power of 2
 *
 * @n: integer to test
 *
 * Return: 0 False, non-ze ro True
 */
int power_of_two(int n)
{
    return (n == 0) ? 0 : (n & (n - 1)) == 0;
}
