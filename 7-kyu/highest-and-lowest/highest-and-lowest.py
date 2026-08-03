def high_and_low(numbers):
    list_of_strings = numbers.split()
    list_of_ints = [int(x) for x in list_of_strings]
    max_num = max(list_of_ints)
    min_num = min(list_of_ints)
    
    return f"{max_num} {min_num}"