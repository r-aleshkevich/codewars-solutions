def derive(coefficient, exponent): 
    new_coeff = coefficient * exponent
    new_exp = exponent - 1
    return f"{new_coeff}x^{new_exp}"
        