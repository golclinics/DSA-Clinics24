# Define the function to check if a number is a power of two
#Power of Two.  Write a program that takes an integer as input and returns true if the input is a power of two. Examples:

#8=> returns true
#6=> returns false

def is_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1

#Interaction with user
print("Hey there:) ! Type any number, and we'll tell you if it's a power of two or not:")

# Prompt the user to  input a value
while True:
    try:
        user_input = int(input("Go on, type in your number: "))
        break
    except ValueError:
        print("Oops,Invalid input. Please enter a whole number.")

# Check if the input is a power of two and give user feedback!
if is_power_of_two(user_input):
    print(f"True, {user_input} is a power of two!")
else:
    print(f"False,  {user_input} is not a power of two. Another try?")

