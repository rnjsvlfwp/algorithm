input = "abyyca"


def is_palindrome(string):
    string_length = len(string) // 2

    for index in range(string_length):
        if string[index] != string[-1-index]:
            return False
    else:
        return True


print(is_palindrome(input))
