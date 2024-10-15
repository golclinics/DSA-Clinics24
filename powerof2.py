def power_of_two(num):
    
 assert num > 0 and int(num)==num

num = int(input("Enter number: "))

if (num & (num - 1)) == 0:
    print("True")
else:
    print("False")
    