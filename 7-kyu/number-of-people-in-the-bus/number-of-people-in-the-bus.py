def number(bus_stops):
    res = 0
    for i in bus_stops:
        result = i[0] - i[1]
        res += result
            
    return res
            