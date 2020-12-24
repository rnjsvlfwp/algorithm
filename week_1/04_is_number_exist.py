input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array: # array의 길이만큼
        if number == num: # 비교 연산 1번
            return True # N * 1 만큼
    else:
        return False

result = is_number_exist(3, input)
print(result)
