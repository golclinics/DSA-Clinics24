def remove_dupes(lst):
    print(set(lst))

    no_dupes=[]
    yes_dupes=[]
    for i in lst:
        if i not in no_dupes:
            if i not in yes_dupes:
                no_dupes.append(i)
        else:
            yes_dupes.append(i)
    print(yes_dupes)
    print(no_dupes)

array = [10, 5, 8, 20, 3,9,6,32,26,60,60,20,32,20,90,26,20,40,90]
remove_dupes(array)