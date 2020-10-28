def strip_str(raw_str):
    cond_str = ''
    for char in raw_str:    # Appends alpha characters in the raw string to the condensed string.
        if char.isalpha():
            cond_str += char.lower()
    return cond_str


def is_specialsub(big_str, small_str):
    big_cond = strip_str(big_str)   # Removes spaces, punctuation, etc from each string.
    small_cond = strip_str(small_str)
    if small_cond in big_cond:
        return True
    else:
        return False
