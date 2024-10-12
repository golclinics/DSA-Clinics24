def is_power_of_two(n: int) -> bool:
    # A number is a power of two if it's greater than 0 and only has one bit set in binary representation.
    return n > 0 and (n & (n - 1)) == 0

# Accepting input from the user
try:
    n = int(input("Enter an integer: "))
    if is_power_of_two(n):
        print(f"{n} is a power of two.")
    else:
        print(f"{n} is not a power of two.")
except ValueError:
    print("Please enter a valid integer.")

#explanation 
#it is an optimized code using the bitwise AND operation that is n&(n-1) operating in o(1) best case with a condition n>0.