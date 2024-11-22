#include <stdio.h>
#include <stdbool.h>

// Function to check if a number is a power of 2
bool isPowerOfTwo(unsigned int n) {
        return (n > 0) && ((n & (n - 1)) == 0);
}

int main() {
	unsigned int num;

	num = 8;
	
    	printf("%u => %s\n", num, isPowerOfTwo(num) ? "true" : "false");

	num = 6;
	printf("%u => %s\n", num, isPowerOfTwo(num) ? "true" : "false");
	return 0;
}

