input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for a_string in string:
        if a_string.isalpha():
            alphabet_occurrence_array[ord(a_string) - ord('a')] += 1

            print(alphabet_occurrence_array)

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    return chr(ord('a') + max_alphabet_index)


result = find_max_occurred_alphabet(input)
print(result)
