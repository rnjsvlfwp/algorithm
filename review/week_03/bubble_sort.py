input_array = [4, 6, 2, 9, 1]


def sort_array(array):
    array_length = len(array)

    for i in range(array_length):
        for j in range(1, array_length - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]

    return array


result = sort_array(input_array)
print(result)
