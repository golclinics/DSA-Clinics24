/**
 * power_of_two - checks whether an integer is a power of 2
 *
 * @n: integer to test
 *
 * Return: 0 False, 1 True
 */
int power_of_two(int n)
{
	if (n == 0)
		return (0);

	return ((n & (n - 1)) == 0);
}
