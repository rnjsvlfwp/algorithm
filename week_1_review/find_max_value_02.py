input = [3, 5, 6, 1, 2, 4]


def find_max(array):

    for a_num in array:
        for comp_num in array:
            if a_num < comp_num:
                break
        else:
            return a_num


result = find_max(input)
print(result)
