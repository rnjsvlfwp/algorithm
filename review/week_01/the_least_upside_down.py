target_array = "0100110010"


def the_least_upside_down(array):
    count_one = 0
    count_zero = 0

    if array[0] == '0':
        count_zero += 1
    elif array[0] == '1':
        count_one += 1

    for index in range(len(array) - 1):
        if array[index] != array[index + 1]:
            if array[index + 1] == '1':
                count_one += 1
            elif array[index + 1] == '0':
                count_zero += 1
    return min(count_one, count_zero)


result = the_least_upside_down(target_array)
print(result)
