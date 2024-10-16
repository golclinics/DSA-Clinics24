def main():
	for i in range(1,101):
		is_multiple_of_three = i % 3 == 0
		is_multiple_of_five = i % 5 == 0
		if is_multiple_of_three and is_multiple_of_five:
			print("FizzBuzz")
		elif is_multiple_of_three:
			print("Fizz")
		elif is_multiple_of_five:
			print("Buzz")
		else:
			print(i)

if __name__ == '__main__':
	main()