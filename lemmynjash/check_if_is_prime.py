def check_if_is_prime(num):
    if num < 1:
        return "its not a prime"
    
    div=num % 2 
    print(div)
    if div == 0:
        print("its dividble by 2 and not prime")
    else:
        print("its prime")
check_if_is_prime(10)