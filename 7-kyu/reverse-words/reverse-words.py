def reverse_words(text):
    result = []
    new_text = text.split(" ")
    for i in new_text:
        result.append(i[::-1])
        
    return " ".join(result)
​
    