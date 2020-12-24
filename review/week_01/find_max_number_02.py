input_array = [3, 5, 6, 1, 2, 4]


def find_max_number(array):
    max_number = array[0]

    for a_num in array:
        if a_num > max_number:
            max_number = a_num
    return max_number

result = find_max_number(input_array)
print(result)
