from collections import Counter

input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    a_num = 0
    simplified_array = []

    for index in range(len(string)):
        a_num = int(string[index])
        simplified_array_range = len(simplified_array)

        if index == 0:
            simplified_array.append(a_num)

        else:
            if simplified_array[simplified_array_range - 1] == a_num:
                continue
            else:
                simplified_array.append(a_num)

    temp_result = Counter(simplified_array)

    array_sorted = []
    for value in temp_result.values():
        array_sorted.append(value)
        array_sorted.sort()

    return array_sorted

result = find_count_to_turn_out_to_all_zero_or_all_one(input)[0]
print(result)
