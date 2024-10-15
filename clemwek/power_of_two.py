def power_of_two(n):
    return bin(n).count('1') == 1

print(power_of_two(10)) # false
print(power_of_two(16)) # true
