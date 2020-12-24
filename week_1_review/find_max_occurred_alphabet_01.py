input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26
    # print(alphabet_array)

    for a_string in string:
        if a_string.isalpha():
            alphabet_array[ord(a_string) - ord('a')] += 1

    max_occurred_alphabet = 0
    max_occurred_alphabet_index = 0

    for index in range(len(alphabet_array)):

        occurred_alphabet = alphabet_array[index]

        if occurred_alphabet > max_occurred_alphabet:
            max_occurred_alphabet = occurred_alphabet
            max_occurred_index = index

    return chr(ord('a') + max_occurred_index)


result = find_max_occurred_alphabet(input)
print(result)
