def fizzbuzz():
    for i in range(1, 101):
        # if the number is a multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # if it is a multiple of 3
        elif i % 3 == 0:
            print("Fizz")
        # if it is a multiple of 5
        elif i % 5 == 0:
            print("Buzz")
        # else print the number
        else:
            print(i)

# Run the fizzbuzz function
fizzbuzz()
