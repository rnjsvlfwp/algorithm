numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_bunja(array):
    length = len(array)
    if length == 1:
        return 1
    return length * get_bunja(array[0:-1])


def get_bunmo(number):
    if number == 1:
        return 1
    return number * get_bunmo(number - 1)


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    array_length = len(array)
    result = get_bunja(array) / (get_bunmo(target) * get_bunmo(array_length - target))

    return result


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))
