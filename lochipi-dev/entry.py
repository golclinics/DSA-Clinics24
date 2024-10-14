"""
2^^n

num = x

case 1; x > 0

2 ^^ 0 => 1
2 ^^ 1 => 2
2 ^^ 2 => 4
2 ^^ 3 => 8

1 -> 2 -> 4 -> 8

skip = x * 2
"""
# Time and space
# O(1) - comparison, O(1) bitwise operation -> avetage O(1) time complexity
# space complexity is O(1)O(1).

def is_power_of_two(num):
     return num > 0 and (num & (num - 1)) == 0 
                        # 1000 - 0111 = 0
                        #  8 -     7

# # Input from the user
# number = int(input("Enter an integer: "))

# # Output whether the number is a power of two
# if is_power_of_two(number):
#     print(f"{number} is a power of two.")
# else:
#     print(f"{number} is not a power of two.")