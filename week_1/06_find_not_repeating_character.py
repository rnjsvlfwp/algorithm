input = "abacabade"


def find_not_repeating_character(string):
    space = [0] * 26

    for index in range(len(string)):
        num_to_asc = ord(string[index])
        num_of_rep = num_to_asc - ord("a")
        space[num_of_rep] += 1

    for index_space in range(len(space)):
        if space[index_space] == 1:
            temp_result = chr(index_space + ord("a"))
            return temp_result

    return "_"

result = find_not_repeating_character(input)
print(result)
