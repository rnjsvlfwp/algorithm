s = "(())()"


def is_correct_parenthesis(string):
    length_s = len(string)
    dict_s = dict()

    ascii_to_hrr_s = []
    for s_index in range(length_s):
        ascii_to_hrr_s.append(ord(string[s_index]) - 40)
        ascii_to_hrr_s.sort()

    for a_num in ascii_to_hrr_s:
        if a_num not in dict_s.keys():
            dict_s[a_num] = 1
        else:
            dict_s[a_num] += 1

    number_of_numbers = list(dict_s.values())
    if number_of_numbers[0] == number_of_numbers[1]:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
