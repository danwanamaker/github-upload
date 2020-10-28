def contains_duplicate(input_str):
    input_str = input_str.lower()
    is_duplicate = False
    for char in input_str:
        if input_str.count(char) > 1:
            is_duplicate = True
    return is_duplicate
