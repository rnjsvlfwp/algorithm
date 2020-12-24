input_array = [3, 5, 6, 1, 2, 4]


def find_max_number(array):
    for a_num in array:
        for a_comp_num in array:
            if a_num < a_comp_num:
                break
        else:
            return a_num


result = find_max_number(input_array)
print(result)
