#write a program to find a number that is prime or not prime.
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input('enter a number:'))
if is_prime(n):
    print(f'given number {n} is prime')
else:
    print(f'given number {n} is not prime')