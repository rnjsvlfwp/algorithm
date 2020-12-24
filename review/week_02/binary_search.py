number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
target_number = 14


def binary_search(array, target):
    max_num = array[-1]
    min_num = array[0]
    guess_num = (max_num + min_num) // 2

    count = 0
    while max_num >= min_num:
        count += 1
        if guess_num < target_number:
            min_num = guess_num

        elif guess_num > target_number:
            max_num = guess_num

        else:
            return count
        guess_num = (max_num + min_num) // 2


result = binary_search(number_array, target_number)
print(True, result)
