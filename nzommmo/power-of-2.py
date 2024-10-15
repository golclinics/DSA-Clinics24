def power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

if __name__ == "__main__":
    num = int(input("Enter a number:"))
    if power_of_two(num):
        print(f"{num} is a power of two.")
    else:
        print(f"{num} is not a power of two")