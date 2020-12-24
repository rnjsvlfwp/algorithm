input = "abcba"


def is_palindrome(string):
    if string[0] != string[-1]:         # a == a / b == b
        return False

    if len(string) <= 1:                # 5 <= 1 / 3 <= 1
        return True                     # pass   / pass

    return is_palindrome(string[1:-1])  #  is_palindrome('bcb') /  is_palindrome("c")


print(is_palindrome(input))
