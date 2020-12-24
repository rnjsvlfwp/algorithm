s = ")())()"


def is_correct_parenthesis(string):
    length_string = len(string)
    print(length_string)
    stack = []

    for i in range(length_string):
        if string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
