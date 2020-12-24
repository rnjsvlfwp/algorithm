finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    max_num = len(array) - 1
    min_num = 0
    cur_guess = (max_num + min_num) // 2

    while cur_guess <= max_num:

        if cur_guess == target:
            return True
        elif cur_guess < target:

            min_num = cur_guess + 1
        else:
            max_num = cur_guess - 1

        cur_guess = (max_num + min_num) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
