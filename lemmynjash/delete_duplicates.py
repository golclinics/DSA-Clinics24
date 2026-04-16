def delete_duplicates(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
            
    return res