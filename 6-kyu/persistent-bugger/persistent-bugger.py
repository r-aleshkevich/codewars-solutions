def persistence(n):
    count = 0
    while n >= 10:
        count += 1
        prod = 1
        for i in str(n):
            prod *= int(i)
            n = prod
    return count
            