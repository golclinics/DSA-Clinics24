# This program checks whether a number between 1 and 100 is divisible by either 3 or 5


# Create a function to wrap all the logic together for possible reuse with different ranges.

def fizz_buzz(n):
    
    result = []  # Store the expected result in a value
    
    for i in range(1, n + 1):  # Define the range. The value n means that the function can be altered for any necessary range. The for loop checks all entities in the range.
        
        # Initialize the output as empty and implement the divisibility tests for 3 and 5 
        
        output = ""  
        
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        
        # If output is still empty, the number isn't divisible by 3 or 5
        
        if not output:
            output = str(i)
        
        result.append(output)  # Add the output to the result variable
    
    return result

# Example of calling the function for numbers 1 to 100

output = fizz_buzz(100)  # The value 100 is passed a n to the fizz_buzz function. 

for value in output:
    print(value)   # Print all values in the output/result
