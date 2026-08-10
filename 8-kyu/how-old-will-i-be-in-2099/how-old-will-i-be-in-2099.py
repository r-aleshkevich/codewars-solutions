def calculate_age(year_of_birth, current_year):
    year = current_year - year_of_birth
​
    if year > 1:
        return f"You are {year} years old."
    if year == 1:
        return f"You are {year} year old."
    if current_year == year_of_birth:
        return "You were born this very year!"
    if year == -1:
        return f"You will be born in {-year} year."
    if year < -1:
        return f"You will be born in {-year} years."