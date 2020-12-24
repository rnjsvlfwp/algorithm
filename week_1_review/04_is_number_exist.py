input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):

    for element in array:     # array 길이만큼, N
        if number == element: # 비교하기, N(1)
            return True       # 결과, N(빅오: N(=O(N)), 빅오메가:1(=오메가(1)))


result = is_number_exist(3, input)
print(result)