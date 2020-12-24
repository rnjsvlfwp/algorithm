array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
target_number = 14


def search_number_one_thru_n(array, target):
    count = 0
    for a_number in array:
        count += 1
        if a_number == target:
            return count


result = search_number_one_thru_n(array, target_number)
print(result)
