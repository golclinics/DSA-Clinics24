def FizzBuzz(n):
    outcomes = []
    for i in range(1, n):
        if i%3 == 0 and i%5 ==0:
            outcomes.append("FizzBuzz")
        elif i%3 == 0:
            outcomes.append("Fizz")
        elif i%5 == 0:
            outcomes.append("Buzz")
        else:
            outcomes.append(str(i))

    return outcomes

result = FizzBuzz(101)
for res in result:
      print(res)