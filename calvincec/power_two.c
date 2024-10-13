#include<stdio.h>

int power2(int n);

int main(void)
{
	int no, conf;
	printf("Enter the number: ");
	scanf("%d", &no);

	conf = power2(no);
	if (conf==0)
	{
		printf("false");
	}
	else
	{
		printf("true");
	}
}

int power2(int n)
{
	if (n <= 0)
	{
		return 0;
	}

	return ((n & (n - 1)) == 0);

}