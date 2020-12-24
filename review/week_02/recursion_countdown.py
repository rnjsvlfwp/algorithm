start_num = 60


def count_down(number):
    if number < 0:
        return True

    print(number)
    count_down(number-1)



print(count_down(start_num))
