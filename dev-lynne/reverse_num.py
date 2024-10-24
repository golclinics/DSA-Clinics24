def reverseNum():
    num = int(input("Enter a number: "))
    numStr = str(num)

    if num < 0:
        revNumStr = '-' + numStr[:0:-1]
    else:
        revNumStr = numStr[::-1]

    return int(revNumStr)

revNum = reverseNum()
print(f"Reversed number:  {revNum}")