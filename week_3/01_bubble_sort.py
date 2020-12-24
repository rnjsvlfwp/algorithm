input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    count = 0
    while count < len(array):
        for index in range(1, len(array)):
            if array[index-1] < array[index]:
                continue
            else:
                array[index-1], array[index] = array[index], array[index-1]
        count += 1
    return array


bubble_sort(input)
print(input)
