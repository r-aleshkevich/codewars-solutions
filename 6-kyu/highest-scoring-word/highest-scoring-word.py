def high(x):
    words = x.split()
    max_score = -1
    best_word = ""
    for word in words:
        current_score = 0
        for char in word:
            current_score += ord(char) - 96
        if current_score > max_score:
            max_score = current_score
            best_word = word
            
    return best_word