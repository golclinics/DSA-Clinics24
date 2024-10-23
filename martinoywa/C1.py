def reversed(n):
    # check if number is -
    negative = n < 0

    # convert to sting and reverse
    n_reversed = int(str(abs(n))[::-1])

    # add - if negative
    n_reversed *= (-1 if negative else 1)
    return n_reversed


if __name__ == "__main__":
    print(f"500: {reversed(500)} == 5")
    print(f"-56: {reversed(-56)} == -65")
    print(f"-90: {reversed(-90)} == -9")
    print(f"91: {reversed(91)} == 19")
