for n in range(1, 101):

    if n % 3 == 0 and n % 5 == 0:
        print('fizzbuzz', end=' ')

    elif n % 3 == 0:
        print('fizz', end=' ')

    elif n % 5 == 0:
        print('buzz', end=' ')

    else:
        print(n, end=' ')


