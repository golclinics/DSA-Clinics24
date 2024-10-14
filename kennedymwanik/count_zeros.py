def power_of_two(num):
    if num < 0:
        return False
    return (num & (num - 1)) == 0

print(power_of_two(8))  
print(power_of_two(7)) 
print(power_of_two(16))  
print(power_of_two(1)) 