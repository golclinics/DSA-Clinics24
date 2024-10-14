def power_of_two(num):
    return True if (num > 0 and (num & (num - 1)) == 0) else False

nums = [2,0,5,16,31,1,64]

if __name__ == "__main__":
    for i in range(len(nums)):
        print(f"{nums[i]} is a power of two: {power_of_two(nums[i])}")