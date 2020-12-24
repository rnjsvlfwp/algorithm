input = "abacabade"


def find_not_repeating_character(string):

    string_array = [0]*26

    for a_str in string:
        a_str_asc = ord(a_str) - ord("a")
        string_array[a_str_asc] += 1

    for index_array in range(len(string_array)):
        if string_array[index_array] == 1:
            return chr(index_array + ord("a"))

    return "_"


result = find_not_repeating_character(input)
print(result)