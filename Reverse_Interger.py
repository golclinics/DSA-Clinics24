# Function to reverse the interger
def reverse_Interger(num):
    # Handle negative numbers by creating a variable sign
    sign= -1 if num<0 else 1
    reversed_num=int(str(abs(num))[::-1])
    reversed_num=int(reversed_num)
    return sign * reversed_num
print("Enter an interger")
number= int(input())
print(reverse_Interger(number))
