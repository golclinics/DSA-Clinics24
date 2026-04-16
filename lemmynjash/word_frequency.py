def word_frequency(sentence):
    words=sentence.split()
    word_count={}
    
    word_found=[]
    word_not_found=[]
    
    for i in words:
        if i not in word_found:
           word_found.append(i)
        else:
            word_not_found.append(i)

        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1
    
    print(word_found)
    print(word_not_found)
    print(word_count)
    
    #then i want to put them in a dictionary
    {'data':3}
text ="data engineer data pyton sql data sql s sql data"
word_frequency(text)