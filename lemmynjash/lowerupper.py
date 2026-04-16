def loweroruppercount(sentence):
    upper = 0
    lower = 0
    
    for char in sentence:           # Use 'char' (the loop variable)
        if char.isupper():           # Check if character is uppercase
            upper += 1                # Increment upper by 1 (CORRECT)
        elif char.islower():          # Check if character is lowercase
            lower += 1                # Increment lower by 1 (CORRECT)
        # Note: spaces, numbers, punctuation are ignored
    
    return upper, lower               # RETURN the values!

# Get input
input_txt = "Hi Welcome to the Wrold of Python programming"

# Call function and store returned values
upper_count, lower_count = loweroruppercount(input_txt)

# Print results
print(f"Given sentence: {input_txt}")
print(f"Uppercase characters count: {upper_count}")
print(f"Lowercase characters count: {lower_count}")