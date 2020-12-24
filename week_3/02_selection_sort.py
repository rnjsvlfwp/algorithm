input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)

    for i in range(n - 1):  # i = 0 / i = 1
        for j in range(i + 1, n):  # j = 1,2,3,4
            min_num = array[i]  # min_num = 4
            if min_num > array[j]:  # 4 < 4 -> false
                min_num = array[j]  # j=4, min_num = 1
                array[i], array[j] = array[j], array[i]  # array = [1,6,2,9,4]

    return array


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
