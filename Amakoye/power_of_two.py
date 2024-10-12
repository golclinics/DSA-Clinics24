def isPowerOfTwo(n):
    if n == 1:
        return True

    if n == 0 or n % 2 != 0:
        return False
    return isPowerOfTwo(n // 2)


print(isPowerOfTwo(6))
