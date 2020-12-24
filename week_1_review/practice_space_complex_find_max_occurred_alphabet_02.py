input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_list = [0] * 26           #26개 공간 사용, 누적: 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')          #1개 공간 사용, 누적: 27
        alphabet_occurrence_list[arr_index] += 1

    max_occurrence = 0                            #1개 공간 사용, 누적: 28
    max_alphabet_index = 0                        #1개 공간 사용, 누적: 29
    for index in range(len(alphabet_occurrence_list)):
        alphabet_occurrence = alphabet_occurrence_list[index]   #1개 공간 사용, 누적: 30
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)