def check_missing_nos_from1_to_n(lst):
    the_missing_n=[]
    for i in range(1,7):
        if i not in lst:
            the_missing_n.append(i)
    print(the_missing_n)

def reverse_the_str(senctence):
    words=senctence.split()
    
    words.reverse()

    final_string=""
    for i in words:
        final_string=final_string+" "+i
    print(final_string)


def anagram_words():
    
    s1="listen"
    s2="silent"
    
    print(sorted(s1) == sorted(s2))
    
    for i in s1:
        if i in s2:
            continue
        
        elif i not in s2:
            return False
    
    return True  
    

def palindrome_word(word):
    reversed_word=word[::-1]
    if word ==reversed_word:
        return True
    else:
        return False
    

def combine_2_list(lst1,lst2):
    final_list=list(zip(lst1,lst2))
    print(final_list)

names = ["Alice", "Bob", "Charlie"]


def remove_duplicates(lst):
    print(set(lst))

# ages = [25, 30, 35,35,35,60,60]


# remove_duplicates(ages)


def sort_array_without_inbuilt(lst):
   unsorted=lst.copy()
   
   sorted_lsit=[]
   
   print(f"Starting with: {unsorted}")

   while len(unsorted) >0:
        small=unsorted[0]
        
        for num in unsorted:
            if num < small:
                small = num
        
        unsorted.remove(small)
        
        sorted_lsit.append(small)
        
        print(f"Found {small}, remaining: {unsorted}, sorted so far: {sorted_lsit}")
   return sorted_lsit

# ages = [25, 30, 12425,10000,35,35,60,60]
# print(sort_array_without_inbuilt(ages))
# print(combine_2_list(names,ages)) 
# print(palindrome_word("racecar"))
# print(anagram_words())
 
sentence="hey i kinda felt i am not comftable"
# reverse_the_str(sentence)

array=[1,3,5,3,7]
# check_missing_nos_from1_to_n(array)

def average_movie_ratings():
    movie_ratings = {
    "Inception": [5, 2, 1, 4, 5],
    "Interstellar": [4, 4, 5, 4, 5],
    "Tenet": [3, 3, 4, 2, 4]
    }
    
    d={}
    
    for key,value in movie_ratings.items():
        item_len=len(value)
        the_total_amount=0
        for num in value:
            the_total_amount+=num

        the_average=the_total_amount/item_len
        
        d[key]=the_average
        
        print(d)
# average_movie_ratings()

def again_reverse_without_inbuilt():
    lst =[2000,129921,21821,102,38,742]
    a=[]
    for i in range(len(lst)-1,-1,-1):
        a.append(lst[i])
    
    print(a)

# again_reverse_without_inbuilt()   

def find_dupes():
    lst=[10,1,10,90,9,9,10,28,89,9,10,9,89,1212121]
    
    lst_dupes=[]
    lst_not_dupes=[]
    
    for i in lst:
        if i not in lst_not_dupes:
            lst_not_dupes.append(i)
        
        elif i not in lst_dupes:
            lst_dupes.append(i)
    
    print(f'not dupes ----> {lst_not_dupes}')
    print(f'are dupes ---> {lst_dupes}')

    d={}
    for i in lst:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(f'find dupes ---> {d}')
# find_dupes()

def largest_elements():
    lst=[10,1,10,90,9,9,10,28,89,9,10,9,89,1212121]
    
    lst.sort(reverse=True)
    
    print(lst[0])
    
    max=lst[0]
    
    for i in lst:
        if i > max:
            max=i
    
    print(max)

largest_elements()

def count_word_freq():
    sentence="hey hey i love the way way you you love me me test me if you could me "
    words=sentence.split()
    d={}
    for i in words:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    print(d)

# count_word_freq()

def reverse_a_string():
    sentence="hey hey i love the way way you you love me me test me if you could me "
    words=sentence.split()
    
    rev_words=""
    for i in words:
        rev_words=i+" "+rev_words
    
    print(rev_words)

# reverse_a_string()

def check_if_prime_or_not():
    lst=[10,1,10,90,9,9,10,28,89,9,10,9,89,1212121]
    
    prme=""
    for i in lst:
        if i < 1:
            return
        
        if i % 2 == 0:
            prme="This is even "+str(i)
            print(prme)
        elif i % 2 == 1:
            prme="This is not even its odd "+str(i)
            print(prme)
            
    
    n =6   
    for i in range(2, n):
        if n%i == 1:
            prme="This is prime "+str(i)
            print(prme)
        
        if n%i == 0:
            prme="This is not prime "+str(i)
            print(prme)
        
check_if_prime_or_not()

def factorial(n):
    print(n)
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(5))