def main():
    print(reverseInt(500))
    print(reverseInt(-56))
    print(reverseInt(-90))
    print(reverseInt(91))


def reverseInt(num):
    string = str(num)
    result = ""
    minus = 0
    for i in range(len(string) - 1, -1, -1):
        if string[i] == "-":
            minus = 1
        else:
            result += string[i]
    if minus == 1:
        result = "-" + result
    return int(result)


if __name__ == "__main__":
    main()
