def powerOfTwo(num):
    return num & num-1 == 0

#test
print(powerOfTwo(8))
print(powerOfTwo(7))