def find_squared_largest(num):
    largest=num[0]
    for i in num:
        if i > largest:
            largest=i
    return largest**2

array = [10, 5, 8, 20, 3,9,6,32,26]
largest_squared_number = find_squared_largest(array)
print(f"The largest squared number in the list is {largest_squared_number}")