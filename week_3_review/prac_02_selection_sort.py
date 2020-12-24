input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(i, n):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return array


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
