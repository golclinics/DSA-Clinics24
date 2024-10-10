def is_power_of_two(n):
    if n <=0:
        return False
    else:
        return  (n & (n -1)) == 0
#testing the function
num = int(input("Enter an integer: "))
print("Is power of two:", is_power_of_two(num))