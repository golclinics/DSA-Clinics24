def is_pow_of_2(i):
    if i <= 0:
        return False
    return (i & (i-1)) == 0

num = int(input("Enter a number: "))
print(is_pow_of_2(num))