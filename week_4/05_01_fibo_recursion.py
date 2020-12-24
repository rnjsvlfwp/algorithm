input = 20


# 1. fibo(1) = 1
# 2. fibo(2) = 1
# 3. fibo(3) = fibo(1) + fibo(2) = 2
# 4. fibo(4) = fibo(2) + fibo(3) = 3
# 5. fibo(5) = fibo(3) + fibo(4) = 5


def fibo_recursion(n):
    result_array = [1, 1]
    i = 0

    while i < n - 2:
        new_result = result_array[i] + result_array[i + 1]
        result_array.append(new_result)
        i += 1
    return result_array[-1]


print(fibo_recursion(input))  # 6765
