def power_of_two(x):
 
 if x <= 0:
    return False
 return (x & (x - 1)) == 0

integer = int(input("Enter integer: "))

if power_of_two(integer):
  print(f"{integer} True. ")
else:
 print(f"{integer} False. ")
