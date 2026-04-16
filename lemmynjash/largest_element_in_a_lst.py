def largest_element(lst):
    print(lst)
    lst.sort(reverse=True)

    print(lst[0])
    
    max = lst[0]
    for i in lst:
        if i>max:
            max=i
    print(f'the max is {max}')
    
array = [10, 5, 8, 20, 3,9,6,32,26,60,60,20,32,20,90,26,20,40,90]
largest_element(array)