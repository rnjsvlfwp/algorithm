numbers = [1, 1, 1, 1, 1]
target_number = 3


def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    sum_array = sum(array)
    rest_number = sum_array - target

    numerator = factorial(sum_array)
    denominator = factorial(rest_number) * factorial(target)

    result = int(numerator / denominator)

    return result


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
