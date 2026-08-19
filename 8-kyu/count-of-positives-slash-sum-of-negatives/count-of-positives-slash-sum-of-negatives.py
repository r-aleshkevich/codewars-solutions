def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pl_sum = 0
    min_sum = 0
    for i in arr:
        if i == 0:
            continue
        elif i < 0:
            min_sum += i
        else:
            pl_sum += 1
    return [pl_sum, min_sum]