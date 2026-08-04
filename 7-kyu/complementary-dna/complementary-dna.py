def DNA_strand(dna):
    pairs = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
    
    result = ""
    for letter in dna:
        result += pairs[letter]
        
    return result