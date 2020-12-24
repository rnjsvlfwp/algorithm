list_array = [0, 3, 5, 6, 1, 2, 4]


def select_plus_or_minus_for_max_number(array):
    result = array[0]

    for index in range(1, len(array)):
        if result * array[index] > result + array[index]:
            result *= array[index]
        elif result * array[index] < result + array[index]:
            result += array[index]

    return result


max_num = select_plus_or_minus_for_max_number(list_array)
print(max_num)
