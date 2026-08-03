def accum(st):
    result = []
    count = 1
    
    for char in st:
        repeated = char * count
        
        formatted = repeated.capitalize()
        
        result.append(formatted)
        
        count += 1
        
    return "-".join(result)