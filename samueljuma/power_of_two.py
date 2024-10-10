def check_if_power_of_two():

    # Take input
    num = int(input("Enter Some Number: "))

    # If the number is less than or equal to zero, it's not a power of 2
    if num <= 0:
        return False

    # Loop to repeatedly divide the number by 2 as long as it's divisible by 2
    while (num % 2) == 0:
        num = num // 2

    # If resulting number is 1, the number is a power of 2
    return num == 1


def main():
    print(check_if_power_of_two())


if __name__ == "__main__":
    main()
