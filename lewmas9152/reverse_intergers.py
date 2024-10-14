a = input("Enter an interger: ")

def is_number(s):
    return s.lstrip('-').isdigit() and s.count('-') and s.index('-') == 0 if '-' in s else s.isdigit()

def reversing(b):
   reverse =list(reversed(b))
   if reverse.count("-") > 0 :
      reverse.pop() 
      reverse[0] = "-" + reverse[0]
   reversed_num  = "".join(map(str,reverse))
   print(int(reversed_num))

if is_number(a):
   reversing(a)
   
else:
    print(0)

