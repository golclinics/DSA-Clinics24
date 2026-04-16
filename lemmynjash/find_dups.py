def find_dups(lst):
    no_dupes=[]
    yes_dupes=[]
    for i in lst:
        if i in no_dupes:
            if i not in yes_dupes:
                yes_dupes.append(i)
        else:
            no_dupes.append(i)
    
    print(f"no dupes --- {no_dupes}")
    print(f'yes dupes ----> {yes_dupes}')
    
    dict={}
    for i in lst:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
    
    return no_dupes

array = [10, 5, 8, 20, 3,9,6,32,26,60,60,20,32,20,90,26,20,40,90]
find_dups(array)
