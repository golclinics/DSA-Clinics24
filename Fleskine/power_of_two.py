def isPowerOfTwo(n: int = None) -> bool:
    if n == None:
        return "Input(n) can't be empty."
    if not isinstance(n, (int)) or n < 1:
        return "Input(n) must be a positive integer."
    return n & (n - 1) == 0
    
print(isPowerOfTwo())
print(isPowerOfTwo(6))
print(isPowerOfTwo(8))
print(isPowerOfTwo(1048))
