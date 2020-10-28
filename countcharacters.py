"""
2: Write a function count_chars, that accepts a string S and a list of characters A as parameter.
    Then returns a list with the count of these characters in the string.[Ignore cases]
"""

def count_chars(input_str, char_list):
    count_list = []
    for char in char_list:
        if char in input_str:
            count_list.append(input_str.count(char))
    return count_list