input = [3, 5, 6, 1, 2, 4]


def find_max(array):

    max_val = input[0]
    for a_num in input:
        if max_val < a_num:
            max_val = a_num
        else:
            max_val = max_val

    return max_val


result = find_max(input)
print(result)
