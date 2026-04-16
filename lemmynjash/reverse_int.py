def reverse_int(num):
    num_str=str(num)
    final_num=''
    for i in num_str:
        final_num=i+final_num
    
    print(final_num)


reverse_int(123456)