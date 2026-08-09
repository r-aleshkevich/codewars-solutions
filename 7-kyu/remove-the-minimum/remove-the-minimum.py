def remove_smallest(numbers):
    if not numbers:
        return []
    res = numbers.copy()
    
    res.remove(min(res))
    return res
​
    
    