import math

def power_of_two(n):
    try:
        n = int(n)  
        if n <= 0:
            return False
        
        log_value = math.log(n, 2)
        return log_value.is_integer()  # True if log2(n) is an integer
    except ValueError:
        # If input cannot be converted to an integer
        print("Invalid!: Please enter an integer.")
        return False

user_input = input("Enter an integer: ")
if power_of_two(user_input):
    print("returns True")
else:
    print("returns False")

