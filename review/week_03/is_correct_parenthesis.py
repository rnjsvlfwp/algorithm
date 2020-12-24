s = "(())()"


def is_correct_parenthesis(string):
    string_length = len(string)

    if string[0] == ")":
        return False

    temp_parenthesis = list()
    for index in range(string_length):
        if len(temp_parenthesis) == 0:
            temp_parenthesis.append(string[index])
        elif temp_parenthesis[len(temp_parenthesis)-1] != string[index]:
            temp_parenthesis.pop()
        elif temp_parenthesis[len(temp_parenthesis)-1] == string[index]:
            temp_parenthesis.append(string[index])

    if len(temp_parenthesis) == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))
