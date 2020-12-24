input = 'abcba'


def palindrome(string):
    if string[0] != string[-1]:
        return False

    if len(string) <= 1:
        return True

    return palindrome(string[1:-1])


print(palindrome(input))
