def second_largest_negative(lst):
    neg_no=[]
    for i in lst:
        if i<0:
            neg_no.append(i)
    remove_neg_lst=list(set(neg_no))
    print(remove_neg_lst)
    remove_neg_lst.sort(reverse=True)
    print(remove_neg_lst)
    return remove_neg_lst[1]

numbers = [3, -5, -28, 7, -81, 4, -16]
result = second_largest_negative(numbers)
print(f"The second-largest negative number is: {result}")