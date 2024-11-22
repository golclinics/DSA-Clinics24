def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

print(is_power_of_two(8))  
print(is_power_of_two(6))  