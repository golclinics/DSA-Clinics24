def reverse_integer(int_num):
    is_negative = int_num < 0
    
    if is_negative:
        result = int(str(abs(int_num))[::-1]) * -1  
    else:
        result = int(str(int_num)[::-1])  
    return result

    
if __name__ == "__main__":
    print(f"For input 500, result is {reverse_integer(500)}.") #should return 5. 
    print(f"For input -56, result is {reverse_integer(-56)}.") #should return -65. 
    print(f"For input -90, result is {reverse_integer(-90)}.") #should return -9. 
    print(f"For input 91, result is {reverse_integer(91)}.") #should return 19. 
