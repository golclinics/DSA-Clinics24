def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n-1)) == 0

try:
    num = int(input("Enter an integer: "))
    result = is_power_of_two(num)
    print(f"{num} is a power of two: {result}")
except ValueError:
    print("Invalid input.")


