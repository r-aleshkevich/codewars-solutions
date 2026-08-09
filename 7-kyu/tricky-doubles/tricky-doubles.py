def tricky_doubles(num):
    s = str(num)
    length = len(s)
    
    if length % 2 != 0:
        return num * 2
    center = length // 2
    if s[:center] == s[center:]:
        return num
    else:
        return num * 2