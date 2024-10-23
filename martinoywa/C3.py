from math import log2


def power_of_two(n):
    # edge case
    if n <= 0:
        return False
    return log2(n) == int(log2(n))


if __name__ == "__main__":
    print(f"-1 => {power_of_two(-1)}")
    print(f"0 => {power_of_two(0)}")
    print(f"8 => {power_of_two(8)}")
    print(f"6 => {power_of_two(6)}")
