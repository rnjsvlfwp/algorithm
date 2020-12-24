input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:               # array 길이만큼 연산, 누적: N
        for compare_num in array:   # array 길이만큼 연산, 누적: N * N (for안에 for문 있으므로)
            if num < compare_num:   # 비교연산 1번, 누적: N * N * 1
                break
        else:
            return num              # 결과: N^2


result = find_max_num(input)
print(result)
