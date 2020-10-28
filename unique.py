def unique_char(input_str):
    char_list = []
    for char in input_str:
        if char.isalpha() and char not in char_list:
            char_list.append(char)
    return char_list