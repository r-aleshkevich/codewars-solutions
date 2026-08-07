import string
def is_pangram(st):
    new_st = st.lower()
    for i in string.ascii_lowercase:
        if i not in new_st:
            return False
        
    return True