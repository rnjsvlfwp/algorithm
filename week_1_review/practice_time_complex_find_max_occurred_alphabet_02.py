input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_list = [0] * 26

    for char in string:                                         # 1. string 길이만큼 반복, N
        if not char.isalpha():                                  # 1. 비교, N(1)
            continue
        arr_index = ord(char) - ord('a')                        # 1. 입력, N(2)
        alphabet_occurrence_list[arr_index] += 1                # 1. 입력, N(3)

    max_occurrence = 0                                          # 2. 대입연산, 1
    max_alphabet_index = 0                                      # 2. 대입연산, 2
    for index in range(len(alphabet_occurrence_list)):          # 3. 알파벳 리스트만큼, 26
        alphabet_occurrence = alphabet_occurrence_list[index]   # 3. 대입 연산, 26(1)
        if alphabet_occurrence > max_occurrence:                # 3. 비교 연산, 26(2)
            max_occurrence = alphabet_occurrence                # 3. 대입 연산, 26(3)
            max_alphabet_index = index                          # 3. 대입 연산, 26(4)
                                                                # 4. 결과: 3N + 2 + 26*4 = 3N + 106
    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)