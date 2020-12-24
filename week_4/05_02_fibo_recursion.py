input = 20


# 1. fibo(1) = 1
# 2. fibo(2) = 1
# 3. fibo(3) = fibo(1) + fibo(2) = 2
# 4. fibo(4) = fibo(2) + fibo(3) = 3
# 5. fibo(5) = fibo(3) + fibo(4) = 5


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765
