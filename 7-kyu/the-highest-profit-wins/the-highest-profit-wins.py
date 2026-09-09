def min_max(lst):
    lst.sort()
    res = []
    res.append(lst[0])
    res.append(lst[-1])
    return res
​