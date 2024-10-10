def reverse_number(x):
    if x < 0:
        reversed_num = -int(str(-x)[::-1])
    else:
        reversed_num = int(str(x)[::-1])
    return reversed_num

x = int(input("Enter the number: "))

rev = reverse_number(x)

print("Reversed number:", rev)
