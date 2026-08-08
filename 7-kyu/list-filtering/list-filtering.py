def filter_list(l):
    result = []
    for item in l:
        if type(item) is int:
            result.append(item)
            
    return result
    