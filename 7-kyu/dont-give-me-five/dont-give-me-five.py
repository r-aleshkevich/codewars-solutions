def dont_give_me_five(start,end):
    res = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            res += 1
    return res