alphabet_array = "hello my name is sparta"

print(alphabet_array.replace(' ', ''))


def search_the_most_showed_alphabet(array):
    list_all = [0] * 26

    new_array = array.replace(' ', '')

    for a_num in new_array:
        index = ord(a_num) - ord('a')
        list_all[index] += 1

    max_num = list_all[0]
    for comp_num in list_all:
        if max_num < comp_num:
            max_num = comp_num

    else:
        return chr(list_all.index(max_num) + ord('a'))


result = search_the_most_showed_alphabet(alphabet_array)
print(result)
