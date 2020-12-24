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
    fixed_seat_array_index = 0
    result = 1

    for a_seat_part in fixed_seat_array:
        seats = a_seat_part - 1

        if seats == fixed_seat_array_index:
            of_result = 1
        else:
            of_result = fibo(seats - fixed_seat_array_index, memo)

        result *= of_result
        fixed_seat_array_index = seats + 1

    of_result = fibo(total_count - fixed_seat_array_index, memo)
    result *= of_result

    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
