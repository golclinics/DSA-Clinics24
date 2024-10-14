


def is_power_two(num):

    if num <= 0:
          return False
    
    return (num & (num - 1)) == 0


if __name__ == "__main__":
    print(is_power_two(64)) # True
    print(is_power_two(70)) # False

# karemacv-cavin