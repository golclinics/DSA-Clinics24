
'''
Reverse Integer

Approach: 
1. While a number is greater than 0, get the last digit of the number by taking the modulo of the number by 10.
2. Multiply the reversed number by 10 and add the last digit to it.
3. Divide the number by 10 to remove the last digit.
4. Repeat the above steps until the number is greater than 0.
'''

def reverse_integer(integer: int) -> int:
    reversed_number = 0
    negative = integer < 0
    integer = abs(integer)

    while integer > 0:
        last_digit = integer % 10
        reversed_number = reversed_number * 10 + last_digit
        integer = integer // 10
    if negative:
        reversed_number = -reversed_number
    return reversed_number



#? Test cases
print(reverse_integer(123))  # 321
print(reverse_integer(-3))  # -321
print(reverse_integer(0))  # 0