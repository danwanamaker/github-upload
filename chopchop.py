def chop_string(input_str, substring):
    output_str = ''
    if substring not in input_str:
        output_str = input_str
    else:
        while True:
            slice_start = input_str.find(substring)
            slice_end = slice_start + len(substring)
            output_str += input_str[:slice_start]
            input_str = input_str[slice_end:]
            if substring not in input_str:
                output_str += input_str
                break
    return output_str