array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge_sort(array1, array2):
    sorted_array = list()
    array1_index = 0
    array2_index = 0
    array1_length = len(array1)
    array2_length = len(array2)

    while array1_index < array1_length and array2_index < array2_length:
        if array1[array1_index] > array2[array2_index]:
            sorted_array.append(array2[array2_index])
            array2_index += 1

        elif array1[array1_index] < array2[array2_index]:
            sorted_array.append(array1[array1_index])
            array1_index += 1

    if array1_index == array1_length:
        while array2_index < array2_length:
            sorted_array.append(array2[array2_index])
            array2_index += 1

    elif array2_index == array2_length:
        while array1_index < array1_length:
            sorted_array.append(array1[array1_index])
            array1_index += 1

    return sorted_array


print(merge_sort(array_a, array_b))
