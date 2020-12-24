alphabet_array = "abvbabae"


def the_least_showed_first_alphabet(array):
    alphabet_list = [0] * 26

    for a_alphabet in array:
        index = ord(a_alphabet) - ord("a")
        alphabet_list[index] += 1
    print(alphabet_list)

    for a_alphabet in array:
        search_index = ord(a_alphabet) - ord("a")
        least_showed = alphabet_list[search_index]
        if least_showed == 1:
            return chr(search_index + ord("a"))
    else:
        return "_"


result = the_least_showed_first_alphabet(alphabet_array)
print(result)  # v가 반환되어야 함
