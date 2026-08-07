def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    vertical_balance = walk.count('n') == walk.count('s')
    horizontal_balance = walk.count('w') == walk.count('e')
    
    return vertical_balance and horizontal_balance