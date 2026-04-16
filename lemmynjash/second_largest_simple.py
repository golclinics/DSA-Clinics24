def second_largest_simple(lst):
    list2 = list(set(lst))
    list2.sort(reverse=True)
    print(list2)
    return list2[1] if len(list2) > 1 else None

array = [2,-5,-9,-3,8,-96,-25,-36,-45]
res = second_largest_simple(array)
print(f"The second-largest number is: {res}")