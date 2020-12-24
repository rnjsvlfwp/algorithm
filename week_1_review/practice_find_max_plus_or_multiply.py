input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    mult_sum = 0                            #1.대입 연산, 1
    for a_num in array:                     #2.array 크기만큼, N
        if a_num <=1 or mult_sum <= 1:      #2.비교연산, N(1)
            mult_sum += a_num               #2.대입연산, N(2)
        else:
            mult_sum *= a_num

    return mult_sum                          #2.시간복잡도 결과, 2N+1(=O(N))


result = find_max_plus_or_multiply(input)
print(result)
