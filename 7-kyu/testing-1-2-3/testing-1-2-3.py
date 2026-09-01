def number(lines):
    if not lines:
        return []
    res = []
    for i, line in enumerate(lines, start = 1):
        res.append(f"{i}: {line}")
    
    return res