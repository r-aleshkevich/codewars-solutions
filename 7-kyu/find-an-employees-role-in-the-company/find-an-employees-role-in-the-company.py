def find_employees_role(name):
    parts = name.split()
    if len(parts) < 2:
        return "Does not work here!"
    first = parts[0]
    last = parts[1]
    for person in employees:
        if person["first_name"] == first and person["last_name"] == last:
            return person["role"]
    return "Does not work here!"