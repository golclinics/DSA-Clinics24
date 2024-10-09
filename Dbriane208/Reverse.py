def reverseNum(num: int) -> int:
    # Check if the input number is negative
    is_negative = num < 0

    # Reverse the absolute value of the number
    reversed_num = int(str(abs(num))[::-1])

    # Reverse the original number if negative
    if is_negative:
        reversed_num = -reversed_num

    return reversed_num

print(reverseNum(-345))
print(reverseNum(500))
print(reverseNum(-90))
print(reverseNum(91))