def solve(s):
    upper_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
    if upper_count > len(s) / 2:
        return s.upper()
    else:
        return s.lower()