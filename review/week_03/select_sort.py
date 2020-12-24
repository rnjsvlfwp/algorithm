input_array = [4, 6, 2, 9, 1]


def select_sort_array(array):
    array_length = len(array)

    for i in range(array_length - 1):
        min_index = i
        for j in range(array_length - i):
            if array[min_index] > array[i+j]:
                min_index = i+j

        array[i], array[min_index] = array[min_index], array[i]


select_sort_array(input_array)
print(input_array)
