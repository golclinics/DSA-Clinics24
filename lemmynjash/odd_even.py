def oddeven(nums):
    odd=[]
    even=[]
    
    for i in nums:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    odd_sum=sum(odd)
    even_sum=sum(even)
    
    print(odd_sum)
    print(even_sum)