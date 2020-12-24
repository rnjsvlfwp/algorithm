input_array = [4, 6, 2, 9, 1, 11, 31, 0]


def select_sort_array(array):
    array_length = len(array)
    for i in range(1, array_length):
        for j in range(i):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]


select_sort_array(input_array)
print(input_array)
