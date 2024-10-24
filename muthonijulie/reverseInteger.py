def reverseInteger(num):
    reverse=0#initialize to zero
    sign=-1 if num<0 else 1#determine the sign of the integer
    num=abs(num)#change it to absolute

    while num>0:
        reverse=reverse*10+num%10#multiply the reverse number by 10 and add it to the remainder of the number
        num=num//10#divide the number

    return sign*reverse

num=int(input("Enter integer:"))#input obtained as string
print(f"The reversed integer is:{reverseInteger(num)}")

#at first i was getting an error when i tried to reverse a negative integer because i had not introduced the sign variable 
#after introducing the sign variable i then assigned the number to an absolute number so that i can work with a positive integer