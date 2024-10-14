user_input = input("Insert a list of numbers separated by spaces: ")

number_list = user_input.split()

reversed_list = number_list[::-1]

print(f"Reversed list {reversed_list}")