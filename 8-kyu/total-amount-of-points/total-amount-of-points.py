def points(games):
    count = 0
    for match in games:
        x = int(match[0])
        y = int(match[2])
        
        if x > y:
            count += 3
        elif x == y:
            count += 1
            
    return count
​
​