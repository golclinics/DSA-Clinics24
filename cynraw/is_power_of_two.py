def is_power_of_two():

    num = int(input("Enter a number you wish to test: "))

    if num <= 0:
        return False

    while(num % 2) == 0:
        num = num // 2

    return num == 1


print(is_power_of_two())
