def reverse_words(sentence):
    words=sentence.split()
    print(words)
    reverse_words=reversed(words)
    final_word=' '.join(reverse_words)
    return final_word


input_sentence = "Hi welcome to the world of python programming"
result = reverse_words(input_sentence)
print(f"Given sentence: {input_sentence}")
print(f"Reversed sentence: {result}")