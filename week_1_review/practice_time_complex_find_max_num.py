input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]        # 입력 1번, 누적: 1
    for num in array:         # array 길이만큼 연산, 누적: 1 + N
        if num > max_num:     # if문 비교 1번, 누적: 1 + N*(1)
            max_num = num     # if문 입력 1번, 누적: 1 + N*(1+1)
    return max_num            # 시간 복잡도 결과: 1 + 2N

result = find_max_num(input)
print(result)