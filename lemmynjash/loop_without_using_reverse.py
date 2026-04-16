def loop(lst):
    final_lst=[]
    for i in range(len(lst) -1,-1,-1):
        final_lst.append(lst[i])
    
    print(final_lst)


    for i in range(len(lst) -1,-1,-1):
        final_lst.append(lst[i])

array = [10, 5, 8, 20, 3,9,6,32,26]
largest_squared_number = loop(array)


