def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    count = 0
    for i in range(begin_number, end_number + 1, step):
        count += i
    return count