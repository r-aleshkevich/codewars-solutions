def find_needle(haystack):
    for index, element in enumerate(haystack):
        if element == "needle":
            return f"found the needle at position {index}"
    