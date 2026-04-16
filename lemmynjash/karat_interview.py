'''
We are building a word processor and we would like to implement a "word-wrap" functionality.

Given a list of words followed by a maximum number of characters in a line, return a collection of strings where each string element represents a line that contains as many words as possible, with the words in each line being concatenated with a single '-' (representing a space, but easier to see for testing). The length of each string must not exceed the maximum character length per line.

Your function should take in the maximum characters per line and return a data structure representing all lines in the indicated max length.

Examples:

words1 = [ "The", "day", "began", "as", "still", "as", "the",
          "night", "abruptly", "lighted", "with", "brilliant",
          "flame" ]

wrapLines(words1, 13) "wrap words1 to line length 13" =>

tem_words
loop

if suffix has -
then add temp_words
else
first_item+-
add temp_words

return temp_words


 [ "The-day-began",
    "as-still-as",
    "the-night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]
 

wrapLines(words1, 12) "wrap words1 to line length 12" =>

  [ "The-day",
    "began-as",
    "still-as-the",
    "night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]    


wrapLines(words1, 20) "wrap words1 to line length 20" =>

  [ "The-day-began-as",
    "still-as-the-night",
    "abruptly-lighted",
    "with-brilliant-flame" ]

words2 = [ "Hello" ]

wrapLines(words2, 5) "wrap words2 to line length 5" =>

  [ "Hello" ]


wrapLines(words2, 30) "wrap words2 to line length 30" =>

  [ "Hello" ]  

words3 = [ "Hello", "Hello" ]

wrapLines(words3, 5) "wrap words3 to line length 5" =>

  [ "Hello",
  "Hello" ]

words4 = ["Well", "Hello", "world" ]

wrapLines(words4, 5) "wrap words4 to line length 5" =>

  [ "Well",
  "Hello",
  "world" ]

words5 = ["Hello", "HelloWorld", "Hello", "Hello"]

wrapLines(words5, 20) "wrap words 5 to line length 20 =>

  [ "Hello-HelloWorld",
    "Hello-Hello" ]


words6 = [ "a", "b", "c", "d" ]
wrapLines(words6, 20) "wrap words 6 to line length 20 =>

  [ "a-b-c-d" ]

words6 = [ "a", "b", "c", "d" ]
wrapLines(words6, 4) "wrap words 6 to line length 4 =>

  [ "a-b",
    "c-d" ]

wrapLines(words6, 1) "wrap words 6 to line length 1 =>

  [ "a",
    "b",
    "c",
    "d" ]

All Test Cases:
          words,  max line length
wrapLines(words1, 13)
wrapLines(words1, 12)
wrapLines(words1, 20)
wrapLines(words2, 5)
wrapLines(words2, 30)
wrapLines(words3, 5)
wrapLines(words4, 5)
wrapLines(words5, 20)
wrapLines(words6, 20)
wrapLines(words6, 4)
wrapLines(words6, 1)

n = number of words OR total characters

'''
words1 = ["The","day","began","as","still","as","the","night","abruptly","lighted","with","brilliant","flame"]
words2 = ["Hello"]
words3 = ["Hello", "Hello"]
words4 = ["Well", "Hello", "world"]
words5 = ["Hello", "HelloWorld", "Hello", "Hello"]
words6 = ["a", "b", "c", "d"]

# Note: built-in functions like the Python textwrap module should not be used as solutions to this problem.

#step write a function wrapLines
#pass list and the length 
#the length passed list
#splitting the list word
#looping through the list
# concate nate them using the -
#deefine list cvariable to add
#returning the list

print("Hello")
def wrapLines(words1, maxLen):
    
    print(maxLen)
    results = []
    current_line = []
    current_len = 0
    
    for word in words1:
        print(word)
        hyphen_len= 1 if current_line else 0
        print(f'hyphen_len --> {hyphen_len}')
        if current_len + hyphen_len + len(word) <= maxLen:
            current_line.append(word)
            current_len += hyphen_len+ len(word)
        else:
            results.append("-".join(current_line))
            current_line = [word]
            current_len = len(word)
    
    if current_line:
        results.append("-".join(current_line))
            
    return results

print(wrapLines(words1, 13))
# print(wrapLines(words1, 12))
# print(wrapLines(words1, 20))
# print(wrapLines(words2, 5))
# print(wrapLines(words2, 30))
# print(wrapLines(words3, 5))
# print(wrapLines(words4, 5))
# print(wrapLines(words5, 20))
# print(wrapLines(words6, 20))
# print(wrapLines(words6, 4))
# print(wrapLines(words6, 1))