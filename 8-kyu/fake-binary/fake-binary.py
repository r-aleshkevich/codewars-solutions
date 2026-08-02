def fake_bin(x):
    result = ""
    for b in x:
        if int(b)  < 5:
            result += "0"
        elif int(b) >= 5:
            result += "1"
    return result