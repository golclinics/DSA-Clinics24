def find_factorial_of_no(num):
    if num < 0:
        return 'Not defined'
    result = 1
    for i in range(1, num+1):
        result=result*i
        print(result)
        
array = 5
find_factorial_of_no(array)