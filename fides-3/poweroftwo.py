def is_Power_Of_Two(num):
    assert num>=0 and int(num) ==num,"the number should be a positive whole integer."
    if num<=0:
        return False
    return(num&(num-1))==0
num=int(input("enter num:"))
if is_Power_Of_Two(num):
        print(f"{num}=>return true")
else:
        print(f"{num}=>return false")



    

 