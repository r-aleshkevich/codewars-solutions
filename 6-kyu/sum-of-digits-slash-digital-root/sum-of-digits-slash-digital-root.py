def digital_root(n):
    while n >= 10:
        current_sum = 0
        for digit in str(n):
            current_sum += int(digit)
            n = current_sum
            
    return n