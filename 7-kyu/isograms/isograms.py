def is_isogram(string):
    string = string.lower()
    already_seen = []
    
    for letter in string:
        if letter in already_seen:
            return False
        already_seen.append(letter)
        
    return True
​
​