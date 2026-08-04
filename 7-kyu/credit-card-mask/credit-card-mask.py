# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    masked_count = len(cc)-4
    return '#' * masked_count + cc[-4 :]
​