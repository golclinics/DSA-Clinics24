#Write a program to find the number of times a number 
# exists in a list. return in descending order of number of occurrences a number exists.

def count_occurrences(lst):
    d= {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return sorted_d