seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}


def fibo(n, memoi):
    if n in memoi:
        return memoi[n]

    nth_fibo = fibo(n - 1, memoi) + fibo(n - 2, memoi)
    memoi[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    fixed_seat_array_length = len(fixed_seat_array)
    result = 1
    for index in range(fixed_seat_array_length + 1):
        if index == 0:
            seats = fixed_seat_array[index] - 1
        elif 0 < index < fixed_seat_array_length:
            seats = fixed_seat_array[index] - fixed_seat_array[index - 1] - 1
        else:
            seats = total_count - fixed_seat_array[index - 1]

        if seats == 0:
            seats = 1

        if seats not in memo:
            fibo(seats, memo)

        result *= memo[seats]
    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
