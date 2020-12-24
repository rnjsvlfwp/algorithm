input = "abcba"


def is_palindrome(string):
    string_length = len(string)

    for index in range(string_length):
        if string[index] != string[string_length - 1 - index]:
            return False

    return True
    # string 0번째와 string 마지막이 같은지 비교한다.
    # 같으면 True, 다르면 False를 반환한다.

    # string 1번째와 string 마지막에서 두 번째가 같은지 비교한다.
    # 같으면 True, 다르면 False를 반환한다.

    # .....

    # string '길이/2'번째와 string 마지막에서 '길이/2'번째가 같은지 비교한다.
    # 같으면 True, 다르면 False를 반환한다.



print(is_palindrome(input))
