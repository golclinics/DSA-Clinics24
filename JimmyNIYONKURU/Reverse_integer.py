def reverse_integer(n:int)->int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_str = str(n)[::-1]
    reversed_int = sign * int(reversed_str)

    return reversed_int

if __name__ == "__main__":
    print(reverse_integer(500))
    print(reverse_integer(-56))
    print(reverse_integer(-90))
    print(reverse_integer(91))
