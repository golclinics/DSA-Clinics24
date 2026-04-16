def print_even(lst):
    even=[]
    for i in lst:
        div=i % 2
        #print(div)
        if i % 2 == 0:
            if i !=0:
                even.append(i)
    
    print(even)

array=[2,5,6,7,8,9,0,2,3,4,5,6,7,8,9,0]
print_even(array)