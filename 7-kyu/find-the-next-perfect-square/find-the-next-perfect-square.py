import math
def find_next_square(sq):
    root = math.sqrt(sq)
    if root.is_integer():
        return int((root + 1) ** 2)
    else:
        return -1
    
​
    
​