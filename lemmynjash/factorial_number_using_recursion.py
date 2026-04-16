def myfactorial(n):
    if n == 0:
        return 1
    else:
        return n * myfactorial(n - 1)


print(myfactorial(5))
x=int(input('Enter a number you want to find factorial value:'))
result = myfactorial(x)
print(f"The factorial of {x} is {result}")