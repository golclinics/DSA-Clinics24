def fizz_buzz(n):
    # result = []

    return ["FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
        "Buzz" if num % 5 == 0 else
        "Fizz" if num % 3 == 0 else num
        for num in range(1, int(n) + 1)]

    # for num in range(1, int(n)+1):

    #     # check if a num is a multiple of both 3 nd 5
    #     if num % 3 == 0 and num % 5 == 0:
    #         result.append("FizzBuzz")

    #     # check if a num is a multple of 5
    #     elif num % 5 == 0:
    #         result.append("Buzz")

    #     # check if a num is a multiple of 3
    #     elif num % 3 == 0:
    #         result.append("Buzz")
    #     else:
    #         result.append(num)
    # return result

if __name__ == '__main__':
    n = input('Enter a number: ')
    result = fizz_buzz(n)
    print(result)