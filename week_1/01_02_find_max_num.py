input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]

    for comp_num in array:

        if comp_num <= max_num:
            max_num = max_num
        else:
            max_num = comp_num
    return max_num


max_num = find_max_num(input)
print(max_num)
