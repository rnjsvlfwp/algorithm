def factorial(n): # 5

    # n = 5    -> 5 * 4 * 3 * 2 * 1
    # n = 100  -> 100 * 99 * 98 * ... * 3 * 2 * 1
    # n = 1000 -> 1000 * 999 * 998 * ... * 3 * 2 * 1
    # n = n    -> n * n-1 * n-2 * ... * 3 * 2 * 1
    # 규칙
    # - 자기 자신보다 1보다 작은 수를 곱한다.
    # - n이 1이면 끝난다.

    if n == 1:
        return 1

    return n * factorial(n-1)
print(factorial(5))