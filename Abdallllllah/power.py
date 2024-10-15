def power(n):
    return n & n-1 == 0


print (power(4)) # True
print (power(5)) # False